# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — edge-case

**Q13.** Assume that, regardless of causation, Blake is charged with the intentional murder of Chris. Can Blake successfully raise the defense of duress?

(a) Yes, because Alex pointing a loaded handgun at Blake's chest constitutes an imminent threat of death that overcomes free will.
(b) Yes, because Blake's role was merely secondary, allowing the court to mitigate his criminal liability based on the coercive circumstances.
(c) No, because the common law categorically bars duress as a defense to intentional homicide regardless of the severity of coercion. <!-- correct -->
(d) No, because Blake could have attempted to disarm Alex or flee the cabin instead of complying with the unlawful order.
(e) No, because accepting financial compensation to act as security legally forfeits the right to claim duress when threatened with violence.

**Answer:** (c)

**Explanation:** (c) is correct because the common law imposes an absolute categorical bar on the use of duress as a defense to intentional homicide. The underlying rationale is that a person may not choose to sacrifice an innocent life to save their own, no matter how severe or imminent the coercion. (a) is wrong because while the threat was imminent and deadly, the homicide bar legally precludes the defense. (b) is wrong because duress is an all-or-nothing excuse, not a mitigating factor for secondary actors in common law murder. (d) is wrong because the availability of alternatives is a standard element of duress, but the homicide bar preempts the defense before alternatives are evaluated. (e) is wrong because accepting a job does not legally forfeit defenses; the homicide bar is the disqualifying rule here.

**Tags:** chapters: [21], topics: [duress, homicide-bar], difficulty: easy, cognitive: recall

