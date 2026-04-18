# Composable Atomic Agent Principle

To combat context window degradation and attention loss in LLMs (even Gemini 3.1 Pro), **Antigravity must never build or rely on monolithic prompts.**

## 1. Single-Domain Scope
Agents must be atomized into single-domain workers. For example, instead of asking one agent to "write and audit and format" an exam question, you must dispatch three separate agents sequentially.

## 2. Stateless JSON Handoffs
Agents must communicate via strict JSON schemas passed through the orchestration layer (Temporal). Do not allow agents to free-write to each other without structure.

## 3. Strict Context Curating
Only pass the absolute minimum required data to an agent. If an agent is fact-checking Question 5, do not pass the raw text for Questions 1-4. Curate the payload at the orchestration layer before dispatching to `gemini_client.py`.
