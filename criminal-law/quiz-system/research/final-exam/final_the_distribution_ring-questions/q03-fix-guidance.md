# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** Assume that, whether or not Darius's conduct satisfied the actus reus, he is convicted of attempted murder. How will his punishment for the attempt compare to the punishment he would have received had he successfully killed Vance?

(a) Under the majority rule, his attempt will be graded equally to the completed offense because he acted with the specific intent to kill Vance, which demonstrates his heightened culpability.
(b) Under the MPC, his attempt will be graded one degree lower than completed murder to reflect the lack of harm, whereas the common law routinely grades the attempt equally.
(c) In most states, the attempt will be punished one grade below the completed offense, but under the MPC's general grading rule, attempts carry the same penalty as the completed crime. <!-- correct -->
(d) He will face a mandatory life sentence under either approach because attempted murder is a structurally inchoate offense that cannot be reduced by the judge at the sentencing phase.
(e) His punishment will be determined solely by the felony murder rule because the incomplete attempt involved the use of a deadly weapon during the commission of a dangerous felony.

**Answer:** (c)

**Explanation:** The correct answer is (c). Most states (majority rule) punish attempts one grade below the completed offense. The MPC's general rule grades attempts identically to the completed offense (with exceptions for capital/first-degree crimes). (a) is wrong because it misstates both rules; specific intent does not dictate equal grading under the majority rule. (b) reverses the rules, falsely attributing the grading reduction to the MPC. (d) is wrong because attempt is not a structurally inchoate offense like burglary, and judges retain sentencing discretion. (e) is wrong because felony murder attaches to resulting deaths, not incomplete attempts where no one dies.

**Tags:** chapters: [17], topics: [attempt, grading, punishment], difficulty: easy, cognitive: recall

**Grounding:** Chapter 17: grading-mpc-equal, grading-general-reduction

<!-- audit: MUST FIX
Check 1: Fails. The marked answer (c) relies on the MPC's general equal-grading rule to imply that Darius's attempted murder would carry the same penalty as completed murder. However, under MPC § 5.05(1), there is an explicit exception: attempts to commit a capital crime or first-degree felony (like murder) are downgraded to a second-degree felony. Therefore, under the MPC, Darius's punishment for attempted murder *would* be one grade lower than completed murder. 
Check 2: Pass. No distractor is entirely correct (option b gets the MPC result for Darius right but misstates the common law), but the correct answer is substantively non-responsive/misleading as applied to the specific crime in the prompt.
Check 3: Fails. The explanation explicitly notes the MPC exception for "capital/first-degree crimes" but fails to recognize that the prompt's crime (murder) is a first-degree crime that triggers this exact exception.
Check 4: Pass.
Check 5: Pass.
Check 6: Pass.
Check 7: Pass.
Recommended fix: Change the target offense in the prompt from "attempted murder" to a lesser felony (e.g., "attempted theft" or "attempted burglary") so that the MPC's general equal-grading rule actually applies to Darius without triggering the first-degree felony exception. Alternatively, rewrite the options to correctly acknowledge that both the majority rule and the MPC would grade *this specific attempt* (murder) lower than the completed crime.
-->

## Issue 2 — edge-case

**Q3.** Assume that, whether or not Darius's conduct satisfied the actus reus, he is convicted of attempted murder. How will his punishment for the attempt compare to the punishment he would have received had he successfully killed Vance?

(a) Under the majority rule, his attempt will be graded equally to the completed offense because he acted with the specific intent to kill Vance, which demonstrates his heightened culpability.
(b) Under the MPC, his attempt will be graded one degree lower than completed murder to reflect the lack of harm, whereas the common law routinely grades the attempt equally.
(c) In most states, the attempt will be punished one grade below the completed offense, but under the MPC's general grading rule, attempts carry the same penalty as the completed crime. <!-- correct -->
(d) He will face a mandatory life sentence under either approach because attempted murder is a structurally inchoate offense that cannot be reduced by the judge at the sentencing phase.
(e) His punishment will be determined solely by the felony murder rule because the incomplete attempt involved the use of a deadly weapon during the commission of a dangerous felony.

