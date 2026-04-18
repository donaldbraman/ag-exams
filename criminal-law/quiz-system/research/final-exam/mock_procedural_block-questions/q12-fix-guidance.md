# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Sal appeals his conviction, arguing that DA Paula's jury selection tactics violated his constitutional rights. When questioned by the judge during voir dire, Paula claimed she struck the Hispanic jurors for expressing skepticism of police, but the record proved three of them never spoke. Did DA Paula's use of peremptory challenges violate the Equal Protection Clause?

(a) Yes, because the record showing that three jurors never spoke proves that her proffered race-neutral reason was a pretext for intentional discrimination. <!-- correct -->
(b) Yes, because striking all six Hispanic prospective jurors from the venire automatically constitutes a structural error requiring immediate reversal of the conviction.
(c) No, because prosecutors are legally entitled to strike any juror who expresses skepticism of police testimony, regardless of the juror's racial background.
(d) No, because the *Batson* framework solely applies to strikes made by defense attorneys and explicitly exempts prosecutors acting on behalf of the state.
(e) No, because peremptory challenges are entirely discretionary and courts cannot second-guess a prosecutor's stated reasons once a race-neutral justification is formally provided.

**Answer:** (a)

**Explanation:** The *Batson* framework prohibits striking jurors based on race. At step three, the judge must evaluate the prosecutor's race-neutral explanation. Because the record shows three of the Hispanic jurors never spoke, DA Paula's claim that they "expressed skepticism" is factually contradicted, proving the reason was a pretext for intentional discrimination. (b) is wrong because striking multiple jurors of one race is not an automatic structural error; the defendant must still prove discriminatory intent through the three-step framework. (c) is incorrect because while skepticism of police is a valid race-neutral reason, using it as a pretext to hide racial discrimination violates Equal Protection. (d) fails because *Batson* originally and primarily applies to prosecutors. (e) is wrong because courts are required to actively second-guess the prosecutor's stated reasons at step three to determine pretext.

**Tags:** chapters: [4], topics: [batson-framework], difficulty: easy, cognitive: application

**Grounding:** Chapter 4 (The Jury and Nullification) - Batson v. Kentucky

<!-- audit: SHOULD FIX
check 1: pass (a factually contradicted justification from the prosecutor is the textbook method of establishing pretext at Batson Step 3)
check 2: pass
check 3: pass
check 4: finding (Option (b) contains a "ghost fact" by referring to "all six Hispanic prospective jurors," but the stem never specifies how many Hispanic jurors there were total, only that "three of them never spoke." This could distract a careful student.)
check 5: pass
check 6: pass
check 7: pass
Recommended fix: In Option (b), change "striking all six Hispanic prospective jurors" to "striking multiple Hispanic prospective jurors" to align with the facts provided in the stem.
-->

## Issue 2 — argpass-opus

**Q12.** Sal appeals his conviction, arguing that DA Paula's jury selection tactics violated his constitutional rights. When questioned by the judge during voir dire, Paula claimed she struck the Hispanic jurors for expressing skepticism of police, but the record proved three of them never spoke. Did DA Paula's use of peremptory challenges violate the Equal Protection Clause?

(a) Yes, because the record showing that three jurors never spoke proves that her proffered race-neutral reason was a pretext for intentional discrimination. <!-- correct -->
(b) Yes, because striking all six Hispanic prospective jurors from the venire automatically constitutes a structural error requiring immediate reversal of the conviction.
(c) No, because prosecutors are legally entitled to strike any juror who expresses skepticism of police testimony, regardless of the juror's racial background.
(d) No, because the *Batson* framework solely applies to strikes made by defense attorneys and explicitly exempts prosecutors acting on behalf of the state.
(e) No, because peremptory challenges are entirely discretionary and courts cannot second-guess a prosecutor's stated reasons once a race-neutral justification is formally provided.

**Answer:** (a)

