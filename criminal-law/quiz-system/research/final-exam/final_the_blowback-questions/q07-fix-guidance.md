# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Assume Oscar is charged with depraved heart murder (second-degree) for Victor's death. Under the Model Penal Code's "extreme indifference" standard, what is the strongest argument that Oscar is NOT guilty of murder?

(a) Oscar lacked the deliberate purpose or actual knowledge required to satisfy the mental state for an intentional first-degree homicide conviction.
(b) Oscar's failure to consult the city sewer maps constituted ordinary negligence rather than a gross deviation from the standard of care.
(c) Oscar did not possess the specific intent to kill or inflict grievous bodily harm upon Victor or any other city worker.
(d) Oscar actually believed the rain would dilute the chemicals, meaning he did not consciously disregard a substantial risk of an explosion. <!-- correct -->
(e) The explosion was triggered by an unforeseeable intervening act—a flickering streetlamp—which legally severs the chain of proximate causation.

**Answer:** (d)

**Explanation:** The Model Penal Code's standard for extreme indifference murder (§ 210.2) requires recklessness, which is defined as the conscious disregard of a substantial and unjustifiable risk. Because Oscar subjectively believed the rain would safely dilute the solvent, he did not consciously disregard the risk of an explosion, dropping his liability from murder down to negligent homicide. (a) is wrong because depraved heart murder does not require purpose or knowledge; it is an unintentional homicide doctrine. (b) is wrong because while his failure to check maps might be negligent, the critical missing element for MPC murder is conscious disregard, not whether the negligence was ordinary or gross. (c) is wrong because depraved heart murder inherently applies to defendants who lack the specific intent to kill. (e) is wrong because a spark from a streetlamp is a foreseeable hazard in a residential area and does not sever proximate causation.

**Tags:** chapters: [13], topics: [depraved heart murder, extreme indifference, recklessness], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, extreme-indifference-standard; MPC § 210.2 requires recklessness, meaning conscious disregard of the risk.

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem is completely missing the underlying fact pattern. It refers to Oscar, Victor, chemical solvents, rain, and sewer maps, but none of these facts are provided in the prompt.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Integrate the missing fact pattern into the question stem so it can function as a standalone question.
-->

## Issue 2 — argpass-sonnet

**Q7.** Assume Oscar is charged with depraved heart murder (second-degree) for Victor's death. Under the Model Penal Code's "extreme indifference" standard, what is the strongest argument that Oscar is NOT guilty of murder?

(a) Oscar lacked the deliberate purpose or actual knowledge required to satisfy the mental state for an intentional first-degree homicide conviction.
(b) Oscar's failure to consult the city sewer maps constituted ordinary negligence rather than a gross deviation from the standard of care.
(c) Oscar did not possess the specific intent to kill or inflict grievous bodily harm upon Victor or any other city worker.
(d) Oscar actually believed the rain would dilute the chemicals, meaning he did not consciously disregard a substantial risk of an explosion. <!-- correct -->
(e) The explosion was triggered by an unforeseeable intervening act—a flickering streetlamp—which legally severs the chain of proximate causation.

**Answer:** (d)

**Explanation:** The Model Penal Code's standard for extreme indifference murder (§ 210.2) requires recklessness, which is defined as the conscious disregard of a substantial and unjustifiable risk. Because Oscar subjectively believed the rain would safely dilute the solvent, he did not consciously disregard the risk of an explosion, dropping his liability from murder down to negligent homicide. (a) is wrong because depraved heart murder does not require purpose or knowledge; it is an unintentional homicide doctrine. (b) is wrong because while his failure to check maps might be negligent, the critical missing element for MPC murder is conscious disregard, not whether the negligence was ordinary or gross. (c) is wrong because depraved heart murder inherently applies to defendants who lack the specific intent to kill. (e) is wrong because a spark from a streetlamp is a foreseeable hazard in a residential area and does not sever proximate causation.

