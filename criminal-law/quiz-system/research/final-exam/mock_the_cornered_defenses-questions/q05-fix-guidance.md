# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Assume Silas is prosecuted in a jurisdiction (like Kansas) that has abolished the affirmative defense of insanity and adopted the mens rea model. How does Silas's mental illness affect his liability for intentional murder?

(a) It provides no legal defense because the abolition model strictly bars all psychological evidence of mental illness from being introduced during a criminal trial.
(b) It provides a complete legal excuse because the United States Supreme Court held the constitutional floor requires categorically acquitting severely delusional criminal defendants.
(c) It can be used to negate the requisite mental state, as his delusion prevented him from forming the specific intent to kill a human being. <!-- correct -->
(d) It acts strictly as a mitigating factor at sentencing, as the jurisdiction explicitly precludes mental illness from directly negating any underlying statutory offense elements.
(e) It shifts the evidentiary burden to the prosecution to prove his sanity beyond a reasonable doubt, restoring the traditional baseline presumption of mental competence.

**Answer:** (c)

**Explanation:** In jurisdictions that have abolished the affirmative defense of insanity (the mens rea model upheld in *Kahler v. Kansas*), evidence of mental illness is still admissible, but only to negate the specific mens rea required by the statute. Because Silas believed he was shooting a "monster made of smoke," he lacked the required intent to kill a human being, meaning his illness can successfully negate the mens rea. (a) is incorrect because the mens rea model explicitly allows mental illness evidence when it negates statutory intent. (b) is incorrect because *Kahler* explicitly held the Constitution does not require states to provide an affirmative insanity excuse. (d) is incorrect because mental illness evidence is used at the guilt phase to challenge the prosecution's proof of mens rea, not merely at sentencing. (e) is incorrect because the mens rea model eliminates the insanity defense entirely; it does not shift the burden to the prosecution to prove sanity, but merely holds the prosecution to its standard burden of proving intent.

**Tags:** chapters: [23], topics: [mens rea model, insanity abolition, kahler v. kansas], difficulty: medium, cognitive: application

**Grounding:** Chapter 23: mens-rea-model-abolition, kahler-constitutional-floor

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: The stem completely omits the facts of Silas's mental illness and the crime. The explanation references him believing he was shooting a "monster made of smoke," but this essential fact is missing from the stem, making option (c)'s factual conclusion ungrounded.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Add the missing factual context to the stem (e.g., "Silas shoots and kills a person while suffering from a severe delusion that he is shooting a 'monster made of smoke'. Assume Silas is prosecuted...").
-->

## Issue 2 — argpass-opus

**Q5.** Assume Silas is prosecuted in a jurisdiction (like Kansas) that has abolished the affirmative defense of insanity and adopted the mens rea model. How does Silas's mental illness affect his liability for intentional murder?

(a) It provides no legal defense because the abolition model strictly bars all psychological evidence of mental illness from being introduced during a criminal trial.
(b) It provides a complete legal excuse because the United States Supreme Court held the constitutional floor requires categorically acquitting severely delusional criminal defendants.
(c) It can be used to negate the requisite mental state, as his delusion prevented him from forming the specific intent to kill a human being. <!-- correct -->
(d) It acts strictly as a mitigating factor at sentencing, as the jurisdiction explicitly precludes mental illness from directly negating any underlying statutory offense elements.
(e) It shifts the evidentiary burden to the prosecution to prove his sanity beyond a reasonable doubt, restoring the traditional baseline presumption of mental competence.

**Answer:** (c)

**Explanation:** In jurisdictions that have abolished the affirmative defense of insanity (the mens rea model upheld in *Kahler v. Kansas*), evidence of mental illness is still admissible, but only to negate the specific mens rea required by the statute. Because Silas believed he was shooting a "monster made of smoke," he lacked the required intent to kill a human being, meaning his illness can successfully negate the mens rea. (a) is incorrect because the mens rea model explicitly allows mental illness evidence when it negates statutory intent. (b) is incorrect because *Kahler* explicitly held the Constitution does not require states to provide an affirmative insanity excuse. (d) is incorrect because mental illness evidence is used at the guilt phase to challenge the prosecution's proof of mens rea, not merely at sentencing. (e) is incorrect because the mens rea model eliminates the insanity defense entirely; it does not shift the burden to the prosecution to prove sanity, but merely holds the prosecution to its standard burden of proving intent.

