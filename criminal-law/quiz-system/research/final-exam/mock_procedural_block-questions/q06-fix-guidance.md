# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** Assume the jurisdiction has abolished the felony murder rule. What is the most appropriate homicide charge for Silas regarding the pedestrian's death under the Model Penal Code?

(a) Murder, because driving 90 mph erratically through a crowded residential neighborhood demonstrates extreme indifference to the value of human life, establishing recklessness equivalent to malice. <!-- correct -->
(b) Negligent homicide, because Silas merely failed to perceive the risk of hitting a pedestrian while he was focused on escaping the pursuing police officers.
(c) Murder, because Silas's decision to flee inherently proves he specifically premeditated and deliberated the pedestrian's eventual death prior to the crash.
(d) Manslaughter, because the stress of the police pursuit constitutes a reasonable explanation or excuse, reducing the homicide from murder to extreme emotional disturbance.
(e) No homicide charge is applicable, because without the felony murder rule, an unintentional killing during a traffic flight cannot be classified as a criminal homicide.

**Answer:** (a)

**Explanation:** Under the MPC, a homicide committed recklessly under circumstances manifesting an extreme indifference to the value of human life is classified as murder (often called depraved heart murder). Driving 90 mph erratically in a residential area perfectly fits this standard. (b) is wrong because his conduct goes far beyond a mere failure to perceive a risk (negligence); it constitutes conscious disregard of a massive risk. (c) is wrong because premeditation requires actual intent and reflection to kill the specific victim, not just dangerous flight. (d) is wrong because EED requires a reasonable explanation or excuse for the disturbance, which fleeing a lawful police stop does not provide. (e) is wrong because unintentional killings can still be punished as extreme indifference murder or manslaughter depending on the degree of recklessness.

**Tags:** chapters: [13], topics: [homicide-grading, extreme-indifference-murder, model-penal-code], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 13, Section: Extreme Indifference Murder

<!-- audit: SHOULD FIX
check 1: pass (though option (a) unnecessarily introduces the common law term "malice" into an explicitly MPC question)
check 2: pass
check 3: explanation drift. The question explicitly asks for the charge under the MPC, but the explanation for (c) evaluates premeditation under common law rules ("premeditation requires actual intent...") instead of pointing out that the MPC explicitly rejected the premeditation/deliberation formula for grading murder (per the `mpc-no-premeditation` tag).
check 4: pass
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Remove "equivalent to malice" from option (a), as the MPC explicitly abolished the malice concept. Update the explanation for (c) to state that the MPC does not use premeditation/deliberation to grade murder, and that his conduct was reckless, not purposeful/knowing.
-->

## Issue 2 — edge-case

**Q6.** Assume the jurisdiction has abolished the felony murder rule. What is the most appropriate homicide charge for Silas regarding the pedestrian's death under the Model Penal Code?

(a) Murder, because driving 90 mph erratically through a crowded residential neighborhood demonstrates extreme indifference to the value of human life, establishing recklessness equivalent to malice. <!-- correct -->
(b) Negligent homicide, because Silas merely failed to perceive the risk of hitting a pedestrian while he was focused on escaping the pursuing police officers.
(c) Murder, because Silas's decision to flee inherently proves he specifically premeditated and deliberated the pedestrian's eventual death prior to the crash.
(d) Manslaughter, because the stress of the police pursuit constitutes a reasonable explanation or excuse, reducing the homicide from murder to extreme emotional disturbance.
(e) No homicide charge is applicable, because without the felony murder rule, an unintentional killing during a traffic flight cannot be classified as a criminal homicide.

**Answer:** (a)

**Explanation:** Under the MPC, a homicide committed recklessly under circumstances manifesting an extreme indifference to the value of human life is classified as murder (often called depraved heart murder). Driving 90 mph erratically in a residential area perfectly fits this standard. (b) is wrong because his conduct goes far beyond a mere failure to perceive a risk (negligence); it constitutes conscious disregard of a massive risk. (c) is wrong because premeditation requires actual intent and reflection to kill the specific victim, not just dangerous flight. (d) is wrong because EED requires a reasonable explanation or excuse for the disturbance, which fleeing a lawful police stop does not provide. (e) is wrong because unintentional killings can still be punished as extreme indifference murder or manslaughter depending on the degree of recklessness.

