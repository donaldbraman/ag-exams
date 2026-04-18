# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q6.** Assume Quinn is charged with involuntary manslaughter under the traditional misdemeanor-manslaughter rule based on his reckless speeding. Which of the following is true?

(a) The prosecution must independently prove that Quinn's driving constituted a gross deviation from the standard of care a reasonable person would exercise.
(b) The prosecution can secure a conviction because Quinn's intent to commit the underlying traffic misdemeanor substitutes for the required manslaughter mens rea. <!-- correct -->
(c) Quinn cannot be convicted under this rule because traffic violations are malum prohibitum and thus categorically excluded from serving as predicate offenses.
(d) Quinn cannot be convicted because the unlawful aspect of his conduct (speeding) was not proximately causally connected to the victim's tragic death.
(e) The prosecution must prove that Quinn possessed actual, subjective awareness that his reckless driving created a substantial and unjustifiable risk of death.

**Answer:** (b)

**Explanation:** Under the traditional misdemeanor-manslaughter rule, an unintentional killing that occurs during the commission of an unlawful act constitutes involuntary manslaughter. The intent to commit the underlying misdemeanor substitutes for the culpable mental state (negligence or recklessness) ordinarily required for manslaughter, creating a form of constructive liability for the resulting death. (a) is wrong because this describes standard involuntary manslaughter, which the misdemeanor-manslaughter rule specifically bypasses. (c) is wrong because many jurisdictions apply the rule to malum prohibitum offenses so long as they are dangerous or causally connected to the death. (d) is wrong because speeding is the exact unlawful aspect of the conduct that caused the collision, satisfying proximate causation. (e) is wrong because this describes the subjective recklessness standard, which is not required when constructive liability applies.

**Tags:** chapters: [14], topics: [misdemeanor manslaughter, constructive liability], difficulty: easy, cognitive: application

**Grounding:** Chapter 14, mm-strict-liability-structure; the intent to commit the misdemeanor substitutes for the manslaughter mens rea (State v. Weitbrecht).

<!-- GROUNDING-FAIL: misdemeanor-manslaughter / constructive liability is not in any chapter map. The closest taught doctrines are: NONE (meta-map artifact is missing from the prompt context, preventing independent verification). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q6.** Assume Quinn is charged with involuntary manslaughter under the traditional misdemeanor-manslaughter rule based on his reckless speeding. Which of the following is true?

(a) The prosecution must independently prove that Quinn's driving constituted a gross deviation from the standard of care a reasonable person would exercise.
(b) The prosecution can secure a conviction because Quinn's intent to commit the underlying traffic misdemeanor substitutes for the required manslaughter mens rea. <!-- correct -->
(c) Quinn cannot be convicted under this rule because traffic violations are malum prohibitum and thus categorically excluded from serving as predicate offenses.
(d) Quinn cannot be convicted because the unlawful aspect of his conduct (speeding) was not proximately causally connected to the victim's tragic death.
(e) The prosecution must prove that Quinn possessed actual, subjective awareness that his reckless driving created a substantial and unjustifiable risk of death.

**Answer:** (b)

**Explanation:** Under the traditional misdemeanor-manslaughter rule, an unintentional killing that occurs during the commission of an unlawful act constitutes involuntary manslaughter. The intent to commit the underlying misdemeanor substitutes for the culpable mental state (negligence or recklessness) ordinarily required for manslaughter, creating a form of constructive liability for the resulting death. (a) is wrong because this describes standard involuntary manslaughter, which the misdemeanor-manslaughter rule specifically bypasses. (c) is wrong because many jurisdictions apply the rule to malum prohibitum offenses so long as they are dangerous or causally connected to the death. (d) is wrong because speeding is the exact unlawful aspect of the conduct that caused the collision, satisfying proximate causation. (e) is wrong because this describes the subjective recklessness standard, which is not required when constructive liability applies.

**Tags:** chapters: [14], topics: [misdemeanor manslaughter, constructive liability], difficulty: easy, cognitive: application

