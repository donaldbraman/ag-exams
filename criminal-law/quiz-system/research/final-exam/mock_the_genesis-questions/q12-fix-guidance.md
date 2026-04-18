# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Assume the court concludes that Albert is the legal cause of Chloe's death. The prosecution seeks a manslaughter conviction based on Albert's mental state regarding the risk of death. Which of the following best supports a finding of gross criminal negligence?

(a) Albert failed to correctly balance the chemical equation in his synthesis notes, which falls below the technical standard of care expected of a reasonable university chemistry professor.
(b) Albert consciously chose to handle highly volatile chemicals next to a public hallway despite knowing he was subject to sudden, severe, and uncontrollable physical muscle spasms. <!-- correct -->
(c) Albert knowingly violated the Chemical Act by failing to apply for a fire safety permit, making him strictly liable for any resulting deaths under the misdemeanor-manslaughter rule.
(d) Albert intended to secretly manufacture an illicit substance, which automatically transfers the specific intent from the underlying drug offense directly to the resulting homicide under common law.
(e) Albert's motivation for the operation was purely financial rather than a malicious desire to cause physical harm to his colleagues, which negates the mens rea for manslaughter.

**Answer:** (b)

**Explanation:** Gross criminal negligence requires a gross deviation from the standard of care that a reasonable person would observe, involving a substantial and unjustifiable risk of death. Handling highly volatile chemicals next to a public hallway while subject to severe, uncontrollable spasms demonstrates this extreme level of risk creation. (a) is incorrect because failing to balance an equation is ordinary professional negligence, which is insufficient for criminal manslaughter. (c) is incorrect because the misdemeanor-manslaughter rule requires the predicate misdemeanor to be the legal cause or malum in se; simple statutory silence does not establish strict liability for resulting deaths. (d) is incorrect because intent does not transfer between entirely different categories of offenses (from drug manufacturing to homicide). (e) is incorrect because manslaughter requires only gross negligence or recklessness, not a malicious desire to cause harm.

**Tags:** chapters: [13], topics: [unintentional homicide, gross-criminal-negligence, manslaughter], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, Unintentional Homicide — gross-criminal-negligence

<!-- audit: MUST FIX
<check 1>: SHOULD FIX. Option (b) establishes that Albert "consciously chose" to act "despite knowing" of his condition. This subjective awareness formally constitutes *recklessness* rather than negligence. While recklessness functionally satisfies the lower threshold of gross negligence, explicitly providing a reckless fact pattern to illustrate "gross criminal negligence" will frustrate well-prepared students who know the distinction.
<check 2>: pass
<check 3>: pass
<check 4>: pass
<check 5>: MUST FIX. The stem states the prosecution seeks a "manslaughter" conviction based on "gross criminal negligence." Under the MPC (`mpc-manslaughter-negligent-homicide-split`), gross negligence only supports Negligent Homicide, whereas manslaughter requires recklessness (or EED). The question conflates these and must explicitly specify a common law jurisdiction for gross criminal negligence to map to involuntary manslaughter.
<check 6>: pass
<check 7>: pass
Recommended fix: Add "Assume a common law jurisdiction" to the stem. In Option (b), consider changing "Consciously chose... despite knowing" to "Handled highly volatile chemicals next to a public hallway despite a documented medical history of sudden, severe, and uncontrollable physical muscle spasms," which better targets the objective "should-have-known" gross deviation standard without explicitly satisfying subjective recklessness.
-->

## Issue 2 — edge-case

**Q12.** Assume the court concludes that Albert is the legal cause of Chloe's death. The prosecution seeks a manslaughter conviction based on Albert's mental state regarding the risk of death. Which of the following best supports a finding of gross criminal negligence?

(a) Albert failed to correctly balance the chemical equation in his synthesis notes, which falls below the technical standard of care expected of a reasonable university chemistry professor.
(b) Albert consciously chose to handle highly volatile chemicals next to a public hallway despite knowing he was subject to sudden, severe, and uncontrollable physical muscle spasms. <!-- correct -->
(c) Albert knowingly violated the Chemical Act by failing to apply for a fire safety permit, making him strictly liable for any resulting deaths under the misdemeanor-manslaughter rule.
(d) Albert intended to secretly manufacture an illicit substance, which automatically transfers the specific intent from the underlying drug offense directly to the resulting homicide under common law.
(e) Albert's motivation for the operation was purely financial rather than a malicious desire to cause physical harm to his colleagues, which negates the mens rea for manslaughter.

