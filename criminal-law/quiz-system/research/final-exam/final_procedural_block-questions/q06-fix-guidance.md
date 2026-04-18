# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q6.** Assume Marcus is charged with distributing fentanyl. He raises a mistake-of-fact defense, arguing he believed he was only distributing counterfeit Adderall. Will this succeed?

(a) Yes, because a genuine, good-faith mistake regarding the specific type of drug completely negates the mental state required for the severe felony conviction.
(b) Yes, because under the Model Penal Code, his liability must be categorically reduced to the misdemeanor grade of the specific offense he believed he was committing.
(c) No, because drug offenses typically apply strict liability to the specific substance type once the defendant knowingly possesses any illegal controlled substance. <!-- correct -->
(d) No, because his mistake was objectively unreasonable given his employment by a known criminal syndicate operating a major pill market on the East End.
(e) No, because mistake of fact is only a valid defense for specific intent crimes, and all narcotics distribution offenses are strict liability public welfare offenses.

**Answer:** (c)

**Explanation:** The correct answer is (c). In narcotics distribution cases, the mens rea requirement typically only demands that the defendant know they are possessing *a* controlled substance. Once that threshold is met, the defendant is strictly liable for the actual type and quantity of the drug they possess, creating a severe distributional asymmetry when the drug turns out to be deadlier (like fentanyl) than expected (Fact 6).

(a) is incorrect because the law does not require the prosecution to prove the defendant knew the exact chemical identity of the substance, only that it was a controlled substance.
(b) is incorrect because while the MPC has a grade-reduction mechanism for mistakes (MPC 2.04(2)), federal and state drug laws heavily reject this in favor of strict liability as to type and quantity.
(d) is incorrect because the defense fails as a matter of law regarding the strict liability element of drug type, regardless of whether the mistake was factually reasonable.
(e) is incorrect because narcotics distribution is not a pure strict liability public welfare offense; it requires the mens rea of knowing possession of a prohibited substance.

**Tags:** chapters: [10, 15], topics: [mistake-of-fact, mens-rea-fentanyl-asymmetry], difficulty: medium, cognitive: application

**Grounding:** Chapter 15 - Drugs and Guns > Mens rea asymmetry (type/quantity strict liability)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The phrase "counterfeit Adderall (a misdemeanor)" creates a fatal mens rea trap. If Marcus genuinely believes the pills are merely "counterfeit" (e.g., fake sugar or caffeine pills passed off as real, which constitutes a misbranding/fraud misdemeanor), he completely lacks the foundational mens rea required for narcotics distribution (e.g., *McFadden v. U.S.*, which requires knowing possession of *a* controlled substance). If he doesn't believe it is a controlled substance at all, his mistake-of-fact defense legally succeeds in negating the mens rea, invalidating answer (c).
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: The Q6 stem asks to assume Marcus is charged with completed "distributing," but Fact 5 and Q5 establish he was intercepted en route and only committed "attempt" (or possession with intent). This creates unnecessary factual friction between Q5 and Q6.
Recommended fix: Change the charge in the stem to "possession with intent to distribute fentanyl" (to perfectly align with Fact 5/Q5), and change his underlying belief in Fact 6 and the stem to a recognized lower-grade controlled substance, such as "Schedule IV sedatives (a lesser offense)." This ensures he holds the baseline mens rea required to trigger the strict-liability asymmetry tested in (c).
-->

## Issue 3 — argpass-opus

**Q6.** Assume Marcus is charged with distributing fentanyl. He raises a mistake-of-fact defense, arguing he believed he was only distributing counterfeit Adderall. Will this succeed?

(a) Yes, because a genuine, good-faith mistake regarding the specific type of drug completely negates the mental state required for the severe felony conviction.
(b) Yes, because under the Model Penal Code, his liability must be categorically reduced to the misdemeanor grade of the specific offense he believed he was committing.
(c) No, because drug offenses typically apply strict liability to the specific substance type once the defendant knowingly possesses any illegal controlled substance. <!-- correct -->
(d) No, because his mistake was objectively unreasonable given his employment by a known criminal syndicate operating a major pill market on the East End.
(e) No, because mistake of fact is only a valid defense for specific intent crimes, and all narcotics distribution offenses are strict liability public welfare offenses.

**Answer:** (c)

