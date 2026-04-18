# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Evaluate defense attorney Rossi's use of peremptory challenges under the Batson framework.

(a) Subject to a Batson challenge, because the prohibition on race-based strikes applies equally to defense attorneys, and the court must determine if the reason is pretextual. <!-- correct -->
(b) Insulated from judicial review, because the Batson framework applies exclusively to prosecutorial strikes, protecting the criminal defendant's absolute constitutional right to aggressively shape the jury.
(c) Automatically invalid at step one, because striking six out of seven members of a protected class constitutes per se unconstitutional discrimination requiring no further analysis.
(d) Automatically valid at step two, because asserting a juror is "hostile to corporate business" serves as a legally irrebuttable race-neutral explanation that definitively ends the inquiry.
(e) Subject to a Batson challenge, but only if the prosecution can successfully prove that Rossi possesses a documented historical pattern of striking minority jurors in previous cases.

**Answer:** (a)

**Explanation:** (a) is correct because *Georgia v. McCollum* extended the *Batson* framework to defense attorneys. The trial court must proceed to step three to determine whether the facially race-neutral reason ("hostile to corporate business") is actually a pretext for racial discrimination. (b) is incorrect because the Equal Protection Clause protects the jurors' right not to be excluded based on race, which restricts defense attorneys as well as prosecutors. (c) is incorrect because statistical disparities at step one only establish a *prima facie* case requiring an explanation; they do not render the strikes per se unconstitutional. (d) is incorrect because a facially neutral reason at step two does not end the inquiry; the judge must still evaluate its genuineness at step three. (e) is incorrect because a *Batson* challenge does not require proof of a historical pattern; it can be established based entirely on the strikes in the current case.

**Tags:** chapters: [4], topics: [Batson-framework, equal-protection], difficulty: medium, cognitive: application

**Grounding:** Chapter 4 - The Jury (Batson framework, McCollum extension to defense attorneys)

<!-- audit: MUST FIX
check 1: pass (The legal framework regarding Georgia v. McCollum and Batson steps is perfectly accurate).
check 2: pass (None of the distractors represent defensible alternative interpretations of Batson).
check 3: pass (The explanation correctly applies the three-step framework and the Equal Protection rationale for defense attorneys).
check 4: FAILS. The stem is missing the factual scenario entirely. The options and the explanation reference highly specific facts (striking "six out of seven members" and giving the reason that a juror is "hostile to corporate business") that never appear in the prompt. A student reading the stem alone has nothing to evaluate.
check 5: pass (Uniform federal constitutional rule).
check 6: pass (No excluded topics).
check 7: pass (batson-framework appears in Ch 4 meta-map tags).
Recommended fix: Insert the missing fact pattern into the stem. E.g., "Defense attorney Rossi is defending a corporate executive. During voir dire, Rossi uses peremptory challenges to strike six out of seven minority jurors. When challenged, Rossi asserts that the stricken jurors appeared 'hostile to corporate business.' Evaluate Rossi's use of peremptory challenges..."
-->

## Issue 2 — argpass-sonnet

**Q12.** Evaluate defense attorney Rossi's use of peremptory challenges under the Batson framework.

(a) Subject to a Batson challenge, because the prohibition on race-based strikes applies equally to defense attorneys, and the court must determine if the reason is pretextual. <!-- correct -->
(b) Insulated from judicial review, because the Batson framework applies exclusively to prosecutorial strikes, protecting the criminal defendant's absolute constitutional right to aggressively shape the jury.
(c) Automatically invalid at step one, because striking six out of seven members of a protected class constitutes per se unconstitutional discrimination requiring no further analysis.
(d) Automatically valid at step two, because asserting a juror is "hostile to corporate business" serves as a legally irrebuttable race-neutral explanation that definitively ends the inquiry.
(e) Subject to a Batson challenge, but only if the prosecution can successfully prove that Rossi possesses a documented historical pattern of striking minority jurors in previous cases.

**Answer:** (a)

