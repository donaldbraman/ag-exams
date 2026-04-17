"""Temporal activities for exam generation pipeline."""

from __future__ import annotations

import asyncio
import json
import re
from pathlib import Path

from temporalio import activity

REPO_ROOT = Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------------------
# Per-Q file helpers (glob patterns, format validators, verdict extractors)
# ---------------------------------------------------------------------------

Q_FILE_RE = re.compile(
    r"^q(\d{2})\.md$"
)  # q01.md .. q99.md (excludes fix-guidance, -grounded, etc.)


def glob_q_files(questions_dir: Path) -> list[Path]:
    """List canonical per-Q files under questions_dir, sorted by number.

    Matches only q<NN>.md (not q<NN>-fix-guidance.md, not q<NN>-grounded.md).
    """
    return sorted(p for p in questions_dir.glob("q*.md") if Q_FILE_RE.match(p.name))


def validate_q_file(path: Path) -> list[str]:
    """Structural validator for a single qNN.md file.

    Returns a list of violation strings. Empty list = valid.
    """
    text = path.read_text()
    violations: list[str] = []

    # Strip Self-check HTML comments before option extraction
    stripped = re.sub(r"<!--\s*Self-check:.*?-->", "", text, flags=re.DOTALL)

    # Q header
    if not re.search(r"^\*\*Q\d+\.\*\*\s", stripped, re.MULTILINE):
        violations.append("missing Q header `**Q<N>.**`")

    # Options: expect exactly 5 lines starting with (a)..(e)
    option_lines: dict[str, str] = {}
    for m in re.finditer(r"^\(([a-e])\)\s+(.+)$", stripped, re.MULTILINE):
        option_lines[m.group(1)] = m.group(2)
    if len(option_lines) != 5:
        violations.append(
            f"expected 5 options (a-e), found {len(option_lines)}: {sorted(option_lines.keys())}"
        )

    # Exactly one <!-- correct --> marker
    correct_markers = list(re.finditer(r"<!--\s*correct\s*-->", stripped))
    if len(correct_markers) != 1:
        violations.append(
            f"expected exactly 1 `<!-- correct -->` marker, found {len(correct_markers)}"
        )

    # Answer line
    ans_m = re.search(r"\*\*Answer:\*\*\s*\(([a-e])\)", stripped)
    if not ans_m:
        violations.append("missing or malformed `**Answer:** (<letter>)` line")
    elif correct_markers:
        # Verify Answer letter matches the <!-- correct --> option
        correct_line = next(
            (line for line in stripped.splitlines() if "<!-- correct -->" in line),
            "",
        )
        correct_option_m = re.match(r"^\(([a-e])\)", correct_line)
        if correct_option_m and correct_option_m.group(1) != ans_m.group(1):
            violations.append(
                f"Answer letter ({ans_m.group(1)}) does not match `<!-- correct -->` option ({correct_option_m.group(1)})"
            )

    # Required blocks
    violations.extend(
        f"missing `{required}` block"
        for required in ("**Explanation:**", "**Tags:**", "**Grounding:**")
        if required not in stripped
    )

    return violations


def extract_grounding_verdict(q_text: str) -> str:
    """Return 'GROUNDED' | 'GROUNDED-WITH-CAVEAT' | 'GROUNDING-FAIL' | 'MISSING'.

    Parses the comment block appended by build_grounding_per_q_prompt.
    """
    if re.search(r"<!--\s*GROUNDING-FAIL", q_text):
        return "GROUNDING-FAIL"
    if re.search(r"<!--\s*grounding:\s*GROUNDED-WITH-CAVEAT", q_text):
        return "GROUNDED-WITH-CAVEAT"
    if re.search(r"<!--\s*grounding:\s*GROUNDED", q_text):
        return "GROUNDED"
    return "MISSING"


