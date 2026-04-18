# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q14.** Assume Dominic appeals his conviction, arguing the judge's final instruction on jury nullification violated his trial rights. How should the appellate court rule?

(a) Uphold the conviction, because trial courts have an affirmative constitutional duty to actively inform juries that nullification is entirely illegal and strictly prohibited.
(b) Uphold the conviction, because the instruction correctly and neutrally stated that juries have absolutely no legal right to nullify contrary to the presented evidence.
(c) Vacate the conviction, because criminal defendants have a fundamental constitutional right to an instruction affirmatively informing the jury of its factual nullification power.
(d) Vacate the conviction, because while courts may inform juries they have no right to nullify, explicitly threatening them with contempt crosses into impermissible coercion. <!-- correct -->
(e) Vacate the conviction, because any judicial mention whatsoever of nullification during final instructions constitutes structural error requiring automatic appellate reversal.

**Answer:** (d)

**Explanation:** The correct answer is (d). Under *United States v. Kleinman*, courts may issue anti-nullification instructions informing the jury that they must follow the law and have no legal right to acquit contrary to the evidence. However, instructing jurors that they will "be subject to contempt proceedings" (Fact 11) crosses the line from permissible guidance into impermissible coercion by threatening the jury's independence with punitive consequences.

(a) is incorrect because courts have the authority, but not an affirmative constitutional *duty*, to issue anti-nullification instructions.
(b) is incorrect because the instruction did not stop at stating the law; it explicitly threatened jurors with contempt, rendering it coercive.
(c) is incorrect because courts consistently hold that defendants have no legal right to demand an instruction informing the jury of their unreviewable power to nullify.
(e) is incorrect because appropriate anti-nullification instructions (without threats of punishment) are permissible and do not constitute error.

**Tags:** chapters: [4], topics: [anti-nullification-instruction-limits], difficulty: medium, cognitive: application

