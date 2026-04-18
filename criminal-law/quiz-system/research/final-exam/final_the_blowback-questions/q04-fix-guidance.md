# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Assume that Penelope is charged with felony murder for Wendy's death based on the predicate felony of grand theft. If the jurisdiction applies California's "abstract elements" approach to the inherently dangerous felony limitation, how should the court rule?

(a) The charge is valid because stealing commercial centrifuges and fleeing the scene creates a concrete, foreseeable risk to human life.
(b) The charge is valid because any felony committed as part of a drug manufacturing conspiracy is categorically deemed inherently dangerous.
(c) The charge is invalid because grand theft can be committed through non-dangerous means like embezzlement, meaning it is not inherently dangerous. <!-- correct -->
(d) The charge is invalid because the merger doctrine prevents an assaultive or property-based felony from serving as a predicate offense.
(e) The charge is invalid because Penelope was not physically driving the vehicle at the exact moment it struck the pedestrian.

**Answer:** (c)

**Explanation:** Under California's abstract elements approach (*People v. Phillips*), a court determines whether a felony is inherently dangerous by looking solely at the statutory definition of the offense, not the defendant's specific conduct. Because grand theft can be committed in ways that do not endanger human life (such as embezzlement or fraud), it fails the abstract test and cannot serve as a predicate for felony murder. (a) is wrong because it applies the facts-as-committed approach used in other states, not California's abstract test. (b) is wrong because there is no categorical rule making all drug-related felonies inherently dangerous. (d) is wrong because the merger doctrine applies to assaultive felonies that lack an independent purpose, whereas theft has an independent purpose. (e) is wrong because the felony murder rule applies to non-driving co-felons during immediate flight.

**Tags:** chapters: [14], topics: [felony murder, inherently dangerous felony, abstract elements approach], difficulty: medium, cognitive: application

**Grounding:** Chapter 14, inherently-dangerous-felony-limitation; California examines the felony's statutory elements in the abstract (People v. Phillips).

<!-- audit: SHOULD FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: The stem is completely missing the underlying fact pattern that distractors (a), (b), and (e) refer to (e.g., stealing commercial centrifuges, drug manufacturing conspiracy, a vehicle striking a pedestrian). Without these facts, the distractors hallucinate information, making the question deeply confusing as a standalone item and allowing a student to guess (c) simply because it is the only option that doesn't rely on unstated facts.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Either provide a brief fact pattern in the stem ("Penelope and Wendy conspired to manufacture drugs, during which Penelope stole commercial centrifuges. While fleeing in a vehicle driven by a co-felon, the car struck and killed a pedestrian. Assume Penelope is charged...") or rewrite the distractors to be purely theoretical/doctrinal without relying on specific facts.
-->
