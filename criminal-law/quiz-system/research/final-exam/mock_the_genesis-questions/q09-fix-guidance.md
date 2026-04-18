# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** Assume the defense challenges the use of the felony murder doctrine by arguing that the drug manufacturing felony merges with the homicide. How will the court rule on the merger issue?

(a) The felony does not merge because manufacturing Blue-X is driven by an independent felonious purpose that is entirely distinct from causing physical injury to the victim. <!-- correct -->
(b) The felony merges because the chemical manufacturing process directly resulted in the victim's death, making it the primary factual cause of the ultimate homicide.
(c) The felony does not merge because all illicit drug manufacturing offenses are automatically classified as malum in se rather than malum prohibitum.
(d) The felony merges because the laboratory explosion and the fatal injury occurred simultaneously within the exact same physical and temporal space.
(e) The felony does not merge because Albert utilized highly reactive and volatile chemicals rather than a traditional deadly weapon to inadvertently cause the death.

**Answer:** (a)

**Explanation:** (a) is correct. Under the merger doctrine, a felony does not merge into the homicide if it has an independent felonious purpose. Manufacturing illicit drugs is distinct from an assaultive purpose, so it serves as a valid, independent felony-murder predicate. (b) is wrong because factual causation does not dictate merger; the legal purpose of the underlying felony does. (c) is wrong because the malum in se classification is not the legal test for merger. (d) is wrong because the physical or temporal proximity of the events does not determine whether the underlying felony merges. (e) is wrong because the type of instrument used (chemicals vs. weapons) does not legally govern the independent purpose requirement.

**Tags:** chapters: [14], topics: [felony murder, merger doctrine], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14, Merger Doctrine / Independent Felonious Purpose

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: fails completely (The stem is missing the entire fact pattern. It references a "drug manufacturing felony," and the options mention "Albert," "Blue-X," and a "laboratory explosion" that are nowhere in the prompt. This appears to have been severed from a multi-question scenario.)
Check 5: pass
Check 6: pass
Check 7: pass (Aligned with `merger-independent-purpose` in Chapter 14)
Check 8: pass
Recommended fix: Restore the missing fact pattern in the stem describing Albert, his manufacturing of the drug Blue-X, and the laboratory explosion that caused the fatal injury.
-->

## Issue 2 — argpass-opus

**Q9.** Assume the defense challenges the use of the felony murder doctrine by arguing that the drug manufacturing felony merges with the homicide. How will the court rule on the merger issue?

(a) The felony does not merge because manufacturing Blue-X is driven by an independent felonious purpose that is entirely distinct from causing physical injury to the victim. <!-- correct -->
(b) The felony merges because the chemical manufacturing process directly resulted in the victim's death, making it the primary factual cause of the ultimate homicide.
(c) The felony does not merge because all illicit drug manufacturing offenses are automatically classified as malum in se rather than malum prohibitum.
(d) The felony merges because the laboratory explosion and the fatal injury occurred simultaneously within the exact same physical and temporal space.
(e) The felony does not merge because Albert utilized highly reactive and volatile chemicals rather than a traditional deadly weapon to inadvertently cause the death.

**Answer:** (a)

**Explanation:** (a) is correct. Under the merger doctrine, a felony does not merge into the homicide if it has an independent felonious purpose. Manufacturing illicit drugs is distinct from an assaultive purpose, so it serves as a valid, independent felony-murder predicate. (b) is wrong because factual causation does not dictate merger; the legal purpose of the underlying felony does. (c) is wrong because the malum in se classification is not the legal test for merger. (d) is wrong because the physical or temporal proximity of the events does not determine whether the underlying felony merges. (e) is wrong because the type of instrument used (chemicals vs. weapons) does not legally govern the independent purpose requirement.

**Tags:** chapters: [14], topics: [felony murder, merger doctrine], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14, Merger Doctrine / Independent Felonious Purpose

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the independent felonious purpose test (e.g., the *Ireland/Burton* doctrine), a felony does not merge if the defendant had a purpose independent of committing an assault or causing physical injury. Here, drug manufacturing is a property, financial, or public health crime, entirely independent of harming the victim. Thus, the doctrine prevents the felony from being swallowed by the homicide.
(b) Argument-for: A student might argue that for a felony to avoid merging, its physical acts must be severable from the acts that ultimately caused death. Because the manufacturing process was the direct, primary factual cause of the death, a student could mistakenly conclude the acts are too intertwined to be separated, dictating merger under a strict act-based identity test.
(c) Argument-for: Students often confuse the requirement that a felony murder predicate be "inherently dangerous" with the concept of malum in se. If a student believes that all malum in se offenses are universally exempt from the merger doctrine due to their inherent moral wrongfulness, they would confidently select this option.
(d) Argument-for: Under the res gestae requirement, the felony and the homicide must be continuous in time and space. A student might invert this doctrine, arguing that complete temporal and physical simultaneity means the acts are legally indivisible, thus forcing a merger. 
(e) Argument-for: Because the merger doctrine was historically developed to limit felony murder in cases of felonious assaults (often involving deadly weapons), a student might reason that the use of highly volatile chemicals—which lacks the directed assaultive intent of a traditional deadly weapon—categorically exempts the manufacturing offense from merger.

Head-to-head: Option (a) correctly applies the standard independent felonious purpose test to correctly conclude that drug manufacturing does not merge. Distractor (c) is firmly locked with the absolute phrasing "automatically classified." However, distractors (b), (d), and (e) rely on "because" to state their false legal rules (factual causation, temporal simultaneity, and weapon type). While they are clearly asserting incorrect legal standards for the merger doctrine, explicitly locking them with "solely because" would ensure they definitively fail the close-call standard by removing any wiggle room for a student to argue that these factors could be part of a broader totality-of-the-circumstances test.

Falsifiable claim per distractor:
- (b): "making it the primary factual cause" — wrong because factual causation is a basic requirement for any felony murder charge; it is not the legal mechanism that triggers the merger doctrine.
- (c): "automatically classified as malum in se" — wrong because malum in se classification is not the legal test for determining if a felony merges, nor does it automatically resolve the independent purpose inquiry.
- (d): "because the laboratory explosion and the fatal injury occurred simultaneously" — wrong because temporal and physical simultaneity fulfills the res gestae requirement but does not legally force a felony to merge.
- (e): "because Albert utilized highly reactive and volatile chemicals rather than a traditional deadly weapon" — wrong because the choice of instrumentality does not legally dictate whether the underlying felony merges into the homicide.

Recommended fix: Change "because" to "solely because" in distractors (b), (d), and (e) to perfectly lock the falsifiable propositions. For example, in (b): "The felony merges solely because the chemical manufacturing process..."
-->
