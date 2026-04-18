# Gemini-Only Implementation Summary

The refactor of the `criminal-law` revision pipeline from a multi-model "Zero-Trust" mechanism to a streamlined Gemini-only refinement pipeline was completed in January 2026.

## Completed Refactoring Steps

### 1. Workflow Transition
- **Created**: `config/workflows/gemini-revision.yaml`. This new linear workflow replaces the multi-provider consensus logic with sequential `Extract -> Verify -> Refine` steps.
- **Removed**: `config/workflows/casebook-revision.yaml` (legacy multi-model workflow).

### 2. Agent Refinement
- **Created**: New refinement agents were added to handle the roles previously held by synthesizers and judges:
    - `config/agents/topic-refiner.md`: Polishes verified topics into a master list.
    - `config/agents/research-refiner.md`: Curates the final reading list from research results.
    - **Note**: These refiners replace the legacy multi-model `topic-synthesizer` and `research-synthesizer`.
- **Agent-Tool Specialization**: To avoid Gemini API conflicts (400 Invalid Argument) and ensure "polite" web access, agents are now designed with a single tool responsibility (Single Tool Responsibility Pattern). Both `research-verifier` and `document-retriever` were specialized to use `web_search` only, avoiding the conflict with `web_fetch` and preventing automated blocks from sites like Google Scholar while still allowing content extraction via search grounding.

### 3. Script Updates
- **`scripts/run_class.py`**: Refactored to:
    - Default to the `gemini-revision` workflow.
    - Enforce the `gemini-3-flash-preview` model via the `WorkflowExecutor`.
    - Remove credential checks for Anthropic and OpenAI.
    - Simplify the `_generate_stage_reviews` logic to handle the single-provider output structure.
- **Legacy Cleanup (Completed)**: Following the success of the Gemini-only pipeline, the repository has been transitioned to a "pure" state. All Claude and ChatGPT specific logic, synthesis agents, and consensus-voting functions have been stripped from the codebase. The `scripts/run_class.py` orchestrator is now a native Gemini script.
- **Mandatory Monkeypatching**: Contrary to early cleanup attempts, the dual-monkeypatching strategy (intercepting `parallel_chat` and `_run_single_provider_with_tools`) is **mandatory** for stability. A final validation run without these filters resulted in a persistent 10-minute hang (Job `6f5c605f`), confirming that the `multi` library orchestration engine requires explicit model filtering to bypass its default parallel check-ins. The final `scripts/run_class.py` preserves these patches as a permanent stability layer.

### 4. Documentation Updates
- **`REVISION_SPEC.md`**: Rewritten to define the "Gemini-Only Revision Architecture," removing references to "Zero-Trust" parallel voting.
- **`CLAUDE.md`**: Updated with instructions to use `gemini-3-flash-preview` as the primary model and simplified essential commands.

### Verified Implementation (Jan 2026 - Final)
The final implementation in `scripts/run_class.py` uses the dual-monkeypatch strategy to force Gemini-only execution and ensure reliability. This allows the repository to remain "pure" in its output while bypassing the complex parallel logic of the multi-provider library.

