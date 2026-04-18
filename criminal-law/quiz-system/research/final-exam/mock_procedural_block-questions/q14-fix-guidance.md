# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-opus

**Q14.** During jury instructions, the trial judge explicitly stated, "There is no such thing as valid jury nullification. If you acquit the defendant contrary to the evidence, you will violate your oath and the law." Sal's defense attorney objects to the language used. Was the trial judge's instruction regarding jury nullification legally permissible?

(a) Yes, because juries lack any constitutional right to nullify, and judges are affirmatively required to prohibit verdicts contrary to the evidentiary record.
(b) Yes, because instructing jurors that nullification is invalid effectively prevents the historical problem of racially discriminatory acquittals in state criminal proceedings.
(c) No, because while judges may discourage nullification, explicitly telling jurors it is invalid and implies they could be punished crosses into unconstitutional coercion. <!-- correct -->
(d) No, because criminal defendants possess a fundamental constitutional right to have the jury informed of its absolute power to nullify the charges.
(e) No, because under the Sixth Amendment, trial judges must remain entirely silent regarding the jury's inherent power to judge both the law and facts.

**Answer:** (c)

**Explanation:** Under *United States v. Kleinman*, while trial judges may strongly discourage jury nullification, they cross the line into unconstitutional coercion if they instruct jurors that nullification is "invalid" or imply that jurors could be punished for violating the law by acquitting. (a) is wrong because while juries lack a legal right to nullification, judges cannot use coercive language implying punishment to prevent it. (b) fails because the historical rationale for preventing discriminatory acquittals does not validate an otherwise coercive jury instruction. (d) is incorrect because criminal defendants do not possess a constitutional right to have the jury affirmatively informed of its nullification power. (e) is wrong because judges are not required to remain silent; they may instruct the jury to follow the law, provided the instruction is not coercive.

**Tags:** chapters: [4], topics: [anti-nullification-instruction-limits], difficulty: medium, cognitive: application

**Grounding:** Chapter 4 (The Jury and Nullification) - United States v. Kleinman

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could reasonably point to *Sparf v. United States* to argue that because the jury lacks a constitutional right to nullify, the trial judge has an affirmative obligation to ensure they do not exercise this power. Under this logic, explicitly forbidding acquittals contrary to the evidence is simply a mandatory enforcement of the jury's legal boundaries.
(b) Argument-for: A student might recall discussions regarding the dark history of jury nullification, such as racially motivated acquittals in the Jim Crow South. They could argue that the instruction is legally permissible because preventing this specific historical abuse justifies strict anti-nullification language, overriding any minor coercive effects on the jury.
(c) Argument-for: Under *United States v. Kleinman*, while judges can instruct juries to follow the law and thereby discourage nullification, telling them nullification is "invalid" is legally inaccurate (because an acquittal by nullification is undeniably valid and final). Furthermore, warning that they will "violate the law" crosses into unconstitutional coercion because it implies jurors could face legal punishment for their verdict.
(d) Argument-for: A student could argue that because nullification is an inherent, unreviewable power of the jury (ensured by the Double Jeopardy Clause), the Sixth Amendment must afford criminal defendants a fundamental right to have the jury explicitly informed of this absolute power so they can exercise it.
(e) Argument-for: A student could argue that any instruction touching on nullification inherently coerces the jury or encroaches on its independence. Therefore, the Sixth Amendment requires judges to remain entirely silent on the jury's power to judge the law and facts, leaving the jury strictly autonomous without any judicial discouragement.

Head-to-head: Option (c) is the only legally correct choice, accurately capturing the boundary between permissible discouragement of nullification and impermissible coercion under *Kleinman*. Option (a) relies on the false legal claim that judges are affirmatively required to prohibit acquittals contrary to the record, which would essentially constitute an unconstitutional directed verdict of guilty. Option (d) asserts the false legal claim that defendants have a fundamental right to a nullification instruction. Option (e) falsely claims that judges must remain entirely silent and that juries have the right to judge the law. Option (b) correctly states a historical rationale but pairs the wrong conclusion ("Yes") with a policy/empirical claim rather than an explicit, falsifiable legal doctrine. Because (b) lacks an absolute legal falsehood in its reasoning, the question should be fixed to lock it down.

Falsifiable claim per distractor:
- (a): "judges are affirmatively required to prohibit verdicts contrary to the evidentiary record" — wrong because judges categorically cannot direct a verdict of guilty or prohibit an acquittal, even if contrary to the evidence.
- (b): "instructing jurors that nullification is invalid effectively prevents the historical problem..." — wrong because the conclusion is incorrect, but its rationale is merely a historical/policy claim rather than an identifiable false legal rule.
- (d): "criminal defendants possess a fundamental constitutional right to have the jury informed of its absolute power" — wrong because defendants categorically lack the right to a nullification instruction in every jurisdiction.
- (e): "trial judges must remain entirely silent regarding the jury's inherent power to judge both the law and facts" — wrong because juries do not have the power to judge the law, and judges are expressly permitted to instruct juries to follow the law.

Recommended fix: Edit (b) to include a formal false legal claim. For example: "(b) Yes, because the Equal Protection Clause categorically requires trial judges to issue strict anti-nullification instructions to prevent racially discriminatory acquittals."
-->
