# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Assume the jurisdiction has adopted accomplice felony murder reforms identical to California's SB 1437. Can Leo be convicted of felony murder for Wendy's death?

(a) Yes, because acting as the designated getaway driver in a high-speed pursuit inherently establishes a reckless indifference to human life.
(b) Yes, because Leo was an active participant in the underlying felony and had prior knowledge that his co-felon Dom was heavily armed.
(c) No, because Leo was neither the actual killer, nor did he act with intent to kill or as a legally defined major participant. <!-- correct -->
(d) No, because Leo did not personally steal any property or cause any injuries during the initial execution of the attempted hijacking operation.
(e) No, because the death was directly caused by a pursuing police officer, which automatically bars felony murder liability for all involved participants.

**Answer:** (c)

**Explanation:** California's SB 1437 restricts felony murder liability for non-killers. To be convicted, the defendant must be the actual killer, act with intent to kill, or be a "major participant" who acts with "reckless indifference to human life." Simply acting as a getaway driver does not automatically satisfy this stringent standard. Option (a) is wrong because the statute requires a fact-specific inquiry, rejecting the premise that driving inherently establishes reckless indifference. Option (b) is wrong because active participation and knowledge of a weapon do not automatically elevate a defendant to a major participant. Option (d) is wrong because failing to personally steal property does not immunize a defendant if the legal criteria are met. Option (e) is wrong because SB 1437 focuses on the defendant's specific mental state, not just the agency of the killer.

**Tags:** chapters: [14], topics: [felony murder, accomplice liability, major participant, sb 1437], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14: sb-1437-major-participant

<!-- audit: MUST FIX
check 1: fail. Without a fact pattern, we cannot know if Leo meets the "major participant" and "reckless indifference" criteria.
check 2: fail. Because the facts are missing, students cannot definitively rule out distractors. Additionally, if the missing facts stipulate a police officer killed Wendy, option (e) would actually be a strong distractor or potentially correct under California's agency rule for felony murder.
check 3: fail. The explanation for (e) misstates doctrine. California follows the agency theory of felony murder; if a police officer kills someone, it is generally a bar to felony murder (though implied malice "Provocative Act" murder may apply). The explanation wrongly implies felony murder could apply regardless of the killer's agency if SB 1437's mental state is met.
check 4: fail. The question is entirely missing its fact pattern. It references Leo, Dom, Wendy, a high-speed pursuit, and an attempted hijacking, but none of this is described in the stem.
check 5: pass. Explicitly specifies CA SB 1437.
check 6: pass. No excluded topics triggered.
check 7: pass. Maps to Chapter 14 `sb-1437-major-participant`.
Recommended fix: Insert the missing fact pattern detailing Leo's exact role in the attempted hijacking, Dom's actions, and the circumstances of Wendy's death. Ensure the facts clearly position Leo as a minor participant (e.g., merely waiting in the car, unaware of specific lethal risks) to make (c) factually accurate. Revise option (e) and its explanation to avoid conflating the agency rule of felony murder with SB 1437 reforms.
-->

## Issue 2 — edge-case

**Q12.** Assume the jurisdiction has adopted accomplice felony murder reforms identical to California's SB 1437. Can Leo be convicted of felony murder for Wendy's death?

(a) Yes, because acting as the designated getaway driver in a high-speed pursuit inherently establishes a reckless indifference to human life.
(b) Yes, because Leo was an active participant in the underlying felony and had prior knowledge that his co-felon Dom was heavily armed.
(c) No, because Leo was neither the actual killer, nor did he act with intent to kill or as a legally defined major participant. <!-- correct -->
(d) No, because Leo did not personally steal any property or cause any injuries during the initial execution of the attempted hijacking operation.
(e) No, because the death was directly caused by a pursuing police officer, which automatically bars felony murder liability for all involved participants.

**Answer:** (c)

**Explanation:** California's SB 1437 restricts felony murder liability for non-killers. To be convicted, the defendant must be the actual killer, act with intent to kill, or be a "major participant" who acts with "reckless indifference to human life." Simply acting as a getaway driver does not automatically satisfy this stringent standard. Option (a) is wrong because the statute requires a fact-specific inquiry, rejecting the premise that driving inherently establishes reckless indifference. Option (b) is wrong because active participation and knowledge of a weapon do not automatically elevate a defendant to a major participant. Option (d) is wrong because failing to personally steal property does not immunize a defendant if the legal criteria are met. Option (e) is wrong because SB 1437 focuses on the defendant's specific mental state, not just the agency of the killer.

