# Quiz Development Pipeline Design

## Goal
To automate the creation of high-pedagogical-value quiz questions and distractors directly from casebook chapter content, moving beyond simple proofing of existing material.

## Architecture: The 4-Phase Human-in-the-Loop Pipeline

To ensure quality coverage and strong distractor generation, the pipeline is divided into distinct phases, keeping the professor in the loop at critical junctures.

### Phase 1: Learning Objective Extraction (The "Topics" Phase)
Before any questions are drafted, a specialized extraction agent maps the pedagogical landscape of the chapter.
- **Input**: A chapter file (e.g., `chapters/09-omissions.qmd`).
- **Process (Gemini 3.1)**: Analysis of the chapter text to identify core doctrines, statutory rules, and their application in anchor cases.
- **Output (The "Menu")**:
    *   **Learning Objective**: The specific rule or exception the student must master.
    *   **Anchor Case/Statute**: The primary authority demonstrating the rule.
    *   **The "Trap" (Target Misconception)**: The precise factual or doctrinal nuance where students most commonly misapply the rule (e.g., confusing moral vs. legal duties).
- **Human Review Gate**: The professor reviews this structured list to approve, merge, or delete topics before drafting begins.

### Phase 2: High-Volume Question Drafting
This phase utilizes the approved Learning Objectives to generate targeted material via two distinct paths:

- **Path A: Single-Objective Questions**: straightforward generation aimed at testing isolated concepts.
- **Path B: Complex Multi-Question Fact Patterns**: The preferred, more rigorous format. The LLM constructs a robust foundational hypothetical and then drafts multiple linked questions that test variations or intersections of multiple Learning Objectives.
    1.  **Foundation Generation**: The pipeline groups 2-4 related Learning Objectives from Phase 1. The LLM drafts a comprehensive, foundational fact pattern encompassing all included concepts (e.g., establishing both actus reus and mens rea in a single story).
    2.  **Linked Question Generation**: The LLM generates a series of questions based on that foundation:
        - **Question 1 (Core Application)**: Tests a primary objective against the base facts.
        - **Question 2 (Factual Modification)**: Introduces a twist ("Assume instead that..."). The LLM generates a new correct answer and tests distractors specific to how the rule shifts.
        - **Question 3 (Intersecting Doctrine)**: Tests a secondary objective present in the foundation (e.g., a defense potentially available under the base facts).
- **Process (Gemini 3.1 Flow)**:
    1.  **Lock-in Ground Truth**: For each question, the model states the unequivocally correct legal outcome and one-sentence doctrinal reasoning for it *before* generating distractors. This prevents logic-drifting.
    2.  **Adversarial Distractor Generation**: 
        - **Distractor 1 (The Trap)**: Explicitly tests the approved misconception from Phase 1.
        - **Distractor 2 (Plausible Alternative)**: A legally formal but inapplicable rule from a related area.
        - **Distractor 3 (The Factual Misread)**: Uses the correct rule but misapplies it to a specific fact.
- **Volume**: Over-generation (5x) to provide a rich menu for automated filtering.

### Phase 3: Automated Verification (The "Turing Test")
- **Goal**: Blind-testing to filter out weak or ambiguous questions.
- **Process**: A fresh "Evaluator Agent" instance (with answer keys hidden) attempts the quiz and outputs a Chain of Thought.
- **Acceptance Criteria (The "Goldilocks" Pass)**: The Evaluator identifies the correct answer but explicitly struggles with or eliminates a well-crafted distractor using precise doctrine (ideally falling for the "Trap" before self-correcting). 
- **Rejection Criteria**: 
    *   **Too Easy**: The Evaluator spots the answer instantly without engaging distractors.
    *   **Ambiguous**: The Evaluator finds multiple answers defensible or the logic flawed.

### Phase 4: Selection, Styling & Integration
- **Retroactive Character Polish (Style Injection)**: Before human review, generic names (e.g., "Defendant A") are replaced with historical thinkers or theorists (Kant, Bentham, Hart) drawn from the chapter's readings. This adds engagement without distracting the drafting agents from doctrinal rigor.
- **Human Review**: The professor selects the final "Dish" from the filtered "Menu."
- **Export**: Approved questions are formatted to local specifications (e.g., `quiz-system/` markdown).

## Tooling & Ecosystem Integration

### Models: Gemini 3.1 Preference
- **Gemini 3.x (e.g., `gemini-3-flash-preview`)** is preferred over 1.5 Pro for its superior "theory of mind" regarding how students misinterpret rules and its leap in logical reasoning.
- **Speed & Context**: Flash variants provide high speed for over-generation, while the 2M context window allows full-chapter context for every prompt.

### Orchestration & Verification
- **Orchestration**: Leverages the `multi` and `auth-utils` libraries for managing multi-step prompts and structured outputs.
- **Evaluation Patterns**: Incorporates the [Blind Student Test](../../llm_interaction_patterns/artifacts/patterns/llm/model_based_evaluation.md) for automated quality gating.

## Testing Quality Assumptions
- **Blind Student Reasoning Audit**: If reasoning for eliminating distractors is "structural" (e.g., "it's too simple") rather than "doctrinal," quality is insufficient.
- **Menu-to-Dish Over-generation**: Generating 10+ distractors and having a ranking prompt select the top 3.