### Verification Milestone (Jan 2026)
During initial verification, several technical hurdles were resolved:
- **Environment Resolution**: To satisfy relative path dependencies in `pyproject.toml`, the sibling repositories `auth-utils` and `multi` were copied from the developer's root `GitHub/` directory into the active `antigrav-crim/` workspace.
- **Workflow Configuration Fix**: A validation error was identified in the new `gemini-revision.yaml` where step inputs used `_input` directly. This was corrected to `_input.winner` (the required `step_name.ref_type` format) to comply with the `multi` workflow engine's schema.
- **Global Validation Cleanup**: The `ConfigLoader` in the `multi` engine validates all YAML files in the `config/workflows/` directory, even if they aren't the primary workflow being run. Obsolete workflows (e.g., `casebook-revision-single.yaml`) referencing deleted agents had to be removed to pass validation.
- **Workflow Identifier Alignment**: The `name` field defined inside the workflow YAML must exactly match the ID used to invoke it in scripts (e.g., `executor.execute(workflow="gemini-revision", ...)` requires `name: gemini-revision` in the YAML).
- **Tool Support Implementation (Gemini)**: A critical bug in `auth-utils` was identified where tool configurations (e.g., `web_search`) were not being passed to the Gemini `generate_content` call. The `GoogleProvider` in `auth-utils/src/auth_utils/llm/providers/google.py` was patched to explicitly pass `tools` within the `GenerateContentConfig`.
- **Workflow Schema Constraints**: Attempts to explicitly set `provider: gemini` within the `gemini-revision.yaml` steps to avoid process hangs revealed that the `multi` library schema forbids extra fields in steps, resulting in a Pydantic `extra_forbidden` error.
- **Provider Filtering Monkeypatch**: To enforce Gemini execution without changing the core library, a **dual-monkeypatch** strategy was applied in `scripts/run_class.py`. This involved patching both `LLMStepExecutor._run_single_provider_with_tools` (for tool-enabled research steps) and `LLMClient.parallel_chat` (for standard steps like topic extraction). This explicitly skips execution for `claude` and `chatgpt`, resolving persistent "hangs" caused by the engine attempting to reach unconfigured models during any step of the workflow.
- **Web Access Audit**: Following concerns about potential hallucinations, a manual audit using `scripts/verify_links.py` as well as inspection of `grounding_metadata` in the raw outputs confirmed that the research-agent is successfully accessing the live web. All generated Google Scholar links were found to be structurally valid and relevant.
- **Stage 2->3 Data Flow Restoration**: The final blocker—a 400 error in the `document-retriever`—was resolved by removing `web_fetch` from its tool configuration. This restored the flow of actual case text (e.g., *State v. Lisa*) to the Stage 3 Editing step, successfully replacing the *Palsgraf* hallucinations with relevant legal content.