def extract_audit_verdict(q_text: str) -> str:
    """Return 'CLEAN' | 'SHOULD FIX' | 'MUST FIX' | 'MISSING'."""
    m = re.search(r"<!--\s*audit:\s*(MUST FIX|SHOULD FIX|CLEAN)", q_text)
    return m.group(1) if m else "MISSING"


def extract_edge_case_verdict(q_text: str) -> str:
    """Return 'CLEAN' | 'SHOULD FIX' | 'MUST FIX' | 'MISSING'."""
    m = re.search(r"<!--\s*edge-case-audit:\s*(MUST FIX|SHOULD FIX|CLEAN)", q_text)
    return m.group(1) if m else "MISSING"


def extract_argument_pass_verdict(q_text: str) -> str:
    """Return 'CLEAN' | 'SHOULD FIX' | 'MUST FIX' | 'MISSING'."""
    m = re.search(r"<!--\s*argument-pass:\s*(MUST FIX|SHOULD FIX|CLEAN)", q_text)
    return m.group(1) if m else "MISSING"


def is_q_flagged(q_text: str) -> tuple[bool, list[str]]:
    """Return (flagged, reasons) based on grounding + audit + argument-pass verdicts.

    A Q is flagged if any check returns MUST FIX, SHOULD FIX, or GROUNDING-FAIL.
    GROUNDED-WITH-CAVEAT is a note but not a flag (caveat, not fix).
    """
    reasons = []
    grounding = extract_grounding_verdict(q_text)
    if grounding == "GROUNDING-FAIL":
        reasons.append(f"grounding: {grounding}")
    audit = extract_audit_verdict(q_text)
    if audit in ("MUST FIX", "SHOULD FIX"):
        reasons.append(f"audit: {audit}")
    edge_case = extract_edge_case_verdict(q_text)
    if edge_case in ("MUST FIX", "SHOULD FIX"):
        reasons.append(f"edge-case: {edge_case}")
    argpass = extract_argument_pass_verdict(q_text)
    if argpass in ("MUST FIX", "SHOULD FIX"):
        reasons.append(f"argument-pass: {argpass}")
    return (bool(reasons), reasons)


from ag_exams.gemini_client import dispatch_gemini

def _extract_json(text: str) -> str:
    """Extract JSON from text that may be wrapped in code fences or LLM output."""
    text = text.strip()
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if match:
        text = match.group(1).strip()
    
    # Find outermost matching braces or brackets
    obj_start = text.find("{")
    obj_end = text.rfind("}")
    arr_start = text.find("[")
    arr_end = text.rfind("]")
    
    if obj_start != -1 and obj_end != -1 and (arr_start == -1 or obj_start < arr_start):
        return text[obj_start : obj_end + 1]
    elif arr_start != -1 and arr_end != -1:
        return text[arr_start : arr_end + 1]
    return text


@activity.defn
async def dispatch_architect(
    scenario_brief: str,
    coverage_priorities: list[str],
    chapters: list[int],
    prior_critique: str | None,
    current_package: str | None,
    round_number: int,
) -> str:
    """Dispatch the exam-architect agent for one whiteboarding round."""
    from ag_exams.prompts import build_architect_prompt, build_architect_extractor_prompt

    prompt = build_architect_prompt(
        scenario_brief,
        coverage_priorities,
        chapters,
        prior_critique,
        current_package,
        round_number,
    )
    from ag_exams.model_config import get_stage_config

    cfg = get_stage_config("architect")
    
    # Step 1: Deep Reasoning (Markdown)
    reasoning_md = await dispatch_gemini(
        prompt,
        model=cfg.model,
        use_diskcache=cfg.cache,
        response_mime_type="text/plain",
    )
    
    # Step 2: JSON Extraction (Flash)
    extractor_prompt = build_architect_extractor_prompt(reasoning_md)
    result_json = await dispatch_gemini(
        extractor_prompt,
        model="gemini-3.0-flash-preview",
        use_diskcache=False,
        response_mime_type="application/json",
    )
    
    # Validate JSON structure
    try:
        data = json.loads(_extract_json(result_json))
        if "facts" not in data or "stubs" not in data:
            msg = "Missing required fields: facts, stubs"
            raise ValueError(msg)
    except (json.JSONDecodeError, ValueError) as e:
        activity.logger.warning("Architect output validation failed: %s", e)
        # Return raw -- workflow can handle
    return result_json