**Answer:** (b)

**Explanation:** Gross criminal negligence requires a gross deviation from the standard of care that a reasonable person would observe, involving a substantial and unjustifiable risk of death. Handling highly volatile chemicals next to a public hallway while subject to severe, uncontrollable spasms demonstrates this extreme level of risk creation. (a) is incorrect because failing to balance an equation is ordinary professional negligence, which is insufficient for criminal manslaughter. (c) is incorrect because the misdemeanor-manslaughter rule requires the predicate misdemeanor to be the legal cause or malum in se; simple statutory silence does not establish strict liability for resulting deaths. (d) is incorrect because intent does not transfer between entirely different categories of offenses (from drug manufacturing to homicide). (e) is incorrect because manslaughter requires only gross negligence or recklessness, not a malicious desire to cause harm.

**Tags:** chapters: [13], topics: [unintentional homicide, gross-criminal-negligence, manslaughter], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, Unintentional Homicide — gross-criminal-negligence

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: Mild factual discrepancy—Fact 11 states Chloe was in an "adjacent hallway," but Option B says "public hallway." Changing it to "adjacent hallway" prevents hyper-technical student complaints.
2. Cross-Doctrine Clashes: The question explicitly asks for "gross criminal negligence," but Option B's phrasing ("consciously chose... despite knowing") defines subjective *Recklessness*. While recklessness legally satisfies a negligence standard, this phrasing may confuse top students trying to apply strict MPC mental state boundaries.
3. Cross-Question Spoilers: Option B explicitly spells out the "prior voluntary act" logic needed to defeat the involuntary act defense in Q8 (time-framing). It hands the student the exact answer to Q8 by highlighting the conscious choice that preceded the involuntary spasm.
Recommended fix: Revise Option B to: "Albert proceeded to handle highly volatile chemicals near an adjacent hallway despite having recently experienced severe medication-induced spasms, representing an extreme deviation from a reasonable standard of care." This keeps the focus on objective negligence and softens the Q8 time-framing spoiler.
-->

## Issue 3 — argpass-sonnet

**Q12.** Assume the court concludes that Albert is the legal cause of Chloe's death. The prosecution seeks a manslaughter conviction based on Albert's mental state regarding the risk of death. Which of the following best supports a finding of gross criminal negligence?

(a) Albert failed to correctly balance the chemical equation in his synthesis notes, which falls below the technical standard of care expected of a reasonable university chemistry professor.
(b) Albert consciously chose to handle highly volatile chemicals next to a public hallway despite knowing he was subject to sudden, severe, and uncontrollable physical muscle spasms. <!-- correct -->
(c) Albert knowingly violated the Chemical Act by failing to apply for a fire safety permit, making him strictly liable for any resulting deaths under the misdemeanor-manslaughter rule.
(d) Albert intended to secretly manufacture an illicit substance, which automatically transfers the specific intent from the underlying drug offense directly to the resulting homicide under common law.
(e) Albert's motivation for the operation was purely financial rather than a malicious desire to cause physical harm to his colleagues, which negates the mens rea for manslaughter.

**Answer:** (b)

**Explanation:** Gross criminal negligence requires a gross deviation from the standard of care that a reasonable person would observe, involving a substantial and unjustifiable risk of death. Handling highly volatile chemicals next to a public hallway while subject to severe, uncontrollable spasms demonstrates this extreme level of risk creation. (a) is incorrect because failing to balance an equation is ordinary professional negligence, which is insufficient for criminal manslaughter. (c) is incorrect because the misdemeanor-manslaughter rule requires the predicate misdemeanor to be the legal cause or malum in se; simple statutory silence does not establish strict liability for resulting deaths. (d) is incorrect because intent does not transfer between entirely different categories of offenses (from drug manufacturing to homicide). (e) is incorrect because manslaughter requires only gross negligence or recklessness, not a malicious desire to cause harm.

