# Legal Research Agent Strategies

This document outlines standard strategies for agents tasked with finding primary and secondary legal authorities.

## 1. Clustered Searching
Research agents should receive topics grouped into search clusters. Using pre-generated queries for clusters reduces the number of high-level planning cycles and provides better coverage across a doctrinal domain.

## 2. Google Scholar Priority
For "Case Opinion" types, agents should prioritize [Google Scholar](https://scholar.google.com).
- **Goal**: Direct, open-access URLs for case law.
- **Polite Handling**: Use **Search Grounding** (see [Polite Retrieval](./polite_retrieval.md)) rather than `web_fetch` to avoid 429 blocks from the Scholar silo.

## 3. Source Diversity
Every legal research task should aim for a multi-dimensional view of the law:
- **Landmark Cases**: Establishing core doctrine.
- **Modern Applications**: Showing how law evolves in contemporary contexts.
- **Statutes**: Model Penal Code and state-level codifications.
- **Academic Commentary**: Law review articles for deeper pedagogical context and critical debate.

## 4. Recency Bias (2016-2026)
To ensure research results are relevant to contemporary developments and social contexts:
- **Search Constraint**: Mandatory requirement to find recent cases (2016-2026) for every core topic.
- **Selection Priority**: Prioritize cases from the last decade over older landmarks whenever they offer equivalent pedagogical clarity.
- **Overcoming Persistence**: Landmark cases often dominate LLM training data and search results. Agents must use explicit date-aware queries (e.g., `[topic] case 2024`) to bypass this retrieval bias.

## 5. Specialized Agent Architecture
For high-fidelity results across domains, favor specialized researchers over a single generalist:
- **Case Researcher**: Focused on date-aware judicial opinion queries.
- **Statute Researcher**: Focused on legislative frameworks and state codes.
- **Commentary Researcher**: Focused on scholarly analysis and treatises.
- **Parallelism**: Run these agents in parallel to ensure deep exploration before consolidation.

## 6. Volume Preservation (Consolidate, Don't Filter)
To support human decision-making and pedagogical variety, agents must preserve research volume.
- **Target**: **3-12 documents** of each specific type (Cases, Statutes, Articles).
- **No Early Filtering**: Refinement agents are forbidden from arbitrarily filtering results down to a single "winner." Duplicate removal is permitted, but distinct candidates must all be preserved in the final curated list.

## 7. Prompt Engineering for Volume Adherence
To ensure LLM agents respect the "3-12 documents" requirement when outputting structured data, use the **Trailing Placeholder** pattern.

- **Details**: See [LLM Interaction Patterns: Structured Output Volume](../../../../llm_interaction_patterns/artifacts/patterns/llm/structured_output_volume.md).
- **Performance Benchmark**: In production verification (Jan 2026), this pattern achieved a **1-to-6 retrieval ratio**, increasing structured JSON output volume by over 500% and providing the professor with a choice-rich curriculum menu.
