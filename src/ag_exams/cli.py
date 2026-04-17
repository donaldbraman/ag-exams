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
    import subprocess
    import time
    
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
        return workflow_id
        
    finally:
        print("Tearing down ephemeral worker...")
        worker_proc.terminate()
        worker_proc.wait()



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
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
