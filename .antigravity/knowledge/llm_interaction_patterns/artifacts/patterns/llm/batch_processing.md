# Pattern: Batch Processing (Long-Context Parallelism)

## Symptom
In agentic pipelines, processing a list of items (e.g., 20 legal cases) by making individual sequential AI calls for each item is:
1. **Slow**: Total latency is the sum of all individual response times.
2. **Inconsistent**: The model may apply different stylistic or logical standards to item #1 than it does to item #20.
3. **Expensive**: Repeatedly sending the same system instructions and boilerplate for every item increases token overhead.

## The Solution: List-to-List Prompting
Leverage the large context window of a model like Gemini to process the entire list of items in a single turn.

### Tactical Techniques

1. **JSON Array Input**:
   - Provide the input as a structured JSON list.
   - Example: `[{"title": "Case A", "text": "..."}, {"title": "Case B", "text": "..."}]`

2. **Strict JSON Array Output**:
   - Instruct the model to return a single JSON object containing an array of processed results that matches the input length.
   - **Crucial Rule**: "Do not skip any items. Process all N inputs provided."

3. **Consistency Anchors**:
   - Including multiple items in one context allows the model to "see" the relative scale and style across the batch, leading to more uniform results (e.g., uniform lengths for edited summaries).

4. **Resource Management**:
   - Monitor the model's `max_output_tokens` limit. For very high-volume tasks (e.g., many full-context edits), ensure the model's response capacity can accommodate the entire batch.

## Proof of Effect
In the January 2026 refactor of the `criminal-law` revision system, the `editing-agent` was updated from a single-case processor to a **Batch Mode** processor. This allowed the system to generate edited versions of **ALL** 18 replacement candidates in a single pass, enabling immediate human review of the final "dishes" rather than just a "menu" of URLs.
