# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Assume Leo is prosecuted for Wendy's death in a jurisdiction that has adopted California's SB 1437 reforms limiting felony murder liability for non-killers. What must the prosecution prove to convict Leo of felony murder, assuming he lacked intent to kill?

(a) That Leo's evasive driving was the direct factual and legal proximate cause of the police cruiser losing control and striking the pedestrian at the intersection.
(b) That Leo was a major participant in the underlying felony and that he acted with reckless indifference to human life during the high-speed pursuit. <!-- correct -->
(c) That the underlying felony of attempted commercial hijacking is strictly categorized as inherently dangerous in the abstract under the jurisdiction's statutory framework.
(d) That Leo subjectively foresaw the exact possibility that an innocent pedestrian could be fatally struck by a pursuing law enforcement vehicle during the escape.
(e) That the police officer's high-speed driving constituted a dependent intervening cause rather than an independent intervening cause that would sever Leo's legal liability.

**Answer:** (b)

**Explanation:** California's SB 1437 restricts felony murder for accomplices. To be convicted, an accomplice who is not the actual killer and lacks intent to kill must be a "major participant" who acts with "reckless indifference to human life." (b) is correct because this states the exact SB 1437 standard. (a) fails because proving proximate cause is insufficient under SB 1437; the statute specifically requires an elevated, individualized mens rea of reckless indifference. (c) fails because while an inherently dangerous felony is a prerequisite for felony murder, SB 1437 adds specific culpability requirements for non-killers. (d) fails because reckless indifference does not require foreseeing the exact manner of death, only a reckless disregard for the risk to human life generally. (e) fails because causation doctrine alone cannot satisfy SB 1437's statutory culpability requirement for accomplices.

**Tags:** chapters: [14, 18], topics: [felony murder, accomplice liability, sb-1437, major participant], difficulty: hard, cognitive: application

**Grounding:** Chapter 14: sb-1437-major-participant

<!-- audit: MUST FIX
Check 1: pass (legally accurate description of SB 1437 requirements for non-killers)
Check 2: pass (none of the distractors accurately reflect the SB 1437 standard)
Check 3: pass (explanation matches doctrine)
Check 4: FAILS. The stem completely omits the factual scenario that the options reference. The options discuss "Leo's evasive driving," a "police cruiser," a "pedestrian," a "high-speed pursuit," and an "attempted commercial hijacking," but none of these facts are established in the stem. A student will be confused about where these specific facts came from (likely a detached or deleted fact pattern).
Check 5: pass (jurisdiction is explicitly stipulated as adopting CA SB 1437)
Check 6: pass (no excluded topics)
Check 7: pass (SB 1437 is properly grounded in Ch 14/18 Refinement tags)
Recommended fix: Add the missing factual context to the stem (e.g., "Leo and an accomplice attempted a commercial hijacking. During their high-speed escape, Leo engaged in evasive driving, causing a pursuing police cruiser to lose control and strike Wendy, an innocent pedestrian."). Alternatively, remove the specific factual references from the options so it functions as a pure rule-based question.
-->

## Issue 2 — edge-case

**Q12.** Assume Leo is prosecuted for Wendy's death in a jurisdiction that has adopted California's SB 1437 reforms limiting felony murder liability for non-killers. What must the prosecution prove to convict Leo of felony murder, assuming he lacked intent to kill?

(a) That Leo's evasive driving was the direct factual and legal proximate cause of the police cruiser losing control and striking the pedestrian at the intersection.
(b) That Leo was a major participant in the underlying felony and that he acted with reckless indifference to human life during the high-speed pursuit. <!-- correct -->
(c) That the underlying felony of attempted commercial hijacking is strictly categorized as inherently dangerous in the abstract under the jurisdiction's statutory framework.
(d) That Leo subjectively foresaw the exact possibility that an innocent pedestrian could be fatally struck by a pursuing law enforcement vehicle during the escape.
(e) That the police officer's high-speed driving constituted a dependent intervening cause rather than an independent intervening cause that would sever Leo's legal liability.

**Answer:** (b)

