# Multi Workflow Engine

The `multi` library provides a core orchestration engine for multi-agent LLM workflows. It uses YAML configurations to define steps, agents, and data flow.

## Configuration & Logic

### 1. Global YAML Validation
The `ConfigLoader` in `multi` performs a global validation of the `config/workflows/` directory. It attempts to load and validate *every* YAML file in that directory, regardless of which workflow is actually being executed.
- **Pitfall**: If an obsolete workflow file exists that references a deleted agent, the entire `loader.load_all()` call will fail.
- **Solution**: Always remove or update legacy workflow configurations when deleting agents.

### 2. Workflow Naming Identity
The `name` field defined *inside* the workflow YAML must exactly match the string used to invoke the workflow in the execution script.
- **Example**: `executor.execute(workflow="gemini-revision", ...)` requires `name: gemini-revision` in the YAML metadata.

### 3. Step Input Referencing
The `input` field in a workflow step must follow a specific `step_name.ref_type` format (or `_input.ref_type` for the root input).
- **Format**: `provider_name.output_type` (e.g., `extract-topics.gemini`) or `_input.winner`.
- **Error**: Passing just `_input` or a step name without a reference type will trigger a Pydantic validation error: `Invalid input ref: _input. Expected format: step_name.ref_type`.

### 4. Step Field Restrictions
The workflow schema is strict regarding which fields can be included in a step definition.
- **Pitfall**: Attempting to specify an explicit `provider` (e.g., `provider: gemini`) at the individual step level will trigger a Pydantic `extra_forbidden` error.
- **Constraint**: Step providers are typically determined by the `WorkflowExecutor` or inferred, rather than being hardcoded in the YAML step definitions.

### 5. Forcing Single Provider Execution
In scenarios where the `multi` library defaults to executing all configured providers (Claude, ChatGPT, Gemini) but only one is desired (e.g., Gemini-only refactor), and the YAML schema forbids per-step provider selection, a **monkeypatching** strategy is required.

Because the `multi` engine routes execution differently for tool-enabled vs. standard steps, a **dual-patch** strategy is often necessary:

1.  **Target 1 (Tool-Enabled Steps)**: `multi.core.executors.llm.LLMStepExecutor._run_single_provider_with_tools`
2.  **Target 2 (Standard Steps)**: `auth_utils.llm.LLMClient.parallel_chat`

- **Technique**: Intercept the provider string or model dictionary and filter out non-target models.
- **Implementation**:
  ```python
  from multi.core.executors.llm import LLMStepExecutor
  from auth_utils.llm import LLMClient

  # Patch 1: Intercept tool-enabled execution
  original_run_provider = LLMStepExecutor._run_single_provider_with_tools
  async def new_run_provider(self, provider: str, *args, **kwargs):
      if provider != "gemini":
          # Skip non-target providers to prevent errors/costs
          return "", "skipped", 0, 0
      return await original_run_provider(self, provider, *args, **kwargs)
  LLMStepExecutor._run_single_provider_with_tools = new_run_provider

  # Patch 2: Intercept parallel chat (non-tool steps)
  original_parallel_chat = LLMClient.parallel_chat
  async def new_parallel_chat(messages, models, **kwargs):
      if "gemini" in models:
          # Force only gemini if present
          models = {"gemini": models["gemini"]}
      return await original_parallel_chat(messages, models, **kwargs)
  LLMClient.parallel_chat = new_parallel_chat
  ```
