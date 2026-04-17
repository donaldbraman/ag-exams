# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Assume the jury concludes that Alex honestly but unreasonably believed Blake was drawing a revolver. What is the result in a jurisdiction that recognizes imperfect self-defense?

(a) He is guilty of murder, because an unreasonable belief in the need for deadly force provides no legal defense whatsoever to an intentional homicide charge.
(b) He is not guilty of any homicide, because his honest belief that his life was in danger entirely justifies his use of deadly force against the victim.
(c) He is guilty of reckless manslaughter, because an unreasonable belief demonstrates a conscious disregard of a substantial risk that the victim was actually unarmed.
(d) He is guilty only of voluntary manslaughter, because his honest belief in the need for deadly force negates the malice element required for a murder conviction. <!-- correct -->
(e) He is guilty of aggravated assault, because imperfect self-defense operates as a complete defense to homicide but leaves the defendant liable for the underlying physical attack.

**Answer:** (d)

**Explanation:** Alex is guilty of voluntary manslaughter. In jurisdictions that recognize imperfect self-defense (like California), a defendant who holds an honest but legally unreasonable belief that deadly force is necessary is spared a murder conviction. The honest belief negates malice, which is the requisite mental state for murder, reducing the charge to voluntary manslaughter. 
(a) fails because it describes the majority rule, ignoring the prompt's specified jurisdiction. 
(b) fails because an unreasonable belief is never a complete justification for homicide. 
(c) fails because imperfect self-defense negates malice to yield voluntary manslaughter, not reckless manslaughter. 
(e) fails because imperfect self-defense applies to the homicide charge itself as a partial mitigation, not as a complete defense.

**Tags:** chapters: [22], topics: [imperfect self-defense, malice negation], difficulty: easy, cognitive: application

**Grounding:** Chapter 22 (Imperfect self-defense, honest but unreasonable belief)

<!-- audit: MUST FIX
Check 1: pass (conditional on adding the missing facts)
Check 2: pass
Check 3: pass
Check 4: fails. The stem lacks an actus reus and a resulting death. It states Alex's belief ("Alex honestly but unreasonably believed...") but completely omits the physical events. We don't know if Alex shot, missed, or killed Blake, yet all options assume a completed homicide occurred.
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Modify the stem to supply the missing act and result. E.g., "Alex shot and killed Blake. Assume the jury concludes that Alex honestly but unreasonably believed Blake was drawing a revolver. What is the result..."
-->

## Issue 2 — edge-case

**Q7.** Assume the jury concludes that Alex honestly but unreasonably believed Blake was drawing a revolver. What is the result in a jurisdiction that recognizes imperfect self-defense?

(a) He is guilty of murder, because an unreasonable belief in the need for deadly force provides no legal defense whatsoever to an intentional homicide charge.
(b) He is not guilty of any homicide, because his honest belief that his life was in danger entirely justifies his use of deadly force against the victim.
(c) He is guilty of reckless manslaughter, because an unreasonable belief demonstrates a conscious disregard of a substantial risk that the victim was actually unarmed.
(d) He is guilty only of voluntary manslaughter, because his honest belief in the need for deadly force negates the malice element required for a murder conviction. <!-- correct -->
(e) He is guilty of aggravated assault, because imperfect self-defense operates as a complete defense to homicide but leaves the defendant liable for the underlying physical attack.

**Answer:** (d)

**Explanation:** Alex is guilty of voluntary manslaughter. In jurisdictions that recognize imperfect self-defense (like California), a defendant who holds an honest but legally unreasonable belief that deadly force is necessary is spared a murder conviction. The honest belief negates malice, which is the requisite mental state for murder, reducing the charge to voluntary manslaughter. 
(a) fails because it describes the majority rule, ignoring the prompt's specified jurisdiction. 
(b) fails because an unreasonable belief is never a complete justification for homicide. 
(c) fails because imperfect self-defense negates malice to yield voluntary manslaughter, not reckless manslaughter. 
(e) fails because imperfect self-defense applies to the homicide charge itself as a partial mitigation, not as a complete defense.

**Tags:** chapters: [22], topics: [imperfect self-defense, malice negation], difficulty: easy, cognitive: application

**Grounding:** Chapter 22 (Imperfect self-defense, honest but unreasonable belief)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The facts explicitly establish that Blake dies from gross medical negligence (a transfusion reaction), which severs proximate causation for the completed homicide. Thus, Alex cannot technically be guilty of a completed homicide like voluntary manslaughter; he would only be guilty of attempt.
2. Cross-Doctrine Clashes: Causation doctrines clash with the assumed completed homicide in the prompt and options.
3. Cross-Question Spoilers: Stem 2 (Q12, Q13) directly tests the fact that causation was severed, heavily confusing any student who reads the entire fact pattern and realizes Alex cannot be guilty of completed manslaughter in Q7. 
Recommended fix: Add "Assume for this question that Blake dies directly from the gunshot wound." to the beginning of the question stem to bypass the intervening cause.
-->

## Issue 3 — argpass-opus

**Q7.** Assume the jury concludes that Alex honestly but unreasonably believed Blake was drawing a revolver. What is the result in a jurisdiction that recognizes imperfect self-defense?

