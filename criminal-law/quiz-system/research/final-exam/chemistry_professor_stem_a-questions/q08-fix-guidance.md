# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q8.** The prosecution charges Chloe with possessing the bulk supply of Compound Y found in the locked safe inside the van. Is Chloe guilty of possessing the bulk drugs?

(a) Yes, because as the owner of the van who kept the only set of vehicle keys, she had constructive possession of all its contents.
(b) No, because she did not have access to or control over the locked safe, as Arthur was the only person who knew the combination. <!-- correct -->
(c) Yes, because she and Arthur were partners in the drug operation, making them joint possessors of the safe's contents by law.
(d) No, because she never physically handled the bulk supply of Compound Y, precluding any finding of possession.
(e) Yes, because her knowledge that the drugs were in the van is sufficient to establish constructive possession.

**Answer:** (b)

**Explanation:** Constructive possession requires both awareness of the contraband and the ability to exercise dominion and control over it. Because Arthur was the only person with the combination to the locked safe, Chloe lacked the physical ability to access or control the contents, defeating constructive possession. (a) is wrong because vehicle ownership does not automatically establish control over a locked container within it to which the owner has no access. (c) is wrong because partnership in an enterprise does not substitute for the physical ability to control the specific contraband. (d) is wrong because physical handling is not required; constructive possession can suffice if control exists. (e) is wrong because mere knowledge is insufficient without the power and intention to exercise control.

**Tags:** chapters: [15], topics: [constructive possession, dominion and control], difficulty: medium, cognitive: application

**Grounding:** cp-exclusive-control

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Pinkerton & Accomplice Liability. Because Chloe and Arthur are co-conspirators in a drug distribution enterprise, Chloe is legally guilty of Arthur's substantive possession of the bulk drugs under Pinkerton liability. She also likely has accomplice liability for his possession, as she provided the van to store them. Therefore, a definitive "No" answer to the broad question "Is Chloe guilty of possessing the bulk drugs?" is legally incorrect. 
3. Cross-Question Spoilers: Q9 and Q11 explicitly establish and test Chloe's conspiracy and Pinkerton liability, priming the student to realize she is guilty of Arthur's foreseeable substantive crimes in furtherance of the conspiracy.
Recommended fix: Change the call of the question to specifically isolate the tested doctrine. Change "Is Chloe guilty of possessing the bulk drugs?" to "Did Chloe have constructive possession of the bulk drugs?"
-->

## Issue 3 — argpass-opus

### Stem 2: Charges Against Chloe

The prosecution is evaluating charges against Chloe Vance. Although she did not synthesize the drugs or personally hand them to Marcus, she provided the van, stopped Arthur from calling 911, and helped hide the body.

**Q8.** The prosecution charges Chloe with possessing the bulk supply of Compound Y found in the locked safe inside the van. Is Chloe guilty of possessing the bulk drugs?

(a) Yes, because as the owner of the van who kept the only set of vehicle keys, she had constructive possession of all its contents.
(b) No, because she did not have access to or control over the locked safe, as Arthur was the only person who knew the combination. <!-- correct -->
(c) Yes, because she and Arthur were partners in the drug operation, making them joint possessors of the safe's contents by law.
(d) No, because she never physically handled the bulk supply of Compound Y, precluding any finding of possession.
(e) Yes, because her knowledge that the drugs were in the van is sufficient to establish constructive possession.

**Answer:** (b)

**Explanation:** Constructive possession requires both awareness of the contraband and the ability to exercise dominion and control over it. Because Arthur was the only person with the combination to the locked safe, Chloe lacked the physical ability to access or control the contents, defeating constructive possession. (a) is wrong because vehicle ownership does not automatically establish control over a locked container within it to which the owner has no access. (c) is wrong because partnership in an enterprise does not substitute for the physical ability to control the specific contraband. (d) is wrong because physical handling is not required; constructive possession can suffice if control exists. (e) is wrong because mere knowledge is insufficient without the power and intention to exercise control.

**Tags:** chapters: [15], topics: [constructive possession, dominion and control], difficulty: medium, cognitive: application

**Grounding:** cp-exclusive-control

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that Chloe's exclusive control over the van (holding the only keys) legally extends to everything inside the vehicle. In property and criminal contexts, the owner of a vehicle who restricts access to it is often presumed to have constructive possession of its contents, meaning her dominion over the macro-container (the van) establishes dominion over the micro-container (the safe).
(b) Argument-for: A student would correctly argue that constructive possession requires both knowledge of the contraband and the power and intent to exercise dominion and control over it. Because Chloe did not know the combination to the safe, she was physically unable to access it, meaning she lacked the requisite power to control the bulk drugs inside regardless of her ownership of the van.
(c) Argument-for: A student could argue that under principles of joint enterprise or co-conspirator liability (Pinkerton), partners in a drug operation share possession of the operation's inventory. Thus, Arthur's physical access to the safe would be legally imputed to Chloe as his partner, making them joint possessors of the enterprise's assets.
(d) Argument-for: A student could argue that actual possession requires physical control or handling of the object. Relying on a strict interpretation of possession, the student might conclude that because Chloe never physically handled the drugs, she cannot be charged with possession, dismissing constructive possession entirely since the container was locked.
(e) Argument-for: A student could argue that knowing contraband is stored in one's own vehicle constitutes constructive possession. Since she provided the van and knew the drugs were there, a student might deduce that her knowing accommodation of the drugs on her property is sufficient to establish possession.

Head-to-head: Option (b) correctly identifies that constructive possession requires both knowledge and the ability to exercise dominion and control, which Chloe lacked regarding the locked safe. Option (d) is easily defeated because it ignores constructive possession entirely, falsely claiming physical handling is required. Option (e) falsely claims that knowledge alone is sufficient, ignoring the dominion and control element. Option (c) incorrectly asserts that partnership automatically establishes joint possession "by law," improperly substituting conspiracy/accomplice liability concepts for the distinct elements of possessory control. Option (a) applies a flawed premise that controlling the exterior vehicle grants constructive possession over a locked interior container accessed exclusively by someone else, though it could use an absolute word to be perfectly falsifiable.

Falsifiable claim per distractor:
- (a): "she had constructive possession of all its contents" — wrong because controlling a vehicle does not legally establish dominion and control over a locked container inside it to which the defendant lacks access.
- (c): "making them joint possessors of the safe's contents by law" — wrong because partnership does not categorically establish possession "by law" if the defendant lacks the actual ability to control the specific locked container.
- (d): "precluding any finding of possession" — wrong because lack of physical handling does not preclude "any" finding; constructive possession remains possible without physical handling.
- (e): "her knowledge... is sufficient to establish constructive possession" — wrong because knowledge alone is categorically insufficient; the ability to exercise dominion and control is also required.

Recommended fix: In (a), add "automatically" to lock the false legal claim: "(a) Yes, because as the owner of the van who kept the only set of vehicle keys, she automatically had constructive possession of all its contents."
-->
