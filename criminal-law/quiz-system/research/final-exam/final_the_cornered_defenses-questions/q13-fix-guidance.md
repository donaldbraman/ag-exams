# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q13.** Assume Silas is charged with attempted murder for shooting Trey and raises a self-defense claim. How would a jury evaluate the objective reasonableness of Silas's belief that deadly force was necessary?

(a) A jury could find Silas's belief unreasonable because an objective person in his situation might not assume a mere reach into a jacket constitutes an imminent lethal threat. <!-- correct -->
(b) A jury must find Silas's belief reasonable because his prior public vow to eliminate Syndicate members legally justifies an immediate preemptive strike against any perceived enemy.
(c) A jury must find Silas's belief reasonable because Trey was a known syndicate hitman, which automatically satisfies the objective standard for deadly force without further factual inquiry.
(d) A jury could find Silas's belief unreasonable because the common law strictly requires the victim to actually visibly brandish a deadly weapon before self-defense can be legitimately claimed.
(e) A jury could find Silas's belief unreasonable because self-defense doctrine strictly requires the perceived threat to involve multiple attackers coordinating a maneuver rather than a single individual.

**Answer:** (a)

**Explanation:** (a) is correct. Self-defense requires an objectively reasonable belief in an imminent threat of death or serious bodily harm. The jury incorporates the situational context (Trey's status as a hitman), but ultimately must decide if a reasonable person with an unobstructed escape route would conclude that a rapid walk and a reach into a jacket necessitated immediate lethal force. The jury could reasonably find Silas's assumption unreasonable. (b) is wrong because a public vow to kill does not legally create a continuous threat justifying a preemptive strike; in fact, it undermines his claim by suggesting he was an aggressor. (c) is wrong because while the victim's reputation informs the reasonableness inquiry, it never automatically or absolutely satisfies the standard. (d) is wrong because the law permits lethal force based on a reasonable perception of a deadly weapon, not strict actual possession or brandishing. (e) is wrong because self-defense applies equally against single attackers and imposes no multiple-assailant requirement.

**Tags:** chapters: [22], topics: [self-defense, objective reasonableness], difficulty: medium, cognitive: application
**Grounding:** Chapter 22, Objective Reasonableness Standard

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: fail - The explanation introduces facts ("an unobstructed escape route," "a rapid walk") that appear nowhere in the stem or the correct answer text.
check 4: fail - The stem is completely missing the underlying fact pattern. It relies on facts (Trey being a hitman, Silas's public vow, reaching into a jacket) that are only revealed in the answer choices or the explanation. This question appears to have been detached from a master fact pattern.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Integrate the missing facts into the stem. For example: "Silas previously made a public vow to eliminate Syndicate members. Later, Silas encounters Trey, a known Syndicate hitman, walking rapidly toward him. Silas has an unobstructed escape route, but when Trey reaches into his jacket, Silas shoots him. Assume Silas is charged with attempted murder..."
-->
