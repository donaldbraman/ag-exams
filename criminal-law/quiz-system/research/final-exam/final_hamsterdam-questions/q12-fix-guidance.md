# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Assume Yasmin's condition qualifies as a mental disease. Under the M'Naghten test, does Yasmin's hallucination that God commanded the killing excuse her conduct?

(a) Yes, because her delusion that God commanded the killing to achieve a moral good prevented her from knowing the act was legally or morally wrong. <!-- correct -->
(b) No, because she successfully formulated the physical intent to strike the clerk with the tire iron, demonstrating clear cognitive capacity.
(c) Yes, because the intense pain from her gunshot wound created an irresistible impulse that destroyed her ability to conform her conduct.
(d) No, because bludgeoning a person to death is an inherently wrongful act that categorically precludes any subjective claim of moral ignorance.
(e) Yes, because taking the car keys demonstrates she lacked the substantial capacity to appreciate the overall criminality of her conduct.

**Answer:** (a)

**Explanation:** The second prong of the M'Naghten test asks whether the defendant, due to mental disease, did not know the act was wrong. The classic application of this prong is a delusional defendant who believes God commanded the killing (Fact 12); such a defendant lacks cognitive awareness of the act's moral wrongfulness. (b) confuses the two M'Naghten prongs; formulating intent to strike relates to knowing the nature and quality of the physical act, but she still failed to know it was *wrong*. (c) applies the irresistible impulse test (a volitional standard), not the M'Naghten cognitive test requested by the prompt. (d) is legally incorrect; the insanity defense exists precisely for defendants whose severe delusions blind them to the inherent wrongfulness of an act. (e) applies the Model Penal Code's "substantial capacity to appreciate" standard, not the strict M'Naghten test requested.

