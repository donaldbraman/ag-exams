# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Assume Trey is charged with felony murder for Omar's death in a jurisdiction that strictly applies the "abstract-elements" test (as in California's *People v. Phillips*) to determine if a predicate felony is inherently dangerous. Which of the following is the most likely outcome?

(a) Not guilty, because the statutory definition of felony evasion could theoretically be violated in a non-dangerous manner, meaning it is not inherently dangerous in the abstract. <!-- correct -->
(b) Guilty, because driving 80 mph through a residential area during a police chase is factually dangerous to human life under the specific circumstances of its actual commission.
(c) Not guilty, because the crime of felony evasion has no independent felonious purpose beyond the violence that caused the death, and therefore merges entirely with the resulting homicide.
(d) Guilty, because any predicate felony that proximately results in a victim's death automatically satisfies the inherently dangerous requirement when applying the rigid contours of the abstract-elements test.
(e) Not guilty, because Trey's primary subjective intent was merely to escape apprehension rather than to harm pedestrians, meaning the underlying felony lacks the required malice aforethought element.

**Answer:** (a)

**Explanation:** (a) is correct. Under California's abstract-elements test (*People v. Phillips*), a court looks only at the statutory definition of the predicate felony, not the defendant's specific conduct. Because "willfully fleeing a pursuing police vehicle" can theoretically be done safely (e.g., driving exactly the speed limit while refusing to pull over), it is not inherently dangerous in the abstract. (b) is wrong because it applies the facts-as-committed test used in other jurisdictions, not the abstract test. (c) is wrong because evasion has an independent felonious purpose (escape) and does not merge like an assault. (d) is wrong because the abstract-elements test is a limiting doctrine, not an automatic inclusion rule. (e) is wrong because felony murder operates as a strict liability substitution for malice; the intent to commit the underlying felony is sufficient.

**Tags:** chapters: [14], topics: [felony murder, abstract-elements test, inherently dangerous], difficulty: medium, cognitive: application

**Grounding:** Chapter 14, elements-vs-facts-approach

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The stem completely omits the fact pattern. It introduces the characters "Trey" and "Omar" and the charge, but provides zero facts about Trey's actual conduct or the statutory definition of the underlying felony. A student is forced to reverse-engineer the facts (fleeing police, driving 80 mph, striking a pedestrian) entirely from the answer choices.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Insert the missing factual background into the stem before the call of the question. For example: "Trey refused to pull over for a police officer, attempting to evade apprehension by driving 80 mph through a residential area. During the chase, he struck and killed Omar, a pedestrian. The statutory definition of felony evasion in this state is 'willfully fleeing a pursuing police vehicle.' Assume Trey is charged..."
-->

## Issue 2 — argpass-opus

**Q5.** Assume Trey is charged with felony murder for Omar's death in a jurisdiction that strictly applies the "abstract-elements" test (as in California's *People v. Phillips*) to determine if a predicate felony is inherently dangerous. Which of the following is the most likely outcome?

(a) Not guilty, because the statutory definition of felony evasion could theoretically be violated in a non-dangerous manner, meaning it is not inherently dangerous in the abstract. <!-- correct -->
(b) Guilty, because driving 80 mph through a residential area during a police chase is factually dangerous to human life under the specific circumstances of its actual commission.
(c) Not guilty, because the crime of felony evasion has no independent felonious purpose beyond the violence that caused the death, and therefore merges entirely with the resulting homicide.
(d) Guilty, because any predicate felony that proximately results in a victim's death automatically satisfies the inherently dangerous requirement when applying the rigid contours of the abstract-elements test.
(e) Not guilty, because Trey's primary subjective intent was merely to escape apprehension rather than to harm pedestrians, meaning the underlying felony lacks the required malice aforethought element.

**Answer:** (a)

**Explanation:** (a) is correct. Under California's abstract-elements test (*People v. Phillips*), a court looks only at the statutory definition of the predicate felony, not the defendant's specific conduct. Because "willfully fleeing a pursuing police vehicle" can theoretically be done safely (e.g., driving exactly the speed limit while refusing to pull over), it is not inherently dangerous in the abstract. (b) is wrong because it applies the facts-as-committed test used in other jurisdictions, not the abstract test. (c) is wrong because evasion has an independent felonious purpose (escape) and does not merge like an assault. (d) is wrong because the abstract-elements test is a limiting doctrine, not an automatic inclusion rule. (e) is wrong because felony murder operates as a strict liability substitution for malice; the intent to commit the underlying felony is sufficient.

