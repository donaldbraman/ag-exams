# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** Leo is charged with criminal homicide for shooting the watchman. Given his actions in Fact 5, what is the most appropriate grading for this offense under the common law?

(a) Involuntary manslaughter, because firing a weapon during a high-stress encounter constitutes gross criminal negligence rather than a fully intentional lethal act.
(b) Voluntary manslaughter, because the sudden appearance of the watchman provided adequate legal provocation to completely mitigate the element of malice aforethought.
(c) Second-degree murder, because his immediate reaction to the surprise appearance shows intent to kill but lacks the reflection required for premeditation and deliberation. <!-- correct -->
(d) First-degree murder, because the law automatically presumes premeditation and deliberation whenever a defendant brings a concealed weapon to an active crime scene.
(e) Negligent homicide, because the lack of any verbal exchange indicates he did not subjectively perceive the substantial risk of causing death.

**Answer:** (c)

**Explanation:** Second-degree murder is the appropriate grade. Leo's act of drawing a weapon and shooting directly at the watchman establishes the intent to kill (malice aforethought), but the instantaneous nature of the reaction to a surprise appearance strongly suggests a lack of the quiet reflection required for premeditation and deliberation. (a) is wrong because shooting directly at someone is an intentional act, not mere negligence. (b) is wrong because a watchman doing his job is not adequate provocation under the traditional common law categories. (d) is wrong because premeditation is not automatically presumed from carrying a concealed weapon; it still requires proof of actual reflection. (e) is wrong because his act of shooting was intentional, not merely negligent.

**Tags:** chapters: [12, 13], topics: [homicide grading, malice, premeditation], difficulty: medium, cognitive: application

**Grounding:** Chapter 12 (Intentional Homicide), four-elements-common-law refinement.

<!-- audit: MUST FIX
check 1: Fails. Option (c) is marked correct based on the premise that an "instantaneous reaction" lacks premeditation. However, in jurisdictions following the traditional "no time is too short" doctrine (mapped in Ch 12), this instantaneous reaction could legally constitute first-degree premeditated murder.
check 2: Pass. While the correct answer is vulnerable, the distractors all contain fatal flaws or absolute language (e.g., "automatically presumes" in (d)), making them difficult for a student to affirmatively defend as the *best* answer, even if they reject (c).
check 3: Fails. The explanation relies entirely on the requirement for "quiet reflection." This reasoning reflects only one side of the common law split (the *Guthrie* approach) and ignores the "no time is too short" doctrine taught in the course. 
check 4: Fails. The stem references "Fact 5" which is missing from the prompt. Furthermore, option (d) reveals the defendant is at an "active crime scene," which raises the unaddressed issue of Felony Murder.
check 5: Fails. The question asks for the grading under "the common law," but the common law is famously split on whether premeditation requires actual reflection or if "no time is too short." The stem fails to stipulate the specific jurisdictional rule necessary to resolve this.
check 6: Pass. No excluded topics are present.
check 7: Pass. Homicide grading and premeditation are covered in Ch 12.
Recommended fix: Remove the floating reference to "Fact 5" and supply the necessary facts in the stem. Explicitly stipulate the jurisdiction's premeditation rule (e.g., "Assume the jurisdiction requires actual reflection for premeditation and rejects the 'no time is too short' rule") and state that the prosecution is not pursuing a felony murder theory.
-->

## Issue 2 — edge-case

**Q9.** Leo is charged with criminal homicide for shooting the watchman. Given his actions in Fact 5, what is the most appropriate grading for this offense under the common law?

(a) Involuntary manslaughter, because firing a weapon during a high-stress encounter constitutes gross criminal negligence rather than a fully intentional lethal act.
(b) Voluntary manslaughter, because the sudden appearance of the watchman provided adequate legal provocation to completely mitigate the element of malice aforethought.
(c) Second-degree murder, because his immediate reaction to the surprise appearance shows intent to kill but lacks the reflection required for premeditation and deliberation. <!-- correct -->
(d) First-degree murder, because the law automatically presumes premeditation and deliberation whenever a defendant brings a concealed weapon to an active crime scene.
(e) Negligent homicide, because the lack of any verbal exchange indicates he did not subjectively perceive the substantial risk of causing death.

