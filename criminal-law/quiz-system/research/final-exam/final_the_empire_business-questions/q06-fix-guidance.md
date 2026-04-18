# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

## The Question

**Q6.** Can Kevin successfully defend against the felon-in-possession charge based on his attorney's 2018 email?

(a) Guilty, because a defendant's ignorance of the law is never a valid defense to a federal firearms charge under traditional strict liability doctrines.
(b) Not guilty, because his genuine belief that he only had a misdemeanor conviction directly negates the required knowledge of his prohibited status. <!-- correct -->
(c) Guilty, because the defense attorney's private email does not legally qualify as an official statement of the law to support a reliance defense.
(d) Not guilty, because relying on the advice of private legal counsel automatically immunizes a criminal defendant from all federal felony liability.
(e) Guilty, because the actual statutory penalty for his prior state offense strictly establishes his prohibited status regardless of his personal beliefs.

**Answer:** (b)

**Explanation:** Under Rehaif v. United States, the government must prove the defendant knew he belonged to the relevant prohibited category (i.e., that he had a qualifying felony conviction). Kevin's genuine belief that his conviction was a misdemeanor negates this required mens rea. Option (a) fails because Rehaif explicitly displaced the traditional strict liability approach for the status element in this statute. Option (c) fails because Kevin does not need the affirmative "official statement" reliance defense; his mistake directly negates the statutory mens rea element. Option (d) fails because advice of counsel is not a blanket immunity doctrine. Option (e) fails because establishing the objective fact of the penalty is insufficient without proving the defendant's subjective knowledge of it.

**Tags:** chapters: [10, 15], topics: [Rehaif knowledge requirement, mistake of law, status element], difficulty: medium, cognitive: application

**Grounding:** Chapter 10 (Rehaif v. United States)

<!-- audit: MUST FIX
check 1: pass (accurately applies Rehaif v. United States regarding knowledge of status)
check 2: pass (distractors are well-designed conceptually, assuming facts exist)
check 3: pass (explanation accurately states the Rehaif rule)
check 4: fail (The entire fact pattern/stem is missing from the provided text. The question references "Kevin," "his attorney's 2018 email," and a "prior state offense," but no facts are provided to establish these elements.)
check 5: pass (federal statute, clear jurisdiction)
check 6: pass
check 7: pass
check 8: pass (options are well-balanced and symmetrical in length)
Recommended fix: Prepend the missing fact pattern to the question stub so students have the necessary context regarding Kevin, his conviction, and the attorney's email.
-->

## Issue 2 — edge-case

**Q6.** Can Kevin successfully defend against the felon-in-possession charge based on his attorney's 2018 email?

(a) Guilty, because a defendant's ignorance of the law is never a valid defense to a federal firearms charge under traditional strict liability doctrines.
(b) Not guilty, because his genuine belief that he only had a misdemeanor conviction directly negates the required knowledge of his prohibited status. <!-- correct -->
(c) Guilty, because the defense attorney's private email does not legally qualify as an official statement of the law to support a reliance defense.
(d) Not guilty, because relying on the advice of private legal counsel automatically immunizes a criminal defendant from all federal felony liability.
(e) Guilty, because the actual statutory penalty for his prior state offense strictly establishes his prohibited status regardless of his personal beliefs.

**Answer:** (b)

**Explanation:** Under Rehaif v. United States, the government must prove the defendant knew he belonged to the relevant prohibited category (i.e., that he had a qualifying felony conviction). Kevin's genuine belief that his conviction was a misdemeanor negates this required mens rea. Option (a) fails because Rehaif explicitly displaced the traditional strict liability approach for the status element in this statute. Option (c) fails because Kevin does not need the affirmative "official statement" reliance defense; his mistake directly negates the statutory mens rea element. Option (d) fails because advice of counsel is not a blanket immunity doctrine. Option (e) fails because establishing the objective fact of the penalty is insufficient without proving the defendant's subjective knowledge of it.

**Tags:** chapters: [10, 15], topics: [Rehaif knowledge requirement, mistake of law, status element], difficulty: medium, cognitive: application