**Tags:** chapters: [14], topics: [felony murder, accomplice liability, major participant, sb 1437], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14: sb-1437-major-participant

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Because the facts state Dom "abandoned the plan entirely without touching the truck" (which Q8 and Q9 test for attempt and abandonment defenses), a student might correctly conclude there is no underlying felony of "attempted hijacking." If there is no underlying felony, felony murder fails outright at step one, meaning the actual reason Leo cannot be convicted is the absence of a felony, rendering Choice (c)'s major-participant rationale technically secondary or moot. 
2. Cross-Doctrine Clashes: Choice (e) perfectly describes the "Agency Rule" of felony murder (liability is categorically barred if a non-felon, like a police officer, kills the victim). Because the prompt explicitly cites "California's SB 1437," it strongly signals California law, which strictly follows the Agency Rule (*People v. Washington*). To a student who knows California law, Choice (e) is a completely correct statement of law and an absolute bar to liability. Furthermore, the explanation for (e) is legally unsound; SB 1437 does not override the agency rule. 
3. Cross-Question Spoilers: The preceding question in the package (testing the *Smith* proximate cause rule for Dom) establishes that this exam universe actually uses the proximate cause theory for felony murder. However, this proximate cause reality directly clashes with this question's strong implication of California's agency rule.
Recommended fix: Add two assumptions to the prompt: "Assume for this question that Dom's actions constituted a valid attempted hijacking, and that the jurisdiction uses the proximate cause theory for felony murder but has adopted accomplice reforms identical to California's SB 1437." Then, revise the explanation for (e) to state: "Option (e) is wrong because the jurisdiction uses the proximate cause theory, which allows felony murder liability even when a police officer is the direct cause of death; thus, Leo's only defense is the SB 1437 major participant standard."
-->

## Issue 3 — argpass-sonnet

**Q12.** Assume the jurisdiction has adopted accomplice felony murder reforms identical to California's SB 1437. Can Leo be convicted of felony murder for Wendy's death?

(a) Yes, because acting as the designated getaway driver in a high-speed pursuit inherently establishes a reckless indifference to human life.
(b) Yes, because Leo was an active participant in the underlying felony and had prior knowledge that his co-felon Dom was heavily armed.
(c) No, because Leo was neither the actual killer, nor did he act with intent to kill or as a legally defined major participant. <!-- correct -->
(d) No, because Leo did not personally steal any property or cause any injuries during the initial execution of the attempted hijacking operation.
(e) No, because the death was directly caused by a pursuing police officer, which automatically bars felony murder liability for all involved participants.

**Answer:** (c)

**Explanation:** California's SB 1437 restricts felony murder liability for non-killers. To be convicted, the defendant must be the actual killer, act with intent to kill, or be a "major participant" who acts with "reckless indifference to human life." Simply acting as a getaway driver does not automatically satisfy this stringent standard. Option (a) is wrong because the statute requires a fact-specific inquiry, rejecting the premise that driving inherently establishes reckless indifference. Option (b) is wrong because active participation and knowledge of a weapon do not automatically elevate a defendant to a major participant. Option (d) is wrong because failing to personally steal property does not immunize a defendant if the legal criteria are met. Option (e) is wrong because SB 1437 focuses on the defendant's specific mental state, not just the agency of the killer.

