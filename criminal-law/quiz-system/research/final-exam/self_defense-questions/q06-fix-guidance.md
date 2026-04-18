# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q6.** Assume Blake faces a homicide charge for the death of Chris. Blake argues that the charge should be reduced to voluntary manslaughter because he shot Chris only after Chris shoved him during a bitter argument. How should the court rule?

(a) Guilty of murder, because a verbal argument and a mere physical shove during a drug transaction are legally insufficient provocation to reduce the charge to manslaughter. <!-- correct -->
(b) Guilty of voluntary manslaughter, because the sudden physical shove triggered an extreme emotional disturbance that legally negates his malice aforethought.
(c) Guilty of murder, because any killing that occurs during the commission of a drug transaction is automatically elevated to capital murder in all jurisdictions.
(d) Guilty of voluntary manslaughter, because Chris's initial physical aggression legally justified Blake's use of a firearm under the mutual combat doctrine.
(e) Guilty of murder, because Blake used a deadly weapon, which creates an irrebuttable presumption of premeditation and deliberation under modern criminal law.

**Answer:** (a)

**Explanation:** Voluntary manslaughter requires adequate provocation (heat of passion) or, in MPC jurisdictions, an extreme emotional disturbance for which there is a reasonable explanation. A minor battery (a shove) during a bitter argument over a drug price is not legally adequate provocation to justify a lethal response and mitigate an intentional shooting from murder to manslaughter. (b) is wrong because the extreme emotional disturbance defense requires a "reasonable explanation or excuse," which is not satisfied by a routine shove in a drug deal. (c) is wrong because drug transactions do not automatically elevate all killings to capital murder in all jurisdictions. (d) is wrong because "mutual combat" requires a mutual physical fight, not a one-sided shove followed by a deadly escalation. (e) is wrong because the use of a deadly weapon supports an inference of intent to kill, not an irrebuttable presumption of premeditation.

**Tags:** chapters: [12, 13], topics: [homicide-grading], difficulty: medium, cognitive: application

**Grounding:** Chapter 12 (Intentional Homicide) - Heat of passion/provocation limits and the insufficiency of minor batteries to mitigate murder.

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The facts state Chris threatened Blake with a "body bag" and reached into his jacket, strongly triggering perfect or imperfect self-defense. A smart student will recognize Blake might not be "Guilty of murder" at all, making option (a) appear factually incorrect despite correctly stating the provocation rule.
2. Cross-Doctrine Clashes: Self-defense/Imperfect self-defense clashes with the ultimate conclusion of "Guilty of murder" based solely on the failure of the provocation defense.
3. Cross-Question Spoilers: Q8, Q9, and Q10 test Blake's self-defense claims. Concluding that Blake is definitively "Guilty of murder" in Q6 preempts and spoils the self-defense analysis.
Recommended fix: Change the prompt to ask "How should the court rule on this specific provocation argument?" and change the start of the options to "Reject the argument, because..." and "Accept the argument, because..." rather than concluding ultimate guilt.
-->

## Issue 3 — argpass-sonnet

**Q6.** Assume Blake faces a homicide charge for the death of Chris. Blake argues that the charge should be reduced to voluntary manslaughter because he shot Chris only after Chris shoved him during a bitter argument. How should the court rule?

(a) Guilty of murder, because a verbal argument and a mere physical shove during a drug transaction are legally insufficient provocation to reduce the charge to manslaughter. <!-- correct -->
(b) Guilty of voluntary manslaughter, because the sudden physical shove triggered an extreme emotional disturbance that legally negates his malice aforethought.
(c) Guilty of murder, because any killing that occurs during the commission of a drug transaction is automatically elevated to capital murder in all jurisdictions.
(d) Guilty of voluntary manslaughter, because Chris's initial physical aggression legally justified Blake's use of a firearm under the mutual combat doctrine.
(e) Guilty of murder, because Blake used a deadly weapon, which creates an irrebuttable presumption of premeditation and deliberation under modern criminal law.

**Answer:** (a)

**Explanation:** Voluntary manslaughter requires adequate provocation (heat of passion) or, in MPC jurisdictions, an extreme emotional disturbance for which there is a reasonable explanation. A minor battery (a shove) during a bitter argument over a drug price is not legally adequate provocation to justify a lethal response and mitigate an intentional shooting from murder to manslaughter. (b) is wrong because the extreme emotional disturbance defense requires a "reasonable explanation or excuse," which is not satisfied by a routine shove in a drug deal. (c) is wrong because drug transactions do not automatically elevate all killings to capital murder in all jurisdictions. (d) is wrong because "mutual combat" requires a mutual physical fight, not a one-sided shove followed by a deadly escalation. (e) is wrong because the use of a deadly weapon supports an inference of intent to kill, not an irrebuttable presumption of premeditation.

**Tags:** chapters: [12, 13], topics: [homicide-grading], difficulty: medium, cognitive: application

