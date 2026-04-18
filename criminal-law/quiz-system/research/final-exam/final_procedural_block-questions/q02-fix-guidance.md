# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q2.** Assume that, whether or not Leo is convicted, Chloe is charged with drug possession and as an accomplice to Leo's drug distribution. Which of the following describes her liability?

(a) Guilty of both offenses, because holding the key establishes possession and simple knowledge of the crime establishes accomplice liability.
(b) Guilty of possession but not accomplice liability, because she lacked the purpose to facilitate the distribution despite her control over the stash. <!-- correct -->
(c) Guilty of accomplice liability but not possession, because she did not personally sell the drugs but actively knew of the criminal enterprise.
(d) Not guilty of either offense, because she was merely present at the location and did not actively participate in the illicit narcotics trade.
(e) Guilty of both offenses, because under the natural and probable consequences doctrine, simple possession automatically leads to distribution liability.

**Answer:** (b)

**Explanation:** The correct answer is (b). Constructive possession requires the power and intent to exercise control over an item, which Chloe has by holding the only key to the stash house. However, accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the crime. Chloe explicitly stated she "didn't care if he succeeded or failed" (Fact 3), demonstrating mere knowledge rather than the required purpose (as established in *Peoni* and *Lauria*).

(a) is incorrect because mere knowledge of the principal's criminal intent is insufficient for accomplice liability; true purpose is required.
(c) is incorrect because her control of the key establishes constructive possession, while her lack of purpose defeats accomplice liability.
(d) is incorrect because holding the sole key establishes constructive possession, making her more than merely present.
(e) is incorrect because the natural and probable consequences doctrine applies to the scope of liability for a crime one has *already* purposefully aided, rather than bootstrapping simple possession into accomplice liability for distribution.

**Tags:** chapters: [15, 18], topics: [accomplice-liability, mens-rea-purpose, constructive-possession], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - Accomplice Liability > Mens rea (purpose); Chapter 15 - Drugs and Guns > Constructive Possession

<!-- audit: MUST FIX
check 1: pass (conditional on the missing facts aligning with the explanation).
check 2: pass
check 3: pass
check 4: fails. The question stem is completely missing the underlying fact pattern. The answer options and the explanation heavily rely on facts—such as Chloe "holding the key" and her statement that she "didn't care" ("Fact 3")—that are nowhere to be found in the provided prompt text. A student cannot answer this question as presented.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Integrate the missing facts directly into the stem so the question can function independently (e.g., "Leo operates a drug distribution ring. Chloe holds the sole key to Leo's stash house and is fully aware of the operation, but explicitly states she 'doesn't care if he succeeds or fails.' Assume that...").
-->

## Issue 2 — edge-case

**Q2.** Assume that, whether or not Leo is convicted, Chloe is charged with drug possession and as an accomplice to Leo's drug distribution. Which of the following describes her liability?

(a) Guilty of both offenses, because holding the key establishes possession and simple knowledge of the crime establishes accomplice liability.
(b) Guilty of possession but not accomplice liability, because she lacked the purpose to facilitate the distribution despite her control over the stash. <!-- correct -->
(c) Guilty of accomplice liability but not possession, because she did not personally sell the drugs but actively knew of the criminal enterprise.
(d) Not guilty of either offense, because she was merely present at the location and did not actively participate in the illicit narcotics trade.
(e) Guilty of both offenses, because under the natural and probable consequences doctrine, simple possession automatically leads to distribution liability.

**Answer:** (b)

**Explanation:** The correct answer is (b). Constructive possession requires the power and intent to exercise control over an item, which Chloe has by holding the only key to the stash house. However, accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the crime. Chloe explicitly stated she "didn't care if he succeeded or failed" (Fact 3), demonstrating mere knowledge rather than the required purpose (as established in *Peoni* and *Lauria*).

(a) is incorrect because mere knowledge of the principal's criminal intent is insufficient for accomplice liability; true purpose is required.
(c) is incorrect because her control of the key establishes constructive possession, while her lack of purpose defeats accomplice liability.
(d) is incorrect because holding the sole key establishes constructive possession, making her more than merely present.
(e) is incorrect because the natural and probable consequences doctrine applies to the scope of liability for a crime one has *already* purposefully aided, rather than bootstrapping simple possession into accomplice liability for distribution.

**Tags:** chapters: [15, 18], topics: [accomplice-liability, mens-rea-purpose, constructive-possession], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - Accomplice Liability > Mens rea (purpose); Chapter 15 - Drugs and Guns > Constructive Possession

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The phrase "selling them to pay my rent" gives Chloe a direct financial stake in the drug distribution venture. Under *People v. Lauria*, a "stake in the venture" allows a fact-finder to infer the required *purpose* from mere knowledge. Because her rent depends on his illicit sales, her statement that she "didn't care if he succeeded" is a logical and legal contradiction. Furthermore, controlling "the only key" to a dedicated "stash house" provides a service with no legitimate legal use—another classic *Lauria* exception that elevates knowledge to purpose. This strongly suggests she *does* have the requisite purpose for accomplice liability, undermining the intended answer (b) and making a strong case for (a).
2. Cross-Doctrine Clashes: Constructive possession requires both the *power* and the *intent* to exercise dominion and control over the contraband. The explanation erroneously assumes that holding the key (power over the premises) automatically satisfies the *intent* to control the specific contraband inside. 
3. Cross-Question Spoilers: Pass
Recommended fix: To cleanly establish possession without triggering accomplice liability for distribution, change her role. Make her a roommate who occasionally uses drugs from the open stash for personal consumption (establishing her intent to control/constructive possession of the stash), but ensure she pays her own flat share of the rent from a lawful job so she has no financial stake in his distribution success.
-->

