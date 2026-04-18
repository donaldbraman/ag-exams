# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-opus

**Q7.** Assume that, instead of intentional murder, Blake is charged with felony murder predicated on the underlying felony of drug distribution. Blake argues the felony-murder charge is barred by the merger doctrine. How should the court rule?

(a) The charge is not barred, because the felony of distributing narcotics has an independent collateral purpose distinct from causing physical injury to the victim. <!-- correct -->
(b) The charge is barred, because the confrontation immediately preceding the shooting was an assaultive act that legally merges with the resulting homicide.
(c) The charge is not barred, because the merger doctrine only applies to strict liability offenses and cannot be invoked when an intentional felony is charged.
(d) The charge is barred, because drug distribution is a non-violent property offense that lacks the inherent dangerousness required to support a felony murder charge.
(e) The charge is not barred, because any underlying felony committed with a deadly weapon automatically escapes the merger doctrine's legal limitations.

**Answer:** (a)

**Explanation:** The merger doctrine (or independent felony rule) prevents the application of felony murder when the underlying felony is assaultive in nature and integral to the homicide (e.g., aggravated assault). However, if the felony has an independent collateral purpose—such as robbery, rape, or drug distribution—it does not merge and can serve as a valid predicate for felony murder. (b) is wrong because the predicate felony is the drug distribution, not the immediate assaultive confrontation. (c) is wrong because the merger doctrine regularly applies to intentional assaultive felonies. (d) is wrong because drug distribution is widely recognized as inherently dangerous and serves as a valid predicate for felony murder in many jurisdictions. (e) is wrong because using a deadly weapon during an assault does not prevent the assault from merging with the homicide.

**Tags:** chapters: [14], topics: [merger-independent-purpose], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14 (Felony Murder and Misdemeanor Manslaughter) - The merger doctrine and independent collateral purpose exception.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student would select this by correctly identifying the independent collateral purpose doctrine (the Ireland rule limits). The merger doctrine bars felony murder only when the underlying felony is an integral part of the homicide (e.g., an assault). Drug distribution has an independent felonious purpose (distributing narcotics/financial gain) distinct from causing physical injury, so it does not merge.
(b) Argument-for: A student could focus on the actus reus that actually caused the death: the "confrontation immediately preceding the shooting." Because this immediate act is assaultive, the student might argue the merger doctrine is triggered by the proximate cause of death, thereby severing the drug distribution from the homicide and barring the charge because the immediate assault merges.
(c) Argument-for: A student might view the merger doctrine as a specific check against the strict liability nature of felony murder. Under this view, they could argue that if a defendant commits an "intentional" felony, the law intends to punish them fully, meaning merger "only applies to strict liability offenses" where the defendant lacked intent to commit a dangerous crime.
(d) Argument-for: To support felony murder, the predicate offense must be inherently dangerous. A student could misclassify drug distribution as purely a "non-violent property offense" or regulatory violation that lacks inherent danger in the abstract, arguing that it therefore cannot legally support a felony murder charge under any circumstance.
(e) Argument-for: A student might conflate the "deadly weapon doctrine" (where use of a deadly weapon infers malice aforethought) with an exception to the merger doctrine. They could argue that the presence of a deadly weapon "automatically escapes" merger because the weapon itself provides the requisite malice for murder, rendering the independent felony requirement moot.

Head-to-head: Option (a) perfectly states the independent collateral purpose exception to the merger doctrine. Options (c), (d), and (e) present explicitly false legal rules locked by absolute phrasing or stark misclassifications ("only applies," "property offense," "automatically escapes"). Option (b) states a false legal rationale (that an assaultive confrontation preceding a shooting bars a charge predicated on a *different* felony) but lacks an absolute word locking the false premise. To fully eliminate ambiguity about whether the immediate assault "legally merges" in the abstract, (b) should use absolute phrasing to definitively assert that the immediate assault extinguishes *all* predicate felonies. 

Falsifiable claim per distractor:
- (b): "the confrontation immediately preceding the shooting was an assaultive act that legally merges" — wrong because the merger analysis looks at the charged predicate felony (drug distribution), not the specific assaultive acts causing death, though the phrasing lacks an absolute lock.
- (c): "only applies to strict liability offenses" — wrong because the merger doctrine primarily and regularly applies to intentional crimes (e.g., intentional assault).
- (d): "drug distribution is a non-violent property offense" — wrong because drug distribution is a controlled substance offense (not a property offense) and is widely held to be inherently dangerous.
- (e): "automatically escapes the merger doctrine's legal limitations" — wrong because assault with a deadly weapon is the quintessential example of a felony that DOES merge.

Recommended fix: Edit (b) to lock the false legal claim with an absolute word.
Change (b) to: "The charge is barred, because any assaultive confrontation immediately preceding a shooting categorically merges with the resulting homicide, extinguishing the drug distribution predicate."
-->