**Grounding:** Chapter 14, mm-strict-liability-structure; the intent to commit the misdemeanor substitutes for the manslaughter mens rea (State v. Weitbrecht).

<!-- audit: MUST FIX
check 1: finding - Option (b) asserts the prosecution "can secure a conviction" but this cannot be determined without factual grounding on causation and the occurrence of a death.
check 2: pass
check 3: pass
check 4: finding - Catastrophic failure. The stem contains no facts whatsoever about a death, a victim, or a collision. Distractor (d) and the explanation refer to a "tragic death" and "collision", but without facts provided in the stem, a student has no way to evaluate proximate cause to rule out (d) or confirm (b).
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Add a factual scenario to the stem. For example: "Assume Quinn is recklessly speeding and collides with a pedestrian, killing them. Quinn is charged..."
-->

## Issue 3 — argpass-sonnet

**Q6.** Assume Quinn is charged with involuntary manslaughter under the traditional misdemeanor-manslaughter rule based on his reckless speeding. Which of the following is true?

(a) The prosecution must independently prove that Quinn's driving constituted a gross deviation from the standard of care a reasonable person would exercise.
(b) The prosecution can secure a conviction because Quinn's intent to commit the underlying traffic misdemeanor substitutes for the required manslaughter mens rea. <!-- correct -->
(c) Quinn cannot be convicted under this rule because traffic violations are malum prohibitum and thus categorically excluded from serving as predicate offenses.
(d) Quinn cannot be convicted because the unlawful aspect of his conduct (speeding) was not proximately causally connected to the victim's tragic death.
(e) The prosecution must prove that Quinn possessed actual, subjective awareness that his reckless driving created a substantial and unjustifiable risk of death.

**Answer:** (b)

**Explanation:** Under the traditional misdemeanor-manslaughter rule, an unintentional killing that occurs during the commission of an unlawful act constitutes involuntary manslaughter. The intent to commit the underlying misdemeanor substitutes for the culpable mental state (negligence or recklessness) ordinarily required for manslaughter, creating a form of constructive liability for the resulting death. (a) is wrong because this describes standard involuntary manslaughter, which the misdemeanor-manslaughter rule specifically bypasses. (c) is wrong because many jurisdictions apply the rule to malum prohibitum offenses so long as they are dangerous or causally connected to the death. (d) is wrong because speeding is the exact unlawful aspect of the conduct that caused the collision, satisfying proximate causation. (e) is wrong because this describes the subjective recklessness standard, which is not required when constructive liability applies.

**Tags:** chapters: [14], topics: [misdemeanor manslaughter, constructive liability], difficulty: easy, cognitive: application

**Grounding:** Chapter 14, mm-strict-liability-structure; the intent to commit the misdemeanor substitutes for the manslaughter mens rea (State v. Weitbrecht).

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could defend (a) by arguing that involuntary manslaughter traditionally requires criminal negligence, defined as a gross deviation from the standard of care. Because modern jurisdictions heavily disfavor constructive liability, a student might reason that even when a misdemeanor occurs, the prosecution still must independently prove this gross deviation. Thus, the underlying speeding doesn't automatically secure a conviction without independent proof of negligence.
(b) Argument-for: A student could defend (b) by relying on the black-letter definition of the traditional misdemeanor-manslaughter rule. Under this rule, the intent to commit the underlying unlawful act (the misdemeanor of speeding) transfers or substitutes for the manslaughter mens rea. This creates constructive liability, allowing the prosecution to secure a conviction without proving independent recklessness or negligence regarding the death.
(c) Argument-for: A student could defend (c) by noting that speeding is a strict liability traffic offense, classifying it as malum prohibitum. Under the strict historical common law approach, only malum in se offenses (those inherently wrong) could serve as predicate offenses for the misdemeanor-manslaughter rule. Therefore, a student could argue that traffic violations are categorically excluded from triggering constructive liability.
(d) Argument-for: A student could defend (d) by pointing out that speeding is merely a condition of driving, and the velocity itself may not be the direct proximate cause of a death. Courts require that the unlawful aspect of the act be the proximate cause of death. If the death resulted from an independent intervening factor rather than the speed itself, proximate causation fails, precluding conviction.
(e) Argument-for: A student could defend (e) by focusing on the prompt's use of the word "reckless." Recklessness, by definition under the Model Penal Code and many common law jurisdictions, requires subjective awareness of a substantial and unjustifiable risk. Therefore, to base a charge on "reckless speeding," the prosecution must prove this subjective awareness of the risk of death.