**Explanation:** California's SB 1437 restricts felony murder for accomplices. To be convicted, an accomplice who is not the actual killer and lacks intent to kill must be a "major participant" who acts with "reckless indifference to human life." (b) is correct because this states the exact SB 1437 standard. (a) fails because proving proximate cause is insufficient under SB 1437; the statute specifically requires an elevated, individualized mens rea of reckless indifference. (c) fails because while an inherently dangerous felony is a prerequisite for felony murder, SB 1437 adds specific culpability requirements for non-killers. (d) fails because reckless indifference does not require foreseeing the exact manner of death, only a reckless disregard for the risk to human life generally. (e) fails because causation doctrine alone cannot satisfy SB 1437's statutory culpability requirement for accomplices.

**Tags:** chapters: [14, 18], topics: [felony murder, accomplice liability, sb-1437, major participant], difficulty: hard, cognitive: application

**Grounding:** Chapter 14: sb-1437-major-participant

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The police cruiser striking the pedestrian triggers the Agency vs. Proximate Cause split for Felony Murder. California (the namesake and standard-bearer for SB 1437 reforms) strictly applies the Agency Theory, meaning felony murder would be completely barred here because a co-felon did not commit the fatal act (California would use Provocative Act Murder instead). Asking students to apply felony murder to a police-killing scenario in a California-style jurisdiction creates a contradiction.
2. Cross-Doctrine Clashes: The Agency Theory of felony murder clashes with the premise that Leo can be convicted of felony murder for a police officer's fatal crash. 
3. Cross-Question Spoilers: The actual Q12 in the stub list tests proximate cause for this exact crash. Applying felony murder here requires a proximate cause jurisdiction, which conflicts with referencing California law without a caveat. (Also, note this question is mislabeled as Q12 in the text; it corresponds to Q13).
Recommended fix: Amend the prompt to explicitly instruct: "Assume the jurisdiction applies the proximate cause theory of felony murder, but has adopted California's SB 1437 reforms limiting liability for non-killers."
-->

## Issue 3 — argpass-sonnet

**Q12.** Assume Leo is prosecuted for Wendy's death in a jurisdiction that has adopted California's SB 1437 reforms limiting felony murder liability for non-killers. What must the prosecution prove to convict Leo of felony murder, assuming he lacked intent to kill?

(a) That Leo's evasive driving was the direct factual and legal proximate cause of the police cruiser losing control and striking the pedestrian at the intersection.
(b) That Leo was a major participant in the underlying felony and that he acted with reckless indifference to human life during the high-speed pursuit. <!-- correct -->
(c) That the underlying felony of attempted commercial hijacking is strictly categorized as inherently dangerous in the abstract under the jurisdiction's statutory framework.
(d) That Leo subjectively foresaw the exact possibility that an innocent pedestrian could be fatally struck by a pursuing law enforcement vehicle during the escape.
(e) That the police officer's high-speed driving constituted a dependent intervening cause rather than an independent intervening cause that would sever Leo's legal liability.

**Answer:** (b)

**Explanation:** California's SB 1437 restricts felony murder for accomplices. To be convicted, an accomplice who is not the actual killer and lacks intent to kill must be a "major participant" who acts with "reckless indifference to human life." (b) is correct because this states the exact SB 1437 standard. (a) fails because proving proximate cause is insufficient under SB 1437; the statute specifically requires an elevated, individualized mens rea of reckless indifference. (c) fails because while an inherently dangerous felony is a prerequisite for felony murder, SB 1437 adds specific culpability requirements for non-killers. (d) fails because reckless indifference does not require foreseeing the exact manner of death, only a reckless disregard for the risk to human life generally. (e) fails because causation doctrine alone cannot satisfy SB 1437's statutory culpability requirement for accomplices.

**Tags:** chapters: [14, 18], topics: [felony murder, accomplice liability, sb-1437, major participant], difficulty: hard, cognitive: application