- **Rationale**: This prevents the orchestration engine from attempting to call providers that are not configured or desired, bypassing the parallel execution default while waiting for a schema-level fix. This is critical for avoiding hangs when the engine attempts to reach unconfigured models (e.g., Anthropic/OpenAI) during steps like `extract-topics`.
- **Evolution (Jan 2026)**: While the `criminal-law` project has transitioned to a Gemini-native script, the monkeypatching strategy remains **mandatory**. A final "cleanup" attempt (removing the patches) directly resulted in a 10-minute pipeline "hang" (Job ID `6f5c605f`), as the underlying `multi` orchestration engine attempted to resolve parallel paths involving unconfigured models (Claude/GPT). Explicitly intercepting `parallel_chat` and filtering for Gemini is the verified solution for a stable, single-provider environment.
- **Parallel Execution Robustness (Jan 2026)**: The strategy was verified to be effective even when the workflow YAML invokes multiple steps in parallel (e.g., Stage 2.1 Research). the patches trap and filter these calls asynchronously, allowing the Gemini path to proceed without interference from the unconfigured Claude/ChatGPT paths.
- **Monkeypatch Tracing**: When debugging logical hangs or validation errors, the target functions should be augmented with inspection prints to verify the raw responses of the LLM before they are processed by the library's internal validators.
    ```python
    async def new_run_provider(self, provider, *args, **kwargs):
        if provider != "gemini": return "", "skipped", 0, 0
        result = await original_run_provider(self, provider, *args, **kwargs)
        # Inspect result structure (usually a tuple for _run_single_provider_with_tools)
        if isinstance(result, tuple) and len(result) > 0:
            content = result[0].content if hasattr(result[0], 'content') else result[0]
            print(f"DEBUG: Gemini raw response: {str(content)[:200]}")
        return result
    ```

### 6. API Latency and Timeout Observations
When processing very large context windows (e.g., 25,000+ characters for lecture notes) or complex parallel searches, the pipeline is subject to significant API latency and potential timeouts.
- **Diagnosis**: Stack traces indicate that execution hangs often occur at the network stream level (`httpx._receive_event` waiting on `anyio` read events), particularly when the Gemini API is under high load or processing large grounding requests.
- **Distinction**: These network-level hangs should be distinguished from "Logical Hangs" caused by unconfigured model fallbacks (which are fixed by monkeypatching). Infrastructure administrators should implement robust retries at the provider level to mitigate these intermittent network issues.

### 4. Zero-Trust vs. Linear Refinement
- **Zero-Trust (Legacy)**: Parallel execution across multiple providers (Claude, GPT, Gemini) with a synthesis/voting step.
- **Linear Refinement (Modern)**: Sequential execution by a primary high-capability model (Gemini) with self-verification and polishing steps.

### 6. Workflow Data Integrity
The sequential nature of the Linear Refinement pipeline makes it vulnerable to "data dropouts" if a verification step fails.
- **Verification Failures**: If a step like `verify-research` or `retrieve-documents` fails (e.g., due to a `400 INVALID_ARGUMENT: Tool use with function calling is unsupported` error), the downstream steps (like `edit-case`) may receive empty or valid-looking but incorrect input. 
- **Hallucination Risk**: If input is missing or corrupted by a failed upstream step, LLM agents may default to "hallucinating" plausible but irrelevant examples (e.g., defaulting to *Palsgraf* for a Criminal Law task) to satisfy their prompt requirements.
- **Final Verification (Job `a44dd897`)**: The restoration of high-fidelity data flow was verified by checking the `retrieve-documents-gemini.json` output against the `edit-case-gemini.json` content. Success was confirmed when the Editor produced a casebook-ready version of **Commonwealth v. Levesque** (retrieved in Stage 2) instead of the *Palsgraf* hallucination seen when the retrieval step was broken.
- **Grounding Metadata**: The `auth-utils` Gemini provider successfully captures and returns grounding metadata (search results and sources), which are essential for research provenance and ensuring the model isn't just "inventing" legal citations.

### 7. Result Extraction Patterns
The `multi` library's `StepResult` object is designed around a multi-model "voting" architecture. This introduces specific patterns for retrieving output in different pipeline configurations:

