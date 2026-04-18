# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q3.** Assume Wallace is found to be the factual and proximate cause of the death. Based on his mental state at the time he set up the mixing station, what is the most appropriate homicide grading for Wallace's conduct under the Model Penal Code?

(a) Murder, because his subjective recognition of the extreme explosion risk and decision to proceed anyway demonstrates extreme indifference to the value of human life. <!-- correct -->
(b) Manslaughter, because while he consciously disregarded a substantial risk, his desperation for money establishes an extreme emotional disturbance that mitigates the murder.
(c) Manslaughter, because he was only aware of a risk of an explosion, whereas a murder conviction requires proof that it was his conscious object to cause the death.
(d) Negligent homicide, because his failure to utilize a specialized respirator was a gross deviation from the standard of care of a reasonable person in his situation.
(e) Felony murder, because the death occurred during his commission of the inherently dangerous, though unenumerated, strict-liability felony of manufacturing illicit drugs.

**Answer:** (a)

**Explanation:** Under the MPC, reckless homicide becomes murder when it manifests extreme indifference to the value of human life. Wallace's subjective recognition of an "extreme risk" of a "lethal explosion" and his conscious decision to proceed merely for cash strongly supports an extreme indifference murder finding. (b) fails because financial desperation does not qualify as an extreme emotional disturbance for which there is a reasonable explanation or excuse. (c) fails because MPC murder includes extreme indifference recklessness; it does not strictly require purpose or knowledge. (d) fails because Wallace was subjectively aware of the risk, which elevates his culpability to recklessness and renders negligence inapplicable. (e) fails because the MPC rejects the strict common-law felony-murder rule, replacing it with a rebuttable presumption of recklessness for specific enumerated felonies only.

**Tags:** chapters: [13], topics: [homicide grading, extreme indifference, recklessness], difficulty: medium, cognitive: application

**Grounding:** Chapter 13 (extreme-indifference-standard; MPC 210.2)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: The Model Penal Code elevates reckless homicide to murder when it is committed under circumstances manifesting extreme indifference to the value of human life (MPC § 210.2(1)(b)). Wallace subjectively recognized an extreme risk of a lethal explosion, making him factually reckless. His choice to proceed anyway merely for financial gain demonstrates a profound lack of concern for human life. Thus, his conduct perfectly satisfies the elements for extreme indifference murder.
(b) Argument-for: Under MPC § 210.3, a homicide that would otherwise be murder is mitigated to manslaughter if committed under the influence of extreme mental or emotional disturbance (EED). The MPC approach to EED evaluates the reasonableness of the actor's excuse from the actor's subjective viewpoint. A student could argue that Wallace’s severe desperation for money created a subjective state of extreme panic and emotional disturbance. Since severe financial ruin can profoundly distress a person, it arguably triggers this mitigation to manslaughter.
(c) Argument-for: Manslaughter is the standard grading for reckless homicide under MPC § 210.3(1)(a). Murder typically requires a purposeful or knowing mental state where causing death is the actor's conscious object. Here, Wallace’s conscious object was solely to manufacture drugs for money, not to kill anyone. Because he merely consciously disregarded a risk without intending the lethal outcome, standard manslaughter is the appropriate grading over murder.
(d) Argument-for: Negligent homicide applies when an actor fails to perceive a substantial and unjustifiable risk, involving a gross deviation from the standard of care (MPC § 210.4). Wallace’s failure to use a specialized respirator constitutes a clear failure to follow basic safety protocols. A reasonable person in a chemical mixing station would have utilized proper equipment. Therefore, his failure to exercise due care perfectly aligns with the elements of negligent homicide.
(e) Argument-for: The felony-murder doctrine traditionally allows for a murder conviction when a death occurs during the commission of an inherently dangerous felony. Manufacturing illicit drugs involves mixing volatile chemicals, making it categorically dangerous to human life. Applying this traditional framework, any proximate death during this crime automatically satisfies the homicide requirement. Consequently, felony murder captures the strict-liability nature of deaths caused during dangerous illicit manufacturing.

