# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q5.** Assume Chloe is charged with attempted possession of narcotics for retrieving the bag of fake powder. Which of the following is correct?

(a) Not guilty because her honest belief that the bag contained stolen cash negates the specific intent required for an attempted narcotics possession conviction. <!-- correct -->
(b) Guilty because her arrival at the gym to retrieve the bag constitutes a substantial step that automatically satisfies the mens rea for attempt.
(c) Guilty because factual impossibility is never a valid defense to an attempt charge, meaning her mistake about the powder is legally irrelevant.
(d) Not guilty because her arrest before opening the locker means her actions constituted mere preparation rather than a substantial step toward the offense.
(e) Guilty because she is held strictly liable for whatever the bag originally contained before the police replaced the narcotics two days prior.

**Answer:** (a)

**Explanation:** (a) is correct because attempt requires the specific intent (purpose) to commit the target offense. Under the mistake of fact doctrine, Chloe's honest belief that the bag contained stolen cash negates the mens rea required for attempted narcotics possession, as she did not intend to possess drugs. (b) is incorrect because although arriving at the gym is a substantial step, she still lacks the required specific intent for the drug offense. (c) is incorrect because while factual impossibility (the bag containing fake powder) is not a defense, her subjective lack of intent to possess narcotics is a valid defense. (d) is incorrect because walking through the front doors to retrieve the target item typically crosses the line from preparation to a substantial step. (e) is incorrect because attempt is a specific intent crime that never imposes strict liability based on prior contents.

**Tags:** chapters: [10, 17], topics: [attempt-mens-rea, mistake-of-fact, impossibility], difficulty: hard, cognitive: application

**Grounding:** Chapter 17 - Attempts (Mens rea specific intent); Chapter 10 - Mistake of Fact

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Factual contradiction. The prompt for Q5 states Chloe is charged "for retrieving the bag," and Fact 5 similarly states "When Chloe retrieved the bag...". However, Fact 6 and Option (d) explicitly state she was intercepted and arrested at the front doors *before* ever opening the locker. This makes the sequence of events incoherent.
2. Cross-Doctrine Clashes: Pass. Even under the "Legal Wrong" exception to the mistake of fact doctrine (MPC 2.04(2)), Chloe would only be liable for the crime she intended to commit (attempted possession of stolen property), not the charged specific-intent crime of attempted possession of narcotics. Option (a) remains legally sound.
3. Cross-Question Spoilers: Pass.
Recommended fix: Update the Q5 prompt to resolve the temporal contradiction: "Assume Chloe is charged with attempted possession of narcotics after being arrested at the gym." (Note: The author should also lightly amend Fact 5 in the global prompt from "When Chloe retrieved the bag..." to "When Chloe agreed to retrieve the bag...").
-->

## Issue 3 — argpass-sonnet

**Q5.** Assume Chloe is charged with attempted possession of narcotics for retrieving the bag of fake powder. Which of the following is correct?

(a) Not guilty because her honest belief that the bag contained stolen cash negates the specific intent required for an attempted narcotics possession conviction. <!-- correct -->
(b) Guilty because her arrival at the gym to retrieve the bag constitutes a substantial step that automatically satisfies the mens rea for attempt.
(c) Guilty because factual impossibility is never a valid defense to an attempt charge, meaning her mistake about the powder is legally irrelevant.
(d) Not guilty because her arrest before opening the locker means her actions constituted mere preparation rather than a substantial step toward the offense.
(e) Guilty because she is held strictly liable for whatever the bag originally contained before the police replaced the narcotics two days prior.

**Answer:** (a)

**Explanation:** (a) is correct because attempt requires the specific intent (purpose) to commit the target offense. Under the mistake of fact doctrine, Chloe's honest belief that the bag contained stolen cash negates the mens rea required for attempted narcotics possession, as she did not intend to possess drugs. (b) is incorrect because although arriving at the gym is a substantial step, she still lacks the required specific intent for the drug offense. (c) is incorrect because while factual impossibility (the bag containing fake powder) is not a defense, her subjective lack of intent to possess narcotics is a valid defense. (d) is incorrect because walking through the front doors to retrieve the target item typically crosses the line from preparation to a substantial step. (e) is incorrect because attempt is a specific intent crime that never imposes strict liability based on prior contents.

