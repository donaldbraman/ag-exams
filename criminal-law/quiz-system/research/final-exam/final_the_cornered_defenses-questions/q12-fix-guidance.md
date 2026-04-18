# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Silas is charged with attempted murder for lying in wait with his drawn firearm. How would his conduct be analyzed under the varying tests for attempt?

(a) He is guilty under both tests, because engaging in mere preparation is legally sufficient to establish a criminal attempt in all modern jurisdictions.
(b) He is guilty under the MPC's substantial step test, but might be acquitted under a common-law proximity test since he had not yet fired. <!-- correct -->
(c) He is guilty under the common-law proximity test, but would be acquitted under the substantial step test because he never fired a single shot.
(d) He is not guilty under either test, because he was inside a parked vehicle and therefore lacked the immediate physical capability to commit murder.
(e) He is not guilty under the substantial step test because the passing police officer's intervention creates a complete legal impossibility defense at trial.

**Answer:** (b)

**Explanation:** Under the MPC's substantial step test, lying in wait with a drawn weapon strongly corroborates criminal purpose and easily satisfies the actus reus requirement. Under the strict common-law proximity test, the defendant must be dangerously close to completion; sitting in a car before the victim even arrives at the door may fail this stricter standard. (a) is wrong because mere preparation is never sufficient for attempt in any jurisdiction. (c) is wrong because it flips the tests—the MPC is broader and more defendant-inclusive than the proximity test. (d) is wrong because physical location inside a vehicle does not inherently defeat the actus reus of attempt. (e) is wrong because police intervention creates a factual impossibility, not a legal impossibility, which is no defense.

**Tags:** chapters: [17], topics: [attempt, actus reus, substantial step], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 (Attempts), actus-reus-substantial-step and actus-reus-proximity-test refinements.

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass (the legal reasoning is sound, but reveals the missing facts issue below)
check 4: The stem is missing critical facts. It fails to mention that Silas was sitting inside a parked vehicle, that the victim hadn't arrived, or that a passing police officer intervened. Options (d) and (e), as well as the explanation, rely heavily on these phantom facts.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Add the missing factual context to the stem. For example: "Silas is sitting inside a parked vehicle outside his enemy's house, lying in wait with his drawn firearm. Before the victim arrives, a passing police officer notices the weapon and arrests Silas. Silas is charged with attempted murder. How would his conduct be analyzed under the varying tests for attempt?"
-->

## Issue 2 — edge-case

**Q12.** Silas is charged with attempted murder for lying in wait with his drawn firearm. How would his conduct be analyzed under the varying tests for attempt?

(a) He is guilty under both tests, because engaging in mere preparation is legally sufficient to establish a criminal attempt in all modern jurisdictions.
(b) He is guilty under the MPC's substantial step test, but might be acquitted under a common-law proximity test since he had not yet fired. <!-- correct -->
(c) He is guilty under the common-law proximity test, but would be acquitted under the substantial step test because he never fired a single shot.
(d) He is not guilty under either test, because he was inside a parked vehicle and therefore lacked the immediate physical capability to commit murder.
(e) He is not guilty under the substantial step test because the passing police officer's intervention creates a complete legal impossibility defense at trial.

**Answer:** (b)

**Explanation:** Under the MPC's substantial step test, lying in wait with a drawn weapon strongly corroborates criminal purpose and easily satisfies the actus reus requirement. Under the strict common-law proximity test, the defendant must be dangerously close to completion; sitting in a car before the victim even arrives at the door may fail this stricter standard. (a) is wrong because mere preparation is never sufficient for attempt in any jurisdiction. (c) is wrong because it flips the tests—the MPC is broader and more defendant-inclusive than the proximity test. (d) is wrong because physical location inside a vehicle does not inherently defeat the actus reus of attempt. (e) is wrong because police intervention creates a factual impossibility, not a legal impossibility, which is no defense.

**Tags:** chapters: [17], topics: [attempt, actus reus, substantial step], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 (Attempts), actus-reus-substantial-step and actus-reus-proximity-test refinements.

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Silas intends to shoot in perceived self-defense (Trey is an approaching hitman). Stating "He is guilty" of attempted murder in the correct option ignores the self-defense / imperfect self-defense claims that could either acquit him or mitigate the charge to attempted voluntary manslaughter.
3. Cross-Question Spoilers: Q13-Q15 directly test Silas's self-defense claims. Forcing the student to declare him definitively "guilty" of attempted murder in Q12 conflicts with the potential outcomes of the self-defense analysis in the subsequent questions.
Recommended fix: Change "He is guilty" to "His conduct satisfies the actus reus" in options (a), (b), and (c), and adjust the second halves to match (e.g., "...but might fail a common-law proximity test...").
-->

## Issue 3 — argpass-sonnet

**Q12.** Silas is charged with attempted murder for lying in wait with his drawn firearm. How would his conduct be analyzed under the varying tests for attempt?

