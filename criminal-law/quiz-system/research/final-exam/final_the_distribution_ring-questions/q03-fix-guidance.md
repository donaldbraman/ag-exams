# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** Assume the jurisdiction has adopted the Model Penal Code approach to impossibility. Can Darius assert impossibility as a defense to attempted murder, given that the "silhouette" was actually a pile of trash bags?

(a) Yes, because it is legally impossible to murder trash bags, meaning his conduct could not constitute a crime even if successful.
(b) No, because the MPC abolished factual impossibility but retained the common law defense of legal impossibility, which applies here.
(c) Yes, because his acts did not create an actual danger to any human life, negating the actus reus requirement for attempted murder.
(d) No, because under the MPC, a defendant is guilty of attempt if the conduct would constitute the crime had the circumstances been as he believed them to be. <!-- correct -->
(e) Yes, because shooting a pile of trash bags is not a prohibited act under any statute, making this a pure legal impossibility.

**Answer:** (d)

**Explanation:** (d) is correct. The MPC largely abolishes the impossibility defense (both factual and hybrid legal) by evaluating the defendant's culpability based on the circumstances as they believed them to be. Since Darius believed the silhouette was a rival dealer, he is liable. (a) is incorrect because the MPC focuses on the defendant's subjective belief, not the objective reality. (b) is incorrect because the MPC essentially collapsed factual and hybrid legal impossibility. (c) is incorrect because actual danger is not required under the MPC's subjectively oriented framework. (e) is incorrect because "pure" legal impossibility (where the intended goal isn't a crime even in the defendant's mind) does not apply; Darius intended to commit murder, which is a crime.

**Tags:** chapters: [17], topics: [attempt, impossibility, mpc], difficulty: medium, cognitive: application

**Grounding:** Chapter 17: Attempts > Liability Limits > Impossibility MPC Abolition

<!-- audit: SHOULD FIX
check 1: pass
check 2: pass
check 3: The explanation misstates the doctrine of pure legal impossibility. It defines it as "(where the intended goal isn't a crime even in the defendant's mind)." This is incorrect: pure legal impossibility occurs when the defendant *does* believe their goal is a crime, but the criminal code simply does not prohibit that conduct.
check 4: pass
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Update the explanation for (e) to correct the definition: "(e) is incorrect because 'pure' legal impossibility (where the defendant's intended act is not actually prohibited by law, even though they mistakenly believe it is) does not apply; Darius's intended act—murdering a person—is explicitly a crime."
-->

## Issue 2 — edge-case

**Q3.** Assume the jurisdiction has adopted the Model Penal Code approach to impossibility. Can Darius assert impossibility as a defense to attempted murder, given that the "silhouette" was actually a pile of trash bags?

(a) Yes, because it is legally impossible to murder trash bags, meaning his conduct could not constitute a crime even if successful.
(b) No, because the MPC abolished factual impossibility but retained the common law defense of legal impossibility, which applies here.
(c) Yes, because his acts did not create an actual danger to any human life, negating the actus reus requirement for attempted murder.
(d) No, because under the MPC, a defendant is guilty of attempt if the conduct would constitute the crime had the circumstances been as he believed them to be. <!-- correct -->
(e) Yes, because shooting a pile of trash bags is not a prohibited act under any statute, making this a pure legal impossibility.

**Answer:** (d)

**Explanation:** (d) is correct. The MPC largely abolishes the impossibility defense (both factual and hybrid legal) by evaluating the defendant's culpability based on the circumstances as they believed them to be. Since Darius believed the silhouette was a rival dealer, he is liable. (a) is incorrect because the MPC focuses on the defendant's subjective belief, not the objective reality. (b) is incorrect because the MPC essentially collapsed factual and hybrid legal impossibility. (c) is incorrect because actual danger is not required under the MPC's subjectively oriented framework. (e) is incorrect because "pure" legal impossibility (where the intended goal isn't a crime even in the defendant's mind) does not apply; Darius intended to commit murder, which is a crime.

**Tags:** chapters: [17], topics: [attempt, impossibility, mpc], difficulty: medium, cognitive: application

**Grounding:** Chapter 17: Attempts > Liability Limits > Impossibility MPC Abolition

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Found. Option (d) explicitly relies on the MPC § 5.01(1)(a) standard for COMPLETED attempts ("conduct would constitute the crime"). However, Darius was intercepted 20 feet away without firing, making this an INCOMPLETE attempt governed by § 5.01(1)(c) (substantial step). Because merely walking toward a figure does not "constitute the crime" of murder even if the target were actually human, the rationale in correct answer (d) technically fails when applied to these specific facts.
2. Cross-Doctrine Clashes: Found. The stem tests impossibility regarding an "attempted murder" charge, which requires the specific intent to kill. The facts establish that Marcus merely ordered the crew to "Beat them down if you have to," and Darius was caught with an unspecified "weapon." This conduct only supports specific intent for battery or assault. Sharp students will realize the impossibility analysis is moot because the underlying mens rea for attempted murder is entirely lacking.
3. Cross-Question Spoilers: pass
Recommended fix: Amend the Q3 stem to cure the mens rea gap: "Assuming Darius possessed the specific intent to kill, can he assert impossibility..." Update Option (d) to accurately reflect the subjective standard for incomplete attempts: "(d) No, because under the MPC, attempt liability (including whether an act is a substantial step) is evaluated based on the circumstances as the defendant believed them to be."
-->