**Tags:** chapters: [23], topics: [mens rea model, insanity abolition, kahler v. kansas], difficulty: medium, cognitive: application

**Grounding:** Chapter 23: mens-rea-model-abolition, kahler-constitutional-floor

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that when a state completely abolishes the insanity defense, it effectively removes mental illness from the guilt phase entirely. In this view, admitting psychological evidence would just be a backdoor to the abolished defense, meaning the abolition model "strictly bars all psychological evidence" to maintain the integrity of the abolition.
(b) Argument-for: A student could argue that fundamental due process and the Eighth Amendment prevent the conviction of individuals completely disconnected from reality. Under this theory, while states can abolish the traditional M'Naghten or ALI tests, the U.S. Supreme Court must have established a constitutional floor that requires acquitting severely delusional defendants, regardless of state statute.
(c) Argument-for: This is the legally correct application of the mens rea model, as upheld in Kahler v. Kansas. When a jurisdiction abolishes the affirmative defense of insanity, it allows mental illness evidence solely to negate the requisite mental state of the crime. Here, Silas's delusion that he was shooting a non-human entity negates the specific intent to kill a human being, barring conviction for intentional murder.
(d) Argument-for: A student might recall that under Clark v. Arizona, states have wide latitude to channel mental illness evidence. If a jurisdiction abolishes the insanity defense, a student could reasonably conclude that it channels mental illness "strictly as a mitigating factor at sentencing," refusing to let it negate the mens rea at the guilt phase to prevent defendants from escaping liability entirely.
(e) Argument-for: A student could argue that if insanity is no longer an affirmative defense (which the defendant typically must prove), the legal baseline changes. By removing the affirmative defense framework, the burden shifts back to the prosecution, requiring them to prove the defendant's sanity beyond a reasonable doubt as an implicit element of proving criminal intent.

Head-to-head: 
Option (c) correctly identifies the mechanical operation of the mens rea model (allowing evidence to negate specific intent, as in Kahler). However, the prompt is completely missing the factual predicate about Silas's specific delusion (shooting a "monster made of smoke"), which is heavily relied upon in the explanation and is necessary to make the second half of option (c) logically follow. Distractors (a), (b), (d), and (e) are well-crafted with falsifiable, legally incorrect claims. (a) falsely claims an absolute evidentiary bar; (b) hallucinates a Supreme Court holding that Kahler explicitly rejected; (d) incorrectly claims evidence is strictly for sentencing; and (e) falsely claims the burden shifts to prove sanity rather than just proving the elements of the offense. Because (c) assumes facts completely absent from the prompt, the question is a MUST FIX.

Falsifiable claim per distractor:
- (a): "strictly bars all psychological evidence of mental illness" — wrong because the mens rea model specifically allows this evidence to negate the mens rea element.
- (b): "the United States Supreme Court held the constitutional floor requires categorically acquitting severely delusional criminal defendants" — wrong because the Court in Kahler held that the Constitution does not require an affirmative insanity defense, even for the severely delusional.
- (d): "explicitly precludes mental illness from directly negating any underlying statutory offense elements" — wrong because the defining feature of the mens rea model is that it allows mental illness to negate statutory offense elements.
- (e): "shifts the evidentiary burden to the prosecution to prove his sanity beyond a reasonable doubt" — wrong because the model eliminates sanity as a legal concept in the guilt phase; the prosecution just proves mens rea, not "sanity."

Recommended fix: Add the missing factual premise to the prompt: "Assume Silas, suffering from a severe delusion that he was shooting a 'monster made of smoke,' shot and killed a person. He is prosecuted in a jurisdiction..."
-->
