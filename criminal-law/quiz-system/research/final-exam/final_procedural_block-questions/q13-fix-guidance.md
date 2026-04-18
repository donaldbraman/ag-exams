# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q13.** Evaluate the trial judge's final instructions regarding jury nullification.

(a) Erroneous, because while courts may instruct jurors to simply follow the law, explicitly threatening them with contempt proceedings crosses the line into unconstitutional juror coercion. <!-- correct -->
(b) Permissible, because juries possess no constitutional right to nullify, granting trial courts the absolute authority to use any measure necessary to guarantee strict legal compliance.
(c) Erroneous, because criminal defendants possess a firmly recognized Sixth Amendment right to a jury instruction explicitly informing the jury of its inherent power to nullify.
(d) Permissible, because the Double Jeopardy Clause guarantees that the jury's acquittal power remains entirely unchecked, rendering any of the trial judge's verbal threats harmless error.
(e) Erroneous, because federal judges are strictly constitutionally prohibited from ever mentioning the controversial concept of nullification during their final jury instructions in any criminal proceeding.

**Answer:** (a)

**Explanation:** (a) is correct because *United States v. Kleinman* holds that while a judge may permissibly instruct a jury to follow the law and discourage nullification, explicitly stating that nullification is invalid or threatening jurors with punitive consequences (like contempt) constitutes unconstitutional coercion. (b) is incorrect because the trial court's authority to discourage nullification is limited and cannot extend to coercive threats of punishment against the jurors. (c) is incorrect because courts have consistently held that while juries possess the *power* to nullify, defendants have no constitutional *right* to a jury instruction informing them of it. (d) is incorrect because the unreviewable nature of an acquittal does not cure the constitutional error of coercing a jury during deliberations. (e) is incorrect because judges are allowed to mention and actively discourage nullification, provided their instructions do not cross into coercive threats.

**Tags:** chapters: [4], topics: [anti-nullification-instruction-limits, jury-nullification], difficulty: easy, cognitive: application

**Grounding:** Chapter 4 - The Jury (United States v. Kleinman)

<!-- argument-pass: MUST FIX
(a) Argument-for: This option correctly concludes that the instruction was erroneous and identifies the exact boundary established in cases like *United States v. Kleinman*. While juries do not have a constitutional right to nullify and courts can instruct them to follow the law, judges cannot cross into unconstitutional coercion. Threatening jurors with contempt proceedings or other punitive measures fundamentally undermines the independence of the jury and improperly coerces a verdict. Thus, this option perfectly captures the prevailing legal standard.
(b) Argument-for: A student could argue that because the Supreme Court firmly rejected a jury's right to nullify, the trial court's authority to enforce strict legal compliance is paramount. If juries possess absolutely no constitutional right to nullify, then any instruction ensuring they do not usurp judicial authority must be valid. Under this theory, threatening contempt is merely an exercise of the judge's absolute authority to prevent unlawful jury conduct, making the instruction permissible.
(c) Argument-for: Given the historical role of the jury as a safeguard against government oppression, a student might infer that the jury's unreviewable power to acquit translates into an affirmative constitutional right for the defendant. Because nullification is widely acknowledged as an inherent power, the argument would be that the Sixth Amendment guarantees the defendant the right to have the jury informed of this power. Therefore, an instruction that not only fails to inform them but threatens them against it would inherently violate the defendant's constitutional rights.
(d) Argument-for: A student might rely on the absolute finality of an acquittal under the Double Jeopardy Clause to argue that any judicial threats are ultimately toothless and therefore harmless error. Since the jury's power to return a "not guilty" verdict remains structurally unchecked regardless of what the judge says, the threat cannot legally prevent nullification. Under this structural perspective, the verbal threats do not constitute reversible error because they cannot override the jury's actual power, rendering the instruction functionally permissible.
(e) Argument-for: A student could argue that introducing the concept of jury nullification during final instructions is inherently prejudicial, as it invites confusion or tempts the jury to violate its oath. To maintain the integrity of the fact-finding process, federal courts might be seen as having a strict, categorical prohibition against even mentioning the controversial topic. Thus, by explicitly addressing nullification, the judge would have automatically committed constitutional error, regardless of whether the mention was intended to discourage it.

