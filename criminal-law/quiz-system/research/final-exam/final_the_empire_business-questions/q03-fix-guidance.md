# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** Did Laura constructively possess the two kilograms of cocaine stored in the locked duffel bag in the breakroom?

(a) Possessed, because she had actual knowledge that the locked duffel bag contained cocaine and it was located in a shared employee breakroom.
(b) Not possessed, because her explicit demand to remove the bag demonstrates she lacked the necessary intent to exercise dominion and control over it. <!-- correct -->
(c) Possessed, because her failure to immediately report the contraband to law enforcement legally constituted an implicit adoption of Kevin's possession.
(d) Not possessed, because a civilian employee cannot constructively possess illegal contraband when it is located inside a commercial workplace setting.
(e) Possessed, because she engaged in an incriminating dialogue with a co-worker regarding the exact location and contents of the illicit materials.

**Answer:** (b)

**Explanation:** Constructive possession requires proof that the defendant both knew of the contraband's presence and had the power and intent to exercise dominion and control over it. Laura's demand that Kevin remove the bag shows she had no intent to control it, and her lack of the combination shows a lack of power. Option (a) fails because awareness of contraband in a shared space is insufficient without dominion and control. Option (c) fails because failure to report does not equate to exercising control. Option (d) fails because constructive possession applies perfectly well in commercial settings if the elements are met. Option (e) fails because while her statement proves awareness, it directly negates intent to control, rendering the statement insufficient to establish possession.

**Tags:** chapters: [15], topics: [constructive possession, awareness vs dominion], difficulty: medium, cognitive: application

**Grounding:** Chapter 15 (State of Louisiana v. Gerald Manchip White)

<!-- audit: MUST FIX
Check 1: pass (The legal rule for constructive possession in the explanation is accurate).
Check 2: pass (Assuming the facts align with the explanation, the distractors rely on legally incorrect doctrines).
Check 3: pass (The explanation correctly applies the dominion and control standard).
Check 4: MUST FIX. The question stem is entirely missing the fact pattern. It references "Laura," "Kevin," a "locked duffel bag," "the breakroom," and an "explicit demand," but absolutely none of these facts are provided in the prompt. Students have nothing to read to answer the question.
Check 5: pass (Constructive possession is standard doctrine; no specific jurisdictional split needs resolving here).
Check 6: pass (No excluded-topic bleed).
Check 7: pass (Constructive possession is standard Chapter 15 material).
Check 8: pass (Options are symmetrical in length and structure).
Recommended fix: Add the missing factual scenario detailing Laura and Kevin's interaction in the breakroom, Laura's lack of the bag's combination, and her explicit demand that he remove it, immediately before the question stub.
-->

## Issue 2 — argpass-sonnet

**Q3.** Did Laura constructively possess the two kilograms of cocaine stored in the locked duffel bag in the breakroom?

(a) Possessed, because she had actual knowledge that the locked duffel bag contained cocaine and it was located in a shared employee breakroom.
(b) Not possessed, because her explicit demand to remove the bag demonstrates she lacked the necessary intent to exercise dominion and control over it. <!-- correct -->
(c) Possessed, because her failure to immediately report the contraband to law enforcement legally constituted an implicit adoption of Kevin's possession.
(d) Not possessed, because a civilian employee cannot constructively possess illegal contraband when it is located inside a commercial workplace setting.
(e) Possessed, because she engaged in an incriminating dialogue with a co-worker regarding the exact location and contents of the illicit materials.

**Answer:** (b)

**Explanation:** Constructive possession requires proof that the defendant both knew of the contraband's presence and had the power and intent to exercise dominion and control over it. Laura's demand that Kevin remove the bag shows she had no intent to control it, and her lack of the combination shows a lack of power. Option (a) fails because awareness of contraband in a shared space is insufficient without dominion and control. Option (c) fails because failure to report does not equate to exercising control. Option (d) fails because constructive possession applies perfectly well in commercial settings if the elements are met. Option (e) fails because while her statement proves awareness, it directly negates intent to control, rendering the statement insufficient to establish possession.

**Tags:** chapters: [15], topics: [constructive possession, awareness vs dominion], difficulty: medium, cognitive: application

