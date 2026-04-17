# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Is Alba guilty of the attempted murder of Dane?

(a) Guilty of attempted murder because striking a person in the head with a handgun demonstrates an extreme indifference to human life.
(b) Guilty of attempted murder because taking a substantial step toward incapacitation satisfies the general intent requirement for attempt.
(c) Not guilty of attempted murder because attempt requires the specific intent to kill, and Alba only intended to knock Dane unconscious. <!-- correct -->
(d) Not guilty of attempted murder because Dane was actually an off-duty paramedic, making the completion of the homicide legally impossible.
(e) Not guilty of attempted murder because Alba abandoned the effort to kill Dane by leaving him incapacitated on the floor.

**Answer:** (c)

**Explanation:** (c) is correct because attempt is a specific intent crime requiring the purpose to commit the target offense; since Alba intended only to incapacitate Dane, Alba lacked the specific intent to kill required for attempted murder. (a) is wrong because extreme indifference to human life (recklessness) is insufficient to support an attempted murder charge, which demands purpose. (b) is wrong because attempt is a specific intent crime, not a general intent crime. (d) is wrong because Dane's status as an off-duty paramedic is irrelevant to the doctrine of legal impossibility. (e) is wrong because abandonment requires complete and voluntary renunciation before the crime is completed, not merely leaving a victim incapacitated after an assault.

**Tags:** chapters: [17], topics: [attempt, mens rea, specific intent], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, mens-rea-specific-intent

<!-- audit: MUST FIX
Check 1: pass (Correctly maps to the doctrine that attempted murder requires specific intent/purpose to kill).
Check 2: pass (Distractors represent common doctrinal misunderstandings, such as attempting a reckless crime, and none are legally defensible).
Check 3: pass (Explanation accurately reflects the mens rea requirements for attempt).
Check 4: fails (The question stem lacks a fact pattern entirely. It asks "Is Alba guilty..." but relies on facts—striking with a handgun, intending only to knock unconscious, Dane being a paramedic—that only appear in the answer choices. A standalone question must provide these facts in the prompt).
Check 5: pass (The specific intent rule for attempted murder is standard across jurisdictions).
Check 6: pass (No excluded topics).
Check 7: pass (Properly grounded in Ch 17 `mens-rea-specific-intent`).
Recommended fix: Add the missing fact pattern to the stem (e.g., "Alba struck Dane, an off-duty paramedic, in the head with a handgun. Alba's sole intention was to knock Dane unconscious. After Dane fell to the floor, Alba left him incapacitated. Is Alba guilty of the attempted murder of Dane?"). If this is a sub-question tied to a master scenario, verify the master stem explicitly states Alba's limited intent.
-->

## Issue 2 — argpass-opus

**Q5.** Is Alba guilty of the attempted murder of Dane?

(a) Guilty of attempted murder because striking a person in the head with a handgun demonstrates an extreme indifference to human life.
(b) Guilty of attempted murder because taking a substantial step toward incapacitation satisfies the general intent requirement for attempt.
(c) Not guilty of attempted murder because attempt requires the specific intent to kill, and Alba only intended to knock Dane unconscious. <!-- correct -->
(d) Not guilty of attempted murder because Dane was actually an off-duty paramedic, making the completion of the homicide legally impossible.
(e) Not guilty of attempted murder because Alba abandoned the effort to kill Dane by leaving him incapacitated on the floor.

**Answer:** (c)

**Explanation:** (c) is correct because attempt is a specific intent crime requiring the purpose to commit the target offense; since Alba intended only to incapacitate Dane, Alba lacked the specific intent to kill required for attempted murder. (a) is wrong because extreme indifference to human life (recklessness) is insufficient to support an attempted murder charge, which demands purpose. (b) is wrong because attempt is a specific intent crime, not a general intent crime. (d) is wrong because Dane's status as an off-duty paramedic is irrelevant to the doctrine of legal impossibility. (e) is wrong because abandonment requires complete and voluntary renunciation before the crime is completed, not merely leaving a victim incapacitated after an assault.

**Tags:** chapters: [17], topics: [attempt, mens rea, specific intent], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, mens-rea-specific-intent

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that because "depraved heart" or extreme indifference to human life is a sufficient mens rea for completed murder, it should also suffice for attempted murder. Striking someone in the head with a handgun objectively demonstrates this extreme recklessness. If a jurisdiction were to mirror the mens rea of the completed crime in its attempt counterpart, establishing extreme indifference would logically lead to a guilty verdict for attempted murder.
(b) Argument-for: A student might argue that attempt simply requires a substantial step toward a criminal act, which they might confuse as a general intent requirement. Since Alba took a substantial step by incapacitating Dane, she fulfilled the actus reus. If the student incorrectly believes attempt inherits the general intent of lesser-included offenses like battery, they would conclude this satisfies the attempt standard for the overarching conflict.
(c) Argument-for: Attempt is universally recognized as a specific intent crime, even when the target offense (like murder) can be committed with a lower mens rea (such as recklessness). To be guilty of attempted murder, the defendant must act with the specific intent or purpose to cause death. Because Alba only intended to knock Dane unconscious, she lacked the requisite purpose to kill, making her unequivocally not guilty of attempted murder.
(d) Argument-for: Legal impossibility occurs when a defendant's intended acts would not constitute a crime even if fully completed. A student might bizarrely reason that because paramedics have a statutory duty to save lives, their occupational status somehow invokes a specialized protection or paradoxical legal impossibility defense. Though legally absurd, a student who fundamentally misunderstands the bounds of legal impossibility might select this option based on Dane's specific career.
(e) Argument-for: Abandonment (or renunciation) is an affirmative defense to attempt if the actor voluntarily and completely renounces their criminal purpose before the crime is completed. A student could argue that Alba voluntarily abandoned the murder by stopping her attack and leaving Dane alive on the floor. By choosing not to deliver a fatal blow when she had the opportunity, she arguably renounced her effort to kill him.

Head-to-head: Option (c) is the legally correct answer because attempt categorically requires the specific intent to commit the target offense, meaning attempted murder requires the specific purpose to kill. Distractor (a) falsely relies on the premise that extreme indifference (recklessness) is legally sufficient for attempted murder, but fails to state this legal rule explicitly. Distractor (b) explicitly but incorrectly claims that attempt has a "general intent requirement." Distractor (d) absurdly misapplies legal impossibility to the victim's status as a paramedic. Distractor (e) misapplies the abandonment defense, which cannot be invoked merely by ceasing an attack after already inflicting harm and completing a substantial step. Because distractor (a) relies on an implicit legal premise rather than an explicit, locked falsifiable claim, the question should be slightly revised.

Falsifiable claim per distractor:
- (a): "because striking a person in the head with a handgun demonstrates an extreme indifference to human life" — wrong implicitly because extreme indifference is insufficient for attempt, but lacks an explicit absolute locking the false legal premise.
- (b): "satisfies the general intent requirement for attempt" — wrong because attempt categorically requires specific intent, not general intent.
- (d): "making the completion of the homicide legally impossible" — wrong because a victim's profession never renders homicide legally impossible.
- (e): "abandoned the effort to kill Dane by leaving him incapacitated" — wrong because mere cessation of a violent attack after inflicting harm does not satisfy the strict requirements for complete and voluntary renunciation.

Recommended fix: Revise (a) to lock the false legal claim explicitly with absolute words: "(a) Guilty of attempted murder because demonstrating an extreme indifference to human life categorically satisfies the mens rea for attempt."
-->