**Tags:** chapters: [14], topics: [felony murder, accomplice liability, major participant, sb 1437], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14: sb-1437-major-participant

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that serving as a getaway driver in a high-speed pursuit demonstrates a profound, objective disregard for human life. Under the *Banks/Clark* continuum, taking actions that dramatically increase the risk of lethal consequences—like fleeing police at high speeds—weighs heavily toward reckless indifference. Therefore, the student could conclude that the act of driving the getaway car inherently meets the standard for reckless indifference required by SB 1437.
(b) Argument-for: A student might justify this option by noting that knowledge of a co-felon's weapon is a key factor in the California Supreme Court's *Banks/Clark* analysis. Because Leo was an "active participant" and knew Dom was heavily armed, a student might infer that Leo accepted the high risk of a lethal encounter. They would argue this combination of active involvement and knowledge of a loaded weapon is legally sufficient to independently sustain a conviction under SB 1437.
(c) Argument-for: This option explicitly tracks the statutory requirements of California Penal Code § 189(e), introduced by SB 1437. To hold a non-killer liable for felony murder, the prosecution must prove the defendant acted with intent to kill or was a "major participant" acting with "reckless indifference to human life." Because Leo meets none of these stringent statutory prerequisites, he categorically cannot be convicted of felony murder under this reformed legal standard.
(d) Argument-for: A student could select this option by reasoning that felony murder liability under SB 1437 requires a high degree of personal involvement in the core dangerous acts of the felony. Since Leo did not personally steal property or inflict injuries during the attempted hijacking, they might view his participation as strictly peripheral. Consequently, the student would argue that the absence of these direct, physical contributions to the underlying crime definitively precludes him from being considered a major participant.
(e) Argument-for: Under the agency theory of felony murder followed in California, liability generally requires the lethal act to be committed by a co-felon rather than a third party like a police officer. A student could argue that because the officer caused the death, the felony murder rule is strictly inapplicable to all felons involved. They would conclude this third-party intervention automatically shields the participants from felony murder liability, regardless of their individual mental states or major participant status.

Head-to-head:
Option (c) is the definitively correct answer because it flawlessly recites the triad of liability established by SB 1437. Option (a) fails because it asserts that high-speed driving "inherently establishes" reckless indifference, overriding the required totality-of-the-circumstances test. Option (e) is demonstrably false because it uses "automatically bars" to exclude alternative liability theories and correctly anchors a rigid legal error. However, Options (b) and (d) lack explicit, absolute words locking their legal claims, relying instead on implied sufficiency or necessity. Because these distractors merely assert facts without explicitly framing them as absolute legal rules, they fail the close-call standard.

Falsifiable claim per distractor:
- (a): "inherently establishes" — wrong because reckless indifference requires a multi-factor factual analysis under *Banks/Clark*, not a categorical presumption based on driving.
- (b): "Yes, because Leo was an active participant... and had prior knowledge" — wrong because it implicitly treats these facts as definitively sufficient for liability, but it fails to lock this claim with absolute wording.
- (d): "No, because Leo did not personally steal... or cause any injuries" — wrong because it suggests these acts are necessary for major participant status, but it lacks an absolute word to make this an explicit legal falsehood.
- (e): "automatically bars felony murder liability for all involved participants" — wrong because it ignores alternative theories like provocative act murder and overstates the agency rule as an absolute categorical bar for all participants.

Recommended fix: Edit (b) to append "...which categorically satisfies the major participant standard." Edit (d) to append "...which automatically precludes a finding of reckless indifference."
-->

## Issue 4 — argpass-opus

**Q12.** Assume the jurisdiction has adopted accomplice felony murder reforms identical to California's SB 1437. Can Leo be convicted of felony murder for Wendy's death?

(a) Yes, because acting as the designated getaway driver in a high-speed pursuit inherently establishes a reckless indifference to human life.
(b) Yes, because Leo was an active participant in the underlying felony and had prior knowledge that his co-felon Dom was heavily armed.
(c) No, because Leo was neither the actual killer, nor did he act with intent to kill or as a legally defined major participant. <!-- correct -->
(d) No, because Leo did not personally steal any property or cause any injuries during the initial execution of the attempted hijacking operation.
(e) No, because the death was directly caused by a pursuing police officer, which automatically bars felony murder liability for all involved participants.

**Answer:** (c)

**Explanation:** California's SB 1437 restricts felony murder liability for non-killers. To be convicted, the defendant must be the actual killer, act with intent to kill, or be a "major participant" who acts with "reckless indifference to human life." Simply acting as a getaway driver does not automatically satisfy this stringent standard. Option (a) is wrong because the statute requires a fact-specific inquiry, rejecting the premise that driving inherently establishes reckless indifference. Option (b) is wrong because active participation and knowledge of a weapon do not automatically elevate a defendant to a major participant. Option (d) is wrong because failing to personally steal property does not immunize a defendant if the legal criteria are met. Option (e) is wrong because SB 1437 focuses on the defendant's specific mental state, not just the agency of the killer.

