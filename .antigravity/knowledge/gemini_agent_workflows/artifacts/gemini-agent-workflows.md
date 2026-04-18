# Composable Gemini Agent Workflows

**Version:** 1.0.0
**Applies to:** `ag-exams` (Gemini & Temporal Integration)

A methodology for building reliable AI agents, organized around one core insight:

> **Agent reliability is inversely proportional to task complexity. Keep jobs simple, short, and composable.**

The simpler and shorter an agent's job, the higher the probability it completes successfully and produces high-quality output. Every factor in this methodology either enforces that principle directly or provides the infrastructure to make it work.

This guide is tailored specifically to our **Gemini API** architecture orchestrated via **Temporal Workflows**, incorporating our lessons on context caching and deterministic fix loops.

## Quick Reference

| Part | Factor | One-liner |
|------|--------|-----------|
| **I. Core** | Decompose into small agents | One agent, one job — split on domain, permissions, and decision points |
| **II. Execution** | Context Caching | Cache large static assets (Maps, Statutes) at the top; append dynamic events at the bottom. |
| | Curate your context | Summarize and select — never dump raw history |
| | Feed errors back | Self-correct by changing input; escalate if stuck |
| | Test your prompts and models | A/B test the combinations that matter most (e.g., `gemini-3.1-pro` vs `gemini-3-flash`) |
| **III. Composition** | Temporal Control Flow | Deterministic Temporal loop structure; LLM picks actions within it |
| | Launch/pause/resume | Temporal manages durable state, making agents inherently resumable |
| | Stateless architecture | No hidden state; same inputs → same behavior |
| | Handoff protocol | Pass task, context, constraints, and escalation path (e.g., `write_fix_guidance`) |

---

## Part I: The Core Principle

### Decompose into Small, Focused Agents

A complex task handled by one monolithic agent will fail in unpredictable ways. The same task decomposed into small, focused steps — each handled by a specialized agent — becomes reliable, testable, and debuggable.

**Decompose** complex workflows into smaller, logical units. **Specialize** each agent in a single domain. **Compose** smaller agents to accomplish complex tasks — orchestration is handled by deterministic code (like our Temporal workflow), not by any single agent trying to manage the whole workflow internally.

#### Where to draw the lines

- **Split by domain.** Data retrieval, data transformation, and output formatting are separate agents. An agent that writes an exam question should not also grade it.
- **Split by permission boundary.** Read-only operations and write operations belong to different agents.
- **Split at human decision points.** Any step that might need human approval (e.g., Temporal wait conditions) is a natural boundary. 

#### Composition patterns

| Pattern | When to use | ag-exams Example |
|---------|-------------|------------------|
| **Sequential (pipeline)** | Each step's output feeds the next | `Architect` → `Critic` |
| **Parallel (fan-out)** | Independent subtasks | `asyncio.gather` for Grounding, Ambiguity, Edge-Case, and Argument Passes |
| **Iterative (loop)** | Repeat until a quality threshold is met | `FIX_LOOP_CAP` regeneration loop |

---

## Part II: Executing Each Step Well

### Context Caching & Curriculum Management

With Gemini, context management is not just about token limits—it's about **latency and cost**.

**The Static/Dynamic Split:**
Place large, unchanging context (like Chapter Maps, Statutes, or systemic instructions) at the absolute top of the prompt. Use Gemini's `diskcache` or native Context Caching API to pre-warm this static layer. Append dynamic context (like the specific question text or the current critic feedback) at the bottom.

### Curate Your Context Window

Output quality degrades well before you hit the context limit. If your agent requires a massive dynamic context, it's probably doing too much in one step.

For orchestrators: treat the dynamic context window as a limited cache. Include only what is directly relevant to the current step. After each step, produce a summary of what happened.

**Before (Raw History):**
Dumping all 10 rounds of Architect/Critic debate into the final Question Writer prompt.
**After (Curated Summary):**
The Critic agent outputs a converged, minimized JSON `scenario_package` containing only accepted stubs and final facts, which is passed cleanly to the Writer.

