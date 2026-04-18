# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** The state charges Sal with the attempted murder of Officer Brady based on the shootout. Sal argues that he cannot be convicted because he believed he was firing at a hitman and therefore acted in self-defense. Which of the following is the most accurate analysis of his liability?

(a) Guilty, because Sal had the specific intent to kill the person he fired at, and his belief that the plainclothes officer was a hitman was objectively unreasonable. <!-- correct -->
(b) Guilty, because an individual who fires a weapon at a law enforcement officer is strictly liable for attempted murder regardless of their subjective beliefs.
(c) Not guilty, because Sal lacked the specific intent to kill a police officer, which is a required element of the attempted murder charge.
(d) Not guilty, because Sal subjectively believed his life was in danger, which automatically satisfies the requirements for a complete self-defense justification.
(e) Not guilty, because the officer was driving an unmarked car, legally negating the mens rea required for any assault or attempted homicide offense.

**Answer:** (a)

**Explanation:** Attempted murder requires the specific intent (purpose) to kill, which Sal possessed when he intentionally fired at the person he believed was a hitman. However, his self-defense claim fails because a plainclothes officer conducting a routine traffic stop does not objectively present an imminent threat of unlawful deadly force, rendering Sal's belief unreasonable. (b) is wrong because there is no strict liability for attempted murder; specific intent is always required. (c) is incorrect because the specific intent to kill a *human being* is sufficient; intent to kill a *police officer* specifically is not required unless charged under a specialized statute. (d) fails because self-defense requires the belief to be objectively reasonable, not just subjectively held. (e) is wrong because the officer's unmarked car does not legally negate the specific intent to kill.

**Tags:** chapters: [17, 22], topics: [attempt-mens-rea, self-defense], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 (Attempts) and Chapter 22 (Self-Defense)

<!-- audit: MUST FIX
check 1: Fails. Option (a) asserts Sal's belief was "objectively unreasonable," which cannot be evaluated without the missing facts. Furthermore, if his belief was genuine but unreasonable, the doctrine of imperfect self-defense (Ch 22) could mitigate attempted murder to attempted voluntary manslaughter in many jurisdictions, making a flat "Guilty" for attempted murder inaccurate.
check 2: pass (While the correct answer is flawed, the distractors all contain explicit misstatements of law, so a student could not affirmatively prove a distractor is correct).
check 3: Fails. The explanation references "a plainclothes officer conducting a routine traffic stop," but these facts are completely absent from the question stem.
check 4: Fails. The stem abruptly begins "based on the shootout" and lacks any of the factual setup required to analyze the reasonableness of Sal's belief or the circumstances of the encounter. It is visibly orphaned from a larger scenario.
check 5: Fails. The question does not establish the jurisdiction's stance on imperfect self-defense, which is critical when analyzing an unreasonable but honest belief in a homicide/attempted homicide context.
check 6: pass
check 7: pass
Recommended fix: Restore the missing fact pattern to the stem (describing the unmarked car, plainclothes officer, and traffic stop). To resolve the imperfect self-defense ambiguity, either specify a jurisdiction that does not recognize it, alter the facts to indicate Sal's belief was purely a post-hoc fabrication (so he lacked even a subjective belief), or change the charge to a non-homicide offense like aggravated assault where imperfect self-defense mitigation does not apply.
-->

## Issue 2 — edge-case

**Q6.** The state charges Sal with the attempted murder of Officer Brady based on the shootout. Sal argues that he cannot be convicted because he believed he was firing at a hitman and therefore acted in self-defense. Which of the following is the most accurate analysis of his liability?

(a) Guilty, because Sal had the specific intent to kill the person he fired at, and his belief that the plainclothes officer was a hitman was objectively unreasonable. <!-- correct -->
(b) Guilty, because an individual who fires a weapon at a law enforcement officer is strictly liable for attempted murder regardless of their subjective beliefs.
(c) Not guilty, because Sal lacked the specific intent to kill a police officer, which is a required element of the attempted murder charge.
(d) Not guilty, because Sal subjectively believed his life was in danger, which automatically satisfies the requirements for a complete self-defense justification.
(e) Not guilty, because the officer was driving an unmarked car, legally negating the mens rea required for any assault or attempted homicide offense.

**Answer:** (a)

**Explanation:** Attempted murder requires the specific intent (purpose) to kill, which Sal possessed when he intentionally fired at the person he believed was a hitman. However, his self-defense claim fails because a plainclothes officer conducting a routine traffic stop does not objectively present an imminent threat of unlawful deadly force, rendering Sal's belief unreasonable. (b) is wrong because there is no strict liability for attempted murder; specific intent is always required. (c) is incorrect because the specific intent to kill a *human being* is sufficient; intent to kill a *police officer* specifically is not required unless charged under a specialized statute. (d) fails because self-defense requires the belief to be objectively reasonable, not just subjectively held. (e) is wrong because the officer's unmarked car does not legally negate the specific intent to kill.

**Tags:** chapters: [17, 22], topics: [attempt-mens-rea, self-defense], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 (Attempts) and Chapter 22 (Self-Defense)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The facts state the officer was in an unmarked car and plainclothes. Given Sal is a cartel courier moving $5M of drugs who just received a death threat, a jury might easily find that his belief he was being ambushed by a hitman was *objectively reasonable*. Option (A) and the explanation presume it is automatically unreasonable as a matter of law, which is factually debatable.
2. Cross-Doctrine Clashes: Imperfect Self-Defense. The prompt stipulates that Sal subjectively "believed he was firing at a hitman and therefore acted in self-defense." In most jurisdictions, an actual but unreasonable belief in the need for self-defense (Imperfect Self-Defense) negates malice, mitigating murder to voluntary manslaughter. Therefore, Sal would be guilty of Attempted Voluntary Manslaughter, NOT Attempted Murder, making Option (A) technically incorrect. 
3. Cross-Question Spoilers: pass
Recommended fix: Add to the prompt: "Assume this jurisdiction does not recognize imperfect self-defense." Additionally, update the Q stem to firmly establish the objective unreasonableness of Sal's belief (e.g., "even though the officer had activated red-and-blue police lights and was visibly wearing a police badge").
-->
