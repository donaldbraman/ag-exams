# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q11.** Assume it is established that Bex possessed the required mens rea and is charged as an accomplice to intentional murder. Does her duress defense succeed?

(a) Yes, because a person of reasonable firmness would have been completely unable to resist Alba's imminent threat of lethal violence.
(b) Yes, because Bex did not personally inflict the fatal harm, making the duress defense fully available for all secondary actors.
(c) No, because the common law categorically bars the use of the duress defense to justify or excuse participation in intentional murder. <!-- correct -->
(d) No, because Bex was at fault in creating the emergency by initially agreeing to participate in the fentanyl distribution operation.
(e) No, because the threat to Bex was not sufficiently imminent since Alba was primarily focused on dealing with the interrupting neighbor.

**Answer:** (c)

**Explanation:** (c) is correct because under the common law, the duress defense is categorically unavailable as an excuse for an intentional homicide; a defendant may not choose to sacrifice an innocent life to save their own. (a) is wrong because the objective reasonable firmness standard is overridden by the categorical homicide bar. (b) is wrong because the homicide bar applies to accomplices to intentional murder just as it does to principals. (d) is wrong because while being at fault in creating the emergency limits duress, the categorical homicide bar is the primary absolute obstacle to the defense here. (e) is wrong because Alba holding Bex at gunpoint is highly imminent; the defense fails due to the murder charge, not the timing.

