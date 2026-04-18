# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q13.** Regarding the baggies of fentanyl found on the passenger seat, which of the following is the strongest argument that Leo is NOT guilty of constructive possession?

(a) Constructive possession requires the defendant to be the legal owner of the contraband, and Dom was the true owner of the backpack.
(b) The baggies were inside Dom's ripped backpack, proving that Leo lacked the physical strength to access them during the high-speed chase.
(c) Constructive possession requires that the contraband be entirely hidden from plain view, which was not the case here.
(d) Leo lacked the requisite awareness of the drugs' presence and character, as they were suddenly tossed into the car by Dom moments before the chase. <!-- correct -->
(e) Constructive possession is inapplicable to vehicles because multiple occupants inherently possess joint control over the entire cabin space.

**Answer:** (d)

**Explanation:** Constructive possession requires that the defendant have both the power and the intention to exercise control over the contraband, which entails awareness of its presence and character. Mere proximity to the drugs is insufficient. Because Dom tossed the backpack into the car during a panicked retreat and the drugs only spilled out subsequently (or during the crash), Leo's claim that he had no idea the drugs were there directly attacks the "awareness" element required for constructive possession. (a) is wrong because possession relies on control, not legal ownership. (b) is wrong because the physical strength to reach the baggies is irrelevant if he lacked intent or awareness; furthermore, they were on the passenger seat. (c) is wrong because contraband in plain view actually *strengthens* the state's argument for awareness, rather than being a barrier to constructive possession. (e) is wrong because constructive possession is routinely applied in vehicle cases; joint control is permissible if awareness and intent are proven.

**Tags:** chapters: [15], topics: [constructive-possession, awareness, control], difficulty: easy, cognitive: application

**Grounding:** Chapter 15: cp-awareness-control

<!-- argument-pass: SHOULD FIX
(a) Argument-for: To be guilty of constructive possession, a defendant must have the right and power to control the item. A student might argue that this right to control is legally synonymous with ownership, as only the true owner has the ultimate authority to dictate the disposition of the property. Therefore, because Dom owned the backpack, Leo could not legally exercise control over it.
(b) Argument-for: Constructive possession requires the present ability and power to exercise dominion over the contraband. A student could argue that if Leo was driving in a high-speed chase, his physical inability to reach into a ripped backpack on the passenger seat means he lacked the requisite immediate power to control the baggies. Thus, this physical barrier to access effectively negates the "power" element.
(c) Argument-for: The doctrine of constructive possession was developed to handle situations where a defendant secretes contraband in places they control rather than holding it on their person. A student might assert that if the drugs are in plain view, the analysis must shift to actual possession, making constructive possession doctrinally inapplicable to visible items.
(d) Argument-for: Constructive possession mandates that the defendant have both the power and intent to exercise control over the illicit item. Intent inherently necessitates knowledge; one cannot intend to control something they do not know exists. Since Dom tossed the baggies into the car just before the chase, Leo's lack of awareness regarding their presence directly negates the mens rea required.
(e) Argument-for: Vehicles present unique spatial dynamics where multiple individuals share very close quarters. A student could contend that because occupants inherently share joint control over the entire cabin, the legal fiction of constructive possession is too broad and thus categorically inapplicable to automobiles, requiring instead proof of actual possession.

Head-to-head: Option (d) correctly applies the core elements of constructive possession by focusing on Leo's lack of awareness, which destroys the necessary intent to exercise control. Option (a) incorrectly equates the power to control with legal ownership, a fundamentally flawed premise. Option (c) introduces a fabricated legal rule that constructive possession only applies to hidden items, when in fact plain view strengthens the case for awareness. Option (e) invents a categorical rule excluding vehicles from constructive possession, which contradicts a vast body of established case law. Option (b) relies on an absurd factual conclusion and lacks an explicitly locked false legal claim, asserting instead that physical strength to access during a chase is the determining factor.

Falsifiable claim per distractor:
- (a): "Constructive possession requires the defendant to be the legal owner of the contraband" — wrong because possession targets the power and intent to control, regardless of legal title.
- (b): "proving that Leo lacked the physical strength to access them" — wrong factually and conceptually, but fails the strict distractor test because it is a factual conclusion rather than an explicit, categorically locked false legal claim.
- (c): "Constructive possession requires that the contraband be entirely hidden from plain view" — wrong because contraband in plain view can absolutely be constructively possessed.
- (e): "Constructive possession is inapplicable to vehicles" — wrong because constructive possession is routinely applied to vehicle occupants.

Recommended fix: Update (b) to include a locked false legal claim. Change (b) to: "Constructive possession categorically requires the defendant to have immediate, unhindered physical access to the contraband, which Leo lacked while driving during the chase."
-->

## Issue 3 — argpass-opus