**Grounding:** Chapter 21 - Duress Murder Bar

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The facts establish that Blake committed both an omission (failing to call 911) and an affirmative act (locking the door). If the hypothetical murder charge is based on his omission, Blake wouldn't even need an affirmative defense—a core element of omission liability is that one has no legal duty to rescue if doing so puts their own life in peril (like facing a loaded gun). This would negate the *actus reus* entirely.
2. Cross-Doctrine Clashes: The MPC explicitly abandoned the common law categorical bar on duress for murder (allowing it if a person of "reasonable firmness" would have yielded). Since the question stem doesn't explicitly restrict the jurisdiction to the common law, an astute student could argue that the defense *can* be successfully raised under the MPC.
3. Cross-Question Spoilers: pass. (The "regardless of causation" caveat successfully inoculates this question from the fact that Dana's injection is the actual cause of death, protecting the hypothetical).
Recommended fix: Update the stem to explicitly lock in the jurisdiction and the affirmative act: "Assume that, regardless of causation, Blake is charged under the common law with the intentional murder of Chris based on his affirmative act of locking the door. Can Blake successfully raise the defense of duress?"
-->

## Issue 2 — argpass-opus

**Q13.** Assume that, regardless of causation, Blake is charged with the intentional murder of Chris. Can Blake successfully raise the defense of duress?

(a) Yes, because Alex pointing a loaded handgun at Blake's chest constitutes an imminent threat of death that overcomes free will.
(b) Yes, because Blake's role was merely secondary, allowing the court to mitigate his criminal liability based on the coercive circumstances.
(c) No, because the common law categorically bars duress as a defense to intentional homicide regardless of the severity of coercion. <!-- correct -->
(d) No, because Blake could have attempted to disarm Alex or flee the cabin instead of complying with the unlawful order.
(e) No, because accepting financial compensation to act as security legally forfeits the right to claim duress when threatened with violence.

**Answer:** (c)

**Explanation:** (c) is correct because the common law imposes an absolute categorical bar on the use of duress as a defense to intentional homicide. The underlying rationale is that a person may not choose to sacrifice an innocent life to save their own, no matter how severe or imminent the coercion. (a) is wrong because while the threat was imminent and deadly, the homicide bar legally precludes the defense. (b) is wrong because duress is an all-or-nothing excuse, not a mitigating factor for secondary actors in common law murder. (d) is wrong because the availability of alternatives is a standard element of duress, but the homicide bar preempts the defense before alternatives are evaluated. (e) is wrong because accepting a job does not legally forfeit defenses; the homicide bar is the disqualifying rule here.

**Tags:** chapters: [21], topics: [duress, homicide-bar], difficulty: easy, cognitive: recall

**Grounding:** Chapter 21 - Duress Murder Bar

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that Alex pointing a loaded handgun at Blake constitutes a textbook imminent threat of death. Since the threat is severe enough to objectively overcome free will, it seemingly satisfies the fundamental elements of the duress defense. A student relying solely on these general elements might mistakenly conclude that the defense successfully applies here, ignoring specific categorical exceptions to the rule.
(b) Argument-for: A student could argue that modern criminal law often scales liability based on the defendant's degree of participation. If Blake was merely a secondary actor in the murder, a student might reason that the court has the equitable power to mitigate his liability based on the extreme coercion. This makes the option an attractive choice for those conflating complete affirmative defenses with mitigating circumstances.
(c) Argument-for: The common law universally dictates that duress is categorically barred as a defense to intentional homicide. The rationale is that a person may not legally choose to sacrifice an innocent life to save their own, regardless of the severity of the threat faced. Because Blake is explicitly charged with intentional murder, this categorical bar definitively precludes the defense, making this option completely legally sound and correct.
(d) Argument-for: A strict requirement of the duress defense is that the defendant must have had no reasonable opportunity to escape the threatened harm. A student could argue that Blake failed to exhaust his alternatives, such as disarming Alex or fleeing the cabin, thereby forfeiting the defense. This option correctly identifies a standard limitation on duress, making it a plausible reason for the defense's failure if one assumes those facts.
(e) Argument-for: Duress is generally unavailable if the defendant recklessly or willingly placed themselves in a situation where they were likely to be subjected to coercion. A student could argue that by accepting financial compensation to act as security in a dangerous setting, Blake assumed the risk of violence. Therefore, this option plausibly but incorrectly applies the "fault in creating the situation" limitation on the duress defense.

Head-to-head:
Option (c) provides the legally definitive answer because the common law imposes an absolute bar on using duress as a defense to intentional homicide. Distractors (b) and (e) contain explicit, falsifiable legal misstatements (duress acting merely as a mitigating factor, and security work legally forfeiting the defense). However, distractors (a) and (d) lack explicit false legal rules. Option (a) relies on an implicit omission of the homicide bar rather than stating an absolutely false legal proposition, while option (d) relies entirely on a factual assumption about Blake's ability to flee rather than a definitive legal claim. Thus, (a) and (d) fail the strict falsifiability standard.

Falsifiable claim per distractor:
- (a): "Yes, because Alex pointing a loaded handgun at Blake's chest constitutes an imminent threat of death that overcomes free will." — wrong because it relies on an implicit omission (the homicide bar) rather than a stated false legal rule. It lacks an absolute, falsifiable legal claim.
- (b): "allowing the court to mitigate his criminal liability based on the coercive circumstances" — wrong because duress at common law is a complete excuse, not a mitigating factor that reduces an intentional murder charge for a secondary actor.
- (d): "because Blake could have attempted to disarm Alex or flee the cabin" — wrong because it asserts a factual conclusion about Blake's options rather than an explicit, false legal proposition.
- (e): "accepting financial compensation to act as security legally forfeits the right to claim duress" — wrong because accepting lawful employment as security does not legally trigger the "fault in creating the situation" exception to categorically forfeit the duress defense.

Recommended fix: Edit (a) to include an absolute legal claim, e.g., "Yes, because an imminent threat of death automatically excuses any criminal act, including intentional homicide." Edit (d) to assert a false legal rule, e.g., "No, because the duress defense is categorically unavailable unless the defendant first sustains physical injury before complying." (Ensure the broader fact pattern introducing Alex, Chris, the cabin, and the security job is visible to the student).
-->
