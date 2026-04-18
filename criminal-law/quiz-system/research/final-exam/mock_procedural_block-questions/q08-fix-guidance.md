# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q8.** DA Miller defends her peremptory strikes of the Black jurors by arguing that residents of high drug-crime neighborhoods are inherently biased against police testimony. How does this justification function within the *Batson* framework?

(a) It will likely be rejected at step three, because using a neighborhood demographic as a blanket proxy for bias without individual inquiry strongly indicates pretext for racial discrimination. <!-- correct -->
(b) It will strictly fail at step one, because the defense attorney has already proven that the prosecutor possesses a documented history of explicitly racist charging decisions.
(c) It will automatically succeed at step two, because neighborhood residency is a geography-based metric that fully insulates the prosecutor from any further equal protection scrutiny.
(d) It will likely be rejected at step two, because prosecutors are legally required to provide justifications that are both race-neutral and demonstrably persuasive.
(e) It will automatically succeed at step three, because courts defer entirely to a prosecutor's subjective assessment of juror bias without reviewing underlying demographics.

**Answer:** (a)

**Explanation:** Under the *Batson* three-step framework, the prosecutor must offer a facially race-neutral reason at step two. A geographic reason is technically race-neutral, satisfying step two. However, at step three, the judge determines if there is purposeful discrimination. Using "high-crime neighborhood" as a blanket proxy for bias, especially without asking individual jurors about their views, is widely recognized by courts as pretext for racial discrimination. (b) is wrong because striking 100% of Black jurors clearly establishes the prima facie case at step one. (c) is wrong because geographic proxies do not insulate prosecutors from step-three scrutiny. (d) is wrong because step two only requires a facially neutral reason, not a persuasive one; persuasiveness is evaluated at step three. (e) is wrong because courts do not defer entirely; they are required to evaluate the genuineness of the explanation.

**Tags:** chapters: [4], topics: [batson-framework, equal-protection, peremptory-challenges], difficulty: intermediate, cognitive: analysis

**Grounding:** Chapter 4, Section: Jury Composition — Equal Protection and Batson

<!-- audit: SHOULD FIX
Check 1: pass
Check 2: pass
Check 3: The explanation for (b) hallucinates facts not found in the stem ("striking 100% of Black jurors") and completely ignores the actual text of option (b). Option (b) asserts facts about the prosecutor's charging history (which aren't in the stem) and misunderstands the framework (justifications are evaluated at Steps 2 and 3, not Step 1). 
Check 4: pass
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Update the explanation for (b) to read: "(b) is wrong because the prosecutor's justification is evaluated at Steps 2 and 3, not Step 1 (which only concerns the defendant's prima facie case). Furthermore, the stem introduces no facts regarding the prosecutor's past charging history."
-->
