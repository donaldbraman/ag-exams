# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Assume the prosecution predicates Damon's felony murder charge on the burglary, defining the burglary as "breaking and entering with the intent to commit a robbery." How does the merger doctrine apply?

(a) The felony murder charge succeeds, because at the moment Damon broke in, he possessed the independent felonious purpose to rob the stash house, meaning the burglary does not merge into the homicide. <!-- correct -->
(b) The felony murder charge fails, because the ultimate result of the break-in was a fatal assault, and the merger doctrine requires all precursor felonies to merge into the final lethal act.
(c) The felony murder charge succeeds, because the merger doctrine only limits the application of lesser-included offenses like manslaughter, and cannot be used to defeat a first-degree felony murder charge.
(d) The felony murder charge fails, because Damon's failure to demand drugs or money proves he abandoned the robbery, transforming the break-in into a pure assault that merges into the homicide.
(e) The felony murder charge succeeds, because kicking in a front door is an inherently dangerous act that categorically satisfies the felony murder rule without any need for an independent purpose analysis.

**Answer:** (a)

**Explanation:** (a) is correct because the merger doctrine asks whether the predicate felony had a purpose independent of the assault that caused death; breaking in with intent to rob provides that independent purpose, preventing the burglary from merging into the homicide. (b) is wrong because the independent purpose test evaluates the defendant's intent at the time the predicate felony is committed (the break-in), not based on the final lethal outcome. (c) is wrong because the entire point of the merger doctrine is to limit the application of the felony murder rule itself. (d) is wrong because abandoning the robbery *after* entry does not retroactively change his intent at the precise moment of the break-in, which establishes the independent purpose. (e) is wrong because even inherently dangerous felonies will merge if they are purely assaultive and lack an independent felonious purpose.

**Tags:** chapters: [14], topics: [felony-murder, merger-doctrine, independent-purpose], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14, merger-independent-purpose

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem relies on facts from a missing overarching fact pattern. It references "Damon," "the stash house," and Damon's "failure to demand drugs or money" (in option d) without actually providing these facts in the question itself.
check 5: fails. The prompt instructions specifically flag the merger doctrine as subject to jurisdictional variation. The stem asks "How does the merger doctrine apply?" without stipulating the applicable rule (e.g., whether the jurisdiction uses the independent felonious purpose test for burglary, or if burglary categorically never merges).
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Integrate the missing facts into the stem (e.g., "Damon breaks into a stash house intending to commit a robbery, but commits a fatal assault without ever demanding drugs or money.") and explicitly stipulate the jurisdictional rule (e.g., "Assume the jurisdiction applies the independent felonious purpose test to the merger doctrine.").
-->