**Tags:** chapters: [10, 17], topics: [attempt-mens-rea, mistake-of-fact, impossibility], difficulty: hard, cognitive: application

**Grounding:** Chapter 17 - Attempts (Mens rea specific intent); Chapter 10 - Mistake of Fact

<!-- argument-pass: SHOULD FIX
(a) Argument-for: This is the legally correct application of doctrine. Attempt is categorically a specific intent crime requiring the defendant to act with the purpose of committing the target offense. Under the mistake of fact doctrine, Chloe’s honest belief that the bag contained stolen cash means she lacked the mens rea to possess narcotics. Without the specific intent to possess drugs, she cannot be guilty of attempted narcotics possession.
(b) Argument-for: A student could argue that arriving at the gym is an objective manifestation of intent that satisfies the Model Penal Code’s "substantial step" test. Since the physical act strongly corroborates criminal purpose, one might reason that completing this substantial step merges the actus reus and mens rea requirements, solidifying liability for an attempt charge.
(c) Argument-for: A student might rely on the modern rule that factual impossibility (the bag containing fake powder instead of real drugs) is not a defense to attempt. If factual impossibility is categorically rejected, a student could incorrectly conclude that any mistake regarding the actual contents of the bag is overridden by the impossibility doctrine, making her subjective belief legally irrelevant.
(d) Argument-for: Under traditional common law proximity tests (e.g., the "dangerous proximity" test), attempt requires the defendant to come very close to success. A student could argue that being arrested merely upon entering the gym—without even opening the locker—leaves too many intervening steps remaining. Thus, as a matter of law under these strict tests, her conduct falls short of a substantial step and remains mere preparation.
(e) Argument-for: A student might argue that certain drug possession offenses carry strict liability elements. Since the bag actually contained narcotics two days prior and she is retrieving the specific container tied to that illicit origin, one could argue she constructively inherits liability for its original contents, regardless of her intent or the police intervention.

Head-to-head: Option (a) is the decisively correct answer because it accurately applies the mistake of fact doctrine to the specific intent requirement of attempt. Option (b) fails by falsely claiming the actus reus (substantial step) "automatically satisfies" the mens rea. Option (c) conflates factual impossibility with mistake of fact. Option (e) falsely applies strict liability to attempt. Option (d), however, presents a structural issue: it claims her arrest before opening the locker "means her actions constituted mere preparation." In jurisdictions utilizing the dangerous proximity doctrine rather than the MPC substantial step test, this could arguably be a true statement. Because the explanation concedes her actions "typically" (rather than definitively) cross the line, (d) lacks an absolute word to lock it as an unambiguously false legal claim in all jurisdictions. 

Falsifiable claim per distractor:
- (b): "automatically satisfies the mens rea for attempt" — wrong because performing a substantial step (actus reus) does not automatically satisfy or replace the independent requirement of specific intent (mens rea).
- (c): "meaning her mistake about the powder is legally irrelevant" — wrong because her mistake of fact (believing it was cash) negates specific intent, which operates as a completely distinct and valid defense from factual impossibility.
- (d): "means her actions constituted mere preparation" — wrong under the MPC, but potentially defensible under common law proximity tests since it lacks an absolute qualifier (like "categorically"). 
- (e): "she is held strictly liable for whatever the bag originally contained" — wrong because attempt is categorically a specific intent crime and does not permit strict liability.

Recommended fix: Add absolute language to (d) to ensure it is demonstrably false regardless of jurisdiction. Change (d) to: "Not guilty because her arrest before opening the locker categorically prevents her actions from constituting a substantial step in any jurisdiction."
-->

## Issue 4 — argpass-opus

**Q5.** Assume Chloe is charged with attempted possession of narcotics for retrieving the bag of fake powder. Which of the following is correct?

(a) Not guilty because her honest belief that the bag contained stolen cash negates the specific intent required for an attempted narcotics possession conviction. <!-- correct -->
(b) Guilty because her arrival at the gym to retrieve the bag constitutes a substantial step that automatically satisfies the mens rea for attempt.
(c) Guilty because factual impossibility is never a valid defense to an attempt charge, meaning her mistake about the powder is legally irrelevant.
(d) Not guilty because her arrest before opening the locker means her actions constituted mere preparation rather than a substantial step toward the offense.
(e) Guilty because she is held strictly liable for whatever the bag originally contained before the police replaced the narcotics two days prior.

