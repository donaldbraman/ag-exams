# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Assume the court determines the Chemical Act requires proof of a "willful" violation. Albert argues his reading of the preamble led him to genuinely believe university labs were exempt from the permit requirement. Does this provide a valid mistake of law defense?

(a) Guilty, because a defendant's personal misinterpretation of a statute's preamble does not qualify as reasonable reliance on an official statement of the law. <!-- correct -->
(b) Not guilty, because his review of the statute establishes that he acted in good faith, thereby negating any willful violation of the permit storage rule.
(c) Guilty, because the ignorance of the law defense only applies when the defendant formally consulted a licensed attorney before engaging in the prohibited conduct.
(d) Not guilty, because the statute's preamble creates an objective ambiguity, rendering the chemical storage regulation unconstitutionally vague as applied to him.
(e) Guilty, because the official reliance exception strictly requires the defendant to possess a written document signed by a sitting judge or state prosecutor.

**Answer:** (a)

**Explanation:** Under *People v. Marrero*, a defendant's personal, even reasonable, misinterpretation of an ambiguous statute does not constitute an "official statement of the law" and thus provides no mistake of law defense. Ignorance of the law is generally no excuse unless the defendant relies on an authoritative official interpretation (like an appellate court decision or official agency guidance). (b) is wrong because "willful" in regulatory contexts generally means intending the conduct, not necessarily knowing it is illegal (unless specifically carved out as in complex federal tax laws under *Cheek*). (c) is wrong because consulting a private attorney does not create a mistake of law defense under the official reliance exception. (d) is wrong because statutory ambiguity alone does not render a law unconstitutionally vague without a much higher showing of incomprehensibility. (e) is wrong because official statements can include published appellate decisions or formal administrative orders; it does not strictly require a signed document from a judge or prosecutor.

**Tags:** chapters: [10], topics: [mistake_of_law, official_statement, marrero], difficulty: medium, cognitive: application

**Grounding:** Chapter 10 - Mistake of Law: People v. Marrero and the rejection of personal misreading defenses

<!-- audit: MUST FIX
check 1: fail. The correct answer accuracy is compromised by the stem's explicit inclusion of "willful." Under the `mol-willfulness-exception` (e.g., *Cheek*, *Ratzlaf*), when a statute specifically requires a "willful" violation, a genuine, good-faith misunderstanding of the law *can* negate the required mens rea. 
check 2: fail. Option (b) is a highly defensible distractor. A well-prepared student who sees the word "willful" explicitly highlighted in the prompt will immediately (and correctly) recognize this as a trigger for the willfulness exception to the mistake of law doctrine, making (b) functionally correct under that line of cases. 
check 3: pass. The explanation accurately states the author's intent, though its dismissal of the *Cheek* exception conflicts with standard testing principles when "willful" is explicitly teed up in the prompt.
check 4: pass.
check 5: pass.
check 6: pass.
check 7: pass. Both *Marrero* (`mol-marrero-no-personal-reading`) and the willfulness exception (`mol-willfulness-exception`) are in Chapter 10.
check 8: pass. Answer options are symmetrical in length and structure.
Recommended fix: Remove the "willfulness" trap so the question cleanly tests *Marrero*. Change the first sentence to: "Assume the Chemical Act makes it a crime to 'knowingly store regulated chemicals without a permit.'" Update option (b) to: "Not guilty, because his good faith review of the statute negates the mental state required for the offense." Update the explanation to remove the convoluted justification about the meaning of "willful."
-->

## Issue 2 — edge-case

**Q5.** Assume the court determines the Chemical Act requires proof of a "willful" violation. Albert argues his reading of the preamble led him to genuinely believe university labs were exempt from the permit requirement. Does this provide a valid mistake of law defense?

(a) Guilty, because a defendant's personal misinterpretation of a statute's preamble does not qualify as reasonable reliance on an official statement of the law. <!-- correct -->
(b) Not guilty, because his review of the statute establishes that he acted in good faith, thereby negating any willful violation of the permit storage rule.
(c) Guilty, because the ignorance of the law defense only applies when the defendant formally consulted a licensed attorney before engaging in the prohibited conduct.
(d) Not guilty, because the statute's preamble creates an objective ambiguity, rendering the chemical storage regulation unconstitutionally vague as applied to him.
(e) Guilty, because the official reliance exception strictly requires the defendant to possess a written document signed by a sitting judge or state prosecutor.

**Answer:** (a)