**Tags:** chapters: [13], topics: [homicide-grading, extreme-indifference-murder, model-penal-code], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 13, Section: Extreme Indifference Murder

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: The correct answer (a) uses the phrase "recklessness equivalent to malice" while explicitly testing the Model Penal Code. The MPC intentionally abolished the concept and terminology of "malice." While the rest of the answer correctly identifies the "extreme indifference" standard, blending in common law "malice" terminology in an explicitly MPC question is doctrinally messy and serves as a booby trap for high-performing students who know the MPC rejected malice aforethought.
3. Cross-Question Spoilers: pass
Recommended fix: In option (a), remove the phrase "equivalent to malice." Change it to something like "...demonstrates extreme indifference to the value of human life, establishing the requisite extreme recklessness for murder."
-->

## Issue 3 — argpass-sonnet

**Q6.** Assume the jurisdiction has abolished the felony murder rule. What is the most appropriate homicide charge for Silas regarding the pedestrian's death under the Model Penal Code?

(a) Murder, because driving 90 mph erratically through a crowded residential neighborhood demonstrates extreme indifference to the value of human life, establishing recklessness equivalent to malice. <!-- correct -->
(b) Negligent homicide, because Silas merely failed to perceive the risk of hitting a pedestrian while he was focused on escaping the pursuing police officers.
(c) Murder, because Silas's decision to flee inherently proves he specifically premeditated and deliberated the pedestrian's eventual death prior to the crash.
(d) Manslaughter, because the stress of the police pursuit constitutes a reasonable explanation or excuse, reducing the homicide from murder to extreme emotional disturbance.
(e) No homicide charge is applicable, because without the felony murder rule, an unintentional killing during a traffic flight cannot be classified as a criminal homicide.

**Answer:** (a)

**Explanation:** Under the MPC, a homicide committed recklessly under circumstances manifesting an extreme indifference to the value of human life is classified as murder (often called depraved heart murder). Driving 90 mph erratically in a residential area perfectly fits this standard. (b) is wrong because his conduct goes far beyond a mere failure to perceive a risk (negligence); it constitutes conscious disregard of a massive risk. (c) is wrong because premeditation requires actual intent and reflection to kill the specific victim, not just dangerous flight. (d) is wrong because EED requires a reasonable explanation or excuse for the disturbance, which fleeing a lawful police stop does not provide. (e) is wrong because unintentional killings can still be punished as extreme indifference murder or manslaughter depending on the degree of recklessness.

**Tags:** chapters: [13], topics: [homicide-grading, extreme-indifference-murder, model-penal-code], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 13, Section: Extreme Indifference Murder

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under MPC § 210.2(1)(b), a criminal homicide constitutes murder when committed recklessly under circumstances manifesting an extreme indifference to the value of human life. A student could argue that driving 90 mph erratically in a crowded residential area presents a profound and obvious risk to human life that perfectly fits this standard. The phrase "equivalent to malice" accurately translates the MPC's standard into the common law "depraved heart" framework that the MPC provision was specifically designed to codify. Therefore, murder is the most appropriate charge.
(b) Argument-for: A student could argue that "negligent homicide" is correct because the prompt does not explicitly state Silas's subjective mental state. Under the MPC, if a defendant genuinely fails to perceive a substantial and unjustifiable risk—perhaps due to intense hyperfocus on escaping the police—his mens rea is negligence, not recklessness. Because a jury could theoretically find that his attention was entirely consumed by the pursuit, treating his failure to perceive the pedestrian as negligent homicide is a legally plausible application of MPC § 210.4.
(c) Argument-for: A student might defend (c) by equating extreme, deliberate risk-taking with specific premeditation. The decision to flee at 90 mph in a residential area is a conscious, ongoing choice. A student could argue that this continuous, deliberate operation of a vehicle in a manner practically certain to cause death inherently satisfies the requirement for premeditation and deliberation, as the driver has ample time to reflect on the deadly consequences of the flight prior to the crash.
(d) Argument-for: Under the MPC, murder is reduced to manslaughter if committed under extreme mental or emotional disturbance (EED) for which there is a reasonable explanation or excuse. A student could argue that a high-speed police chase induces severe, involuntary physiological panic and stress. Viewing the situation from the actor's panicked perspective, this overwhelming emotional disturbance explains his erratic driving, arguably making manslaughter the appropriate mitigated charge under MPC § 210.3.
(e) Argument-for: If the jurisdiction has abolished the felony murder rule, a student could conclude that any unintentional death occurring during the commission of a felony (such as fleeing police) can no longer be charged as homicide. The argument assumes that without the felony murder doctrine to impute malice or intent, traffic-related deaths must be prosecuted under specialized vehicular statutes rather than general criminal homicide, rendering general homicide charges inapplicable to accidental flight deaths.

