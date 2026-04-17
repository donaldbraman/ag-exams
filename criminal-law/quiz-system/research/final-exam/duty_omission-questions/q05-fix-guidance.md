# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Assume it is established that Blake owed Chris a duty of care. The prosecution charges Blake with attempted murder by omission for failing to call 911. Will this charge likely succeed?

(a) No, because attempt requires the specific intent or purpose to cause the prohibited result, and Blake acted out of terror rather than a purpose to kill Chris. <!-- correct -->
(b) No, because it is categorically impossible to commit an attempt crime through an act of omission under any legal circumstances.
(c) Yes, because Blake's deliberate failure to act constituted a direct and substantial step toward the commission of the offense.
(d) Yes, because Blake knew with practical certainty that his failure to call 911 would result in Chris's death.
(e) Yes, because the mental state for attempt automatically matches the extreme indifference standard of the underlying homicide.

**Answer:** (a)

**Explanation:** Attempt is a specific intent crime. To be guilty of attempted murder, the defendant must act with the purpose to cause death. Blake locked the door because of Alex's threat, not with the conscious object of killing Chris. (b) is wrong because omission liability can support an attempt charge if the duty and specific intent are present. (c) is wrong because it ignores the missing mens rea element entirely. (d) is wrong because attempt requires purpose, not mere knowledge or practical certainty. (e) is wrong because attempt mens rea does not match the underlying crime; it always elevates to specific intent/purpose.

**Tags:** chapters: [17], topics: [mens-rea-specific-intent, attempt], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, Attempt Mens Rea (Purpose)

