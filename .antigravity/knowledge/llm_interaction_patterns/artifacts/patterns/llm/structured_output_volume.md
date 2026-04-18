# Pattern: Structured Output Volume (Trailing Placeholders)

## Symptom
When asked to find a list of items (e.g., "Find 3-12 case replacements"), LLMs frequently converge on a single high-confidence result and stop. This happens because the model's "stop" token heuristic is triggered after the first valid JSON object is completed, even if the prompt requested more.

## The Solution: Visual "Trailing State" Cues
Use JSON examples that explicitly show continuation and multiple entries. This disrupts the single-object completion pattern.

### Tactical Techniques

1. **Ellipses in Examples**:
   - In the "Output Format" or "Example" section of the prompt, do not provide a closed list with 1-2 items. Provide 1 item followed by ellipses (`...`) inside the array.
   - **Example**:
     ```json
     {
       "results": [
         { "item_name": "Example 1", ... },
         { "item_name": "Example 2", ... },
         "..."
       ]
     }
     ```

2. **Explicit Item Range Mandate**:
   - Use bold emphasis: "Return strictly between **3 and 12** results."

3. **Landmark Checklists**:
   - List expected items to find as an anchor to prove the context window is large enough.

## Proof of Effect
Updating the `case-replacement-finder` and `case-researcher` with these visual cues increased the average candidate volume from **~1 to ~6 per legacy case**, providing a much higher-quality choice menu for the final research refiner.