Head-to-head: Option (a) is definitively the best answer because the MPC explicitly allows for extreme indifference murder based on subjective recognition of high risk. Options (c) and (e) are excellent distractors because they contain explicitly false legal claims under the Model Penal Code: (c) falsely asserts the MPC requires a "conscious object" (purpose) for all murders, and (e) falsely imports the common-law "strict-liability" felony murder rule which the MPC explicitly rejects. However, distractors (b) and (d) are slightly weaker because they lack absolute falsifying words. They rely on incorrect factual application (financial desperation is universally held not to be an EED; respirator negligence is trumped by subjective awareness of the explosion risk) rather than definitively false legal rules. While unlikely to be successfully appealed, locking them with absolute phrasing would render the question bulletproof.

Falsifiable claim per distractor:
- (b): "his desperation for money establishes an extreme emotional disturbance" — wrong because financial desperation does not establish EED as a matter of law, though it lacks an absolute word to make it a strictly false legal rule.
- (c): "whereas a murder conviction requires proof that it was his conscious object to cause the death" — wrong because the MPC explicitly permits murder convictions for extreme indifference recklessness (where death is not the conscious object).
- (d): "failure to utilize a specialized respirator was a gross deviation" — wrong in application because subjective awareness of an explosion risk elevates culpability to recklessness (and an explosion renders respirator negligence causally irrelevant), but it lacks an explicit false legal claim.
- (e): "strict-liability felony of manufacturing illicit drugs" — wrong because the MPC explicitly rejects strict-liability felony murder, instead using a rebuttable presumption of extreme indifference for only a specific enumerated list of felonies (which does not include drug manufacturing).

Recommended fix: Add absolute modifiers to (b) and (d) to lock in explicit legal falsity. 
Change (b) to: "Manslaughter, because his desperation for money automatically establishes an extreme emotional disturbance..." 
Change (d) to: "Negligent homicide, because his failure to utilize a specialized respirator categorically limits his liability to negligence."
-->

## Issue 3 — argpass-opus

**Q3.** Assume Wallace is found to be the factual and proximate cause of the death. Based on his mental state at the time he set up the mixing station, what is the most appropriate homicide grading for Wallace's conduct under the Model Penal Code?

(a) Murder, because his subjective recognition of the extreme explosion risk and decision to proceed anyway demonstrates extreme indifference to the value of human life. <!-- correct -->
(b) Manslaughter, because while he consciously disregarded a substantial risk, his desperation for money establishes an extreme emotional disturbance that mitigates the murder.
(c) Manslaughter, because he was only aware of a risk of an explosion, whereas a murder conviction requires proof that it was his conscious object to cause the death.
(d) Negligent homicide, because his failure to utilize a specialized respirator was a gross deviation from the standard of care of a reasonable person in his situation.
(e) Felony murder, because the death occurred during his commission of the inherently dangerous, though unenumerated, strict-liability felony of manufacturing illicit drugs.

**Answer:** (a)

**Explanation:** Under the MPC, reckless homicide becomes murder when it manifests extreme indifference to the value of human life. Wallace's subjective recognition of an "extreme risk" of a "lethal explosion" and his conscious decision to proceed merely for cash strongly supports an extreme indifference murder finding. (b) fails because financial desperation does not qualify as an extreme emotional disturbance for which there is a reasonable explanation or excuse. (c) fails because MPC murder includes extreme indifference recklessness; it does not strictly require purpose or knowledge. (d) fails because Wallace was subjectively aware of the risk, which elevates his culpability to recklessness and renders negligence inapplicable. (e) fails because the MPC rejects the strict common-law felony-murder rule, replacing it with a rebuttable presumption of recklessness for specific enumerated felonies only.

**Tags:** chapters: [13], topics: [homicide grading, extreme indifference, recklessness], difficulty: medium, cognitive: application