**Tags:** chapters: [13], topics: [unintentional homicide, gross-criminal-negligence, manslaughter], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, Unintentional Homicide — gross-criminal-negligence

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Gross criminal negligence involves a deviation from the standard of care expected of a reasonable person in the actor's situation. For a university chemistry professor, the standard of care includes technical precision in formulating chemical reactions. Failing to correctly balance a chemical equation before synthesizing volatile chemicals creates a substantial risk of a fatal explosion. A student could argue that this extreme technical failure by a professional clearly breaches their elevated duty of care, thereby supporting a finding of gross criminal negligence.
(b) Argument-for: Gross criminal negligence requires a gross deviation from the standard of care, often involving the creation of a substantial and unjustifiable risk of death. Handling highly volatile chemicals near a public hallway while knowing one is subject to severe, uncontrollable muscle spasms is an extreme risk to others. A student would rightly conclude that consciously disregarding this profound physical limitation while engaged in an ultra-hazardous activity provides the strongest factual basis for finding a gross deviation from the standard of care.
(c) Argument-for: The misdemeanor-manslaughter rule allows a manslaughter conviction when a death results from the commission of an unlawful act. By knowingly violating the Chemical Act's permit requirement, Albert committed an unlawful act that led to a fatal fire. A student could argue that this regulatory violation triggers strict liability for the resulting death, perfectly substituting for the gross criminal negligence mens rea under the unlawful-act manslaughter doctrine.
(d) Argument-for: Under the doctrine of transferred intent, the mens rea for an underlying offense can sometimes establish the fault required for a resulting homicide. Albert intended to secretly manufacture an illicit substance, an inherently dangerous activity. A student could argue that common law automatically transfers the specific intent from this illicit drug manufacturing directly to the homicide, fulfilling the fault requirement and establishing gross criminal negligence.
(e) Argument-for: Manslaughter requires a specific degree of fault, such as gross negligence or recklessness, but not malice aforethought. A purely financial motivation demonstrates that Albert did not possess a malicious desire to cause physical harm. A student could argue that establishing this lack of malice is essential to negate a murder charge, thus affirmatively supporting a manslaughter finding by ruling out higher degrees of culpability.

Head-to-head: Option (b) is the correct answer because it provides the strongest factual scenario for a gross deviation from the standard of care, explicitly combining a highly dangerous act with an uncontrollable physical condition. Options (c), (d), and (e) are strong distractors because they invoke real criminal law concepts (misdemeanor-manslaughter, transferred intent, and malice aforethought) but apply them incorrectly using explicitly falsifiable legal claims. Distractor (a), however, merely describes ordinary professional negligence and correctly notes that it "falls below the technical standard of care." While factually weaker than (b) as support for *gross* negligence, (a) lacks an explicitly false legal claim or absolute language declaring that ordinary negligence legally suffices for manslaughter, violating the close-call standard.

Falsifiable claim per distractor:
- (a): None. The option truthfully states that failing to balance an equation "falls below the technical standard of care expected of a reasonable university chemistry professor," which accurately describes ordinary negligence but lacks an explicit false legal claim regarding gross negligence.
- (c): "making him strictly liable for any resulting deaths under the misdemeanor-manslaughter rule" — wrong because regulatory permit violations (malum prohibitum) do not automatically trigger strict liability for homicide without a showing of proximate cause and foreseeability of death.
- (d): "automatically transfers the specific intent from the underlying drug offense directly to the resulting homicide under common law" — wrong because intent does not categorically transfer from a drug manufacturing offense to establish gross criminal negligence.
- (e): "which negates the mens rea for manslaughter" — wrong because an absence of malice or a purely financial motivation does not negate the mens rea for manslaughter (which relies on gross negligence or recklessness, not malice).

Recommended fix: Change (a) to: "Albert failed to correctly balance the chemical equation in his synthesis notes, which categorically establishes gross criminal negligence solely because it breached a professional standard of care."
-->

## Issue 4 — argpass-opus

**Q12.** Assume the court concludes that Albert is the legal cause of Chloe's death. The prosecution seeks a manslaughter conviction based on Albert's mental state regarding the risk of death. Which of the following best supports a finding of gross criminal negligence?

(a) Albert failed to correctly balance the chemical equation in his synthesis notes, which falls below the technical standard of care expected of a reasonable university chemistry professor.
(b) Albert consciously chose to handle highly volatile chemicals next to a public hallway despite knowing he was subject to sudden, severe, and uncontrollable physical muscle spasms. <!-- correct -->
(c) Albert knowingly violated the Chemical Act by failing to apply for a fire safety permit, making him strictly liable for any resulting deaths under the misdemeanor-manslaughter rule.
(d) Albert intended to secretly manufacture an illicit substance, which automatically transfers the specific intent from the underlying drug offense directly to the resulting homicide under common law.
(e) Albert's motivation for the operation was purely financial rather than a malicious desire to cause physical harm to his colleagues, which negates the mens rea for manslaughter.

**Answer:** (b)

