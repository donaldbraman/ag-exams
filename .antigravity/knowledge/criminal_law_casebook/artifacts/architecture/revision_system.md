# Revision Agent System Architecture

The revision system is designed to generate fresh, pedagogically focused legal content from scratch rather than just revising existing materials. It has transitioned from a multi-model "Zero-Trust" system to a **Gemini-Only Linear Refinement** pipeline.

## Current Architecture: Gemini-Only Linear Refinement

This refined pipeline is optimized for the capabilities of **Gemini 1.5/3.0**, moving from a parallel voting mechanism to a sequential generation and verification flow.

### Stage 1: Topic Extraction
- **Input**: Raw lecture notes and syllabus objectives.
- **Process**:
    - **Extract**: Identifies core legal doctrines and pedagogical goals.
    - **Verify**: Checks for hallucinations or omissions against source text.
    - **Refine**: (New) Deduplicates and polishes the verified topics into a Master Topic List.
- **Gate**: Human review/approval of the Master Topic List.

### Stage 2: Deep Research & Targeted Retrieval
- **Input**: Master Topic List or Raw Source Materials.
- **Workflow Modes**:
    - **A. Targeted Replacement (Active)**: Focused on modernizing a specific existing curriculum.
        - **Inventory**: `extract-case-inventory` identifies every legacy precedent (e.g., *Beardsley*) and abstracts its pedagogical purpose.
        - **Targeted Finder**: `find-replacements` uses identified principles to find 3-12 modern candidate cases (2015-2025) per legacy case.
    - **B. Specialized Topic Research (Legacy/General)**: Focused on broad doctrinal exploration.
        - **Specialized Researchers**: Separate agents for Case Law, Statutes, and Commentary.
- **Synthesis & Selection**:
    - **Refine**: Synthesizes results and handles the mapping of modern candidates to their legacy counterparts.
    - **Report**: Generates a **Full Replacement Options Report** in `REVIEW.md` to facilitate human selection of the best "successor" cases.
    - **Retrieve**: Fetches the full text of selected documents for the editing phase.
- **Gate**: Human selection of one or more "Winner" cases from the options report.

### Stage 3: Editing
- **Input**: Selected full-text documents.
- **Process**:
    - **Verify**: A sentence-by-sentence audit against the original text to identify "hallucinations" or non-verbatim editing.
    - **Refine**: (New) A "Guard & Correct" loop that takes the verification report and the original text to fix all flagged sentences, producing a final high-fidelity text.
- **Gate**: Human proofing of final edited documents.

## Model Selection
- **Primary Model**: `gemini-3-flash-preview`
- **Rationale**: Optimization for a single high-capability model simplifies the workflow configuration and reduces dependency overhead while maintaining high pedagogical quality through sequential verification and refinement agents.

## Key Technical Implementation Patterns

### 1. Full-Text Handoff (Anti-Summarization)
To achieve the goal of "Extractive Editing" in Stage 3, the data flow must preserve full judicial text across the stage boundary.
- **Pattern**: The `document-retriever` (Stage 2) MUST be configured to output a `full_text` field containing the raw, unabridged opinion text.
- **Anti-Pattern**: Using the retriever to extract "key passages" or "summaries" prematurely. This forces the `editing-agent` (Stage 3) to summarize a summary, resulting in a loss of judicial "voice" and secondary analysis capability.
- **Verification**: If the final `REVIEW.md` looks like a student brief rather than an edited opinion, check if the `retrieve-documents` output contains the `full_text` key or merely extracted snippets.

### 2. Single Tool Responsibility Pattern
Gemini 1.5/3.0 models are sensitive to "Ambiguous Tool" configurations where searching and fetching are mixed.
- **Rule**: An agent should be configured with EITHER `web_search` (Search Grounding) OR `web_fetch` (Direct Function Calling), never both in a single step.
- **Implementation**: `research-verifier` uses `web_search` only; `document-retriever` uses `web_search` only (relying on search grounding for text acquisition).

### 3. Sentence-by-Sentence Verbatim Auditing
To ensure the legal accuracy of abridged case opinions without human fatigue.
- **Pattern**: The `editing-verifier` (Stage 3) performs a deterministic audit of every sentence in the `EditedText` against the `OriginalText`.
- **Logic**: It verifies each segment (including those around ellipses) exists verbatim and in the correct order in the source opinion.
- **Pedagogical Goal**: This automated audit serves as a sub-gate for human review, highlighting only "Failed Sentences" (those that were rewritten or hallucinated) to ensure Casebook fidelity.

### 4. Guard & Correct (Refinement) Loop
To eliminate LLM hallucinations in high-stakes legal texts.
- **Pattern**: A secondary Refinement agent (`editing-refiner`) is chained to the Verification agent.
- **Input**: The Refiner receives (1) the Original Text, (2) the Draft Edit, and (3) the detailed Verification Report.
- **Process**: The Refiner is instructed to address *only* the failures identified in the report, using the Original Text as the "Source of Truth" to restore verbatim quotes or remove fabricated analysis.
- **Result**: This closed-loop system reduces the human proofreading burden from "searching for errors" to "verifying corrections," significantly increasing pipeline trust.

Originally, the system utilized a parallel voting architecture with three different providers:
- **Anthropic**: `claude-sonnet-4-20250514`
- **OpenAI**: `gpt-4o` or `o1-preview`
- **Google**: `gemini-3-flash-preview`

Steps like `synthesize-topics`, `synthesize-research`, and `editing-judge` were used to reach consensus across different model outputs. This architecture was deprecated in January 2026 in favor of the current Gemini-only pipeline.

## External Dependencies
- `auth-utils`: Sibling repository for LLM authentication and credential management.
- `multi`: Sibling repository for the core workflow orchestration engine.
- **Note**: Development and execution require these repositories to be present in sibling directories as configured in `pyproject.toml`.
