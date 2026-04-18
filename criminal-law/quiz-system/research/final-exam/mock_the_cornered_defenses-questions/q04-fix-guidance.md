# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Assume Silas is charged with murder in a jurisdiction that requires the defendant to prove insanity. How would Silas fare under the M'Naghten and Model Penal Code (MPC) tests?

(a) He would satisfy M'Naghten because he failed to understand he was killing a human, but fail the MPC test because he physically controlled his weapon.
(b) He would fail M'Naghten because he consciously intended to fire the weapon, but satisfy the MPC test because his schizophrenia inherently compelled the fatal shooting.
(c) He would satisfy both tests because his intense delusion prevented him from understanding the nature of his act and appreciating its fundamental legal wrongfulness. <!-- correct -->
(d) He would fail both tests because his underlying motive was to protect the drug operation, demonstrating a rational awareness of the surrounding criminal enterprise.
(e) He would satisfy the MPC test strictly due to his medical history, but fail M'Naghten because he demonstrated consciousness of guilt by remaining upon arrest.

**Answer:** (c)

**Explanation:** Silas suffers from a severe delusion that he is shooting a "monster made of smoke." Under M'Naghten's first prong, this means he does not understand the nature and quality of his physical act (he does not know he is killing a human being). Because the MPC test is broader ("lacks substantial capacity to appreciate the criminality/wrongfulness of his conduct"), a defendant who satisfies M'Naghten's strict cognitive standard will almost universally satisfy the MPC's cognitive prong as well. (a) is incorrect because the MPC contains a cognitive prong ("appreciate") that Silas clearly meets; he does not need to rely solely on the volitional prong. (b) is incorrect because Silas easily satisfies M'Naghten by failing to recognize he is killing a human. (d) is incorrect because his delusion entirely overtook his perception of reality regarding the victim's identity. (e) is incorrect because remaining at the scene and bragging about slaying a monster demonstrates a lack of consciousness of guilt, further supporting his insanity claim under both tests.