**Grounding:** Chapter 14: sb-1437-major-participant

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that causation is a fundamental prerequisite for any homicide liability, including felony murder. Since the police cruiser actually struck the pedestrian, the prosecution absolutely must establish that Leo's evasive driving proximately caused the crash to impute the death to him. Because the option merely states that causation must be proved—a true legal requirement—without claiming it is the *only* requirement, it is technically a correct statement of a necessary element.
(b) Argument-for: A student could argue that California's SB 1437 restricts felony murder for non-killers to those who are "major participants" acting with "reckless indifference to human life." Because Leo is not the actual killer and the prompt stipulates he lacked the intent to kill, this statutory standard is the only available pathway for a felony murder conviction under these facts, making it exactly what the prosecution must prove.
(c) Argument-for: A student could argue that felony murder liability categorically requires the underlying offense to be an inherently dangerous felony (or an enumerated felony). Without proving that attempted commercial hijacking falls into this category, the felony murder rule cannot be invoked at all. Since the prompt asks what the prosecution "must prove," establishing the inherently dangerous nature of the felony is an indispensable foundational element.
(d) Argument-for: A student could argue that "reckless indifference" requires subjective awareness of the grave risk to human life created by one's actions. Given the specific factual matrix—a high-speed escape resulting in a police cruiser hitting a pedestrian—the prosecution must prove Leo subjectively foresaw the deadly risk his evasive driving posed.
(e) Argument-for: A student could argue that when a third party strikes the victim, the causal chain is highly contested. The prosecution must definitively prove that the officer's driving was a dependent intervening cause stemming naturally from Leo's flight, rather than an independent/superseding cause. Failing to prove dependent causation would result in acquittal, making it an essential element the prosecution "must prove."

Head-to-head: The keyed answer (b) accurately identifies the specific mens rea and actus reus requirements introduced by SB 1437. However, options (a), (c), and (e) are dangerously strong because they also describe foundational elements the prosecution "must prove" (causation, an inherently dangerous felony). Because the prompt simply asks what the prosecution "must prove to convict," any necessary foundational element is technically a correct answer unless the distractor claims to be the *sole* requirement. Options (a), (c), and (e) lack exclusionary language and therefore fail the close-call standard's rule against implicit omissions. Option (d) is safely falsifiable because of the word "exact."

Falsifiable claim per distractor:
- (a): None. Implicitly omits the SB 1437 requirements, but accurately states that proximate causation must be proved for a homicide conviction.
- (c): None. Implicitly omits the SB 1437 requirements, but accurately states that an inherently dangerous felony must be proved.
- (d): "subjectively foresaw the exact possibility" — wrong because reckless indifference requires subjective awareness of a grave risk to life generally, not foresight of the "exact" sequence of events.
- (e): None. Implicitly omits the SB 1437 requirements, but accurately states that the prosecution must prove the intervening cause was dependent to maintain liability.

Recommended fix: Add exclusionary language to distractors (a), (c), and (e) to make them explicitly false. For example, change (a) to "...proximate cause, which is solely sufficient to establish liability regardless of mens rea"; change (c) to "...categorized as inherently dangerous, which automatically satisfies the culpability requirement"; change (e) to "...dependent intervening cause, which categorically overrides the need to prove individualized reckless indifference."
-->

## Issue 4 — argpass-opus

**Q12.** Assume Leo is prosecuted for Wendy's death in a jurisdiction that has adopted California's SB 1437 reforms limiting felony murder liability for non-killers. What must the prosecution prove to convict Leo of felony murder, assuming he lacked intent to kill?

(a) That Leo's evasive driving was the direct factual and legal proximate cause of the police cruiser losing control and striking the pedestrian at the intersection.
(b) That Leo was a major participant in the underlying felony and that he acted with reckless indifference to human life during the high-speed pursuit. <!-- correct -->
(c) That the underlying felony of attempted commercial hijacking is strictly categorized as inherently dangerous in the abstract under the jurisdiction's statutory framework.
(d) That Leo subjectively foresaw the exact possibility that an innocent pedestrian could be fatally struck by a pursuing law enforcement vehicle during the escape.
(e) That the police officer's high-speed driving constituted a dependent intervening cause rather than an independent intervening cause that would sever Leo's legal liability.

**Answer:** (b)

**Explanation:** California's SB 1437 restricts felony murder for accomplices. To be convicted, an accomplice who is not the actual killer and lacks intent to kill must be a "major participant" who acts with "reckless indifference to human life." (b) is correct because this states the exact SB 1437 standard. (a) fails because proving proximate cause is insufficient under SB 1437; the statute specifically requires an elevated, individualized mens rea of reckless indifference. (c) fails because while an inherently dangerous felony is a prerequisite for felony murder, SB 1437 adds specific culpability requirements for non-killers. (d) fails because reckless indifference does not require foreseeing the exact manner of death, only a reckless disregard for the risk to human life generally. (e) fails because causation doctrine alone cannot satisfy SB 1437's statutory culpability requirement for accomplices.