**Explanation:** Under *People v. Marrero*, a defendant's personal, even reasonable, misinterpretation of an ambiguous statute does not constitute an "official statement of the law" and thus provides no mistake of law defense. Ignorance of the law is generally no excuse unless the defendant relies on an authoritative official interpretation (like an appellate court decision or official agency guidance). (b) is wrong because "willful" in regulatory contexts generally means intending the conduct, not necessarily knowing it is illegal (unless specifically carved out as in complex federal tax laws under *Cheek*). (c) is wrong because consulting a private attorney does not create a mistake of law defense under the official reliance exception. (d) is wrong because statutory ambiguity alone does not render a law unconstitutionally vague without a much higher showing of incomprehensibility. (e) is wrong because official statements can include published appellate decisions or formal administrative orders; it does not strictly require a signed document from a judge or prosecutor.

**Tags:** chapters: [10], topics: [mistake_of_law, official_statement, marrero], difficulty: medium, cognitive: application

**Grounding:** Chapter 10 - Mistake of Law: People v. Marrero and the rejection of personal misreading defenses

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The use of the word "willful" in the prompt's assumption ("requires proof of a 'willful' violation") inadvertently triggers the Cheek/Ratzlaf exception, where "willful" often requires the prosecution to prove the defendant knew their conduct was illegal. This makes option (b) a highly defensible answer, as a good faith mistake would negate a "willful" mens rea.
2. Cross-Doctrine Clashes: Mistake of Law as an affirmative defense (Marrero) clashes with Mistake of Law as a mens rea negation (Cheek). By specifying "willful," the question invites the latter, undermining the intended correct answer.
3. Cross-Question Spoilers: pass
Recommended fix: Change the first sentence to "Assume the court determines the Chemical Act requires proof that the defendant 'knowingly' stored the chemicals." This ensures the mens rea cleanly applies only to the factual conduct (storage), thereby perfectly isolating the Marrero official reliance issue. Also, in option (b), change "any willful violation" to "any knowing violation".
-->

## Issue 3 — argpass-sonnet

**Q5.** Assume the court determines the Chemical Act requires proof of a "willful" violation. Albert argues his reading of the preamble led him to genuinely believe university labs were exempt from the permit requirement. Does this provide a valid mistake of law defense?

(a) Guilty, because a defendant's personal misinterpretation of a statute's preamble does not qualify as reasonable reliance on an official statement of the law. <!-- correct -->
(b) Not guilty, because his review of the statute establishes that he acted in good faith, thereby negating any willful violation of the permit storage rule.
(c) Guilty, because the ignorance of the law defense only applies when the defendant formally consulted a licensed attorney before engaging in the prohibited conduct.
(d) Not guilty, because the statute's preamble creates an objective ambiguity, rendering the chemical storage regulation unconstitutionally vague as applied to him.
(e) Guilty, because the official reliance exception strictly requires the defendant to possess a written document signed by a sitting judge or state prosecutor.

**Answer:** (a)

**Explanation:** Under *People v. Marrero*, a defendant's personal, even reasonable, misinterpretation of an ambiguous statute does not constitute an "official statement of the law" and thus provides no mistake of law defense. Ignorance of the law is generally no excuse unless the defendant relies on an authoritative official interpretation (like an appellate court decision or official agency guidance). (b) is wrong because "willful" in regulatory contexts generally means intending the conduct, not necessarily knowing it is illegal (unless specifically carved out as in complex federal tax laws under *Cheek*). (c) is wrong because consulting a private attorney does not create a mistake of law defense under the official reliance exception. (d) is wrong because statutory ambiguity alone does not render a law unconstitutionally vague without a much higher showing of incomprehensibility. (e) is wrong because official statements can include published appellate decisions or formal administrative orders; it does not strictly require a signed document from a judge or prosecutor.

**Tags:** chapters: [10], topics: [mistake_of_law, official_statement, marrero], difficulty: medium, cognitive: application

**Grounding:** Chapter 10 - Mistake of Law: People v. Marrero and the rejection of personal misreading defenses