**Tags:** chapters: [14], topics: [felony murder, accomplice liability, major participant, sb 1437], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14: sb-1437-major-participant

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that high-speed pursuits from dangerous felonies inherently pose a massive risk to bystanders. Under this view, driving the getaway car justifies a per se finding of reckless indifference to human life. Option (a) leverages this plausible policy argument to conclude that liability automatically attaches to the driver. This makes it a tempting choice for students who believe getaway drivers are categorically strictly liable.
(b) Argument-for: A student could argue that knowing a co-felon is heavily armed and actively participating in the felony sufficiently satisfies the "major participant" and "reckless indifference" standards. Under this interpretation, Leo’s direct involvement and awareness of the lethal risk are all that is required to meet SB 1437's threshold. This provides a strong, fact-based rationale for conviction, especially to students unfamiliar with the strict *Banks/Clark* factors.
(c) Argument-for: A student would select this because it precisely mirrors the statutory language and constraints of California's SB 1437. The statute explicitly shields non-killers from felony murder unless they acted with intent to kill or were major participants acting with reckless indifference. Assuming the facts align, because Leo fails to meet any of these specific statutory prongs, he is legally protected from a felony murder conviction, making this the keyed answer.
(d) Argument-for: A student could argue that strict accomplice liability requires direct participation in the *actus reus* of the underlying felony. Because Leo didn't steal property or injure anyone personally, he lacks the nexus required to be held responsible for the resulting homicide. This option appeals to students who mistakenly believe felony murder requires personal commission of the underlying crime's physical elements.
(e) Argument-for: A student could argue that under the agency theory of felony murder, a killing by a non-participant breaks the causal chain. California strictly follows this rule (*People v. Washington*), meaning a death directly caused by a pursuing police officer categorically bars a felony murder conviction for the felons (though they may be liable for provocative act murder). Therefore, a student could select this option believing it correctly applies black-letter agency limits to the specific charge of felony murder.

Head-to-head: The question suffers from two fatal flaws. First, it completely lacks a fact pattern, making it impossible to evaluate the factual premises injected into every option (e.g., whether a cop shot Wendy, whether Leo was a getaway driver, etc.). Second, assuming these facts are implied by the answers, distractor (e) contains a perfectly *true* statement of law: California's agency rule for felony murder does indeed bar a felony murder conviction when the fatal act is committed by a non-participant, such as a pursuing police officer. Thus, (e) is arguably just as correct (if not more correct) than (c) depending on the missing facts. Furthermore, distractors (b) and (d) lack explicit absolute phrasing to lock in falsifiable legal errors, merely misapplying facts or implying rules. 

Falsifiable claim per distractor:
- (a): "inherently establishes a reckless indifference to human life" — wrong because CA uses a totality-of-the-circumstances test, so acting as a getaway driver does not categorically establish this element.
- (b): None. "Yes, because Leo was an active participant... and had prior knowledge..." — lacks an absolute falsifiable claim. It states a legal conclusion drawn from specific facts, which a student could argue is a valid application of the totality test rather than an explicitly false black-letter rule.
- (d): None. "No, because Leo did not personally steal..." — lacks an absolute word (like "solely" or "categorically"), though it implicitly relies on the false rule that personal commission of the underlying theft is required.
- (e): None. "automatically bars felony murder liability for all involved participants" — This is actually *true* under California's agency theory of felony murder (*People v. Washington*), meaning (e) does not contain a false legal claim and would be a fully correct answer if the cop killed Wendy.

Recommended fix: Provide the missing fact pattern detailing Leo's exact role, Dom's actions, and how Wendy died. Ensure the facts state that Dom (the co-felon) killed Wendy, not the police, to safely eliminate (e). To fix the distractors: ensure each contains an absolute legal falsehood (e.g., rewrite (b) to "Yes, because prior knowledge that a co-felon is armed automatically satisfies the major participant standard"; rewrite (d) to "No, because felony murder categorically requires the accomplice to personally commit the underlying theft"). Rewrite (e) so it contains a false statement of law regarding SB 1437 rather than a true statement about the agency rule.
-->
