# Pattern: Downstream Starvation Prevention (Default to Action)

## Symptom
In a sequential pipeline (e.g., Inventory -> Research -> Edit), if an early agent (Inventory) makes a conservative or negative decision (e.g., "This case probably doesn't need replacement"), the downstream agents are "starved" of input. They may complete successfully (logic-wise) but produce zero output, making the entire pipeline appear ineffective.

## The Solution: Bias Towards Action
Instruct early-stage extraction or decision agents to **Default to YES** or **Include everything** unless there is a strictly defined exclusion criterion.

### Tactical Techniques

1. **The "Default True" Instruction**:
   - Instead of asking "Should this case be replaced?", instruct: "Mark `could_be_replaced: true` by default. Only set to `false` if the case is a globally recognized landmark (e.g., *Miranda v. Arizona*) that students must read in its original form."

2. **Semantic Blockage Avoidance**:
   - LLMs often interpret "replacement" as a heavy task and may try to "save work" by identifying fewer items. By framing it as a passive "default" state, you bypass this hidden work-saving heuristic.

3. **Broad Mapping**:
   - Ensure the output schema supports broad categories (e.g., `inventory_items[]`). If the list is empty, the subsequent `research-agent` will have no work to do.

## Proof of Effect
In Class 09 (Omissions) testing, the inventory agent initially flagged only *Jones v. United States* for replacement, missing *Beardsley* and *Pope*. By updating the prompt to **Force High Recall** and setting the **Replacement Default to True**, the pipeline successfully generated 18+ replacement candidates across all three cases.
