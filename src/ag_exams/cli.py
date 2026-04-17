"""CLI for launching exam generation workflows."""

from __future__ import annotations

import asyncio
import sys
from datetime import timedelta

from temporalio.client import Client

from ag_exams.models import ExamConfig
from ag_exams.workflow import BuildFinalExam

TASK_QUEUE = "exam-pipeline"


async def start_exam(config: ExamConfig) -> str:
    """Start a BuildFinalExam workflow and return the workflow ID."""
    import json
    import subprocess
    import time
    from pathlib import Path
    
    print("Starting ephemeral Temporal worker...")
    worker_proc = subprocess.Popen(
        [sys.executable, "-m", "ag_exams.worker"],
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    time.sleep(2)  # Give the worker a moment to bind to Temporal
    
    try:
        client = await Client.connect("localhost:7233")

        scenario_tag = "-".join(config.scenarios) if len(config.scenarios) <= 3 else "full"
        workflow_id = f"exam-{scenario_tag}"

        print(f"Executing workflow: {workflow_id}")
        print(f"  Scenarios: {config.scenarios}")
        print(f"  Dry run: {config.dry_run}")
        print(f"  Output: {config.output_dir}")
        print()
        print("Note: If the workflow pauses for human review, run in another terminal:")
        print(f"  uv run python -m ag_exams.cli approve {workflow_id}")
        print()
        
        start_time = time.time()
        # We use execute_workflow to block until the workflow finishes or fails
        result = await client.execute_workflow(
            BuildFinalExam.run,
            config,
            id=workflow_id,
            task_queue=TASK_QUEUE,
            execution_timeout=timedelta(hours=24),
            task_timeout=timedelta(seconds=300),
        )

        print(f"Workflow {workflow_id} completed successfully.")
        print(f"Result: {result}")
        
        # Generate metrics report
        end_time = time.time()
        _generate_metrics_report(start_time, end_time, config, workflow_id)
        
        return workflow_id
        
    finally:
        print("Tearing down ephemeral worker...")
        worker_proc.terminate()
        worker_proc.wait()


def _generate_metrics_report(start_time: float, end_time: float, config: ExamConfig, workflow_id: str) -> None:
    """Aggregate token usage from the metrics log and generate a cost report."""
    import json
    from pathlib import Path
    
    elapsed_seconds = end_time - start_time
    minutes, seconds = divmod(elapsed_seconds, 60)
    
    metrics_path = Path.home() / ".cache" / "ag-exams" / "metrics.jsonl"
    repo_root = Path(__file__).resolve().parents[3]
    report_path = repo_root / config.output_dir / f"{workflow_id}-metrics.md"
    
    model_usage: dict[str, dict[str, int]] = {}
    
    if metrics_path.exists():
        with open(metrics_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    ts = data.get("timestamp", 0)
                    if ts >= start_time:
                        m = data.get("model", "unknown")
                        if m not in model_usage:
                            model_usage[m] = {"prompt": 0, "output": 0}
                        model_usage[m]["prompt"] += data.get("prompt_tokens", 0)
                        model_usage[m]["output"] += data.get("output_tokens", 0)
                except json.JSONDecodeError:
                    continue
                    
    total_cost = 0.0
    report_lines = [
        f"# Pipeline Execution Metrics: {workflow_id}",
        "",
        f"**Total Execution Time:** {int(minutes)}m {int(seconds)}s",
        "",
        "## Model Token Usage and Cost",
        "| Model | Input Tokens | Output Tokens | Est. Cost ($) |",
        "|---|---|---|---|"
    ]
    
    for m, usage in model_usage.items():
        # Pricing logic
        cost = 0.0
        p_tok = usage["prompt"]
        o_tok = usage["output"]
        
        if "pro" in m.lower():
            cost = (p_tok / 1_000_000 * 1.25) + (o_tok / 1_000_000 * 5.00)
        elif "flash" in m.lower():
            cost = (p_tok / 1_000_000 * 0.075) + (o_tok / 1_000_000 * 0.30)
            
        total_cost += cost
        report_lines.append(f"| `{m}` | {p_tok:,} | {o_tok:,} | ${cost:.4f} |")
        
    report_lines.extend([
        "",
        f"**Total Estimated API Cost:** ${total_cost:.4f}"
    ])
    
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\\n".join(report_lines))
    print(f"Metrics report written to {report_path}")



async def approve_scenario(workflow_id: str, feedback: str = "") -> None:
    """Send the approve_scenario signal to a running workflow."""
    client = await Client.connect("localhost:7233")
    handle = client.get_workflow_handle(workflow_id)
    await handle.signal(BuildFinalExam.approve_scenario, feedback)
    print(f"Approved scenario for workflow {workflow_id}")


async def get_status(workflow_id: str) -> None:
    """Query workflow status."""
    client = await Client.connect("localhost:7233")
    handle = client.get_workflow_handle(workflow_id)
    status = await handle.query(BuildFinalExam.get_status)
    print(f"Status: {status}")


def _parse_start_args(args: list[str]) -> ExamConfig:
    """Parse CLI arguments for the start command into an ExamConfig."""
    scenarios: list[str] = ["all"]
    dry_run = False
    skip_grounding = False
    skip_adversarial = False
    reuse_whiteboard = False
    output_dir = "criminal-law/quiz-system/research/final-exam"

    i = 0
    while i < len(args):
        if args[i] == "--scenario" and i + 1 < len(args):
            scenarios = [args[i + 1]]
            i += 2
        elif args[i] == "--output-dir" and i + 1 < len(args):
            output_dir = args[i + 1]
            i += 2
        elif args[i] == "--dry-run":
            dry_run = True
            i += 1
        elif args[i] == "--skip-grounding":
            skip_grounding = True
            i += 1
        elif args[i] == "--skip-adversarial":
            skip_adversarial = True
            i += 1
        elif args[i] == "--reuse-whiteboard":
            reuse_whiteboard = True
            i += 1
        else:
            scenarios = [args[i]]
            i += 1

    return ExamConfig(
        scenarios=scenarios,
        dry_run=dry_run,
        skip_grounding=skip_grounding,
        skip_adversarial=skip_adversarial,
        reuse_whiteboard=reuse_whiteboard,
        output_dir=output_dir,
    )


def _print_usage() -> None:
    """Print CLI usage and exit."""
    print("Usage:")
    print(
        "  uv run python -m ag_exams start "
        "[--scenario NAME] [--dry-run] "
        "[--skip-grounding] [--skip-adversarial]"
    )
    print("  uv run python -m ag_exams approve WORKFLOW_ID [FEEDBACK]")
    print("  uv run python -m ag_exams status WORKFLOW_ID")
    print("  uv run python -m ag_exams qa-maps [--chapter NUMBER | --all]")
    print("  uv run python -m ag_exams fix-traps [--chapter NUMBER | --all]")
    sys.exit(1)


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 2:
        _print_usage()

    command = sys.argv[1]

    if command == "start":
        config = _parse_start_args(sys.argv[2:])
        asyncio.run(start_exam(config))
    elif command == "approve":
        if len(sys.argv) < 3:
            print("Usage: approve WORKFLOW_ID [FEEDBACK]")
            sys.exit(1)
        wf_id = sys.argv[2]
        feedback = sys.argv[3] if len(sys.argv) > 3 else ""
        asyncio.run(approve_scenario(wf_id, feedback))
    elif command == "status":
        if len(sys.argv) < 3:
            print("Usage: status WORKFLOW_ID")
            sys.exit(1)
        asyncio.run(get_status(sys.argv[2]))
    elif command == "qa-maps":
        from ag_exams.qa_chapter_maps import run_all
        import argparse
        parser = argparse.ArgumentParser(prog="uv run python -m ag_exams qa-maps")
        parser.add_argument("--chapter", "-c", type=int, help="Chapter number to QA")
        parser.add_argument("--all", action="store_true", help="QA all chapters")
        qa_args = parser.parse_args(sys.argv[2:])
        
        if qa_args.all:
            asyncio.run(run_all())
        elif qa_args.chapter:
            asyncio.run(run_all([qa_args.chapter]))
        else:
            parser.print_help()
    elif command == "fix-traps":
        from ag_exams.fix_map_traps import run_all
        import argparse
        parser = argparse.ArgumentParser(prog="uv run python -m ag_exams fix-traps")
        parser.add_argument("--chapter", "-c", type=int, help="Chapter number to fix")
        parser.add_argument("--all", action="store_true", help="Fix all chapters")
        fix_args = parser.parse_args(sys.argv[2:])
        
        if fix_args.all:
            asyncio.run(run_all())
        elif fix_args.chapter:
            asyncio.run(run_all([fix_args.chapter]))
        else:
            parser.print_help()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