(a) He is guilty under both tests, because engaging in mere preparation is legally sufficient to establish a criminal attempt in all modern jurisdictions.
(b) He is guilty under the MPC's substantial step test, but might be acquitted under a common-law proximity test since he had not yet fired. <!-- correct -->
(c) He is guilty under the common-law proximity test, but would be acquitted under the substantial step test because he never fired a single shot.
(d) He is not guilty under either test, because he was inside a parked vehicle and therefore lacked the immediate physical capability to commit murder.
(e) He is not guilty under the substantial step test because the passing police officer's intervention creates a complete legal impossibility defense at trial.

**Answer:** (b)

**Explanation:** Under the MPC's substantial step test, lying in wait with a drawn weapon strongly corroborates criminal purpose and easily satisfies the actus reus requirement. Under the strict common-law proximity test, the defendant must be dangerously close to completion; sitting in a car before the victim even arrives at the door may fail this stricter standard. (a) is wrong because mere preparation is never sufficient for attempt in any jurisdiction. (c) is wrong because it flips the tests—the MPC is broader and more defendant-inclusive than the proximity test. (d) is wrong because physical location inside a vehicle does not inherently defeat the actus reus of attempt. (e) is wrong because police intervention creates a factual impossibility, not a legal impossibility, which is no defense.

**Tags:** chapters: [17], topics: [attempt, actus reus, substantial step], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 (Attempts), actus-reus-substantial-step and actus-reus-proximity-test refinements.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under modern criminal justice policies, some jurisdictions have aggressively expanded the scope of attempt liability to prevent harm before it occurs. A student might argue that the MPC’s “substantial step” test essentially criminalizes conduct that the traditional common law would have labeled "mere preparation." Therefore, stating that mere preparation is legally sufficient in modern jurisdictions is just another way of describing the MPC's lower threshold. If one equates the MPC standard with criminalizing preparation, option (a) correctly concludes he is guilty under all modern tests.
(b) Argument-for: The Model Penal Code’s substantial step test explicitly designates "lying in wait" as conduct that can strongly corroborate the actor's criminal purpose, satisfying the actus reus. Consequently, Silas is guilty under the MPC. In contrast, the common-law dangerous proximity test requires the defendant to be dangerously close to completing the crime. Because Silas had merely drawn his firearm and had not yet fired or even encountered his victim, his conduct is likely too remote to satisfy the proximity test, making option (b) the legally correct analysis.
(c) Argument-for: A student could argue that lying in wait with a drawn firearm puts Silas in such immediate physical proximity to the intended attack that it satisfies the strict common-law proximity test. However, under the MPC, one might argue that a "substantial step" requires an overt action directly towards the victim's person, rather than just waiting. Under this inverted understanding, Silas would pass the proximity threshold but fail the substantial step test because he never fired a shot, justifying option (c).
(d) Argument-for: Attempt liability requires the defendant to have the apparent ability to complete the crime. A student might reason that being inside a parked vehicle inherently restricts Silas’s line of sight and physical mobility, preventing him from immediately carrying out the murder. Because this physical barrier negates his immediate capability to complete the offense, he cannot be deemed dangerously close or to have taken a substantial step. Thus, option (d) is correct because his location defeats the actus reus under either test.
(e) Argument-for: When a passing police officer intervenes, the completion of the crime is prevented by legal authority. A student could mistakenly categorize this intervention as "legal impossibility" because a legal actor (the police) made the crime impossible to complete. Since legal impossibility is traditionally recognized as a valid defense, the student could argue that the officer's presence provides Silas with a complete defense to the attempt charge under the substantial step test, making option (e) the right answer.

Head-to-head: Option (b) is the clear winner as it accurately maps the facts to the differing legal standards: lying in wait is an explicit MPC substantial step, but may not satisfy the strict common-law proximity test. The distractors all hinge on explicitly false legal rules. Option (a) falsifies the baseline standard by claiming mere preparation is sufficient everywhere. Option (c) falsifies the MPC test by asserting a shot must be fired. Option (d) incorrectly asserts that being in a vehicle categorically negates physical capability. Option (e) mischaracterizes police intervention as legal, rather than factual, impossibility. However, the question stem completely fails to mention the "parked vehicle" and "passing police officer" facts relied upon by (d) and (e), which forces students to guess whether they missed facts or if the distractors are improperly importing them. I will flag this SHOULD FIX to add these missing facts into the stem.

Falsifiable claim per distractor:
- (a): "engaging in mere preparation is legally sufficient to establish a criminal attempt in all modern jurisdictions." — wrong because mere preparation is universally insufficient; both common law and MPC draw the line strictly past mere preparation.
- (c): "would be acquitted under the substantial step test because he never fired a single shot." — wrong because the MPC specifically lists "lying in wait" as a substantial step; firing a shot is categorically not required.
- (d): "he was inside a parked vehicle and therefore lacked the immediate physical capability to commit murder." — wrong because being inside a vehicle does not categorically negate the physical capability or the actus reus of attempt.
- (e): "the passing police officer's intervention creates a complete legal impossibility defense" — wrong because police intervention is a textbook example of factual impossibility (or simply being thwarted), which is not a defense.

Recommended fix: Update the question stem to introduce the facts referenced in options (d) and (e) and the explanation. Change the first sentence to: "Silas is charged with attempted murder after being thwarted by a passing police officer while lying in wait inside a parked vehicle with his drawn firearm."
-->

