# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q3.** Assume Leo is charged with the murder of the rival distributor and raises a self-defense claim because the rival drew a weapon. How should the court rule?

(a) Not guilty, because Leo was legally permitted to defend his life once the rival distributor introduced deadly force into the encounter.
(b) Guilty of manslaughter, because his subjective belief in the absolute need for self-defense mitigates the killing even if he initiated the encounter.
(c) Guilty of murder, because he killed the rival during an attempted robbery and the initial aggressor bar completely precludes his self-defense claim. <!-- correct -->
(d) Guilty of murder, because the initial use of a firearm in a territorial dispute creates an irrebuttable presumption of premeditation and deliberation.
(e) Guilty of manslaughter, because the sudden escalation by the rival constitutes adequate provocation, successfully negating the required malice aforethought.

**Answer:** (c)

**Explanation:** The correct answer is (c). Self-defense is entirely unavailable to an initial aggressor who uses or threatens deadly force without first effectively withdrawing from the conflict. Furthermore, because Leo killed the rival while attempting an inherently dangerous felony (robbery—drawing a gun and demanding the stash), he is strictly liable for murder under the felony-murder rule (Fact 4).

(a) is incorrect because the initial aggressor bar strips Leo of the right to claim self-defense, regardless of the rival's response.
(b) is incorrect because imperfect self-defense is unavailable to a defendant who wrongfully initiated the deadly confrontation as the initial aggressor.
(d) is incorrect because felony murder, not an irrebuttable presumption of premeditation, provides the malice aforethought, and constitutional rules generally forbid mandatory irrebuttable presumptions of mens rea elements.
(e) is incorrect because the rival's lawful or foreseeable response to Leo's armed robbery attempt does not constitute legally adequate provocation to reduce murder to manslaughter.

**Tags:** chapters: [14, 22], topics: [initial-aggressor-bar, felony-murder, homicide-grading], difficulty: medium, cognitive: application

**Grounding:** Chapter 22 - Self-Defense > Initial aggressor bar; Chapter 14 - Felony Murder > Strict liability substitution

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that if the rival drew a weapon, it escalated the confrontation into a deadly one, reviving Leo's right to self-defense. Under this theory, once the rival presented an imminent threat of death, Leo was no longer bound by his initial aggression and was legally permitted to defend his life, warranting an acquittal.
(b) Argument-for: This option appeals to the doctrine of imperfect self-defense. A student might argue that even if Leo was the initial aggressor, his genuine, subjective fear of the rival's drawn weapon negates the malice aforethought required for murder. Therefore, his honest but legally barred belief mitigates the killing to manslaughter.
(c) Argument-for: This is the legally correct outcome. Leo's commission of an armed robbery triggers the felony-murder rule, which supplies malice. Furthermore, as an initial deadly aggressor, Leo completely forfeits his right to self-defense unless he effectively withdraws. Thus, the initial aggressor bar completely precludes his self-defense claim.
(d) Argument-for: A student could assert that bringing a firearm to a territorial dispute demonstrates clear pre-planning. Therefore, the use of the firearm creates an irrebuttable presumption of premeditation and deliberation, meaning Leo is automatically guilty of first-degree murder regardless of the felony-murder rule.
(e) Argument-for: This option invokes the heat of passion/provocation defense. A student might reason that being confronted suddenly by a drawn weapon is a terrifying event. This sudden escalation by the rival constitutes legally adequate provocation, successfully negating malice aforethought and reducing the charge to manslaughter.

Head-to-head: Option (c) is legally sound, properly applying both the initial aggressor bar and felony murder. Option (a) relies heavily on a factual mischaracterization (claiming the rival "introduced" deadly force, when Leo did so by attempting an armed robbery) to justify a false legal premise. Option (b) fails because imperfect self-defense categorically does not mitigate murder when the defendant wrongfully initiated an armed robbery. Option (d) contains a clear constitutional error, as mandatory irrebuttable presumptions of mens rea elements violate Due Process (Sandstrom v. Montana). Option (e) is legally false because lawful self-defense by a victim against a felony categorically cannot constitute adequate provocation. While all distractors contain falsifiable claims, Option (a) should be tightened to present an explicit legal error locked with an absolute word, rather than relying on a factual misstatement.

Falsifiable claim per distractor:
- (a): "legally permitted to defend his life once the rival distributor introduced deadly force" — wrong factually (Leo introduced deadly force) and wrong legally because a victim's lawful defensive force does not revive an armed initial aggressor's right to self-defense.
- (b): "mitigates the killing even if he initiated the encounter" — wrong because imperfect self-defense is categorically unavailable to one who initiates a deadly confrontation.
- (d): "creates an irrebuttable presumption of premeditation and deliberation" — wrong because the Supreme Court explicitly prohibits mandatory irrebuttable presumptions regarding mens rea elements.
- (e): "sudden escalation by the rival constitutes adequate provocation" — wrong because a victim's lawful resistance to a violent felony categorically fails to serve as adequate provocation for voluntary manslaughter.

Recommended fix: Change (a) to lock in a definitive false legal claim rather than a factual error: "(a) Not guilty, because an initial aggressor categorically regains the right to self-defense if the victim responds to the initial threat by drawing a deadly weapon."
-->

## Issue 3 — argpass-opus

**Q3.** Assume Leo is charged with the murder of the rival distributor and raises a self-defense claim because the rival drew a weapon. How should the court rule?

