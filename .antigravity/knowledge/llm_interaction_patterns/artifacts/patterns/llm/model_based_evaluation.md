# Pattern: Model-Based Evaluation & Quality Assessment

## Problem: The "Quality Ceiling" of Zero-Shot Generation
In automated content pipelines (e.g., quiz generation, doctrinal summaries), zero-shot generation often produces technically correct but pedantic or overly simple results. Misconceptions are ignored, and distractors are often too easy for even an uninitiated student to eliminate.

## The Solution: Adversarial and Diagnostic Evaluation Loops

### 1. The "Blind Student" Test (Diagnostic Verification)
This pattern validates the quality of a generated item (like a multiple-choice question) by forcing a fresh instance of a high-capability model to "take" the test.
- **Workflow**:
    1.  Provide the model with the source grounding material (e.g., a chapter) and the generated question.
    2.  Ask the model to solve the problem step-by-step.
    3.  **Crucial Element**: Require the model to justify why it eliminated every single distractor *before* confirming the correct answer.
- **Diagnostic Signal**: If the model's reasoning is "Option B is clearly absurd," the distractor is weak. If the model is genuinely "torn" between the correct answer and a distractor, the item is high-quality (or correctly identifies a subtle distinction).

### 2. The Distractor-Only Turing Test
This pattern evaluates whether distractors are distinguishable from human-authored errors based on structure or linguistic style.
- **Workflow**:
    1.  Strip out the correct answer from the generated item.
    2.  Ask a human (or an experienced model with "expert professor" framing) to review the remaining stem and options.
    3.  If the distractors lack the "legalese camouflage" or structural complexity of human-authored mistakes, the generation prompt should be refined to include specific phrasing constraints or stylistic markers.

### 3. Misconception-Driven Distractor Generation (Human-in-the-Loop)
Instead of asking an LLM to generate "3 distractors," first perform a **Learning Objective/Topics Analysis** that includes anticipated student errors.
- **Phase 1: Topics Extraction (Human Review)**: "Extract the core rules, case applications, and the 3 most likely ways a student would misapply this rule."
- **Phase 2: Human-in-the-Loop Gating**: The expert (e.g., a professor) reviews the extracted rules and misconceptions to ensure the pedagogical target is correct.
- **Phase 3: Targeted Generation**: "Generate distractors that stem *directly* from the approved misconceptions. Each distractor must be a plausible 'trap' for a student who holds that specific misconception."
    *   **Distractor Taxonomy**:
        *   **The Trap**: Tests the exact misconception identified (e.g., student confuses moral vs legal duty).
        *   **The Plausible Alternative**: A legally formal but inapplicable rule from a related area.
        *   **The Factual Misread**: Uses the correct rule but applies it incorrectly to a specific fact in the hypothetical.

### 4. Menu-to-Dish Over-Generation (Plausibility Ranking)
Follow the [Menu-to-Dish](./standalone_verification.md) pattern to leverage volume over prompt precision.
- **Workflow**:
    1.  Generate 10+ potential distractors for a single item.
    2.  Use a second model pass to rank the distractors by "Plausibility + Definitive Incorrectness."
    3.  Select the top 3 highest-rated candidates to form the final "Dish."

### 5. Retroactive Style Injection (Narrative Polish vs. Doctrinal Focus)
To keep specialized agents focused on logical rigor (e.g., doctrinal accuracy in law), separate the "drafting/verification" pass from the "narrative/thematic polish" pass.
- **Workflow**:
    1.  **Stage 1-3**: Generate fact patterns and distractors using generic placeholders (e.g., "Defendant A", "Situation B") to minimize distraction and context pollution.
    2.  **Verification**: Pass the generic draft through the [Evaluator Agent](#blind-student-test) to confirm logical soundness.
    3.  **Retroactive Polish**: Once verified, use a final "Stylist" agent to replace placeholders with thematic characters (e.g., historical thinkers, legal theorists) or specific narrative contexts.
- **Rationale**: This prevents "hallucination-by-narrative," where an LLM inadvertently alters legal outcomes or facts just to make a specific character reference or joke work more effectively. It ensures the "core" of the content is logically flawless before adding engagement-focused "skin."

## Rationale
Testing assumptions about quality is better achieved through adversarial and multi-pass "Reviewer" loops than through single-prompt optimization. By forcing the LLM to model the *failure state* (misconceptions) or represent a *consumer* of the content (the blind student), we increase the doctrinal depth and pedagogical value of the output.
