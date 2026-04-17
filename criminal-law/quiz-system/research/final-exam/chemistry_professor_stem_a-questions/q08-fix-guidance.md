# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q8.** Assume Silas argues that his attempt to call 911 constituted a complete withdrawal from the conspiracy, shielding him from any criminal liability for the drug distribution and the conspiracy itself. How should the court rule on this specific claim?

(a) Invalid claim, because pulling out his phone and stating his intent was not an affirmative act completely inconsistent with the conspiracy.
(b) Invalid claim, because he did not effectively attempt to thwart the completion of the crime before the victim ultimately died.
(c) Invalid claim, because withdrawal only limits liability for future substantive offenses and does not erase liability for the conspiracy itself. <!-- correct -->
(d) Invalid claim, because he did not successfully complete the 911 call to law enforcement before physically leaving the motel room.
(e) Invalid claim, because a co-conspirator must successfully turn state's evidence to effectively withdraw from an ongoing drug distribution conspiracy.

**Answer:** (c)

**Explanation:** (c) is correct. Under traditional conspiracy doctrine, an effective withdrawal cuts off liability for *future* collateral crimes committed by co-conspirators under *Pinkerton*, but it does not erase liability for the conspiracy itself or for substantive crimes (like the distribution) that were already completed prior to the withdrawal. (a) and (b) fail because even a valid withdrawal does not provide retrospective immunity for completed crimes. (d) fails because successful police contact is not always required if communication to co-conspirators is sufficient, though it is irrelevant to completed crimes. (e) fails because turning state's evidence is not a legal requirement for withdrawal.

**Tags:** chapters: [19], topics: [conspiracy, withdrawal requirements], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, Withdrawal requirements and limitations.

<!-- audit: MUST FIX
Check 1: Fails. Option (c) asserts categorically that withdrawal "does not erase liability for the conspiracy itself." While this is accurate under common law, it is incorrect under the MPC. Under MPC § 5.03(6), renunciation CAN serve as an affirmative defense erasing liability for the conspiracy itself if the defendant thwarts the success of the conspiracy.
Check 2: Fails. A prepared student applying the MPC would reject (c) as a false statement of law. They could credibly argue for (b), recognizing that under the MPC, Silas's attempt to erase his conspiracy liability fails precisely because he did not actually thwart the crime's completion.
Check 3: Pass. The explanation correctly maps to common law doctrine, but inadvertently reveals the issue by explicitly relying on "traditional conspiracy doctrine..." when the stem does not.
Check 4: Pass. (Assuming the overarching fact pattern establishes that the drug distribution was completed prior to the 911 attempt).
Check 5: Fails. The question tests a doctrine with a major jurisdictional split (Common Law withdrawal vs. MPC renunciation/thwarting), but the stem fails to stipulate the jurisdiction.
Check 6: Pass.
Check 7: Pass.
Recommended fix: Add a jurisdictional constraint to the prompt: "Under common law, how should the court rule on this specific claim?"
-->

## Issue 2 — argpass-opus

**Q8.** Assume Silas argues that his attempt to call 911 constituted a complete withdrawal from the conspiracy, shielding him from any criminal liability for the drug distribution and the conspiracy itself. How should the court rule on this specific claim?

(a) Invalid claim, because pulling out his phone and stating his intent was not an affirmative act completely inconsistent with the conspiracy.
(b) Invalid claim, because he did not effectively attempt to thwart the completion of the crime before the victim ultimately died.
(c) Invalid claim, because withdrawal only limits liability for future substantive offenses and does not erase liability for the conspiracy itself. <!-- correct -->
(d) Invalid claim, because he did not successfully complete the 911 call to law enforcement before physically leaving the motel room.
(e) Invalid claim, because a co-conspirator must successfully turn state's evidence to effectively withdraw from an ongoing drug distribution conspiracy.

**Answer:** (c)

**Explanation:** (c) is correct. Under traditional conspiracy doctrine, an effective withdrawal cuts off liability for *future* collateral crimes committed by co-conspirators under *Pinkerton*, but it does not erase liability for the conspiracy itself or for substantive crimes (like the distribution) that were already completed prior to the withdrawal. (a) and (b) fail because even a valid withdrawal does not provide retrospective immunity for completed crimes. (d) fails because successful police contact is not always required if communication to co-conspirators is sufficient, though it is irrelevant to completed crimes. (e) fails because turning state's evidence is not a legal requirement for withdrawal.

