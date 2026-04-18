# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Are the elements of constructive possession satisfied for Thorne regarding the AR-15 found in the employee breakroom locker?

(a) No, because although Thorne had the power to access the locker via the master key, his refusal to handle the weapon indicates he lacked the intent to exercise dominion. <!-- correct -->
(b) Yes, because possessing the sole master key establishes exclusive physical control, which automatically satisfies all elements of constructive possession regardless of Thorne's intent.
(c) Yes, because Thorne made an incriminating statement acknowledging the rifle's exact location, which legally equates to dominion and control under modern federal standards.
(d) No, because the locker was situated fifty feet away from Thorne's desk, meaning he lacked the necessary geographic proximity to establish constructive possession.
(e) No, because the rifle legally belonged to Locke, and property ownership absolutely precludes anyone else from constructively possessing the item.

**Answer:** (a)

**Explanation:** Constructive possession requires three elements: awareness of the contraband, the power to exercise dominion and control, and the intent to exercise dominion and control. Thorne had awareness and power (the only key), but his statement "I refuse to touch it" evidences a lack of intent to exercise dominion over the weapon. (b) is wrong because power/access does not automatically establish constructive possession without the corresponding intent to control. (c) is wrong because under cases like *White*, mere awareness (knowing its location) is a necessary but not sufficient condition for constructive possession; it does not equate to dominion. (d) is wrong because strict physical proximity is not the test; dominion and control is the standard regardless of distance. (e) is wrong because multiple people can constructively possess an item owned by someone else.

**Tags:** chapters: [15], topics: [constructive possession, awareness vs. control], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 15 - Constructive Possession Elements and State v. White

<!-- audit: SHOULD FIX
Check 1: pass - The correct answer accurately tracks the doctrine: constructive possession requires both the power and the intent to exercise dominion and control.
Check 2: pass - No distractors are legally defensible; they rely on classic misunderstandings (e.g., that power alone is sufficient, or that mere knowledge equates to control).
Check 3: fail - The explanation improperly cites *State v. White* as a constructive possession case. The meta-map confirms *State v. White* is a Chapter 17 Attempts case (`mens-rea-state-v-white`). The substantive legal rule is correct, but the case citation is a hallucination/cross-chapter contamination.
Check 4: fail - The question stem contains no facts and relies entirely on an assumed master fact pattern. If this question is meant to be a standalone item, it is unanswerable without importing the required facts (Thorne's key, his refusal statement) from the options into the stem.
Check 5: pass - Constructive possession elements are standard; no jurisdictional split needs resolving.
Check 6: pass - No excluded topics are present.
Check 7: fail - Coverage mismatch on the case name. The Grounding and explanation rely on *State v. White*, which is not mapped to Chapter 15. The underlying doctrines (`cp-elements`, `cp-awareness-control`) are properly mapped, but the case attribution is wrong.
Check 8: pass - Length parity is solid across all options.
Recommended fix: Remove the references to *State v. White* in the explanation and Grounding. If this will be deployed as a standalone question (rather than attached to a master fact pattern), integrate the essential facts directly into the question stem.
-->
