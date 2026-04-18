# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q1.** Are Marcus, Darius, and Leon guilty of conspiracy to assault Vance's crew based on the events on Tuesday?

(a) Guilty, because their coordinated action of taking up watch positions following Marcus's command allows a jury to infer a mutual agreement. <!-- correct -->
(b) Not guilty, because Darius and Leon did not verbally consent or explicitly communicate their acceptance of Marcus's plan.
(c) Not guilty, because Marcus's command to "beat them down if you have to" was conditional, preventing the formation of a definite criminal purpose.
(d) Guilty, because Marcus possessed the specific intent to promote an assault, which satisfies the unilateral requirement for all three parties.
(e) Not guilty, because taking up a watch position is merely preparatory and fails to satisfy the overt act requirement for conspiracy.

**Answer:** (a)

**Explanation:** (a) is correct. Conspiracy requires an agreement, but explicit words are rarely necessary; a mutual understanding can be inferred from coordinated conduct that has no plausible innocent explanation. (b) is incorrect because explicit verbal agreement is not required. (c) is incorrect because conditional intent to commit a crime still constitutes a criminal agreement. (d) is incorrect because the unilateral approach focuses on a specific defendant's belief that they are agreeing, but does not impute an agreement to parties who haven't actually formed one. (e) is incorrect because the overt act requirement for conspiracy is exceedingly minimal and easily satisfied by taking a watch position.

**Tags:** chapters: [19], topics: [conspiracy, agreement-inference], difficulty: medium, cognitive: application

**Grounding:** Chapter 19: Conspiracy > Elements > Prima Facie Elements > Agreement (Inferring agreement from coordinated conduct)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The question uses the character "Leon," but the master character list and the Q1 stub rely on "Trey" for this exact lookout/driver role (reflecting a duplication/typo in the original Facts array between Fact 2 and Fact 3). This will confuse students when deployed within the full exam. The legal reasoning itself, however, is clean.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change "Leon" to "Trey" in the question stem and answer choices to ensure consistency across the scenario package.
-->

## Issue 3 — argpass-sonnet

**Q1.** Are Marcus, Darius, and Leon guilty of conspiracy to assault Vance's crew based on the events on Tuesday?

(a) Guilty, because their coordinated action of taking up watch positions following Marcus's command allows a jury to infer a mutual agreement. <!-- correct -->
(b) Not guilty, because Darius and Leon did not verbally consent or explicitly communicate their acceptance of Marcus's plan.
(c) Not guilty, because Marcus's command to "beat them down if you have to" was conditional, preventing the formation of a definite criminal purpose.
(d) Guilty, because Marcus possessed the specific intent to promote an assault, which satisfies the unilateral requirement for all three parties.
(e) Not guilty, because taking up a watch position is merely preparatory and fails to satisfy the overt act requirement for conspiracy.

**Answer:** (a)

**Explanation:** (a) is correct. Conspiracy requires an agreement, but explicit words are rarely necessary; a mutual understanding can be inferred from coordinated conduct that has no plausible innocent explanation. (b) is incorrect because explicit verbal agreement is not required. (c) is incorrect because conditional intent to commit a crime still constitutes a criminal agreement. (d) is incorrect because the unilateral approach focuses on a specific defendant's belief that they are agreeing, but does not impute an agreement to parties who haven't actually formed one. (e) is incorrect because the overt act requirement for conspiracy is exceedingly minimal and easily satisfied by taking a watch position.

**Tags:** chapters: [19], topics: [conspiracy, agreement-inference], difficulty: medium, cognitive: application