**Grounding:** Chapter 10 (Rehaif v. United States)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Found. There are two statutory traps in the facts regarding 18 U.S.C. § 921(a)(20). First, Fact 8 sets the max penalty at 18 months, and Fact 9 labels it a "misdemeanor." Under § 921(a)(20)(B), state misdemeanors punishable by 2 years or less are expressly exempt from being federal qualifying offenses. An intermediate student who knows *Rehaif* requires knowledge of the penalty length (>1 year)—but who is unaware of this obscure 2-year misdemeanor exception—will assume Kevin's knowledge of the 18-month penalty satisfies the mens rea, leading them to wrongly reject (b). Second, the conviction is for "commercial fraud," which flirts dangerously with the § 921(a)(20)(A) exemption for offenses "relating to the regulation of business practices." Both create unintended legal ambiguities that derail a standard *Rehaif* analysis.
2. Cross-Doctrine Clashes: pass.
3. Cross-Question Spoilers: pass.
Recommended fix: Change Fact 8's charge to "grand larceny" and its maximum penalty to "3 years." Change Fact 9's email to focus on the penalty length rather than the label: "The maximum penalty for this charge is 6 months. You are not a felon." Update Option (b) and the explanation to reflect that his genuine belief that the penalty was under a year negates the *Rehaif* knowledge requirement.
-->

## Issue 3 — argpass-sonnet

**Q6.** Can Kevin successfully defend against the felon-in-possession charge based on his attorney's 2018 email?

(a) Guilty, because a defendant's ignorance of the law is never a valid defense to a federal firearms charge under traditional strict liability doctrines.
(b) Not guilty, because his genuine belief that he only had a misdemeanor conviction directly negates the required knowledge of his prohibited status. <!-- correct -->
(c) Guilty, because the defense attorney's private email does not legally qualify as an official statement of the law to support a reliance defense.
(d) Not guilty, because relying on the advice of private legal counsel automatically immunizes a criminal defendant from all federal felony liability.
(e) Guilty, because the actual statutory penalty for his prior state offense strictly establishes his prohibited status regardless of his personal beliefs.

**Answer:** (b)

**Explanation:** Under Rehaif v. United States, the government must prove the defendant knew he belonged to the relevant prohibited category (i.e., that he had a qualifying felony conviction). Kevin's genuine belief that his conviction was a misdemeanor negates this required mens rea. Option (a) fails because Rehaif explicitly displaced the traditional strict liability approach for the status element in this statute. Option (c) fails because Kevin does not need the affirmative "official statement" reliance defense; his mistake directly negates the statutory mens rea element. Option (d) fails because advice of counsel is not a blanket immunity doctrine. Option (e) fails because establishing the objective fact of the penalty is insufficient without proving the defendant's subjective knowledge of it.

**Tags:** chapters: [10, 15], topics: [Rehaif knowledge requirement, mistake of law, status element], difficulty: medium, cognitive: application

**Grounding:** Chapter 10 (Rehaif v. United States)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Prior to the Supreme Court's ruling in Rehaif, the status element of 18 U.S.C. § 922(g) was widely treated by lower courts as a strict liability element. Furthermore, a defendant's mistaken belief about the legal grading of their prior offense (felony vs. misdemeanor) is fundamentally a mistake of law. Because the maxim "ignorantia juris non excusat" applies heavily in federal criminal law, one could argue that under traditional strict liability doctrines, Kevin's ignorance of his true legal status is entirely irrelevant and provides no valid defense.
(b) Argument-for: In Rehaif v. United States, the Supreme Court held that the "knowingly" mens rea requirement applies both to the defendant's conduct and to their prohibited status. Therefore, the government must prove that Kevin actually knew he belonged to the category of persons barred from possessing a firearm (i.e., convicted felons). Because Kevin held a genuine, factually supported belief that his prior conviction was only a misdemeanor, he lacked the requisite knowledge of his prohibited status. This subjective mistake directly negates the mens rea required for the offense, rendering him not guilty.
(c) Argument-for: To successfully mount an affirmative "mistake of law" defense (often under the doctrine of entrapment by estoppel), a defendant typically must demonstrate reasonable reliance on an official statement of the law from a government official or authoritative body. A private defense attorney's email clearly does not meet this rigorous standard. If evaluated strictly through the lens of an affirmative reliance defense, the email fails as a matter of law to excuse his conduct, which a student might argue necessitates a guilty verdict.
(d) Argument-for: The advice-of-counsel defense is a well-established mechanism for negating specific intent or knowledge in federal criminal law. When a defendant fully discloses the relevant facts to competent legal counsel and relies in good faith on the resulting advice, they theoretically lack the culpable state of mind necessary to commit the crime. Because Kevin received an email from his attorney assuring him of his legal status, a student might reason that this reliance serves as a complete shield, automatically immunizing him from liability for possessing the firearm.
(e) Argument-for: The definition of a "felony" for the purposes of federal firearms disabilities is strictly determined by the objective statutory penalty (whether it is punishable by more than one year in prison) in the jurisdiction of conviction. A student could argue that this objective reality strictly controls the outcome, as the statute aims to disarm objectively dangerous individuals. Therefore, the objective statutory penalty firmly establishes his prohibited status as a matter of law, completely regardless of any subjective personal beliefs Kevin held regarding the classification of his crime.

