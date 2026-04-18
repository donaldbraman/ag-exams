# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Assume the jurisdiction has abolished the felony murder rule, forcing the State to rely on standard homicide grading. Based on Brenda's storage of the Solv-X, what is the most severe homicide charge the prosecution can realistically pursue against her?

(a) First-degree murder, because her deliberate decision to bypass zoning laws demonstrates premeditation. This establishes the deliberation necessary to cause massive structural damage and death.
(b) Voluntary manslaughter, because the sudden ignition of the chemicals constitutes adequate provocation. This sudden emergency would cause a reasonable person to lose self-control.
(c) Second-degree "depraved heart" murder, because placing a known sparking heater next to volatile chemical drums demonstrates an extreme indifference to the value of human life. <!-- correct -->
(d) Involuntary manslaughter, because predicate property damage offenses can only support negligence-based homicides. This limitation applies regardless of the defendant's subjective awareness of the risk.
(e) Negligent homicide, because she only failed to perceive the highly specific risk that an unconscious employee would sleepwalk. She could not have known he would specifically knock over the mislabeled drum.

**Answer:** (c)

**Explanation:** Option (c) is correct because depraved heart (or extreme recklessness) murder occurs when a defendant acts with a conscious disregard for a substantial and unjustifiable risk to human life, demonstrating extreme indifference. Placing a known sparking heater directly next to highly flammable chemicals in a residential high-rise easily meets this threshold. Option (a) is incorrect because bypassing zoning laws does not constitute premeditation or intent to kill. Option (b) is incorrect because adequate provocation requires a sudden heat of passion triggered by a legally recognized provocation (like discovering adultery or mutual combat), not a self-created emergency. Option (d) is incorrect because homicide grading turns on the defendant's mental state regarding the risk of death, not the categorization of the underlying property offense. Option (e) is incorrect because her conduct was reckless, not merely negligent, regarding the risk of fire.

**Tags:** chapters: [14], topics: [homicide grading, depraved heart murder, extreme recklessness], difficulty: medium, cognitive: application

**Grounding:** Homicide Grading - Depraved Heart Murder (extreme indifference to the value of human life)

<!-- audit: SHOULD FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: fail. The stem relies on a master fact pattern that is missing. The facts regarding Brenda, the storage of Solv-X, the sparking heater, the residential high-rise, and the sleepwalking employee are necessary to answer the question but are absent from the prompt.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: If this question is intended to be standalone rather than part of a multi-question hypo, integrate the essential facts into the stem (e.g., "Brenda stored highly volatile chemical drums of Solv-X directly next to a known sparking heater in a residential high-rise...").
-->

## Issue 2 — edge-case

**Q10.** Assume the jurisdiction has abolished the felony murder rule, forcing the State to rely on standard homicide grading. Based on Brenda's storage of the Solv-X, what is the most severe homicide charge the prosecution can realistically pursue against her?

(a) First-degree murder, because her deliberate decision to bypass zoning laws demonstrates premeditation. This establishes the deliberation necessary to cause massive structural damage and death.
(b) Voluntary manslaughter, because the sudden ignition of the chemicals constitutes adequate provocation. This sudden emergency would cause a reasonable person to lose self-control.
(c) Second-degree "depraved heart" murder, because placing a known sparking heater next to volatile chemical drums demonstrates an extreme indifference to the value of human life. <!-- correct -->
(d) Involuntary manslaughter, because predicate property damage offenses can only support negligence-based homicides. This limitation applies regardless of the defendant's subjective awareness of the risk.
(e) Negligent homicide, because she only failed to perceive the highly specific risk that an unconscious employee would sleepwalk. She could not have known he would specifically knock over the mislabeled drum.

**Answer:** (c)

**Explanation:** Option (c) is correct because depraved heart (or extreme recklessness) murder occurs when a defendant acts with a conscious disregard for a substantial and unjustifiable risk to human life, demonstrating extreme indifference. Placing a known sparking heater directly next to highly flammable chemicals in a residential high-rise easily meets this threshold. Option (a) is incorrect because bypassing zoning laws does not constitute premeditation or intent to kill. Option (b) is incorrect because adequate provocation requires a sudden heat of passion triggered by a legally recognized provocation (like discovering adultery or mutual combat), not a self-created emergency. Option (d) is incorrect because homicide grading turns on the defendant's mental state regarding the risk of death, not the categorization of the underlying property offense. Option (e) is incorrect because her conduct was reckless, not merely negligent, regarding the risk of fire.

**Tags:** chapters: [14], topics: [homicide grading, depraved heart murder, extreme recklessness], difficulty: medium, cognitive: application

**Grounding:** Homicide Grading - Depraved Heart Murder (extreme indifference to the value of human life)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: By validating that a standard homicide charge can be realistically pursued for Victor's death, Q10 implicitly confirms that Charles's sleepwalking did not sever the chain of causation, thereby spoiling the intervening cause analysis intended for Q4.
Recommended fix: Amend the prompt's assumption to explicitly bypass the causation issue: "Assume the jurisdiction has abolished the felony murder rule and that proximate causation is established. Based on Brenda's..."
-->

## Issue 3 — argpass-sonnet

**Q10.** Assume the jurisdiction has abolished the felony murder rule, forcing the State to rely on standard homicide grading. Based on Brenda's storage of the Solv-X, what is the most severe homicide charge the prosecution can realistically pursue against her?