**Explanation:** (a) is correct because *Georgia v. McCollum* extended the *Batson* framework to defense attorneys. The trial court must proceed to step three to determine whether the facially race-neutral reason ("hostile to corporate business") is actually a pretext for racial discrimination. (b) is incorrect because the Equal Protection Clause protects the jurors' right not to be excluded based on race, which restricts defense attorneys as well as prosecutors. (c) is incorrect because statistical disparities at step one only establish a *prima facie* case requiring an explanation; they do not render the strikes per se unconstitutional. (d) is incorrect because a facially neutral reason at step two does not end the inquiry; the judge must still evaluate its genuineness at step three. (e) is incorrect because a *Batson* challenge does not require proof of a historical pattern; it can be established based entirely on the strikes in the current case.

**Tags:** chapters: [4], topics: [Batson-framework, equal-protection], difficulty: medium, cognitive: application

**Grounding:** Chapter 4 - The Jury (Batson framework, McCollum extension to defense attorneys)

<!-- argument-pass: MUST FIX
(a) Argument-for: Under *Georgia v. McCollum*, the *Batson* framework applies to peremptory strikes exercised by criminal defense attorneys. A prosecutor may object to defense strikes on equal protection grounds. The trial court must then move through the three-step *Batson* process, ultimately determining at step three whether the proffered race-neutral reason is merely a pretext for discrimination.
(b) Argument-for: The Sixth Amendment guarantees a criminal defendant the right to an impartial jury, and peremptory challenges are traditionally a core component of the defense strategy to eliminate potentially biased jurors without cause. One could argue that applying *Batson* to the defense impinges on this constitutional right. The original *Batson* ruling specifically addressed state action via the prosecutor, leading a student to conclude the framework protects the defendant from the state, not the other way around.
(c) Argument-for: Striking six out of seven members of a protected class is an overwhelming statistical disparity that establishes an undeniable inference of discriminatory intent. A student might argue that such an extreme pattern shifts the inquiry entirely, moving past a mere *prima facie* case to a conclusive finding of discrimination at step one. In extreme cases of disparate impact, the sheer numbers might be argued to render the strike *per se* invalid.
(d) Argument-for: Step two of the *Batson* framework requires only that the striking party offer a facially race-neutral reason. "Hostile to corporate business" contains no reference to race or protected characteristics. Since the Supreme Court in *Purkett v. Elem* held that a reason need not be persuasive or even plausible at step two, a student could argue that offering such a legally neutral reason definitively satisfies the proponent's burden and effectively ends the inquiry at that stage if uncontested.
(e) Argument-for: Proving discriminatory intent at step three is notoriously difficult without a pattern of behavior. Before *Batson*, *Swain v. Alabama* required showing a systemic, historical pattern of striking protected jurors. A student might conflate this older standard with *Batson*, arguing that establishing defense pretext requires the prosecution to point to documented historical practices rather than relying solely on the current trial's strikes.

Head-to-head: The distractors are actually incredibly well-crafted and comply perfectly with the close-call standard. They effectively use absolute language ("exclusively," "automatically invalid," "definitively ends," "only if") to lock in falsifiable legal propositions. Option (a) correctly applies *McCollum*. The catastrophic failure here, however, is the question stem itself: there is no fact pattern. Options (c) and (d) reference specific facts ("six out of seven members," "hostile to corporate business") that never appear in the prompt, making the question completely incoherent as written. Thus, despite the excellent distractors, the question warrants a MUST FIX.

Falsifiable claim per distractor:
- (b): "applies exclusively to prosecutorial strikes" — wrong because *Georgia v. McCollum* extended the *Batson* framework to criminal defense attorneys.
- (c): "constitutes per se unconstitutional discrimination requiring no further analysis" — wrong because step one statistics only establish a rebuttable *prima facie* case and never bypass steps two and three.
- (d): "legally irrebuttable race-neutral explanation that definitively ends the inquiry" — wrong because step two reasons are rebuttable and must be evaluated for pretext at step three.
- (e): "only if the prosecution can successfully prove that Rossi possesses a documented historical pattern" — wrong because *Batson* explicitly overruled the *Swain* requirement for a historical pattern, allowing proof based solely on the current case.

Recommended fix: Add the missing fact pattern to the question stem. Change the stem to: "During jury selection for a white-collar criminal trial, defense attorney Rossi uses peremptory challenges to strike six out of seven Black prospective jurors. When the prosecution raises an objection, Rossi states that he struck them because they appeared 'hostile to corporate business.' Evaluate defense attorney Rossi's use of peremptory challenges under the Batson framework."
-->
