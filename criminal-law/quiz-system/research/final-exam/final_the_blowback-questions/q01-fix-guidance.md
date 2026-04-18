# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q1.** Under the Pennsylvania rule for premeditation, is Carmine guilty of first-degree premeditated murder for Paulie's death?

(a) Yes, because a conscious decision to kill, even if formed in the seconds after the insult, fully satisfies the requirement for premeditation. <!-- correct -->
(b) Yes, because keeping a loaded revolver on the boat console demonstrates a pre-existing plan to cause lethal harm to passengers.
(c) No, because grabbing the gun and shooting in under ten seconds constitutes an impulsive reflex rather than a deliberate, pre-planned decision.
(d) No, because his original intent for bringing the revolver was for shooting sharks rather than killing Paulie.
(e) No, because the vicious insult about his wife provoked the killing, legally negating the malice required for murder.

**Answer:** (a)

**Explanation:** Under the Pennsylvania rule (*Commonwealth v. Carroll*), "no time is too short" to form premeditation. A conscious decision to kill, even if formed in a brief instant before acting, suffices for first-degree murder. The fact that Carmine did not pre-plan the murder does not defeat premeditation under this standard. (b) is wrong because the rule does not require a pre-existing plan or preparation. (c) is wrong because the PA rule explicitly permits convictions based on rapid, spur-of-the-moment decisions. (d) is wrong because the relevant intent is assessed at the moment of the shooting, not the reason for initially carrying the weapon. (e) is wrong because words alone are never legally adequate provocation at common law to reduce murder to manslaughter.

**Tags:** chapters: [12], topics: [premeditation, pennsylvania-rule], difficulty: easy, cognitive: application

**Grounding:** Chapter 12: no-time-too-short

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Distractor (e) explicitly resolves whether the insult constitutes adequate provocation to negate malice, which is the exact doctrinal target of Q2 (Voluntary Manslaughter). If a student knows (a) is correct for Q1, they logically deduce that (e) is legally false, thereby giving away the answer to Q2.
Recommended fix: Change distractor (e) to focus purely on premeditation concepts to avoid spoiling Q2. For example: "(e) No, because his motive for shooting was based on sudden anger rather than a cold, calculated plan."
-->

## Issue 3 — argpass-sonnet

**Q1.** Under the Pennsylvania rule for premeditation, is Carmine guilty of first-degree premeditated murder for Paulie's death?

(a) Yes, because a conscious decision to kill, even if formed in the seconds after the insult, fully satisfies the requirement for premeditation. <!-- correct -->
(b) Yes, because keeping a loaded revolver on the boat console demonstrates a pre-existing plan to cause lethal harm to passengers.
(c) No, because grabbing the gun and shooting in under ten seconds constitutes an impulsive reflex rather than a deliberate, pre-planned decision.
(d) No, because his original intent for bringing the revolver was for shooting sharks rather than killing Paulie.
(e) No, because the vicious insult about his wife provoked the killing, legally negating the malice required for murder.

**Answer:** (a)

**Explanation:** Under the Pennsylvania rule (*Commonwealth v. Carroll*), "no time is too short" to form premeditation. A conscious decision to kill, even if formed in a brief instant before acting, suffices for first-degree murder. The fact that Carmine did not pre-plan the murder does not defeat premeditation under this standard. (b) is wrong because the rule does not require a pre-existing plan or preparation. (c) is wrong because the PA rule explicitly permits convictions based on rapid, spur-of-the-moment decisions. (d) is wrong because the relevant intent is assessed at the moment of the shooting, not the reason for initially carrying the weapon. (e) is wrong because words alone are never legally adequate provocation at common law to reduce murder to manslaughter.

**Tags:** chapters: [12], topics: [premeditation, pennsylvania-rule], difficulty: easy, cognitive: application

**Grounding:** Chapter 12: no-time-too-short