**Grounding:** Chapter 19: Conspiracy > Elements > Prima Facie Elements > Agreement (Inferring agreement from coordinated conduct)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A jury may properly infer an agreement from coordinated conduct that lacks a plausible innocent explanation. When Marcus commanded his associates to be ready to assault Vance's crew, and Darius and Leon subsequently took up watch positions in accordance with that command, their actions manifested a mutual understanding. In conspiracy law, tacit agreement inferred from concerted action is fully sufficient to establish the agreement element, making this option clearly correct.
(b) Argument-for: Conspiracy requires a genuine "meeting of the minds" between the parties. Without verbal consent or explicit communication of acceptance, Darius and Leon's actions might be characterized as uncommunicated parallel action rather than a definitive agreement. An adversarial reader could argue that penalizing individuals purely based on ambiguous actions—without explicit proof of their assent to Marcus's exact plan—fails to legally establish the required agreement element.
(c) Argument-for: At common law, conspiracy requires the specific intent to commit a target offense. Marcus's command to "beat them down if you have to" is strictly conditional. A student could argue that because the assault was contingent on a specific triggering event, the parties did not form a definite and present intent to commit the crime, meaning the requisite absolute criminal purpose was never fully established.
(d) Argument-for: Under the Model Penal Code's unilateral approach to conspiracy, an individual can be guilty if they possess the specific intent to agree to commit a crime, regardless of the other parties' genuine agreement. Marcus clearly possessed the intent to promote the assault. A student might mistakenly extrapolate this to conclude that Marcus's unilateral intent creates a conspiracy that inherently ensnares the entire group, satisfying the element for all three parties.
(e) Argument-for: Conspiracy requires an overt act in furtherance of the agreement. While the overt act requirement is generally minimal, a student could argue that taking a watch position is far too remote from the actual assault to qualify. By conflating the attempt standard (which generally excludes mere preparation) with the conspiracy standard, a student could wrongly conclude that a preparatory watch position fails to satisfy the necessary overt act requirement.

Head-to-head:
Option (a) correctly identifies that a tacit agreement can be inferred from coordinated conduct, reflecting standard conspiracy doctrine. Distractor (b) correctly states the facts but relies on an implicit, unstated legal premise that explicit communication is strictly required; because it lacks absolute language, it fails the standard for an explicit false legal claim. Distractor (c) claims that conditional intent prevents a conspiracy, which is legally false but lacks a categorical locking word. Distractor (d) contains an explicitly false legal claim: that the unilateral approach can satisfy the agreement element for *all three* parties based on one person's intent. Distractor (e) explicitly and falsely claims that a "merely preparatory" act fails the overt act requirement for conspiracy (improperly importing the attempt standard). Because (b) relies entirely on an implicit omission rather than an explicit, locked legal proposition, the question requires a SHOULD FIX.

Falsifiable claim per distractor:
- (b): "because Darius and Leon did not verbally consent or explicitly communicate" — wrong because tacit agreement inferred from conduct is legally sufficient, but the option lacks an explicit legal claim locked by absolute words (e.g., "categorically requires").
- (c): "preventing the formation of a definite criminal purpose" — wrong because conditional intent is generally sufficient for conspiracy, though adding "automatically" would better lock the legal falsehood.
- (d): "satisfies the unilateral requirement for all three parties" — wrong because the unilateral approach applies only to the individual who possesses the requisite intent; it cannot legally impute guilt to non-agreeing parties.
- (e): "is merely preparatory and fails to satisfy the overt act requirement" — wrong because the overt act for conspiracy requires only any act in furtherance, explicitly including mere preparation, unlike the higher standard for attempt.

Recommended fix: Add absolute locking words to (b) and (c) to ensure they make explicit false legal claims. For (b): "Not guilty, solely because Darius and Leon did not verbally consent..." For (c): "...was conditional, automatically preventing the formation..."
-->

## Issue 4 — argpass-opus

**Q1.** Are Marcus, Darius, and Leon guilty of conspiracy to assault Vance's crew based on the events on Tuesday?

(a) Guilty, because their coordinated action of taking up watch positions following Marcus's command allows a jury to infer a mutual agreement. <!-- correct -->
(b) Not guilty, because Darius and Leon did not verbally consent or explicitly communicate their acceptance of Marcus's plan.
(c) Not guilty, because Marcus's command to "beat them down if you have to" was conditional, preventing the formation of a definite criminal purpose.
(d) Guilty, because Marcus possessed the specific intent to promote an assault, which satisfies the unilateral requirement for all three parties.
(e) Not guilty, because taking up a watch position is merely preparatory and fails to satisfy the overt act requirement for conspiracy.