<!-- argument-pass: SHOULD FIX
(a) Argument-for: This option directly applies the black-letter rule from *People v. Marrero*. The official reliance exception to the mistake of law doctrine requires reliance on an actual official statement (e.g., a judicial decision, an administrative order, or a later-invalidated statute). A defendant's own personal misinterpretation of a statute, even if based on a close reading of a preamble, does not qualify as an official statement of the law. Therefore, Albert remains guilty.
(b) Argument-for: In some contexts (such as complex tax laws in *Cheek v. United States* or currency structuring in *Ratzlaf*), courts interpret the heightened mens rea of "willfully" to require proof that the defendant actually knew their conduct was unlawful. Under this reading, Albert's genuine, good-faith belief that university labs were exempt means he did not intentionally violate a known legal duty. Therefore, his mistake directly negates the specific "willful" mens rea required by the statute, making him not guilty.
(c) Argument-for: A student could argue that mistake of law requires an objectively verifiable attempt to ascertain the law's meaning before acting. Formal consultation with a licensed attorney provides a documented, professional legal opinion that a defendant could theoretically rely upon to show they did not knowingly break the law. Under this reasoning, because Albert only relied on his own lay interpretation rather than securing formal counsel, he forfeits the defense. 
(d) Argument-for: The void-for-vagueness doctrine requires that a criminal statute provide fair warning of the prohibited conduct. If the preamble creates an objective ambiguity regarding who is subject to the permit requirement, the statute fails to provide this fair warning to a reasonable person in Albert's position. Therefore, the regulation is unconstitutionally vague as applied to him, excusing his conduct.
(e) Argument-for: The official reliance exception is narrowly tailored to prevent abuse and fabricated claims of ignorance. To ensure defendants rely on truly authoritative sources, courts require strict, verifiable proof of official authorization. A written document signed by a sitting judge or state prosecutor satisfies this rigorous evidentiary threshold. Without such definitive documentation, Albert's defense automatically fails.

Head-to-head: Option (a) is the clearly correct answer under standard common law and MPC principles, accurately reflecting the *Marrero* ruling that personal misinterpretations of statutes do not excuse criminal conduct. However, options (b) and (d) apply false legal outcomes to the facts without utilizing the strict absolute phrasing required by the close-call standard. Because "willful" *does* sometimes require knowledge of illegality (as the explanation concedes regarding *Cheek*), option (b) is a dangerous distractor that needs an absolute word to make it categorically false in all general contexts. Similarly, option (d) applies the vagueness doctrine incorrectly but lacks absolute phrasing to lock the legal proposition as purely false rather than just a weak factual application. Options (c) and (e) successfully use absolutes ("only applies", "strictly requires").

Falsifiable claim per distractor:
- (b): "his review of the statute establishes that he acted in good faith, thereby negating any willful violation" — wrong because outside of specific exceptions (*Cheek*), good faith mistakes of law do not negate a "willful" mens rea, which generally requires only the intent to commit the act. (Lacks an absolute word).
- (c): "only applies when the defendant formally consulted a licensed attorney" — wrong because relying on private counsel explicitly does *not* constitute a valid official reliance defense under criminal law.
- (d): "creates an objective ambiguity, rendering the chemical storage regulation unconstitutionally vague" — wrong because objective ambiguity in a preamble does not meet the high constitutional threshold to render a statute void for vagueness. (Lacks an absolute word).
- (e): "strictly requires the defendant to possess a written document signed by a sitting judge or state prosecutor" — wrong because the official reliance doctrine recognizes other official statements like appellate judicial opinions and formal agency rulings.

Recommended fix: Add absolute words to (b) and (d) to lock their falsifiability. 
Change (b) to: "Not guilty, because a good-faith misinterpretation of a statute's text automatically negates a 'willful' mens rea requirement in criminal law."
Change (d) to: "Not guilty, because objective ambiguity in a statutory preamble categorically renders the underlying regulation unconstitutionally vague."
-->

## Issue 4 — argpass-opus

**Q5.** Assume the court determines the Chemical Act requires proof of a "willful" violation. Albert argues his reading of the preamble led him to genuinely believe university labs were exempt from the permit requirement. Does this provide a valid mistake of law defense?

(a) Guilty, because a defendant's personal misinterpretation of a statute's preamble does not qualify as reasonable reliance on an official statement of the law. <!-- correct -->
(b) Not guilty, because his review of the statute establishes that he acted in good faith, thereby negating any willful violation of the permit storage rule.
(c) Guilty, because the ignorance of the law defense only applies when the defendant formally consulted a licensed attorney before engaging in the prohibited conduct.
(d) Not guilty, because the statute's preamble creates an objective ambiguity, rendering the chemical storage regulation unconstitutionally vague as applied to him.
(e) Guilty, because the official reliance exception strictly requires the defendant to possess a written document signed by a sitting judge or state prosecutor.

**Answer:** (a)