**Explanation:** Gross criminal negligence requires a gross deviation from the standard of care that a reasonable person would observe, involving a substantial and unjustifiable risk of death. Handling highly volatile chemicals next to a public hallway while subject to severe, uncontrollable spasms demonstrates this extreme level of risk creation. (a) is incorrect because failing to balance an equation is ordinary professional negligence, which is insufficient for criminal manslaughter. (c) is incorrect because the misdemeanor-manslaughter rule requires the predicate misdemeanor to be the legal cause or malum in se; simple statutory silence does not establish strict liability for resulting deaths. (d) is incorrect because intent does not transfer between entirely different categories of offenses (from drug manufacturing to homicide). (e) is incorrect because manslaughter requires only gross negligence or recklessness, not a malicious desire to cause harm.

**Tags:** chapters: [13], topics: [unintentional homicide, gross-criminal-negligence, manslaughter], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, Unintentional Homicide — gross-criminal-negligence

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that as a university chemistry professor, Albert is held to an elevated, specialized standard of care. Failing to balance a chemical equation involving dangerous compounds represents a shocking abdication of professional duties. Because this error inherently risks an explosion, a student might reason that this technical failure constitutes a gross deviation from the standard of care, thereby satisfying the requirement for gross criminal negligence.
(b) Argument-for: A student would recognize that handling highly volatile chemicals in a trafficked area (a public hallway) while suffering from uncontrollable spasms creates a massive, unjustified risk of a fatal accident. The fact that Albert "consciously chose" to do this despite "knowing" his condition proves extreme risk creation. Because subjective recklessness legally subsumes the objective standard of gross criminal negligence, these facts powerfully and directly support the prosecution's required mental state for manslaughter.
(c) Argument-for: A student could conflate gross criminal negligence with the misdemeanor-manslaughter (unlawful act) doctrine. If Albert knowingly violated a fire safety statute, a student might argue this unlawful omission is inherently dangerous. Therefore, they could conclude that the statutory violation triggers strict liability for any resulting deaths, effectively substituting for the gross negligence mens rea required for an involuntary manslaughter conviction.
(d) Argument-for: A student might rely on a misunderstanding of transferred intent or the felony-murder rule. They could argue that the intent to commit a dangerous illicit act (manufacturing drugs) supplies the necessary culpable mental state for any resulting harm. Under this logic, the specific intent to manufacture the substance automatically transfers to the homicide, satisfying the mens rea requirement without needing a separate negligence analysis.
(e) Argument-for: A student might argue that criminal liability requires a culpable mental state directed specifically at the resulting harm. If Albert's motive was "purely financial" and he had no malicious desire to cause physical harm, a student might mistakenly reason that this absence of malice defeats a finding of gross negligence or recklessness. They would conclude that an innocent or collateral motive negates the mens rea required for manslaughter.

Head-to-head: Option (b) is the clear winner because handling explosive chemicals in a public space while suffering from uncontrollable physical spasms easily satisfies the "substantial and unjustifiable risk" and "gross deviation" requirements of criminal negligence. However, Option (a) is structurally weak as a distractor. It relies merely on being factually "less severe" (ordinary negligence) than (b), rather than containing an explicitly false legal claim. Options (c), (d), and (e) all appropriately contain explicitly false statements of criminal law (strict liability for malum prohibitum omissions, improperly transferring specific intent across crime categories, and conflating motive with mens rea). 

Falsifiable claim per distractor:
- (a): None. The statement "falls below the technical standard of care..." is factually and legally true (it is ordinary negligence), making this option incorrect merely by degree rather than by containing an identifiable false legal claim.
- (c): "making him strictly liable for any resulting deaths under the misdemeanor-manslaughter rule" — wrong because regulatory omissions (malum prohibitum) do not trigger strict liability for homicide without proximate cause and foreseeability of death.
- (d): "automatically transfers the specific intent from the underlying drug offense directly to the resulting homicide" — wrong because transferred intent applies to intended harms against different victims, not transferring specific intent between entirely different crime categories.
- (e): "which negates the mens rea for manslaughter" — wrong because manslaughter requires only gross negligence or recklessness, which are not legally negated by the presence of a financial motive or the absence of malicious desire.

Recommended fix: Add an absolute legal claim to (a) to ensure it is falsifiable. 
Change (a) to: "Albert failed to correctly balance the chemical equation in his synthesis notes, which automatically constitutes gross criminal negligence because it falls below the technical standard of care expected of a reasonable university chemistry professor."
-->