Head-to-head: Option (b) correctly states the holding of Rehaif v. United States: subjective knowledge of one's prohibited status is required, and a genuine mistake negates this element. Option (a) and Option (e) both provide strong distractors by relying on pre-Rehaif strict liability logic, but they both use absolute language ("never", "regardless") that allows them to be explicitly falsified under modern precedent. Option (d) presents a wildly overbroad version of the advice-of-counsel defense ("automatically immunizes... from all federal felony liability"), making it easily falsifiable. Option (c), however, relies on a technically true premise—that a private email doesn't qualify as an official statement of law. It reaches the wrong conclusion ("Guilty") only because it implicitly omits that Kevin can win via a mens rea negation rather than an affirmative reliance defense. Because the Close-Call Standard explicitly states "Implicit omissions do not suffice," Option (c) is flawed as it lacks an explicit, identifiable false legal claim.

Falsifiable claim per distractor:
- (a): "never a valid defense... under traditional strict liability doctrines" — wrong because Rehaif explicitly rejected strict liability for the status element of § 922(g), making a mistake of legal status a valid defense.
- (c): Implicit omission only (no falsifiable claim) — The phrase "the defense attorney's private email does not legally qualify as an official statement of the law" is a true statement of law; the option is only wrong because it ignores a separate pathway to acquittal (mens rea negation).
- (d): "automatically immunizes a criminal defendant from all federal felony liability" — wrong because advice-of-counsel is not a blanket immunity doctrine that automatically applies to all federal felonies.
- (e): "strictly establishes his prohibited status regardless of his personal beliefs" — wrong because Rehaif demands subjective knowledge of the prohibited status, meaning it cannot be established "regardless of his personal beliefs."