**Answer:** (c)

**Explanation:** Second-degree murder is the appropriate grade. Leo's act of drawing a weapon and shooting directly at the watchman establishes the intent to kill (malice aforethought), but the instantaneous nature of the reaction to a surprise appearance strongly suggests a lack of the quiet reflection required for premeditation and deliberation. (a) is wrong because shooting directly at someone is an intentional act, not mere negligence. (b) is wrong because a watchman doing his job is not adequate provocation under the traditional common law categories. (d) is wrong because premeditation is not automatically presumed from carrying a concealed weapon; it still requires proof of actual reflection. (e) is wrong because his act of shooting was intentional, not merely negligent.

**Tags:** chapters: [12, 13], topics: [homicide grading, malice, premeditation], difficulty: medium, cognitive: application

**Grounding:** Chapter 12 (Intentional Homicide), four-elements-common-law refinement.

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: MUST FIX. The facts explicitly establish that Leo and Marcus were pouring gasoline to commit Arson (a traditional BARRK felony). Under the traditional grading scheme (Pennsylvania model), a killing committed during an Arson is First-Degree Felony Murder. Concluding that the maximum grade is Second-Degree Murder because it lacks premeditation ignores the felony murder rule entirely.
3. Cross-Question Spoilers: MUST FIX. Q3 actively evaluates Felony Murder liability for Marcus for this exact same death. Since Felony Murder is clearly "active" in this scenario, a student who synthesizes the facts will correctly recognize that Leo is guilty of First-Degree Felony Murder, rendering option (c) factually incorrect.
Recommended fix: Modify the question stem to isolate the intended doctrine, e.g., "Assuming the prosecution pursues an intentional homicide theory and does not rely on the felony murder rule, what is the most appropriate grading..."
-->

## Issue 3 — argpass-sonnet

**Q9.** Leo is charged with criminal homicide for shooting the watchman. Given his actions in Fact 5, what is the most appropriate grading for this offense under the common law?

(a) Involuntary manslaughter, because firing a weapon during a high-stress encounter constitutes gross criminal negligence rather than a fully intentional lethal act.
(b) Voluntary manslaughter, because the sudden appearance of the watchman provided adequate legal provocation to completely mitigate the element of malice aforethought.
(c) Second-degree murder, because his immediate reaction to the surprise appearance shows intent to kill but lacks the reflection required for premeditation and deliberation. <!-- correct -->
(d) First-degree murder, because the law automatically presumes premeditation and deliberation whenever a defendant brings a concealed weapon to an active crime scene.
(e) Negligent homicide, because the lack of any verbal exchange indicates he did not subjectively perceive the substantial risk of causing death.

**Answer:** (c)

**Explanation:** Second-degree murder is the appropriate grade. Leo's act of drawing a weapon and shooting directly at the watchman establishes the intent to kill (malice aforethought), but the instantaneous nature of the reaction to a surprise appearance strongly suggests a lack of the quiet reflection required for premeditation and deliberation. (a) is wrong because shooting directly at someone is an intentional act, not mere negligence. (b) is wrong because a watchman doing his job is not adequate provocation under the traditional common law categories. (d) is wrong because premeditation is not automatically presumed from carrying a concealed weapon; it still requires proof of actual reflection. (e) is wrong because his act of shooting was intentional, not merely negligent.

**Tags:** chapters: [12, 13], topics: [homicide grading, malice, premeditation], difficulty: medium, cognitive: application

