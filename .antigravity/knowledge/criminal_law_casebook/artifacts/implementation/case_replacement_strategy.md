# Targeted Case Replacement Strategy

This strategy is used to modernize the casebook by systematically replacing outdated precedents found in legacy lecture notes and syllabi with multiple high-fidelity modern candidates.

## 1. Objectives
- **Modernization**: Move away from cases with dated social contexts (e.g., early 1900s cases like *People v. Beardsley*).
- **Volume**: Provide the professor with a "1-to-N" choice (1 legacy case → 3–12 modern options).
- **Pedagogical Parity**: Ensure the replacement case teaches the exact same legal principle/concept as the original (e.g., the "Special Relationship" requirement for duty to act).

## 2. Two-Step "Inventory & Replace" Loop

### Step A: Case Inventory (`case-inventory`)
- **Input**: Raw lecture notes, syllabus, or legacy casebook chapters.
- **Process**: The agent identifies every case mentioned (both excerpted and cited) and extracts its **Pedagogical Purpose**.
- **Exhaustiveness Requirement (Universal Coverage)**: The user mandates identifying **ALL** cases in the provided materials. This overcomes **"Convergence Bias,"** where models focused only on primary anchors. See [Universal Coverage](../../../../llm_interaction_patterns/artifacts/patterns/universal_coverage.md) (Header Scanning, In-Context Examples, **Explicit Anchor Checklist**).
- **Default to Action**: To ensure the replacement loop isn't prematurely terminated, the inventory agent is instructed to **DEFAULT to `could_be_replaced: true`**. This prevents "Semantic Blockage" where a conservative model decision starves downstream research. See [Downstream Starvation Prevention](../../../../llm_interaction_patterns/artifacts/patterns/downstream_starvation_prevention.md).
- **Pedagogical Purpose extraction**: The agent is instructed to state the **general legal principle** rather than facts. This allows for modern replacements with different fact patterns.

### Step B: Targeted Finder (`case-replacement-finder`)
- **Input**: The JSON inventory of source cases and their pedagogical functions.
- **Process**: For each source case, the agent performs targeted search queries focused on the **pedagogical function** + modern year constraints (2015–2025).
- **Evaluation Criteria**:
    - **Year**: 2015 or later is mandatory.
    - **Engagement**: Compelling, discussable fact patterns (e.g., social media, gig economy, modern forensics).
    - **Hierarchy**: State Supreme Court or Federal Circuit Court opinions are prioritized for doctrinal stability.

## 3. Workflow Integration (January 2026 Refactor)
Following a requirement to prioritize curriculum replacement volume over broad topic research, the Stage 2 architecture was pivoted to a "Precedent-Led" workflow in `gemini-revision.yaml`:

- **Stage 1 (Inventory)**: `extract-topics` → `verify-topics` → `refine-topics` → **`extract-case-inventory`**.
  - This ensures that before research begins, the system has a complete map of the legacy "anchors" that need replacing.
- **Stage 2 (Targeted Research)**: **`find-replacements`** → `refine-research` → `retrieve-documents`.
  - **Parallel Search Logic**: The user requirement for "running each source case in parallel" is addressed by feeding the aggregated `case-inventory` JSON into the `find-replacements` step.
  - **1-to-N Volume Targeting**: The finder retrieval retrieval is tuned for **3-12 modern candidates** for each single legacy precedent. This provides a diverse candidate menu (e.g., *Crumbley* 2024, *Zemek* 2023).
- **Reporting**: The `scripts/run_class.py` logic generates a **Full Replacement Options Report** in the Stage 2 `REVIEW.md`, allowing the professor to see the lineage of each modern recommendation.

## 4. Parallel Execution & Scaling
To satisfy the requirement of "multiple cases for each older case," the search strategy is designed to be exhaustive rather than filtering.
- **Scaling Requirement**: When a module contains many legacy cases, the finder runs for each case as a discrete pedagogical unit. 
- **Workflow Pattern**: The logic maps one `case-inventory` output (a list of N cases) to a high-volume research task.
- **Prompt Engineering for Volume**: To strictly enforce the 3-12 candidate requirement, use the **Trailing Placeholder** pattern. See [LLM Interaction Patterns: Structured Output Volume](../../../../llm_interaction_patterns/artifacts/patterns/structured_output_volume.md).

## 5. Successful Legacy-to-Modern Mappings (Class 09: Omissions)
The following mappings were successfully generated and verified in the January 2026 validation run:

| Legacy Case (Old) | Modern Replacement Candidates (2015-2025) | Pedagogical Function |
| :--- | :--- | :--- |
| *People v. Beardsley* | *State v. Shell* (2023; 998 N.W.2d 597), *State v. Perea* (2020) | Duty based on special relationship |
| *Jones v. United States* | *The Crumbley Cases* (James and Jennifer Crumbley, 2024), *Commonwealth v. Carter* (2019) | Duty based on creating the peril / control |
| *Pope v. State* | *Nguyen v. State* (2025) | Scope of duty for bystanders/third parties |

These results confirmed that the **Inventory & Replace** loop can effectively map obscure legacy headers to high-engagement modern precedents.

## 6. Distinction from General Research
Unlike the `case-researcher` (which searches by broad topic clusters), the Targeted Replacement workflow is **Precedent-Led**. It starts with a specific legacy anchor and aims to find its modern "successor" in the law.

## 7. Scaling for Multi-Anchor Workflows (The "Menu-to-Dish" Problem)
A key architectural principle is the **"Menu-to-Dish Selection Loop"**:
- **The Menu (Stage 2)**: The system automatically searches for ALL inventoried legacy cases and generates 3-12 candidates for EACH. This creates a high-volume selection menu.
- **The Selection (Review & Gate)**: The human reviewer inspects the Stage 2 `REVIEW.md` and selects which candidates from the menu should be "promoted" to the final casebook.
- **The Dish (Stage 3)**: Traditionally, Stage 3 focused on editing only the "selected" winner.

## 8. Batch Editing Mode (January 2026 Update)
To address the difficulty of reviewing cases via external URLs (which may be blocked or paywalled), the system was updated to support **Batch Editing Mode**:
- **All-in-One Processing**: Instead of requiring a human choice after Stage 2, the `research-refiner` passes **ALL** candidates through to Stage 3.
- **Sequential Refinement**: The `editing-agent` and `document-retriever` are configured to handle batches (18+ cases) using Gemini's long-context window.
- **Result**: The professor receives a Stage 3 `REVIEW.md` containing the fully edited, verbatim text for **every** candidate, allowing for a side-by-side "pedagogical taste test" without leaving the repository environment.
- **Pattern**: See [Batch Processing (llm_interaction_patterns)](../../../../llm_interaction_patterns/artifacts/patterns/llm/batch_processing.md).
