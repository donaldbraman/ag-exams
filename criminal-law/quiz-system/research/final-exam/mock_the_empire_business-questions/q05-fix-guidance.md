# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Assuming Locke is charged with possession with intent to distribute 400 grams of fentanyl, which triggers a severe weight-based mandatory minimum sentence, is Locke guilty of the fentanyl offense?

(a) Yes, because Locke knew he was transporting a controlled substance, satisfying the mens rea element regardless of his mistake regarding the specific drug type. <!-- correct -->
(b) Yes, because federal drug statutes impose absolute strict liability for all elements, removing the need to prove any mental state regarding the crates' contents.
(c) No, because Locke genuinely believed he possessed oxycodone, and the government must prove he had specific knowledge of the exact substance identity.
(d) No, because applying a severe weight-based mandatory minimum for an unknowingly transported substance violates the constitutional proportionality doctrine.
(e) Yes, provided the government can prove that a reasonable person in Locke's position would have independently tested the crates to verify their contents.

**Answer:** (a)

**Explanation:** Under the *McFadden* general-nature rule and federal fentanyl asymmetry, the government only needs to prove the defendant knew the substance was a controlled substance. Because Locke knew he possessed oxycodone (a controlled substance), he is legally liable for the fentanyl he actually possessed and its resulting weight-based enhancements. (b) is wrong because the statute is not strict liability as to the general nature of the substance; the government must still prove he knew it was *some* kind of illegal drug. (c) is wrong because knowledge of the exact chemical identity of the substance is not required. (d) is wrong because courts routinely uphold weight-based mandatory minimums even when the defendant is mistaken about the drug's type or purity. (e) is wrong because the standard is not negligence (what a reasonable person would test for); his actual knowledge that it was oxycodone satisfies the mens rea.

**Tags:** chapters: [15], topics: [fentanyl asymmetry, mandatory minimums, McFadden], difficulty: hard, cognitive: application

**Grounding:** Chapter 15 - Fentanyl Substitution Problem and McFadden v. United States

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: The stem contains no facts about Locke's conduct or mental state. It completely omits the crucial factual premise that he was transporting crates and mistakenly believed they contained oxycodone. Students are forced to guess the scenario by reading the answer choices.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Insert the missing facts into the stem: "Locke is caught transporting crates containing 400 grams of fentanyl. He genuinely believed the crates contained oxycodone. Assuming Locke is charged..."
-->

## Issue 2 — argpass-opus

**Q5.** Assuming Locke is charged with possession with intent to distribute 400 grams of fentanyl, which triggers a severe weight-based mandatory minimum sentence, is Locke guilty of the fentanyl offense?

(a) Yes, because Locke knew he was transporting a controlled substance, satisfying the mens rea element regardless of his mistake regarding the specific drug type. <!-- correct -->
(b) Yes, because federal drug statutes impose absolute strict liability for all elements, removing the need to prove any mental state regarding the crates' contents.
(c) No, because Locke genuinely believed he possessed oxycodone, and the government must prove he had specific knowledge of the exact substance identity.
(d) No, because applying a severe weight-based mandatory minimum for an unknowingly transported substance violates the constitutional proportionality doctrine.
(e) Yes, provided the government can prove that a reasonable person in Locke's position would have independently tested the crates to verify their contents.

**Answer:** (a)

**Explanation:** Under the *McFadden* general-nature rule and federal fentanyl asymmetry, the government only needs to prove the defendant knew the substance was a controlled substance. Because Locke knew he possessed oxycodone (a controlled substance), he is legally liable for the fentanyl he actually possessed and its resulting weight-based enhancements. (b) is wrong because the statute is not strict liability as to the general nature of the substance; the government must still prove he knew it was *some* kind of illegal drug. (c) is wrong because knowledge of the exact chemical identity of the substance is not required. (d) is wrong because courts routinely uphold weight-based mandatory minimums even when the defendant is mistaken about the drug's type or purity. (e) is wrong because the standard is not negligence (what a reasonable person would test for); his actual knowledge that it was oxycodone satisfies the mens rea.