**Explanation:** Under *People v. Marrero*, a defendant's personal, even reasonable, misinterpretation of an ambiguous statute does not constitute an "official statement of the law" and thus provides no mistake of law defense. Ignorance of the law is generally no excuse unless the defendant relies on an authoritative official interpretation (like an appellate court decision or official agency guidance). (b) is wrong because "willful" in regulatory contexts generally means intending the conduct, not necessarily knowing it is illegal (unless specifically carved out as in complex federal tax laws under *Cheek*). (c) is wrong because consulting a private attorney does not create a mistake of law defense under the official reliance exception. (d) is wrong because statutory ambiguity alone does not render a law unconstitutionally vague without a much higher showing of incomprehensibility. (e) is wrong because official statements can include published appellate decisions or formal administrative orders; it does not strictly require a signed document from a judge or prosecutor.

**Tags:** chapters: [10], topics: [mistake_of_law, official_statement, marrero], difficulty: medium, cognitive: application

**Grounding:** Chapter 10 - Mistake of Law: People v. Marrero and the rejection of personal misreading defenses

<!-- argument-pass: MUST FIX
(a) Argument-for: Under Model Penal Code § 2.04 and cases like *People v. Marrero*, the mistake of law defense based on reliance requires an "official statement of the law" (like a judicial decision or administrative order). A defendant's personal misinterpretation of a statute's text or preamble—even if reasonable—does not qualify. Option (a) correctly identifies this doctrine and its application to Albert's guilt.
(b) Argument-for: The prompt specifically establishes that the Chemical Act requires proof of a "willful" violation. Under federal criminal law (e.g., *Cheek v. United States*, *Ratzlaf v. United States*), the specific mens rea of "willfulness" frequently requires the government to prove the defendant intentionally violated a known legal duty. If Albert genuinely believed labs were exempt, he did not act willfully, and his good-faith mistake of law negates the mens rea, making (b) legally correct under this standard.
(c) Argument-for: A student might argue that the only way to establish a good-faith mistake of law is by showing formal, diligent effort to ascertain the law. Therefore, option (c) could be defended on the theory that without formal consultation with a licensed attorney, an ignorance defense categorically fails, leading to his guilt.
(d) Argument-for: A preamble that contradicts the statutory text or creates a trap for the unwary could be argued to violate the Due Process Clause's requirement for fair notice. If the ambiguity is severe enough that an ordinary person cannot determine what is prohibited, the statute is unconstitutionally vague as applied, making (d) a plausible constitutional defense.
(e) Argument-for: The official reliance doctrine is highly restrictive to prevent abuse. A student could argue that to qualify, the defendant must rely on something concretely and formally issued by a top legal authority—like a judge or prosecutor—and therefore, mere personal reading of a statute is insufficient without a signed, authoritative document.

Head-to-head:
Option (a) correctly applies the *Marrero* rule for official reliance. However, option (b) is fundamentally problematic because the prompt explicitly sets the mens rea as "willful." In many jurisdictions, "willful" is a term of art that specifically allows a good-faith mistake of law to negate mens rea (*Cheek*). By needlessly introducing "willful," the prompt accidentally makes (b) a highly defensible answer under the mens rea exception to the mistake of law doctrine, contradicting the intended focus on *Marrero*. Options (c), (d), and (e) are successfully falsifiable because they rely on absolute misstatements of law ("only applies when", "rendering... vague", "strictly requires"). 

Falsifiable claim per distractor:
- (b): "thereby negating any willful violation" — intended to be wrong under general intent, but arguably true because "willful" often legally requires a known legal duty, making the claim completely unfalsifiable without dictating a specific jurisdiction's interpretation of the statute.
- (c): "only applies when the defendant formally consulted a licensed attorney" — wrong because relying on a private attorney explicitly *fails* to qualify for the official reliance exception, and it is certainly not the "only" requirement.
- (d): "rendering the chemical storage regulation unconstitutionally vague" — wrong because mere ambiguity in a preamble does not categorically render a statute unconstitutionally vague.
- (e): "strictly requires the defendant to possess a written document signed by a sitting judge or state prosecutor" — wrong because official statements include published statutes, appellate opinions, and agency rulings, not solely personally signed documents from judges or prosecutors.

Recommended fix: Change the prompt to remove the word "willful." Use a standard mens rea: "Assume the Chemical Act requires proof that the defendant 'knowingly' stored the chemicals." Update (b) to: "Not guilty, because his review of the statute establishes that he acted in good faith, thereby negating the knowing mens rea of the permit storage rule." This makes (b) safely false, as "knowingly" only applies to the factual conduct, not the legal requirement.
-->
