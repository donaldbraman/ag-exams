"""Temporal workflow for building criminal law final exams."""

from __future__ import annotations

import asyncio
import json
import re
from dataclasses import dataclass
from datetime import timedelta
from pathlib import PurePosixPath

from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from ag_exams.activities import (
        delete_q_file,
        dispatch_ambiguity_audit_per_q,
        dispatch_edge_case_audit_per_q,
        dispatch_architect,
        dispatch_argument_pass_per_q_opus,
        dispatch_argument_pass_per_q_sonnet,
        dispatch_blind_take,
        dispatch_critic,
        dispatch_grounding_per_q,
        dispatch_question_writer,
        extract_argument_pass_verdict,
        extract_audit_verdict,
        extract_edge_case_verdict,
        extract_grounding_verdict,
        list_q_files,
        read_existing_package,
        read_file,
        write_artifact,
        write_file,
        write_fix_guidance,
        wipe_directory,
        commit_run_to_git,
    )
    from ag_exams.coverage import CoverageTracker
    from ag_exams.models import SCENARIO_MAP, ExamConfig, ExamResult

FIX_LOOP_CAP = 5


@dataclass
class ScenarioInput:
    config: ExamConfig
    scenario_name: str
    priorities: list[str]


@dataclass
class ScenarioResult:
    name: str
    converged: bool
    rounds: int
    questions: int
    package_json: str | None


def _extract_json(text: str) -> str:
    """Extract JSON from text that may be wrapped in code fences."""
    text = text.strip()
    if text.startswith("{") or text.startswith("["):
        return text
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1:
        return text[start : end + 1]
    return text