**Grounding:** Chapter 15 (State of Louisiana v. Gerald Manchip White)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that actual knowledge combined with proximity in a jointly occupied space gives rise to a presumption of constructive possession. Under some interpretations, knowing contraband is in a shared area and failing to remove oneself establishes sufficient nexus to the illicit goods. Therefore, Laura's awareness and the bag's location in a space she had access to could be seen as satisfying the elements of possession.
(b) Argument-for: Constructive possession requires both the power and the intent to exercise dominion and control over the contraband. The facts indicate Laura explicitly demanded that Kevin remove the bag, demonstrating her rejection of the item rather than an intent to control it. Mere knowledge of its presence without the requisite intent or capability (since it was locked and she lacked the combination) means she cannot be held to have constructively possessed it, making this clearly correct.
(c) Argument-for: A student could contend that in certain legal contexts, failing to report known contraband constitutes an act of harboring or adopting possession. By knowing of the cocaine and choosing not to notify law enforcement, Laura arguably acquiesced to its presence on the premises. This "implicit adoption" could be misconstrued as exercising a form of dominion, fulfilling the requirements for constructive possession.
(d) Argument-for: A student could argue that constructive possession doctrine is traditionally applied to residential settings, vehicles, or personal items, rather than commercial workplaces where employees lack general dominion over the premises. Because an ordinary civilian employee does not have authority over a shared commercial breakroom in the same way a homeowner does over a living room, they might mistakenly believe an employee categorically cannot form constructive possession over items left there.
(e) Argument-for: Engaging in an "incriminating dialogue" about the location and contents of the bag demonstrates a high degree of specific knowledge. A student might argue that such detailed knowledge proves Laura was involved in the possession enterprise with Kevin. In drug cases, detailed discussions about the contraband are often used as circumstantial evidence of dominion and control, making this option a plausible trap.

Head-to-head: Option (b) is the clear winner because it correctly applies the rule of constructive possession, explicitly noting that her demand to remove the bag negates the intent to exercise dominion and control. Options (c) and (d) are strong distractors because they contain explicitly false legal claims ("legally constituted an implicit adoption" and "cannot constructively possess"). However, Options (a) and (e) are weaker distractors under the close-call standard because they lack absolute phrasing. They simply state "Possessed, because [Fact]," relying on the *implicit omission* of the dominion/control requirement rather than an explicitly false, falsifiable legal rule.

Falsifiable claim per distractor:
- (a): "Possessed, because she had actual knowledge..." — wrong because knowledge without intent/power to control is insufficient. However, this FAILS the close-call standard because it lacks an absolute word (like "solely") to make the legal claim explicitly false rather than just incomplete.
- (c): "legally constituted an implicit adoption" — wrong because there is no legal doctrine where failure to report automatically constitutes an adoption of possession.
- (d): "cannot constructively possess... inside a commercial workplace setting" — wrong because constructive possession can occur in commercial settings.
- (e): "Possessed, because she engaged in an incriminating dialogue..." — wrong because dialogue alone doesn't establish dominion. Like (a), this FAILS the close-call standard as it lacks an absolute word, relying on implied sufficiency.

Recommended fix: Add absolute words to (a) and (e) to lock their false legal claims.
Change (a) to: "Possessed, solely because she had actual knowledge that the locked duffel bag contained cocaine and it was located in a shared employee breakroom."
Change (e) to: "Possessed, because engaging in an incriminating dialogue with a co-worker regarding illicit materials automatically establishes dominion and control."
-->

## Issue 3 — argpass-opus

**Q3.** Did Laura constructively possess the two kilograms of cocaine stored in the locked duffel bag in the breakroom?

(a) Possessed, because she had actual knowledge that the locked duffel bag contained cocaine and it was located in a shared employee breakroom.
(b) Not possessed, because her explicit demand to remove the bag demonstrates she lacked the necessary intent to exercise dominion and control over it. <!-- correct -->
(c) Possessed, because her failure to immediately report the contraband to law enforcement legally constituted an implicit adoption of Kevin's possession.
(d) Not possessed, because a civilian employee cannot constructively possess illegal contraband when it is located inside a commercial workplace setting.
(e) Possessed, because she engaged in an incriminating dialogue with a co-worker regarding the exact location and contents of the illicit materials.