## Issue 3 — argpass-opus

**Q2.** Assume that, whether or not Leo is convicted, Chloe is charged with drug possession and as an accomplice to Leo's drug distribution. Which of the following describes her liability?

(a) Guilty of both offenses, because holding the key establishes possession and simple knowledge of the crime establishes accomplice liability.
(b) Guilty of possession but not accomplice liability, because she lacked the purpose to facilitate the distribution despite her control over the stash. <!-- correct -->
(c) Guilty of accomplice liability but not possession, because she did not personally sell the drugs but actively knew of the criminal enterprise.
(d) Not guilty of either offense, because she was merely present at the location and did not actively participate in the illicit narcotics trade.
(e) Guilty of both offenses, because under the natural and probable consequences doctrine, simple possession automatically leads to distribution liability.

**Answer:** (b)

**Explanation:** The correct answer is (b). Constructive possession requires the power and intent to exercise control over an item, which Chloe has by holding the only key to the stash house. However, accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the crime. Chloe explicitly stated she "didn't care if he succeeded or failed" (Fact 3), demonstrating mere knowledge rather than the required purpose (as established in *Peoni* and *Lauria*).

(a) is incorrect because mere knowledge of the principal's criminal intent is insufficient for accomplice liability; true purpose is required.
(c) is incorrect because her control of the key establishes constructive possession, while her lack of purpose defeats accomplice liability.
(d) is incorrect because holding the sole key establishes constructive possession, making her more than merely present.
(e) is incorrect because the natural and probable consequences doctrine applies to the scope of liability for a crime one has *already* purposefully aided, rather than bootstrapping simple possession into accomplice liability for distribution.

**Tags:** chapters: [15, 18], topics: [accomplice-liability, mens-rea-purpose, constructive-possession], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - Accomplice Liability > Mens rea (purpose); Chapter 15 - Drugs and Guns > Constructive Possession

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might recall that in some jurisdictions or under specific interpretations, knowingly providing a material instrumentality for a serious crime can establish accomplice liability. They could mistakenly believe that this elevated "simple knowledge" serves as a sufficient mens rea across the board. Furthermore, holding the key clearly establishes the dominion and control necessary for possession, making convictions for both offenses seem legally sound.
(b) Argument-for: This is the correct answer. Constructive possession requires the power and intent to exercise dominion and control over an item, which Chloe clearly has by holding the sole key to the stash house. However, accomplice liability generally requires the specific intent or purpose to facilitate the underlying offense (*United States v. Peoni*). Because Chloe explicitly "didn't care if he succeeded or failed," she possessed mere knowledge rather than purpose, shielding her from accomplice liability.
(c) Argument-for: A student might mistakenly believe that possession strictly requires direct physical handling or personal involvement in the sale of the contraband. They might also incorrectly apply general conspiracy or facilitation principles, assuming that active knowledge of a criminal enterprise is fully sufficient to trigger accomplice liability. Thus, they would conclude she is guilty of being an accomplice to the enterprise but not guilty of possession.
(d) Argument-for: A student might over-apply the "mere presence" doctrine, concluding that Chloe's failure to actively participate in the drug sales means she lacks both the actus reus and mens rea for any crime. If they incorrectly view holding the key as merely an incidental detail rather than a legal instrument of dominion and control, they would logically argue she is not guilty of either offense.
(e) Argument-for: A student might conflate criminal doctrines, assuming that the natural and probable consequences doctrine functions as a strict liability bridge between any two associated crimes. They could argue that because distribution is a highly foreseeable consequence of possessing a massive drug stash, her simple possession automatically triggers accomplice liability for the distribution without needing to prove independent purpose.

Head-to-head: 
Option (b) is the clear correct answer because it accurately tracks the *Peoni* rule for accomplice liability (purpose) and the standard for constructive possession (dominion and control). Option (a) provides a strong falsifiable claim by stating "simple knowledge ... establishes accomplice liability." Option (e) explicitly and falsely asserts that possession "automatically leads" to distribution liability. However, options (c) and (d) fail the close-call standard. They rely on implicit legal omissions or factual mischaracterizations rather than explicit, absolutely locked false legal claims. Option (c) implicitly rests on the premise that personal sale is required for possession, while (d) incorrectly applies the facts by calling Chloe "merely present" despite her holding the key. 

Falsifiable claim per distractor:
- (a): "simple knowledge of the crime establishes accomplice liability" — wrong because accomplice liability generally requires the specific purpose to promote or facilitate the crime, not merely simple knowledge.
- (c): "because she did not personally sell the drugs but actively knew of the criminal enterprise" — wrong because it relies on the implicit (and false) rule that personal sale is required for possession; lacks an explicit, absolute legal falsifier.
- (d): "because she was merely present at the location and did not actively participate" — wrong primarily on the facts (holding the sole key establishes control, defeating mere presence), and completely lacks an explicitly locked false legal claim.
- (e): "simple possession automatically leads to distribution liability" — wrong because the natural and probable consequences doctrine requires purposeful aiding of a target crime, not an "automatic" bootstrap from simple possession.

Recommended fix: Update (c) and (d) to feature explicitly locked false legal claims using absolute words. Edit (c) to: "Guilty of accomplice liability but not possession, because constructive possession categorically requires personally selling the drugs." Edit (d) to: "Not guilty of either offense, because constructive possession always requires direct physical handling of the illicit narcotics."
-->
