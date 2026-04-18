# Pattern: Diagnostic Verification (Stale vs. Fresh)

## Symptom
In complex agentic pipelines with stage-based caching (like the `multi` library), a pipeline may appear to complete successfully but produce outdated results. This happens when the engine detects existing metadata or files from a previous run and "skips" fresh execution.

## The Solution: Physical Timestamp Verification
Do not trust the console output's "Success" message or the simple existence of an output file. Verify the physical "Freshness" of the artifact.

### Tactical Techniques

1. **Detailed Listing (`ls -lT` or `ls --full-time`)**:
   - Check the exact modification time of the output JSON/Markdown files.
   - If the file timestamp is older than the current execution start time, the pipeline used a **Stale Result**.
   
2. **Raw Output Audit**:
   - Check the raw `*-gemini.json` provider outputs rather than the polished `REVIEW.md` files. Reporting scripts often accumulate or fail to clear old review content.
   
3. **Execution State Purge**:
   - If a workflow's structure changes (new steps added), perform a "Clean Restart" by deleting the output directory (`rm -rf outputs/class-XX`). This forces the orchestration engine to rebuild its execution graph from scratch.

4. **Linear Refinement Audit (Guard & Correct)**:
   - For high-stakes extractive tasks, use a three-step **Draft -> Verify -> Refine** sequence.
   - **Diagnostic Value**: If the Verifier (`Step 2`) identifies a high failure rate in the Draft (`Step 1`), it serves as a diagnostic signal that the Drafter agent needs a restrictive prompt update (e.g., "Verbatim Only") or better context grounding. In Class 09 verification, the Verifier successfully caught truncation and mid-sentence cut-offs that the Drafter had passed as "complete."

5. **Continuous Polling Verification**:
   - When monitoring a background pipeline, do not rely on the simple presence of a file. Use `ls -lT` repeatedly to confirm the modification time moves past the current run's start time. This prevents "Logical Hangs" where the developer investigates a stale file while the background process is still stuck or running on old logic.

6. **Flash-based Standalone Verification**:
   - Use a specialized script (e.g., `test_gemini_only.py`) that forces a lightweight model (Gemini Flash) to re-run the core logic.
   - **Diagnostic Value**: If the standalone run succeeds but the production run fails or hangs, the issue is likely in the orchestration engine's state management or provider fallback logic rather than the agent's prompts.
   - See [Standalone Verification Executor](./standalone_verification.md).

### Rationale: Stale Data Conflict
Orchestration engines often track progress to save tokens/time. If a step's *name* remains the same but its *content/logic* changes, the engine may erroneously believe the step is already complete.
