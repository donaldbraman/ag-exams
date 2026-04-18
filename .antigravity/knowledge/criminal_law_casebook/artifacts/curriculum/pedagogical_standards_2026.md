# Pedagogical Standards for 2026 Casebook Revision

To ensure the Criminal Law casebook remains doctrinally sound, contemporary, and engaging for modern students, the Gemini-Only Revision System adheres to the following standards.

## 1. Mandatory Recency Bias (2016–2026)
While foundational landmark cases (e.g., *Beardsley*, *Lambert*) are essential for historical doctrine, the 2026 revision explicitly prioritizes cases decided within the last decade.
- **Objective**: To demonstrate how ancient legal principles (like Omissions or Mens Rea) are applied in modern social, technological, and institutional contexts.
- **Requirement**: Specialized research agents must prioritize cases from the 2016–2026 window. A landmark case should only be selected for the final text if a more recent case of equivalent pedagogical clarity is unavailable.
- **Volume of Recency**: The system is mandated to provide a choice-rich curriculum. For every legacy anchor case, the system must generate **3–12 modern successor candidates** (2015–2025). Single-case retrieval is considered a system failure. This was definitively verified in the Omissions module (Job `c4f130b0`), where the system successfully generated a diverse menu of 21st-century cases for legacy precedents.
- **Verification Example**: The success of the Class 09 (Omissions) module was defined by several high-fidelity outcomes:
    - **Modern Successor Retrieval**: In the broad topic search, the system successfully retrieved **_Norg v. City of Seattle_ (2023)** alongside classic doctrines.
    - **Precedent-Led Replacement**: In the targeted replacement loop, the system successfully inventoried **_Jones v. United States_ (1962)** and (following JSON volume tuning with trailing placeholders) proposed a high-volume candidate menu including **_People v. Crumbley_ (2024)**, **_People v. Zemek_ (2023)**, **_State v. Shell_ (2023)**, and **_Commonwealth v. Carter_ (2019)**. This achieved a **1-to-6 replacement ratio**, proving the effectiveness of the "Inventory & Replace" mechanism in generating choice-rich curriculum options.
- **Targeted Replacement Standard**: See the [Targeted Case Replacement Strategy](../implementation/case_replacement_strategy.md) for technical implementation.

## 2. Structural Diversity (The Tripartite Model)
Every module must be supported by three distinct types of primary and secondary authorities to provide a multi-dimensional view of the law:
1. **Case Law**: Focusing on contemporary fact patterns and judicial reasoning.
2. **Statutes & MPC**: Grounding the doctrine in the Model Penal Code and state-level codifications.
3. **Academic Commentary**: Including Law Review articles and treatises to provide critical pedagogical context and debate (e.g., philosophical justifications for the Good Samaritan doctrine).

## 3. Volume Preservation ("Consolidate, Don't Filter")
The revision pipeline is designed to serve as a high-fidelity "Research Assistant" for the professor, not a final arbiter.
- **Requirement**: Research agents are tasked with finding **3–12 documents per type** (e.g., 5 cases, 4 statutes, 6 articles).
- **Mandate**: The `research-refiner` must preserve this volume. It is explicitly forbidden from filtering the list down to a single "winner." 
- **Rationale**: Providing a range of options allows the human editor to select the specific case or article that best fits the planned classroom discussion or specific pedagogical nuances for that year.

## 4. Specialized Research Implementation
To overcome "Landmark Persistence" (the tendency of LLMs to return the same 5-10 classic cases found in their training data), the system uses **Specialized Researchers**:
- **Case Researcher**: Focused on date-aware queries for judicial opinions.
- **Statute Researcher**: Focused on legislative frameworks.
- **Commentary Researcher**: Focused on scholarly analysis.
- **Execution**: These agents run in parallel to ensure deep exploration of each domain before results are consolidated.

## 5. Extractive Editing Fidelity
To preserve the intellectual rigor of a law school casebook, the final output in Stage 3 follows an "Extractive, Not Summarized" mandate for judicial reasoning.
- **Requirement**: While the Facts and Procedural Posture are summarized for clarity, the "Reasoning" or "Opinion" section must consist of direct, verbatim excerpts from the judicial opinion.
- **Formatting**: Mandatory use of ellipses (...) to indicate where text has been omitted for brevity.
- **Pedagogical Goal**: Students must be able to "read the court's own words." Redacting a case into a third-person summary is considered a pedagogical failure for primary case studies, as it robs students of the opportunity to practice the skill of close textual analysis.

## 6. Automated Content Verification (Hallucination Guard)
Given the high stakes of legal pedagogical materials, the system must enforce a "Zero-Hallucination" standard for verbatim judicial reasoning.
- **Requirement**: All Stage 3 outputs must undergo a "Guard & Correct" loop.
- **Mechanism**: An automated `editing-verifier` performs a sentence-by-sentence verbatim audit against the retrieved full text.
- **Correction**: Any sentences flagged as non-verbatim (e.g., drifting into third-person summary or fabricating sentencing details) are surgically corrected by an `editing-refiner` agent before being presented for human review.
- **Standard**: The final output is only considered valid if it has passed this automated refinement pass, ensuring that students are never presented with fabricated judicial quotes.

## 7. Pedagogical Assessment (Quiz Quality)
To move beyond simple reading comprehension, the Casebook Revision System includes a dedicated assessment pipeline.
 
 - **High-Quality Distractor Mandate**: Multiple-choice questions must include distractors (incorrect answers) that are legally formal and plausible. Distractors are explicitly designed to test identified student misconceptions (the "Trap") and must avoid being easily eliminated by common sense.
 - **Complex Multi-Question Fact Patterns (Path B)**: While simple single-objective questions are supported, the preferred format is the **Complex Fact Pattern**. This involves a robust fictional foundation followed by a series of linked questions that test variations of the doctrine ("Assume instead that...") or intersections of multiple learning objectives.
 - **Retroactive Style Injection**: To increase engagement, fact patterns use hypothetical characters drawn from historical legal thinkers and theorists (e.g., Kant, Bentham, Mill) mentioned in the chapter's readings. This is performed retroactively after doctrinal validation to ensure stylistic polish does not interfere with logical rigor.
 - **Automated "Blind Student" Verification**: All generated questions must pass an automated "Turing Test." A fresh LLM instance (the Reviewer) is given the question without the answer key. A question is only considered high-quality if the Reviewer correctly identifies the answer while explicitly identifying and struggling with the plausibility of the distractors.
 - **Human-in-the-Loop "Topics" Gate**: Questions are never generated zero-shot. A professor must first review and approve a list of "Learning Objectives" and associated "Doctrinal Traps" before the drafting of questions begins. This ensures that the assessment aligns with the professor's specific classroom goals.
