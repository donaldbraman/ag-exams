# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q7.** Assume Marlowe is convicted of the federal felony of storing hazardous chemicals, which triggered the fire. Is Marlowe guilty of felony murder for the death of Inspector Greggs?

(a) Guilty, because the death occurred during the res gestae of his ongoing federal chemical storage felony.
(b) Guilty, because but for the chemical fire he started, the inspector would not have been killed by the beam.
(c) Not guilty, because the federal hazardous chemical storage statute does not qualify as an inherently dangerous felony.
(d) Not guilty, because the termite-weakened beam was an independent intervening cause severing the proximate causal chain. <!-- correct -->
(e) Not guilty, because the inspector voluntarily assumed the risk of death by entering a burning commercial structure.

**Answer:** (d)

**Explanation:** (d) is correct because even under the felony murder rule, the death must be proximately caused by the felony. An entirely independent, unforeseeable superseding event (the ceiling collapse due strictly to preexisting termites, not the fire) breaks the causal chain. (a) fails because satisfying the res gestae (time and place) requirement is insufficient if proximate causation is severed. (b) fails because "but-for" factual causation alone is insufficient; legal (proximate) cause is required. (c) fails because even if it is inherently dangerous, the lack of proximate causation defeats the charge. (e) fails because the rescue doctrine makes rescuer presence foreseeable; it does not sever causation.

**Tags:** chapters: [14, 8], topics: [felony murder, proximate cause limit, intervening cause], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14 - Felony Murder and Misdemeanor Manslaughter (Proximate Cause Limit)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Option (c) introduces a second completely valid answer. "Storing hazardous chemicals without a permit" is highly unlikely to qualify as an inherently dangerous felony under the abstract test. If a jurisdiction requires the felony to be inherently dangerous and it fails that test, the felony murder charge is defeated on that ground alone, making (c) just as correct as (d). 
3. Cross-Question Spoilers: Option (d) explicitly spoils Q2 by directly answering that the termite-weakened beam constitutes an independent intervening cause that severs proximate causation.
Recommended fix: Revise Q7 to test the inherently dangerous felony limitation (making C the correct answer) and remove the explicit legal conclusion about intervening causes from the distractors, or state "Assuming the felony is deemed inherently dangerous..." and modify Q2 so it doesn't overlap identically with Q7.
-->

## Issue 3 — argpass-sonnet

**Q7.** Assume Marlowe is convicted of the federal felony of storing hazardous chemicals, which triggered the fire. Is Marlowe guilty of felony murder for the death of Inspector Greggs?

(a) Guilty, because the death occurred during the res gestae of his ongoing federal chemical storage felony.
(b) Guilty, because but for the chemical fire he started, the inspector would not have been killed by the beam.
(c) Not guilty, because the federal hazardous chemical storage statute does not qualify as an inherently dangerous felony.
(d) Not guilty, because the termite-weakened beam was an independent intervening cause severing the proximate causal chain. <!-- correct -->
(e) Not guilty, because the inspector voluntarily assumed the risk of death by entering a burning commercial structure.

**Answer:** (d)

**Explanation:** (d) is correct because even under the felony murder rule, the death must be proximately caused by the felony. An entirely independent, unforeseeable superseding event (the ceiling collapse due strictly to preexisting termites, not the fire) breaks the causal chain. (a) fails because satisfying the res gestae (time and place) requirement is insufficient if proximate causation is severed. (b) fails because "but-for" factual causation alone is insufficient; legal (proximate) cause is required. (c) fails because even if it is inherently dangerous, the lack of proximate causation defeats the charge. (e) fails because the rescue doctrine makes rescuer presence foreseeable; it does not sever causation.

