# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Under the *Lauria* standard for accomplice liability, does Frankie possess the requisite mens rea regarding the planned hijacking?

(a) Yes, because any vendor who sells a product with knowledge of its intended illicit use is strictly liable as an accomplice.
(b) Yes, because by charging triple the usual rental rate, Frankie derived a specialized financial stake in the venture that allows an inference of purpose. <!-- correct -->
(c) No, because his statement "I don't care what you do" proves he was legally indifferent and lacked a shared purpose with the crew.
(d) No, because renting a vehicle is an ordinary commercial transaction that cannot form the basis of accomplice liability.
(e) No, because he did not personally participate in or plan the substantive acts of the hijacking itself.

**Answer:** (b)

**Explanation:** Under *People v. Lauria*, mere knowledge of a purchaser's criminal intent is generally insufficient to establish the "purpose" required for accomplice liability. However, purpose can be inferred if the provider has a special stake in the venture, such as by charging an inflated price for the goods or services. By charging triple the usual rate because the car was for a hijacking, Frankie demonstrated the required purpose. (a) is wrong because *Lauria* explicitly rejects the rule that knowledge alone establishes purpose for ordinary vendors. (c) is wrong because despite his words, his action of charging a massive premium provides the necessary inference of purpose. (d) is wrong because providing ordinary goods can create liability if the *Lauria* exceptions (inflated price, volume, high-severity crime) apply. (e) is wrong because accomplice liability criminalizes aiding and abetting; personal participation in the primary actus reus is not required.

**Tags:** chapters: [18], topics: [accomplice-liability, lauria, mens-rea], difficulty: medium, cognitive: application

**Grounding:** Chapter 18: lauria-knowledge-vs-purpose and lauria-three-inferences

<!-- audit: MUST FIX
Check 1: pass (the application of Lauria's inflated-price inference to find purpose is correct doctrine)
Check 2: pass (assuming facts were present, the distractors are reasonably designed)
Check 3: pass 
Check 4: MUST FIX. The question stem is completely missing a fact pattern. It asks about "Frankie" and a "planned hijacking" but provides zero facts about the scenario. Students are forced to reverse-engineer the operative facts (renting a vehicle, charging triple, saying "I don't care") entirely from the answer options and explanation.
Check 5: pass
Check 6: pass
Check 7: MUST FIX. Coverage mismatch. The question's tags and grounding attribute `lauria-knowledge-vs-purpose` and `lauria-three-inferences` to Chapter 18 (Accomplice Liability), but the meta-map explicitly locates these tags strictly under Chapter 19 (Conspiracy). Applying a Chapter 19 specific-case doctrine to a Chapter 18 framework violates the map boundaries.
Recommended fix: 1) Add the missing fact pattern to the stem (e.g., "Frankie knows a crew is planning a hijacking and rents them a van. He says 'I don't care what you do,' but charges them triple his normal rate."). 2) Reframe the question and explanation around Conspiracy rather than Accomplice Liability to align with the meta-map, and update the tags/grounding to Chapter 19.
-->

## Issue 2 — argpass-opus

**Q7.** Under the *Lauria* standard for accomplice liability, does Frankie possess the requisite mens rea regarding the planned hijacking?

(a) Yes, because any vendor who sells a product with knowledge of its intended illicit use is strictly liable as an accomplice.
(b) Yes, because by charging triple the usual rental rate, Frankie derived a specialized financial stake in the venture that allows an inference of purpose. <!-- correct -->
(c) No, because his statement "I don't care what you do" proves he was legally indifferent and lacked a shared purpose with the crew.
(d) No, because renting a vehicle is an ordinary commercial transaction that cannot form the basis of accomplice liability.
(e) No, because he did not personally participate in or plan the substantive acts of the hijacking itself.

**Answer:** (b)

