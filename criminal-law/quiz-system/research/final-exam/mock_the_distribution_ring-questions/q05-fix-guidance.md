# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Cole is charged as an accomplice to armed robbery in a federal jurisdiction applying the *Rosemond* standard. Cole argues he lacked the necessary mens rea because he only agreed to an unarmed robbery. Is Cole guilty as an accomplice to armed robbery?

(a) Yes, because he acquired knowledge of the firearm before committing the crime and chose to continue his participation despite having a meaningful opportunity to walk away. <!-- correct -->
(b) Yes, because under the strict liability standard for accomplices, any assistance rendered to an armed principal automatically transfers the weapon enhancement to the accomplice.
(c) No, because he vocally objected when he saw the gun, which constitutes an effective withdrawal from the armed portion of the offense.
(d) No, because the *Rosemond* standard requires that the accomplice participate in acquiring or supplying the firearm used in the offense.
(e) No, because his advance knowledge of the firearm was acquired only moments before exiting the car, which does not constitute advance knowledge during the planning phase.

**Answer:** (a)

**Explanation:** Under *Rosemond*, accomplice liability for an armed offense requires advance knowledge of the firearm at a time when the accomplice has a meaningful opportunity to walk away. Cole learned of the gun before exiting the car to take his lookout position. By proceeding with the crime instead of leaving, he satisfied the temporal advance knowledge requirement. (b) is wrong because accomplice liability requires specific mens rea, not strict liability. (c) is wrong because verbal objection without actual withdrawal is insufficient if the defendant continues to aid the crime. (d) is wrong because *Rosemond* requires knowledge, not physical provision of the weapon. (e) is wrong because "advance" means before participation is complete such that he can no longer walk away, not during remote planning.

**Tags:** chapters: [18], topics: [accomplice, mens_rea, rosemond], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (Accomplice Liability), mr-temporal-advance-knowledge

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The stem completely lacks the facts required to answer the question. It never mentions Cole acting as a lookout, being in a car, or the timeline of when he discovered the gun. These critical facts only appear retroactively in the answer choices and explanation, making the question impossible to answer based on the stem alone.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Add the missing factual scenario to the stem. For example: "Cole agrees to act as a lookout for a robbery. Just as they park the car at the target location, the principal pulls out a gun. Cole vocally objects, but proceeds to exit the car and take his lookout position anyway. Cole is charged..."
-->

## Issue 2 — edge-case

**Q5.** Cole is charged as an accomplice to armed robbery in a federal jurisdiction applying the *Rosemond* standard. Cole argues he lacked the necessary mens rea because he only agreed to an unarmed robbery. Is Cole guilty as an accomplice to armed robbery?

(a) Yes, because he acquired knowledge of the firearm before committing the crime and chose to continue his participation despite having a meaningful opportunity to walk away. <!-- correct -->
(b) Yes, because under the strict liability standard for accomplices, any assistance rendered to an armed principal automatically transfers the weapon enhancement to the accomplice.
(c) No, because he vocally objected when he saw the gun, which constitutes an effective withdrawal from the armed portion of the offense.
(d) No, because the *Rosemond* standard requires that the accomplice participate in acquiring or supplying the firearm used in the offense.
(e) No, because his advance knowledge of the firearm was acquired only moments before exiting the car, which does not constitute advance knowledge during the planning phase.

**Answer:** (a)

**Explanation:** Under *Rosemond*, accomplice liability for an armed offense requires advance knowledge of the firearm at a time when the accomplice has a meaningful opportunity to walk away. Cole learned of the gun before exiting the car to take his lookout position. By proceeding with the crime instead of leaving, he satisfied the temporal advance knowledge requirement. (b) is wrong because accomplice liability requires specific mens rea, not strict liability. (c) is wrong because verbal objection without actual withdrawal is insufficient if the defendant continues to aid the crime. (d) is wrong because *Rosemond* requires knowledge, not physical provision of the weapon. (e) is wrong because "advance" means before participation is complete such that he can no longer walk away, not during remote planning.