(a) He is guilty of murder, because an unreasonable belief in the need for deadly force provides no legal defense whatsoever to an intentional homicide charge.
(b) He is not guilty of any homicide, because his honest belief that his life was in danger entirely justifies his use of deadly force against the victim.
(c) He is guilty of reckless manslaughter, because an unreasonable belief demonstrates a conscious disregard of a substantial risk that the victim was actually unarmed.
(d) He is guilty only of voluntary manslaughter, because his honest belief in the need for deadly force negates the malice element required for a murder conviction. <!-- correct -->
(e) He is guilty of aggravated assault, because imperfect self-defense operates as a complete defense to homicide but leaves the defendant liable for the underlying physical attack.

**Answer:** (d)

**Explanation:** Alex is guilty of voluntary manslaughter. In jurisdictions that recognize imperfect self-defense (like California), a defendant who holds an honest but legally unreasonable belief that deadly force is necessary is spared a murder conviction. The honest belief negates malice, which is the requisite mental state for murder, reducing the charge to voluntary manslaughter. 
(a) fails because it describes the majority rule, ignoring the prompt's specified jurisdiction. 
(b) fails because an unreasonable belief is never a complete justification for homicide. 
(c) fails because imperfect self-defense negates malice to yield voluntary manslaughter, not reckless manslaughter. 
(e) fails because imperfect self-defense applies to the homicide charge itself as a partial mitigation, not as a complete defense.

**Tags:** chapters: [22], topics: [imperfect self-defense, malice negation], difficulty: easy, cognitive: application

**Grounding:** Chapter 22 (Imperfect self-defense, honest but unreasonable belief)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might choose this if they assume "recognizes imperfect self-defense" is a distractor phrase for a jurisdiction that only allows the defense in narrow statutory circumstances (e.g., defending a dwelling). Under a strict objective standard, an honest but unreasonable belief is legally irrelevant to an intentional homicide charge. The phrase "no legal defense whatsoever" definitively captures this strict common-law objective view.
(b) Argument-for: A student could rely on the subjective framework of the Model Penal Code justification defenses. Under MPC § 3.04, the use of force is justifiable when the actor simply "believes" it is immediately necessary. A student might interpret "imperfect self-defense" as a doctrine that fully honors this subjective belief for the purpose of the intentional act, reasoning that an honest belief entirely justifies the intentional use of deadly force against the victim.
(c) Argument-for: This option relies on the practical outcome under the Model Penal Code's approach to imperfect self-defense (MPC § 3.09). Under the MPC, if a defendant's belief in the necessity of force is reckless, they lose the justification defense for reckless offenses like manslaughter. A student could argue that an "unreasonable" belief in this context is equivalent to recklessness, meaning Alex's unreasonableness demonstrates a conscious disregard of the risk that deadly force was unnecessary, thereby dropping his liability to reckless manslaughter.
(d) Argument-for: This option correctly states the traditional common-law doctrine of imperfect self-defense, as applied in states like California or Maryland. The core function of this doctrine is that an honest but unreasonable belief in the need for deadly force negates the malice aforethought required for murder. Because the killing is intentional but lacks malice, the appropriate conviction is mitigated directly to voluntary manslaughter.
(e) Argument-for: A student might mistakenly blend imperfect self-defense with concepts of transferred intent or assault mitigation. They could argue that because the self-defense is "imperfect," it shields the defendant from the ultimate homicide liability (because he didn't intend a wrongful death) but leaves him on the hook for the underlying physical assault that caused the death. Thus, they conclude it operates as a complete defense to homicide but a failure to defend the aggravated assault.

Head-to-head: 
Option (d) is the keyed answer and accurately describes the traditional common-law imperfect self-defense doctrine (malice negation leading to voluntary manslaughter). Option (c) is the strongest distractor, as it evokes the Model Penal Code's approach, which can result in a reckless manslaughter conviction; however, (c) falsely equates objective "unreasonableness" with subjective "conscious disregard." Option (a) is explicitly contradicted by the prompt's premise that the jurisdiction recognizes imperfect self-defense. Option (b) falsely claims the doctrine provides complete justification rather than partial mitigation. Option (e) incorrectly frames the doctrine as a complete defense to homicide while preserving assault liability. To ensure (c) is strictly falsifiable under the close-call standard, its error regarding mens rea should be locked with an absolute word.

Falsifiable claim per distractor:
- (a): "provides no legal defense whatsoever" — wrong because the prompt explicitly states the jurisdiction recognizes imperfect self-defense, which acts as a partial defense to murder.
- (b): "entirely justifies his use of deadly force" — wrong because imperfect self-defense, by definition, is a partial mitigation, not a complete justification.
- (c): "an unreasonable belief demonstrates a conscious disregard" — wrong because an unreasonable belief establishes only negligence (an objective failure to perceive a risk), whereas "conscious disregard" requires subjective awareness (recklessness).
- (e): "operates as a complete defense to homicide" — wrong because imperfect self-defense mitigates murder to manslaughter; it does not completely absolve homicide liability.

Recommended fix: Change (c) to include an absolute word to lock the falsifiable claim: "(c) He is guilty of reckless manslaughter, because an unreasonable belief categorically demonstrates a conscious disregard of a substantial risk that the victim was actually unarmed."
-->