@activity.defn
async def dispatch_critic(
    current_package: str,
    coverage_priorities: list[str],
    chapters: list[int],
    round_number: int,
) -> str:
    """Dispatch the exam-critic agent for one whiteboarding round."""
    from ag_exams.prompts import build_critic_prompt, build_critic_extractor_prompt

    prompt = build_critic_prompt(
        current_package,
        coverage_priorities,
        chapters,
        round_number,
    )
    from ag_exams.model_config import get_stage_config

    cfg = get_stage_config("critic")
    
    # Step 1: Deep Reasoning (Markdown)
    reasoning_md = await dispatch_gemini(
        prompt,
        model=cfg.model,
        use_diskcache=cfg.cache,
        response_mime_type="text/plain",
    )
    
    # Step 2: JSON Extraction (Flash)
    extractor_prompt = build_critic_extractor_prompt(reasoning_md)
    result_json = await dispatch_gemini(
        extractor_prompt,
        model="gemini-3.0-flash-preview",
        use_diskcache=False,
        response_mime_type="application/json",
    )
    
    # Check for convergence signal
    try:
        data = json.loads(_extract_json(result_json))
        status = data.get("status", "ITERATE")
        activity.logger.info("Critic round %d status: %s", round_number, status)
    except json.JSONDecodeError:
        activity.logger.warning("Could not parse critic JSON output")
    return result_json


@activity.defn
async def dispatch_question_writer(
    scenario_package: str,
    chapters: list[int],
    statutes: str,
    output_dir: str,
    scenario_name: str,
) -> str:
    """Dispatch the question writer using the resumable one-file-per-Q pattern.

    Writer emits each question as its own markdown file under
    {output_dir}/{scenario_name}-questions/qNN.md. On retry, it globs existing
    files and resumes from the first missing index — so timeouts don't waste
    completed work.

    After the subprocess completes (or Temporal times out the activity and
    retries), this function reads all qNN.md files + header.md from disk,
    concatenates them in order, and returns the merged markdown.
    """
    from ag_exams.prompts import build_question_writer_prompt

    questions_dir = Path(output_dir) / f"{scenario_name}-questions"
    questions_dir.mkdir(parents=True, exist_ok=True)
    header_path = questions_dir / "header.md"

    system_instruction, prompt = build_question_writer_prompt(
        scenario_package,
        chapters,
        statutes,
        str(questions_dir),
        str(header_path),
    )

    # Dispatch with Write tool enabled. Any retry will see the files already
    # on disk and resume from the first missing Q.
    from ag_exams.model_config import get_stage_config

    cfg = get_stage_config("question_writer")
    try:
        result_text = await dispatch_gemini(
            prompt,
            system_instruction=system_instruction,
            model=cfg.model,
            use_diskcache=cfg.cache,
            response_mime_type="text/plain",
        )
        
        # Parse the Markdown output using regex
        file_blocks = re.split(r"---FILE:\s*(.+?)\s*---", result_text)
        for i in range(1, len(file_blocks), 2):
            filename = file_blocks[i].strip()
            content = file_blocks[i+1].strip()
            if filename == "header.md":
                header_path.write_text(content)
            elif filename.startswith("q") and filename.endswith(".md"):
                q_file = questions_dir / filename
                q_file.write_text(content)
                
    except Exception as e:
        activity.logger.warning(f"question-writer failed: {e}")
        raise  # Let Temporal retry

    # Run structural validator per q file. Delete any that fail — Option A's
    # resumption will regenerate them on the next writer invocation.
    q_files = glob_q_files(questions_dir)
    invalid: list[tuple[Path, list[str]]] = []
    for qf in q_files:
        violations = validate_q_file(qf)
        if violations:
            invalid.append((qf, violations))
    if invalid:
        for qf, violations in invalid:
            activity.logger.warning(
                "writer-validator deleting invalid %s: %s",
                qf.name,
                "; ".join(violations),
            )
            qf.unlink()
        # Re-list after deletions
        q_files = glob_q_files(questions_dir)

    # Concatenate header + valid per-Q files in order.
    header_text = header_path.read_text() if header_path.exists() else ""
    parts = [header_text] if header_text else []
    parts.extend(qf.read_text() for qf in q_files)
    return "\n\n---\n\n".join(parts)


