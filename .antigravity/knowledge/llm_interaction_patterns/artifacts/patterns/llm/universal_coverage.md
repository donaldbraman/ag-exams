# Pattern: Universal Coverage (Scan-to-EOF)

## Symptom
In inventorying or extraction tasks (e.g., "Identify every case in these notes"), LLMs often focus on the primary or most prominent anchor (Landmark cases) and miss secondary references. This **Convergence Bias** leads to under-inclusive data sets.

## The Solution: Explicit Scanning Mandates
To ensure 100% recall, the prompt must explicitly disable the model's "representative sample" heuristic.

### Tactical Techniques

1. **The Scan-to-EOF Directive**:
   - Instruct the model: "Continue searching until you reach the very end of the document. Do not stop after finding the most prominent examples."
   
2. **Implicit Cite Capture**:
   - Specifically instruct the model to look for cases mentioned by facts or holding description even if a formal Bluebook citation is missing.
   
3. **Header Scanning**:
   - Explicitly instruct the model to scan section headers and titles, as these are often where foundational cases are introduced without repetitive citations in the body.
   
4. **Negative Constraint**:
   - "Crucially: You are forbidden from choosing only a 'best' or 'representative' list. You must provide an exhaustive inventory."

5. **Targeted In-Context Examples**:
   - If the model repeatedly misses specific items during development, add those exact items to the prompt as examples of "what to find." This calibrates the model's "discovery threshold" for those specific types of entries (e.g., "Look for cases even in headers like *State v. X*").

6. **Threshold Recalibration (Temperature)**:
   - For extraction tasks where the model consistently misses items despite explicit instructions, increase the sampling temperature (e.g., to 0.4 or 0.5). A slightly higher temperature can help the model break out of high-confidence "early exits" and more thoroughly scan the context window.

7. **The Explicit Anchor Checklist**:
   - For high-value landmark cases or sections that *must* be identified, list them by name in the instruction (e.g., "Look for *Beardsley*, *Pope*, and *Jones*"). This provides a "Landmark Anchor" that helps the model orient its search and recalibrates its understanding of what constitutes a "valid" discovery in the specific document.

### Proof of Effect
In Class 09 verification, the baseline `case-inventory` agent initially missed *Beardsley* and *Pope* (prominent only in headers). 

Recall was restored to **100%** through a tiered application of:
1. **Header Scanning**: Instructing the model to treat section headers as valid case sources.
2. **Temperature Calibration**: Increasing sampling to **0.5** to prevent early termination of the context scan.
3. **Explicit Anchor Checklist**: Naming the "Big Three" (*Beardsley*, *Pope*, *Jones*) in the prompt instructions to calibrate the discovery threshold.