**Grounding:** Chapter 12 (Intentional Homicide), four-elements-common-law refinement.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that when an individual is surprised and acts in a split-second panic, the action is instinctual and lacks the conscious, directed intent required for murder. Under the theory of gross criminal negligence, an actor's failure to control their actions in a high-stress environment leading to a fatal discharge of a weapon falls squarely within involuntary manslaughter. Because Leo did not have time to form specific intent to kill, his reckless or negligent discharge of the firearm satisfies the mens rea for involuntary manslaughter.
(b) Argument-for: A student might assert that under the common law, "adequate legal provocation" (or heat of passion) can mitigate murder to voluntary manslaughter if the defendant was reasonably provoked and acted before a cooling-off period. The unexpected, sudden appearance of a watchman in a tense situation could be argued to cause extreme fright or panic, analogous to mutual combat or a sudden assault. This fright could produce a "heat of passion" that completely mitigates malice aforethought, making voluntary manslaughter the proper grade.
(c) Argument-for: Under common law, drawing a weapon and shooting someone directly establishes malice aforethought (intent to kill or cause grievous bodily harm), fulfilling the elements of murder. However, first-degree murder requires premeditation and deliberation—a period of quiet reflection. Because Leo's action was an immediate, instantaneous reaction to a surprise appearance, he lacked the time and presence of mind to deliberate, making second-degree murder the appropriate charge.
(d) Argument-for: A student could argue that bringing a lethal weapon to a crime scene demonstrates prior planning and reflection about the possibility of using deadly force. Under common law principles, arming oneself in preparation for a felony can satisfy the requirement for premeditation and deliberation. Therefore, the law automatically elevates the homicide to first-degree murder, presuming that the defendant had already deliberated on the decision to kill.
(e) Argument-for: A student could contend that negligent homicide applies when a defendant fails to perceive a substantial and unjustifiable risk of death. Because there was no verbal exchange or prior interaction, Leo might not have subjectively processed the identity of the person or the lethal risk of his instinctual response. Without subjective awareness of the risk, his mens rea falls below recklessness to mere negligence, justifying a charge of negligent homicide.

Head-to-head: Option (c) is the correct answer because it accurately applies the common law distinction between first- and second-degree murder, noting that a split-second reaction lacks premeditation and deliberation but still demonstrates malice aforethought. Option (d) features a strong distractor but relies on the explicitly false legal claim that the law "automatically presumes" premeditation. Option (b) falsely identifies a watchman's appearance as "adequate legal provocation," which defies established common law categories. Options (a) and (e) present falsifiable claims about the mens rea required, though they rely slightly more on factual inferences ("constitutes," "indicates") rather than locked categorical legal rules. 

Falsifiable claim per distractor:
- (a): "firing a weapon during a high-stress encounter constitutes gross criminal negligence rather than a fully intentional lethal act" — wrong because an intentional lethal act does not become mere negligence simply due to a high-stress encounter.
- (b): "the sudden appearance of the watchman provided adequate legal provocation to completely mitigate" — wrong because common law adequate provocation requires specific triggers (e.g., extreme assault, mutual combat, adultery), not the lawful presence or mere sudden appearance of a watchman.
- (d): "the law automatically presumes premeditation and deliberation whenever a defendant brings a concealed weapon" — wrong because bringing a weapon is merely evidence of premeditation, not an automatic legal presumption.
- (e): "the lack of any verbal exchange indicates he did not subjectively perceive the substantial risk" — wrong because the lack of a verbal exchange has no legal bearing on whether a defendant subjectively perceived the risk of an intentional shooting.

Recommended fix: Change "constitutes" in (a) to "categorically constitutes" and "indicates" in (e) to "categorically proves" to firmly lock the falsifiable legal propositions with absolute words.
-->

## Issue 4 — argpass-opus

**Q9.** Leo is charged with criminal homicide for shooting the watchman. Given his actions in Fact 5, what is the most appropriate grading for this offense under the common law?

(a) Involuntary manslaughter, because firing a weapon during a high-stress encounter constitutes gross criminal negligence rather than a fully intentional lethal act.
(b) Voluntary manslaughter, because the sudden appearance of the watchman provided adequate legal provocation to completely mitigate the element of malice aforethought.
(c) Second-degree murder, because his immediate reaction to the surprise appearance shows intent to kill but lacks the reflection required for premeditation and deliberation. <!-- correct -->
(d) First-degree murder, because the law automatically presumes premeditation and deliberation whenever a defendant brings a concealed weapon to an active crime scene.
(e) Negligent homicide, because the lack of any verbal exchange indicates he did not subjectively perceive the substantial risk of causing death.

**Answer:** (c)

