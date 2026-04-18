# Execution Rules for ag-exams Pipeline

When working in the `ag-exams` repository, the user has mandated that long-running tasks must not block the agent's context.

## Asynchronous Execution

When dispatching the `ag-exams` Temporal pipeline (e.g., `uv run python -m ag_exams start ...`):
1. **Never run the command synchronously.** Do not wait for the command to finish.
2. Use the `run_command` tool and set `WaitMsBeforeAsync` to a small value (e.g., `500` or `1000` ms).
3. Let the command dispatch to the background. 
4. Use the `command_status` tool to periodically check on the execution status or output if necessary.

This ensures that the agent's context is conserved and the conversational loop remains unblocked while the heavy pipeline execution (like the 15-question Architect/Critic generation loops) completes in the background.