Head-to-head: Option (b) correctly states the legal operation of the traditional misdemeanor-manslaughter rule. Options (a) and (e) both contain falsifiable legal claims, asserting that the prosecution "must independently prove" gross deviation or subjective awareness, which is directly contradicted by the traditional rule's use of constructive liability. Option (c) is cleanly falsifiable because it asserts that malum prohibitum offenses are "categorically excluded," which is false since many traditional jurisdictions allow them if proximate cause is met. Option (d), however, presents a fatal issue: it relies on facts that do not exist. It asserts the speeding "was not proximately causally connected to the victim's tragic death," yet the prompt completely omits a fact pattern regarding a collision, a victim, or how the death occurred. The explanation for (d) hallucinates that "speeding is the exact unlawful aspect... that caused the collision," confirming the author accidentally deleted or forgot to write the actual fact pattern.

Falsifiable claim per distractor:
- (a): "The prosecution must independently prove that Quinn's driving constituted a gross deviation" — wrong because under the traditional rule, constructive liability substitutes for independent proof.
- (c): "traffic violations are... categorically excluded" — wrong because many jurisdictions permit malum prohibitum offenses to serve as predicates if they proximately cause death.
- (d): "was not proximately causally connected to the victim's tragic death" — wrong factually (assuming the author's intended missing facts are added), but currently untestable because the prompt contains no facts about a death or collision.
- (e): "The prosecution must prove that Quinn possessed actual, subjective awareness" — wrong because constructive liability bypasses the need to prove subjective awareness of the risk of death.

Recommended fix: Add the missing fact pattern to the prompt: "Assume Quinn was recklessly speeding when he struck and killed a pedestrian. Quinn is charged with involuntary manslaughter under the traditional misdemeanor-manslaughter rule based on his reckless speeding. Which of the following is true?" Additionally, to ensure (d) contains an explicitly false legal claim rather than a mere factual dispute, revise it to: "(d) Quinn cannot be convicted because speeding is a regulatory offense, which categorically precludes a finding of proximate causation for manslaughter."
-->

## Issue 4 — argpass-opus

**Q6.** Assume Quinn is charged with involuntary manslaughter under the traditional misdemeanor-manslaughter rule based on his reckless speeding. Which of the following is true?

(a) The prosecution must independently prove that Quinn's driving constituted a gross deviation from the standard of care a reasonable person would exercise.
(b) The prosecution can secure a conviction because Quinn's intent to commit the underlying traffic misdemeanor substitutes for the required manslaughter mens rea. <!-- correct -->
(c) Quinn cannot be convicted under this rule because traffic violations are malum prohibitum and thus categorically excluded from serving as predicate offenses.
(d) Quinn cannot be convicted because the unlawful aspect of his conduct (speeding) was not proximately causally connected to the victim's tragic death.
(e) The prosecution must prove that Quinn possessed actual, subjective awareness that his reckless driving created a substantial and unjustifiable risk of death.

**Answer:** (b)

**Explanation:** Under the traditional misdemeanor-manslaughter rule, an unintentional killing that occurs during the commission of an unlawful act constitutes involuntary manslaughter. The intent to commit the underlying misdemeanor substitutes for the culpable mental state (negligence or recklessness) ordinarily required for manslaughter, creating a form of constructive liability for the resulting death. (a) is wrong because this describes standard involuntary manslaughter, which the misdemeanor-manslaughter rule specifically bypasses. (c) is wrong because many jurisdictions apply the rule to malum prohibitum offenses so long as they are dangerous or causally connected to the death. (d) is wrong because speeding is the exact unlawful aspect of the conduct that caused the collision, satisfying proximate causation. (e) is wrong because this describes the subjective recklessness standard, which is not required when constructive liability applies.

**Tags:** chapters: [14], topics: [misdemeanor manslaughter, constructive liability], difficulty: easy, cognitive: application

**Grounding:** Chapter 14, mm-strict-liability-structure; the intent to commit the misdemeanor substitutes for the manslaughter mens rea (State v. Weitbrecht).

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that because a traffic violation is generally a low-level offense, traditional jurisdictions require independent proof of a gross deviation from the standard of care (criminal negligence) to elevate a resulting death to manslaughter.
(b) Argument-for: Under the traditional misdemeanor-manslaughter (unlawful act) doctrine, the mens rea required for the underlying misdemeanor effectively substitutes for the mens rea ordinarily required for manslaughter. A student would correctly recognize this as the central mechanism of constructive liability defining the rule.
(c) Argument-for: Because speeding is a regulatory, *malum prohibitum* offense rather than one inherently evil (*malum in se*), a student might reason that it lacks the moral culpability necessary for a homicide conviction. Therefore, such traffic offenses must be categorically excluded from serving as predicate misdemeanors.
(d) Argument-for: A student might notice that the prompt provides absolutely zero facts establishing a causal link between the speeding and the death (or even that a crash occurred). Without facts showing proximate causation, a student could logically conclude that the prosecution's case fails on causation grounds.
(e) Argument-for: The prompt explicitly uses the phrase "reckless speeding." Because the legal definition of recklessness requires actual, subjective awareness of a substantial and unjustifiable risk, a student could conclude that the prosecution must prove this subjective mens rea regarding the risk of death to secure a conviction.

Head-to-head: 
The keyed answer (b) accurately describes the doctrine of mens rea substitution under the traditional misdemeanor-manslaughter rule. However, the question as written is fundamentally flawed because it is missing its factual scenario. The prompt mentions "the victim's tragic death" in the options, and the explanation explicitly relies on facts that aren't there ("speeding is the exact unlawful aspect of the conduct that caused the collision"). Because the prompt omits any details about a collision or causation, (d)'s assertion that proximate causation is lacking is arguably correct based solely on the (empty) provided text. Additionally, (b)'s claim that the prosecution "can secure a conviction" assumes actus reus and causation elements that are absent. Distractors (a), (c), and (e) contain explicit, falsifiable legal errors, but the missing fact pattern makes this question a MUST FIX.

Falsifiable claim per distractor:
- (a): "must independently prove that Quinn's driving constituted a gross deviation" — wrong because the traditional rule's defining feature is that it substitutes the misdemeanor intent for the manslaughter mens rea, explicitly bypassing independent proof of gross deviation.
- (c): "categorically excluded from serving as predicate offenses" — wrong because many traditional jurisdictions permit malum prohibitum offenses to serve as predicates, provided proximate cause or foreseeability is established.
- (d): "was not proximately causally connected to the victim's tragic death" — wrong based on the *intended* fact pattern (where the speeding caused the crash), but currently broken/unfalsifiable because the prompt contains no facts about the incident whatsoever.
- (e): "must prove that Quinn possessed actual, subjective awareness... of death" — wrong because the traditional rule imposes constructive liability; the prosecution only needs to prove the mens rea of the underlying misdemeanor, not subjective awareness of the risk of death.

Recommended fix: Add the missing factual context to the prompt. Rewrite the prompt to read: "Assume Quinn was recklessly speeding down a residential street and struck a pedestrian, causing her tragic death. Quinn is charged with involuntary manslaughter under the traditional misdemeanor-manslaughter rule based on this conduct. Which of the following is true?"
-->
