# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Assume instead that Cole is prosecuted in California under the reformed standards established by SB 1437. How does the reformed law affect Cole's liability for Vic's murder?

(a) Cole is guilty of murder because SB 1437 retains the traditional Natural and Probable Consequences doctrine for all violent felonies.
(b) Cole is guilty of murder because acting as a lookout automatically satisfies the requirement for personal malice aforethought.
(c) Cole is not guilty of murder because SB 1437 eliminated murder liability based solely on participation in a target crime without proof of personal malice or major participation. <!-- correct -->
(d) Cole is not guilty of murder because SB 1437 established a categorical exemption for any accomplice who is not physically present in the room where the death occurs.
(e) Cole is not guilty of murder because SB 1437 requires the prosecution to prove that the accomplice actually fired the fatal shot to establish the required malice.

**Answer:** (c)

**Explanation:** California's SB 1437 abolished the Natural and Probable Consequences doctrine for murder. Under the reform, malice cannot be imputed solely based on participation in a target crime; the accomplice must personally harbor malice, or be a major participant in a felony who acts with reckless indifference to human life. (a) is wrong because SB 1437 abolished NPC for murder. (b) is wrong because being a lookout does not automatically prove personal malice. (d) is wrong because physical presence in the specific room is not the test; a major participant outside could still theoretically be liable. (e) is wrong because accomplices can still be convicted of murder if they are major participants acting with reckless indifference, even if they do not pull the trigger.

**Tags:** chapters: [18], topics: [accomplice, npc, sb1437], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (Accomplice Liability), npc-reform-sb1437

<!-- audit: MUST FIX
check 1: pass (the legal rule stated in (c) accurately reflects SB 1437, though its conclusion regarding Cole is unverifiable without facts)
check 2: pass
check 3: pass
check 4: FAIL. The stem ("Assume instead that Cole...") clearly relies on a missing, orphaned fact pattern. We don't know who Cole or Vic are, what Cole actually did, or whether Cole's actions might inadvertently meet the "major participant / reckless indifference" standard (which would make the "Cole is not guilty" conclusion in (c) factually incorrect). Option (b) implies Cole was a lookout, but we have no facts to confirm this.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Provide the missing fact pattern in the stem (e.g., "Cole agreed to act as an unarmed lookout while his friend robbed a convenience store. During the robbery, the friend unexpectedly shot and killed Vic. Cole had no idea his friend was armed. Cole is prosecuted in California...").
-->
