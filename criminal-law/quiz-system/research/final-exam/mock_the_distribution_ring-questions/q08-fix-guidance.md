# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q8.** Assume the jurisdiction has adopted California's SB 1437 reform regarding accomplice liability for murder. How does this reform affect Cole's potential liability for Vic's death?

(a) Cole cannot be convicted of murder under the NPC doctrine unless the prosecution proves he personally acted with malice or was a major participant acting with reckless indifference to life. <!-- correct -->
(b) Cole is categorically immune from any murder liability because the reform completely abolished all forms of accomplice liability for homicides committed by a separate principal actor.
(c) Cole remains fully liable for first-degree murder because the reform explicitly preserved the traditional NPC doctrine for any crimes involving the use or display of a loaded firearm.
(d) Cole cannot be convicted of murder because his role as a lookout mathematically precludes him from meeting the required standard of possessing the specific intent to kill the victim.
(e) Cole is strictly liable for manslaughter rather than murder, because the reform downgraded all foreseeable accomplice homicides to a lesser degree to reduce racial disparities in sentencing.

**Answer:** (a)

**Explanation:** (a) is correct because SB 1437 eliminated murder liability under the NPC doctrine, requiring instead that the prosecution prove personal malice or that the accomplice was a major participant in the underlying felony who acted with reckless indifference to human life. (b) is wrong because SB 1437 did not completely abolish accomplice liability for murder; it simply removed the NPC pathway. (c) is wrong because the reform applies to all felonies, including armed offenses; there is no carve-out preserving NPC for gun crimes. (d) is wrong because a lookout *can* be a major participant acting with reckless indifference (e.g., if they knew about the gun and the violence risk), so liability is not mathematically precluded, nor is specific intent to kill strictly required. (e) is wrong because the reform did not automatically downgrade NPC murders to strict liability manslaughter; it required elevated proof for murder.

**Tags:** chapters: [18], topics: [accomplice, npc-reform, sb1437], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 18, npc-reform-sb1437

<!-- audit: MUST FIX
check 1: Fails. Option (a) incorrectly implies that a defendant CAN be convicted of murder *under the NPC doctrine* as long as they have personal malice or are a major participant (due to the "unless" phrasing). Under SB 1437, the NPC doctrine is entirely abolished for murder. If the prosecution proves personal malice, the conviction is for direct aiding and abetting; if they prove major participant with reckless indifference, it is for felony murder. A well-prepared student would rightfully eliminate (a) because NPC is dead for murder, period.
check 2: pass
check 3: Fails. The explanation correctly notes that "SB 1437 eliminated murder liability under the NPC doctrine," which directly contradicts the wording of option (a) ("cannot be convicted... under the NPC doctrine unless...").
check 4: Fails entirely. The stem asks about "Cole's potential liability for Vic's death" and the options mention his "role as a lookout," but the stem contains absolutely zero facts about Cole, Vic, or the underlying crime. This question appears to have been orphaned from a common fact pattern.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: First, supply the missing fact pattern in the stem. Second, rewrite option (a) so it doesn't imply NPC survives (e.g., "Cole cannot be convicted of murder under the NPC doctrine; instead, the prosecution must prove he personally acted with malice or was a major participant acting with reckless indifference to life.").
-->

## Issue 2 — edge-case

**Q8.** Assume the jurisdiction has adopted California's SB 1437 reform regarding accomplice liability for murder. How does this reform affect Cole's potential liability for Vic's death?

(a) Cole cannot be convicted of murder under the NPC doctrine unless the prosecution proves he personally acted with malice or was a major participant acting with reckless indifference to life. <!-- correct -->
(b) Cole is categorically immune from any murder liability because the reform completely abolished all forms of accomplice liability for homicides committed by a separate principal actor.
(c) Cole remains fully liable for first-degree murder because the reform explicitly preserved the traditional NPC doctrine for any crimes involving the use or display of a loaded firearm.
(d) Cole cannot be convicted of murder because his role as a lookout mathematically precludes him from meeting the required standard of possessing the specific intent to kill the victim.
(e) Cole is strictly liable for manslaughter rather than murder, because the reform downgraded all foreseeable accomplice homicides to a lesser degree to reduce racial disparities in sentencing.

**Answer:** (a)

**Explanation:** (a) is correct because SB 1437 eliminated murder liability under the NPC doctrine, requiring instead that the prosecution prove personal malice or that the accomplice was a major participant in the underlying felony who acted with reckless indifference to human life. (b) is wrong because SB 1437 did not completely abolish accomplice liability for murder; it simply removed the NPC pathway. (c) is wrong because the reform applies to all felonies, including armed offenses; there is no carve-out preserving NPC for gun crimes. (d) is wrong because a lookout *can* be a major participant acting with reckless indifference (e.g., if they knew about the gun and the violence risk), so liability is not mathematically precluded, nor is specific intent to kill strictly required. (e) is wrong because the reform did not automatically downgrade NPC murders to strict liability manslaughter; it required elevated proof for murder.

**Tags:** chapters: [18], topics: [accomplice, npc-reform, sb1437], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 18, npc-reform-sb1437

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The phrasing in option (a) "convicted of murder under the NPC doctrine unless" creates a technical logical paradox. SB 1437 completely abolished the NPC doctrine for murder. If the prosecution proves personal malice, the conviction is for direct aiding and abetting, not NPC. If they prove major participant/reckless indifference, the conviction is for Felony Murder, not NPC. Therefore, stating he can be convicted "under the NPC doctrine" if those elements are proven is technically false.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change option (a) to: "Cole cannot be convicted of murder as an accomplice unless the prosecution proves he personally acted with malice or was a major participant acting with reckless indifference to life." Modify the first sentence of the explanation to match.
-->