**Tags:** chapters: [15], topics: [fentanyl asymmetry, mandatory minimums, McFadden], difficulty: hard, cognitive: application

**Grounding:** Chapter 15 - Fentanyl Substitution Problem and McFadden v. United States

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under *McFadden v. United States*, the government satisfies the mens rea for a drug offense under 21 U.S.C. § 841 if it proves the defendant knew they possessed a controlled substance, even if they were mistaken about its specific identity. Since Locke knew he was transporting oxycodone—a Schedule II controlled substance—he possessed the requisite knowledge. The actual identity and weight of the drug (fentanyl) serve as sentencing factors or elements that do not require specific mens rea. Therefore, Locke is guilty and subject to the mandatory minimum regardless of his specific mistake.
(b) Argument-for: Drug trafficking statutes are designed to severely punish the distribution of dangerous narcotics. Courts could theoretically interpret the statutory scheme as a public welfare offense imposing absolute strict liability for all elements to maximize deterrence. Under this strict liability theory, the mere actus reus of transporting crates containing fentanyl would remove the need to prove any mental state regarding the crates' contents.
(c) Argument-for: Basic principles of criminal law suggest that a defendant's mens rea should align with the actus reus. When a statute imposes drastically different penalties based on the specific drug, one could argue under *Apprendi* and *Alleyne* that the drug's exact identity must be treated as an element of the offense subject to a specific knowledge requirement. Therefore, Locke lacks the requisite mens rea for fentanyl since he genuinely believed he possessed oxycodone.
(d) Argument-for: The Eighth Amendment prohibits cruel and unusual punishment, which encompasses a proportionality doctrine. Imposing a severe, weight-based mandatory minimum on a defendant for a highly potent drug they did not know they possessed could be seen as grossly disproportionate to their actual culpability. Thus, applying such an extreme penalty for unknowingly transported fentanyl violates constitutional proportionality limits.
(e) Argument-for: In cases involving the transportation of sealed containers, courts sometimes employ standards akin to willful blindness to establish mens rea. One could argue this standard allows for an objective negligence inquiry in heavily regulated contexts like drug trafficking. Under this theory, Locke could be held liable if a reasonable person in his position would have independently tested or verified the crates' contents.

Head-to-head: Option (a) accurately reflects the established rule from *McFadden v. United States*, making it the legally correct answer. Option (b) is demonstrably false because 21 U.S.C. § 841 explicitly requires a "knowing or intentional" mens rea; it does not impose "absolute strict liability for all elements." Option (c) is false because *McFadden* expressly rejects the notion that the government must prove knowledge of the "exact substance identity." Option (e) is legally false because the mens rea requirement under § 841 demands actual knowledge or subjective willful blindness, not an objective "reasonable person" standard. Option (d) presents a false statement of law (courts routinely uphold such mandatory minimums against Eighth Amendment challenges), but it lacks an absolute trigger word to firmly lock the legal proposition as categorically false per the close-call standard.

Falsifiable claim per distractor:
- (b): "impose absolute strict liability for all elements" — wrong because the statute explicitly includes a mens rea requirement ("knowing or intentional") for the base offense.
- (c): "must prove he had specific knowledge of the exact substance identity" — wrong because *McFadden* holds that knowledge that the substance is *any* controlled substance suffices.
- (d): "violates the constitutional proportionality doctrine" — wrong because courts have consistently rejected Eighth Amendment proportionality challenges to mandatory minimums based on unknowingly transported drug quantities, but it lacks an absolute word to strictly lock the falsehood.
- (e): "provided the government can prove that a reasonable person... would have independently tested" — wrong because the criminal mens rea standard is actual knowledge or willful blindness, not objective civil negligence.

Recommended fix: In (d), insert an absolute word to rigidly lock the falsifiable proposition. Change (d) to: "No, because categorically applying a severe weight-based mandatory minimum for an unknowingly transported substance automatically violates the constitutional proportionality doctrine."
-->