**Answer:** (c)

**Explanation:** The correct answer is (c). Most states (majority rule) punish attempts one grade below the completed offense. The MPC's general rule grades attempts identically to the completed offense (with exceptions for capital/first-degree crimes). (a) is wrong because it misstates both rules; specific intent does not dictate equal grading under the majority rule. (b) reverses the rules, falsely attributing the grading reduction to the MPC. (d) is wrong because attempt is not a structurally inchoate offense like burglary, and judges retain sentencing discretion. (e) is wrong because felony murder attaches to resulting deaths, not incomplete attempts where no one dies.

**Tags:** chapters: [17], topics: [attempt, grading, punishment], difficulty: easy, cognitive: recall

**Grounding:** Chapter 17: grading-mpc-equal, grading-general-reduction

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: The MPC's general equal-grading rule (MPC 5.05(1)) contains an explicit exception for first-degree felonies and capital crimes, downgrading them to second-degree felonies. Because Darius is convicted of attempted *murder* (a first-degree felony/capital crime), the MPC *would* actually reduce his punishment. Option (c) incorrectly implies that under the MPC, Darius's attempt carries the same penalty as completed murder by relying solely on the general rule, making the answer legally inaccurate as applied to this specific defendant's crime. 
3. Cross-Question Spoilers: pass
Recommended fix: Adjust option (c) to acknowledge the exception. For example: "(c) In most states, his attempt will be punished one grade below the completed offense; under the MPC, attempts generally carry the same penalty as the completed crime, though his attempted murder would be explicitly reduced to a second-degree felony." Alternatively, change the question stem to ask purely about the general rules rather than applying them to Darius ("How do the general rules for grading attempts compare...?").
-->

## Issue 3 — argpass-sonnet

**Q3.** Assume that, whether or not Darius's conduct satisfied the actus reus, he is convicted of attempted murder. How will his punishment for the attempt compare to the punishment he would have received had he successfully killed Vance?

(a) Under the majority rule, his attempt will be graded equally to the completed offense because he acted with the specific intent to kill Vance, which demonstrates his heightened culpability.
(b) Under the MPC, his attempt will be graded one degree lower than completed murder to reflect the lack of harm, whereas the common law routinely grades the attempt equally.
(c) In most states, the attempt will be punished one grade below the completed offense, but under the MPC's general grading rule, attempts carry the same penalty as the completed crime. <!-- correct -->
(d) He will face a mandatory life sentence under either approach because attempted murder is a structurally inchoate offense that cannot be reduced by the judge at the sentencing phase.
(e) His punishment will be determined solely by the felony murder rule because the incomplete attempt involved the use of a deadly weapon during the commission of a dangerous felony.

**Answer:** (c)

**Explanation:** The correct answer is (c). Most states (majority rule) punish attempts one grade below the completed offense. The MPC's general rule grades attempts identically to the completed offense (with exceptions for capital/first-degree crimes). (a) is wrong because it misstates both rules; specific intent does not dictate equal grading under the majority rule. (b) reverses the rules, falsely attributing the grading reduction to the MPC. (d) is wrong because attempt is not a structurally inchoate offense like burglary, and judges retain sentencing discretion. (e) is wrong because felony murder attaches to resulting deaths, not incomplete attempts where no one dies.

**Tags:** chapters: [17], topics: [attempt, grading, punishment], difficulty: easy, cognitive: recall