**Q13.** Regarding the baggies of fentanyl found on the passenger seat, which of the following is the strongest argument that Leo is NOT guilty of constructive possession?

(a) Constructive possession requires the defendant to be the legal owner of the contraband, and Dom was the true owner of the backpack.
(b) The baggies were inside Dom's ripped backpack, proving that Leo lacked the physical strength to access them during the high-speed chase.
(c) Constructive possession requires that the contraband be entirely hidden from plain view, which was not the case here.
(d) Leo lacked the requisite awareness of the drugs' presence and character, as they were suddenly tossed into the car by Dom moments before the chase. <!-- correct -->
(e) Constructive possession is inapplicable to vehicles because multiple occupants inherently possess joint control over the entire cabin space.

**Answer:** (d)

**Explanation:** Constructive possession requires that the defendant have both the power and the intention to exercise control over the contraband, which entails awareness of its presence and character. Mere proximity to the drugs is insufficient. Because Dom tossed the backpack into the car during a panicked retreat and the drugs only spilled out subsequently (or during the crash), Leo's claim that he had no idea the drugs were there directly attacks the "awareness" element required for constructive possession. (a) is wrong because possession relies on control, not legal ownership. (b) is wrong because the physical strength to reach the baggies is irrelevant if he lacked intent or awareness; furthermore, they were on the passenger seat. (c) is wrong because contraband in plain view actually *strengthens* the state's argument for awareness, rather than being a barrier to constructive possession. (e) is wrong because constructive possession is routinely applied in vehicle cases; joint control is permissible if awareness and intent are proven.

**Tags:** chapters: [15], topics: [constructive-possession, awareness, control], difficulty: easy, cognitive: application

**Grounding:** Chapter 15: cp-awareness-control

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that dominion and control over an item is most clearly established by property rights. Since Dom was the true owner of the backpack, Dom retained exclusive legal rights to the items within it. Therefore, under strict property principles, Leo could not legally possess the items, preventing the state from proving that Leo had the rightful authority to exercise control. Thus, lack of legal ownership automatically defeats constructive possession.
(b) Argument-for: Constructive possession requires the present physical ability to exercise control over the item. During a high-speed chase, a driver must use both hands and full physical capacity to operate the vehicle, making it physically impossible to reach into a ripped backpack on the passenger seat. Because Leo lacked the physical strength and mobility to access the drugs while driving evasively, one could argue he lacked the requisite physical power to control them.
(c) Argument-for: Constructive possession is traditionally used when contraband is not found on the defendant's person but is hidden in an area they control. If an item is in plain view, actual possession might be the proper framework, not constructive possession. Therefore, a student might argue that the constructive possession doctrine is exclusively reserved for hidden items where control must be inferred from the surroundings.
(d) Argument-for: Constructive possession requires both the power and intent to exercise dominion and control over the contraband. Intent necessarily requires awareness of the presence and illegal character of the substance. If Dom suddenly tossed the baggies into the car moments before the chase, Leo had no time to perceive or understand what they were. Without this requisite awareness, Leo could not form the intent to control the drugs.
(e) Argument-for: A student could argue that vehicle cabins present a unique legal environment where proximity alone cannot establish dominion and control due to the confined space. Because multiple occupants share joint control over the entire cabin, attributing possession of loose items to the driver requires additional connecting evidence. Therefore, one could argue that the standard doctrine of constructive possession is categorically inapplicable to vehicles.

Head-to-head: Option (d) correctly identifies the core elements of constructive possession—power and intent to control—and accurately applies the fact that Leo lacked awareness, thus negating intent. Options (a), (c), and (e) rely on explicitly false legal rules ("requires the defendant to be the legal owner", "requires that the contraband be entirely hidden", "inapplicable to vehicles"). Option (b) makes a convoluted factual argument about "physical strength" which doesn't correctly align with the legal standard of power to control. Because (b) relies on an absurd factual inference rather than an explicitly false legal claim, it technically fails the strictures of the close-call standard.

Falsifiable claim per distractor:
- (a): "Constructive possession requires the defendant to be the legal owner" — wrong because constructive possession relies on control and intent, not legal ownership or property rights.
- (b): "proving that Leo lacked the physical strength to access them" — wrong because it is a factual absurdity rather than a falsifiable legal rule; physical strength is not a distinct legal element of control.
- (c): "requires that the contraband be entirely hidden from plain view" — wrong because contraband in plain view often strengthens the inference of awareness and control.
- (e): "Constructive possession is inapplicable to vehicles" — wrong because constructive possession is routinely and categorically applied in vehicle cases involving multiple occupants.

Recommended fix: Edit (b) to include an explicitly false legal claim locked with absolute words. For example: "(b) Constructive possession categorically requires proof that the defendant possessed the physical strength to destroy the contraband, which Leo lacked during the high-speed chase."
-->