Head-to-head:
Option (a) correctly applies the distinction between permissibly instructing a jury to follow the law and unconstitutionally coercing them with punitive threats. Distractor (b) is wrong because it incorrectly claims trial courts have "absolute authority to use any measure necessary," which is false since coercive threats are prohibited. Distractor (c) asserts a "firmly recognized Sixth Amendment right" to a nullification instruction, which courts uniformly reject. Distractor (d) claims the Double Jeopardy Clause makes verbal threats "harmless error," but coercive jury instructions are not categorized as harmless error, nor do they make the underlying act "Permissible." Distractor (e) claims federal judges are "strictly constitutionally prohibited from ever mentioning" nullification, which is false since judges may instruct juries against it. While the distractors are perfectly falsifiable and well-written, the question stem is entirely missing its fact pattern, forcing students to guess the judge's actions from the options.

Falsifiable claim per distractor:
- (b): "absolute authority to use any measure necessary to guarantee strict legal compliance" — wrong because judges are bounded by the Constitution and cannot use coercive threats of punishment.
- (c): "firmly recognized Sixth Amendment right to a jury instruction explicitly informing the jury" — wrong because there is no such recognized right; courts consistently refuse to give this instruction.
- (d): "rendering any of the trial judge's verbal threats harmless error" — wrong because coercive jury instructions that threaten contempt are not harmless error and do not render the instruction "permissible."
- (e): "strictly constitutionally prohibited from ever mentioning the controversial concept of nullification" — wrong because judges are permitted to mention nullification in order to explicitly instruct jurors against it.

Recommended fix: The distractors effectively utilize the close-call standard and are structurally excellent. However, the question stem is missing the fact pattern describing the judge's actions. Add a vignette before the question stem, such as: "At the close of a federal criminal trial, the judge instructed the jury that if they engaged in jury nullification to acquit the defendant, they would face contempt proceedings."
-->

## Issue 3 — argpass-opus

**Q13.** Evaluate the trial judge's final instructions regarding jury nullification.

(a) Erroneous, because while courts may instruct jurors to simply follow the law, explicitly threatening them with contempt proceedings crosses the line into unconstitutional juror coercion. <!-- correct -->
(b) Permissible, because juries possess no constitutional right to nullify, granting trial courts the absolute authority to use any measure necessary to guarantee strict legal compliance.
(c) Erroneous, because criminal defendants possess a firmly recognized Sixth Amendment right to a jury instruction explicitly informing the jury of its inherent power to nullify.
(d) Permissible, because the Double Jeopardy Clause guarantees that the jury's acquittal power remains entirely unchecked, rendering any of the trial judge's verbal threats harmless error.
(e) Erroneous, because federal judges are strictly constitutionally prohibited from ever mentioning the controversial concept of nullification during their final jury instructions in any criminal proceeding.

**Answer:** (a)

**Explanation:** (a) is correct because *United States v. Kleinman* holds that while a judge may permissibly instruct a jury to follow the law and discourage nullification, explicitly stating that nullification is invalid or threatening jurors with punitive consequences (like contempt) constitutes unconstitutional coercion. (b) is incorrect because the trial court's authority to discourage nullification is limited and cannot extend to coercive threats of punishment against the jurors. (c) is incorrect because courts have consistently held that while juries possess the *power* to nullify, defendants have no constitutional *right* to a jury instruction informing them of it. (d) is incorrect because the unreviewable nature of an acquittal does not cure the constitutional error of coercing a jury during deliberations. (e) is incorrect because judges are allowed to mention and actively discourage nullification, provided their instructions do not cross into coercive threats.

**Tags:** chapters: [4], topics: [anti-nullification-instruction-limits, jury-nullification], difficulty: easy, cognitive: application