@activity.defn
async def dispatch_grounding(
    questions_text: str,
    chapter_paths: list[str],
) -> str:
    """Dispatch the grounding verifier."""
    from ag_exams.prompts import build_grounding_prompt

    prompt = build_grounding_prompt(questions_text, chapter_paths)
    return await dispatch_gemini(prompt)


@activity.defn
async def dispatch_adversarial(stripped_questions: str) -> str:
    """Dispatch the adversarial test-taker."""
    from ag_exams.prompts import build_adversarial_prompt

    prompt = build_adversarial_prompt(stripped_questions)
    return await dispatch_gemini(prompt)


@activity.defn
async def dispatch_ambiguity_audit(
    questions_text: str,
    chapter_paths: list[str],
) -> str:
    """Dispatch the ambiguity auditor to check answer defensibility.

    Uses Opus with high effort to ensure thorough doctrinal analysis.
    Returns the structured audit report text.
    """
    from ag_exams.prompts import build_ambiguity_audit_prompt

    prompt = build_ambiguity_audit_prompt(questions_text, chapter_paths)
    return await dispatch_gemini(
        prompt,
        model="gemini-3.1-pro", # Highest effort model equivalent to Opus
    )


@activity.defn
async def write_artifact(path: str, content: str) -> str:
    """Write an artifact file. Idempotent."""
    full_path = REPO_ROOT / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content)
    return str(full_path)


@activity.defn
async def read_existing_package(output_dir: str, scenario_name: str) -> str:
    """Read an existing scenario package from disk.

    Used when ExamConfig.reuse_whiteboard=True to skip the architect/critic
    loop and proceed directly to the writer with a previously-generated
    scenario package. Returns the file contents (expected to be the JSON
    package text the critic emitted on convergence).

    Raises FileNotFoundError if the expected file doesn't exist — this is
    a correctable error; the caller should catch it and fall through to
    running the whiteboard loop.
    """
    full_path = REPO_ROOT / output_dir / f"{scenario_name}-scenario.md"
    if not full_path.exists():
        raise FileNotFoundError(f"reuse_whiteboard=True but no existing package at {full_path}")
    return full_path.read_text()


# ---------------------------------------------------------------------------
# Per-Q QA activities (maps-as-authority, severity-tagged output)
# ---------------------------------------------------------------------------


@activity.defn
async def dispatch_grounding_per_q(q_text: str) -> str:
    """Grounding verification for one Q against the full chapter-map corpus.

    The agent starts with the meta-map and Greps for the doctrine — no
    preloaded focus maps, no reliance on the Q's chapter tags.
    """
    from ag_exams.model_config import get_stage_config
    from ag_exams.prompts import build_grounding_per_q_prompt

    cfg = get_stage_config("grounding_per_q")
    prompt = build_grounding_per_q_prompt(q_text)
    return await dispatch_gemini(
        prompt,
        model=cfg.model,
        use_diskcache=cfg.cache,
    )