(a) Not guilty, because Leo was legally permitted to defend his life once the rival distributor introduced deadly force into the encounter.
(b) Guilty of manslaughter, because his subjective belief in the absolute need for self-defense mitigates the killing even if he initiated the encounter.
(c) Guilty of murder, because he killed the rival during an attempted robbery and the initial aggressor bar completely precludes his self-defense claim. <!-- correct -->
(d) Guilty of murder, because the initial use of a firearm in a territorial dispute creates an irrebuttable presumption of premeditation and deliberation.
(e) Guilty of manslaughter, because the sudden escalation by the rival constitutes adequate provocation, successfully negating the required malice aforethought.

**Answer:** (c)

**Explanation:** The correct answer is (c). Self-defense is entirely unavailable to an initial aggressor who uses or threatens deadly force without first effectively withdrawing from the conflict. Furthermore, because Leo killed the rival while attempting an inherently dangerous felony (robbery—drawing a gun and demanding the stash), he is strictly liable for murder under the felony-murder rule (Fact 4).

(a) is incorrect because the initial aggressor bar strips Leo of the right to claim self-defense, regardless of the rival's response.
(b) is incorrect because imperfect self-defense is unavailable to a defendant who wrongfully initiated the deadly confrontation as the initial aggressor.
(d) is incorrect because felony murder, not an irrebuttable presumption of premeditation, provides the malice aforethought, and constitutional rules generally forbid mandatory irrebuttable presumptions of mens rea elements.
(e) is incorrect because the rival's lawful or foreseeable response to Leo's armed robbery attempt does not constitute legally adequate provocation to reduce murder to manslaughter.

**Tags:** chapters: [14, 22], topics: [initial-aggressor-bar, felony-murder, homicide-grading], difficulty: medium, cognitive: application

**Grounding:** Chapter 22 - Self-Defense > Initial aggressor bar; Chapter 14 - Felony Murder > Strict liability substitution

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Leo's defense relies on the principle that the right to self-defense can be revived when a victim escalates an encounter to a deadly level. Even if Leo initiated the robbery, he might argue that the rival's drawing of a weapon constituted an immediate, disproportionate threat to his life. By this logic, the rival "introduced deadly force," granting Leo the legal permission to meet deadly force with deadly force. A student could argue that self-defense is justifiable the moment the rival exceeds proportional response, warranting an acquittal.
(b) Argument-for: Imperfect self-defense applies when a defendant harbors an actual but unreasonable belief in the need for deadly self-defense, or when the defendant is at fault for the encounter but lacks malice. A student might argue that Leo's subjective fear for his life negates malice aforethought, dropping the charge to manslaughter. Because he actually believed his life was in danger when the rival drew a weapon, this subjective belief mitigates the killing, even if Leo was the initial aggressor who started the dispute.
(c) Argument-for: This is the keyed answer. Leo is strictly liable for murder under the felony-murder rule because the killing occurred during the commission of an inherently dangerous felony (attempted armed robbery). Furthermore, the initial aggressor bar completely precludes a self-defense claim, whether perfect or imperfect, because Leo initiated the deadly encounter by drawing a gun. Without an effective withdrawal, he cannot claim self-defense against the victim's lawful right to resist the robbery.
(d) Argument-for: The deadly weapon rule permits the inference of malice from the use of a deadly weapon. A student could extend this inference to argue that bringing a firearm to a territorial dispute automatically establishes the requisite premeditation and deliberation for first-degree murder. By initiating an armed confrontation, Leo demonstrated a preconceived plan to kill if necessary. Thus, the court must rule him guilty of murder based on an irrebuttable presumption stemming from the initial use of the firearm.
(e) Argument-for: Provocation (heat of passion) can mitigate murder to manslaughter if a reasonable person would have been adequately provoked. A student could argue that being suddenly drawn upon by a rival creates a terrifying and highly provoking situation, causing Leo to act out of sudden fear or passion. This sudden escalation by the rival constitutes adequate provocation, legally negating the malice aforethought required for murder and reducing the conviction to manslaughter.

Head-to-head: 
Option (c) correctly synthesizes the initial aggressor doctrine and the felony-murder rule, rendering it the strongest argument. Distractor (d) is perfectly falsifiable because irrebuttable presumptions of mens rea are unconstitutional under *Sandstrom*. Distractor (b) successfully uses "even if" to state a broad, falsifiable claim that imperfect self-defense is always available to initial aggressors. However, distractors (a) and (e) lack absolute words to strictly lock their falsifiable legal claims, making them slightly vulnerable to edge-case counterarguments about non-deadly initiation or specific definitions of provocation. Adding absolute words would guarantee they fail the close-call standard.

Falsifiable claim per distractor:
- (a): "legally permitted to defend his life once the rival distributor introduced deadly force" — wrong because an initial aggressor who provokes a conflict with deadly force (armed robbery) is categorically barred from claiming self-defense unless they effectively withdraw; furthermore, Leo introduced the deadly force first.
- (b): "mitigates the killing even if he initiated the encounter" — wrong because imperfect self-defense is categorically unavailable to an initial aggressor who initiates the conflict with a deadly weapon or the intent to kill.
- (d): "creates an irrebuttable presumption of premeditation and deliberation" — wrong because mandatory irrebuttable presumptions against criminal defendants regarding mens rea elements are unconstitutional.
- (e): "sudden escalation by the rival constitutes adequate provocation" — wrong because a victim's lawful or foreseeable resistance to an armed robbery categorically cannot serve as legally adequate provocation.

Recommended fix: Add absolute locking words to (a) and (e). 
Change (a) to: "Not guilty, because a defendant is automatically permitted to defend his life once the victim introduces a deadly weapon into the encounter."
Change (e) to: "Guilty of manslaughter, because a victim's defensive escalation categorically constitutes adequate provocation, successfully negating the required malice aforethought."
-->