**Answer:** (a)

**Explanation:** (a) is correct. Conspiracy requires an agreement, but explicit words are rarely necessary; a mutual understanding can be inferred from coordinated conduct that has no plausible innocent explanation. (b) is incorrect because explicit verbal agreement is not required. (c) is incorrect because conditional intent to commit a crime still constitutes a criminal agreement. (d) is incorrect because the unilateral approach focuses on a specific defendant's belief that they are agreeing, but does not impute an agreement to parties who haven't actually formed one. (e) is incorrect because the overt act requirement for conspiracy is exceedingly minimal and easily satisfied by taking a watch position.

**Tags:** chapters: [19], topics: [conspiracy, agreement-inference], difficulty: medium, cognitive: application

**Grounding:** Chapter 19: Conspiracy > Elements > Prima Facie Elements > Agreement (Inferring agreement from coordinated conduct)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: This option correctly identifies the core mechanism for proving a conspiratorial agreement when express words are absent. A jury is permitted to infer a "meeting of the minds" from concerted action. By taking up watch positions immediately following Marcus's command, Darius and Leon engaged in coordinated conduct that strongly evidences a tacit mutual agreement to further the criminal objective.
(b) Argument-for: This option rests on the premise that a criminal agreement requires a genuine meeting of the minds, which must be clearly evidenced. A student could argue that without explicit verbal consent or communication, the defendants' actions might just constitute mere presence or unrelated obedience, meaning the prosecution cannot prove an actual agreement beyond a reasonable doubt.
(c) Argument-for: Conspiracy requires the specific intent to achieve a criminal objective. If a plan is explicitly conditional ("if you have to"), a student could argue that the parties have not committed to the actual commission of the crime, but only to a mere possibility. This arguably negates the "definite criminal purpose" required to form a completed conspiratorial agreement.
(d) Argument-for: The Model Penal Code adopts a "unilateral" approach to conspiracy, meaning that a conspiracy can exist even if only one party genuinely intends to agree. A student could misapply this doctrine, arguing that because Marcus had the specific intent to promote the assault, his unilateral intent satisfies the statutory requirement for the whole group, making all three guilty.
(e) Argument-for: Conspiracy in most jurisdictions requires an overt act in furtherance of the agreement. A student might import the "mere preparation" doctrine from the law of attempt, arguing that simply standing in a watch position is too preliminary to constitute an overt act, meaning the conspiracy remains legally incomplete.

Head-to-head: 
Option (a) correctly applies the universally accepted rule that a conspiratorial agreement can be inferred from coordinated conduct. Option (d) contains an explicitly false claim by asserting the unilateral approach makes "all three parties" guilty, rather than just the one with the requisite intent. Option (e) contains a legally false claim by conflating attempt with conspiracy, asserting that a "merely preparatory" act fails the overt act requirement (when in conspiracy, preparation is legally sufficient). However, options (b) and (c) rely on implying false legal rules without using absolute modifiers to lock them in as definitively false statements of law, making them vulnerable to arguments about implicit factual omissions.

Falsifiable claim per distractor:
- (b): "did not verbally consent or explicitly communicate their acceptance" — wrong because it relies on the implicit false assumption that explicit agreement is a necessary element of conspiracy, but lacks an absolute word to firmly state this as a false legal rule.
- (c): "was conditional, preventing the formation of a definite criminal purpose" — wrong because conditional intent is generally sufficient for conspiracy, but it lacks an absolute word to explicitly claim conditional intent categorically negates an agreement.
- (d): "satisfies the unilateral requirement for all three parties" — wrong because the unilateral approach establishes liability only for the individual who actually possesses the required intent, not for the non-agreeing parties.
- (e): "is merely preparatory and fails to satisfy the overt act requirement" — wrong because unlike the law of attempt, mere preparation is legally sufficient to satisfy the overt act requirement for conspiracy.

Recommended fix: Edit (b) to: "Not guilty, solely because Darius and Leon did not explicitly communicate their acceptance of Marcus's plan." Edit (c) to: "Not guilty, because a conditional command automatically prevents the formation of a criminal agreement."
-->