Head-to-head: 
Option (a) correctly maps the extreme facts to the MPC's "extreme indifference" murder standard, though its use of the word "malice" is a technical common-law intrusion into an MPC question. Option (c) is easily dismissed because it relies on the falsifiable legal claim that flight "inherently proves" specific premeditation. Option (d) asserts as a matter of law that police pursuit stress "constitutes a reasonable explanation," which courts uniformly reject. Option (e) provides a clear falsifiable absolute ("cannot be classified"). Option (b), however, is flawed as a distractor under the strict close-call standard. Instead of stating an identifiable, absolute false legal rule, it relies on a purely factual assumption ("because Silas merely failed to perceive") that does not contain a legally falsifiable mechanism. The question requires a fix to make (b)'s legal error explicit and to clean up the terminology in (a).

Falsifiable claim per distractor:
- (b): "because Silas merely failed to perceive the risk" — lacks a false legal claim; this is a factual assertion about the defendant's mental state rather than a universally falsifiable proposition of law.
- (c): "inherently proves he specifically premeditated" — wrong because engaging in reckless flight does not legally equate to or automatically prove the specific intent and reflection required for premeditation.
- (d): "the stress of the police pursuit constitutes a reasonable explanation" — wrong because criminal flight from law enforcement categorically cannot serve as a "reasonable" explanation or excuse for EED under the MPC.
- (e): "an unintentional killing during a traffic flight cannot be classified as a criminal homicide" — wrong because unintentional killings can unconditionally be charged as manslaughter or extreme indifference murder depending solely on the degree of recklessness.

Recommended fix: Edit (b) to include a falsifiable legal claim: "Negligent homicide, because a driver fleeing police categorically lacks the subjective awareness required to establish recklessness." Edit (a) to remove common-law terminology: "...demonstrates extreme indifference to the value of human life, establishing the required aggravated recklessness."
-->

## Issue 4 — argpass-opus

**Q6.** Assume the jurisdiction has abolished the felony murder rule. What is the most appropriate homicide charge for Silas regarding the pedestrian's death under the Model Penal Code?

(a) Murder, because driving 90 mph erratically through a crowded residential neighborhood demonstrates extreme indifference to the value of human life, establishing recklessness equivalent to malice. <!-- correct -->
(b) Negligent homicide, because Silas merely failed to perceive the risk of hitting a pedestrian while he was focused on escaping the pursuing police officers.
(c) Murder, because Silas's decision to flee inherently proves he specifically premeditated and deliberated the pedestrian's eventual death prior to the crash.
(d) Manslaughter, because the stress of the police pursuit constitutes a reasonable explanation or excuse, reducing the homicide from murder to extreme emotional disturbance.
(e) No homicide charge is applicable, because without the felony murder rule, an unintentional killing during a traffic flight cannot be classified as a criminal homicide.

**Answer:** (a)

**Explanation:** Under the MPC, a homicide committed recklessly under circumstances manifesting an extreme indifference to the value of human life is classified as murder (often called depraved heart murder). Driving 90 mph erratically in a residential area perfectly fits this standard. (b) is wrong because his conduct goes far beyond a mere failure to perceive a risk (negligence); it constitutes conscious disregard of a massive risk. (c) is wrong because premeditation requires actual intent and reflection to kill the specific victim, not just dangerous flight. (d) is wrong because EED requires a reasonable explanation or excuse for the disturbance, which fleeing a lawful police stop does not provide. (e) is wrong because unintentional killings can still be punished as extreme indifference murder or manslaughter depending on the degree of recklessness.