**Grounding:** Chapter 17: grading-mpc-equal, grading-general-reduction

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that option (a) represents the correct underlying theory of modern attempt law as adopted by the majority. Because the actus reus and mens rea of an attempt demonstrate the same specific intent and moral culpability as the completed offense, modern penal theory suggests they should be punished equally. A student might assume that the "majority rule" has formally adopted this culpability-based approach. Furthermore, they could argue that for a severe crime like attempted murder, most states make no grading distinction.
(b) Argument-for: A student could strongly defend option (b) by pointing out that under MPC § 5.05(1), attempt is generally graded equally *except* for capital crimes and first-degree felonies. Since completed murder is a first-degree felony under the MPC, attempted murder is graded as a second-degree felony—exactly "one degree lower," making the first half of (b) perfectly accurate. The student might then assume that the strict common law graded attempts equally to completed crimes, justifying the second half.
(c) Argument-for: A student could argue that option (c) correctly identifies the standard pedagogical distinction between the majority rule and the MPC. In most states, attempts are graded one level below the completed offense to reflect the lack of resulting harm. Conversely, the MPC's *general* grading provision (MPC § 5.05) equalizes the punishment for inchoate and completed offenses, emphasizing the actor's culpability over the harm. This option provides the standard black-letter comparison taught in criminal law.
(d) Argument-for: A student could argue that attempted murder is a uniquely severe inchoate offense that triggers mandatory sentencing schemes. They might interpret "structurally inchoate" to mean that the crime is fully complete upon the attempt itself, stripping judges of the discretion to depart downward from mandatory life sentences. Therefore, they could conclude that judicial reduction at sentencing is categorically prohibited.
(e) Argument-for: A student could defend (e) by incorrectly importing the felony-murder rule into the attempt context. If Darius was committing a dangerous felony and used a deadly weapon, the student might believe that the "attempted felony murder" doctrine strictly controls. Under this theory, the strict liability mechanism of the felony-murder rule entirely determines the punishment, stripping away standard attempt grading rules.

Head-to-head: Option (c) is the keyed answer and captures the general distinction between the majority reduction rule and the MPC's equal-grading rule. However, option (b) accurately reflects a major structural flaw in the question: under MPC § 5.05(1), attempted murder is an exception to the general equal-grading rule and is actually graded one degree lower (second-degree felony). Because the prompt specifically asks how *his* punishment compares, the implication in (c) that his attempt carries the same penalty under the MPC is legally incorrect for murder, while the MPC half of (b) is correct. The distractors (a), (b), (d), and (e) all contain explicit falsifiable errors in their second clauses or majority rules, but (c) must be edited to account for the first-degree felony exception under the MPC if the underlying crime is attempted murder.

Falsifiable claim per distractor:
- (a): "Under the majority rule, his attempt will be graded equally" — wrong because the majority of non-MPC jurisdictions grade attempts lower (typically one class or degree below) than the completed offense.
- (b): "whereas the common law routinely grades the attempt equally" — wrong because at common law, attempts were generally punished as misdemeanors, significantly lower than completed felonies like murder.
- (d): "He will face a mandatory life sentence under either approach" — wrong because attempt sentencing does not categorically carry mandatory life, and judges generally retain sentencing discretion.
- (e): "determined solely by the felony murder rule" — wrong because felony murder requires a resulting death, and attempted felony murder is largely a conceptual impossibility unpunished by the strict liability of the felony-murder rule.

Recommended fix: Change the underlying crime in the prompt from "attempted murder" to a lesser felony (e.g., "attempted robbery") so that the MPC's equal-grading rule applies without triggering the first-degree/capital exception under MPC § 5.05(1). Alternatively, change (c) to explicitly acknowledge the MPC exception for murder.
-->

## Issue 4 — argpass-opus

**Q3.** Assume that, whether or not Darius's conduct satisfied the actus reus, he is convicted of attempted murder. How will his punishment for the attempt compare to the punishment he would have received had he successfully killed Vance?

(a) Under the majority rule, his attempt will be graded equally to the completed offense because he acted with the specific intent to kill Vance, which demonstrates his heightened culpability.
(b) Under the MPC, his attempt will be graded one degree lower than completed murder to reflect the lack of harm, whereas the common law routinely grades the attempt equally.
(c) In most states, the attempt will be punished one grade below the completed offense, but under the MPC's general grading rule, attempts carry the same penalty as the completed crime. <!-- correct -->
(d) He will face a mandatory life sentence under either approach because attempted murder is a structurally inchoate offense that cannot be reduced by the judge at the sentencing phase.
(e) His punishment will be determined solely by the felony murder rule because the incomplete attempt involved the use of a deadly weapon during the commission of a dangerous felony.