**Tags:** chapters: [21], topics: [duress, murder bar, accomplice liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 21, duress-murder-bar

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: The distractor (d) inadvertently presents a second fully valid legal reason Bex's duress defense would fail. Under common law, voluntarily joining a criminal enterprise where one knows the co-conspirator is armed (the facts state Bex agreed to the operation and "knew Alba was armed") constitutes being "at fault" in creating the coercive situation, which categorically bars the duress defense. This creates a dual-correct-answer problem between (c) and (d). 
3. Cross-Question Spoilers: pass
Recommended fix: Rewrite (d) to rely on a demonstrably false legal premise so (c) is the only correct path. For example: "(d) No, because the common law duress defense is only available to protect a third party, not oneself."
-->

## Issue 3 — argpass-sonnet

**Q11.** Assume it is established that Bex possessed the required mens rea and is charged as an accomplice to intentional murder. Does her duress defense succeed?

(a) Yes, because a person of reasonable firmness would have been completely unable to resist Alba's imminent threat of lethal violence.
(b) Yes, because Bex did not personally inflict the fatal harm, making the duress defense fully available for all secondary actors.
(c) No, because the common law categorically bars the use of the duress defense to justify or excuse participation in intentional murder. <!-- correct -->
(d) No, because Bex was at fault in creating the emergency by initially agreeing to participate in the fentanyl distribution operation.
(e) No, because the threat to Bex was not sufficiently imminent since Alba was primarily focused on dealing with the interrupting neighbor.

**Answer:** (c)

**Explanation:** (c) is correct because under the common law, the duress defense is categorically unavailable as an excuse for an intentional homicide; a defendant may not choose to sacrifice an innocent life to save their own. (a) is wrong because the objective reasonable firmness standard is overridden by the categorical homicide bar. (b) is wrong because the homicide bar applies to accomplices to intentional murder just as it does to principals. (d) is wrong because while being at fault in creating the emergency limits duress, the categorical homicide bar is the primary absolute obstacle to the defense here. (e) is wrong because Alba holding Bex at gunpoint is highly imminent; the defense fails due to the murder charge, not the timing.

**Tags:** chapters: [21], topics: [duress, murder bar, accomplice liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 21, duress-murder-bar

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the Model Penal Code § 2.09, which many modern jurisdictions adopt, the categorical common law "homicide bar" is rejected in favor of an objective standard. The MPC allows a duress defense for any crime, including murder, if a person of reasonable firmness in the actor's situation would have been unable to resist the coercion. Given that Bex faced an imminent threat of lethal violence (a gun to her head), a person of reasonable firmness would likely succumb to save their own life, making the defense successful regardless of the homicide charge.

(b) Argument-for: There is a significant minority legal theory and historical debate suggesting that the moral "choice of evils" rationale for the murder bar should only apply to the principal who directly takes the life. In this view, an accomplice who provides minor or secondary assistance under the threat of death did not personally "inflict the fatal harm" and thus did not make the ultimate choice to kill. Therefore, the duress defense remains fully available to secondary actors even when the underlying charge is intentional murder.

(c) Argument-for: The common law has maintained for centuries that no person may take the life of an innocent human being to save their own. Because the law values all lives equally, it demands that a person face death rather than commit murder; consequently, the duress defense is categorically barred for intentional homicide. Since Bex is charged as an accomplice to intentional murder, her participation is legally inexcusable under the common law, even if she acted under an absolute threat of death.

(d) Argument-for: A fundamental limitation on the duress defense is the "fault in the situation" doctrine, which provides that the defense is unavailable if the defendant recklessly placed themselves in a situation where coercion was foreseeable. By voluntarily joining a fentanyl distribution operation—a known violent criminal enterprise—Bex assumed the risk of lethal threats from her co-conspirators. This prior fault serves as an independent and sufficient legal basis to deny her the defense, even before considering the nature of the specific crime charged.

(e) Argument-for: To successfully plead duress, the threat of death or serious bodily injury must be "imminent," meaning it must be present and immediate at the exact moment the crime is committed. If Alba’s focus shifted "primarily" to an interrupting neighbor, the immediate pressure on Bex was momentarily suspended, providing her a window to escape or desist. Because the threat lacked the requisite legal imminency at the time Bex assisted in the murder, the defense fails on its own terms.

Head-to-head: (c) is the strongest answer because the "homicide bar" is a categorical, absolute rule of common law that renders all other considerations—such as the reasonableness of Bex's fear (a) or her role as an accomplice (b)—irrelevant. (d) is a very strong distractor because "fault in the situation" is a valid legal ground to deny duress, but it is fact-dependent and logically secondary to the categorical murder bar. (e) is the weakest "No" answer because being held at gunpoint generally satisfies imminency regardless of the perpetrator's momentary gaze. (a) and (b) are legally incorrect under the prevailing common law rule. The question is flagged "SHOULD FIX" because option (d) is a legally sound reason to deny the defense that lacks an explicit falsifiable error, making it a potentially "correct" alternative to (c).

Falsifiable claim per distractor:
- (a): "Yes, because a person of reasonable firmness would have been completely unable to resist" — wrong because the common law homicide bar applies regardless of whether the actor's fear met the reasonable firmness standard.
- (b): "making the duress defense fully available for all secondary actors" — wrong because the majority of common law jurisdictions apply the murder bar to accomplices and principals alike.
- (d): "Bex was at fault in creating the emergency by initially agreeing to participate in the fentanyl distribution operation" — This is not necessarily false; it is a legally plausible application of the "prior fault" rule, though it is less "categorical" than the murder bar.
- (e): "the threat to Bex was not sufficiently imminent" — wrong because a lethal threat at gunpoint satisfies the imminency requirement even if the threatener is momentarily distracted by a third party.

Recommended fix: Add absolute "locking" language to (d) to make it falsifiable (e.g., "because voluntary participation in any illegal activity automatically bars the duress defense for all subsequent crimes") and add an absolute to (a) to ensure it is clearly incorrect at common law (e.g., "Yes, because the reasonable firmness standard always overrides the nature of the crime charged").
-->

## Issue 4 — argpass-opus

**Q11.** Assume it is established that Bex possessed the required mens rea and is charged as an accomplice to intentional murder. Does her duress defense succeed?

(a) Yes, because a person of reasonable firmness would have been completely unable to resist Alba's imminent threat of lethal violence.
(b) Yes, because Bex did not personally inflict the fatal harm, making the duress defense fully available for all secondary actors.
(c) No, because the common law categorically bars the use of the duress defense to justify or excuse participation in intentional murder. <!-- correct -->
(d) No, because Bex was at fault in creating the emergency by initially agreeing to participate in the fentanyl distribution operation.
(e) No, because the threat to Bex was not sufficiently imminent since Alba was primarily focused on dealing with the interrupting neighbor.

**Answer:** (c)

**Explanation:** (c) is correct because under the common law, the duress defense is categorically unavailable as an excuse for an intentional homicide; a defendant may not choose to sacrifice an innocent life to save their own. (a) is wrong because the objective reasonable firmness standard is overridden by the categorical homicide bar. (b) is wrong because the homicide bar applies to accomplices to intentional murder just as it does to principals. (d) is wrong because while being at fault in creating the emergency limits duress, the categorical homicide bar is the primary absolute obstacle to the defense here. (e) is wrong because Alba holding Bex at gunpoint is highly imminent; the defense fails due to the murder charge, not the timing.

**Tags:** chapters: [21], topics: [duress, murder bar, accomplice liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 21, duress-murder-bar

<!-- argument-pass: MUST FIX
(a) Argument-for: Under the Model Penal Code, the categorical common-law bar against using duress as a defense to intentional murder is eliminated. MPC § 2.09 allows the duress defense for any offense, including murder, if the defendant was coerced by a threat of force that a person of reasonable firmness in their situation would have been unable to resist. Assuming the jurisdiction follows the MPC and an objectively reasonable person would yield to Alba's lethal threat, Bex's defense would succeed, making this option correct.
(b) Argument-for: While the traditional common law rule bars the duress defense for the principal in the first degree to intentional murder, some legal theorists and minority jurisdictions have recognized exceptions for secondary actors. An accomplice who does not personally inflict the fatal blow is arguably less culpable and is not directly making the choice to trade an innocent life for their own in the same manner. Therefore, Bex could successfully claim duress because her role was strictly secondary, avoiding the categorical murder bar.
(c) Argument-for: The common law features a strict, well-established rule that duress is never a defense to intentional murder. This categorical bar is based on the principle that a person must not save their own life by killing an innocent victim. Because the prompt establishes that Bex possessed the required mens rea for intentional murder and is charged as an accomplice to it, the common law rule applies equally to her, making the defense completely unavailable regardless of the severity of Alba's threat.
(d) Argument-for: The defense of duress is universally unavailable to a defendant who recklessly places herself in a situation where she is likely to be subjected to coercion. By voluntarily joining a fentanyl distribution operation—a dangerous criminal enterprise inherently associated with violence—Bex was at fault in creating the emergency. This threshold limitation defeats the duress defense independently of the murder charge, making her initial fault a fully sufficient legal basis to deny the defense under the common law.
(e) Argument-for: A fundamental requirement of the common-law duress defense is that the threat must be present, imminent, and impending, leaving the defendant with no reasonable opportunity to escape. If Alba was distracted and primarily focused on dealing with the interrupting neighbor, the imminence of the threat to Bex was broken. Without an immediate threat strictly compelling her action at that exact moment, the defense of duress fails on its core elements, making this the correct procedural reason for failure.

Head-to-head: 
Option (c) accurately states the traditional common-law rule barring duress for intentional murder. However, the stem fails to specify the jurisdiction, meaning (a) could be perfectly correct under the Model Penal Code. Furthermore, (d) presents a classic "true but not primary" distractor; if Bex was indeed at fault by joining a drug ring, her duress defense would be legally barred on those grounds as well, meaning (d) contains no explicitly false legal claim and is arguably just as correct as (c) under the common law. Option (b) successfully uses absolute language ("fully available for all secondary actors") to become falsifiable. Option (e) relies on a factual interpretation of imminence rather than a false legal rule. Because (d) is legally true and (a) is potentially true depending on jurisdiction, the question requires significant edits.

Falsifiable claim per distractor:
- (a): "a person of reasonable firmness would have been completely unable to resist" — NOT explicitly false; this is the correct standard under the MPC, and the stem fails to specify the common law.
- (b): "fully available for all secondary actors" — wrong because the common law murder bar applies to accomplices to intentional murder just as it does to principals.
- (d): "because Bex was at fault in creating the emergency" — NOT explicitly false; under common law, being at fault in creating the coercive situation is a fully valid, independent reason to deny the defense.
- (e): "was not sufficiently imminent since Alba was primarily focused" — NOT explicitly false legally; it merely asserts a factual interpretation that could arguably defeat the imminence element, lacking a falsifiable rule of law.

Recommended fix: 1) In the stem, ask: "Under the common law, does her duress defense succeed?" 2) In (a), add an absolute: "Yes, because the common law categorically excuses accomplices who face imminent lethal violence." 3) In (d), add an absolute error: "No, solely because any prior criminal activity automatically permanently waives the duress defense for all future acts." 4) In (e), lock it: "No, because a threat of violence is categorically never imminent if the coercer looks away."
-->
