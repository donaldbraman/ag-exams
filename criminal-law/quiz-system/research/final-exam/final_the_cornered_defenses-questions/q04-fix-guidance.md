# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — edge-case

**Q4.** Assume Marcus's conduct is completely excused by the defense of duress. Can Dexter claim Marcus's duress defense to shield himself from accomplice liability?

(a) Dexter has no defense because duress is merely an excuse that operates personally for Marcus, rather than a justification that renders the act lawful. <!-- correct -->
(b) Dexter has no defense because accomplice liability under the common law ignores the principal's mental state and focuses only on the helper's actions.
(c) Dexter has a defense because duress is a justification that makes the underlying act legally correct, shielding any knowing accomplices from derivative liability.
(d) Dexter has a defense because an accomplice cannot be convicted if the primary principal offender is acquitted based on any affirmative defense.
(e) Dexter has a defense because the defense of necessity applies automatically to secondary actors whenever the principal faces an imminent threat of death.

**Answer:** (a)

**Explanation:** (a) is correct. The distinction between a justification and an excuse is foundational to derivative liability. A justification (like self-defense) establishes that the act itself was legally correct, shielding any secondary actors who assist. An excuse (like duress or insanity) concedes the act was wrongful but forgives the principal actor due to personal circumstances. Because duress is a personal excuse, the wrongful act remains illegal, and an unexcused accomplice like Dexter can still be convicted. (b) is wrong because accomplice liability requires analyzing both the principal's conduct and the accomplice's mens rea. (c) is wrong because it incorrectly classifies duress as a justification rather than an excuse. (d) is wrong because modern accomplice liability permits the conviction of an accomplice even if the principal is excused or acquitted. (e) is wrong because necessity evaluates a choice of evils, not human coercion, and does not automatically extend to unthreatened secondary actors.

**Tags:** chapters: [18, 21], topics: [accomplice liability, justification vs excuse], difficulty: medium, cognitive: application
**Grounding:** Chapter 21, Justification vs. Excuse framework; Chapter 18, Accomplice Liability

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Dexter's liability as an accomplice is heavily dependent on the mens rea of purpose vs. knowledge (since he is merely a supplier). Stating absolutely that "Dexter has no defense" in Option A ignores that he may have a perfectly valid mens rea defense.
3. Cross-Question Spoilers: Q6 explicitly tests Dexter's purpose vs. knowledge for this exact transaction. Stating "Dexter has no defense" here in Q4 forces a conclusion on his liability that spoils/complicates Q6, potentially confusing students who correctly spot the *Lauria* mens rea issue.
Recommended fix: Change the beginning of the options to directly answer the prompt's Yes/No question. For example, change (a) to "No, because duress is merely an excuse..." and (c) to "Yes, because duress is a justification..."
-->