### Feed Errors Back as Context

When an agent fails, add a concise, descriptive error summary back into the agent's context. In `ag-exams`, this is handled by compiling the outputs of the QA fan-out into a `qNN-fix-guidance.md` file, which is then explicitly fed back to the `question_writer` on the next iteration.

---

## Part III: Making Agents Composable

### Own Your Control Flow (Temporal Workflows)

The loop structure, break conditions, and guard rails are deterministic code. The LLM decides the next action *within those constraints*.

In `ag-exams`, **Temporal** owns the control flow. The `BuildFinalExam` workflow explicitly manages the `while` loops, tracking iteration counts (`FIX_LOOP_CAP`), aggregating parallel activity results, and determining convergence. The LLM never writes the orchestration loop itself.

### Launch, Pause, and Resume

An agent's lifecycle must be controllable through simple, explicit API calls. Break work into discrete, resumable steps instead of a single monolithic execution block.

Because we use Temporal, our workflows are durable. If the worker crashes mid-generation, Temporal pauses execution and resumes exactly where it left off, recovering the JSON state and avoiding redundant API calls.

### Stateless Architecture

Design each agent so that its behavior is fully determined by its inputs — the current state and the new event. No internal, hidden state between invocations.

Given the same state and event, the agent will follow the same logic. This is why our Temporal Activities simply take primitive arguments (`q_text`, `scenario_package`), call `dispatch_gemini()`, and return strings. No Python class state is mutated during the prompt execution.

### Handoff Protocol

When one agent passes work to another, send a structured handoff.
In `ag-exams`, our `fix_guidance` is a perfect example of a handoff protocol from the QA agents back to the Writer agent:

```markdown
# Fix Guidance for q01
The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below.

## Issue 1 — edge-case
<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The phrase "only key" triggers impossibility...
-->
```

---

## Part IV: Gemini-Native Best Practices

### The "Extractor Agent" Pattern (Markdown vs. JSON)

LLMs think autoregressively and reason best when allowed to "think out loud" in plain text. Forcing a model to generate a strict JSON schema during a complex reasoning task severely degrades output quality, as the model's "attention" is split between solving the problem and adhering to syntax rules.

**The Golden Rule:**
* **LLMs read Markdown. Code reads JSON.**
* If an agent is handing off context to another agent, use plain text/Markdown.
* If deterministic code needs structured state, **use the Extractor Pattern.**

**The Extractor Pattern:**
Do not force your deep-reasoning agent to output JSON. Instead, decompose the task:
1. **The Reasoner:** An agent (using `gemini-3.1-pro`) analyzes the problem and outputs pure Markdown.
2. **The Extractor:** A simple, fast agent (using `gemini-3-flash`) takes the Markdown output and uses Gemini's native `response_schema` to map the conclusions into strict JSON for the code to read. 

This perfectly embodies the "One agent, one job" principle—separating the domain of "reasoning" from the domain of "data formatting."

### Model Tiering

Aggressively split work between model tiers based on the task:
- **`gemini-3-flash`**: Use for high-volume, structural, formatting, routing, or extraction tasks (like the Extractor Agent pattern above, or simple structural linting).
- **`gemini-3.1-pro`**: Reserve exclusively for deep reasoning, complex content generation (like drafting exam questions), and critical audits (like the Edge-Case Auditor). Drafting requires immense nuance to synthesize rules without accidentally creating ambiguity, so the highest-tier model is required.

### Native Structured Outputs

When you *do* use the Extractor Agent, never rely on prompt engineering ("Please return only valid JSON"). Use Gemini's native `response_schema` feature with `response_mime_type="application/json"`. This guarantees the Temporal workflow will receive a payload that parses perfectly every time, eliminating the need for arbitrary JSON-fixing retry loops.

---

*Compose small, focused agents into reliable workflows.*