**Explanation:** The correct answer is (c). In narcotics distribution cases, the mens rea requirement typically only demands that the defendant know they are possessing *a* controlled substance. Once that threshold is met, the defendant is strictly liable for the actual type and quantity of the drug they possess, creating a severe distributional asymmetry when the drug turns out to be deadlier (like fentanyl) than expected (Fact 6).

(a) is incorrect because the law does not require the prosecution to prove the defendant knew the exact chemical identity of the substance, only that it was a controlled substance.
(b) is incorrect because while the MPC has a grade-reduction mechanism for mistakes (MPC 2.04(2)), federal and state drug laws heavily reject this in favor of strict liability as to type and quantity.
(d) is incorrect because the defense fails as a matter of law regarding the strict liability element of drug type, regardless of whether the mistake was factually reasonable.
(e) is incorrect because narcotics distribution is not a pure strict liability public welfare offense; it requires the mens rea of knowing possession of a prohibited substance.

**Tags:** chapters: [10, 15], topics: [mistake-of-fact, mens-rea-fentanyl-asymmetry], difficulty: medium, cognitive: application

**Grounding:** Chapter 15 - Drugs and Guns > Mens rea asymmetry (type/quantity strict liability)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that due process and the presumption of mens rea require the government to prove the defendant knew the specific facts that make his conduct subject to severe penalties. If he thought he was distributing Adderall, his lack of knowledge about the fentanyl means he lacks the precise mens rea for a fentanyl-specific conviction, meaning his mistake negates the required mental state.
(b) Argument-for: A student could point to the Model Penal Code § 2.04(2), which addresses situations where a defendant's mistake of fact still leaves them committing a lesser crime. Under this provision, the defense is available but the grade of the offense is reduced to the one the defendant believed he was committing, meaning he should only be liable for the lesser offense he intended.
(c) Argument-for: This reflects the legally correct standard in most jurisdictions, including federal law under *McFadden*. The mens rea requirement for drug distribution is satisfied if the defendant knows they are distributing *a* controlled substance. Once they have this general knowledge, courts apply strict liability regarding the specific chemical type and quantity of the drug, meaning the mistake defense fails.
(d) Argument-for: A student could argue that mistake of fact defenses generally require the mistake to be reasonable, particularly for general intent crimes. Since Marcus is assumed to be working in a major illicit pill market, believing the pills were merely Adderall is objectively unreasonable, meaning his defense must fail on those factual grounds.
(e) Argument-for: A student could argue that narcotics offenses originated as public welfare offenses designed to protect public health, which often dispense with mens rea entirely. Under this view, drug distribution is a strict liability crime in its entirety, meaning mistake of fact is categorically inapplicable because the offense does not require specific intent or knowledge.

Head-to-head: Option (c) correctly identifies that drug offenses apply strict liability to the specific substance type once knowing possession of a controlled substance is established. Option (a) is incorrect because the mistake does not "completely negate" the mental state; the defendant still knew it was a controlled substance. Option (b) misapplies the MPC by claiming it "must be categorically reduced to the misdemeanor grade," whereas distributing Adderall is typically a felony, not a misdemeanor. Option (e) is explicitly false in claiming that "all narcotics distribution offenses are strict liability public welfare offenses," as they require knowledge that the substance is illicit. Option (d) attempts to fail the defense based on objective unreasonableness and invents outside facts not found in the prompt, but it lacks an absolute claim locking its legal error.

Falsifiable claim per distractor:
- (a): "completely negates the mental state required" — wrong because knowing possession of *any* controlled substance satisfies the threshold mens rea.
- (b): "must be categorically reduced to the misdemeanor grade" — wrong because distributing Adderall is a felony, and MPC 2.04(2) reduces to the grade of the believed offense, not an automatic misdemeanor.
- (d): "because his mistake was objectively unreasonable" — wrong because reasonableness is legally irrelevant to the element of drug type, which carries strict liability; however, it lacks an absolute modifier.
- (e): "all narcotics distribution offenses are strict liability public welfare offenses" — wrong because they require the mens rea of knowing possession of a prohibited substance.

Recommended fix: Change (d) to lock the false legal premise with an absolute word and remove the unprompted facts. Example: "(d) No, because a mistake regarding specific drug type categorically fails as a defense unless the defendant proves the belief was objectively reasonable."
-->