@workflow.defn
class BuildScenarioWorkflow:
    """Orchestrates whiteboarding and QA loops for a single scenario."""

    def __init__(self) -> None:
        self._human_approved = False
        self._human_feedback: str | None = None
        self._status: dict = {"phase": "init", "round": 0}

    @workflow.signal
    async def approve_scenario(self, feedback: str = "") -> None:
        """Human signals approval to proceed past the review gate."""
        self._human_approved = True
        self._human_feedback = feedback or None

    @workflow.signal
    async def skip_review(self) -> None:
        """Skip the human review gate."""
        self._human_approved = True

    @workflow.query
    def get_status(self) -> dict:
        """Query current workflow status."""
        return self._status

    @workflow.run
    async def run(self, input: ScenarioInput) -> ScenarioResult:
        config = input.config
        scenario_name = input.scenario_name
        priorities = input.priorities

        scenario = SCENARIO_MAP.get(scenario_name)
        if not scenario:
            raise ValueError(f"Unknown scenario: {scenario_name}")

        chapters = scenario.chapters  # type: ignore[attr-defined]

        if config.reuse_whiteboard:
            self._status = {
                "phase": "reuse-whiteboard",
                "round": 0,
            }
            package_json = await workflow.execute_activity(
                read_existing_package,
                args=[config.output_dir, scenario_name],
                start_to_close_timeout=timedelta(minutes=1),
            )
            converged = True
            workflow.logger.info(
                f"Skipped whiteboarding for {scenario_name} — reused existing package"
            )
        else:
            self._status = {"phase": "whiteboarding", "round": 0}
            package_json, converged = await self._whiteboard(scenario, priorities, chapters)

            await workflow.execute_activity(
                write_artifact,
                args=[f"{config.output_dir}/{scenario_name}-scenario.md", package_json or ""],
                start_to_close_timeout=timedelta(minutes=1),
            )

        if config.dry_run:
            return ScenarioResult(
                name=scenario_name,
                converged=converged,
                rounds=self._status["round"],
                questions=0,
                package_json=package_json,
            )

        # Human review gate
        self._human_approved = False
        self._status["phase"] = "awaiting-review"
        workflow.logger.info(
            f"Scenario {scenario_name} ready for review. "
            "Send 'approve_scenario' signal to continue."
        )
        await workflow.wait_condition(lambda: self._human_approved)

        questions_text = await self._write_and_verify(config, scenario, package_json)

        await workflow.execute_activity(
            write_artifact,
            args=[f"{config.output_dir}/{scenario_name}-questions.md", questions_text],
            start_to_close_timeout=timedelta(minutes=1),
        )

        # Auto-commit to Git at the very end
        git_result = await workflow.execute_activity(
            commit_run_to_git,
            args=[config.output_dir, scenario_name],
            start_to_close_timeout=timedelta(minutes=1),
        )
        workflow.logger.info(f"Git auto-commit result: {git_result}")

        return ScenarioResult(
            name=scenario_name,
            converged=converged,
            rounds=self._status["round"],
            questions=questions_text.count("**Q"),
            package_json=package_json,
        )

    async def _whiteboard(
        self,
        scenario: object,
        priorities: list[str],
        chapters: list[int],
    ) -> tuple[str | None, bool]:
        """Run architect/critic rounds until convergence or max rounds."""
        package_json: str | None = None
        critique_json: str | None = None
        retry_policy = RetryPolicy(maximum_attempts=2, initial_interval=timedelta(seconds=10))

        for round_num in range(1, 11):
            self._status["round"] = round_num

            if round_num % 2 == 1:
                package_json = await workflow.execute_activity(
                    dispatch_architect,
                    args=[
                        scenario.brief_text,  # type: ignore[attr-defined]
                        priorities,
                        chapters,
                        critique_json,
                        package_json,
                        round_num,
                    ],
                    start_to_close_timeout=timedelta(minutes=20),
                    retry_policy=retry_policy,
                )
                workflow.logger.info(f"Architect round {round_num} complete")
            else:
                critique_json = await workflow.execute_activity(
                    dispatch_critic,
                    args=[package_json or "", priorities, chapters, round_num],
                    start_to_close_timeout=timedelta(minutes=15),
                    retry_policy=retry_policy,
                )
                workflow.logger.info(f"Critic round {round_num} complete")

                converged, package_json = self._check_convergence(
                    critique_json, package_json, round_num
                )
                if converged:
                    return package_json, True

        workflow.logger.warning("Scenario did not converge in 10 rounds, using last package")
        return package_json, False

    def _check_convergence(
        self,
        critique_json: str,
        package_json: str | None,
        round_num: int,
    ) -> tuple[bool, str | None]:
        """Check convergence and apply critic diffs to the package."""
        try:
            critique = json.loads(_extract_json(critique_json))
            package_json = self._apply_critic_diffs(package_json, critique)
            if critique.get("status") == "CONVERGED":
                workflow.logger.info(f"Converged at round {round_num}")
                return True, package_json
        except (json.JSONDecodeError, KeyError) as e:
            workflow.logger.warning(f"Could not parse critic round {round_num}: {e}")
        return False, package_json

    @staticmethod
    def _apply_critic_diffs(package_json: str | None, critique: dict) -> str:
        """Merge critic diffs into the scenario package (deterministic Python)."""
        try:
            package = json.loads(_extract_json(package_json or "{}"))
        except json.JSONDecodeError:
            return package_json or "{}"

        # Apply fact revisions (key = index, value = new text)
        revised_facts = critique.get("revised_facts", {})
        facts = package.get("facts", [])
        for idx_str, new_text in revised_facts.items():
            idx = int(idx_str)
            if 0 <= idx < len(facts):
                facts[idx] = new_text
        package["facts"] = facts

        # Append new facts
        new_facts = critique.get("new_facts", [])
        if new_facts:
            package["facts"].extend(new_facts)

        # Update stub statuses
        stubs = package.get("stubs", [])
        
        raw_accepted = critique.get("accepted_stubs", [])
        accepted = set()
        for a in raw_accepted:
            if isinstance(a, dict) and "id" in a:
                accepted.add(a["id"])
            elif isinstance(a, str):
                accepted.add(a)
                
        raw_rejected = critique.get("rejected_stubs", [])
        rejected_ids = set()
        for r in raw_rejected:
            if isinstance(r, dict) and "id" in r:
                rejected_ids.add(r["id"])
            elif isinstance(r, str):
                rejected_ids.add(r)

        for stub in stubs:
            sid = stub.get("id", "")
            if sid in accepted:
                stub["status"] = "accepted"
            elif sid in rejected_ids:
                stub["status"] = "rejected"

        # Add proposed stubs
        proposed = critique.get("proposed_stubs", [])
        if proposed:
            stubs.extend(proposed)

        # Remove rejected stubs
        package["stubs"] = [s for s in stubs if s.get("status") != "rejected"]

        # Update confidence
        if "confidence" in critique:
            package["critic_confidence"] = critique["confidence"]

        return json.dumps(package)

    async def _write_and_verify(
        self,
        config: ExamConfig,
        scenario: object,
        package_json: str | None,
    ) -> str:
        """Write questions, then run per-Q QA fix loop (grounding, audit, dual argument-pass).

        Loop caps at FIX_LOOP_CAP iterations with early-stop on non-decreasing flag count.
        Any MUST/SHOULD flag from audit or either argument-pass triggers regeneration;
        GROUNDING-FAIL also triggers regeneration. Convergence = all checks CLEAN/GROUNDED.
        """
        writer_retry = RetryPolicy(maximum_attempts=2, initial_interval=timedelta(seconds=10))
        qa_retry = RetryPolicy(maximum_attempts=4, initial_interval=timedelta(seconds=5))
        chapters: list[int] = scenario.chapters  # type: ignore[attr-defined]
        scenario_name: str = scenario.name  # type: ignore[attr-defined]
        questions_dir = f"{config.output_dir}/{scenario_name}-questions"

        # Auto-wipe questions dir before initial writer invocation
        await workflow.execute_activity(
            wipe_directory,
            args=[questions_dir],
            start_to_close_timeout=timedelta(seconds=30),
        )

        # Initial writer invocation
        self._status["phase"] = "question-writing"
        await workflow.execute_activity(
            dispatch_question_writer,
            args=[
                package_json or "",
                chapters,
                scenario.statutes,  # type: ignore[attr-defined]
                config.output_dir,
                scenario_name,
            ],
            start_to_close_timeout=timedelta(minutes=35),
            retry_policy=writer_retry,
        )

        # Fix loop
        prev_flag_count: int | None = None
        iteration_reached = 0
        final_per_q_results: list[dict] = []
        flagged_final: list[dict] = []

        for iteration in range(1, FIX_LOOP_CAP + 1):
            iteration_reached = iteration
            self._status["phase"] = f"qa-iteration-{iteration}"

            # Read all current q files
            q_paths = await workflow.execute_activity(
                list_q_files,
                args=[questions_dir],
                start_to_close_timeout=timedelta(seconds=30),
                retry_policy=qa_retry,
            )
            if not q_paths:
                workflow.logger.warning("no Q files found — writer may have failed")
                break

            q_texts = await asyncio.gather(
                *[
                    workflow.execute_activity(
                        read_file,
                        args=[p],
                        start_to_close_timeout=timedelta(seconds=30),
                        retry_policy=qa_retry,
                    )
                    for p in q_paths
                ]
            )

            # Fan out 4 QA activities per Q, all in parallel
            qa_tasks: list = []
            for q_text in q_texts:
                qa_tasks.append(
                    workflow.execute_activity(
                        dispatch_grounding_per_q,
                        args=[q_text],
                        start_to_close_timeout=timedelta(minutes=6),
                        retry_policy=qa_retry,
                    )
                )
                qa_tasks.append(
                    workflow.execute_activity(
                        dispatch_ambiguity_audit_per_q,
                        args=[q_text],
                        start_to_close_timeout=timedelta(minutes=12),
                        retry_policy=qa_retry,
                    )
                )
                qa_tasks.append(
                    workflow.execute_activity(
                        dispatch_edge_case_audit_per_q,
                        args=[q_text, package_json or ""],
                        start_to_close_timeout=timedelta(minutes=12),
                        retry_policy=qa_retry,
                    )
                )
                qa_tasks.append(
                    workflow.execute_activity(
                        dispatch_argument_pass_per_q_sonnet,
                        args=[q_text],
                        start_to_close_timeout=timedelta(minutes=12),
                        retry_policy=qa_retry,
                    )
                )
                qa_tasks.append(
                    workflow.execute_activity(
                        dispatch_argument_pass_per_q_opus,
                        args=[q_text],
                        start_to_close_timeout=timedelta(minutes=12),
                        retry_policy=qa_retry,
                    )
                )

            results = await asyncio.gather(*qa_tasks)

            # Group by Q (5 results per Q, in order)
            per_q_results = []
            for i, q_path in enumerate(q_paths):
                base = i * 5
                per_q_results.append(
                    {
                        "path": q_path,
                        "q_text": q_texts[i],
                        "grounding": results[base],
                        "audit": results[base + 1],
                        "edge_case": results[base + 2],
                        "argpass_sonnet": results[base + 3],
                        "argpass_opus": results[base + 4],
                    }
                )
            final_per_q_results = per_q_results

            # Persist per-Q QA artifacts to disk
            persist_tasks = []
            for pr in per_q_results:
                q_stem = PurePosixPath(pr["path"]).stem  # "q01"
                q_dir = str(PurePosixPath(pr["path"]).parent)
                for suffix, content in [
                    ("grounded", pr["grounding"]),
                    ("audit", pr["audit"]),
                    ("edge-case", pr["edge_case"]),
                    ("argpass-sonnet", pr["argpass_sonnet"]),
                    ("argpass-opus", pr["argpass_opus"]),
                ]:
                    persist_tasks.append(
                        workflow.execute_activity(
                            write_file,
                            args=[f"{q_dir}/{q_stem}-{suffix}.md", content],
                            start_to_close_timeout=timedelta(seconds=30),
                            retry_policy=qa_retry,
                        )
                    )
            await asyncio.gather(*persist_tasks)

            # Flag set — union across all 4 checks
            flagged = []
            for pr in per_q_results:
                reasons = []
                g = extract_grounding_verdict(pr["grounding"])
                if g == "GROUNDING-FAIL":
                    reasons.append(("grounding", pr["grounding"]))
                a = extract_audit_verdict(pr["audit"])
                if a in ("MUST FIX", "SHOULD FIX"):
                    reasons.append(("audit", pr["audit"]))
                e = extract_edge_case_verdict(pr["edge_case"])
                if e in ("MUST FIX", "SHOULD FIX"):
                    reasons.append(("edge-case", pr["edge_case"]))
                s = extract_argument_pass_verdict(pr["argpass_sonnet"])
                if s in ("MUST FIX", "SHOULD FIX"):
                    reasons.append(("argpass-sonnet", pr["argpass_sonnet"]))
                o = extract_argument_pass_verdict(pr["argpass_opus"])
                if o in ("MUST FIX", "SHOULD FIX"):
                    reasons.append(("argpass-opus", pr["argpass_opus"]))
                if reasons:
                    flagged.append({**pr, "reasons": reasons})
            flagged_final = flagged

            workflow.logger.info(f"iter {iteration}: {len(flagged)}/{len(per_q_results)} flagged")

            # Convergence
            if not flagged:
                workflow.logger.info(f"converged at iteration {iteration}")
                break

            # Early-stop: flag count didn't decrease
            if prev_flag_count is not None and len(flagged) >= prev_flag_count:
                workflow.logger.warning(
                    f"no progress on iteration {iteration} "
                    f"({len(flagged)} >= {prev_flag_count}); escalating"
                )
                break
            prev_flag_count = len(flagged)

            # If this was the last iteration, don't regenerate
            if iteration == FIX_LOOP_CAP:
                workflow.logger.warning(f"cap exhausted with {len(flagged)} flagged Qs")
                break

            # Write fix-guidance + delete flagged q files, then re-run writer
            fix_tasks = []
            for pr in flagged:
                q_stem = PurePosixPath(pr["path"]).stem  # "q01"
                q_dir = str(PurePosixPath(pr["path"]).parent)
                guidance_path = f"{q_dir}/{q_stem}-fix-guidance.md"
                guidance = self._build_fix_guidance(q_stem, pr["reasons"])
                fix_tasks.append(
                    workflow.execute_activity(
                        write_fix_guidance,
                        args=[guidance_path, guidance],
                        start_to_close_timeout=timedelta(seconds=30),
                        retry_policy=qa_retry,
                    )
                )
                fix_tasks.append(
                    workflow.execute_activity(
                        delete_q_file,
                        args=[pr["path"]],
                        start_to_close_timeout=timedelta(seconds=30),
                        retry_policy=qa_retry,
                    )
                )
            await asyncio.gather(*fix_tasks)

            # Re-run writer; Option A resumption regenerates deleted Qs using guidance
            self._status["phase"] = f"writer-regeneration-{iteration}"
            await workflow.execute_activity(
                dispatch_question_writer,
                args=[
                    package_json or "",
                    chapters,
                    scenario.statutes,  # type: ignore[attr-defined]
                    config.output_dir,
                    scenario_name,
                ],
                start_to_close_timeout=timedelta(minutes=35),
                retry_policy=writer_retry,
            )

        # Blind-take (handicapped Haiku floor check) on final Qs
        self._status["phase"] = "blind-take"
        stripped_text = self._strip_for_blind_take(final_per_q_results)
        blind_result = await workflow.execute_activity(
            dispatch_blind_take,
            args=[stripped_text],
            start_to_close_timeout=timedelta(minutes=4),
            retry_policy=qa_retry,
        )

        # Review summary
        summary = self._build_review_summary(
            scenario_name,
            iteration_reached,
            final_per_q_results,
            flagged_final,
            blind_result,
        )
        await workflow.execute_activity(
            write_file,
            args=[f"{config.output_dir}/{scenario_name}-review-summary.md", summary],
            start_to_close_timeout=timedelta(seconds=30),
            retry_policy=qa_retry,
        )

        # Assemble final concatenated questions text
        q_texts_final = [pr["q_text"] for pr in final_per_q_results]
        return "\n\n---\n\n".join(q_texts_final)

    @staticmethod
    def _build_fix_guidance(q_stem: str, reasons: list[tuple[str, str]]) -> str:
        """Compose a fix-guidance markdown file from the QA findings for one Q.

        Writer reads this on next iteration and addresses each numbered issue.
        """
        lines = [
            f"# Fix Guidance for {q_stem}",
            "",
            f"The QA pipeline flagged this question. Rewrite `{q_stem}.md` addressing each "
            "numbered issue below. Do NOT delete this guidance file — the pipeline handles it.",
            "",
        ]
        for i, (source, content) in enumerate(reasons, start=1):
            lines.append(f"## Issue {i} — {source}")
            lines.append("")
            # Include the full QA block so writer sees the reasoning
            lines.append(content.strip())
            lines.append("")
        return "\n".join(lines)

    @staticmethod
    def _strip_for_blind_take(per_q_results: list[dict]) -> str:
        """Strip answers / correct markers / explanations / tags for Haiku blind-take.

        Output contains only stem + 5 options per Q.
        """
        parts = []
        for pr in per_q_results:
            q_text = pr["q_text"]
            # Remove <!-- correct --> markers
            stripped = re.sub(r"\s*<!--\s*correct\s*-->", "", q_text)
            # Remove everything from **Answer:** onward
            stripped = re.split(r"\n\*\*Answer:\*\*", stripped, maxsplit=1)[0]
            # Remove any trailing QA comment blocks that may have leaked in
            stripped = re.sub(r"<!--.*?-->", "", stripped, flags=re.DOTALL).strip()
            parts.append(stripped)
        return "\n\n---\n\n".join(parts)

    @staticmethod
    def _build_review_summary(
        scenario_name: str,
        iteration_reached: int,
        per_q_results: list[dict],
        flagged: list[dict],
        blind_result: str,
    ) -> str:
        """Build the human-readable review summary for this scenario."""
        converged = not flagged
        lines = [
            f"# Review Summary — {scenario_name}",
            "",
            f"**Iterations:** {iteration_reached} of {FIX_LOOP_CAP}",
            f"**Converged:** {'yes' if converged else 'NO — cap exhausted or early-stop'}",
            f"**Total Qs:** {len(per_q_results)}",
            f"**Flagged at end:** {len(flagged)}",
            "",
        ]

        # Per-Q verdicts table
        lines.append("## Per-Q Verdicts")
        lines.append("")
        lines.append("| Q | Grounding | Audit | Edge Case | Sonnet argpass | Opus argpass |")
        lines.append("|---|---|---|---|---|---|")
        for pr in per_q_results:
            q_stem = PurePosixPath(pr["path"]).stem
            g = extract_grounding_verdict(pr["grounding"])
            a = extract_audit_verdict(pr["audit"])
            e = extract_edge_case_verdict(pr["edge_case"])
            s = extract_argument_pass_verdict(pr["argpass_sonnet"])
            o = extract_argument_pass_verdict(pr["argpass_opus"])
            lines.append(f"| {q_stem} | {g} | {a} | {e} | {s} | {o} |")
        lines.append("")

        # Flagged items needing professor review
        if flagged:
            lines.append("## Flagged Qs (needs professor review)")
            lines.append("")
            for pr in flagged:
                q_stem = PurePosixPath(pr["path"]).stem
                lines.append(f"### {q_stem}")
                for source, _ in pr["reasons"]:
                    lines.append(f"- Flagged by: **{source}**")
                lines.append(
                    f"- Full QA artifacts: `{q_stem}-grounded.md`, "
                    f"`{q_stem}-audit.md`, `{q_stem}-edge-case.md`, "
                    f"`{q_stem}-argpass-sonnet.md`, "
                    f"`{q_stem}-argpass-opus.md`"
                )
                lines.append("")

        # Blind-take result
        lines.append("## Handicapped-Haiku Blind-Take (floor check)")
        lines.append("")
        lines.append("```")
        lines.append(blind_result.strip())
        lines.append("```")
        lines.append("")
        lines.append(
            "Interpretation: Haiku (effort=low, no tools, single turn) should "
            "score in the 50-75% range on a well-calibrated exam. Scores above "
            "85% suggest Qs may be too easy; scores below 40% suggest unfair or "
            "overly-subtle phrasing."
        )
        return "\n".join(lines)


