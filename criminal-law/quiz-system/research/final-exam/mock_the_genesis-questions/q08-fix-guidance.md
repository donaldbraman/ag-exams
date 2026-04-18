# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q8.** Assuming proximate causation is satisfied, the prosecution is comparing felony murder and extreme indifference murder to determine the most viable path to convict Albert for Chloe's death. Which is the most viable path?

(a) Felony murder is the most viable path because the jurisdiction explicitly enumerates the manufacturing process, relieving the prosecution of proving a specific homicide mental state. <!-- correct -->
(b) Extreme indifference murder is the most viable path because the involuntary muscle spasm entirely negates the underlying felony requirement for the felony murder doctrine.
(c) Felony murder is the most viable path because all drug possession offenses automatically qualify for the doctrine regardless of specific statutory enumeration.
(d) Extreme indifference murder is the most viable path because felony murder cannot legally apply when a third party's negligence contributes directly to the death.
(e) Both paths are equally unviable because the subsequent medical malpractice fundamentally severs the causal chain required to secure any type of homicide conviction.

**Answer:** (a)

**Explanation:** (a) is correct. Because manufacturing Blue-X is explicitly enumerated as a qualifying felony in this jurisdiction, it strictly triggers the felony-murder rule, relieving the prosecution of the heavy burden of proving malice or extreme indifference. (b) is wrong because the time-framing doctrine preserves the voluntary act for the underlying felony despite the spasm. (c) is wrong because felony murder typically requires the felony to be either inherently dangerous or statutorily enumerated; not all drug offenses automatically qualify. (d) is wrong because proximate causation principles apply equally to felony murder; the ordinary medical negligence does not sever liability. (e) is wrong because ordinary medical malpractice does not sever the causal chain.

**Tags:** chapters: [12, 13, 14], topics: [homicide grading, felony murder, extreme indifference], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14, Enumerated Felony Murder

<!-- audit: MUST FIX
check 1: pass (Assuming the intended facts, the correct answer accurately applies enumerated felony murder doctrine to relieve the mens rea burden).
check 2: pass
check 3: pass
check 4: FAIL. The question is entirely missing its fact pattern. The stem and options refer to "Albert," "Chloe," a "manufacturing process" for "Blue-X", an "involuntary muscle spasm," and "subsequent medical malpractice" without ever introducing these facts. Students cannot answer the question without the scenario.
check 5: FAIL. Option (a) relies on the jurisdiction explicitly enumerating drug manufacturing as a felony murder predicate. Without a fact pattern establishing this jurisdictional rule, students cannot deduce that this is the correct path.
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Prepend the full fact pattern to the stem. The scenario must detail Albert's drug manufacturing, his involuntary muscle spasm, Chloe's resulting injury, the subsequent medical malpractice, and explicitly stipulate that the jurisdiction's felony murder statute enumerates the manufacturing of Blue-X.
-->

## Issue 2 — edge-case

**Q8.** Assuming proximate causation is satisfied, the prosecution is comparing felony murder and extreme indifference murder to determine the most viable path to convict Albert for Chloe's death. Which is the most viable path?

(a) Felony murder is the most viable path because the jurisdiction explicitly enumerates the manufacturing process, relieving the prosecution of proving a specific homicide mental state. <!-- correct -->
(b) Extreme indifference murder is the most viable path because the involuntary muscle spasm entirely negates the underlying felony requirement for the felony murder doctrine.
(c) Felony murder is the most viable path because all drug possession offenses automatically qualify for the doctrine regardless of specific statutory enumeration.
(d) Extreme indifference murder is the most viable path because felony murder cannot legally apply when a third party's negligence contributes directly to the death.
(e) Both paths are equally unviable because the subsequent medical malpractice fundamentally severs the causal chain required to secure any type of homicide conviction.

**Answer:** (a)

**Explanation:** (a) is correct. Because manufacturing Blue-X is explicitly enumerated as a qualifying felony in this jurisdiction, it strictly triggers the felony-murder rule, relieving the prosecution of the heavy burden of proving malice or extreme indifference. (b) is wrong because the time-framing doctrine preserves the voluntary act for the underlying felony despite the spasm. (c) is wrong because felony murder typically requires the felony to be either inherently dangerous or statutorily enumerated; not all drug offenses automatically qualify. (d) is wrong because proximate causation principles apply equally to felony murder; the ordinary medical negligence does not sever liability. (e) is wrong because ordinary medical malpractice does not sever the causal chain.

**Tags:** chapters: [12, 13, 14], topics: [homicide grading, felony murder, extreme indifference], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14, Enumerated Felony Murder

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The prompt explicitly tells students "Assuming proximate causation is satisfied," but option (e) asserts that "medical malpractice fundamentally severs the causal chain." This allows students to instantly eliminate (e) based on pure reading comprehension rather than doctrinal knowledge.
2. Cross-Doctrine Clashes: pass.
3. Cross-Question Spoilers: Q8's correct answer definitively establishes that felony murder is "the most viable path" because the manufacturing felony is explicitly enumerated. This heavily spoils Q9, which tests whether the independent felonious purpose (merger) doctrine blocks Blue-X manufacturing from serving as a valid felony murder predicate. 
Recommended fix: Add "Assuming the manufacturing offense is a valid predicate..." to the prompt to properly isolate Q9's issue. Completely replace options (d) and (e) with distractors focused on the muscle spasm or mens rea (e.g., arguing that extreme indifference requires a purposeful mental state, or that an involuntary spasm precludes strict liability) so they do not contradict the prompt's explicit causation assumptions.
-->
