# LLM Interaction Patterns

This Knowledge Item documents reusable strategies for optimizing interactions with high-capability LLMs (specifically Gemini 1.5/3.0) within automated agentic workflows. It focuses on overcoming common model biases (convergence, landmark persistence) and ensuring stable data flow.

## Core Patterns

- **[Structured Output Volume](./patterns/structured_output_volume.md)**: Using "Trailing Placeholders" to force high-volume JSON results.
- **[Universal Coverage](./patterns/universal_coverage.md)**: Overcoming "Convergence Bias" in inventory and scanning tasks.
- **[Downstream Starvation Prevention](./patterns/downstream_starvation_prevention.md)**: Using "Default to Action" flags to prevent early-stage filtering from starving later stages.
- **[Diagnostic Verification](./patterns/diagnostic_verification.md)**: Techniques for identifying stale output and logical hangs in complex pipelines.
- **[Model-Based Evaluation Patterns](./patterns/llm/model_based_evaluation.md)**: Using "Blind Student" tests and misconception analysis to assess content quality.

## Architectural Context
These patterns are essential for any "Menu-to-Dish" choice architecture, where an LLM is first used to generate a broad set of options for human review before performing deep processing on a selected winner.