**Explanation:** Second-degree murder is the appropriate grade. Leo's act of drawing a weapon and shooting directly at the watchman establishes the intent to kill (malice aforethought), but the instantaneous nature of the reaction to a surprise appearance strongly suggests a lack of the quiet reflection required for premeditation and deliberation. (a) is wrong because shooting directly at someone is an intentional act, not mere negligence. (b) is wrong because a watchman doing his job is not adequate provocation under the traditional common law categories. (d) is wrong because premeditation is not automatically presumed from carrying a concealed weapon; it still requires proof of actual reflection. (e) is wrong because his act of shooting was intentional, not merely negligent.

**Tags:** chapters: [12, 13], topics: [homicide grading, malice, premeditation], difficulty: medium, cognitive: application

**Grounding:** Chapter 12 (Intentional Homicide), four-elements-common-law refinement.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that Leo's reaction occurred during a "high-stress encounter," implying an unthinking, panic-driven firing of the weapon rather than a deliberate act. Under common law, causing death through gross negligence—such as recklessly discharging a firearm when startled—can be graded as involuntary manslaughter. If the student legally equates sudden panic with a complete lack of specific intent to kill, this option becomes defensible as a negligence claim.
(b) Argument-for: A student might argue that being suddenly surprised by a watchman constitutes a form of provocation. Under the heat of passion doctrine, adequate legal provocation mitigates murder to voluntary manslaughter by negating malice aforethought. If the surprise was overwhelming enough to cause a reasonable person to lose control, Leo's immediate reaction could be seen as acting under a legally mitigating heat of passion.
(c) Argument-for: Second-degree murder encompasses intentional killings that are not premeditated and deliberated. Leo's act of shooting directly at the watchman establishes malice aforethought (intent to kill or cause grievous bodily harm). However, because his reaction was instantaneous and driven by surprise, he lacked the time and cool reflection required for first-degree murder, making second-degree murder the exact doctrinal fit.
(d) Argument-for: First-degree murder requires premeditation and deliberation. A student could argue that bringing a concealed weapon to an active crime scene demonstrates prior planning and a preconceived readiness to kill. Because he armed himself beforehand, a student might incorrectly assume the law applies an automatic presumption of premeditation derived from this calculated choice.
(e) Argument-for: Negligent homicide involves causing death without subjective awareness of the risk. If Leo fired without any verbal exchange, a student could argue he acted on pure reflex, completely lacking the subjective perception of a risk of death. In the absence of subjective awareness, the killing could be framed as purely accidental, fitting a lower tier of negligence.

Head-to-head: 
Option (c) is the clear winner, correctly applying the legal distinction between malice aforethought (intent to kill) and premeditation/deliberation (reflection). Distractor (d) is well-crafted with a strong, explicit legal lock ("automatically presumes... whenever"). Distractor (b) relies on a clear legal error, as common law recognizes rigid categories for adequate provocation that categorically exclude being startled by a lawful watchman. Distractor (a) asserts a false legal rule but lacks an absolute modifier. Distractor (e) relies on a weak factual inference ("indicates") rather than a locked false legal claim, and "negligent homicide" is generally a modern statutory grade (MPC) rather than a traditional common law category. 

Falsifiable claim per distractor:
- (a): "firing a weapon during a high-stress encounter constitutes gross criminal negligence rather than a fully intentional lethal act" — wrong because high stress does not operate as a legal rule to negate intent or reduce an intentional shooting to negligence.
- (b): "the sudden appearance of the watchman provided adequate legal provocation" — wrong because a lawful watchman performing his duties does not fit any traditional common law category of adequate provocation.
- (d): "the law automatically presumes premeditation... whenever a defendant brings a concealed weapon" — wrong because premeditation requires actual proof of reflection; a weapon is merely evidence, not an automatic legal presumption.
- (e): "the lack of any verbal exchange indicates he did not subjectively perceive" — wrong because silence does not legally preclude subjective awareness of risk, and the wording relies on a soft factual inference rather than an explicit legal falsity.

Recommended fix: Add absolute locks to (a) and (e) to eliminate soft factual inferences. Change (a) to: "...because firing a weapon during a high-stress encounter categorically constitutes gross criminal negligence..." Change (e) to: "...because the lack of any verbal exchange conclusively proves he lacked the subjective perception..." (Additionally, changing "Negligent homicide" to "Involuntary manslaughter" in (e) would better align with the prompt's common law constraint).
-->