## Issue 3 — argpass-opus

**Q3.** Assume the jurisdiction has adopted the Model Penal Code approach to impossibility. Can Darius assert impossibility as a defense to attempted murder, given that the "silhouette" was actually a pile of trash bags?

(a) Yes, because it is legally impossible to murder trash bags, meaning his conduct could not constitute a crime even if successful.
(b) No, because the MPC abolished factual impossibility but retained the common law defense of legal impossibility, which applies here.
(c) Yes, because his acts did not create an actual danger to any human life, negating the actus reus requirement for attempted murder.
(d) No, because under the MPC, a defendant is guilty of attempt if the conduct would constitute the crime had the circumstances been as he believed them to be. <!-- correct -->
(e) Yes, because shooting a pile of trash bags is not a prohibited act under any statute, making this a pure legal impossibility.

**Answer:** (d)

**Explanation:** (d) is correct. The MPC largely abolishes the impossibility defense (both factual and hybrid legal) by evaluating the defendant's culpability based on the circumstances as they believed them to be. Since Darius believed the silhouette was a rival dealer, he is liable. (a) is incorrect because the MPC focuses on the defendant's subjective belief, not the objective reality. (b) is incorrect because the MPC essentially collapsed factual and hybrid legal impossibility. (c) is incorrect because actual danger is not required under the MPC's subjectively oriented framework. (e) is incorrect because "pure" legal impossibility (where the intended goal isn't a crime even in the defendant's mind) does not apply; Darius intended to commit murder, which is a crime.

**Tags:** chapters: [17], topics: [attempt, impossibility, mpc], difficulty: medium, cognitive: application

**Grounding:** Chapter 17: Attempts > Liability Limits > Impossibility MPC Abolition

<!-- argument-pass: MUST FIX
(a) Argument-for: A student might argue that even under modern statutes, courts recognize the impossibility of killing an inanimate object. If a defendant shoots an object rather than a person, the actus reus of homicide cannot be completed. Thus, because it is objectively impossible to murder trash bags, a student could conclude the conduct intrinsically fails to satisfy the elements of a crime, rendering it an absolute defense.
(b) Argument-for: A student could argue that the MPC retains the defense of "pure legal impossibility" (where the intended act is not a crime). They might conflate this concept with the scenario at hand, reasoning that the MPC abolished factual impossibility but kept a form of legal impossibility. Therefore, they could conclude that shooting a non-human object must trigger the retained legal impossibility defense.
(c) Argument-for: A student might point to the doctrine of inherent impossibility under MPC § 5.05(2), which allows a court to dismiss an attempt charge if the conduct is so inherently unlikely to culminate in a crime that it presents no public danger. Because shooting a pile of trash bags creates no actual danger to human life, a student could argue this lack of objective danger completely negates the actus reus requirement for attempt.
(d) Argument-for: This is the correct application of MPC § 5.01(1)(a). The MPC explicitly shifts the focus of attempt liability from objective reality to the defendant's subjective culpability. A person is guilty of an attempt if they purposefully engage in conduct that would constitute the crime if the attendant circumstances were as they believed them to be. Assuming Darius believed he was shooting a person, he perfectly satisfies the elements of attempted murder.
(e) Argument-for: A student could argue that the MPC's retention of "pure legal impossibility" stems from the principle of legality. Under this principle, a person cannot be convicted for attempting something that is not legally prohibited. Since no statute criminalizes shooting at trash bags, the objective act itself is perfectly legal, leading a student to mistakenly categorize this as pure legal impossibility.

Head-to-head: Option (d) correctly states the MPC rule for attempt, which bases liability on the circumstances as the defendant believed them to be, thereby abolishing traditional factual and hybrid legal impossibility defenses. However, the question prompt is missing the crucial facts (that Darius intended to kill a rival dealer) necessary to structurally support (d). Assuming those facts are inserted, (d) is clearly superior. The distractors are securely falsifiable: (a) incorrectly applies an objective impossibility standard under the MPC; (b) falsely claims the MPC retained common law legal impossibility; (c) incorrectly asserts that actual danger is required to satisfy the actus reus; and (e) mischaracterizes the scenario as "pure legal impossibility" (which requires the actor's *intended* goal to be lawful).

Falsifiable claim per distractor:
- (a): "Yes, because it is legally impossible to murder trash bags..." — wrong because under the MPC, objective impossibility does not provide a defense ("Yes" is definitively false); attempt liability is anchored to subjective belief.
- (b): "retained the common law defense of legal impossibility, which applies here" — wrong because the MPC explicitly abolished the common law distinction between factual and legal impossibility, and the defense does not apply here.
- (c): "negating the actus reus requirement for attempted murder" — wrong because the MPC attempt actus reus (a substantial step strongly corroborative of criminal purpose) does not require the creation of an actual danger to human life.
- (e): "making this a pure legal impossibility" — wrong because pure legal impossibility dictates that the defendant's intended end goal is not a crime, whereas here the intended goal was murder.

Recommended fix: MUST FIX. The question is missing the foundational fact pattern it relies upon (Darius's intent and belief), meaning it was likely pulled from a longer fact-pattern series. Add a sentence to the prompt to establish the scenario: "Darius, intending to kill a rival dealer, shot at a silhouette in a dark alley. The 'silhouette' turned out to be a pile of trash bags. Assume the jurisdiction has adopted the Model Penal Code approach to impossibility. Can Darius assert impossibility as a defense to attempted murder?"
-->
