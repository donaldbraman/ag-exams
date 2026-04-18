# write-assist Multi-LLM Writing Pipeline

The `write-assist` repository is a specialized application for legal academic writing (law review articles and casebooks) that uses an ensemble of Large Language Models (LLMs).

## Core Architecture: The 3-Phase Pipeline

The system employs three different LLMs—**Claude, Gemini, and ChatGPT**—in a tiered workflow:

1.  **Phase 1: DRAFTING (Parallel)**
    *   **Agents**: Three instances of the Drafter Agent (one per model).
    *   **Task**: Create initial drafts complete with research notes and Academic Bluebook citations.
    *   **Output**: 3 independent drafts.

2.  **Phase 2: EDITING (Parallel)**
    *   **Agents**: Three instances of the Editor Agent (one per model).
    *   **Task**: Review and integrate the 3 drafts from Phase 1 into a cohesive document.
    *   **Output**: 3 integrated drafts.

3.  **Phase 3: JUDGING (Parallel)**
    *   **Agents**: Three instances of the Judge Agent (one per model).
    *   **Task**: Rank the 3 integrated drafts and provide detailed explanations for the rankings.
    *   **Output**: 3 sets of rankings for human review.

## System Diagram

```
Phase 1: DRAFTING (parallel)     Phase 2: EDITING (parallel)     Phase 3: JUDGING (parallel)
┌─────────┐                      ┌─────────┐                      ┌─────────┐
│ Claude  │──┐                   │ Claude  │──┐                   │ Claude  │──┐
│ Drafter │  │                   │ Editor  │  │                   │ Judge   │  │
└─────────┘  │  3 Drafts         └─────────┘  │  3 Integrated     └─────────┘  │  3 Rankings
┌─────────┐  ├─────────────►     ┌─────────┐  ├─────────────►     ┌─────────┐  ├─────────►  Human
│ Gemini  │──┤                   │ Gemini  │──┤                   │ Gemini  │──┤            Review
│ Drafter │  │                   │ Editor  │  │                   │ Judge   │  │
└─────────┘  │                   └─────────┘  │                   └─────────┘  │
┌─────────┐  │                   ┌─────────┐  │                   ┌─────────┐  │
│ ChatGPT │──┘                   │ ChatGPT │──┘                   │ ChatGPT │──┘
│ Drafter │                      │ Editor  │                      │ Judge   │
└─────────┘                      └─────────┘                      └─────────┘
```