**Tags:** chapters: [23], topics: [insanity defense, M'Naghten, moral wrongness], difficulty: medium, cognitive: application

**Grounding:** Chapter 23, M'Naghten Wrongness Prong (mnaghten-wrongness)

<!-- audit: SHOULD FIX
Check 1: Option (a) asserts the delusion prevented Yasmin from knowing the act was "legally or morally wrong." However, the hallmark of the deific decree exception is that it excuses the defendant *even if* they know the act is legally wrong (i.e., illegal), because God's command nullifies their appreciation of moral wrongness. Stating she didn't know it was legally wrong is typically factually inaccurate in these scenarios.
Check 2: pass
Check 3: The explanation correctly notes that a deific decree defendant "lacks cognitive awareness of the act's moral wrongfulness." This contradicts option (a)'s inclusion of "legally or...".
Check 4: pass (assuming facts like the tire iron, clerk, and gunshot wound are established in a shared master fact pattern).
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Edit option (a) to remove "legally or", so it reads: "Yes, because her delusion that God commanded the killing to achieve a moral good prevented her from knowing the act was morally wrong."
-->

## Issue 2 — argpass-sonnet

**Q12.** Assume Yasmin's condition qualifies as a mental disease. Under the M'Naghten test, does Yasmin's hallucination that God commanded the killing excuse her conduct?

(a) Yes, because her delusion that God commanded the killing to achieve a moral good prevented her from knowing the act was legally or morally wrong. <!-- correct -->
(b) No, because she successfully formulated the physical intent to strike the clerk with the tire iron, demonstrating clear cognitive capacity.
(c) Yes, because the intense pain from her gunshot wound created an irresistible impulse that destroyed her ability to conform her conduct.
(d) No, because bludgeoning a person to death is an inherently wrongful act that categorically precludes any subjective claim of moral ignorance.
(e) Yes, because taking the car keys demonstrates she lacked the substantial capacity to appreciate the overall criminality of her conduct.

**Answer:** (a)

**Explanation:** The second prong of the M'Naghten test asks whether the defendant, due to mental disease, did not know the act was wrong. The classic application of this prong is a delusional defendant who believes God commanded the killing (Fact 12); such a defendant lacks cognitive awareness of the act's moral wrongfulness. (b) confuses the two M'Naghten prongs; formulating intent to strike relates to knowing the nature and quality of the physical act, but she still failed to know it was *wrong*. (c) applies the irresistible impulse test (a volitional standard), not the M'Naghten cognitive test requested by the prompt. (d) is legally incorrect; the insanity defense exists precisely for defendants whose severe delusions blind them to the inherent wrongfulness of an act. (e) applies the Model Penal Code's "substantial capacity to appreciate" standard, not the strict M'Naghten test requested.

**Tags:** chapters: [23], topics: [insanity defense, M'Naghten, moral wrongness], difficulty: medium, cognitive: application

**Grounding:** Chapter 23, M'Naghten Wrongness Prong (mnaghten-wrongness)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the M'Naghten test, a defendant is excused if a mental disease prevents them from knowing the nature of their act or knowing that it was wrong. The "deific decree" doctrine establishes that a defendant who hallucinates a command from God believes their action is morally justified. Consequently, this specific delusion perfectly satisfies the wrongness prong, as Yasmin genuinely did not know her conduct was legally or morally wrong. This accurately applies the requested legal standard to the facts.
(b) Argument-for: The first prong of M'Naghten focuses on the defendant's awareness of the "nature and quality" of the physical act. A student could argue that because Yasmin formulated the specific intent to strike the clerk with a tire iron, she clearly understood the physical reality of what she was doing. They might wrongly conclude that this baseline cognitive awareness of the physical act inherently defeats an insanity claim, believing that physical intent equates to complete legal sanity.
(c) Argument-for: A student might argue that severe physical trauma can trigger a psychological break that forces a person to act against their will. If the pain from a gunshot wound caused Yasmin to lose control, they could frame this as an "irresistible impulse." This relies on a well-known volitional insanity standard, and a student might mistakenly believe this standard is part of or interchangeable with M'Naghten.
(d) Argument-for: M'Naghten requires the defendant to not know the act is wrong. A student could argue that bludgeoning a person to death is universally understood as malum in se (inherently wrongful). Under this reasoning, the sheer brutality of the act categorically overrides any subjective claim of moral ignorance, leading a student to conclude that extreme violence strictly precludes the M'Naghten defense regardless of delusions.
(e) Argument-for: A student could argue that insanity is determined by evaluating the defendant's overall capacity to appreciate their actions. The fact that Yasmin took the car keys shows some level of organized thought, but a student might argue this highlights her diminished state and lack of "substantial capacity" to grasp the full criminality of her behavior. This argument uses the Model Penal Code framework, which a student might confuse with M'Naghten.

Head-to-head: Option (a) is definitively correct because a deific decree maps directly onto the M'Naghten wrongness prong. Distractor (c) explicitly relies on a volitional test ("irresistible impulse"), which contradicts the prompt's restriction to the cognitive M'Naghten test. Distractor (d) makes an explicitly false categorical claim that inherently wrongful acts preclude the defense. Distractor (e) applies the wrong legal framework entirely by using MPC terminology ("substantial capacity"). Distractor (b) correctly notes she formulated physical intent, but incorrectly concludes this mandates a "No" outcome; however, because it relies on an implicit assumption (that physical intent defeats the wrongness prong), it should be fortified with an absolute word to ensure it explicitly violates the close-call standard. 

Falsifiable claim per distractor:
- (b): "she successfully formulated the physical intent... demonstrating clear cognitive capacity" — wrong because under M'Naghten, demonstrating cognitive capacity over the physical act does not preclude the defense if the separate wrongness prong is met. (Needs an absolute word to lock the falsifiability).
- (c): "created an irresistible impulse that destroyed her ability to conform her conduct" — wrong because it explicitly invokes the volitional "irresistible impulse" standard, not M'Naghten.
- (d): "categorically precludes any subjective claim of moral ignorance" — wrong because M'Naghten specifically exists to evaluate subjective claims of moral ignorance driven by mental disease, even for malum in se crimes.
- (e): "lacked the substantial capacity to appreciate the overall criminality" — wrong because it explicitly uses the Model Penal Code test language rather than M'Naghten's strict "did not know" cognitive standard.

Recommended fix: Change (b) to: "No, solely because successfully formulating the physical intent to strike the clerk with the tire iron automatically demonstrates sufficient cognitive capacity to preclude the defense."
-->

## Issue 3 — argpass-opus

**Q12.** Assume Yasmin's condition qualifies as a mental disease. Under the M'Naghten test, does Yasmin's hallucination that God commanded the killing excuse her conduct?

(a) Yes, because her delusion that God commanded the killing to achieve a moral good prevented her from knowing the act was legally or morally wrong. <!-- correct -->
(b) No, because she successfully formulated the physical intent to strike the clerk with the tire iron, demonstrating clear cognitive capacity.
(c) Yes, because the intense pain from her gunshot wound created an irresistible impulse that destroyed her ability to conform her conduct.
(d) No, because bludgeoning a person to death is an inherently wrongful act that categorically precludes any subjective claim of moral ignorance.
(e) Yes, because taking the car keys demonstrates she lacked the substantial capacity to appreciate the overall criminality of her conduct.

**Answer:** (a)

**Explanation:** The second prong of the M'Naghten test asks whether the defendant, due to mental disease, did not know the act was wrong. The classic application of this prong is a delusional defendant who believes God commanded the killing (Fact 12); such a defendant lacks cognitive awareness of the act's moral wrongfulness. (b) confuses the two M'Naghten prongs; formulating intent to strike relates to knowing the nature and quality of the physical act, but she still failed to know it was *wrong*. (c) applies the irresistible impulse test (a volitional standard), not the M'Naghten cognitive test requested by the prompt. (d) is legally incorrect; the insanity defense exists precisely for defendants whose severe delusions blind them to the inherent wrongfulness of an act. (e) applies the Model Penal Code's "substantial capacity to appreciate" standard, not the strict M'Naghten test requested.

**Tags:** chapters: [23], topics: [insanity defense, M'Naghten, moral wrongness], difficulty: medium, cognitive: application

**Grounding:** Chapter 23, M'Naghten Wrongness Prong (mnaghten-wrongness)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the M'Naghten test, a defendant is excused if a mental disease prevents them from knowing their act is wrong. The "deific decree" delusion is the quintessential example of this exact cognitive failure. A defendant who genuinely believes God commanded their actions cannot comprehend that the act is morally (or sometimes legally) wrong. Therefore, this option perfectly applies M'Naghten to the specific hallucination, providing a legally sound justification for the excuse.
(b) Argument-for: A student could argue that M'Naghten is a strict cognitive test focusing heavily on the nature and quality of the physical act. Because Yasmin successfully formed the physical intent to strike the clerk, she possessed baseline cognitive awareness of what she was doing mechanically. A student might argue that this clear intent to strike demonstrates sufficient cognitive capacity to negate insanity. Thus, her physical volition serves as proof that she does not meet the high threshold for cognitive impairment.
(c) Argument-for: An argument can be made based on the severity of the circumstances destroying volitional control. If Yasmin was in intense pain from a gunshot wound, a student might argue this generated an irresistible impulse that nullified her capacity to conform her conduct. Though traditionally a distinct defense test, a student might reason that severe physical trauma operates under M'Naghten to destroy cognition and volition alike. Therefore, her conduct is legally excused due to an overriding impairment.
(d) Argument-for: Under this view, some acts are *malum in se* (inherently wrongful) to such a degree that subjective delusions cannot legally overcome their objective wrongness. A student might argue that bludgeoning someone to death is so categorically egregious that the law imposes an irrebuttable presumption of moral knowledge. This would preclude any subjective M'Naghten defense based on moral ignorance. Thus, the extreme objective nature of the act automatically overrides her subjective excuse.
(e) Argument-for: A student could argue that taking the car keys demonstrates a focused objective that highlights her mental state during the crime. Applying the "substantial capacity" standard, the student might view this test as the overarching, modern equivalent used to evaluate insanity in most jurisdictions today. Under this framework, her actions with the keys provide factual proof she lacked the requisite capacity to appreciate the broader criminality. Therefore, this option successfully matches the facts to a valid insanity doctrine.

Head-to-head: Option (a) correctly applies the disjunctive M'Naghten "wrongfulness" prong to a deific decree delusion, making it the clear key. Options (c) and (e) are trivially falsifiable because they explicitly cite the wrong legal tests ("irresistible impulse" and "substantial capacity") while the prompt strictly mandates the M'Naghten test. Option (d) contains a highly effective falsifiable claim by explicitly asserting that inherently wrongful acts "categorically preclude" a subjective claim, which is factually false under M'Naghten doctrine. Option (b), however, relies on an implicit omission: it argues that physical intent demonstrates "clear cognitive capacity," failing to recognize the wrongness prong, but it lacks an absolute trigger word to make the claim strictly and independently falsifiable under the close-call standard.

Falsifiable claim per distractor:
- (b): "demonstrating clear cognitive capacity" — wrong because forming physical intent only addresses the "nature and quality" prong; it does not universally demonstrate the total cognitive capacity required to defeat the disjunctive M'Naghten test, but it relies on an implicit omission of the second prong rather than a falsifiable absolute.
- (c): "created an irresistible impulse" — wrong because it explicitly cites the volitional irresistible impulse test, whereas the prompt strictly limits the inquiry to the M'Naghten test.
- (d): "categorically precludes any subjective claim" — wrong because the M'Naghten defense is specifically designed to evaluate and allow subjective claims of moral ignorance, even for inherently wrongful acts like murder.
- (e): "lacked the substantial capacity" — wrong because it explicitly invokes the Model Penal Code standard, which is legally distinct from the required M'Naghten test.

Recommended fix: Add an absolute modifier to (b) to lock the error. Change (b) to: "No, because she successfully formulated the physical intent to strike the clerk with the tire iron, which automatically demonstrates the clear cognitive capacity required to defeat a M'Naghten defense."
-->
