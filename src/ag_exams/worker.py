"""Temporal worker for the exam generation pipeline."""

from __future__ import annotations

import asyncio
import concurrent.futures

from temporalio.client import Client
from temporalio.worker import Worker

from ag_exams.activities import (
    delete_q_file,
    dispatch_adversarial,
    dispatch_ambiguity_audit,
    dispatch_ambiguity_audit_per_q,
    dispatch_edge_case_audit_per_q,
    dispatch_architect,
    dispatch_argument_pass_per_q_opus,
    dispatch_argument_pass_per_q_sonnet,
    dispatch_blind_take,
    dispatch_critic,
    dispatch_grounding,
    dispatch_grounding_per_q,
    dispatch_question_writer,
    list_q_files,
    read_existing_package,
    read_file,
    write_artifact,
    write_file,
    write_fix_guidance,
    wipe_directory,
    commit_run_to_git,
)
from ag_exams.workflow import BuildFinalExam

TASK_QUEUE = "exam-pipeline"


async def main() -> None:
    """Start the exam pipeline worker."""
    client = await Client.connect("localhost:7233")

    activity_executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[BuildFinalExam],
        activities=[
            dispatch_architect,
            dispatch_critic,
            dispatch_question_writer,
            dispatch_grounding,
            dispatch_grounding_per_q,
            dispatch_adversarial,
            dispatch_ambiguity_audit,
            dispatch_ambiguity_audit_per_q,
            dispatch_edge_case_audit_per_q,
            dispatch_argument_pass_per_q_sonnet,
            dispatch_argument_pass_per_q_opus,
            dispatch_blind_take,
            delete_q_file,
            list_q_files,
            read_existing_package,
            read_file,
            write_artifact,
            write_file,
            write_fix_guidance,
            wipe_directory,
            commit_run_to_git,
        ],
        activity_executor=activity_executor,
        max_concurrent_activities=5,
    )

    print(f"Exam pipeline worker started, listening on: {TASK_QUEUE}")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
