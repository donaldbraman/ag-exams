# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-opus

**Q9.** Is Alba guilty of depraved-heart murder for Cody's death?

(a) Guilty, because isolating an overdosing victim and incapacitating his rescuer demonstrates extreme indifference to the value of human life.
(b) Guilty, because Alba's specific intent to knock Dane unconscious automatically transfers to the subsequent and connected death of Cody.
(c) Not guilty, because depraved-heart murder requires the use of a deadly weapon against the actual victim who suffers the fatal injury.
(d) Not guilty, because Alba did not harbor the specific purpose to cause Cody's death when moving him into the windowless bathroom.
(e) Not guilty, because Cody was already suffering from respiratory failure before Alba took any affirmative action to prevent the rescue.

**Answer:** (a)

**Explanation:** (a) is correct because depraved-heart murder requires a mental state of extreme indifference to the value of human life; actively dragging a dying victim into a windowless bathroom and incapacitating the only rescuer easily satisfies this standard. (b) is wrong because transferred intent applies to hitting the wrong target with the same intended harm, not aggregating intent across different victims and crimes. (c) is wrong because depraved-heart murder focuses on the defendant's reckless mental state and conduct, not the direct use of a weapon on the deceased. (d) is wrong because depraved-heart murder explicitly does not require specific intent or purpose to kill. (e) is wrong because hastening or ensuring a death by preventing rescue satisfies the causation requirement for homicide.

**Tags:** chapters: [13], topics: [depraved heart murder, extreme indifference, omissions], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, extreme-indifference-standard

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Depraved-heart murder requires a conscious disregard of an unjustifiable risk, demonstrating extreme indifference to human life. By affirmatively isolating a dying overdose victim in a windowless room and incapacitating his only rescuer, Alba created a grave and inevitable risk of death. This affirmative interference with rescue objectively manifests extreme recklessness. Therefore, Alba's actions satisfy the actus reus and malice aforethought required for depraved-heart murder.
(b) Argument-for: The doctrine of transferred intent allows a defendant's malicious mens rea to be legally applied to an unintended victim. A student could argue that Alba possessed specific intent to cause severe bodily harm when knocking Dane unconscious. Because Cody's death was a direct, connected consequence of that intentional battery, Alba's malicious intent to harm Dane automatically transfers to the resulting death, satisfying the requirements for murder.
(c) Argument-for: Depraved-heart murder traditionally involves conduct that carries a staggeringly high risk of death, often associated with inherently dangerous instrumentalities like firing a gun into a crowd. A student could argue that merely moving a victim into a bathroom does not meet the extreme actus reus threshold. Thus, because the charge requires the use of a deadly weapon or similarly lethal instrument directed at the victim to demonstrate "depravity," Alba must be found not guilty.
(d) Argument-for: Murder convictions fundamentally rely on the presence of malice aforethought, which traditionally encompasses the specific intent to kill or cause grievous bodily harm. Moving Cody into a bathroom may demonstrate negligence or even recklessness, but it lacks explicit malice. A student could argue that without the specific purpose to cause Cody's death, Alba lacks the requisite specific intent for murder, precluding a guilty verdict.
(e) Argument-for: In criminal homicide, the defendant's act must be the primary "but-for" and proximate cause of death. Cody was actively dying from an independent physiological event—drug-induced respiratory failure. A student could argue that because the fatal mechanism was the overdose itself, Alba’s failure to rescue merely constituted a concurrent condition. Thus, the pre-existing fatal condition severs causation and prevents Alba from being legally responsible for the death.

Head-to-head: Option (a) cleanly identifies the correct application of the extreme indifference standard to affirmative interference with rescue. The distractors all rely on clear legal misunderstandings, but they vary in how rigidly they lock those misunderstandings behind absolute language. Option (b) explicitly uses "automatically transfers," and (c) uses the absolute constraint "requires." Options (d) and (e), however, lack explicit absolute modifiers. While they provide false legal rationales, they do not strictly adhere to the prompt's close-call standard requiring words like "solely because" or "categorically" to lock the falsifiable proposition.

Falsifiable claim per distractor:
- (b): "automatically transfers" — wrong because intent to commit a battery against one victim does not legally or automatically transfer to form the malice aforethought for the murder of a completely different victim.
- (c): "requires the use of a deadly weapon" — wrong because depraved-heart murder is based on the extreme recklessness of the conduct and mens rea, not a categorical requirement that a deadly weapon be used.
- (d): "because Alba did not harbor the specific purpose" — wrong because depraved-heart murder is an unintentional murder doctrine that explicitly does *not* require specific purpose or intent to kill.
- (e): "because Cody was already suffering from respiratory failure before Alba took any affirmative action" — wrong because hastening death or affirmatively preventing a rescue satisfies the causation element; pre-existing fatal conditions do not immunize a defendant.

Recommended fix: Add absolute locking words to (d) and (e) to meet the strict close-call standard. 
Edit (d) to: "Not guilty, solely because Alba did not harbor the specific purpose to cause Cody's death when moving him into the windowless bathroom."
Edit (e) to: "Not guilty, because Cody's pre-existing respiratory failure automatically breaks the chain of causation regardless of Alba's affirmative actions to prevent rescue."
-->