**Answer:** (a)

**Explanation:** (a) is correct because attempt requires the specific intent (purpose) to commit the target offense. Under the mistake of fact doctrine, Chloe's honest belief that the bag contained stolen cash negates the mens rea required for attempted narcotics possession, as she did not intend to possess drugs. (b) is incorrect because although arriving at the gym is a substantial step, she still lacks the required specific intent for the drug offense. (c) is incorrect because while factual impossibility (the bag containing fake powder) is not a defense, her subjective lack of intent to possess narcotics is a valid defense. (d) is incorrect because walking through the front doors to retrieve the target item typically crosses the line from preparation to a substantial step. (e) is incorrect because attempt is a specific intent crime that never imposes strict liability based on prior contents.

**Tags:** chapters: [10, 17], topics: [attempt-mens-rea, mistake-of-fact, impossibility], difficulty: hard, cognitive: application

**Grounding:** Chapter 17 - Attempts (Mens rea specific intent); Chapter 10 - Mistake of Fact

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Attempt requires the specific intent, or purpose, to commit the target offense. Under the mistake of fact doctrine, Chloe's subjective, honest belief that the bag contained stolen cash prevents her from forming the requisite intent to possess narcotics. Without the mens rea for the specific target crime of narcotics possession, she cannot be guilty of an attempt to commit it.
(b) Argument-for: Under the Model Penal Code, attempt requires a "substantial step" strongly corroborative of the actor's criminal purpose. A student might argue that taking the physical step of arriving at the gym to retrieve the contraband crosses the line from mere preparation to a valid actus reus. If the act is so clearly established, one could mistakenly infer that the mens rea requirement is thereby automatically satisfied by the overt act.
(c) Argument-for: Factual impossibility occurs when a defendant intends to commit a crime but fails due to an unknown factual circumstance. Because modern jurisdictions overwhelmingly reject factual impossibility as a defense to attempt, a student could argue that Chloe's mistake about the bag's contents is simply an impossibility issue. This leads to the conclusion that her mistake about the powder is legally irrelevant to her liability.
(d) Argument-for: Under the common law "dangerous proximity" test, a defendant must be very close to completing the crime to be convicted of attempt. A student could argue that because Chloe was arrested before even opening the locker, she was not dangerously close to possession. Consequently, one might conclude that her distance from the final act means she was only in the preparation phase.
(e) Argument-for: Some drug possession statutes include strict liability elements regarding the nature or quantity of the substance. A student might argue that this strict liability transfers to the attempt charge, making her accountable for the actual prior contents of the bag. Therefore, she would be held legally accountable for the bag's original illicit nature before the police substituted them, regardless of her subjective intent.

Head-to-head: Option (a) correctly identifies that attempt is a specific intent crime and Chloe's mistake of fact negates this mens rea. Option (b) is legally false because the actus reus (substantial step) does not automatically satisfy the mens rea. Option (c) wrongly conflates her mistake of fact (which negates intent) with factual impossibility (which assumes intent but fails due to facts), falsely stating her mistake is legally irrelevant. Option (d) falsely suggests that failing to open the locker definitively prevents a substantial step finding; however, it lacks an absolute locking word like "categorically," making it a potentially debatable conclusion rather than an explicitly falsifiable rule. Option (e) falsely applies strict liability to an attempt charge, which always requires specific intent. Because (d) relies on the softer verb "means" rather than an absolute lock, a minor edit is recommended to fully lock the distractor.

Falsifiable claim per distractor:
- (b): "automatically satisfies the mens rea for attempt" — wrong because establishing the actus reus never automatically satisfies the independent requirement to prove specific intent.
- (c): "meaning her mistake about the powder is legally irrelevant" — wrong because her mistake relates to her intent (thinking it was cash), making it a mistake of fact that negates mens rea, which is legally relevant.
- (d): "means her actions constituted mere preparation rather than a substantial step" — wrong because arriving at the location to retrieve an item often qualifies as a substantial step or dangerous proximity, so an early arrest does not absolutely rule out an attempt. (Lacks an absolute word).
- (e): "she is held strictly liable for whatever the bag originally contained" — wrong because attempt is categorically a specific intent crime and cannot be based on strict liability.

Recommended fix: In (d), change "means her actions constituted" to "categorically renders her actions".
-->