**Tags:** chapters: [18], topics: [accomplice, mens_rea, rosemond], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (Accomplice Liability), mr-temporal-advance-knowledge

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The facts explicitly state that Damon shot Vic "without searching for drugs or demanding money" and "didn't get any product." Because no property was taken, a completed robbery never occurred. Since accomplice liability is derivative of the principal's conduct, Cole cannot be legally convicted as an accomplice to a *completed* armed robbery if the principal never completed the target offense. 
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change the charge in the question stem from "accomplice to armed robbery" to "accomplice to attempted armed robbery" to reflect the actual derivative liability. Update Option (a) to read "...before participating in the attempt..."
-->

## Issue 3 — argpass-sonnet

**Q5.** Cole is charged as an accomplice to armed robbery in a federal jurisdiction applying the *Rosemond* standard. Cole argues he lacked the necessary mens rea because he only agreed to an unarmed robbery. Is Cole guilty as an accomplice to armed robbery?

(a) Yes, because he acquired knowledge of the firearm before committing the crime and chose to continue his participation despite having a meaningful opportunity to walk away. <!-- correct -->
(b) Yes, because under the strict liability standard for accomplices, any assistance rendered to an armed principal automatically transfers the weapon enhancement to the accomplice.
(c) No, because he vocally objected when he saw the gun, which constitutes an effective withdrawal from the armed portion of the offense.
(d) No, because the *Rosemond* standard requires that the accomplice participate in acquiring or supplying the firearm used in the offense.
(e) No, because his advance knowledge of the firearm was acquired only moments before exiting the car, which does not constitute advance knowledge during the planning phase.

**Answer:** (a)

**Explanation:** Under *Rosemond*, accomplice liability for an armed offense requires advance knowledge of the firearm at a time when the accomplice has a meaningful opportunity to walk away. Cole learned of the gun before exiting the car to take his lookout position. By proceeding with the crime instead of leaving, he satisfied the temporal advance knowledge requirement. (b) is wrong because accomplice liability requires specific mens rea, not strict liability. (c) is wrong because verbal objection without actual withdrawal is insufficient if the defendant continues to aid the crime. (d) is wrong because *Rosemond* requires knowledge, not physical provision of the weapon. (e) is wrong because "advance" means before participation is complete such that he can no longer walk away, not during remote planning.

**Tags:** chapters: [18], topics: [accomplice, mens_rea, rosemond], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (Accomplice Liability), mr-temporal-advance-knowledge

<!-- argument-pass: MUST FIX
(a) Argument-for: *Rosemond v. United States* establishes that accomplice liability for an armed offense requires advance knowledge of the firearm. This advance knowledge must occur when the accomplice still has a realistic, meaningful opportunity to walk away from the crime. Option (a) accurately applies this standard, concluding that because Cole chose to continue his participation despite having a meaningful opportunity to walk away after learning of the gun, he is guilty. Therefore, this option represents the correct application of federal doctrine.
(b) Argument-for: Under theories of transferred intent or the natural and probable consequences doctrine, some jurisdictions hold accomplices liable for armed enhancements if the principal's use of a weapon was foreseeable. A student might confuse this with federal doctrine, arguing that an armed robbery charge operates under a strict liability standard for accomplices. Option (b) explicitly invokes this automatic transfer theory, asserting that any assistance rendered to an armed principal attaches the weapon enhancement regardless of the accomplice's mens rea.
(c) Argument-for: To effectively withdraw from a crime, a defendant generally must communicate their repudiation to co-felons before the crime becomes unstoppable. A student could argue that by vocally objecting when he saw the gun, Cole effectively limited the scope of his agreement to an unarmed robbery. By communicating this objection, Cole negated the mens rea for the armed portion of the offense, which a student might view as a valid partial withdrawal.
(d) Argument-for: *Rosemond* requires that an accomplice actively participate in the armed offense with advance knowledge of the gun. A student might misconstrue the actus reus requirement for the armed component, believing it strictly demands that the accomplice's assistance relate directly to the firearm itself. Under this flawed interpretation, merely participating in the robbery is insufficient, and Cole would need to have physically acquired or supplied the firearm to be liable.
(e) Argument-for: *Rosemond* dictates that knowledge must be "advance," providing a "realistic opportunity to quit." A student could argue that learning of the weapon "moments before exiting the car" does not provide such an opportunity, as the plan is already in full motion and walking away is practically impossible. Therefore, a student might conclude that knowledge must be acquired earlier, during the planning phase, to satisfy the mens rea requirement for accomplice liability.