**Tags:** chapters: [23], topics: [insanity, m'naghten, mpc, mental disease], difficulty: medium, cognitive: application

**Grounding:** Chapter 23: mnaghten-nature-quality, mpc-appreciate-criminality

<!-- audit: MUST FIX
check 1: pass (the legal analysis for the correct answer is accurate, assuming the facts were present)
check 2: pass
check 3: pass
check 4: fails - The stem is completely missing the factual scenario. There are no facts about Silas, his delusion of a "monster made of smoke," the drug operation, or his behavior upon arrest. The question is impossible to answer as written.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Add the missing fact pattern into the question stem (describing Silas's physical actions, his delusion about the smoke monster, the drug operation context, and his behavior at arrest).
-->

## Issue 2 — argpass-opus

**Q4.** Assume Silas is charged with murder in a jurisdiction that requires the defendant to prove insanity. How would Silas fare under the M'Naghten and Model Penal Code (MPC) tests?

(a) He would satisfy M'Naghten because he failed to understand he was killing a human, but fail the MPC test because he physically controlled his weapon.
(b) He would fail M'Naghten because he consciously intended to fire the weapon, but satisfy the MPC test because his schizophrenia inherently compelled the fatal shooting.
(c) He would satisfy both tests because his intense delusion prevented him from understanding the nature of his act and appreciating its fundamental legal wrongfulness. <!-- correct -->
(d) He would fail both tests because his underlying motive was to protect the drug operation, demonstrating a rational awareness of the surrounding criminal enterprise.
(e) He would satisfy the MPC test strictly due to his medical history, but fail M'Naghten because he demonstrated consciousness of guilt by remaining upon arrest.

**Answer:** (c)

**Explanation:** Silas suffers from a severe delusion that he is shooting a "monster made of smoke." Under M'Naghten's first prong, this means he does not understand the nature and quality of his physical act (he does not know he is killing a human being). Because the MPC test is broader ("lacks substantial capacity to appreciate the criminality/wrongfulness of his conduct"), a defendant who satisfies M'Naghten's strict cognitive standard will almost universally satisfy the MPC's cognitive prong as well. (a) is incorrect because the MPC contains a cognitive prong ("appreciate") that Silas clearly meets; he does not need to rely solely on the volitional prong. (b) is incorrect because Silas easily satisfies M'Naghten by failing to recognize he is killing a human. (d) is incorrect because his delusion entirely overtook his perception of reality regarding the victim's identity. (e) is incorrect because remaining at the scene and bragging about slaying a monster demonstrates a lack of consciousness of guilt, further supporting his insanity claim under both tests.

**Tags:** chapters: [23], topics: [insanity, m'naghten, mpc, mental disease], difficulty: medium, cognitive: application

**Grounding:** Chapter 23: mnaghten-nature-quality, mpc-appreciate-criminality

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Silas believed he was shooting a "monster made of smoke," meaning he did not comprehend the nature and quality of his act, squarely meeting the cognitive prong of M'Naghten. However, a student might incorrectly assume that under the MPC, physical control over a weapon demonstrates sufficient volitional capacity to defeat the insanity defense. Because Silas aimed and fired the weapon, this argument posits he retained behavioral control, thus causing him to fail the MPC test despite his delusions.
(b) Argument-for: M'Naghten's strict cognitive focus asks whether the defendant knew what they were doing physically. A student could argue that because Silas consciously intended to pull the trigger, he understood the mechanical nature of his act, thereby failing M'Naghten. Conversely, because the MPC includes a volitional prong, the argument asserts that Silas's severe schizophrenia inherently destroyed his volitional capacity, legally compelling the shooting and automatically satisfying the broader MPC test.
(c) Argument-for: Under M'Naghten, a defendant must not know the nature and quality of his act. Believing the victim was a smoke monster means Silas did not know he was shooting a human, unequivocally satisfying M'Naghten. The MPC standard is broader, requiring only a lack of "substantial capacity" to appreciate criminality. Because Silas's cognitive impairment is total under M'Naghten, it inherently satisfies the MPC's lower threshold for cognitive impairment, allowing him to easily satisfy both tests.
(d) Argument-for: Even though Silas suffered from a severe delusion, his underlying motive to protect a drug operation reveals a rational, goal-oriented mindset. Both M'Naghten and the MPC require the mental disease or defect to be the primary cause of the inability to understand or conform conduct. A student could logically argue that his rational awareness of the criminal enterprise demonstrates sufficient cognitive and volitional capacity, proving that his rational motive overrides the delusion and causes him to fail both tests.
(e) Argument-for: The MPC is generally viewed as a modern, medically informed standard. A student could argue that a documented severe medical history strictly satisfies the MPC's "mental disease or defect" requirement without needing further proof of cognitive or volitional incapacity. Meanwhile, under M'Naghten, a student might interpret his decision to remain at the scene as a rational awareness of submitting to authority, demonstrating a consciousness of his surroundings that contradicts the total cognitive disconnect required by M'Naghten.

Head-to-head: Option (c) flawlessly applies the legal standard, correctly recognizing that a delusion masking a victim's human identity easily satisfies the strict cognitive requirement of M'Naghten and, a fortiori, the broader MPC cognitive standard. Distractor (a) correctly applies M'Naghten but contains a falsifiable legal error regarding the MPC, ignoring that the MPC test is disjunctive (cognitive OR volitional) and misstating the volitional standard as mere physical control. Distractor (b) relies on a falsifiable claim that mere mechanical intent to fire a weapon defeats M'Naghten's qualitative requirement. Distractor (d) introduces a legally false application, implying that partial rationality categorically defeats insanity claims for specific, delusion-driven acts. Distractor (e) relies on the highly falsifiable claim that medical history alone strictly satisfies the MPC test. While the distractors contain identifiable legal errors, distractors (a) and (d) would benefit from absolute modifiers to lock their falsifiability and prevent students from arguing they merely reflect poor partial applications.

Falsifiable claim per distractor:
- (a): "fail the MPC test because he physically controlled his weapon" — wrong because the MPC test is disjunctive (he already satisfies the cognitive prong) and mere physical control of a weapon does not legally defeat the volitional prong.
- (b): "fail M'Naghten because he consciously intended to fire the weapon" — wrong because M'Naghten evaluates the qualitative nature of the act (shooting a human), not just the physical movement, and "inherently compelled" is a categorically false legal standard.
- (d): "fail both tests because his underlying motive... [demonstrated] a rational awareness" — wrong because partial rationality or a separate criminal enterprise does not legally negate an insanity defense if the specific actus reus was completely overridden by a qualifying delusion.
- (e): "satisfy the MPC test strictly due to his medical history" — wrong because the MPC always requires proving an impairment of substantial capacity (cognitive or volitional), not merely pointing to a medical diagnosis.

Recommended fix: Add absolute words to (a) and (d) to ensure their false claims are undeniably falsifiable. Change (a) to "...but fail the MPC test solely because he physically controlled his weapon." Change (d) to "He would automatically fail both tests because..."
-->
