# Hallucination Guard: The 'Guard & Correct' Pattern

The 'Guard & Correct' pattern is a sequential refinement loop designed to ensure 100% verbatim accuracy in extractive legal editing, preventing the common LLM tendency to drift into paraphrasing or fabrication during summarization.

## 1. Pipeline Architecture
The pattern follows a three-step sequential workflow:
1. **Drafter (`edit-case`)**: Performs the initial editing/reduction of a full judicial opinion.
2. **Verifier (`verify-edits`)**: Conducts a sentence-by-sentence audit of the draft against the original full text.
3. **Refiner (`refine-edits`)**: Surgically corrects any sentences flagged as "Not Verbatim" or "Fabricated" by the verifier.

## 2. Agent Responsibilities

### Step A: Verifier (`editing-verifier`)
The verifier does not edit text. It only audits.
- **Input**: `{original_text}`, `{draft_edit}`.
- **Output**: A structured report identifying every sentence in the draft that cannot be found verbatim in the source.
- **Critical Check**: It flags "Semantic Drift" (where the model summarizes a judge's reasoning instead of quoting it) and "Out-of-Distribution Facts" (hallucinated details like sentencing or procedural dates not in the provided text).

### Step B: Refiner (`editing-refiner`)
The refiner takes the verification report and "repairs" the draft.
- **Input**: `{original_text}`, `{draft_edit}`, `{verification_report}`.
- **Instruction**: "Using the verification report, identify every hallucinated or paraphrased sentence. Replace it with the exact verbatim equivalent from the `original_text` or remove it if no verbatim equivalent exists."
- **Goal**: To preserve the "Judge's Voice" while maintaining the target word count.

## 3. Tool & Data Binding
- **Verbatim Standard**: The loop enforces that for primary case studies, students must read "the court's own words."
- **Workflow Binding**: The `multi` orchestration engine handles the data handoff. It is critical that the Drafter, Verifier, and Refiner use explicit `{placeholders}` for inputs to avoid Gemini "ambiguity pauses" (where the model asks for missing context).

## 4. Verification Milestone (Jan 2026)
This pattern was definitively verified in the **Class 09 (Omissions)** module.
- **Success (Fabrication)**: The `editing-verifier` flagged a hallucinated sentencing detail (*Jones v. US*). The `editing-refiner` successfully removed the fabrication.
- **Success (Truncation)**: In the Class 09 run for *State v. Burris* (2024), the verifier caught a mid-sentence truncation ("Her argument is") that resulted from model output limits. This allowed for a diagnostic update to the refiner to ensure sentence completion.
- **Context**: This loop replaced the legacy "Zero-Trust" parallel voting mechanism with a more efficient "Generate & Self-Correct" model.