**Tags:** chapters: [14, 8], topics: [felony murder, proximate cause limit, intervening cause], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14 - Felony Murder and Misdemeanor Manslaughter (Proximate Cause Limit)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Felony murder typically applies when a death occurs within the *res gestae*—the time, place, and causal sequence—of the predicate felony. Because Inspector Greggs died at the scene of the fire triggered by Marlowe's ongoing felony, the death was undeniably part of this continuous transaction. A student could argue that under strict applications of felony murder, satisfying the res gestae nexus is sufficient to assign liability for any resulting death.
(b) Argument-for: Criminal liability fundamentally requires actual causation. But for Marlowe storing the hazardous chemicals, there would be no fire; and but for the fire, Inspector Greggs would not have entered the building and stood under the weakened beam. A student could argue that because felony murder is a strict liability doctrine regarding the death, establishing this direct factual (but-for) causation chain is sufficient to render Marlowe guilty.
(c) Argument-for: Many jurisdictions limit the application of the felony murder rule strictly to felonies that are inherently dangerous to human life in the abstract (or a specific BARRK list). A student could argue that a generic federal statute regarding the storage of hazardous chemicals is merely a *malum prohibitum* regulatory offense. If the statute itself does not qualify as inherently dangerous, it cannot serve as the predicate for felony murder, categorically precluding guilt.
(d) Argument-for: While felony murder is a strict liability offense regarding the death, it still requires proximate (legal) causation. Even if Marlowe's felony was the but-for cause of the inspector's presence, the collapse of the beam was an independent, unforeseeable superseding cause because it collapsed strictly due to preexisting termites, not structural damage from the fire. This unforeseeable intervening event breaks the proximate causal chain, properly relieving Marlowe of homicide liability.
(e) Argument-for: Under the professional rescuer doctrine (often termed the "fireman's rule"), emergency responders are deemed to have voluntarily assumed the risks inherent in their dangerous duties. A student could argue that by affirmatively choosing to enter a burning commercial structure, the inspector assumed the risk of structural collapse. This voluntary assumption of risk could be viewed as severing the defendant's duty of care or breaking the causal chain, rendering Marlowe not guilty.

Head-to-head: (d) correctly identifies the dispositive legal concept: an unforeseeable, independent intervening cause (preexisting termite damage) severs proximate causation, which is an absolute requirement for felony murder. However, distractors (a) and (b) fail the strict close-call standard. They state factually true premises (the death occurred during the res gestae; but-for causation exists) and reach a false conclusion ("Guilty"), but they rely on an implicit omission (ignoring proximate cause) rather than explicitly claiming those elements are *solely* or *automatically* sufficient. Distractor (c) makes a definitive legal claim about a generic federal statute that cannot actually be falsified using the facts provided. Distractor (e) successfully asserts a false legal claim, as the tort concept of assumption of risk does not sever proximate causation in criminal homicide.

Falsifiable claim per distractor:
- (a): "Guilty, because the death occurred during the res gestae..." — wrong conclusion, but technically an implicit omission because it fails to explicitly state that res gestae *automatically* overcomes a lack of proximate cause.
- (b): "Guilty, because but for the chemical fire he started..." — wrong conclusion, but an implicit omission because it fails to explicitly assert that but-for causation is *categorically sufficient* for liability.
- (c): "...because the federal hazardous chemical storage statute does not qualify as an inherently dangerous felony." — potentially unfalsifiable because we are not given the statute's text, so whether it qualifies is technically unknown.
- (e): "Not guilty, because the inspector voluntarily assumed the risk..." — explicitly false because a victim's assumption of risk (fireman's rule) does not negate criminal homicide liability or sever proximate causation.

Recommended fix: Add absolute words to lock the false legal rules in the distractors. 
Change (a) to: "Guilty, solely because the death occurred during the res gestae of his ongoing federal chemical storage felony." 
Change (b) to: "Guilty, because but-for factual causation is categorically sufficient to satisfy the felony murder rule." 
Change (c) to: "Not guilty, because regulatory storage statutes categorically cannot serve as predicate felonies for felony murder."
-->

## Issue 4 — argpass-opus

**Q7.** Assume Marlowe is convicted of the federal felony of storing hazardous chemicals, which triggered the fire. Is Marlowe guilty of felony murder for the death of Inspector Greggs?

(a) Guilty, because the death occurred during the res gestae of his ongoing federal chemical storage felony.
(b) Guilty, because but for the chemical fire he started, the inspector would not have been killed by the beam.
(c) Not guilty, because the federal hazardous chemical storage statute does not qualify as an inherently dangerous felony.
(d) Not guilty, because the termite-weakened beam was an independent intervening cause severing the proximate causal chain. <!-- correct -->
(e) Not guilty, because the inspector voluntarily assumed the risk of death by entering a burning commercial structure.

**Answer:** (d)

