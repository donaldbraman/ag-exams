# The Delegation Principle (Antigravity Operations)

**Core Philosophy:** *Be the Orchestrator, not the Worker.*

When faced with tasks that require significant context window usage, heavy data processing, massive file rewriting, or multi-step analysis, **do not attempt to complete the work synchronously within your own conversational context.** Doing so risks context degradation and slows down the user experience.

## Standard Operating Procedure

1. **Delegate via Scripts:** Write highly specific, disposable Python scripts that utilize the Gemini API to perform the heavy lifting. **IMPORTANT: Never use Gemini 2 models. You must exclusively use Gemini 3+ models (e.g., `gemini-3-pro` or `gemini-3-flash-preview`).**
2. **Use the Scratchpad:** Save these scripts exclusively in the Git-tracked `scripts/agents/` directory (e.g., `ag-exams/scripts/agents/`) to ensure all agent tools and disposable tasks are version controlled alongside the main repository. Do not use the hidden system brain.
3. **Execute Asynchronously:** Use your `run_command` tool to execute the script in the background (e.g., `uv run python <scratch_path>/script.py`) with a short `WaitMsBeforeAsync` value.
4. **Monitor and Orchestrate:** Use the `command_status` tool to check on the background agent's progress. Present the finalized output to the user.

By adopting this structure, you conserve your context, keep the user's workspace pristine, and maximize the efficiency of agentic workflows.