<!-- argument-pass: SHOULD FIX
(a) Argument-for: The Pennsylvania rule, notably applied in *Commonwealth v. Carroll*, establishes that "no time is too short" to form the premeditation necessary for first-degree murder. As long as the defendant forms a conscious decision to kill before committing the act, premeditation is satisfied, even if formed in a fraction of a second. Because Carmine made a conscious decision to kill in the seconds after the insult, his actions fully meet this legal standard. Therefore, (a) correctly concludes he is guilty.
(b) Argument-for: Premeditation can often be inferred from a defendant's prior acts of preparation or the staging of a weapon. A student could argue that bringing a loaded revolver and leaving it readily accessible on the boat console constitutes an inherently dangerous act of preparation. This pre-existing readiness to use deadly force demonstrates a prior plan to cause lethal harm to anyone on board, which justifies a finding of premeditated first-degree murder.
(c) Argument-for: Even under the lenient "no time is too short" Pennsylvania rule, premeditation still requires a deliberate decision rather than an unreflecting response. A student could argue that reacting to a vicious insult by grabbing a gun and firing in under ten seconds is the epitome of an impulsive reflex. Because true premeditation requires at least some modicum of conscious deliberation rather than pure instinct, this brief, reactive timeframe precludes a first-degree murder conviction.
(d) Argument-for: Premeditated murder analyses often look to the defendant's specific intent in bringing the murder weapon to the scene. If Carmine brought the revolver explicitly for a lawful or unrelated purpose (shooting sharks), he lacked the pre-existing intent to murder Paulie when he armed himself. A student could argue that this original innocent intent governs the character of the weapon possession, rendering the subsequent shooting an unplanned crime of opportunity rather than a premeditated killing.
(e) Argument-for: To be guilty of murder, a defendant must act with malice aforethought, which can be mitigated by adequate provocation. A vicious insult about a defendant's wife can incite a sudden heat of passion in a reasonable person, overwhelming their self-control. A student could argue that this intense provocation legally negates the malice required for murder, reducing the crime to voluntary manslaughter.

Head-to-head: Option (a) correctly identifies that under the Pennsylvania rule, the specific timeframe is irrelevant so long as a conscious decision to kill is formed. Option (b) fails because keeping a gun for general purposes does not legally establish a plan to kill specific passengers. Option (c) fails because a short timeframe does not legally mandate a finding of an impulsive reflex, especially under the PA rule. Option (d) fails because the intent at the time of the act controls, not the original reason for carrying a weapon. Option (e) fails because words alone (a vicious insult) are never legally adequate provocation at common law to negate malice. While the distractors contain explicit false legal assumptions, they rely somewhat on factual inferences rather than categorical legal claims. Adding absolute words would firmly lock the distractors as legally falsifiable.

Falsifiable claim per distractor:
- (b): "demonstrates a pre-existing plan" — wrong because keeping a weapon for a different purpose does not legally or automatically establish a plan to kill passengers.
- (c): "constitutes an impulsive reflex" — wrong because shooting quickly does not legally default to an impulsive reflex under the PA rule.
- (d): "his original intent... [precludes premeditation]" — wrong because the specific intent at the exact moment of the act controls, regardless of original intent for bringing the weapon.
- (e): "legally negating the malice required" — wrong because words alone are never legally adequate provocation at common law to negate malice.

Recommended fix: Add absolute words to strictly lock the false legal claims in the distractors.
(b) Yes, because keeping a loaded revolver on the boat console automatically demonstrates a pre-existing plan...
(c) No, because grabbing the gun and shooting in under ten seconds categorically constitutes an impulsive reflex...
(d) No, because his original intent for bringing the revolver was for shooting sharks, which strictly precludes a finding of premeditation.
(e) No, because the vicious insult about his wife provoked the killing, automatically negating the malice required...
-->

## Issue 4 — argpass-opus

**Q1.** Under the Pennsylvania rule for premeditation, is Carmine guilty of first-degree premeditated murder for Paulie's death?

(a) Yes, because a conscious decision to kill, even if formed in the seconds after the insult, fully satisfies the requirement for premeditation. <!-- correct -->
(b) Yes, because keeping a loaded revolver on the boat console demonstrates a pre-existing plan to cause lethal harm to passengers.
(c) No, because grabbing the gun and shooting in under ten seconds constitutes an impulsive reflex rather than a deliberate, pre-planned decision.
(d) No, because his original intent for bringing the revolver was for shooting sharks rather than killing Paulie.
(e) No, because the vicious insult about his wife provoked the killing, legally negating the malice required for murder.

**Answer:** (a)