- **Voting/Consensus (Legacy)**: Use `step_result.winner` or `step_result.get_winner_content()`. These rely on the library's internal logic to determine which model produced the "best" response.
- **Single-Provider Fallback**: In linear, single-provider pipelines (where the `.winner` attribute may not be reliably populated by the orchestration engine), a robust content extraction helper is required.
- **Robust Extraction Helper**:
  ```python
  def get_content(step_result):
      if not step_result: return None
      # 1. Try legacy winner logic first
      if hasattr(step_result, 'winner') and step_result.winner:
          return step_result.get_winner_content()
      # 2. Extract directly from the target provider storage
      if hasattr(step_result, 'outputs') and Provider.GEMINI in step_result.outputs:
          output = step_result.outputs[Provider.GEMINI]
          return output.content if hasattr(output, 'content') else str(output)
      return None
  ```
- **Rationale**: Relying solely on `.winner` can result in data-extraction failures (e.g., empty strings or `None`) when the orchestration engine does not perform a voting pass. Explicitly checking the `outputs` dictionary by provider ensures that data flow between the AI pipeline and external reporting/storage systems is preserved. This pattern was definitively verified in the `criminal-law` repository with the successful generation of review files for **Class 09** (Job `4bcf410b`) and **Class 10** (Job `22558bc1`).

### 8. Workflow Execution State & Caching
The `multi` orchestration engine tracks execution progress through mechanisms involving `metadata.json` and step-level artifacts in the output directory.
- **Stale Metadata Conflict**: When a workflow YAML is refactored—particularly when changing step names or adding new sequential steps (e.g., adding `refine-edits` after `verify-edits`)—the `multi` engine may skip the new steps if it detects existing metadata from a previous, differently structured run.
- **Symptom**: New steps appear in the workflow YAML but do not appear in the final `metadata.json`'s `steps_completed` list, even if all other steps succeed.
- **Diagnosis**: If a pipeline hangs indefinitely or fails to execute newly added steps after a workflow structurally changes, the root cause is often "Stale Execution State."
- **Mitigation**: Perform a "Clean Restart" by deleting previous run artifacts (e.g., `rm -rf outputs/class-XX`) to ensure a fresh, consistent execution pass.
- **Diagnostic Technique: Timestamp Verification**: To prove the engine is using stale data, verify the physical freshness of the artifact using `ls -lT` or raw result audit. See [LLM Interaction Patterns: Diagnostic Verification](../../../llm_interaction_patterns/artifacts/patterns/llm/diagnostic_verification.md).

### 9. Infinite Retry Loops & Execution Hangs
Structural changes to a workflow or malformed agent responses can sometimes trigger an "Infinite Retry Loop" within the orchestration engine.
- **Behavior**: The console logs show repeated calls to `new_run_provider` (or the underlying provider function) for the same step identifier (e.g., `extract-topics`) without ever advancing to the "Saving result" logic.
- **Cause**: This is often indicative of a **Validation Failure** or **Uncaught Exception** inside the `multi` library's step execution loop. If the model output does not meet a required schema (e.g., missing specific JSON keys), some versions of the engine may attempt to "retry" the call automatically to resolve the ambiguity, leading to an infinite hang.
- **Diagnosis**: Use the **Monkeypatch Tracing** pattern (Section 5) to inspect the raw model output. Compare this output against the `output_format` specified in the agent's markdown configuration.
### 10. Agent-Workflow Data Binding (Placeholders)
The connection between a workflow's `input` mapping and an agent's execution is not automatic. The agent's markdown configuration must explicitly include placeholders to "catch" the data provided by the workflow.
- **Pattern**: If a workflow step maps multiple inputs (e.g., `original_text`, `draft_edit`), the target agent's `.md` file MUST contain corresponding `{original_text}` and `{draft_edit}` tokens.
- **Ambiguity Pitfall**: If placeholders are missing, the agent will receive the system instructions but will have no "slots" for the actual data. High-capability models (like Gemini) may respond by explicitly asking for the missing inputs rather than processing them.
- **Best Practice**: Always wrap agent inputs in clear headers or section markers within the agent markdown to maintain structural injection (e.g., `## Your Inputs\n{input_variable}`).