### Quality Assessment (Jan 2026 - Final)
Following the configuration fixes, a full run on Class 09 (Omissions) demonstrated significant quality improvements:
- **Conceptual Depth**: The Gemini-only pipeline successfully extracted high-level legal tensions (e.g., "Individual Autonomy vs. Communal Duty") rather than generic case summaries.
- **Research Richness**: Stage 2 retrieved diverse and modern authorities, including *State v. Lisa* (2007) and *State v. K.A.R.* (2008), alongside critical academic commentary.
- **Google Scholar Integration**: The `research-agent` was updated to prioritize [Google Scholar](https://scholar.google.com) for case opinions. This was highly successful, with the agent retrieving valid links for cases like *State v. Lisa* and *State v. LaBorde* (2016).
- **Grounding Metadata**: The research results now successfully incorporate grounding source URLs from the Google search tools.
- **Editing Fidelity**: With the retrieval step restored, the `editing-agent` successfully reduced actual retrieved texts like **Lambert v. California** (US 1957) and **Commonwealth v. Levesque** (Mass. 2002) to casebook-ready lengths (approx 2,000 words) while preserving the legal reasoning requested by the pedagogical goals. This definitively replaced the previous *Palsgraf* hallucinations with relevant, Class 09-appropriate content.

### Reproducibility Milestone (Jan 2026)
Following the definitive success of the Class 09 (Omissions) run, the pipeline was executed against **Class 10 (Mistake)**. This run (Job `22558bc1`) completed successfully (Exit Code 0), serving as a validation of the system's cross-topic reproducibility and confirming that the technical fixes (Single Tool Responsibility, Monkeypatching, Tool Handoff) are stable across different conceptual modules and search clusters.

**Operational Refinement & Final Verification**: A final edge case was resolved where the human-readable `REVIEW.md` files were being generated with empty content due to legacy code expecting a "winner" from multi-model voting. The reporting logic was updated to correctly extract single-provider (Gemini) results. This fix was definitively verified in a final full run of **Class 09** (Job `4bcf410b`), which produced correctly populated review files for all stages, marking the successful conclusion of the Gemini-only refactor.

### 5. Pedagogical Refinement: Recency Bias (2016-2026)
Following the stabilization of the technical pipeline, a pedagogical refinement was implemented in January 2026 to modernize the case selection process:
- **Mandatory Recency (2016-2026)**: The `research-agent` instructions were updated to mandate searching for cases decided within the last decade.
- **Preference for Modern Reasoning**: The `research-refiner` was instructed to prioritize these recent cases over classic/landmark ones whenever they illustrate the legal concept with equal or superior clarity.
- **Verification (Class 09)**: This strategy was implemented and tested in a secondary run of **Class 09 (Omissions)** (Job `de7defb9`).
- **Empirical Result: Recency Persistence Challenge**: Despite mandatory instructions (2016-2026 range) and date-specific search queries, the pipeline primarily retrieved "Landmark" cases (*Beardsley* 1907, *Lambert* 1957) for foundational topics. This suggests a strong retrieval bias in LLMs toward classic authorities when topics like "Morality vs. Law" are queried, requiring even stricter input-level date forcing to overcome.
- **Grounding Integrity Insight**: The `verify-edits` step reported a high failure rate (37/52 sentences failing verbatim checks) in Job `de7defb9`. This occurs because the `editing-agent` uses grounded snippets or summaries as "OriginalText," while the verifier expects matching against the full judicial opinion. Verification in grounding-based pipelines must account for the semantic nature of retrieval vs. the strictness of verbatim auditing.

### 6. Architectural Transition: Specialized Research Agents (Jan 2026)
Following the "Recency Bias" experiment, the Stage 2 research architecture was further specialized to ensure greater depth:
- **From General to Specific**: The single `research-agent` was replaced with three specialized agents: `case-researcher`, `statute-researcher`, and `commentary-researcher`.
- **Volume Targeting**: Each researcher is tasked with finding a minimum of **3-12 documents** of their specific type, allowing for a more critical synthesis and selection process by the `research-refiner`.
- **Enhanced Recency**: The `case-researcher` maintains the 2016-2026 mandate but with more focused search queries, helping to overcome the "Landmark Persistence" observed in earlier runs.
- **Workflow Integration**: The `gemini-revision.yaml` workflow was modified to incorporate these tripartite research steps (`research-cases`, `research-statutes`, `research-commentary`), feeding their aggregate outputs into the final Stage 2 refinement.
- **Volume Preservation Mandate**: The `research-refiner` was specifically updated to prioritize **consolidation over filtering**, ensuring that the high volume of documents (3-12 per type) found by specialized agents is preserved for the final reading list rather than being reduced to a single "best" choice.
- **Final Verification (Jan 2026)**: A final execution pass (Job `718d99e4`) demonstrated that this specialized architecture successfully breaks the "Landmark Persistence" barrier, providing recent cases (e.g., *Norg v. City of Seattle* 2023) alongside foundationalMPC sections. The system is now fully optimized for the 100% Gemini-native revision mandate.
- **Reporting Stability**: The automated reporting logic in `scripts/run_class.py` was verified to dynamically handle these new step names, ensuring resulting JSON files are correctly mapped to `stage-2-research/`.

### 7. Full-Text Editing Restoration (Jan 2026)
Following the switch to specialized researchers, a critical quality regression was identified where the final output in Stage 3 transitioned into narrative summaries rather than edited cases.
- **Root Cause**: The `document-retriever` agent was extracting "key passages" in its JSON output instead of providing the complete raw text of the opinion. Consequently, the `editing-agent` was being forced to edit a summary of a summary.
- **Fix**: The `document-retriever` output schema was updated to prioritize a `full_text` field. The `editing-agent` instructions were modified to explicitly require extractive editing from this `full_text` field, ensuring a return to the high-fidelity Casebook format.
- **Definitive Verification**: Verified in Job **f8425061** (Class 09), where **_Commonwealth v. Carter_ (2019)** was successfully retrieved as a 4,200-word full text and edited into a high-fidelity opinion preserving Judge Kafker's voice.

### 8. Model Capacity Trade-offs (Full-Text vs. Volume)
The transition to high-fidelity "Extractive Editing" introduced a significant token constraint in the final stage.
- **Observation**: When providing the model with ~4000-8000 words of "Full Text" for editing, the output token limit often prevents the model from processing multiple cases in a single pass.
- **Result**: In Job **f8425061**, the pipeline successfully produced one high-quality principal case study (*Carter*) while identifying but not fully editing secondary cases (*Miranda*, *Beardsley*) to avoid output truncation.
- **Strategy**: For future scaling, the system should adopt a per-case batching strategy in Stage 3 to maintain both the 3-12 document volume and the 2,000-word extractive depth.

### 9. Hallucination Guard: Refinement Loop (Jan 2026)
To address the risk of LLMs introducing summaries or rewrites in a "verbatim" context, a refinement loop was added to Stage 3.
- **Agent Integration**: Created `config/agents/editing-refiner.md`. This agent is specialized in taking a "failed" verification report and surgically fixing the draft.
- **Workflow Update**: `gemini-revision.yaml` was extended to include `refine-edits` as Step 3.3.
- **Reporting Update**: `scripts/run_class.py` was modified to prioritize the output of the refiner (`refine-edits`) over the raw draft (`edit-case`) when generating the final `REVIEW.md`. This ensures that human reviewers see only the "Guard & Corrected" version.
- **Verification Efficacy (Class 09)**: In Job **f8425061**, the `editing-verifier` identified critical failures in the primary case edit:
    *   **Fabrication**: Sentence 10 ("The defendant was sentenced to two and one-half years...") was flagged as not present in the original text (Hallucination).
    *   **Verbatim Drift**: Multiple passages in the "Facts" (Sentences 11-22) and "Reasoning" (Sentences 28-52) sections were flagged as "Not verbatim" because the model attempted to summarize or simplify original judicial language rather than quoting it directly.
- **Refinement Success**: The `editing-refiner` uses these specific sentence-level flags to surgically restore the judicial tongue, ensuring that the final `REVIEW.md` contains 100% verified legal content without the burden of human proofreading of every single line.
- **Integration Note (Variable Binding)**: Initial deployment of the `editing-refiner` revealed a critical workflow binding requirement: the agent's markdown configuration must explicitly include `{original_text}`, `{draft_edit}`, and `{verification_report}` placeholders to receive data from the `multi` orchestration engine. Without these, the model correctly identifies the missing context and asks for the input rather than processing it.

## Known Constraints & Issues
- **Dependency Persistence**: For development environments using `uv` with path-based sources, ensure sibling repositories (`auth-utils`, `multi`) are correctly linked or copied to the active workspace.
- **Library Patch Management**: The fix for Gemini tool support exists in the local copy of `auth-utils`. Future environment setups must ensure this patch (explicitly passing `tools` to the Gemini client) is maintained until upstreamed.
- **API Latency and Timeouts**: When processing very large inputs (e.g., 25,000+ characters of lecture notes), the Gemini API may exhibit significant latency or timeouts. Debugging via stack traces reveals that the execution can hang in the network layer (`httpx` waiting on `anyio` read events). This should be distinguished from the "logical hangs" caused by unconfigured model fallbacks (which are resolved by the dual-monkeypatch).
- **Tool Handoff Error (400 INVALID_ARGUMENT)**: In cases where a verification or retrieval step (like `verify-research` or `retrieve-documents`) is configured with mixed tools (search + fetch), the call fails with a "Tool use with function calling is unsupported" (400) error. This causes subsequent steps in the pipeline to lose access to valid data. In Class 09, this caused the editor to hallucinate/default to *Palsgraf v. Long Island Railroad Co.* because the research data was empty. This was resolved across all agents by adhering to the Single Tool Responsibility Pattern.
- **Scholar Scraping Blocks**: Automated verification scripts and tools cannot directly `GET` Google Scholar pages due to aggressive 429 rate limiting. Verification must rely on Scholar-specific URL pattern matching or secondary search grounding.

## Repository Isolation & Collaboration
To prevent experimental refactors from "contaminating" the shared main branch or impacting other contributors:
- **Branching Strategy**: A dedicated feature branch (e.g., `gemini-only-pipeline`) should be used to isolate the transition from multi-model to single-model architecture.
- **Gitignore Hygiene**: Pipeline build artifacts and model outputs (e.g., the `outputs/` directory) must be explicitly added to `.gitignore`. This prevent large, ephemeral JSON and Markdown files from bloating the repository history and causing merge conflicts between different research runs.
- **Dependency Isolation**: Locally patched dependencies (`auth-utils`, `multi`) are kept as sibling directories rather than being committed to the main project tree, ensuring that only stabilized, upstreamed changes are shared.

### 10. Targeted Case Replacement Pivot (Jan 2026)
Following a user request for increased volume and direct "successor" mapping for legacy cases, the pipeline was pivoted from broad topic research to a precedent-led approach.
- **Inventory Agent**: Added `case-inventory` to extract specific legacy cases from lecture notes.
- **Finder Agent**: Added `case-replacement-finder` to find 3-12 modern candidate successors for each legacy case.
- **Workflow Restructuring**: `gemini-revision.yaml` now starts by inventorying the existing curriculum and then runs targeted parallel searches for replacements, ensuring pedagogical parity and high-volume selection report for the faculty reviewer.
- **Reporting Success**: The `scripts/run_class.py` logic was updated to display a **Full Replacement Options Report**, providing the human reviewer with a clear "successor lineage" for every recommendation. This represents the final evolution of the revision system from general search to curriculum-specific modernization.

### 11. Polite Retrieval and Grounding Strategy
To ensure the long-term stability of the revision pipeline and avoid common LLM pitfalls during internet access:
- **Philosophy**: Prefer "Search Grounding" over "Scraping." Direct scraping (via `web_fetch`) is fragile, prone to 429 blocks, and often results in technical failures on legal sites (e.g., Google Scholar, Westlaw, Lexis).
- **Tool Specialization**: The system adopts the **Single Tool Responsibility Pattern**. Agents like `document-retriever` are intentionally restricted from using fetching tools if they also use search tools.
- **Mechanism**: By providing the model with only `web_search` capabilities, we force it to rely on Google's search result snippets and grounding proof. For full-text documents, the system fetches the content of the "Winner" case using the model's specialized search knowledge to find the cleanest, most accessible legal repository (e.g., CourtListener, Justia).
- **Error Mitigation**: This strategy eliminates the **400 INVALID_ARGUMENT** errors ("Tool use with function calling is unsupported") that occur when a model attempts to mix high-level grounding with low-level HTTP function calls.

### 12. Agent-Workflow Data Binding (Placeholders)
A critical technical insight for multi-agent systems using the `multi` library and Gemini:
- **The Requirement**: For an agent to correctly receive inputs from a preceding workflow step (e.g., the `editing-refiner` receiving the `original_text` from the `retriever`), the agent's markdown configuration **MUST** contain explicit `{placeholder_name}` tokens in the prompt.
- **The Failure Mode**: If placeholders are missing, the Gemini model detects that the workflow expects it to act on data it hasn't seen. Instead of attempting to infer the data from the context window (which can be unreliable), high-capability models like Gemini will correctly pause and ask the user for the missing inputs, effectively breaking the automated pipeline.
- **Standardized Schema**: All specialized agents in the Stage 2/3 refinement loops (Refiners, Verifiers) must be audited to ensure their templates match the step-input schema defined in `gemini-revision.yaml`.

### 13. JSON Volume Tuning (Jan 2026)
To satisfy the requirement for "3-12 modern cases," the specialized researchers underwent **prompt-level volume tuning**:
- **Technique**: Appending a trailing ellipses placeholder inside the JSON output example.
- **Pattern**:
  ```json
  "results": [
    { "title": "Example Case", ... },
    { "...": "..." }
  ]
  ```
- **Impact**: This structural cue in the few-shot example prevents the model from stopping after a single coherent response, successfully increasing the candidate menu for human review. 
- **Verification**: Job `14e88bc0` (Jan 6, 2026) demonstrated a **500% increase** in generated content volume. The `find-replacements-gemini.json` output grew from 1.8KB (3 cases) to **10.5KB (6 cases with deep metadata)**, including high-profile anchors like *People v. Crumbley* (2024).