**Tags:** chapters: [14], topics: [felony murder, abstract-elements test, inherently dangerous], difficulty: medium, cognitive: application

**Grounding:** Chapter 14, elements-vs-facts-approach

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Option (a) accurately articulates the abstract-elements test from cases like *People v. Phillips*. Under this test, courts look strictly at the statutory elements of the predicate offense in the abstract, ignoring the defendant's actual conduct. If the statute can be violated in a way that does not inherently endanger human life—such as felony evasion accomplished by driving safely but simply refusing to stop—the felony is not inherently dangerous. Therefore, it cannot serve as a predicate for felony murder, making Trey not guilty.
(b) Argument-for: A student could argue that if a jurisdiction interprets the evasion statute narrowly, the act of "fleeing a pursuing police vehicle" inherently contemplates a high-speed chase, which is inherently dangerous. A student might assert that even under an abstract framework, courts recognize the inherent factual danger of specific statutorily prohibited acts. Because the 80 mph chase demonstrates a grave risk to human life, a student could conclude that the felony clearly satisfies the danger requirement, justifying a guilty verdict.
(c) Argument-for: A student could rely on the merger doctrine established in *People v. Ireland*, which bars felony murder if the predicate felony is an integral part of the homicide and lacks an independent felonious purpose. Because Trey's evasion culminated directly in the fatal violence against Omar, a student might argue the evasion was not independent of the vehicular assault that caused the death. If the evasion merges into the homicide, Trey cannot be convicted of felony murder, making (c) a plausible path to a not-guilty verdict.
(d) Argument-for: A student might view the abstract-elements test as a rigid proxy for causation rather than a substantive limitation. Under this view, if a felony proximately causes death, the law abstractly infers the inherent danger of the underlying felony from the resulting death itself. A student could argue that modern felony murder rules use the abstract test simply to categorically bridge the gap between the felony and the death, meaning any felony that foreseeably results in death automatically satisfies the requirement.
(e) Argument-for: A student could argue that felony murder, while a substitute for malice, still requires that the underlying felony itself reflect a sufficiently culpable mental state (a "malignant heart"). If Trey's subjective intent was solely to escape—a self-preservation motive lacking ill will toward Omar—the predicate felony lacks the malicious character required to support the felony murder fiction. Thus, without an inherently malicious motive, the felony murder rule cannot constitutionally or doctrinally apply.

Head-to-head: Option (a) is the only legally correct application of the abstract-elements test, recognizing that if a statute can theoretically be violated safely, it is not inherently dangerous in the abstract. Option (b) explicitly contradicts the prompt's mandate to use the abstract-elements test by assessing danger based on "the specific circumstances of its actual commission." Option (c) misstates the merger doctrine; felony evasion possesses a distinct independent purpose (escaping apprehension), meaning it does not merge. Option (d) incorrectly defines the abstract-elements test as an automatic inclusion rule based on proximate cause, whereas it operates as a limiting doctrine. Option (e) wrongly suggests that the defendant's subjective lack of intent to harm defeats the felony murder rule, whereas the rule operates precisely to substitute the mere intent to commit the felony for malice aforethought. 

Falsifiable claim per distractor:
- (b): "under the specific circumstances of its actual commission" — wrong because analyzing actual circumstances is the hallmark of the "facts-as-committed" test, which directly contradicts the prompt's instruction to apply the abstract-elements test.
- (c): "has no independent felonious purpose beyond the violence that caused the death" — wrong because the crime of evasion legally possesses an independent felonious purpose (to escape law enforcement), meaning it does not merge into the homicide.
- (d): "any predicate felony that proximately results in a victim's death automatically satisfies the inherently dangerous requirement" — wrong because the abstract-elements test requires analyzing the statutory elements for inherent danger, not automatically finding danger solely because proximate cause is established.
- (e): "meaning the underlying felony lacks the required malice aforethought element" — wrong because the felony murder rule strictly substitutes the intent to commit the underlying felony for malice aforethought, making the subjective intent to avoid harming pedestrians legally irrelevant.

Recommended fix: The question text is missing its preliminary fact pattern, forcing the reader to extract the facts retrospectively from the options. Insert a brief fact pattern at the beginning of the prompt: "Trey fled from pursuing police officers by driving his car 80 mph through a residential area. During the chase, Trey struck and killed Omar, a pedestrian. Assume Trey is charged with felony murder for Omar's death based on the predicate felony of evasion..."
-->
