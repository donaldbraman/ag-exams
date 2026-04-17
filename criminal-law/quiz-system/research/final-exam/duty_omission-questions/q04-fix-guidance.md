# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Assume Evan is charged as an accomplice to Blake's crime of locking the door. Can Evan successfully assert a derivative defense based on Blake's coercion?

(a) Evan cannot claim the defense because duress is an excuse that applies only to the specific coerced individual. <!-- correct -->
(b) Evan can claim the defense because he acted under the same immediate threat that compelled Blake's original action.
(c) Evan can claim the defense because Blake's duress is a justification that legally transfers to any knowing accomplice.
(d) Evan cannot claim the defense because he fled through the window rather than remaining to complete the offense.
(e) Evan cannot claim the defense because justification defenses require an official statutory authorization to use protective physical force.

**Answer:** (a)

**Explanation:** (a) is correct because duress is an excuse, meaning it reflects a lack of moral culpability due to coercion but does not render the underlying act legally "correct" or justified. Because it is a personal excuse, it cannot be derivatively claimed by an accomplice assisting the coerced actor. (b) is wrong because Evan was not threatened by Alex; his general panic does not constitute the specific directed threat required for duress. (c) is wrong because duress is an excuse, not a justification. (d) is wrong because Evan successfully completed the actus reus of aiding the lock before fleeing, meaning the derivative liability attached. (e) is wrong because justification defenses include necessity and self-defense, neither of which require statutory authorization to be raised in criminal proceedings.

**Tags:** chapters: [18, 21], topics: [accomplice-liability, justification-vs-excuse], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 21 - Justification vs. Excuse (The Core Distinction)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: MUST FIX (The explanation relies on facts—"threatened by Alex," "general panic"—that do not appear anywhere in the stem.)
check 4: MUST FIX (The stem is missing the master fact pattern entirely. It refers to "Blake's crime of locking the door," but the options and explanation refer to phantom facts like "Alex," "fled through the window," and Evan's "general panic." This looks like a sub-question that was severed from its narrative.)
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Import the missing narrative into the stem. (e.g., "Assume Alex threatened Blake with a weapon, forcing Blake to lock a door. Evan, in a general panic but not directly threatened by Alex, helped Blake lock the door and then fled through a window. Evan is charged as an accomplice...")
-->

## Issue 2 — argpass-opus

**Q4.** Assume Evan is charged as an accomplice to Blake's crime of locking the door. Can Evan successfully assert a derivative defense based on Blake's coercion?

(a) Evan cannot claim the defense because duress is an excuse that applies only to the specific coerced individual. <!-- correct -->
(b) Evan can claim the defense because he acted under the same immediate threat that compelled Blake's original action.
(c) Evan can claim the defense because Blake's duress is a justification that legally transfers to any knowing accomplice.
(d) Evan cannot claim the defense because he fled through the window rather than remaining to complete the offense.
(e) Evan cannot claim the defense because justification defenses require an official statutory authorization to use protective physical force.

**Answer:** (a)

**Explanation:** (a) is correct because duress is an excuse, meaning it reflects a lack of moral culpability due to coercion but does not render the underlying act legally "correct" or justified. Because it is a personal excuse, it cannot be derivatively claimed by an accomplice assisting the coerced actor. (b) is wrong because Evan was not threatened by Alex; his general panic does not constitute the specific directed threat required for duress. (c) is wrong because duress is an excuse, not a justification. (d) is wrong because Evan successfully completed the actus reus of aiding the lock before fleeing, meaning the derivative liability attached. (e) is wrong because justification defenses include necessity and self-defense, neither of which require statutory authorization to be raised in criminal proceedings.

**Tags:** chapters: [18, 21], topics: [accomplice-liability, justification-vs-excuse], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 21 - Justification vs. Excuse (The Core Distinction)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: This option correctly identifies the fundamental doctrinal distinction between justifications and excuses. Because duress is an excuse, it focuses on the individual's diminished culpability due to coercion, rather than rendering the act legally permissible. Thus, excuse defenses are entirely personal and cannot be derivatively claimed by an accomplice. Evan is liable regardless of Blake's personal excuse.
(b) Argument-for: A student might argue that if a threat is pervasive or immediate enough to coerce the principal, the "zone of danger" applies to the accomplice as well. Under this logic, the underlying rationale for duress—that a reasonable person would yield—would theoretically protect anyone acting within that same coercive environment, justifying a shared or derived defense.
(c) Argument-for: A student could easily misclassify duress as a justification defense, confusing it with necessity (the choice of evils). Under justification doctrine, a justified act is legally correct and socially desirable, meaning the justification transfers to anyone who assists. If Blake's duress were a justification, Evan would legally derive that protection.
(d) Argument-for: A student might apply the rules of abandonment or withdrawal to conclude that fleeing the scene severs Evan's legal connection to the principal's defenses. If the student incorrectly believes that derivative defenses require the accomplice to remain until the crime's completion, Evan's flight through the window would logically preclude him from claiming Blake's defense.
(e) Argument-for: A student might conflate public duty defenses with general justification defenses. Because execution of a public duty requires statutory authorization, the student could mistakenly deduce that all justification defenses (and thus any argument for derivative justification) require official statutory authorization to use physical force.

Head-to-head: Option (a) correctly applies the core black-letter rule that excuses are personal and do not transfer to accomplices, making it cleanly correct. Options (c) and (e) contain explicit, falsifiable legal errors regarding the classification of duress and the requirements for justification defenses. Option (d) presents a false legal condition by claiming that fleeing precludes a defense that would otherwise attach at the moment of assistance. However, option (b) primarily relies on a factual contradiction (the explanation notes Evan was not threatened) rather than an explicitly falsifiable legal claim, making it weaker as a distractor under the strict adversarial standard. 

Falsifiable claim per distractor:
- (b): "he acted under the same immediate threat" — wrong because it relies on a factual mismatch with the unseen prompt rather than an explicit, absolute false legal claim about derivative defenses.
- (c): "Blake's duress is a justification" — wrong because duress is canonically classified as an excuse defense, not a justification.
- (d): "because he fled through the window rather than remaining" — wrong because legally, the right to a derivative defense is not negated by fleeing after the actus reus of aiding has already been completed.
- (e): "justification defenses require an official statutory authorization" — wrong because necessity and self-defense are common justification defenses available to private individuals without official statutory authorization.

Recommended fix: Revise (b) to include an explicitly false legal absolute. For example: "(b) Evan can claim the defense because an accomplice automatically derives any duress defense successfully claimed by the principal."
-->