**Grounding:** Chapter 12 (Intentional Homicide) - Heat of passion/provocation limits and the insufficiency of minor batteries to mitigate murder.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A conviction for murder is appropriate because Blake lacked the "adequate provocation" required to mitigate the killing to manslaughter. Under the common law "heat of passion" test, provocation must be sufficient to cause a reasonable person to lose self-control. Traditional doctrine holds that words alone and minor batteries, such as a "mere physical shove," are categorically insufficient to meet this legal threshold. Because the provocation was inadequate as a matter of law, the malice aforethought remains intact. Therefore, the court must rule that Blake is guilty of murder.

(b) Argument-for: Under the Model Penal Code (MPC), a homicide is mitigated to manslaughter if committed under the influence of "extreme mental or emotional disturbance" (EED). Unlike the rigid common law categories for provocation, EED is a broader standard that focuses on the defendant’s subjective emotional state. Blake can argue that the combination of a bitter argument and a physical shove was sufficient to trigger a loss of control. If the jury finds there is a "reasonable explanation or excuse" for this state from Blake's perspective, the EED legally negates the malice required for murder.

(c) Argument-for: In many jurisdictions, the felony-murder rule or specific drug-trafficking homicide statutes apply to deaths occurring during dangerous illicit activities. This argument posits that because the killing occurred during a drug transaction, the underlying felony provides the requisite "malice" to support a murder conviction. Some legal frameworks classify drug-related violence as inherently dangerous, automatically elevating any resulting death to capital murder to deter such conduct. Under this bright-line rule, the defendant’s claim of provocation is irrelevant given the illegal context of the encounter.

(d) Argument-for: Blake’s actions could be classified as voluntary manslaughter under the "mutual combat" doctrine. This doctrine applies when two individuals engage in a sudden quarrel that escalates into physical violence, resulting in a death caused in the "heat of blood." By shoving Blake during a bitter argument, Chris initiated physical contact, signaling the start of a combat scenario. Blake can argue that this initial aggression legally justified his lethal response as a sudden heat-of-passion reaction. This doctrine recognizes that a person's judgment is clouded during physical struggle, necessitating a reduction in the charge.

(e) Argument-for: The "deadly weapon doctrine" allows a court or jury to infer the mental state required for murder based on the instrument used in the killing. This argument asserts that Blake’s intentional use of a firearm directed at Chris creates a specific legal status for the homicide. In some modern interpretations, the deliberate use of a lethal weapon in response to a non-lethal shove creates an irrebuttable presumption of premeditation and deliberation. Because the law presumes Blake intended the natural and probable consequences of using a gun, his claim of emotional provocation is legally precluded.

Head-to-head: (a) is the strongest option because it correctly identifies that a minor physical battery is legally insufficient to meet the standard of "adequate provocation" for mitigation under both common law and modern standards. (b) fails because a routine shove generally does not meet the "reasonable explanation" threshold for EED and misapplies the MPC standard to the concept of "negating malice." (c) uses an overbroad "all jurisdictions" claim that is factually incorrect regarding drug-trafficking statutes. (d) incorrectly labels manslaughter as a "justification" (which would lead to acquittal) rather than a mitigation. (e) relies on an "irrebuttable presumption" of a mental state, which is unconstitutional under Sandstrom v. Montana. However, the inclusion of the "drug transaction" in options (a) and (c) when it is absent from the prompt constitutes a factual inconsistency.

Falsifiable claim per distractor:
- (b): "legally negates his malice aforethought" — While provocation mitigates murder, a minor shove is legally insufficient to trigger this negation under the "reasonable explanation" test.
- (c): "automatically elevated to capital murder in all jurisdictions" — Felony murder and capital sentencing statutes vary by state and do not universally treat every drug-related death as capital murder.
- (d): "legally justified... under the mutual combat doctrine" — The mutual combat doctrine provides a mitigation to manslaughter (an excuse/partial justification), not a full legal justification (like self-defense).
- (e): "irrebuttable presumption of premeditation and deliberation" — Under the Due Process Clause, the law may allow for a permissive inference of intent from the use of a deadly weapon, but an irrebuttable presumption of an element of the crime is unconstitutional.

Recommended fix: Update the prompt to include the fact that the argument occurred during a "drug transaction" to ensure the stem matches the correct answer (a) and the distractor (c).
-->

## Issue 4 — argpass-opus

**Q6.** Assume Blake faces a homicide charge for the death of Chris. Blake argues that the charge should be reduced to voluntary manslaughter because he shot Chris only after Chris shoved him during a bitter argument. How should the court rule?