**Answer:** (b)

**Explanation:** Constructive possession requires proof that the defendant both knew of the contraband's presence and had the power and intent to exercise dominion and control over it. Laura's demand that Kevin remove the bag shows she had no intent to control it, and her lack of the combination shows a lack of power. Option (a) fails because awareness of contraband in a shared space is insufficient without dominion and control. Option (c) fails because failure to report does not equate to exercising control. Option (d) fails because constructive possession applies perfectly well in commercial settings if the elements are met. Option (e) fails because while her statement proves awareness, it directly negates intent to control, rendering the statement insufficient to establish possession.

**Tags:** chapters: [15], topics: [constructive possession, awareness vs dominion], difficulty: medium, cognitive: application

**Grounding:** Chapter 15 (State of Louisiana v. Gerald Manchip White)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that actual knowledge combined with the contraband being in a shared employee space (over which she has some level of workplace access) establishes constructive possession. In some jurisdictions, proximity and knowledge in a jointly accessible area might allow an inference of control. Therefore, option (a) correctly identifies her knowledge and the shared nature of the room as establishing the necessary elements of constructive possession.
(b) Argument-for: Constructive possession requires not just knowledge, but the power and intent to exercise dominion and control over the contraband. The facts state Laura explicitly demanded Kevin remove the bag, which directly negates any intent to control the cocaine. Because she overtly rejected the contraband and lacked the ability to access it (locked bag), she did not have constructive possession, making this the correct application of the rule.
(c) Argument-for: A student might argue that under the doctrine of omission or accomplice liability, failing to report known felonies or contraband in one's own domain can constitute legal adoption of the crime. Since she knew of the massive quantity of cocaine in her workplace and did nothing to alert authorities, her silence operated as tacit consent and an implicit adoption of Kevin's possession, establishing her own constructive possession.
(d) Argument-for: A student could argue that constructive possession requires a level of exclusive or residential control (like a home or personal vehicle) that a low-level civilian employee simply does not possess over a commercial workplace breakroom. Because the breakroom is a commercial space controlled by the employer, an ordinary employee as a matter of law cannot exercise the requisite dominion and control to constructively possess items left there by others.
(e) Argument-for: A student could argue that an incriminating dialogue regarding the exact location and contents of the illicit materials shows more than mere presence; it shows active engagement and intimate knowledge of the contraband operation. By discussing the illicit materials in detail, Laura demonstrated the kind of insider knowledge that courts often use to infer an intent and ability to exercise dominion and control over the drugs.

Head-to-head: Option (b) is the clear winner because it correctly applies the rule for constructive possession—requiring intent to exercise dominion and control—which Laura explicitly negated by demanding the bag's removal. Options (c) and (d) contain explicitly false legal claims: (c) invents an "implicit adoption" doctrine for failing to report, and (d) invents a categorical exception for "commercial workplace settings." However, options (a) and (e) simply present true facts (actual knowledge, shared breakroom, incriminating dialogue) and conclude they equal possession. They rely on implicit omissions of the dominion/control element rather than asserting an explicit, falsifiable legal claim locked by an absolute word.

Falsifiable claim per distractor:
- (a): "Possessed, because she had actual knowledge..." — wrong because knowledge and proximity do not equal dominion and control, but relies on an implicit omission rather than an explicit false claim.
- (c): "legally constituted an implicit adoption" — wrong because there is no legal doctrine where failure to report contraband constitutes an implicit adoption of possession.
- (d): "cannot constructively possess illegal contraband when it is located inside a commercial workplace setting" — wrong because constructive possession absolutely can apply in commercial settings.
- (e): "Possessed, because she engaged in an incriminating dialogue" — wrong because dialogue alone doesn't prove control, but like (a), relies on an implicit omission rather than an absolute, locked falsifiable claim.

Recommended fix: Add absolute words to (a) and (e) to lock their falsifiable claims. For (a), edit to: "Possessed, solely because she had actual knowledge..." For (e), edit to: "Possessed, because engaging in an incriminating dialogue automatically establishes constructive possession."
-->
