# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

## The Question

### Stem 2: The Stash House Raid

*While the sting was unfolding, the rest of the ring hit the East Side stash house, and it went sideways. We have a dead body. I need you to evaluate the homicide liability for both the shooter and the lookout. Focus on whether the shooter's personal reaction changes the underlying felony, and whether the lookout can be held liable for the murder under different complicity theories.*

---

**Q5.** Assume Cole is charged as an accomplice to armed robbery under the federal *Rosemond* standard. Does Cole possess the requisite mental state regarding the weapon?

(a) Yes, because Cole acquired advance knowledge that a firearm would be used while he still had a meaningful opportunity to walk away before taking his post as the lookout. <!-- correct -->
(b) Yes, because Cole was physically present during the preparation phase and his mere presence automatically satisfies the specific intent required for an accomplice to an armed offense.
(c) No, because Cole expressed surprise when the weapon was revealed, which definitively proves he lacked the specific intent required to commit the underlying crime of armed robbery.
(d) No, because Damon explicitly stated the gun was "just for show," negating any inference that Cole shared Damon's true criminal purpose to utilize the weapon forcefully.
(e) Yes, because under the natural and probable consequences doctrine, any use of a weapon during a stash house raid is strictly foreseeable regardless of Cole's actual prior knowledge.

**Answer:** (a)

**Explanation:** (a) is correct because under *Rosemond*, accomplice liability for an armed offense requires advance knowledge of the weapon at a time when the defendant still has a meaningful opportunity to withdraw; Cole saw the gun while in the car and still chose to take his post. (b) is wrong because mere presence is never sufficient for accomplice liability; purposive participation and advance knowledge are required. (c) is wrong because despite his initial surprise, Cole elected to continue participating after acquiring the knowledge, satisfying the temporal requirement. (d) is wrong because using a gun "for show" to intimidate victims during a robbery is still utilizing it to commit an armed offense, and Cole chose to proceed. (e) is wrong because the *Rosemond* standard tests direct accomplice liability through advance knowledge, not the separate foreseeability-based natural and probable consequences doctrine.

**Tags:** chapters: [18], topics: [accomplice, mens-rea, rosemond], difficulty: medium, cognitive: application

**Grounding:** Chapter 18, mr-temporal-advance-knowledge

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fail (The stem completely lacks the facts needed to answer. It never introduces Cole or Damon, never mentions a car, and never establishes when Cole saw the gun or whether he had a meaningful opportunity to walk away. The explanation and distractors rely on phantom facts—e.g., Damon saying the gun was "just for show" and Cole seeing the gun in the car—that do not exist in the prompt.)
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Provide the actual factual narrative in the stem. Detail the interaction between Cole and Damon in the car, Damon showing the gun, Damon's "just for show" comment, and Cole subsequently taking his post as the lookout, so students can actually apply the *Rosemond* test to the facts.
-->
