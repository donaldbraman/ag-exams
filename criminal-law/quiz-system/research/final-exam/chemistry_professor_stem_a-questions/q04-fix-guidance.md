# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Can the prosecution establish that Arthur's omission—his failure to allow a 911 call—was the factual (but-for) cause of Julian's death?

(a) Yes, because the medical examiner established that Julian would have had a 95% chance of survival if Arthur had not prevented the 911 call and abandoned him. <!-- correct -->
(b) Yes, because Arthur's failure to call 911 was a concurrent sufficient cause that operates identically to the drug ingestion in establishing factual causation.
(c) No, because the acute cardiac arrhythmia was already fully in progress before Arthur failed to call 911, breaking the chronological causal chain.
(d) No, because the factual but-for test requires the defendant's omission to be the sole and exclusive cause of the harmful result.
(e) No, because Arthur's genuine but mistaken belief that Julian would recover negates the factual causal link between his omission and the resulting death.

**Answer:** (a)

**Explanation:** (a) is correct. Factual cause for an omission requires proving that but for the defendant's failure to act during the window when intervention could have saved the victim, the death would not have occurred. The ME's testimony that paramedics would have provided a 95% chance of survival easily satisfies this empirical requirement. (b) is incorrect because an omission to rescue is a necessary condition for the death in this scenario, not an independent concurrent sufficient cause (like two simultaneous fatal shots). (c) is incorrect because the chronological chain is not broken; the omission permitted an ongoing condition to become fatal when it could have been stopped. (d) is incorrect because the but-for test requires only that the defendant's conduct was necessary to the result, not the sole cause. (e) is incorrect because the defendant's subjective belief goes to mens rea, not to the empirical question of factual causation.

**Tags:** chapters: [8], topics: [causation, factual cause, but-for test], difficulty: easy, cognitive: application

**Grounding:** Chapter 8 - Factual Cause (But-For Test)

<!-- audit: MUST FIX
Check 1: Fails strictly on act vs. omission terminology. The question categorizes Arthur's conduct as an "omission" but then describes it as "failure to allow a 911 call" (stem) and "prevented the 911 call" (option a). Actively preventing someone from calling 911 or refusing to allow a call is an affirmative act of interference/seclusion, not an omission. This will cause cognitive friction for a well-prepared student who correctly identifies "preventing a call" as an act of commission. 
Check 2: Pass. Despite the terminology error, (a) remains the only empirically correct application of the but-for test among the choices.
Check 3: Pass. The explanation correctly maps the but-for counterfactual to the causal question, though it refers to "failure to act," further highlighting the terminology clash with option (a).
Check 4: Fails. The fact pattern (stem) is completely missing from the prompt text; it assumes a shared scenario but cannot be evaluated completely standalone.
Check 5: Pass. The empirical "but-for" counterfactual is jurisdictionally stable.
Check 6: Pass. No excluded-topic bleed.
Check 7: Pass. The but-for test and concurrent sufficient cause distractors are well-grounded in Chapter 8.
Recommended fix: Harmonize the act vs. omission phrasing to stick cleanly to an omission framework. Change the stem to: "...Arthur's omission—his failure to call 911—was..." and change option (a) to: "Yes, because the medical examiner established that Julian would have had a 95% chance of survival if Arthur had called 911 instead of abandoning him."
-->

## Issue 2 — edge-case

**Q4.** Can the prosecution establish that Arthur's omission—his failure to allow a 911 call—was the factual (but-for) cause of Julian's death?

(a) Yes, because the medical examiner established that Julian would have had a 95% chance of survival if Arthur had not prevented the 911 call and abandoned him. <!-- correct -->
(b) Yes, because Arthur's failure to call 911 was a concurrent sufficient cause that operates identically to the drug ingestion in establishing factual causation.
(c) No, because the acute cardiac arrhythmia was already fully in progress before Arthur failed to call 911, breaking the chronological causal chain.
(d) No, because the factual but-for test requires the defendant's omission to be the sole and exclusive cause of the harmful result.
(e) No, because Arthur's genuine but mistaken belief that Julian would recover negates the factual causal link between his omission and the resulting death.

**Answer:** (a)

**Explanation:** (a) is correct. Factual cause for an omission requires proving that but for the defendant's failure to act during the window when intervention could have saved the victim, the death would not have occurred. The ME's testimony that paramedics would have provided a 95% chance of survival easily satisfies this empirical requirement. (b) is incorrect because an omission to rescue is a necessary condition for the death in this scenario, not an independent concurrent sufficient cause (like two simultaneous fatal shots). (c) is incorrect because the chronological chain is not broken; the omission permitted an ongoing condition to become fatal when it could have been stopped. (d) is incorrect because the but-for test requires only that the defendant's conduct was necessary to the result, not the sole cause. (e) is incorrect because the defendant's subjective belief goes to mens rea, not to the empirical question of factual causation.

**Tags:** chapters: [8], topics: [causation, factual cause, but-for test], difficulty: easy, cognitive: application

**Grounding:** Chapter 8 - Factual Cause (But-For Test)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Mild clash - The prompt categorizes Arthur's conduct as an "omission—his failure to allow a 911 call." Actively knocking a phone out of someone's hand and locking a door to prevent rescue are affirmative acts (commissions), not omissions. A pure omission here would simply be his own failure to call 911. Blurring act and omission in the prompt could confuse students, particularly since Q3 specifically evaluates these affirmative acts for creating peril.
3. Cross-Question Spoilers: pass
Recommended fix: Change the prompt's phrasing from "omission—his failure to allow a 911 call" to simply "conduct" or "failure to call 911 and prevention of a rescue call".
-->