**Explanation:** The *Batson* framework prohibits striking jurors based on race. At step three, the judge must evaluate the prosecutor's race-neutral explanation. Because the record shows three of the Hispanic jurors never spoke, DA Paula's claim that they "expressed skepticism" is factually contradicted, proving the reason was a pretext for intentional discrimination. (b) is wrong because striking multiple jurors of one race is not an automatic structural error; the defendant must still prove discriminatory intent through the three-step framework. (c) is incorrect because while skepticism of police is a valid race-neutral reason, using it as a pretext to hide racial discrimination violates Equal Protection. (d) fails because *Batson* originally and primarily applies to prosecutors. (e) is wrong because courts are required to actively second-guess the prosecutor's stated reasons at step three to determine pretext.

**Tags:** chapters: [4], topics: [batson-framework], difficulty: easy, cognitive: application

**Grounding:** Chapter 4 (The Jury and Nullification) - Batson v. Kentucky

<!-- argument-pass: SHOULD FIX
(a) Argument-for: This relies correctly on Step 3 of the *Batson* framework. In cases like *Snyder v. Louisiana* and *Miller-El v. Dretke*, the Supreme Court established that when a prosecutor's stated race-neutral reason is objectively contradicted by the record (e.g., claiming a juror spoke when they were silent), it is powerful evidence of pretext. Because Paula's reason was factually false, it demonstrates intentional discrimination in violation of the Equal Protection Clause.
(b) Argument-for: A student might argue that the wholesale removal of a cognizable racial group from the venire creates an irrebuttable presumption of prejudice. Because the Supreme Court treats certain jury selection violations (like excluding a race from grand juries) as structural errors, one might incorrectly conclude that striking all minority jurors bypasses the need for the granular *Batson* steps and triggers automatic reversal for structural taint.
(c) Argument-for: Skepticism of police is widely recognized as a valid, race-neutral justification for a peremptory strike under *Purkett v. Elem*. A student might reason that because peremptory challenges generally require no "cause," invoking a recognized legal category categorically shields the strike from an Equal Protection claim. If the stated reason is facially valid, they might argue the prosecutor is fully entitled to the strike regardless of race.
(d) Argument-for: Historically, peremptory challenges were an absolute prerogative of the Crown/State. A student might confusedly recall that the *McCollum* decision expanded *Batson* to defense counsel and creatively (but wrongly) deduce that the modern Equal Protection framework only polices the newly granted rights of the defense, explicitly leaving the state's traditional prerogative unreviewable.
(e) Argument-for: Under *Batson* Step 2, the prosecutor's burden of production is incredibly low and does not require a "persuasive, or even plausible" explanation (*Purkett*). A student could argue that once this minimal formal burden is met with a facially neutral reason, the traditional discretionary nature of peremptory challenges takes over, legally barring the court from second-guessing the prosecutor's subjective logic.

Head-to-head: Option (a) is the decisively correct application of *Batson* Step 3. The distractors successfully use absolute language to lock in falsifiable legal propositions, making them robust under the close-call standard. However, option (b) hallucinates a fact not present in the prompt ("all six Hispanic prospective jurors"). While (b) is still legally false due to its claim of "automatic structural error," introducing a highly specific, unstated fact allows students to eliminate the distractor for the wrong reason (i.e., "the prompt didn't say there were six"). 

Falsifiable claim per distractor:
- (b): "automatically constitutes a structural error requiring immediate reversal" — wrong because excluding multiple jurors of a single race establishes a *prima facie* case at Step 1, but does not "automatically" establish a structural error bypassing the rest of the *Batson* burden-shifting framework.
- (c): "legally entitled to strike any juror who expresses skepticism... regardless of the juror's racial background" — wrong because the absolute word "any" fails in pretext scenarios; a prosecutor is *not* legally entitled to strike a skeptical juror if the actual motivation for the strike is racial discrimination.
- (d): "solely applies to strikes made by defense attorneys and explicitly exempts prosecutors" — wrong because *Batson* explicitly and originally governs prosecutors.
- (e): "courts cannot second-guess a prosecutor's stated reasons once a race-neutral justification is formally provided" — wrong because Step 3 of *Batson* explicitly requires courts to second-guess and evaluate the genuineness of the stated reasons.

Recommended fix: In option (b), delete the hallucinated "all six" to read: "Yes, because striking the Hispanic prospective jurors from the venire automatically constitutes..."
-->
