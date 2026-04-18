# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q3.** Assume George is charged with attempted murder. Is Felix liable as an accomplice to attempted murder?

(a) Yes, Felix is liable as an accomplice. Because he knowingly provided the murder weapon, he shares full liability for whatever violent actions George ultimately decides to take.
(b) Yes, Felix is liable as an accomplice. His dismissive shrug clearly established that he had the specific purpose of promoting the premeditated murder of a rival lookout.
(c) No, Felix is not liable as an accomplice. His instructions were only to scare the rivals, meaning he lacked the purpose to promote an actual murder when he provided the gun. <!-- correct -->
(d) No, Felix is not liable as an accomplice. He walked away and turned his back before George drove off, which constitutes an effective legal withdrawal from the planned shooting.
(e) Yes, Felix is liable as an accomplice. A crew chief is strictly liable as an accomplice for any violent felonies committed by his subordinate members while on duty.

**Answer:** (c)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the specific offense (*Gladstone*). Because Felix only instructed George to fire into the air to scare the rivals, he lacked the specific purpose to promote an actual murder. (a) is wrong because providing a weapon does not create blanket liability for any subsequent unilateral escalation. (b) is wrong because a dismissive shrug indicates indifference, not the purposive intent required for accomplice liability. (d) is wrong because walking away does not constitute a valid withdrawal once the weapon is provided and the plan is in motion. (e) is wrong because criminal law does not impose strict vicarious liability on crew chiefs outside of specific conspiracy doctrines.

**Tags:** chapters: [18], topics: [accomplice mens rea, purpose], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - Mens Rea: Purpose Requirement (*State v. Gladstone*)

<!-- GROUNDING-FAIL: Accomplice mens rea (purpose requirement) is not in any chapter map. The closest taught doctrines are: None (meta-map artifact is missing from the prompt). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q3.** Assume George is charged with attempted murder. Is Felix liable as an accomplice to attempted murder?

(a) Yes, Felix is liable as an accomplice. Because he knowingly provided the murder weapon, he shares full liability for whatever violent actions George ultimately decides to take.
(b) Yes, Felix is liable as an accomplice. His dismissive shrug clearly established that he had the specific purpose of promoting the premeditated murder of a rival lookout.
(c) No, Felix is not liable as an accomplice. His instructions were only to scare the rivals, meaning he lacked the purpose to promote an actual murder when he provided the gun. <!-- correct -->
(d) No, Felix is not liable as an accomplice. He walked away and turned his back before George drove off, which constitutes an effective legal withdrawal from the planned shooting.
(e) Yes, Felix is liable as an accomplice. A crew chief is strictly liable as an accomplice for any violent felonies committed by his subordinate members while on duty.

**Answer:** (c)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the specific offense (*Gladstone*). Because Felix only instructed George to fire into the air to scare the rivals, he lacked the specific purpose to promote an actual murder. (a) is wrong because providing a weapon does not create blanket liability for any subsequent unilateral escalation. (b) is wrong because a dismissive shrug indicates indifference, not the purposive intent required for accomplice liability. (d) is wrong because walking away does not constitute a valid withdrawal once the weapon is provided and the plan is in motion. (e) is wrong because criminal law does not impose strict vicarious liability on crew chiefs outside of specific conspiracy doctrines.

**Tags:** chapters: [18], topics: [accomplice mens rea, purpose], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - Mens Rea: Purpose Requirement (*State v. Gladstone*)

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: Fail. The stem is entirely missing the fact pattern. It references Felix, George, and a shooting, but critical facts needed to answer the question—such as Felix's instructions to only "scare" the rivals, his shrug, and his provision of the weapon—are only revealed retroactively in the answers and explanation.
Check 5: Fail. The stem fails to specify if the jurisdiction follows the MPC/Gladstone purpose requirement or the Common Law Natural and Probable Consequences (NPC) doctrine. Under NPC, Felix could arguably be liable for attempted murder if it was a reasonably foreseeable consequence of the target offense he *did* intend to facilitate (aggravated assault/scaring the rivals with a gun).
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Insert the missing fact pattern into the stem, and explicitly stipulate that the jurisdiction follows the *Gladstone* rule or the Model Penal Code (requiring purpose) to eliminate common-law NPC as a defensible theory.
-->

## Issue 3 — edge-case

**Q3.** Assume George is charged with attempted murder. Is Felix liable as an accomplice to attempted murder?

(a) Yes, Felix is liable as an accomplice. Because he knowingly provided the murder weapon, he shares full liability for whatever violent actions George ultimately decides to take.
(b) Yes, Felix is liable as an accomplice. His dismissive shrug clearly established that he had the specific purpose of promoting the premeditated murder of a rival lookout.
(c) No, Felix is not liable as an accomplice. His instructions were only to scare the rivals, meaning he lacked the purpose to promote an actual murder when he provided the gun. <!-- correct -->
(d) No, Felix is not liable as an accomplice. He walked away and turned his back before George drove off, which constitutes an effective legal withdrawal from the planned shooting.
(e) Yes, Felix is liable as an accomplice. A crew chief is strictly liable as an accomplice for any violent felonies committed by his subordinate members while on duty.

**Answer:** (c)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the specific offense (*Gladstone*). Because Felix only instructed George to fire into the air to scare the rivals, he lacked the specific purpose to promote an actual murder. (a) is wrong because providing a weapon does not create blanket liability for any subsequent unilateral escalation. (b) is wrong because a dismissive shrug indicates indifference, not the purposive intent required for accomplice liability. (d) is wrong because walking away does not constitute a valid withdrawal once the weapon is provided and the plan is in motion. (e) is wrong because criminal law does not impose strict vicarious liability on crew chiefs outside of specific conspiracy doctrines.

**Tags:** chapters: [18], topics: [accomplice mens rea, purpose], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - Mens Rea: Purpose Requirement (*State v. Gladstone*)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Fact 2 (established for Q2's conspiracy) has Felix telling the crew, "We defend this turf against the rivals by any means necessary." This fact spills over and ruins the isolated "only intended to scare" premise of Q3. Providing a loaded gun, having just declared "by any means necessary," and shrugging at George's explicit murder threat creates a massive factual inference that Felix *did* have the purpose to promote murder. This makes (c)'s definitive conclusion that "he lacked the purpose" highly debatable or factually inaccurate for a sharp student.
Recommended fix: Add a clarifying premise to the question stem, such as: "Assume the jury finds Felix's shrug indicated mere indifference and he strictly only intended to scare the rivals." Alternatively, revise option (c) to be conditional: "No, assuming his shrug indicated mere indifference to George's escalation, he lacked the specific purpose..."
-->