<!-- audit: MUST FIX
check 1: pass (accurately states that attempt requires specific intent/purpose, not mere knowledge).
check 2: pass (distractors represent common doctrinal confusions, such as (d) testing knowledge vs. purpose).
check 3: fails (the explanation references completely absent facts, specifically "Blake locked the door because of Alex's threat").
check 4: fails (the question stem is missing the factual scenario entirely. It provides no information about Blake's mental state, Alex, or why Blake failed to call 911. Students cannot determine which option accurately applies the law because the underlying facts have been severed from the stem).
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Restore the missing fact pattern to the stem. Add the background facts explaining that Alex threatened Blake, which caused Blake to lock the door in terror and fail to call 911, thereby establishing that Blake lacked the purpose to kill Chris.
-->

## Issue 2 — argpass-sonnet

**Q5.** Assume it is established that Blake owed Chris a duty of care. The prosecution charges Blake with attempted murder by omission for failing to call 911. Will this charge likely succeed?

(a) No, because attempt requires the specific intent or purpose to cause the prohibited result, and Blake acted out of terror rather than a purpose to kill Chris. <!-- correct -->
(b) No, because it is categorically impossible to commit an attempt crime through an act of omission under any legal circumstances.
(c) Yes, because Blake's deliberate failure to act constituted a direct and substantial step toward the commission of the offense.
(d) Yes, because Blake knew with practical certainty that his failure to call 911 would result in Chris's death.
(e) Yes, because the mental state for attempt automatically matches the extreme indifference standard of the underlying homicide.

**Answer:** (a)

**Explanation:** Attempt is a specific intent crime. To be guilty of attempted murder, the defendant must act with the purpose to cause death. Blake locked the door because of Alex's threat, not with the conscious object of killing Chris. (b) is wrong because omission liability can support an attempt charge if the duty and specific intent are present. (c) is wrong because it ignores the missing mens rea element entirely. (d) is wrong because attempt requires purpose, not mere knowledge or practical certainty. (e) is wrong because attempt mens rea does not match the underlying crime; it always elevates to specific intent/purpose.

**Tags:** chapters: [17], topics: [mens-rea-specific-intent, attempt], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, Attempt Mens Rea (Purpose)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: To convict for attempt, the prosecution must prove the defendant acted with the specific intent or purpose to bring about the criminal result. Even if a defendant owes a legal duty and fails to act, they are not guilty of attempt unless they specifically desire the victim's death. Because Blake's inaction was motivated by terror of a third party rather than a conscious objective to kill Chris, the specific intent (purpose) element is missing, making a conviction unlikely.

(b) Argument-for: This option relies on a formalistic interpretation of the actus reus requirement for inchoate offenses. A student could argue that "attempt" requires a physical movement or an affirmative "act" toward the commission of a crime, which a mere omission (a failure to act) cannot satisfy. Under this view, while an omission can lead to liability for a completed crime if a duty exists, it is categorically impossible for a "failure to act" to meet the "substantial step" or "proximity" tests required for an attempt charge.

(c) Argument-for: Once a legal duty to act is established, a defendant's failure to perform that duty is the legal equivalent of an affirmative act. By deliberately choosing not to call 911 while Chris was in mortal danger, Blake took the final step necessary to allow the criminal result (death) to occur. In jurisdictions following the Model Penal Code, an omission that is strongly corroborative of a criminal end constitutes a substantial step, satisfying the conduct element of attempt.

(d) Argument-for: Under the Model Penal Code and various modern statutes, the line between "purpose" and "knowledge" is often blurred in result-oriented crimes. If Blake knew with "practical certainty" that his failure to act would lead to Chris's death, his state of mind is functionally equivalent to the intent to kill. A student might argue that for an attempt charge, knowing a result will occur with certainty is sufficient to satisfy the mens rea requirement, regardless of whether the defendant "desired" that result.

(e) Argument-for: This argument posits that the mens rea for an attempt should be coextensive with the mens rea for the completed version of the target offense. If the underlying crime of murder can be established through "extreme indifference to the value of human life" (depraved heart murder), it follows logically that an attempt to commit that crime should require the same level of culpability. Under this "matching" principle, Blake's extreme indifference to Chris's plight automatically satisfies the mental state requirement for attempted murder.

Head-to-head: Option (a) is the strongest because it correctly identifies that attempt is a specific-intent crime requiring "purpose," even when the underlying completed crime (murder) might only require knowledge or recklessness. This distinguishes it from (d) and (e). (b) is legally incorrect because omissions can support attempt charges if a duty and purpose are present. (c) fails because it treats the "substantial step" as the sole requirement for success, ignoring the necessity of specific intent. (d) is incorrect because "practical certainty" (knowledge) is insufficient for attempt, which requires "conscious object." (e) is incorrect because attempt mens rea does not "match" the underlying crime; it always requires purpose.

Falsifiable claim per distractor:
- (b): "categorically impossible... under any legal circumstances" — wrong because omission liability can support an attempt charge if a duty and specific intent are present.
- (c): "Yes, because Blake's deliberate failure to act constituted a direct and substantial step" — wrong because a "Yes" verdict requires both a substantial step AND specific intent; the step alone is insufficient for the charge to succeed.
- (d): "Yes, because Blake knew with practical certainty" — wrong because attempt requires specific intent (purpose), and knowledge of a practically certain result is a lower, insufficient mental state for an attempt charge.
- (e): "automatically matches the extreme indifference standard" — wrong because the mens rea for attempt does not follow the underlying crime; it must always be specific intent/purpose.

Recommended fix: Options (c) and (d) should be strengthened with absolute words to ensure they contain explicit false legal claims. For (c), change to: "Yes, because every deliberate failure to act while under a duty constitutes a direct and substantial step sufficient for an attempt conviction." For (d), change to: "Yes, because knowledge that a result is practically certain is always sufficient to satisfy the specific intent requirement of attempt."
-->

## Issue 3 — argpass-opus

**Q5.** Assume it is established that Blake owed Chris a duty of care. The prosecution charges Blake with attempted murder by omission for failing to call 911. Will this charge likely succeed?

(a) No, because attempt requires the specific intent or purpose to cause the prohibited result, and Blake acted out of terror rather than a purpose to kill Chris. <!-- correct -->
(b) No, because it is categorically impossible to commit an attempt crime through an act of omission under any legal circumstances.
(c) Yes, because Blake's deliberate failure to act constituted a direct and substantial step toward the commission of the offense.
(d) Yes, because Blake knew with practical certainty that his failure to call 911 would result in Chris's death.
(e) Yes, because the mental state for attempt automatically matches the extreme indifference standard of the underlying homicide.

**Answer:** (a)

**Explanation:** Attempt is a specific intent crime. To be guilty of attempted murder, the defendant must act with the purpose to cause death. Blake locked the door because of Alex's threat, not with the conscious object of killing Chris. (b) is wrong because omission liability can support an attempt charge if the duty and specific intent are present. (c) is wrong because it ignores the missing mens rea element entirely. (d) is wrong because attempt requires purpose, not mere knowledge or practical certainty. (e) is wrong because attempt mens rea does not match the underlying crime; it always elevates to specific intent/purpose.

**Tags:** chapters: [17], topics: [mens-rea-specific-intent, attempt], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, Attempt Mens Rea (Purpose)

<!-- argument-pass: MUST FIX
(a) Argument-for: Under common law doctrine, attempt is an inchoate offense that always requires the specific intent, or purpose, to cause the prohibited result. Because murder is a result crime, attempted murder requires the specific purpose to cause the victim's death. The facts indicate that Blake acted out of terror rather than a conscious object to bring about Chris's death. Since the specific intent requirement is not satisfied, the charge for attempted murder will fail.
(b) Argument-for: A student could argue that attempt requires an affirmative overt act—traditionally a "substantial step" or "dangerous proximity" to success. Because an omission is merely a failure to act, it inherently lacks the physical volition and affirmative trajectory necessary to constitute a step "toward" the commission of a crime. Therefore, the student would conclude that it is categorically impossible to commit an attempt crime through an act of omission under any legal circumstances.
(c) Argument-for: A student could argue that criminal omissions function as the legal equivalent of voluntary acts when a defendant owes a recognized duty of care. Because Blake owed Chris a duty, his deliberate decision not to intervene satisfied the actus reus requirements for attempt. By consciously failing to act, this omission served as a direct and substantial step toward the commission of murder. Consequently, a student could conclude the charge succeeds because the objective actus reus threshold was crossed.
(d) Argument-for: Under the Model Penal Code § 5.01(1)(b), an individual is guilty of attempt if they act with the "belief" that their conduct will cause the prohibited result without further conduct on their part. Knowledge to a practical certainty is the doctrinal equivalent of a "belief" that the result will occur. If Blake knew with practical certainty that his failure to call 911 would result in Chris's death, the mens rea for attempt is satisfied under the MPC. Therefore, this charge could successfully proceed.
(e) Argument-for: A student could argue that the mens rea for an attempt logically follows the mens rea of the completed target offense. If a defendant is charged with attempting a depraved-heart murder, which requires only extreme indifference to human life, the attempt must mirror that culpability standard. Under this framework, the mens rea for attempt automatically matches the extreme indifference standard of the underlying homicide, making Blake guilty if his omission was reckless enough.

Head-to-head: 
Option (a) correctly applies the common law specific intent requirement. However, (d) presents a massive issue: it correctly applies the Model Penal Code rule for attempt (§ 5.01(1)(b)), which permits attempt liability when a defendant acts with the "belief that it will cause such result." Since the prompt does not specify the jurisdiction (Common Law vs. MPC), (d) is legally defensible and potentially correct. Furthermore, option (c) relies entirely on an implicit omission; it does not contain a false legal claim, but rather falsely concludes "Yes" simply by analyzing the actus reus while ignoring the missing mens rea. This violates the close-call standard. Options (b) and (e) properly use absolute language to lock their false legal claims. 

Falsifiable claim per distractor:
- (b): "categorically impossible to commit an attempt crime through an act of omission under any legal circumstances" — wrong because attempts by omission are recognized if a duty and specific intent exist.
- (c): None. It relies on an implicit omission. The statement that the deliberate failure constituted a substantial step is arguably true, and it only fails because it ignores the mens rea analysis.
- (d): None. The claim that knowledge to a practical certainty justifies an attempt charge is a legally correct statement of the law under Model Penal Code § 5.01(1)(b).
- (e): "automatically matches the extreme indifference standard" — wrong because attempt always elevates the mens rea to specific intent/purpose, even if the underlying crime requires a lesser mental state like recklessness.

Recommended fix: Update (c) and (d) to include explicitly false, locked legal statements. 
Edit (c) to: "Yes, because establishing a substantial step automatically dictates attempt liability in every jurisdiction, regardless of the defendant's underlying mens rea."
Edit (d) to: "Yes, because attempt is a general intent crime, and proving mere criminal negligence is always sufficient to establish the mens rea for attempted murder."
-->