@workflow.defn
class BuildFinalExam:
    """Orchestrates the multi-scenario exam generation pipeline."""

    def __init__(self) -> None:
        self._status: dict = {"phase": "init"}

    @workflow.query
    def get_status(self) -> dict:
        """Query current workflow status."""
        return self._status

    @workflow.run
    async def run(self, config: ExamConfig) -> ExamResult:
        self._status = {"phase": "dispatching-scenarios"}

        tracker = (
            CoverageTracker.from_json(config.tracker_state)
            if config.tracker_state
            else CoverageTracker(self._default_weights())
        )

        scenario_names = (
            list(SCENARIO_MAP.keys()) if "all" in config.scenarios else config.scenarios
        )

        inputs: list[ScenarioInput] = []
        for scenario_name in scenario_names:
            if scenario_name in config.completed_scenarios:
                continue

            priorities = tracker.next_priorities(15)
            inputs.append(ScenarioInput(config, scenario_name, priorities))

        child_tasks = []
        for inp in inputs:
            child_tasks.append(
                workflow.execute_child_workflow(
                    BuildScenarioWorkflow.run,
                    inp,
                    id=f"build-scenario-{inp.scenario_name}-{workflow.info().run_id}",
                )
            )

        results: list[ScenarioResult] = await asyncio.gather(*child_tasks)

        # Merge actual coverage back into tracker
        for result in results:
            self._update_coverage(tracker, result.package_json)

        # Phase 3: Assembly
        self._status = {"phase": "assembly"}
        report = tracker.coverage_report()
        gaps = tracker.uncovered_doctrines(min_weight=3)

        return ExamResult(
            exam_file=f"{config.output_dir}/exam-final.md",
            total_questions=sum(r.questions for r in results),
            scenarios_completed=[r.name for r in results],
            coverage_report=report,
            gaps=gaps,
        )

    def _update_coverage(self, tracker: CoverageTracker, package_json: str | None) -> None:
        """Extract doctrines from package and record coverage."""
        try:
            pkg = json.loads(_extract_json(package_json or "{}"))
            for doctrine in pkg.get("doctrines_covered", []):
                if doctrine in tracker.static_weight:
                    tracker.record_coverage(doctrine)
        except (json.JSONDecodeError, KeyError):
            pass

    @staticmethod
    def _default_weights() -> dict[str, int]:
        """Default doctrine weights (estimated, replace with inventory-derived)."""
        return {
            "possession-distribution": 8,
            "constructive-possession": 5,
            "accomplice-purpose-vs-knowledge": 7,
            "conspiracy-agreement": 8,
            "pinkerton-liability": 7,
            "rico-enterprise": 6,
            "rico-conspiracy": 5,
            "attempt-proximity": 6,
            "attempt-substantial-step": 6,
            "duress": 5,
            "necessity": 4,
            "mistake-of-fact": 5,
            "mistake-of-law": 4,
            "strict-liability": 4,
            "public-welfare-offense": 4,
            "felony-murder": 6,
            "homicide-grading": 7,
            "provocation-ehr": 5,
            "self-defense": 6,
            "causation": 5,
            "omission-liability": 4,
            "voluntary-act": 3,
            "mens-rea-hierarchy": 6,
            "statutory-interpretation": 4,
            "prosecutorial-discretion": 3,
            "punishment-theory": 3,
            "procedural-justice": 3,
            "motivated-cognition": 3,
            "abandonment-renunciation": 4,
            "conspiracy-withdrawal": 5,
            "conspiracy-scope-kotteakos": 5,
        }