**Tags:** chapters: [13], topics: [depraved heart murder, extreme indifference, recklessness], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, extreme-indifference-standard; MPC § 210.2 requires recklessness, meaning conscious disregard of the risk.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that asserting the absence of deliberate purpose or actual knowledge effectively insulates Oscar against the most severe homicide charges. Because first-degree murder requires these heightened mental states, confirming their absence is a crucial step in the defense's broader strategy to pull Oscar's culpability away from intentional murder.
(b) Argument-for: Under the MPC, both recklessness and criminal negligence require a "gross deviation" from the standard of care. By characterizing Oscar's failure to check the sewer maps as mere "ordinary negligence," a student could argue that his conduct falls entirely outside the realm of criminal homicide liability, making this an absolute defense to the murder charge if accepted.
(c) Argument-for: Specific intent to kill or inflict grievous bodily harm is the traditional hallmark of common-law malice aforethought. A student could contend that explicitly negating specific intent highlights the accidental nature of the death, functioning as a powerful rhetorical defense to sway the jury against a severe depraved heart conviction.
(d) Argument-for: Under MPC § 210.2, extreme indifference murder requires "recklessness," defined as the conscious disregard of a substantial and unjustifiable risk. If Oscar actually believed the rain would dilute the chemicals, he lacked the subjective awareness of the explosion risk. This directly defeats the mens rea required for the charge, representing the strongest and most legally precise argument.
(e) Argument-for: Proximate cause is a prerequisite for any homicide conviction. A student could argue that if the flickering streetlamp is classified as a superseding cause, it legally severs the causal chain between Oscar's act and Victor's death. Negating causation completely overrides any analysis of mens rea, serving as a total bar to liability.

Head-to-head: Option (d) is the unequivocally correct answer because it directly attacks the specific subjective mens rea (conscious disregard) required for extreme indifference murder under the MPC. However, distractors (a), (b), and (c) fail the close-call standard because they do not contain explicit, falsifiable false legal claims. Instead, they state factually true but legally irrelevant premises (e.g., that Oscar lacked the intent for a *different* crime) or present valid defense theories that simply lose on the facts (e.g., arguing ordinary negligence). Option (b) is especially precarious: if Oscar's conduct *was* merely ordinary negligence, he actually *would* be completely cleared of murder, meaning the distractor's underlying legal premise is technically true and acts as a valid (albeit factually weaker) defense rather than a strictly falsifiable distractor.

Falsifiable claim per distractor:
- (a): None. The option states a true but irrelevant premise (he lacked the mens rea for 1st-degree murder) without explicitly claiming this legally precludes a depraved heart conviction.
- (b): None. The option raises a factual argument (ordinary negligence vs. gross deviation) which, if accepted, would genuinely defeat a murder charge under the MPC. It contains no false legal claim.
- (c): None. The option correctly states a fact (he lacked specific intent), relying merely on the *implicit* false assumption that specific intent is required for extreme indifference murder.
- (e): "unforeseeable intervening act—a flickering streetlamp—which legally severs the chain of proximate causation" — wrong because a normal environmental condition like a flickering streetlamp is legally foreseeable and does not sever proximate causation.

Recommended fix: Lock (a), (b), and (c) with explicit false legal claims. 
- Change (a) to: "Oscar lacked deliberate purpose, which is categorically required to satisfy the mental state for any murder conviction under the MPC."
- Change (b) to: "Oscar's failure to consult the city sewer maps constitutes ordinary negligence, which automatically precludes liability solely because the extreme indifference standard requires an intent to cause a gross deviation."
- Change (c) to: "Oscar did not possess the specific intent to kill, which is categorically required in every jurisdiction to sustain an extreme indifference murder conviction."
-->

## Issue 3 — argpass-opus

**Q7.** Assume Oscar is charged with depraved heart murder (second-degree) for Victor's death. Under the Model Penal Code's "extreme indifference" standard, what is the strongest argument that Oscar is NOT guilty of murder?

(a) Oscar lacked the deliberate purpose or actual knowledge required to satisfy the mental state for an intentional first-degree homicide conviction.
(b) Oscar's failure to consult the city sewer maps constituted ordinary negligence rather than a gross deviation from the standard of care.
(c) Oscar did not possess the specific intent to kill or inflict grievous bodily harm upon Victor or any other city worker.
(d) Oscar actually believed the rain would dilute the chemicals, meaning he did not consciously disregard a substantial risk of an explosion. <!-- correct -->
(e) The explosion was triggered by an unforeseeable intervening act—a flickering streetlamp—which legally severs the chain of proximate causation.

**Answer:** (d)