**Grounding:** Chapter 4 - The Jury and Nullification > Anti-nullification instruction limits

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might reason that because jury nullification contravenes the rule of law and the juror's oath to follow the judge's instructions, courts must actively prevent it. Under this view, due process and the constitutional structure inherently demand that trial courts take proactive steps to instruct juries against nullification in every case. Therefore, the student would conclude that the judge's instruction was not just permissible, but a mandatory constitutional duty.
(b) Argument-for: A student could argue that because courts consistently hold juries have no legal right to nullify (as established in cases like *United States v. Dougherty*), an instruction stating this fact is legally impeccable. The student might view the threat of contempt as a mere factual consequence or enforcement mechanism of the neutral legal principle that nullification is prohibited. Thus, the conviction should be upheld because the instruction's underlying premise correctly stated the law without necessarily recognizing the coercion boundary.
(c) Argument-for: A student might conflate the jury's unreviewable power to acquit with a defendant's right to a jury trial. Relying on the historical role of the jury as a bulwark against government oppression (e.g., *Bushell's Case*), the student could argue that defendants have a fundamental constitutional right to have the jury explicitly informed of its power to nullify. Under this theory, any anti-nullification instruction is a violation of the Sixth Amendment requiring reversal.
(d) Argument-for: Under *United States v. Kleinman*, it is well-established that while a trial judge may instruct a jury that they have no right to nullify, the judge crosses into impermissible coercion by actively threatening the jury. Informing the jury that they will face contempt proceedings for acquitting the defendant destroys the independence of the jury and coerces a verdict. Therefore, this violates the defendant's trial rights and requires the conviction to be vacated.
(e) Argument-for: A student could argue that because the jury's power to nullify is historically ingrained and strictly unreviewable, any judicial comment addressing it intrudes upon the jury's exclusive province. Under this strict view, even a neutral anti-nullification instruction fundamentally infects the trial process. This would logically lead to the conclusion that such an instruction constitutes a structural error that cannot be subject to harmless error review and automatically requires appellate reversal.

Head-to-head: Option (d) correctly applies doctrine by drawing the line established in *Kleinman*: courts may instruct against nullification but cannot coerce jurors with threats of contempt. Options (a), (c), and (e) present explicit, falsifiable legal claims that contradict established precedent using strong, absolute language ("affirmative constitutional duty", "fundamental constitutional right", "structural error requiring automatic appellate reversal"). Option (b), however, is weaker as a distractor. Its primary legal proposition—that juries have "absolutely no legal right to nullify"—is actually a true statement of law. The option is only rendered incorrect because characterizing the instruction as "correctly and neutrally stated" ignores the fact pattern's detail about the contempt threat. Because (b) relies on an implicit factual omission rather than an explicitly false legal claim, it fails the close-call standard. 

Falsifiable claim per distractor:
- (a): "affirmative constitutional duty to actively inform juries" — wrong because courts have the discretion, not a mandatory constitutional duty, to issue anti-nullification instructions.
- (b): "correctly and neutrally stated" — wrong because the instruction contained a coercive threat of contempt, but this relies on a factual mischaracterization of the prompt rather than a strictly false legal claim.
- (c): "fundamental constitutional right to an instruction affirmatively informing the jury" — wrong because courts uniformly hold that defendants have no legal right to demand a nullification instruction.
- (e): "any judicial mention whatsoever... constitutes structural error requiring automatic appellate reversal" — wrong because neutral anti-nullification instructions are generally permissible and do not inherently constitute reversible error.

Recommended fix: Edit (b) to explicitly assert a false legal claim regarding the judge's authority. For example: "(b) Uphold the conviction, because trial judges are categorically permitted to explicitly threaten jurors with contempt to enforce the rule that juries have absolutely no legal right to nullify."
-->

## Issue 3 — argpass-opus

**Q14.** Assume Dominic appeals his conviction, arguing the judge's final instruction on jury nullification violated his trial rights. How should the appellate court rule?

(a) Uphold the conviction, because trial courts have an affirmative constitutional duty to actively inform juries that nullification is entirely illegal and strictly prohibited.
(b) Uphold the conviction, because the instruction correctly and neutrally stated that juries have absolutely no legal right to nullify contrary to the presented evidence.
(c) Vacate the conviction, because criminal defendants have a fundamental constitutional right to an instruction affirmatively informing the jury of its factual nullification power.
(d) Vacate the conviction, because while courts may inform juries they have no right to nullify, explicitly threatening them with contempt crosses into impermissible coercion. <!-- correct -->
(e) Vacate the conviction, because any judicial mention whatsoever of nullification during final instructions constitutes structural error requiring automatic appellate reversal.

**Answer:** (d)

**Explanation:** The correct answer is (d). Under *United States v. Kleinman*, courts may issue anti-nullification instructions informing the jury that they must follow the law and have no legal right to acquit contrary to the evidence. However, instructing jurors that they will "be subject to contempt proceedings" (Fact 11) crosses the line from permissible guidance into impermissible coercion by threatening the jury's independence with punitive consequences.

(a) is incorrect because courts have the authority, but not an affirmative constitutional *duty*, to issue anti-nullification instructions.
(b) is incorrect because the instruction did not stop at stating the law; it explicitly threatened jurors with contempt, rendering it coercive.
(c) is incorrect because courts consistently hold that defendants have no legal right to demand an instruction informing the jury of their unreviewable power to nullify.
(e) is incorrect because appropriate anti-nullification instructions (without threats of punishment) are permissible and do not constitute error.

**Tags:** chapters: [4], topics: [anti-nullification-instruction-limits], difficulty: medium, cognitive: application

**Grounding:** Chapter 4 - The Jury and Nullification > Anti-nullification instruction limits

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might recall that juries must apply the law as instructed by the judge (*Sparf v. United States*). Building on this, the student could logically conclude that to protect the integrity of the legal system, trial courts must possess an "affirmative constitutional duty" to expressly forbid nullification in every case, making this option seem legally sound.
(b) Argument-for: A student might focus exclusively on the core doctrine that juries have absolutely no *legal right* to nullify. If they gloss over the coercive threat of contempt in the fact pattern, they could conclude the judge's instruction was merely a strong, legally accurate, and "neutral" statement regarding the rigid boundaries of the jury's power.
(c) Argument-for: A student could argue that because juries possess the unreviewable de facto power to nullify—secured by the Double Jeopardy Clause and general verdict rules—defendants must logically have a corresponding "fundamental constitutional right" to ensure the jury is made fully aware of this inherent power to judge both law and fact.
(d) Argument-for: This is the correct answer. Under cases like *United States v. Kleinman*, trial courts are legally permitted to instruct a jury that they have no right to nullify, but they are forbidden from using language that coerces the jury. Explicitly threatening the jury with contempt proceedings inherently coerces jurors by promising punitive consequences, thereby violating the defendant's right to an independent jury verdict.
(e) Argument-for: A student could believe that the jury's nullification power is so deeply embedded in the Sixth Amendment that any interference by the trial judge is strictly forbidden. They might reasonably argue that "any judicial mention whatsoever" of nullification prejudices the jury's deliberative secrecy and independence, thereby constituting structural error that warrants automatic reversal.

Head-to-head:
The keyed answer (d) perfectly resolves the scenario by correctly distinguishing between permissible anti-nullification guidance and impermissible coercion. Distractors (a), (c), and (e) are highly effective because they contain beautifully locked, easily falsifiable legal claims ("affirmative constitutional duty," "fundamental constitutional right," "any judicial mention whatsoever... structural error"). However, distractor (b) relies primarily on a factual mischaracterization ("neutrally stated") rather than asserting a false *legal* premise. Under the strict close-call standard, distractors must contain an explicit, identifiable false legal claim rather than merely misstating the facts of the prompt.

Falsifiable claim per distractor:
- (a): "trial courts have an affirmative constitutional duty" — wrong because courts have discretion, not a mandatory constitutional obligation, to issue anti-nullification instructions.
- (b): "correctly and neutrally stated" — wrong primarily on the facts (the instruction included a threat of contempt), though it implicitly assumes a contempt threat can legally be a "neutral" statement of law.
- (c): "criminal defendants have a fundamental constitutional right to an instruction" — wrong because federal and state case law universally denies defendants the right to demand a pro-nullification instruction.
- (e): "any judicial mention whatsoever... constitutes structural error requiring automatic appellate reversal" — wrong because courts are widely permitted to give neutral anti-nullification instructions without triggering structural error.

Recommended fix: Revise (b) to feature a purely false legal claim locked with absolute language. For example: "Uphold the conviction, because trial judges are categorically permitted to explicitly threaten jurors with contempt to prevent the lawless act of nullification."
-->