(a) Guilty of murder, because a verbal argument and a mere physical shove during a drug transaction are legally insufficient provocation to reduce the charge to manslaughter. <!-- correct -->
(b) Guilty of voluntary manslaughter, because the sudden physical shove triggered an extreme emotional disturbance that legally negates his malice aforethought.
(c) Guilty of murder, because any killing that occurs during the commission of a drug transaction is automatically elevated to capital murder in all jurisdictions.
(d) Guilty of voluntary manslaughter, because Chris's initial physical aggression legally justified Blake's use of a firearm under the mutual combat doctrine.
(e) Guilty of murder, because Blake used a deadly weapon, which creates an irrebuttable presumption of premeditation and deliberation under modern criminal law.

**Answer:** (a)

**Explanation:** Voluntary manslaughter requires adequate provocation (heat of passion) or, in MPC jurisdictions, an extreme emotional disturbance for which there is a reasonable explanation. A minor battery (a shove) during a bitter argument over a drug price is not legally adequate provocation to justify a lethal response and mitigate an intentional shooting from murder to manslaughter. (b) is wrong because the extreme emotional disturbance defense requires a "reasonable explanation or excuse," which is not satisfied by a routine shove in a drug deal. (c) is wrong because drug transactions do not automatically elevate all killings to capital murder in all jurisdictions. (d) is wrong because "mutual combat" requires a mutual physical fight, not a one-sided shove followed by a deadly escalation. (e) is wrong because the use of a deadly weapon supports an inference of intent to kill, not an irrebuttable presumption of premeditation.

**Tags:** chapters: [12, 13], topics: [homicide-grading], difficulty: medium, cognitive: application

**Grounding:** Chapter 12 (Intentional Homicide) - Heat of passion/provocation limits and the insufficiency of minor batteries to mitigate murder.

<!-- argument-pass: MUST FIX
(a) Argument-for: Option (a) correctly applies the common law rule of adequate provocation. Mere words (a bitter argument) and a minor physical battery (like a single shove) are historically and legally insufficient to constitute adequate provocation that would mitigate murder to voluntary manslaughter. Therefore, Blake remains guilty of murder.
(b) Argument-for: Under the Model Penal Code, voluntary manslaughter can be found if the defendant acted under an Extreme Emotional Disturbance (EED). A student might argue that a bitter argument coupled with a sudden physical shove could theoretically trigger such a disturbance subjectively, negating the malice aforethought required for murder and thus correctly grading the homicide as voluntary manslaughter.
(c) Argument-for: Felony murder rules elevate killings committed during certain inherently dangerous felonies to first-degree or capital murder. A student might argue that a drug transaction is a recognized inherently dangerous felony, and thus any killing during its commission automatically warrants a capital murder charge to deter violent drug trafficking.
(d) Argument-for: The mutual combat doctrine applies when parties enter into a sudden physical altercation. Because Chris initiated the physical aggression with a shove, a student could argue that this sparked mutual combat, thereby providing a legal basis to reduce the grading of the resulting homicide from murder to voluntary manslaughter.
(e) Argument-for: The deadly weapon doctrine allows a factfinder to infer an intent to kill when a defendant uses a deadly weapon on another person. A student might interpret this doctrine rigidly, believing it has hardened into an irrebuttable presumption of premeditation and deliberation under modern law to ensure convictions in clear-cut gun homicides.

Head-to-head:
Option (a) correctly identifies the legal outcome: a minor shove and an argument are insufficient to mitigate murder to manslaughter. However, (a) explicitly references a "drug transaction," a fact that is completely missing from the question stem (though it appears in the explanation). This makes the keyed answer factually defective, as students are trained not to assume facts not in evidence. The distractors successfully lock themselves into falsity: (b) claims a shove "legally negates" malice (it is a jury question at best, and EED does not formally "negate malice aforethought" in the jurisdiction-agnostic way described); (c) falsely claims "automatically... in all jurisdictions"; (d) falsely states the mutual combat doctrine "legally justified" the use of a firearm (justification results in an acquittal, whereas mutual combat only mitigates); and (e) explicitly invents an "irrebuttable presumption." Because the keyed answer relies on a hallucinated fact, the question is a MUST FIX.

Falsifiable claim per distractor:
- (b): "legally negates his malice aforethought" — wrong because a minor shove does not establish EED as a matter of law to automatically negate malice.
- (c): "automatically elevated to capital murder in all jurisdictions" — wrong because capital punishment and felony murder rules vary wildly by jurisdiction; there is no such universal rule.
- (d): "legally justified Blake's use of a firearm under the mutual combat doctrine" — wrong because mutual combat mitigates murder to manslaughter; it does not "legally justify" the use of deadly force (which would require self-defense and yield an acquittal).
- (e): "creates an irrebuttable presumption of premeditation and deliberation" — wrong because the deadly weapon rule at most allows a permissive inference of intent to kill, not an irrebuttable presumption of premeditation.

Recommended fix: Add "over a drug deal" to the question stem ("...because he shot Chris only after Chris shoved him during a bitter argument over a drug deal.").
-->
