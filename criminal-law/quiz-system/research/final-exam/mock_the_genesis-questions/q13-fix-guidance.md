# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q13.** Assume Benny is charged with homicide for killing Slash and raises a claim of self-defense. Based on the jurisdiction's stated rules, will Benny's self-defense claim succeed?

(a) Benny's self-defense claim fails because he did not attempt to exit through the available ground-floor window, violating the jurisdiction's statutory duty to retreat. <!-- correct -->
(b) Benny's self-defense claim fails because a rival drug dealer's threat of violence is never legally considered objectively reasonable under any circumstances.
(c) Invalid defense because Benny panicked and failed to utilize the open back door, violating his statutory duty to retreat before employing lethal force.
(d) Benny's self-defense claim succeeds because Slash's machete attack constituted a sudden escalation that automatically waives the mandatory retreat requirement.
(e) Benny's self-defense claim succeeds because he was actively defending valuable commercial inventory, which inherently justifies the immediate use of lethal force.

**Answer:** (a)

**Explanation:**
* In a duty-to-retreat jurisdiction, a defendant cannot use deadly force if they know they can avoid the necessity of using such force with complete safety by retreating. Because a completely safe escape route existed via the open back door (Fact 15), Benny's panic-driven choice to shoot rather than exit precludes his self-defense claim. (a) fails because the Castle Doctrine generally applies to one's own home, and Benny did not live at the stash house. (b) fails because while he faced an imminent threat, the statutory duty to retreat must still be satisfied if a safe escape route is available. (d) fails because being engaged in a crime does not categorically strip a person of the right to self-defense against a lethal attack, though it may trigger initial aggressor issues. (e) fails because a machete is a deadly weapon, making a handgun a proportional response to a lethal threat.

**Tags:** chapters: [22], topics: [self-defense, duty to retreat], difficulty: medium, cognitive: application

**Grounding:** Chapter 22, Duty to Retreat

<!-- audit: MUST FIX
<check 1>: pass (the legal rule applied in the explanation is accurate for duty to retreat jurisdictions)
<check 2>: pass (distractors are theoretically plausible, but impossible to evaluate accurately without facts)
<check 3>: pass (explanation matches Ch 22 doctrine)
<check 4>: MUST FIX. The stem is entirely missing the fact pattern! It mentions Benny and Slash, but omits all substantive facts necessary to answer the question, such as the machete attack, the stash house, the open ground-floor window, and Benny's failure to use it.
<check 5>: MUST FIX. The stem says "Based on the jurisdiction's stated rules..." but completely fails to state those rules (i.e., that it is a duty-to-retreat jurisdiction).
<check 6>: pass
<check 7>: pass (Duty to retreat and castle doctrine scope are covered in Ch 22)
<check 8>: pass (lengths are roughly symmetrical)
Recommended fix: Rewrite the stem to actually include the fact pattern. Detail Benny's presence in the stash house, Slash's machete attack, the open ground-floor window, and explicitly state that the jurisdiction has a statutory duty to retreat.
-->

## Issue 2 — edge-case

**Q13.** Assume Benny is charged with homicide for killing Slash and raises a claim of self-defense. Based on the jurisdiction's stated rules, will Benny's self-defense claim succeed?

(a) Benny's self-defense claim fails because he did not attempt to exit through the available ground-floor window, violating the jurisdiction's statutory duty to retreat. <!-- correct -->
(b) Benny's self-defense claim fails because a rival drug dealer's threat of violence is never legally considered objectively reasonable under any circumstances.
(c) Invalid defense because Benny panicked and failed to utilize the open back door, violating his statutory duty to retreat before employing lethal force.
(d) Benny's self-defense claim succeeds because Slash's machete attack constituted a sudden escalation that automatically waives the mandatory retreat requirement.
(e) Benny's self-defense claim succeeds because he was actively defending valuable commercial inventory, which inherently justifies the immediate use of lethal force.

**Answer:** (a)

**Explanation:**
* In a duty-to-retreat jurisdiction, a defendant cannot use deadly force if they know they can avoid the necessity of using such force with complete safety by retreating. Because a completely safe escape route existed via the open back door (Fact 15), Benny's panic-driven choice to shoot rather than exit precludes his self-defense claim. (a) fails because the Castle Doctrine generally applies to one's own home, and Benny did not live at the stash house. (b) fails because while he faced an imminent threat, the statutory duty to retreat must still be satisfied if a safe escape route is available. (d) fails because being engaged in a crime does not categorically strip a person of the right to self-defense against a lethal attack, though it may trigger initial aggressor issues. (e) fails because a machete is a deadly weapon, making a handgun a proportional response to a lethal threat.

**Tags:** chapters: [22], topics: [self-defense, duty to retreat], difficulty: medium, cognitive: application

**Grounding:** Chapter 22, Duty to Retreat

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The facts state that Slash "cornered" Benny with a machete. The duty to retreat generally only applies if the defendant knows they can retreat in *complete safety*. A sharp student could successfully argue that turning one's back on an armed attacker who has already "cornered" you to climb out a window does not objectively constitute a "safe retreat," making option (a)'s factual premise debatable.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Modify the fact pattern or option (a) to explicitly stipulate safety, e.g., "The room had an open, ground-floor window immediately behind Benny, through which Benny knew he could easily and safely escape." Or remove the word "cornered" from the scenario.
-->