## Issue 4 — argpass-opus

**Q12.** Silas is charged with attempted murder for lying in wait with his drawn firearm. How would his conduct be analyzed under the varying tests for attempt?

(a) He is guilty under both tests, because engaging in mere preparation is legally sufficient to establish a criminal attempt in all modern jurisdictions.
(b) He is guilty under the MPC's substantial step test, but might be acquitted under a common-law proximity test since he had not yet fired. <!-- correct -->
(c) He is guilty under the common-law proximity test, but would be acquitted under the substantial step test because he never fired a single shot.
(d) He is not guilty under either test, because he was inside a parked vehicle and therefore lacked the immediate physical capability to commit murder.
(e) He is not guilty under the substantial step test because the passing police officer's intervention creates a complete legal impossibility defense at trial.

**Answer:** (b)

**Explanation:** Under the MPC's substantial step test, lying in wait with a drawn weapon strongly corroborates criminal purpose and easily satisfies the actus reus requirement. Under the strict common-law proximity test, the defendant must be dangerously close to completion; sitting in a car before the victim even arrives at the door may fail this stricter standard. (a) is wrong because mere preparation is never sufficient for attempt in any jurisdiction. (c) is wrong because it flips the tests—the MPC is broader and more defendant-inclusive than the proximity test. (d) is wrong because physical location inside a vehicle does not inherently defeat the actus reus of attempt. (e) is wrong because police intervention creates a factual impossibility, not a legal impossibility, which is no defense.

**Tags:** chapters: [17], topics: [attempt, actus reus, substantial step], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 (Attempts), actus-reus-substantial-step and actus-reus-proximity-test refinements.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that modern attempt law has expanded significantly to criminalize early stages of conduct to prevent harm. If "lying in wait" is considered sufficiently dangerous, a student might mistakenly believe that modern jurisdictions have categorically collapsed the preparation/attempt distinction, effectively making mere preparation legally sufficient to establish liability.
(b) Argument-for: This accurately applies the Model Penal Code and common-law frameworks. Under MPC § 5.01, lying in wait is an enumerated example of a "substantial step" that strongly corroborates the actor's criminal purpose. However, under the stricter common-law "dangerous proximity" or "physical proximity" tests, courts require the defendant to have the present ability to complete the crime and be immediately proximate to the harm. Because Silas had not yet fired or engaged his target, a proximity jurisdiction might find his actions too remote.
(c) Argument-for: A student might argue that under a strict reading of "lying in wait," the physical proximity test is met because he is at the scene with a drawn weapon, satisfying the common law requirement of being dangerously close. Conversely, the student might mistakenly believe the MPC categorically requires an overt act that goes beyond mere waiting (such as firing) to constitute a substantial step, leading to an acquittal under the MPC.
(d) Argument-for: If Silas is confined inside a parked vehicle, he may lack a clear line of sight or the physical ability to immediately execute the murder. A student could argue that under either the MPC or common law, being enclosed in a vehicle categorically negates the immediate physical capability required to satisfy the actus reus of attempt, leading to an automatic acquittal.
(e) Argument-for: A student could argue that when an outside force, such as a passing police officer, intervenes before the defendant can complete the offense, it frustrates the legal elements of the completed crime. If the jurisdiction recognizes broad impossibility defenses, the student might mistakenly classify police intervention as creating legal impossibility rather than factual impossibility, thereby defeating the substantial step.

Head-to-head: Option (b) is clearly the keyed correct answer because it correctly juxtaposes the MPC's specific inclusion of "lying in wait" as a substantial step against the much stricter common-law proximity test. Distractors (a), (c), (d), and (e) all fail because they rely on definitively false legal rules (e.g., mere preparation is sufficient, MPC requires firing a shot, factual impossibility equals legal impossibility). However, options (d) and (e), as well as the explanation, rely on facts (a parked vehicle, a passing police officer) that do not appear anywhere in the question stem, requiring students to guess at unstated premises. 

Falsifiable claim per distractor:
- (a): "engaging in mere preparation is legally sufficient to establish a criminal attempt in all modern jurisdictions." — wrong because mere preparation is universally and categorically insufficient for attempt liability under both common law and the MPC.
- (c): "would be acquitted under the substantial step test because he never fired a single shot." — wrong because the MPC's substantial step test explicitly includes "lying in wait" as sufficient and categorically does not require firing a shot.
- (d): "because he was inside a parked vehicle and therefore lacked the immediate physical capability to commit murder." — wrong because physical location inside a vehicle does not categorically defeat the physical capability to commit murder (e.g., drive-by shootings).
- (e): "because the passing police officer's intervention creates a complete legal impossibility defense at trial." — wrong because police intervention is a classic textbook example of factual impossibility, which is legally no defense at all.

Recommended fix: Amend the question stem to include the facts referenced in the distractors and the explanation. For example: "Silas is charged with attempted murder after he was discovered lying in wait with his drawn firearm inside a parked vehicle by a passing police officer." The legal claims within the distractors are beautifully falsifiable and need no edits.
-->