**Explanation:** Under *People v. Lauria*, mere knowledge of a purchaser's criminal intent is generally insufficient to establish the "purpose" required for accomplice liability. However, purpose can be inferred if the provider has a special stake in the venture, such as by charging an inflated price for the goods or services. By charging triple the usual rate because the car was for a hijacking, Frankie demonstrated the required purpose. (a) is wrong because *Lauria* explicitly rejects the rule that knowledge alone establishes purpose for ordinary vendors. (c) is wrong because despite his words, his action of charging a massive premium provides the necessary inference of purpose. (d) is wrong because providing ordinary goods can create liability if the *Lauria* exceptions (inflated price, volume, high-severity crime) apply. (e) is wrong because accomplice liability criminalizes aiding and abetting; personal participation in the primary actus reus is not required.

**Tags:** chapters: [18], topics: [accomplice-liability, lauria, mens-rea], difficulty: medium, cognitive: application

**Grounding:** Chapter 18: lauria-knowledge-vs-purpose and lauria-three-inferences

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under a broad view of accomplice liability, facilitating a crime with knowledge of its illicit purpose provides necessary material support. A student might argue that since Frankie knew of the hijacking, his provision of the vehicle makes him strictly liable as an accomplice, reasoning that knowledge of a severe crime automatically satisfies the mens rea. Therefore, his awareness alone is enough to trigger liability regardless of his financial stake.
(b) Argument-for: *People v. Lauria* establishes that a vendor's knowledge of illicit use can translate into the requisite "purpose" if the vendor acquires a special stake in the venture. By explicitly charging triple the usual rental rate because the vehicle was to be used in a hijacking, Frankie derived a specialized financial stake. This financial premium allows a clear, objective legal inference of purpose that satisfies the mens rea requirement for accomplice liability.
(c) Argument-for: Accomplice liability requires the defendant to actively share the criminal intent of the principal. A student could argue that Frankie's explicit statement, "I don't care what you do," serves as direct evidence that negates any shared purpose with the hijackers. They might contend that this express disavowal definitively proves legal indifference, overriding any circumstantial inferences drawn from the rental rate.
(d) Argument-for: *Lauria* protects vendors engaging in everyday commerce from being held liable as accomplices merely because they know a buyer's illicit intent. A student could argue that renting a vehicle is an inherently lawful, routine service available to the general public. Thus, it falls safely within the bounds of ordinary commercial transactions that categorically cannot form the basis of accomplice liability.
(e) Argument-for: Accomplice liability typically requires an act of assistance or encouragement coupled with the intent to facilitate the specific crime. A student might argue that because Frankie did not personally participate in or help plan the substantive acts of the hijacking, his involvement is merely peripheral. Therefore, without direct participation or planning, his connection to the actus reus is too remote to satisfy the requirements for accomplice liability.

Head-to-head: Option (b) is the clear, correct application of *Lauria*'s "special stake" exception. Option (a) uses absolute language ("any vendor", "strictly liable") to make a blatantly false legal claim. Option (d) also uses absolute language ("cannot form the basis") to falsely claim ordinary commercial transactions are universally exempt from liability. Options (c) and (e), however, rely on implicit legal premises without absolute locking words. Option (c) claims the statement "proves" indifference, and option (e) asserts "No, because he did not personally participate," which structurally implies participation is an absolute legal requirement, but fails to lock this claim with rigid terminology as required by the close-call standard. Additionally, the question stem is entirely missing the fact pattern, forcing the student to reverse-engineer the facts from the options.

Falsifiable claim per distractor:
- (a): "any vendor... is strictly liable" — wrong because *Lauria* explicitly holds that mere knowledge of a purchaser's criminal intent is generally insufficient to establish purpose for vendors.
- (c): "proves he was legally indifferent" — wrong because a self-serving verbal statement does not conclusively prove legal indifference when objective actions (price gouging) establish a special stake under *Lauria*.
- (d): "cannot form the basis of accomplice liability" — wrong because *Lauria* provides specific exceptions (such as an inflated rate) where ordinary commercial transactions absolutely can form the basis of liability.
- (e): "because he did not personally participate" — wrong because accomplice liability inherently criminalizes aiding and abetting from the periphery; personal participation in the substantive act is categorically not required.

Recommended fix: Insert the missing fact pattern into the question stem. To harden the distractors to the close-call standard, add absolute locking words to (c) and (e). Change (c) to "...categorically proves he was legally indifferent..." and change (e) to "No, because accomplice liability legally requires personal participation in or planning of the substantive acts."
-->