**Tags:** chapters: [19], topics: [conspiracy, withdrawal requirements], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, Withdrawal requirements and limitations.

<!-- argument-pass: MUST FIX
(a) Argument-for: A student might choose (a) by focusing on the factual requirements of withdrawal. To withdraw, a conspirator must take an affirmative act inconsistent with the conspiracy and communicate it to co-conspirators or law enforcement. A student could argue that merely stating an intent to call 911 without completing the call or ensuring all co-conspirators hear it falls short of an affirmative act. Therefore, his claim of withdrawal is invalid based on factual insufficiency.
(b) Argument-for: A student could apply the Model Penal Code's renunciation defense, which allows a conspirator to avoid liability for the conspiracy itself if they thwart the success of the conspiracy under circumstances manifesting a complete and voluntary renunciation. Because the victim died, Silas failed to thwart the crime. Thus, his claim that he is shielded from conspiracy liability is invalid precisely because he did not effectively thwart the crime, making (b) factually and legally plausible.
(c) Argument-for: Under traditional common law conspiracy doctrine, the crime of conspiracy is complete the moment the agreement is made (and an overt act occurs). Withdrawal can sever liability for *future* substantive offenses committed by co-conspirators, but it cannot retroactively erase liability for the conspiracy itself. Silas's claim that withdrawal shields him from liability for the conspiracy itself is therefore fundamentally legally invalid, making (c) correct.
(d) Argument-for: A student might choose (d) by reasoning that a withdrawal must be fully communicated to be effective. Since Silas was attempting to withdraw via law enforcement, his failure to successfully complete the 911 call means the authorities were never notified. Without completing this notification before leaving, his withdrawal was ineffective, making his claim invalid on this factual ground.
(e) Argument-for: A student could assume that once a serious drug distribution conspiracy is underway, the only legally recognized way to sufficiently establish withdrawal and abandonment is to fully cooperate with law enforcement. By arguing that Silas needed to turn state's evidence to effectively withdraw, a student might select (e) as the legally required standard for such an ongoing enterprise.

Head-to-head: Option (c) correctly identifies the core legal limitation of common law withdrawal: it is not a retrospective defense to the conspiracy charge itself. However, options (a), (b), and (d) present factual reasons why Silas's withdrawal was ineffective. Because the prompt does not specify that Silas factually *did* validly withdraw (and in fact suggests his withdrawal might be incomplete), his claim could be invalid *both* because of the legal rule in (c) and because his actions were factually insufficient as described in (a), (b), or (d). Furthermore, under the MPC, renunciation *is* a defense to conspiracy if the defendant thwarts the crime; thus, (b) is arguably a completely correct legal and factual reason why his claim fails under the MPC. The distractors lack absolute words to lock them into explicitly false legal claims.

Falsifiable claim per distractor:
- (a): "pulling out his phone and stating his intent was not an affirmative act completely inconsistent with the conspiracy" — wrong because stating intent to call 911 *is* arguably an affirmative act, but the option lacks absolute words, making it a debated factual characterization rather than a clear false legal claim.
- (b): "he did not effectively attempt to thwart the completion of the crime before the victim ultimately died" — wrong because under common law, thwarting is not required for mere withdrawal (only for MPC renunciation), but without absolute words locking it as a requirement in "every jurisdiction," it functions as a true factual statement that accurately invalidates an MPC renunciation defense.
- (d): "he did not successfully complete the 911 call to law enforcement before physically leaving the motel room" — wrong because completing a call is not the *only* way to withdraw, but the option does not use absolute words to claim it is the "sole" way, making it a potentially true factual reason why his specific attempt failed.
- (e): "a co-conspirator must successfully turn state's evidence to effectively withdraw" — wrong because turning state's evidence is categorically not a legal requirement for withdrawal.

Recommended fix: Add absolute words to (a), (b), and (d) to lock them into explicitly false legal propositions.
(a) Invalid claim, because withdrawal categorically requires physically restraining co-conspirators.
(b) Invalid claim, because an effective withdrawal solely occurs if the conspirator successfully thwarts the target offense in every jurisdiction.
(d) Invalid claim, because an individual automatically fails to withdraw unless they successfully complete a call to law enforcement.
-->
