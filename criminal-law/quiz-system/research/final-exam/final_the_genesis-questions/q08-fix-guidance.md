# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q8.** Putting aside the felony murder rule, what is Marlowe's homicide liability for Greggs's death under traditional proximate causation principles?

(a) Murder, because his extreme indifference to the value of human life created the deadly chemical fire scenario.
(b) Manslaughter, because his reckless omission to call 911 was the direct cause of the ceiling beam collapsing.
(c) Negligent homicide, because a reasonable person would have checked the chemical warning labels before ordering them mixed.
(d) Not guilty of homicide, because the inspector's death from a termite-rotted beam was an unforeseeable, highly extraordinary event. <!-- correct -->
(e) Not guilty of homicide, because the inspector's death was caused by her own negligence in entering the burning building.

**Answer:** (d)

**Explanation:** (d) is correct because under both common law foreseeability tests and the MPC's "too remote or accidental" standard, a death caused entirely by unrelated termite rot is a highly extraordinary intervening event that severs proximate cause, precluding any homicide grading. (a) fails because extreme indifference murder still requires proximate causation to be established. (b) fails factually because his omission did not cause the beam to collapse. (c) fails because negligence still requires the resulting harm to be proximately caused by the negligent act. (e) fails because a firefighter entering a burning building is foreseeable and not considered an independent negligent act.

**Tags:** chapters: [8, 13], topics: [proximate cause, homicide grading, highly extraordinary result], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 8 - Causation (Highly Extraordinary Result / Proximate Cause Foreseeability)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: The independent intervening cause facts completely preempt the homicide grading analysis. Because proximate cause is severed by the termite rot, grading is moot, turning a purported "homicide grading" question into a duplicative causation question.
3. Cross-Question Spoilers: Q8's correct answer (D) explicitly resolves Q2. By stating that the termite-rotted beam is an "unforeseeable, highly extraordinary event" that precludes liability, Q8 gives away the exact legal conclusion required to answer Q2's evaluation of independent intervening causes.
Recommended fix: Revise Q8's prompt to "Assuming for this question that proximate causation is established, what is Marlowe's homicide liability?" and rewrite the options to test his mens rea (recklessness vs. negligence) regarding his decision to trust the invoice over the chemical warning labels.
-->

## Issue 3 — argpass-sonnet

**Q8.** Putting aside the felony murder rule, what is Marlowe's homicide liability for Greggs's death under traditional proximate causation principles?

(a) Murder, because his extreme indifference to the value of human life created the deadly chemical fire scenario.
(b) Manslaughter, because his reckless omission to call 911 was the direct cause of the ceiling beam collapsing.
(c) Negligent homicide, because a reasonable person would have checked the chemical warning labels before ordering them mixed.
(d) Not guilty of homicide, because the inspector's death from a termite-rotted beam was an unforeseeable, highly extraordinary event. <!-- correct -->
(e) Not guilty of homicide, because the inspector's death was caused by her own negligence in entering the burning building.

**Answer:** (d)

**Explanation:** (d) is correct because under both common law foreseeability tests and the MPC's "too remote or accidental" standard, a death caused entirely by unrelated termite rot is a highly extraordinary intervening event that severs proximate cause, precluding any homicide grading. (a) fails because extreme indifference murder still requires proximate causation to be established. (b) fails factually because his omission did not cause the beam to collapse. (c) fails because negligence still requires the resulting harm to be proximately caused by the negligent act. (e) fails because a firefighter entering a burning building is foreseeable and not considered an independent negligent act.

