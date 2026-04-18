# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q9.** Assume Cole is charged with felony murder for Vic's death, predicated on the attempted robbery. Which of the following provides his strongest legal argument against conviction?

(a) He is not guilty of felony murder because Damon's sudden act of personal rage was not committed in furtherance of the underlying attempted robbery. <!-- correct -->
(b) He is not guilty of felony murder because he was stationed outside the house, defeating the spatial proximity requirement needed to impute the principal's lethal actions.
(c) He is not guilty of felony murder because robbing an illegal drug stash house is not recognized as an inherently dangerous predicate felony under modern statutes.
(d) He is not guilty of felony murder because he lacked the specific intent to cause Vic's death, which is required for all capital-eligible accomplice charges.
(e) He is not guilty of felony murder because Vic's decision to unexpectedly mock an armed invader constitutes an independent intervening act that breaks the chain of causation.

**Answer:** (a)

**Explanation:** (a) is correct because the felony murder rule requires the death to occur "in furtherance" of the predicate felony; Damon shooting Vic in a sudden personal rage without demanding drugs or money gives Cole a strong argument that the killing was an independent act outside the scope of the robbery. (b) is wrong because physical presence in the exact room where the shooting occurs is not required for an accomplice to face felony murder liability. (c) is wrong because robbery and burglary are classic enumerated inherently dangerous felonies, regardless of whether the victim is running an illegal business. (d) is wrong because felony murder acts as a strict liability substitute for mens rea regarding the death; specific intent to kill is not required. (e) is wrong because a victim's verbal resistance is highly foreseeable during a home invasion and does not legally break the chain of proximate causation.

**Tags:** chapters: [14], topics: [felony-murder, in-furtherance], difficulty: medium, cognitive: application

**Grounding:** Chapter 14, felony-murder

<!-- GROUNDING-FAIL: The "in furtherance" requirement (or independent personal act exception) for felony murder is not in any chapter map. The closest taught doctrines are: `brown-remote-outer-fringes` (covering temporal/spatial scope of the felony), `merger-independent-purpose`, and `dependent-vs-independent-intervening-cause` (Ch 8). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q9.** Assume Cole is charged with felony murder for Vic's death, predicated on the attempted robbery. Which of the following provides his strongest legal argument against conviction?

(a) He is not guilty of felony murder because Damon's sudden act of personal rage was not committed in furtherance of the underlying attempted robbery. <!-- correct -->
(b) He is not guilty of felony murder because he was stationed outside the house, defeating the spatial proximity requirement needed to impute the principal's lethal actions.
(c) He is not guilty of felony murder because robbing an illegal drug stash house is not recognized as an inherently dangerous predicate felony under modern statutes.
(d) He is not guilty of felony murder because he lacked the specific intent to cause Vic's death, which is required for all capital-eligible accomplice charges.
(e) He is not guilty of felony murder because Vic's decision to unexpectedly mock an armed invader constitutes an independent intervening act that breaks the chain of causation.

**Answer:** (a)

**Explanation:** (a) is correct because the felony murder rule requires the death to occur "in furtherance" of the predicate felony; Damon shooting Vic in a sudden personal rage without demanding drugs or money gives Cole a strong argument that the killing was an independent act outside the scope of the robbery. (b) is wrong because physical presence in the exact room where the shooting occurs is not required for an accomplice to face felony murder liability. (c) is wrong because robbery and burglary are classic enumerated inherently dangerous felonies, regardless of whether the victim is running an illegal business. (d) is wrong because felony murder acts as a strict liability substitute for mens rea regarding the death; specific intent to kill is not required. (e) is wrong because a victim's verbal resistance is highly foreseeable during a home invasion and does not legally break the chain of proximate causation.

**Tags:** chapters: [14], topics: [felony-murder, in-furtherance], difficulty: medium, cognitive: application

**Grounding:** Chapter 14, felony-murder

<!-- audit: MUST FIX
<check 1>: pass
<check 2>: pass
<check 3>: pass
<check 4>: fails. The question stem is completely missing the underlying fact pattern. It refers to Cole, Damon, Vic, Cole being "stationed outside," Damon's "sudden act of personal rage," and Vic "mocking an armed invader," but none of these facts are actually provided in the stem. Students have nothing to base their analysis on.
<check 5>: fails. Felony murder limitations (e.g., agency vs. proximate cause, "in furtherance" requirements) vary widely by jurisdiction. The stem fails to stipulate the jurisdictional rules being applied, violating the pedagogical principle.
<check 6>: pass
<check 7>: fails. The "in furtherance" doctrine does not appear in the Chapter 14 Refinement tags. The closest mapped concepts for felony murder boundaries are `brown-remote-outer-fringes` (temporal/spatial res gestae limits) and `smith-proximate-cause-police`.
<check 8>: pass
Recommended fix: Insert the omitted fact pattern into the stem so students know what happened. Provide the relevant jurisdictional felony murder rule in the stem, and ensure the correct answer targets an explicitly taught doctrine (like the res gestae boundaries from `brown-remote-outer-fringes`) rather than relying on unmapped limits.
-->