**Grounding:** Chapter 13 (extreme-indifference-standard; MPC 210.2)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under MPC § 210.2(1)(b), homicide constitutes murder when committed recklessly under circumstances manifesting extreme indifference to the value of human life. Wallace subjectively recognized an extreme risk of explosion and proceeded anyway simply for financial gain. This conscious disregard of a grave, lethal risk to human life, driven by a base motive rather than any socially useful purpose, perfectly fits the extreme indifference standard. Thus, murder is the most appropriate grading.
(b) Argument-for: Under MPC § 210.3, a homicide that would otherwise be murder is manslaughter if committed under the influence of extreme mental or emotional disturbance for which there is reasonable explanation or excuse. A student could argue that Wallace's severe financial desperation pushed him into a state of extreme emotional disturbance, clouding his judgment. The MPC's EED formulation is broad ("determined from the viewpoint of a person in the actor's situation"), so a jury could theoretically find that his financial desperation establishes an excuse that mitigates the grading to manslaughter.
(c) Argument-for: A student could argue that murder strictly requires specific intent or purpose to kill, leaning on common lay understandings of murder versus manslaughter. If Wallace merely foresaw an explosion risk but did not have the conscious object to kill anyone, his mental state aligns with recklessness (awareness of a substantial and unjustifiable risk) rather than purpose. Therefore, under this rationale, he lacks the specific mens rea required for murder, making manslaughter the appropriate charge.
(d) Argument-for: Negligent homicide under MPC § 210.4 applies when an actor should be aware of a substantial and unjustifiable risk, and failure to perceive it involves a gross deviation from the standard of care. A student could argue that Wallace's failure to use safety equipment like a specialized respirator constitutes exactly this kind of gross deviation. If the explosion risk was caused by this specific negligent omission regarding standard safety protocols, negligent homicide appropriately captures the essence of his culpability.
(e) Argument-for: A student could argue that manufacturing illicit drugs is an inherently dangerous felony, which traditionally supports a felony murder conviction if a death results. Since the death occurred during the commission of this dangerous felony, the strict liability mechanism of the felony-murder rule automatically applies. Option (e) explicitly states that the death occurred during this strict-liability felony, making it an attractive choice for a student applying the common-law felony murder doctrine.

Head-to-head: Option (a) correctly applies the MPC's "extreme indifference" murder standard to Wallace's reckless conduct. Option (c) contains a clearly false legal claim by asserting that an MPC murder conviction strictly "requires proof" of a conscious object to cause death. Option (e) also contains a clear legal error because the MPC abandons the unenumerated strict-liability felony-murder rule. However, options (b) and (d) are weaker distractors because their errors rely more on factual misapplications or implicit omissions rather than explicit, absolute false legal claims. Option (b) claims desperation "establishes" EED, which is factually incorrect but lacks an absolute legal lock. Option (d) justifies negligence based on a gross deviation, which isn't a false legal rule in a vacuum; it merely ignores the facts establishing subjective awareness. These distractors should be locked with absolute language.

Falsifiable claim per distractor:
- (b): "his desperation for money establishes an extreme emotional disturbance" — wrong because financial desperation does not legally or categorically establish EED (this is a factual/application omission rather than a locked false legal rule).
- (c): "a murder conviction requires proof that it was his conscious object to cause the death" — wrong because MPC murder explicitly includes recklessness manifesting extreme indifference to human life.
- (d): "Negligent homicide, because his failure to utilize a specialized respirator was a gross deviation" — wrong because negligence is inapplicable when the actor possesses subjective awareness of the risk, but the distractor currently lacks an explicit false legal claim regarding this rule.
- (e): "strict-liability felony of manufacturing illicit drugs" — wrong because the MPC explicitly rejects the strict-liability felony-murder rule for unenumerated felonies.

Recommended fix: Add absolute words to (b) and (d) to lock their falsifiability. 
Change (b) to: "Manslaughter, because while he consciously disregarded a substantial risk, his desperation for money categorically qualifies as an extreme emotional disturbance that mitigates the murder."
Change (d) to: "Negligent homicide, solely because his failure to utilize a specialized respirator was a gross deviation from the standard of care, which automatically caps his liability at negligence."
-->