**Explanation:** (d) is correct because even under the felony murder rule, the death must be proximately caused by the felony. An entirely independent, unforeseeable superseding event (the ceiling collapse due strictly to preexisting termites, not the fire) breaks the causal chain. (a) fails because satisfying the res gestae (time and place) requirement is insufficient if proximate causation is severed. (b) fails because "but-for" factual causation alone is insufficient; legal (proximate) cause is required. (c) fails because even if it is inherently dangerous, the lack of proximate causation defeats the charge. (e) fails because the rescue doctrine makes rescuer presence foreseeable; it does not sever causation.

**Tags:** chapters: [14, 8], topics: [felony murder, proximate cause limit, intervening cause], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14 - Felony Murder and Misdemeanor Manslaughter (Proximate Cause Limit)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that in felony murder, the res gestae requirement (time, place, and causal connection) acts as a strict liability substitute for traditional proximate cause. Because the fire was an ongoing direct result of the chemical storage, and the inspector's death occurred at the time and place of the felony, the elements of the felony murder rule are met. Under broad felony murder interpretations, as long as the death occurs within the res gestae, liability automatically attaches.
(b) Argument-for: A student might argue that under the strict liability rationale of felony murder, actual (but-for) causation is sufficient. Similar to the tort eggshell-plaintiff rule adopted in criminal cases like *People v. Stamp*, a felon takes the building as he finds it. Since the fire foreseeably brought the inspector under the beam, but-for factual causation is satisfied, mandating a guilty verdict.
(c) Argument-for: A student could argue that felony murder requires the predicate felony to be "inherently dangerous" in the abstract. Storing hazardous chemicals can be done safely with proper precautions and thus is not inherently dangerous. If the predicate felony fails this essential test, felony murder cannot apply, making Marlowe not guilty regardless of causation.
(d) Argument-for: A student would argue that felony murder still unequivocally requires proximate causation. An independent, unforeseeable intervening cause—such as a ceiling collapsing solely due to preexisting termite damage rather than structural damage from the fire itself—acts as a superseding cause. This severs the chain of legal causation, relieving the defendant of homicide liability.
(e) Argument-for: A student might argue that the inspector's voluntary decision to enter a burning commercial building constitutes an assumption of the risk. Because the inspector knowingly confronted an extreme danger, this volitional act serves as a superseding cause that breaks the causal chain from Marlowe's original felony, rendering Marlowe not guilty.

Head-to-head: 
Option (d) is the decisively correct answer because it correctly applies the proximate cause limitation to felony murder, recognizing that an unforeseeable, independent intervening cause (termites) severs liability. However, distractors (a) and (b) rely heavily on implicit omissions: they assert true factual premises (the death occurred during the res gestae; but-for causation exists) and conclude "Guilty," relying on the student to deduce that these elements are necessary but not *sufficient*. Without absolute modifiers, they violate the close-call standard. Option (c) introduces an unverified, debatable categorization of a federal statute rather than asserting a demonstrably false rule. Option (e) contains a solid explicit false legal claim, as the rescue doctrine prevents an emergency responder's entry from severing proximate cause.

Falsifiable claim per distractor:
- (a): "Guilty, because the death occurred during the res gestae" — wrong because it implies res gestae is legally sufficient to prove guilt, an implicit omission of the proximate cause element.
- (b): "Guilty, because but for the chemical fire he started" — wrong because it implies factual causation is sufficient on its own, another implicit omission.
- (c): "does not qualify as an inherently dangerous felony" — wrong because it makes a factual/legal assertion about a specific regulatory statute rather than relying on a universally false rule.
- (e): "voluntarily assumed the risk of death" — wrong because the rescue doctrine explicitly makes a rescuer's entry legally foreseeable, meaning it cannot sever criminal proximate causation.

Recommended fix: Lock the distractors with absolute language to explicitly assert false legal rules.
(a) Change to: "Guilty, solely because the death occurred during the res gestae of his ongoing federal felony, which categorically forecloses any intervening cause defense."
(b) Change to: "Guilty, because establishing but-for factual causation is automatically sufficient for felony murder liability regardless of proximate cause."
(c) Change to: "Not guilty, categorically because statutory regulatory felonies can never serve as predicate offenses for felony murder."
-->