**Tags:** chapters: [8, 13], topics: [proximate cause, homicide grading, highly extraordinary result], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 8 - Causation (Highly Extraordinary Result / Proximate Cause Foreseeability)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that Marlowe's extreme recklessness in creating a deadly chemical fire satisfies the "depraved heart" mens rea for murder. If a victim dies in a fire scenario created by the defendant, some might erroneously believe the specific mechanism of death within the zone of danger does not need to be perfectly foreseeable. Therefore, the extreme indifference to human life correctly identifies the culpability level, leading the student to select murder.
(b) Argument-for: A student might argue that Marlowe had a duty to mitigate the danger he created, making his failure to call 911 a reckless omission. Because the omission allowed the fire to persist, leading to the inspector being under the beam when it collapsed, a student could conclude this omission was the direct cause of the collapse. This leads to manslaughter based on reckless omission.
(c) Argument-for: A student could conclude that failing to check warning labels before mixing chemicals is a clear deviation from the standard of care, establishing negligence. If the fire would not have happened but for this negligence, a student might reason that negligent homicide is the correct charge, overlooking the nuanced proximate cause requirement for the specific mechanism of death.
(d) Argument-for: This is the correct answer. Traditional proximate causation requires the harm to be a foreseeable result of the defendant's conduct. A ceiling beam collapsing entirely due to unrelated termite rot, rather than the fire, is a highly extraordinary and unforeseeable intervening event. This superseding cause severs the chain of legal causation, meaning Marlowe is not guilty of homicide.
(e) Argument-for: A student could argue that an inspector entering a burning building constitutes a voluntary assumption of risk or contributory negligence. If the inspector's own actions put her in harm's way, a student might conclude her negligence was a superseding cause of her death. Thus, Marlowe is absolved of homicide liability because the victim's own conduct broke the causal chain.

Head-to-head: Option (d) correctly identifies that the termite-rotted beam acts as an unforeseeable superseding cause, breaking proximate causation. However, distractors (a) and (c) are structurally weak because they merely state a true premise about mens rea (extreme indifference / failure to act as a reasonable person) but fail to supply an explicitly false legal rule bridging that premise to the incorrect conclusion, relying instead on the implicit omission of the proximate cause requirement. Distractor (b) contains a clear factual/legal error by labeling the omission the "direct cause" of the collapse. Distractor (e) incorrectly classifies a first responder's foreseeable entry as superseding negligence. To meet the close-call standard, (a) and (c) must be locked with absolute language.

Falsifiable claim per distractor:
- (a): "created the deadly chemical fire scenario" — wrong because this relies on an implicit omission of proximate cause; it provides no explicitly false legal rule asserting that creating the scenario is sufficient for liability regardless of the mechanism of death.
- (b): "was the direct cause of the ceiling beam collapsing" — wrong because an omission to call 911 is neither factually nor legally the direct cause of a structural collapse triggered by independent termite rot.
- (c): "because a reasonable person would have checked" — wrong because, like (a), it relies on an implicit omission of proximate causation and lacks a falsifiable assertion that negligence automatically guarantees liability.
- (e): "her own negligence in entering the burning building" — wrong because a first responder entering a burning building is legally foreseeable and does not constitute an independent superseding negligent act.

Recommended fix: Edit (a) and (c) to include absolute words that assert an explicitly false legal claim. Change (a) to: "Murder, because creating a deadly fire automatically satisfies proximate causation for any subsequent death on the premises." Change (c) to: "Negligent homicide, because failing to check chemical warning labels categorically establishes liability regardless of intervening causes."
-->

## Issue 4 — argpass-opus

**Q8.** Putting aside the felony murder rule, what is Marlowe's homicide liability for Greggs's death under traditional proximate causation principles?

(a) Murder, because his extreme indifference to the value of human life created the deadly chemical fire scenario.
(b) Manslaughter, because his reckless omission to call 911 was the direct cause of the ceiling beam collapsing.
(c) Negligent homicide, because a reasonable person would have checked the chemical warning labels before ordering them mixed.
(d) Not guilty of homicide, because the inspector's death from a termite-rotted beam was an unforeseeable, highly extraordinary event. <!-- correct -->
(e) Not guilty of homicide, because the inspector's death was caused by her own negligence in entering the burning building.

**Answer:** (d)