**Tags:** chapters: [13], topics: [homicide-grading, extreme-indifference-murder, model-penal-code], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 13, Section: Extreme Indifference Murder

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under Model Penal Code § 210.2(1)(b), criminal homicide constitutes murder when it is committed recklessly under circumstances manifesting extreme indifference to the value of human life. Driving 90 mph erratically through a crowded residential neighborhood perfectly satisfies this standard, as it demonstrates a conscious disregard of a substantial and unjustifiable risk to human life. The phrase "equivalent to malice" helps analogize this MPC standard to the common law concept of depraved heart murder, establishing the requisite mens rea. Therefore, this represents the most legally sound and doctrinally appropriate charge.
(b) Argument-for: A student could argue that Silas's primary focus was entirely on the police pursuit, blinding him to the secondary risks of his driving. Under MPC § 2.02(2)(d), a person acts negligently when he should be aware of a substantial and unjustifiable risk. If the stress of the chase caused Silas to literally fail to consciously perceive the risk to the pedestrian, his conduct meets the MPC's standard for negligent homicide. This option correctly identifies the failure to perceive a risk as the legal hallmark of negligence.
(c) Argument-for: Engaging in an inherently dangerous evasion tactic with a massive probability of death could be construed as demonstrating specific intent. A student might argue that the conscious decision to drive 90 mph in a crowded neighborhood is practically certain to cause death, satisfying the MPC's "knowingly" standard for murder. Furthermore, one could argue that planning such a lethal flight path "inherently proves" a level of deliberation comparable to premeditation, justifying the highest degree of murder available.
(d) Argument-for: Under MPC § 210.3, murder can be downgraded to manslaughter if committed under the influence of an extreme emotional disturbance (EED) for which there is a reasonable explanation or excuse. A student could argue that the terror, adrenaline, and stress of a high-speed police pursuit induces a genuine state of extreme emotional disturbance. Because the MPC assesses reasonableness from the viewpoint of a person in the actor's situation, a jury could conceivably find that Silas's panic provides a reasonable excuse for his emotional state.
(e) Argument-for: Without the felony murder rule, a jurisdiction requires strict adherence to mens rea specifically for the homicide itself. A student could argue that while traffic flights are reckless, absent a predicate felony to automatically elevate intent, an entirely accidental crash cannot satisfy the independent mens rea for murder or manslaughter. This argument relies on the premise that a mere traffic violation, even vehicular flight, categorically precludes homicide liability without the scaffolding of the felony murder doctrine.

Head-to-head: Option (a) is the strongest because it correctly applies the MPC standard for "extreme indifference" murder to the facts. However, it contains a minor doctrinal flaw by appending the phrase "equivalent to malice," since the MPC explicitly abolished the concept of malice aforethought. Despite this, the distractors all fail due to strict, falsifiable legal errors. Option (b) makes the unsupportable claim that Silas "merely failed to perceive" the risk, which is legally defeated by the objective recklessness of driving 90 mph in a residential area. Option (c) wrongly claims flight "inherently proves" specific premeditation. Option (d) falsely asserts that fleeing lawful arrest constitutes a legally "reasonable" explanation for EED. Option (e) relies on the easily falsifiable absolute claim that unintentional flight killings "cannot be classified" as criminal homicide. 

Falsifiable claim per distractor:
- (b): "merely failed to perceive the risk" — wrong because driving 90 mph erratically in a crowded residential area constitutes conscious disregard (recklessness) as a matter of law, precluding a "mere failure to perceive" (negligence) defense.
- (c): "inherently proves he specifically premeditated" — wrong because premeditation requires actual reflection and intent to kill, which is categorically not "inherently proven" by the mere act of dangerous flight.
- (d): "constitutes a reasonable explanation or excuse" — wrong because the stress of fleeing a lawful police pursuit is legally categorically excluded as a "reasonable" excuse to trigger an Extreme Emotional Disturbance mitigation under the MPC.
- (e): "cannot be classified as a criminal homicide" — wrong because unintentional killings are routinely classified as criminal homicide (e.g., reckless murder, manslaughter) irrespective of the existence of the felony murder rule.

Recommended fix: Remove the phrase ", establishing recklessness equivalent to malice" from option (a) to ensure strict adherence to the Model Penal Code, which intentionally abolished malice terminology.
-->