Recommended fix: Edit (c) to contain an explicitly false legal claim. For example: "(c) Guilty, because a defendant can only negate the knowledge element of a federal firearms charge by relying on an official public statement of the law."
-->```

## Issue 4 — argpass-opus

**Q6.** Can Kevin successfully defend against the felon-in-possession charge based on his attorney's 2018 email?

(a) Guilty, because a defendant's ignorance of the law is never a valid defense to a federal firearms charge under traditional strict liability doctrines.
(b) Not guilty, because his genuine belief that he only had a misdemeanor conviction directly negates the required knowledge of his prohibited status. <!-- correct -->
(c) Guilty, because the defense attorney's private email does not legally qualify as an official statement of the law to support a reliance defense.
(d) Not guilty, because relying on the advice of private legal counsel automatically immunizes a criminal defendant from all federal felony liability.
(e) Guilty, because the actual statutory penalty for his prior state offense strictly establishes his prohibited status regardless of his personal beliefs.

**Answer:** (b)

**Explanation:** Under Rehaif v. United States, the government must prove the defendant knew he belonged to the relevant prohibited category (i.e., that he had a qualifying felony conviction). Kevin's genuine belief that his conviction was a misdemeanor negates this required mens rea. Option (a) fails because Rehaif explicitly displaced the traditional strict liability approach for the status element in this statute. Option (c) fails because Kevin does not need the affirmative "official statement" reliance defense; his mistake directly negates the statutory mens rea element. Option (d) fails because advice of counsel is not a blanket immunity doctrine. Option (e) fails because establishing the objective fact of the penalty is insufficient without proving the defendant's subjective knowledge of it.

**Tags:** chapters: [10, 15], topics: [Rehaif knowledge requirement, mistake of law, status element], difficulty: medium, cognitive: application

**Grounding:** Chapter 10 (Rehaif v. United States)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Traditional criminal law often applies strict liability to jurisdictional or status elements, following the maxim that ignorance of the law is no excuse. A student could argue that federal firearms charges have historically treated the defendant's status as a strict liability element, meaning Kevin's lack of knowledge about his felony classification is legally irrelevant. Therefore, he is guilty because ignorance of the law never excuses this strict liability element.
(b) Argument-for: In Rehaif v. United States, the Supreme Court held that the government must prove both that the defendant knew he possessed a firearm and that he knew he belonged to the prohibited category of persons. Because Kevin genuinely believed his prior conviction was only a misdemeanor, he lacked the requisite knowledge of his felon status. This mistake negates the statutory mens rea, making him not guilty.
(c) Argument-for: To successfully mount an affirmative reliance defense (such as public authority or entrapment by estoppel), a defendant must rely on an official statement from a government actor. A student could argue that because Kevin's advice came from a private defense attorney, it lacks the official character required to legally excuse his conduct. Under this view, he remains guilty because his private email cannot support an official reliance defense.
(d) Argument-for: The advice of counsel doctrine can serve to negate specific intent when a defendant fully discloses all facts to an attorney and relies on their advice in good faith. A student might overextend this doctrine, arguing that good-faith reliance on a lawyer's email provides absolute legal protection. Under this reasoning, Kevin is not guilty because relying on private counsel automatically immunizes him from any federal felony liability.
(e) Argument-for: The definition of a prohibited person under the felon-in-possession statute relies on the objective reality of the prior conviction's penalty (punishable by more than one year). A student could argue that as long as the prior offense actually meets this objective threshold, the status element is strictly satisfied. Therefore, Kevin is guilty because the actual statutory penalty establishes his status regardless of subjective personal beliefs.

Head-to-head: Option (b) correctly applies Rehaif, concluding that Kevin's mistake about his felony status negates the required mens rea. Option (a) incorrectly claims that ignorance is "never" a valid defense, ignoring Rehaif's abrogation of strict liability for the status element. Option (d) incorrectly states that advice of counsel "automatically immunizes" from "all" liability, which is a gross exaggeration of the doctrine. Option (e) falsely asserts that the objective penalty establishes status "regardless of his personal beliefs," directly contravening Rehaif's subjective knowledge requirement. Option (c), however, presents a legally true statement ("does not legally qualify as an official statement..."). It is the wrong answer because it mischaracterizes the type of defense Kevin is raising, but its actual legal proposition is true, meaning it fails the standard of containing an explicit, identifiable false legal claim.

Falsifiable claim per distractor:
- (a): "a defendant's ignorance of the law is never a valid defense to a federal firearms charge" — wrong because under Rehaif, strict liability no longer applies to the status element, and ignorance of one's legal status can indeed be a valid defense.
- (c): None. The phrase "does not legally qualify as an official statement of the law to support a reliance defense" is factually and legally true regarding a private attorney's email. The option is wrong only via the implicit omission that an affirmative reliance defense is unnecessary in this context.
- (d): "automatically immunizes a criminal defendant from all federal felony liability" — wrong because advice of counsel only negates specific intent and does not provide blanket, automatic immunity for all federal felonies.
- (e): "strictly establishes his prohibited status regardless of his personal beliefs" — wrong because Rehaif explicitly requires the government to prove the defendant's subjective knowledge of his status, rendering personal beliefs highly relevant.

Recommended fix: Change (c) to contain a falsifiable error: "(c) Guilty, because advice from private legal counsel categorically cannot be used to negate the statutory knowledge element of a federal criminal offense."
-->
