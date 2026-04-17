# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Assume Alex had a legal duty to call 911. How should a court evaluate whether his omission was the factual (but-for) cause of Blake's death?

(a) The omission did not cause the death, because an omission is a failure to act and therefore cannot serve as a factual legal cause.
(b) The omission did not cause the death, because the medical examiner's findings regarding hypothetical survival timelines are fundamentally too speculative for criminal causation.
(c) The omission was a factual cause of death, because the medical evidence establishes that Blake would have survived but for the 45-minute delay. <!-- correct -->
(d) The omission was a factual cause of death, because Alex's subjective panic provides the required mental state to establish direct proximate criminal causation.
(e) The omission was the sole proximate cause of death, completely superseding the initial shooting and absorbing all criminal liability for the entire incident.

**Answer:** (c)

**Explanation:** Factual causation requires showing that "but for" the defendant's conduct, the result would not have occurred. When evaluating omissions, courts apply a hypothetical counterfactual: if the defendant *had* performed the legal duty, would the harm have been averted? Here, the medical examiner explicitly concluded that "Blake would have survived if 911 had been called immediately" (Fact 12). Therefore, but for Alex's failure to call 911, Blake would not have died, establishing factual causation. Option (a) incorrectly claims omissions cannot be causal. Option (b) misstates the role of expert medical testimony, which is the standard method for establishing causation in delayed-treatment cases. Option (d) incorrectly blends mens rea (panic) with the actus reus element of factual causation. Option (e) is incorrect because an omission following a shooting does not absorb or supersede the liability for the shooting itself; both contribute to the causal chain.

**Tags:** chapters: [8, 9], topics: [causation, but-for-causation, omissions], difficulty: medium, cognitive: application

**Grounding:** Chapter 8 (Causation) and Chapter 9 (Omissions) - Factual cause applied to a failure to act.

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: Fails. The stem lacks the facts necessary to answer the question. The options and explanation reference a "45-minute delay," "medical evidence/Fact 12," and an "initial shooting" that are entirely absent from the provided stem. 
check 5: pass
check 6: pass
check 7: pass
Recommended fix: If this is a standalone question, incorporate the missing facts into the stem (e.g., "Assume Alex had a legal duty to call 911 after Blake was shot, but delayed for 45 minutes. A medical examiner concluded Blake would have survived if 911 had been called immediately..."). If this is attached to a master fact pattern, verify that these specific facts (including the 45-minute timeline and the medical examiner's conclusion) are explicitly included there.
-->
