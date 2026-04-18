# Pattern: Standalone Verification Executor (Monkeypatch Isolation)

## Symptom
Testing a complex multi-stage pipeline is slow, expensive, and difficult to debug if every test run requires the full orchestration infrastructure (e.g., loading all providers, processing all files, running every stage).

## The Solution: The Monkeypatch Standalone Test
Create a lightweight, standalone script that reuses the workflow logic but isolates it using an overridden executor and a fast, low-cost model (e.g., Gemini Flash).

### Tactical Techniques

1. **Subclassed Isolation**:
   - Subclass the standard `LLMStepExecutor` (or equivalent) to create a test-specific version.
   - Override the `execute` method to bypass standard provider selection and multi-model voting.
   
2. **The "Flash-Only" Patch**:
   - Hardcode the use of a lightweight model like `gemini-3-flash-preview` within the overridden executor.
   - **Benefit**: Faster iteration and significantly lower token cost during repeated debugging of prompt logic.

3. **In-Memory Config Loading**:
   - Use the standard `ConfigLoader` but inject only the specific agent and workflow configurations needed for the test.

4. **Transparent Token Tracking**:
   - Explicitly print token counts and latency for each step in the loop.
   - **Diagnostic Value**: Helps identify "Token Bloat" early—where an agent consumes more context than necessary for its task.

5. **Standalone Output Shielding**:
   - Route test results to a unique directory (e.g., `outputs/test-run-XX/`) to avoid corrupting the production output or triggering the "Stale State" caching issues of the main engine.

## Implementation Example: `test_gemini_only.py`
In the `criminal-law` repository, this pattern is implemented to verify the "Inventory & Replace" workflow:
```python
class GeminiOnlyExecutor(LLMStepExecutor):
    async def execute(self, step, context):
        # Override to force Gemini Flash
        model = "gemini-3-flash-preview"
        print(f"  [{step.name}] Running Gemini Flash...")
        
        # ... logic to call LLM directly and return StepResult ...
        
        print(f"  [{step.name}] Done ({out_tokens} tokens)")
```

6. **Verbatim Logic Verification (Text Preview)**:
   - Include a step that prints a preview of the final rendered text (e.g., the first 1000 characters).
   - **Diagnostic Value**: Allows the developer to immediately confirm that the "Hallucination Guard" and editing logic are working (e.g., verifying the presence of specific judicial citations and the preserve/remove balance) without having to manually open the output files.
   - **Result Context**: In the Class 09 test, this preview confirmed the successful verbatim extraction of *State v. Shell* (2023) within the automated test environment.

7. **Structured Artifact Inspection**:
   - The standalone script should generate discrete JSON files for each workflow step (e.g., `inventory-cases.json`, `find-replacements.json`, `edit-cases.json`). 
   - **Diagnostic Value**: This allows for surgical inspection of the data flow. For example, if `inventory-cases.json` is correct but `find-replacements.json` is missing content, the developer can pinpoint the error to the specific agent's search logic rather than the orchestration layer.
   - **File Mapping**: These files are typically stored in a temporary test directory (e.g., `outputs/class-XX-gemini-test/`) to preserve the production `outputs/class-XX/` state.

## Proof of Effect
This pattern allowed for the verification of Class 09 case inventory recall in **90 seconds** per run, compared to the **10+ minutes** required for the full pipeline. It enabled rapid tuning of the "Header Scanning" and "Anchor Checklist" prompts without the overhead of Stage 3 editing.