**Tags:** chapters: [14, 18], topics: [felony murder, accomplice liability, sb-1437, major participant], difficulty: hard, cognitive: application

**Grounding:** Chapter 14: sb-1437-major-participant

<!-- argument-pass: MUST FIX
(a) Argument-for: To convict Leo of felony murder, the prosecution must establish factual and proximate causation. If Leo's evasive driving was not a cause of the death, he cannot be convicted of murder, regardless of SB 1437's mens rea reforms. Since establishing the causal chain is a necessary element of the offense, a student could argue the prosecution "must prove" it, making this option technically correct as a mandatory prerequisite for conviction.
(b) Argument-for: Under California's SB 1437 (Penal Code § 189(e)), an accomplice who is not the actual killer and did not act with the intent to kill can only be convicted of felony murder if they were a "major participant in the underlying felony" and acted "with reckless indifference to human life." Option (b) correctly identifies and quotes this exact statutory standard, directly answering the premise of the prompt's reference to SB 1437.
(c) Argument-for: Felony murder liability generally requires that the underlying felony be a qualifying offense, which is often one that is inherently dangerous. If a jurisdiction assesses this "in the abstract," the prosecution must establish this legal categorization to proceed with a felony murder theory. Proving the nature of the underlying felony is a mandatory prerequisite to conviction, making this an arguably correct answer to the broad question of what the prosecution "must prove."
(d) Argument-for: To establish the "reckless indifference to human life" standard required by SB 1437, the prosecution must show the defendant had a subjective awareness of the grave risk to human life. A student could argue that foreseeing the possibility of a fatal collision involving the police during a high-speed pursuit is the factual equivalent of proving this subjective recklessness in this specific scenario. Therefore, establishing this foresight is practically required to secure a conviction.
(e) Argument-for: In cases where a third party (here, a police officer) is the actual instrument of death, the prosecution must prove that the third party's actions did not break the chain of causation. Demonstrating that the officer's driving was a dependent intervening cause (a normal response to the defendant's fleeing) rather than an independent superseding one is a necessary element of proving proximate cause. Thus, a student could defend this as a true requirement for conviction under the prompt's broad phrasing.

Head-to-head: Option (b) correctly identifies the specific mens rea and participation requirements introduced by SB 1437. However, because the stem broadly asks "What must the prosecution prove to convict Leo...", any necessary element of the crime (causation, qualifying felony) is technically a correct answer unless it contains an explicitly false legal claim. Options (a), (c), and (e) describe general felony murder requirements and only fail due to highly pedantic misstatements of legal doctrine (e.g., claiming the driving must be the "direct" cause in (a), or strictly a "dependent" cause in (e)). Because students could successfully appeal that these distractors describe mandatory elements of the prosecution's case, the question's open-ended stem creates a severe multiple-key vulnerability.

Falsifiable claim per distractor:
- (a): "direct factual and legal proximate cause" — wrong because the police cruiser's involvement means Leo's driving was an indirect cause, and proximate causation does not require the defendant's conduct to be the "direct" factual cause.
- (c): "strictly categorized as inherently dangerous in the abstract" — wrong because many jurisdictions (including California under § 189) use enumerated felonies for first-degree felony murder without requiring an abstract inherent-danger analysis.
- (d): "subjectively foresaw the exact possibility" — wrong because reckless indifference requires subjective awareness of a grave risk to human life generally, not foresight of the precise sequence of events or exact manner of death.
- (e): "dependent intervening cause rather than an independent intervening cause" — wrong because an independent intervening cause does not automatically sever liability if it is objectively foreseeable; the prosecution does not strictly have to prove the cause was "dependent."

Recommended fix: Change the stem to specifically target the reform and exclude general elements: "Under California's SB 1437 reforms, what specific statutory culpability element must the prosecution establish to convict an accomplice like Leo of felony murder, assuming he lacked intent to kill?"
-->
