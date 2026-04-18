# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q9.** Investigators charge Avon with possession of the drug sales ledger and the restricted warehouse keys found in the locked box in his office. Does Avon have constructive possession of these items?

(a) No, because Marlowe had actual physical possession of the illicit warehouse itself, which legally precludes Avon from constructively possessing the keys to that same building.
(b) Yes, because the specific items were kept in a locked box in his personal office, establishing his awareness and his power to exercise dominion and control. <!-- correct -->
(c) No, because the metal keys and written ledger technically belonged to the corporate entity, Barksdale Logistics Corp., rather than to Avon as a private individual.
(d) Yes, because as the chief executive officer, Avon is legally presumed to possess every physical item located anywhere within the corporation's geographically dispersed facilities.
(e) No, because Avon was not physically holding the locked box or the items inside when the government investigators executed the search warrant at corporate headquarters.

**Answer:** (b)

**Explanation:** (b) is correct because constructive possession requires proof that the defendant had knowledge of the item and the power and intent to exercise dominion and control over it. Storing items in a locked box inside one's own private office satisfies these elements. (a) is wrong because multiple people can have joint or constructive possession of an area or items; Marlowe's control of the warehouse does not negate Avon's control of the keys. (c) is wrong because possession relies on dominion and control, not formal legal ownership of the items. (d) is wrong because corporate officers do not automatically possess all corporate property; constructive possession requires specific awareness and control. (e) is wrong because constructive possession was designed precisely to cover situations where the defendant is not in actual physical possession.

**Tags:** chapters: [15], topics: [constructive possession, dominion and control], difficulty: easy, cognitive: application

**Grounding:** cp-awareness-control / cp-exclusive-control

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Being "charged" with possession of a ledger and keys is factually weird, as possession is generally a standalone offense for contraband (like drugs or illegal weapons), not mere evidence or instruments like keys/ledgers. This might momentarily confuse students looking for an actus reus/legality issue.
3. Cross-Question Spoilers: pass
Recommended fix: Change "Investigators charge Avon with possession of the drug sales ledger..." to "Prosecutors seek to establish that Avon possessed the drug sales ledger..."
-->

## Issue 3 — argpass-opus

**Q9.** Investigators charge Avon with possession of the drug sales ledger and the restricted warehouse keys found in the locked box in his office. Does Avon have constructive possession of these items?

(a) No, because Marlowe had actual physical possession of the illicit warehouse itself, which legally precludes Avon from constructively possessing the keys to that same building.
(b) Yes, because the specific items were kept in a locked box in his personal office, establishing his awareness and his power to exercise dominion and control. <!-- correct -->
(c) No, because the metal keys and written ledger technically belonged to the corporate entity, Barksdale Logistics Corp., rather than to Avon as a private individual.
(d) Yes, because as the chief executive officer, Avon is legally presumed to possess every physical item located anywhere within the corporation's geographically dispersed facilities.
(e) No, because Avon was not physically holding the locked box or the items inside when the government investigators executed the search warrant at corporate headquarters.

**Answer:** (b)

**Explanation:** (b) is correct because constructive possession requires proof that the defendant had knowledge of the item and the power and intent to exercise dominion and control over it. Storing items in a locked box inside one's own private office satisfies these elements. (a) is wrong because multiple people can have joint or constructive possession of an area or items; Marlowe's control of the warehouse does not negate Avon's control of the keys. (c) is wrong because possession relies on dominion and control, not formal legal ownership of the items. (d) is wrong because corporate officers do not automatically possess all corporate property; constructive possession requires specific awareness and control. (e) is wrong because constructive possession was designed precisely to cover situations where the defendant is not in actual physical possession.

**Tags:** chapters: [15], topics: [constructive possession, dominion and control], difficulty: easy, cognitive: application

**Grounding:** cp-awareness-control / cp-exclusive-control

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could defend this option by relying on principles of exclusive possession. They might argue that actual physical possession of a warehouse by one individual (Marlowe) definitively overrides or nullifies any claim that someone else constructively possesses the keys. The argument would assert that constructive possession is a fallback doctrine that cannot apply when another party already exercises actual physical dominion over the underlying property. Thus, Marlowe's possession legally precludes Avon's.
(b) Argument-for: A student could defend this option by pointing directly to the standard legal definition of constructive possession. The locked box in a personal office proves Avon had exclusive access, which establishes his power to exercise dominion and control over the contents. Storing specific items there also demonstrates his awareness of their presence, satisfying both the mental and physical elements of the doctrine. This makes it the strongest legal conclusion based on the facts.
(c) Argument-for: A student could argue this based on formal property and corporate law distinctions. The reasoning would be that corporate assets are legally possessed by the corporate entity itself, not by its agents in their individual capacities. Because Avon lacks private legal title to the ledger and keys, he cannot be charged as a private individual possessor. This relies on a strict but flawed belief that ownership dictates criminal possession.
(d) Argument-for: A student could defend this by incorrectly extending the responsible corporate officer doctrine. They might argue that a CEO, by virtue of their supreme executive authority, is legally presumed to have absolute control—and thus constructive possession—over every item within the corporation's facilities. The reasoning assumes that geographic dispersion does not sever the automatic legal presumption of control tied to the CEO title.
(e) Argument-for: A student could defend this by arguing that criminal possession charges require immediate physical nexus when a warrant is executed. They might mistakenly believe that constructive possession is entirely negated if the defendant is present but not physically holding the contraband. Under this logic, being in the room without holding the locked box physically shields the defendant from possession liability.

Head-to-head: 
Option (b) stands out as clearly correct by accurately applying the legal standard for constructive possession: the awareness and power to exercise dominion and control. Option (a) fails because actual possession of a building does not legally preclude someone else from possessing the keys. Option (c) wrongly substitutes formal corporate ownership for the required dominion and control. Option (d) invents a false absolute presumption that CEOs constructively possess all corporate property. Option (e) falsely implies that a lack of physical holding defeats a constructive possession charge, contradicting the core purpose of the doctrine. While the distractors all contain false legal logic, options (c) and (e) lack the absolute wording recommended by the close-call standard to firmly lock their falsifiable claims against student appeals.

Falsifiable claim per distractor:
- (a): "legally precludes Avon from constructively possessing" — wrong because actual possession of a premises by one person does not legally preclude another from constructively possessing the keys.
- (c): "No, because the metal keys... technically belonged to the corporate entity" — wrong because constructive possession depends on actual dominion and control, not formal corporate ownership or legal title.
- (d): "legally presumed to possess every physical item located anywhere" — wrong because there is no blanket legal presumption that a CEO constructively possesses all physical items within corporate facilities.
- (e): "No, because Avon was not physically holding the locked box" — wrong because the lack of physical holding is exactly what the doctrine of constructive possession is designed to address, meaning it cannot legally defeat the charge.

Recommended fix: Change "No, because" to "No, solely because" in options (c) and (e) to lock their falsifiable legal claims absolutely (e.g., "(c) No, solely because the metal keys...").
-->