(a) First-degree murder, because her deliberate decision to bypass zoning laws demonstrates premeditation. This establishes the deliberation necessary to cause massive structural damage and death.
(b) Voluntary manslaughter, because the sudden ignition of the chemicals constitutes adequate provocation. This sudden emergency would cause a reasonable person to lose self-control.
(c) Second-degree "depraved heart" murder, because placing a known sparking heater next to volatile chemical drums demonstrates an extreme indifference to the value of human life. <!-- correct -->
(d) Involuntary manslaughter, because predicate property damage offenses can only support negligence-based homicides. This limitation applies regardless of the defendant's subjective awareness of the risk.
(e) Negligent homicide, because she only failed to perceive the highly specific risk that an unconscious employee would sleepwalk. She could not have known he would specifically knock over the mislabeled drum.

**Answer:** (c)

**Explanation:** Option (c) is correct because depraved heart (or extreme recklessness) murder occurs when a defendant acts with a conscious disregard for a substantial and unjustifiable risk to human life, demonstrating extreme indifference. Placing a known sparking heater directly next to highly flammable chemicals in a residential high-rise easily meets this threshold. Option (a) is incorrect because bypassing zoning laws does not constitute premeditation or intent to kill. Option (b) is incorrect because adequate provocation requires a sudden heat of passion triggered by a legally recognized provocation (like discovering adultery or mutual combat), not a self-created emergency. Option (d) is incorrect because homicide grading turns on the defendant's mental state regarding the risk of death, not the categorization of the underlying property offense. Option (e) is incorrect because her conduct was reckless, not merely negligent, regarding the risk of fire.

**Tags:** chapters: [14], topics: [homicide grading, depraved heart murder, extreme recklessness], difficulty: medium, cognitive: application

**Grounding:** Homicide Grading - Depraved Heart Murder (extreme indifference to the value of human life)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that first-degree murder is appropriate because Brenda's actions were intentional and highly calculated. By deliberately bypassing zoning laws to store hazardous chemicals, she engaged in a premeditated course of conduct that created a lethal environment. Since the resulting death was a direct consequence of this planned evasion of safety regulations, it mirrors the deliberation required for first-degree murder.
(b) Argument-for: A student might argue for voluntary manslaughter by conceptualizing the sudden chemical fire as an overwhelming emergency that functions as adequate provocation. If the unexpected ignition caused an intense panic, depriving her of self-control, this "heat of passion" equivalent could logically mitigate the homicide. The law downgrades murder when sudden, terrifying circumstances overpower reason.
(c) Argument-for: This is the correct answer. Second-degree depraved heart murder applies when a defendant acts with conscious disregard for a substantial and unjustifiable risk to human life. Placing a known sparking heater directly adjacent to volatile chemical drums demonstrates extreme indifference to the value of human life, easily satisfying the extreme recklessness standard.
(d) Argument-for: A student could argue for involuntary manslaughter based on the abolition of the felony murder rule. Without felony murder to automatically elevate deaths occurring during property offenses to murder, such deaths must fall to the default level for unintentional killings. Therefore, predicate property offenses inherently cap homicide grading at involuntary manslaughter, regardless of subjective recklessness.
(e) Argument-for: A student could choose negligent homicide by focusing on the highly unforeseeable intervening act of the sleepwalking employee. Criminal recklessness requires conscious disregard of a risk, and an argument can be made that Brenda could not have consciously disregarded the bizarre sequence of an unconscious person sleepwalking into a drum. Because she failed to foresee this specific causal chain, she was only negligent.

Head-to-head: Option (c) is the clear correct answer because it accurately applies the depraved heart murder standard to the creation of a massive, known fire risk. Options (a) and (b) rely on gross misapplications of legal terms of art (premeditation and adequate provocation). Option (d) uses strong absolute language to make a legally false categorical claim about property offenses capping homicide grading. Option (e) is a good distractor conceptually (focusing on the unforeseeable mechanism of death) but fails the close-call standard because it lacks an explicit, absolute false legal claim. It merely implies that unforeseeability of the exact mechanism reduces the charge to negligence based on a factual assertion, rather than stating a categorical legal rule.

Falsifiable claim per distractor:
- (a): "her deliberate decision to bypass zoning laws demonstrates premeditation." — wrong because intentionally violating a zoning ordinance does not satisfy the specific intent to kill or deliberation required for first-degree murder.
- (b): "the sudden ignition of the chemicals constitutes adequate provocation." — wrong because adequate provocation requires legally recognized circumstances (e.g., mutual combat, discovering adultery) that incite heat of passion, not an inanimate emergency or accidental fire.
- (d): "can only support negligence-based homicides. This limitation applies regardless of the defendant's subjective awareness" — wrong because if a defendant's subjective awareness and conduct demonstrate extreme indifference to human life, a property offense can absolutely support second-degree depraved heart murder.
- (e): "she only failed to perceive the highly specific risk" — wrong because criminal recklessness does not require foreseeing the precise mechanism of harm, but the distractor lacks absolute wording to lock this as a formal false legal proposition.

Recommended fix: Update (e) to include an absolute legal falsifier regarding the mechanism of harm. Change (e) to: "Negligent homicide, because a recklessness finding categorically requires the defendant to foresee the exact mechanism of harm. She could not have known the employee would specifically sleepwalk and knock over the mislabeled drum."
-->