**Explanation:** (d) is correct because under both common law foreseeability tests and the MPC's "too remote or accidental" standard, a death caused entirely by unrelated termite rot is a highly extraordinary intervening event that severs proximate cause, precluding any homicide grading. (a) fails because extreme indifference murder still requires proximate causation to be established. (b) fails factually because his omission did not cause the beam to collapse. (c) fails because negligence still requires the resulting harm to be proximately caused by the negligent act. (e) fails because a firefighter entering a burning building is foreseeable and not considered an independent negligent act.

**Tags:** chapters: [8, 13], topics: [proximate cause, homicide grading, highly extraordinary result], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 8 - Causation (Highly Extraordinary Result / Proximate Cause Foreseeability)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that Marlowe's creation of a deadly chemical fire satisfies the elements of depraved-heart murder. By demonstrating extreme indifference, he established the actual cause that brought the inspector to the scene. Since the fire necessitated an emergency response, a broad foreseeability test might encompass any death occurring during that response. Thus, his extreme indifference justifies a murder conviction despite the precise mechanism of death.
(b) Argument-for: A student could argue that Marlowe had a duty to act after creating the peril, making his failure to call 911 a reckless omission. By delaying emergency services, the omission factually allowed the fire to persist, leading to the beam's collapse at the exact moment the inspector was underneath. Because the collapse would not have injured her had he called promptly, it can be framed as the direct cause. Therefore, manslaughter is appropriate.
(c) Argument-for: A student could argue that ordering chemicals mixed without checking warning labels is a gross deviation from the standard of care. Because this negligence sparked the fire that ultimately led to the inspector's death, factual causation is met. Applying a strict approach to negligent acts that result in death, a student could conclude proximate cause is satisfied by the mere creation of the hazard. Thus, negligent homicide applies.
(d) Argument-for: A student could argue this is correct because proximate causation requires the resulting harm to be within the scope of foreseeable risks. A termite-rotted beam collapsing is an independent, preexisting condition unrelated to the fire's foreseeable risks (like burns or smoke inhalation). Under traditional proximate causation and the MPC, such a highly extraordinary intervening event breaks the causal chain. Consequently, Marlowe cannot be held liable for any degree of homicide.
(e) Argument-for: A student could argue that the inspector's decision to enter a burning building was a voluntary, independent act of negligence. If a victim knowingly walks into a hazardous scenario, their own conduct can sometimes sever the causal chain. By treating the inspector's entry as a superseding intervening act, Marlowe is relieved of homicide liability.

Head-to-head: Option (d) is clearly the best answer because it correctly identifies the termite rot as a highly extraordinary superseding cause that severs proximate causation. However, distractors (a) and (c) merely provide correct statements of mens rea and actual cause while implicitly omitting the proximate cause requirement. Because they lack absolute words, they do not contain explicitly falsifiable legal claims. Option (b) correctly fails by asserting an omission directly caused a physical collapse, which is factually falsifiable. Option (e) fails by misapplying the "fireman's rule" but lacks absolute framing to lock in the legal error.

Falsifiable claim per distractor:
- (a): "created the deadly chemical fire scenario" — wrong because it ignores superseding causes, but fails the standard because it relies on an implicit omission rather than an explicitly false absolute legal claim.
- (b): "was the direct cause of the ceiling beam collapsing" — wrong because a failure to call 911 cannot factually or legally be the "direct cause" of a structural collapse.
- (c): "because a reasonable person would have checked the chemical warning labels" — wrong because it merely establishes a breach of duty and implicitly skips proximate cause, lacking an absolute claim.
- (e): "caused by her own negligence in entering the burning building" — wrong because an inspector entering a fire is highly foreseeable and not a superseding cause, though the distractor lacks absolute phrasing.

Recommended fix: Add absolute wording to distractors to lock in the false legal propositions. For example: 
(a) "Murder, because creating a deadly fire scenario automatically establishes proximate cause regardless of how the victim dies." 
(c) "Negligent homicide, because a factual breach of duty categorically satisfies liability for any resulting death." 
(e) "Not guilty of homicide, because an official entering a burning building always constitutes a superseding cause."
-->
