# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Silas is charged with first-degree murder for shooting Dexter after Dexter lunged at him with a machete. Which of the following provides the most viable pathways for the prosecution to establish the requisite mental state for murder?

(a) The prosecution must prove that Silas acted with premeditation and deliberation, because the felony murder rule does not apply when the victim initiates the physical confrontation to protect their own property.
(b) The prosecution can prove that Silas formed a premeditated intent during his conversation with Marcus, or use the felony murder rule to substitute his robbery intent for malice aforethought. <!-- correct -->
(c) The prosecution can only use the felony murder rule, because the suddenness of Dexter's machete attack legally negates any prior premeditation Silas may have formed before entering the stash house.
(d) The prosecution must rely exclusively on the natural and probable consequences doctrine because the underlying crime of robbery is an inherently dangerous felony that cannot support a direct murder charge.
(e) The prosecution will fail under both theories because Silas's split-second decision to shoot was a reflex response to a deadly threat, preventing the formation of malice or a culpable mental state.

**Answer:** (b)

**Explanation:** The correct answer is (b). The prosecution can pursue a premeditation theory based on Silas's prior agreement to "eliminate them," or it can rely on the felony murder rule, which substitutes the intent to commit the underlying robbery for malice aforethought. (a) is wrong because the victim's defensive use of force does not block the application of the felony murder rule to the initial aggressor. (c) is wrong because premeditation formed prior to the attack is not negated by the victim's defensive actions. (d) is wrong because Silas is the principal, not an accomplice, so NPC is irrelevant to his direct liability. (e) is wrong because Silas already formed intent and triggered the confrontation himself.

**Tags:** chapters: [12, 14], topics: [homicide, premeditation, felony murder], difficulty: medium, cognitive: application

**Grounding:** Chapter 12: four-elements-common-law; Chapter 14: strict-liability-substitution

<!-- audit: MUST FIX
check 1: pass (assuming the missing facts support it)
check 2: pass (conditional on missing facts)
check 3: pass
check 4: MUST FIX. The question stem is completely missing the underlying fact pattern. The options and explanation refer to a "conversation with Marcus," an underlying "robbery," a "stash house," and a prior agreement to "eliminate them," none of which are provided in the prompt. This is a detached vignette question.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Insert the missing factual scenario into the question stem (detailing Silas and Marcus planning the robbery at the stash house, their agreement, and the confrontation) so students have the facts necessary to evaluate the options.
-->