**Answer:** (c)

**Explanation:** The correct answer is (c). Most states (majority rule) punish attempts one grade below the completed offense. The MPC's general rule grades attempts identically to the completed offense (with exceptions for capital/first-degree crimes). (a) is wrong because it misstates both rules; specific intent does not dictate equal grading under the majority rule. (b) reverses the rules, falsely attributing the grading reduction to the MPC. (d) is wrong because attempt is not a structurally inchoate offense like burglary, and judges retain sentencing discretion. (e) is wrong because felony murder attaches to resulting deaths, not incomplete attempts where no one dies.

**Tags:** chapters: [17], topics: [attempt, grading, punishment], difficulty: easy, cognitive: recall

**Grounding:** Chapter 17: grading-mpc-equal, grading-general-reduction

<!-- argument-pass: MUST FIX
(a) Argument-for: A student might argue that because attempt requires specific intent to commit the target offense, the actor's culpability is fully formed. If they conflate the MPC's general equal-grading philosophy with the majority rule, they might conclude that majority jurisdictions punish attempts equally due to this heightened mens rea.
(b) Argument-for: A student could correctly recall that under MPC § 5.05(1), an attempt to commit a first-degree felony (such as murder) is explicitly downgraded to a second-degree felony. Therefore, his specific attempt *will* be graded one degree lower under the MPC. They might accept the second clause about the common law as a colloquial reference to modern statutory trends, making this a highly plausible answer based on the actual MPC outcome for this specific crime.
(c) Argument-for: A student will recognize this as the classic textbook comparison: most states downgrade attempts by one level, whereas the MPC's general framework punishes attempts at the same grade as the completed crime. The explicit reference to the "general grading rule" signals that the question is testing the broad doctrinal difference rather than the MPC's specific exception for first-degree felonies.
(d) Argument-for: A student might incorrectly classify attempt as a rigid sentencing mechanism rather than a separate substantive offense, reasoning that "attempted murder" locks in a mandatory life sentence in tough-on-crime jurisdictions, thereby categorically removing a judge's downward departure discretion.
(e) Argument-for: A student might mistakenly apply the felony murder doctrine to an incomplete crime, reasoning that the strict liability nature of felony murder transfers to the attempt, dictating the punishment solely based on the use of a deadly weapon during a dangerous felony.

Head-to-head:
Option (c) is the keyed answer, testing the broad doctrinal split between the majority rule (one grade lower) and the MPC general rule (equal grading). However, the question facts involve attempted *murder*. Under MPC § 5.05(1), while the general rule is equal grading, an attempt to commit a capital crime or first-degree felony (like murder) is explicitly downgraded to a second-degree felony. Therefore, applied to Darius, the MPC *would* grade his attempt lower than the completed offense. Option (b) accurately describes the MPC outcome for Darius, even though its clause about the common law is false. The conflict between the general MPC rule stated in (c) and the specific MPC application to the tested crime (murder) makes the key dangerously misleading.

Falsifiable claim per distractor:
- (a): "Under the majority rule, his attempt will be graded equally to the completed offense" — wrong because the majority rule generally grades attempts one degree lower than the completed crime.
- (b): "the common law routinely grades the attempt equally" — wrong because historical common law treated attempts as misdemeanors (much lower than the completed felonies), and modern common law typically downgrades them.
- (d): "cannot be reduced by the judge at the sentencing phase" — wrong because attempt is not structurally exempt from judicial sentencing discretion across all jurisdictions.
- (e): "determined solely by the felony murder rule" — wrong because the felony murder rule applies only when a death results, which is absent in an incomplete attempt.

Recommended fix: Change the underlying crime in the prompt from "attempted murder" to a lesser felony (e.g., "attempted robbery" or "attempted arson") so that the MPC's general equal-grading rule directly applies to his punishment, cleanly avoiding the first-degree felony exception.
-->