Head-to-head: 
Option (a) states the correct legal standard under *Rosemond*. However, the question prompt completely omits the facts regarding when Cole learned about the gun, how he reacted, and whether he had a meaningful opportunity to walk away. Consequently, options (a), (c), and (e) all introduce extrinsic facts (e.g., "moments before exiting the car," "vocally objected") that are absent from the prompt but present in the explanation. Because a student cannot deduce the factual scenario from the prompt alone, the keyed answer cannot be logically selected over the distractors without guessing the author's hidden intent. Thus, the distractors are as strong as the key, triggering a MUST FIX.

Falsifiable claim per distractor:
- (b): "strict liability standard for accomplices... automatically transfers" — wrong because *Rosemond* explicitly requires advance knowledge, rejecting strict liability for the firearm element.
- (c): "vocally objected ... constitutes an effective withdrawal" — wrong because vocal objection without actual cessation of participation does not constitute legal withdrawal.
- (d): "requires that the accomplice participate in acquiring or supplying the firearm" — wrong because *Rosemond* holds that participating in the underlying crime with knowledge of the firearm satisfies the actus reus; the accomplice need not supply the gun.
- (e): "does not constitute advance knowledge during the planning phase" — wrong because *Rosemond* explicitly rejects the idea that knowledge must be acquired during the planning phase; acquiring knowledge just before exiting the car satisfies the standard if there is still a realistic opportunity to quit.

Recommended fix: Add the missing facts to the prompt. E.g., change the second sentence to: "Just moments before exiting the getaway car to take his lookout position, Cole saw his confederate draw a gun. Cole argues he lacked the necessary mens rea because he had only agreed to an unarmed robbery during the planning phase, and he vocally objected when he saw the weapon, though he proceeded to act as lookout anyway despite having a chance to walk away."
-->

## Issue 4 — argpass-opus

**Q5.** Cole is charged as an accomplice to armed robbery in a federal jurisdiction applying the *Rosemond* standard. Cole argues he lacked the necessary mens rea because he only agreed to an unarmed robbery. Is Cole guilty as an accomplice to armed robbery?

(a) Yes, because he acquired knowledge of the firearm before committing the crime and chose to continue his participation despite having a meaningful opportunity to walk away. <!-- correct -->
(b) Yes, because under the strict liability standard for accomplices, any assistance rendered to an armed principal automatically transfers the weapon enhancement to the accomplice.
(c) No, because he vocally objected when he saw the gun, which constitutes an effective withdrawal from the armed portion of the offense.
(d) No, because the *Rosemond* standard requires that the accomplice participate in acquiring or supplying the firearm used in the offense.
(e) No, because his advance knowledge of the firearm was acquired only moments before exiting the car, which does not constitute advance knowledge during the planning phase.

**Answer:** (a)

**Explanation:** Under *Rosemond*, accomplice liability for an armed offense requires advance knowledge of the firearm at a time when the accomplice has a meaningful opportunity to walk away. Cole learned of the gun before exiting the car to take his lookout position. By proceeding with the crime instead of leaving, he satisfied the temporal advance knowledge requirement. (b) is wrong because accomplice liability requires specific mens rea, not strict liability. (c) is wrong because verbal objection without actual withdrawal is insufficient if the defendant continues to aid the crime. (d) is wrong because *Rosemond* requires knowledge, not physical provision of the weapon. (e) is wrong because "advance" means before participation is complete such that he can no longer walk away, not during remote planning.

**Tags:** chapters: [18], topics: [accomplice, mens_rea, rosemond], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (Accomplice Liability), mr-temporal-advance-knowledge