**Grounding:** Chapter 4 - The Jury (United States v. Kleinman)

<!-- argument-pass: MUST FIX
(a) Argument-for: Option (a) accurately reflects the holding in cases like *United States v. Kleinman*. While trial courts possess the authority to instruct juries to strictly follow the law, they cannot cross the line into outright coercion. Explicitly threatening jurors with contempt or other punitive measures for nullifying violates the Sixth Amendment right to an independent, uncoerced jury. Because this option captures both the permissible scope and the constitutional limit of anti-nullification instructions, it is legally correct.
(b) Argument-for: A student could defend (b) by relying on *Sparf v. United States*, which established that juries have no legal right to nullify. Since nullification is technically a violation of the juror's oath to apply the law to the facts, trial courts have a compelling interest in preventing it. Therefore, a student might deduce that courts possess absolute authority to enforce strict legal compliance by any means necessary, including threats of contempt, to uphold the rule of law.
(c) Argument-for: Option (c) appeals to the historical role of the jury as a safeguard against government oppression. Because the jury possesses the unreviewable power to acquit against the weight of the evidence, a student could argue that this power is a fundamental component of the Sixth Amendment. Consequently, criminal defendants must possess a corresponding constitutional right to have the jury explicitly instructed on this inherent power, making any failure to do so, or instructions to the contrary, erroneous.
(d) Argument-for: A student might argue for (d) based on the absolute protections of the Double Jeopardy Clause. Because a jury's decision to acquit—even through nullification—is final and completely unreviewable, any verbal threats from the judge cannot legally prevent an acquittal. The argument follows that since the jury's ultimate power remains unchecked in practice, any coercive statements by the trial judge are rendered harmless error, making the instruction functionally permissible.
(e) Argument-for: Option (e) posits that because nullification is an inherent jury prerogative, any judicial interference is unconstitutional. A student could argue that even mentioning nullification to discourage it improperly prejudices the jury and invades their deliberative independence. Therefore, federal judges must be categorically prohibited from ever bringing up the concept during final instructions, rendering the judge's comments erroneous simply for addressing the topic.

Head-to-head: 
Option (a) correctly identifies the balance struck in *Kleinman*: judges may instruct juries to follow the law, but cannot coerce them with threats of punishment. Options (b), (c), (d), and (e) all contain clear, falsifiable legal errors regarding the rights of defendants, the absolute authority of judges, or the impact of the Double Jeopardy Clause. However, the question as written is fundamentally broken because it completely lacks a fact pattern. The prompt merely says "Evaluate the trial judge's final instructions..." without describing what the judge actually said or did. The student is forced to reverse-engineer the facts (that the judge explicitly threatened the jury with contempt) from the correct answer, which is unacceptable for a multiple-choice question.

Falsifiable claim per distractor:
- (b): "absolute authority to use any measure necessary" — wrong because a judge's authority to enforce compliance is constrained by the Sixth Amendment; they cannot use coercive threats of punishment.
- (c): "firmly recognized Sixth Amendment right to a jury instruction explicitly informing the jury of its inherent power" — wrong because courts uniformly hold that defendants have no right to a nullification instruction.
- (d): "rendering any of the trial judge's verbal threats harmless error" — wrong because unconstitutional juror coercion is a violation of the Sixth Amendment right to an impartial jury and is not cured or rendered harmless simply because acquittals are protected by Double Jeopardy.
- (e): "strictly constitutionally prohibited from ever mentioning the controversial concept" — wrong because judges are generally permitted to instruct juries that they must follow the law and actively discourage nullification, provided they do not cross into coercion.

Recommended fix: Add a brief fact pattern to the prompt. For example: "During a federal criminal trial, the judge suspects the jury might acquit against the weight of the evidence. In the final instructions, the judge explicitly warns the jurors that they must follow the law and threatens them with contempt of court proceedings if they engage in jury nullification. Evaluate the trial judge's final instructions regarding jury nullification."
-->