**Explanation:** Under the Pennsylvania rule (*Commonwealth v. Carroll*), "no time is too short" to form premeditation. A conscious decision to kill, even if formed in a brief instant before acting, suffices for first-degree murder. The fact that Carmine did not pre-plan the murder does not defeat premeditation under this standard. (b) is wrong because the rule does not require a pre-existing plan or preparation. (c) is wrong because the PA rule explicitly permits convictions based on rapid, spur-of-the-moment decisions. (d) is wrong because the relevant intent is assessed at the moment of the shooting, not the reason for initially carrying the weapon. (e) is wrong because words alone are never legally adequate provocation at common law to reduce murder to manslaughter.

**Tags:** chapters: [12], topics: [premeditation, pennsylvania-rule], difficulty: easy, cognitive: application

**Grounding:** Chapter 12: no-time-too-short

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the Pennsylvania rule (*Commonwealth v. Carroll*), "no time is too short" for a defendant to form the intent to kill. Premeditation does not require a prolonged period of reflection or a pre-existing plan. Thus, a conscious decision to kill, even if formed in the seconds immediately following an insult, fully satisfies the requirement. Carmine's actions align perfectly with this standard, making him guilty of first-degree murder.
(b) Argument-for: A student could argue that keeping a loaded revolver readily accessible on a boat console is circumstantial evidence of preparation and a pre-existing plan. Premeditation often involves bringing a deadly weapon to the scene. Therefore, having the loaded gun at hand effectively demonstrates a readiness and plan to cause lethal harm, satisfying the premeditation requirement through prior preparation.
(c) Argument-for: Some courts emphasize that true premeditation requires actual reflection and a "cool mind." Grabbing a gun and shooting in under ten seconds in response to an insult could be characterized purely as an impulsive reflex or a rash, unconsidered action. Even under flexible standards, true premeditation requires a conscious choice rather than a mere automatic response, meaning the brevity of time precludes premeditation.
(d) Argument-for: To be guilty of premeditated murder, the defendant's plan must be directed toward the victim. If the original and sole intent for bringing the weapon was a lawful or distinct purpose—like shooting sharks—then the presence of the weapon cannot be used to infer a pre-planned intent to kill Paulie. Without prior intent directed at the victim, the sudden shooting lacks the necessary long-standing premeditation.
(e) Argument-for: Murder requires malice aforethought, which is negated if the killing occurs in the heat of passion upon adequate provocation. A vicious insult about one's wife can incite a sudden and intense passion, clouding reason and judgment. By provoking the killing, the insult legally negates malice, thereby reducing the crime from first-degree murder to voluntary manslaughter.

Head-to-head: Option (a) correctly identifies and applies the Pennsylvania rule's "no time is too short" standard. Option (b) makes a false factual/legal leap that bringing a gun for one purpose demonstrates a plan to harm passengers. Option (c) falsely asserts that a ten-second timeframe inherently constitutes an impulsive reflex under the PA rule. Option (d) relies on the false premise that original intent controls and precludes subsequent instantaneous premeditation. Option (e) relies on the false legal claim that mere words can legally negate malice. While the keyed answer is clearly best, the distractors would benefit from absolute locking words to ensure they contain explicitly false, unfudgeable legal claims.

Falsifiable claim per distractor:
- (b): "demonstrates a pre-existing plan to cause lethal harm to passengers" — wrong because possessing a gun for shooting sharks does not automatically or legally demonstrate a pre-existing plan to harm passengers.
- (c): "shooting in under ten seconds constitutes an impulsive reflex" — wrong because under the PA rule, a killing in under ten seconds can legally constitute a deliberate, premeditated decision; it does not universally constitute a reflex.
- (d): "because his original intent... was for shooting sharks rather than killing Paulie" — wrong because original intent for carrying a weapon does not legally preclude forming premeditation at the time of the act.
- (e): "the vicious insult about his wife provoked the killing, legally negating the malice" — wrong because at common law, mere words or insults never legally constitute adequate provocation to negate malice.

Recommended fix: Add absolute locking words to distractors to firmly establish their falsifiability. For example: (c) "categorically constitutes"; (d) "original intent... automatically precludes"; (e) "always legally negating" or "categorically negating".
-->