**Explanation:** The Model Penal Code's standard for extreme indifference murder (§ 210.2) requires recklessness, which is defined as the conscious disregard of a substantial and unjustifiable risk. Because Oscar subjectively believed the rain would safely dilute the solvent, he did not consciously disregard the risk of an explosion, dropping his liability from murder down to negligent homicide. (a) is wrong because depraved heart murder does not require purpose or knowledge; it is an unintentional homicide doctrine. (b) is wrong because while his failure to check maps might be negligent, the critical missing element for MPC murder is conscious disregard, not whether the negligence was ordinary or gross. (c) is wrong because depraved heart murder inherently applies to defendants who lack the specific intent to kill. (e) is wrong because a spark from a streetlamp is a foreseeable hazard in a residential area and does not sever proximate causation.

**Tags:** chapters: [13], topics: [depraved heart murder, extreme indifference, recklessness], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, extreme-indifference-standard; MPC § 210.2 requires recklessness, meaning conscious disregard of the risk.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A defense attorney could reasonably argue that emphasizing a defendant's lack of purpose or knowledge is a crucial strategy in any homicide case. By firmly establishing that Oscar did not have the mental state for an intentional first-degree murder conviction, the defense prevents the prosecution from inappropriately inflating the charges. Highlighting the absence of deliberate intent frames Oscar's conduct as an accident rather than a malicious act, making this a strong narrative argument to mitigate culpability before a jury.
(b) Argument-for: Criminal liability, even for extreme indifference murder, requires conduct that is a gross deviation from the standard of care. If Oscar's failure to consult the city sewer maps is characterized merely as ordinary civil negligence, it falls below the threshold of criminal negligence or recklessness. Arguing that his conduct was merely ordinary negligence directly attacks the objective severity of his actions, completely undermining the foundational requirement for criminal liability. 
(c) Argument-for: Under traditional common law, malice aforethought is required for murder, and two of the primary forms of malice are the specific intent to kill and the specific intent to inflict grievous bodily harm. By proving Oscar lacked these specific intents, the defense systematically dismantles the most common avenues for a murder conviction. Explicitly negating these intent elements establishes an irrefutable baseline that Oscar's actions were devoid of traditional malicious intent.
(d) Argument-for: Under Model Penal Code § 210.2, extreme indifference murder requires the defendant to act recklessly, which is defined as the conscious disregard of a substantial and unjustifiable risk. If Oscar actually believed the rain would dilute the chemicals, he lacked the subjective awareness of the risk of an explosion. Without this subjective awareness, he cannot have consciously disregarded the risk, thereby cleanly failing the mens rea requirement for extreme indifference murder.
(e) Argument-for: Proximate causation is a strict prerequisite for any homicide conviction. If the explosion was triggered by a flickering streetlamp, one could argue this was an independent, unforeseeable intervening act that breaks the chain of causation. If proximate causation is severed, Oscar cannot be held legally responsible for Victor's death, serving as an absolute bar to a murder conviction regardless of his initial mental state.

Head-to-head: Option (d) is definitively the strongest argument because it precisely attacks the required mens rea (subjective conscious disregard) for MPC extreme indifference murder. The distractors fail because they either attack irrelevant elements or rely on factually unsound legal conclusions. However, options (a) and (c) do not actually contain false legal statements on their face; they simply state true facts (Oscar lacked purpose/knowledge for first-degree murder, and lacked specific intent to kill) that are logically unresponsive to defending against a second-degree depraved heart charge. Because they lack an explicit, identifiable false legal claim internally, they fail the strict close-call standard.

Falsifiable claim per distractor:
- (a): None. "Oscar lacked the deliberate purpose... required to satisfy... first-degree homicide" is a factually and legally true statement, merely irrelevant to the specific charge.
- (b): "constituted ordinary negligence rather than a gross deviation" — wrong because dumping explosive chemicals into a public sewer without checking maps is objectively a gross deviation from the standard of care, not ordinary civil negligence.
- (c): None. "Oscar did not possess the specific intent to kill..." is a true factual statement, simply irrelevant to an unintentional homicide charge.
- (e): "unforeseeable intervening act... which legally severs the chain of proximate causation" — wrong because a flickering streetlamp in a city is a highly foreseeable hazard and does not legally sever proximate causation.

Recommended fix: Lock (a) and (c) with explicit false legal rules. Change (a) to: "Oscar cannot be convicted of murder because depraved heart murder categorically requires deliberate purpose or actual knowledge." Change (c) to: "Oscar is legally immune from murder liability because the charge automatically requires the specific intent to kill or inflict grievous bodily harm."
-->