<!-- argument-pass: MUST FIX
(a) Argument-for: Cole meets the *Rosemond* standard for accomplice liability to an armed offense. In *Rosemond v. United States*, the Supreme Court held that an accomplice must have "advance knowledge" of a confederate's firearm. The Court defined this to mean learning of the weapon at a time when there is still a "meaningful opportunity" to walk away from the crime. Because Cole discovered the weapon before committing the underlying offense and proceeded to participate rather than leaving, he established the requisite mens rea, superseding his initial unarmed agreement.
(b) Argument-for: Accomplice liability often rests on the premise that one who aids a crime is responsible for its natural and probable consequences. Since armed robbery is a highly foreseeable escalation of an unarmed robbery, one could argue that Cole is strictly liable for the weapon enhancement. If a jurisdiction automatically transfers weapon enhancements to all accomplices who render any assistance to an armed principal, Cole's initial assistance would satisfy the standard regardless of his specific prior knowledge regarding the gun.
(c) Argument-for: A defendant cannot be held liable for a crime they have effectively withdrawn from. Under general accomplice liability principles, an effective withdrawal negates mens rea for the subsequent criminal acts. By vocally objecting to the gun upon seeing it, Cole arguably communicated a clear repudiation of the armed portion of the enterprise. This explicit limitation of his agreement could be construed as legally severing his liability for the principal's unilateral escalation to an armed offense.
(d) Argument-for: To be liable as an accomplice, a defendant must take an affirmative act to aid or encourage the specific offense. When the offense includes a highly specific aggravating element like a firearm under § 924(c), a plausible defense argument is that the accomplice's aiding conduct must relate directly to that element. Therefore, under a strict actus reus interpretation of the enhancement, Cole cannot be liable unless he actively participated in procuring, supplying, or loading the firearm used by his confederate.
(e) Argument-for: The *Rosemond* standard focuses on the ability of the accomplice to alter their conduct based on advance knowledge of the weapon. If Cole only discovered the gun moments before exiting the vehicle, he was already in the immediate zone of danger and execution of the crime. One could forcefully argue this late discovery practically deprives him of a "meaningful opportunity" to safely walk away, as required by the Supreme Court, meaning his knowledge did not occur early enough in the planning phase to establish liability.

Head-to-head: Option (a) correctly applies the specific holding of *Rosemond v. United States*. Options (b) and (d) fail because they rely on explicit misstatements of the law (accomplices are not strictly liable for § 924(c) offenses, nor do they need to supply the gun). Option (c) relies on a false rule of withdrawal, as merely objecting without stopping assistance is legally insufficient. Option (e) incorrectly states that knowledge moments before exiting the car cannot constitute advance knowledge. However, this question is a MUST FIX because the question stem is entirely missing the facts required to answer it. The stem merely says Cole "agreed to an unarmed robbery." It never states that he learned of the gun before exiting a car, acted as a lookout, or vocally objected—these crucial facts only appear as assumed predicates in the options and the explanation.

Falsifiable claim per distractor:
- (b): "...under the strict liability standard for accomplices, any assistance rendered to an armed principal automatically transfers..." — wrong because Rosemond explicitly requires advance knowledge of the firearm, completely rejecting strict liability for this element.
- (c): "...vocally objected when he saw the gun, which constitutes an effective withdrawal..." — wrong because verbal objection does not categorically constitute effective withdrawal if the defendant continues to aid the underlying felony.
- (d): "...requires that the accomplice participate in acquiring or supplying the firearm..." — wrong because Rosemond explicitly states the accomplice only needs to participate in the underlying crime with advance knowledge of the gun, not supply the gun itself.
- (e): "...acquired only moments before exiting the car, which does not constitute advance knowledge..." — wrong because Rosemond explicitly notes that learning of a gun right before the crime commences can still provide a meaningful opportunity to walk away.

Recommended fix: 1. Add the missing facts to the question stem so the options make sense: "Cole agreed to act as a getaway driver for an unarmed bank robbery. Just moments before his confederate exited the car to enter the bank, the confederate pulled out a loaded gun. Cole vocally objected but remained in the driver's seat and successfully drove the confederate away after the robbery." 2. In (c), add absolute language: "which categorically constitutes an effective withdrawal". 3. In (e), lock the legal claim: "which categorically fails to satisfy the advance knowledge requirement because the knowledge must be acquired during the remote planning phase."
-->
