# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** Silas is charged with possessing the drugs located inside the locked bedroom of the stash house. Can the state establish that Silas possessed the drugs in that room?

(a) Yes, because holding the only key to the locked bedroom demonstrates his power and intention to exercise exclusive control over the contraband inside. <!-- correct -->
(b) No, because the police interrupted him in the living room before he could physically access the locked bedroom or directly touch the drugs.
(c) Yes, because his presence in the same overall building creates an irrebuttable legal presumption of possession for all illegal substances on the premises.
(d) No, because constructive possession requires proof that he actually purchased or manufactured the drugs, rather than merely having temporary access to the room.
(e) Yes, because constructive possession only requires mere proximity to the illegal items, regardless of whether the defendant had the ability to control them.

**Answer:** (a)

**Explanation:** Constructive possession is established when a person lacks physical custody but possesses the power and intention to exercise control over the item. Holding the sole key to a locked room containing contraband establishes exclusive control. (b) is wrong because actual physical contact is not required for constructive possession. (c) is wrong because mere presence in a building does not create an irrebuttable presumption of possession. (d) is wrong because possession relies on current control, not historical procurement or manufacture. (e) is wrong because mere proximity without the power to exercise control is insufficient to prove constructive possession.

**Tags:** chapters: [15], topics: [constructive-possession, drugs], difficulty: easy, cognitive: application

**Grounding:** Chapter 15, Section: Possession Mechanics

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem completely omits the critical facts that are referenced in the answer choices (that Silas held the only key, and that he was interrupted in the living room). The student has to infer the facts from the answers, which violates standard exam drafting principles.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Add the missing facts to the stem. For example: "Police raid a stash house and find Silas in the living room. They discover drugs in a locked bedroom. Silas is found to be carrying the only key to that bedroom. Silas is charged..."
-->

## Issue 2 — argpass-opus

**Q3.** Silas is charged with possessing the drugs located inside the locked bedroom of the stash house. Can the state establish that Silas possessed the drugs in that room?

(a) Yes, because holding the only key to the locked bedroom demonstrates his power and intention to exercise exclusive control over the contraband inside. <!-- correct -->
(b) No, because the police interrupted him in the living room before he could physically access the locked bedroom or directly touch the drugs.
(c) Yes, because his presence in the same overall building creates an irrebuttable legal presumption of possession for all illegal substances on the premises.
(d) No, because constructive possession requires proof that he actually purchased or manufactured the drugs, rather than merely having temporary access to the room.
(e) Yes, because constructive possession only requires mere proximity to the illegal items, regardless of whether the defendant had the ability to control them.

**Answer:** (a)

**Explanation:** Constructive possession is established when a person lacks physical custody but possesses the power and intention to exercise control over the item. Holding the sole key to a locked room containing contraband establishes exclusive control. (b) is wrong because actual physical contact is not required for constructive possession. (c) is wrong because mere presence in a building does not create an irrebuttable presumption of possession. (d) is wrong because possession relies on current control, not historical procurement or manufacture. (e) is wrong because mere proximity without the power to exercise control is insufficient to prove constructive possession.

**Tags:** chapters: [15], topics: [constructive-possession, drugs], difficulty: easy, cognitive: application

**Grounding:** Chapter 15, Section: Possession Mechanics

<!-- argument-pass: MUST FIX
(a) Argument-for: Option (a) correctly states the rule for constructive possession, which applies when a defendant lacks actual physical custody but has the power and intent to control an item. By positing that Silas holds the only key to the locked bedroom, the option establishes his exclusive dominion and control over the drugs inside. This perfectly satisfies the standard for constructive possession, leading to the correct conclusion that the state can establish possession.
(b) Argument-for: A student could argue that constructive possession requires a present and immediate ability to exercise control over the contraband. Because the police intercepted Silas in the living room, he was geographically and physically separated from the drugs by a locked door. Consequently, one could argue he lacked the imminent "power" required for possession, meaning the interception successfully prevented the crime of possession from vesting.
(c) Argument-for: If a student views the location as a dedicated "stash house," they might believe special rules apply to such criminally purposed properties. One could argue that entering a purely illegal environment inherently establishes complicity and control over the contents. Under this theory, the law might impose an irrebuttable presumption of joint possession for anyone found inside, making his mere presence legally sufficient to establish possession.
(d) Argument-for: Constructive possession requires not just power, but the intention to exercise control over the item. A student could argue that mere temporary access to a room does not prove intent to control the specific contraband inside unless there is evidence of ownership or a proprietary relationship to the drugs. Therefore, proving he purchased or manufactured them would be necessary to establish the requisite intent, distinguishing him from a mere visitor.
(e) Argument-for: In the context of a stash house, a student might argue that the standard for possession is significantly relaxed due to the nature of the premises. They could argue that because the entire house is devoted to illegal drugs, anyone in close physical proximity is deemed to possess them. Thus, proximity alone becomes the operational standard for constructive possession, overriding the traditional need to prove a specific ability to control.

Head-to-head: 
Option (a) presents a textbook application of constructive possession, correctly noting that holding the sole key establishes the requisite dominion and control. However, (a) relies on a critical fact ("holding the only key") that is entirely absent from the question stem! The distractors (b), (c), (d), and (e) are all properly constructed with explicitly false, falsifiable legal rules locked by absolute language (e.g., "irrebuttable legal presumption," "requires proof that he actually purchased," "regardless of whether"). Because the correct answer relies on unstated facts, it cannot logically follow from the prompt as written. This mandates a fix to the stem.

Falsifiable claim per distractor:
- (b): "[N]o, because the police interrupted him... before he could physically access... or directly touch the drugs" — wrong because constructive possession categorically does not require physical access or direct touching; power and intent to control suffice.
- (c): "[C]reates an irrebuttable legal presumption of possession for all illegal substances" — wrong because mere presence never creates an irrebuttable presumption of possession in criminal law.
- (d): "[C]onstructive possession requires proof that he actually purchased or manufactured the drugs" — wrong because dominion and control do not require historical procurement or manufacture; a person can constructively possess drugs belonging to or made by someone else.
- (e): "[C]onstructive possession only requires mere proximity... regardless of whether the defendant had the ability to control them" — wrong because the ability to control is a definitional, mandatory requirement of constructive possession.

Recommended fix: Add "When arrested, Silas was holding the only key to that bedroom." to the end of the question stem.
-->