@activity.defn
async def dispatch_ambiguity_audit_per_q(q_text: str) -> str:
    """7-check ambiguity audit on one Q. Opus high effort for sharpest pass.

    Like grounding, this uses progressive disclosure via the meta-map —
    no preloaded focus maps, no trust of the Q's chapter tags.
    """
    from ag_exams.model_config import get_stage_config
    from ag_exams.prompts import build_ambiguity_audit_per_q_prompt

    cfg = get_stage_config("ambiguity_audit_per_q")
    prompt = build_ambiguity_audit_per_q_prompt(q_text)
    return await dispatch_gemini(
        prompt,
        model=cfg.model,
        use_diskcache=cfg.cache,
    )


@activity.defn
async def dispatch_edge_case_audit_per_q(q_text: str, scenario_package: str) -> str:
    """3-check Edge-Case audit on one Q. Checks for booby traps and cross-Q spoilers."""
    from ag_exams.model_config import get_stage_config
    from ag_exams.prompts import build_edge_case_audit_per_q_prompt

    cfg = get_stage_config("edge_case_audit_per_q")
    prompt = build_edge_case_audit_per_q_prompt(q_text, scenario_package)
    return await dispatch_gemini(
        prompt,
        model=cfg.model,
        use_diskcache=cfg.cache,
    )


@activity.defn
async def dispatch_argument_pass_per_q_sonnet(q_text: str) -> str:
    """5-per-option argument pass on one Q. Config stage: argument_pass_sonnet."""
    from ag_exams.model_config import get_stage_config
    from ag_exams.prompts import build_argument_pass_per_q_prompt

    cfg = get_stage_config("argument_pass_sonnet")
    prompt = build_argument_pass_per_q_prompt(q_text)
    return await dispatch_gemini(
        prompt,
        model=cfg.model,
        use_diskcache=cfg.cache,
    )


@activity.defn
async def dispatch_argument_pass_per_q_opus(q_text: str) -> str:
    """5-per-option argument pass on one Q. Config stage: argument_pass_opus."""
    from ag_exams.model_config import get_stage_config
    from ag_exams.prompts import build_argument_pass_per_q_prompt

    cfg = get_stage_config("argument_pass_opus")
    prompt = build_argument_pass_per_q_prompt(q_text)
    return await dispatch_gemini(
        prompt,
        model=cfg.model,
        use_diskcache=cfg.cache,
    )


@activity.defn
async def dispatch_blind_take(stripped_questions: str) -> str:
    """Handicapped floor check. No tools, single turn, letters only.

    Model is configurable via the ``blind_take`` stage, but the handicap
    (no tools, max_turns=1) is fixed — switching models without the handicap
    would defeat the check's purpose.
    """
    from ag_exams.model_config import get_stage_config
    from ag_exams.prompts import build_blind_take_prompt

    cfg = get_stage_config("blind_take")
    prompt = build_blind_take_prompt(stripped_questions)
    return await dispatch_gemini(
        prompt,
        model=cfg.model,
        use_diskcache=cfg.cache,
    )


@activity.defn
async def write_fix_guidance(path: str, content: str) -> str:
    """Write a qNN-fix-guidance.md file for the writer to consume on next iter."""
    full_path = REPO_ROOT / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content)
    return str(full_path)


@activity.defn
async def delete_q_file(path: str) -> bool:
    """Delete a qNN.md file so writer resumption regenerates it. No-op if missing."""
    full_path = REPO_ROOT / path
    if full_path.exists():
        full_path.unlink()
        return True
    return False


@activity.defn
async def list_q_files(questions_dir: str) -> list[str]:
    """List canonical qNN.md files in dir (excludes fix-guidance, grounded, etc.)."""
    dir_path = REPO_ROOT / questions_dir
    if not dir_path.exists():
        return []
    return [str(p.relative_to(REPO_ROOT)) for p in glob_q_files(dir_path)]


@activity.defn
async def read_file(path: str) -> str:
    """Generic file read activity for workflow-accessible reads."""
    full_path = REPO_ROOT / path
    return full_path.read_text()


@activity.defn
async def write_file(path: str, content: str) -> str:
    """Generic file write activity. Idempotent, creates parent dirs."""
    full_path = REPO_ROOT / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content)
    return str(full_path)
