# Antigravity Workflow Patterns

This document serves as the "Rosetta Stone" between the organization's master `cross-repo` principles and the specific operational paradigm of Antigravity and Gemini.

## 1. State Persistence & Resumption
**Cross-Repo Goal:** Never lose agent state if a session crashes.
**Antigravity Implementation:**
Do not write `PROGRESS.md` files to Git. Instead, use **UI Artifacts** (e.g., `task.md` and `implementation_plan.md`) combined with the auto-persisted **Conversation Brain Logs** (`~/.gemini/antigravity/brain/<id>/overview.txt`). This achieves exact state resumption natively within the IDE without polluting Git history.

## 2. Context Protection & Unblocking
**Cross-Repo Goal:** Isolate heavy development so it doesn't block or corrupt the main workflow (e.g., using `git worktree`).
**Antigravity Implementation:**
Use the **Delegation Principle**. Isolate via *compute* rather than Git branches. Heavy tasks must be abstracted into disposable Python scripts in `ag-exams/scripts/agents/` and fired off asynchronously. The conversational loop must never be blocked.

## 3. Agent Reliability & Orchestration
**Cross-Repo Goal:** Expect LLMs to fail; build circuit breakers and retries.
**Antigravity Implementation:**
Do not write brittle bash scripting loops for retries. Rely exclusively on **Temporal Workflows** combined with **Gemini Context Caching**. Temporal handles the automatic retries and state machines, while Gemini's massive token window safely digests the orchestration logs.

## 4. Hook Compliance
**Cross-Repo Goal:** Never bypass pre-commit hooks.
**Antigravity Implementation:**
Strict 1:1 match. If a hook fails, Antigravity treats the output as a programmatic remediation step and fixes the code natively before re-committing.

## 5. Iterative Review Loops (Critic & Editor)
**Cross-Repo Goal:** Prevent oscillation and "whack-a-mole" regressions by using discrete Critic and Editor agents, saving snapshots to disk, and executing programmatic rollbacks when scores drop.
**Antigravity Implementation:**
Do not dump snapshots to a `temp/` directory. Expose the review cycle to the user via **UI Artifacts** (e.g., `draft_v1`, `draft_v2`). Use a **Temporal Workflow** to manage the deterministic loop. The Critic agent outputs structured JSON which Temporal evaluates. If regression is detected, Temporal routes Gemini back to the cached context of the highest-scoring artifact version.

## 6. Composable Workflows & Handoffs
**Cross-Repo Goal:** Prevent context window exhaustion by aggressively summarizing context and passing structured JSON handoffs (task, context, constraints, escalation) between sub-agents.
**Antigravity Implementation:**
This rule is **strictly maintained**. Despite Gemini's 2M token window, attention degradation is real. Do not dump entire conversation logs or massive codebases into sub-agent prompts. You must adhere to the **Atomic Agent Principle**: aggressively summarize context, curate the payload, and use strict JSON handoffs between the Temporal orchestration layer and the Gemini API.

## 7. Cross-Repo Swarms & Agent Messaging
**Cross-Repo Goal:** Coordinate agents across multiple sibling repositories using GitHub Issues with correlation IDs (`msg-{from}-{to}-{timestamp}`) and bash-based fan-out/fan-in loops.
**Antigravity Implementation:**
Do not use GitHub Issues as a message bus or bash scripts for fan-out. Use **Temporal Child Workflows and Signals**. The master Temporal orchestrator fans out asynchronous Child Workflows for each repository. Cross-agent communication happens instantly via Temporal Signals. The final aggregated state is rendered into a single **UI Artifact** (e.g., `swarm_report.md`) in the IDE.

## 8. Fact-Checking & Quote Verification
**Cross-Repo Goal:** Use a tiered lookup pipeline (Zotero local -> cite-assist -> CourtListener -> discovery) combined with vocabulary verification to prevent LLM hallucinations, logging results to a `.jsonl` file.
**Antigravity Implementation:**
The tiered lookup logic must be encapsulated in pure Python as a **Temporal Workflow**. Instead of generating terminal output and background `.jsonl` logs, the workflow surfaces potential fabrications and exact fuzzy-match diffs natively in a `verification_report.md` **UI Artifact**. The user clicks to accept/reject fixes directly in the IDE editor.

## 9. Deep Research & Human-in-the-Loop Gates
**Cross-Repo Goal:** Pause deep research workflows to get human approval on the research plan via CLI prompts or Telegram bots before committing budget/time to the search.
**Antigravity Implementation:**
Replace external notification channels with **IDE Native State**. The agent writes the proposed plan into a `research_plan.md` **UI Artifact**. The Temporal workflow hits a `wait_condition` bound to the artifact's state. The user edits or approves the markdown file directly in the IDE, which seamlessly unblocks the Temporal workflow to proceed.

## 10. Parallel Projects & Workspace Isolation
**Cross-Repo Goal:** Use `git worktree` for every new task so multiple CLI agents don't fight over `.git/index.lock` or interleave staging areas.
**Antigravity Implementation:**
Antigravity does not rely on concurrent CLI agents. The user interacts with a single Antigravity instance. For parallel file mutations, Antigravity generates isolated **Draft Artifacts** in memory/UI. Changes are only applied to the main Git working tree upon explicit user approval, eliminating Git lock conflicts entirely without the overhead of physical worktrees.

## 11. GitHub PRs & Labeling
**Cross-Repo Goal:** Standardize Git history via semantic commit types, mandatory labels (`enhancement`, `bug`, `agent-message`), and squash merging via the `gh` CLI.
**Antigravity Implementation:**
Maintain the exact labeling schema and semantic commit standards, but execute them programmatically via a Python GitHub API client encapsulated in a **Temporal Activity**. Do not shell out to `gh` CLI. If a PR requires review or has failing CI checks, Antigravity updates a **UI Artifact** tracking the PR status, allowing the user to monitor and remediate without leaving the IDE.

## 12. Reasoning Quality & JSON Extraction
**Cross-Repo Goal:** Maximize LLM analytical quality by allowing models to reason in free-form Markdown, utilizing secondary "Extractor" scripts/agents for JSON parsing.
**Antigravity Implementation:**
This is a critical rule. **Never force a primary analytical agent (e.g., Gemini 3.1 Pro) to output complex JSON schemas.** Constraining the model's output to JSON significantly degrades substantive reasoning quality. Analytical agents must read and write pure **Markdown**. When the Temporal orchestration layer requires structured data (JSON), a separate, fast "Extractor" helper function or a lightweight model (e.g., `gemini-3.0-flash`) must be used to parse the Markdown artifact into JSON.