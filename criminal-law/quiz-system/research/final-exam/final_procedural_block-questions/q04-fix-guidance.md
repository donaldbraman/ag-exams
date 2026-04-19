# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Evaluating the five kilograms of cocaine found inside the locked filing cabinet, which of the following best describes Kevin and Steve's liability under the doctrine of constructive possession?

(a) Both Kevin and Steve constructively possessed the cocaine because they each held a key to the cabinet, demonstrating the shared power and intent to exercise control over it. <!-- correct -->
(b) Only Steve constructively possessed the cocaine because the locked filing cabinet was physically located within the exclusive confines of his private, designated corporate legal office space.
(c) Only Kevin constructively possessed the cocaine because he was the undisputed leader of the criminal enterprise and the ultimate financial owner of the illicit commercial narcotics inventory.
(d) Neither man constructively possessed the cocaine because law enforcement executed the decisive headquarters raid when both specific individuals were completely physically absent from the private office room.
(e) Neither man constructively possessed the cocaine because the doctrine strictly requires exclusive physical access, which is legally defeated whenever two or more individuals hold matching cabinet keys.

**Answer:** (a)

**Explanation:** Constructive possession is established when an individual has both the power and intention to exercise control over an item, which can be held jointly. Both Kevin and Steve holding keys to the cabinet demonstrates this shared power and control, making (a) correct. (b) is incorrect because Steve's office location does not negate Kevin's joint constructive possession via his own key. (c) is incorrect because Kevin's leadership does not negate Steve's joint possession over a cabinet in his own office. (d) is incorrect because constructive possession explicitly accounts for situations where defendants are not physically present. (e) is incorrect because the doctrine fully recognizes joint constructive possession among multiple individuals.

**Tags:** chapters: [2, 10], topics: [actus reus, constructive possession, joint possession], difficulty: medium, cognitive: application

**Grounding:** Constructive possession requires the power and intent to exercise control over an object; it can be established through keys to a locked container and may be held jointly by multiple parties.

<!-- audit: MUST FIX
Check 1: Correct-answer accuracy fails. Option (a) incorrectly claims that holding a key demonstrates both power *and* intent to exercise control over the cocaine. A key establishes the *power* (access) to control the cabinet, but *intent* to control the contraband requires knowledge of its presence inside, which holding a key alone does not doctrinally establish. 
Check 2: pass
Check 3: pass
Check 4: Fails. The stem/fact pattern is completely missing from the prompt. Without a fact pattern establishing that Kevin and Steve knew the cocaine was in the cabinet, there are insufficient facts to conclude they had the requisite intent for constructive possession.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Provide the missing fact pattern. Revise option (a) to read: "...because they each held a key to the cabinet and knew of its contents, demonstrating the shared power and intent to exercise control over it."
-->

## Issue 2 — argpass-opus

**Q4.** Evaluating the five kilograms of cocaine found inside the locked filing cabinet, which of the following best describes Kevin and Steve's liability under the doctrine of constructive possession?

(a) Both Kevin and Steve constructively possessed the cocaine because they each held a key to the cabinet, demonstrating the shared power and intent to exercise control over it. <!-- correct -->
(b) Only Steve constructively possessed the cocaine because the locked filing cabinet was physically located within the exclusive confines of his private, designated corporate legal office space.
(c) Only Kevin constructively possessed the cocaine because he was the undisputed leader of the criminal enterprise and the ultimate financial owner of the illicit commercial narcotics inventory.
(d) Neither man constructively possessed the cocaine because law enforcement executed the decisive headquarters raid when both specific individuals were completely physically absent from the private office room.
(e) Neither man constructively possessed the cocaine because the doctrine strictly requires exclusive physical access, which is legally defeated whenever two or more individuals hold matching cabinet keys.

**Answer:** (a)

**Explanation:** Constructive possession is established when an individual has both the power and intention to exercise control over an item, which can be held jointly. Both Kevin and Steve holding keys to the cabinet demonstrates this shared power and control, making (a) correct. (b) is incorrect because Steve's office location does not negate Kevin's joint constructive possession via his own key. (c) is incorrect because Kevin's leadership does not negate Steve's joint possession over a cabinet in his own office. (d) is incorrect because constructive possession explicitly accounts for situations where defendants are not physically present. (e) is incorrect because the doctrine fully recognizes joint constructive possession among multiple individuals.

**Tags:** chapters: [2, 10], topics: [actus reus, constructive possession, joint possession], difficulty: medium, cognitive: application

**Grounding:** Constructive possession requires the power and intent to exercise control over an object; it can be established through keys to a locked container and may be held jointly by multiple parties.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the doctrine of constructive possession, an individual need not have actual physical custody of an object to possess it; instead, they must have the power and intent to exercise dominion and control. Joint constructive possession allows multiple individuals to possess the same item simultaneously. Because both Kevin and Steve held keys to the filing cabinet, they both had the requisite power to access and control the cocaine. As the option stipulates their shared power and intent, this perfectly satisfies the elements of joint constructive possession, making them both liable.
(b) Argument-for: Constructive possession is often tied to dominion and control over the premises where contraband is found. Because the filing cabinet was located strictly within Steve’s private, designated corporate legal office space, a student could argue that Steve alone had the ultimate authority over that space. If Kevin merely held a key but lacked dominion over the office itself, his power to control the cabinet might be viewed as legally subordinate to Steve's exclusive territorial control, rendering Steve the sole possessor.
(c) Argument-for: Constructive possession inherently relies on the intent to exercise control, which is often dictated by ownership and hierarchical authority. A student could argue that as the undisputed leader of the criminal enterprise and ultimate financial owner of the cocaine, Kevin retained the exclusive ultimate authority to direct its disposition. In this view, Steve is merely a custodian or subordinate whose possession of a key does not equate to independent legal dominion and control, leaving Kevin as the sole constructive possessor.
(d) Argument-for: Constructive possession requires a present nexus between the defendant and the contraband. A student might argue that because both men were physically absent from the private office during the raid, their ability to immediately exercise control was severed. Under a highly restrictive view of the actus reus of possession, the lack of proximity at the precise moment of police seizure could be interpreted as defeating their immediate power to control the narcotics, meaning neither possessed it.
(e) Argument-for: A strict, traditional interpretation of possession focuses on exclusive physical control over an item. A student might argue that the very nature of multiple people holding matching keys destroys the concept of "exclusive" access. Under this logic, because the doctrine allegedly requires exclusive physical access to establish dominion, the existence of duplicate keys legally defeats the possession claim for any single individual, absolving both Kevin and Steve.

Head-to-head: Option (a) correctly applies the settled legal rule that constructive possession can be held jointly and is established by the power (keys) and intent to exercise control. Option (e) is easily eliminated because it explicitly relies on a blatantly false legal premise ("strictly requires exclusive physical access"), which contradicts the core doctrine of joint possession. Options (b), (c), and (d) offer plausible factual reasons why only one or neither man might possess the drugs, but they fail to state explicitly false *legal* propositions locked with absolute terms; they rely on the word "because" to imply a false rule of exclusivity based on office location, ownership, or physical absence. To cleanly pass the close-call standard, (b), (c), and (d) should explicitly assert that these factors categorically or automatically defeat constructive possession as a matter of law.

Falsifiable claim per distractor:
- (b): "Only Steve constructively possessed the cocaine because the locked filing cabinet was physically located within the exclusive confines of his private... office space" — wrong because joint possession is not legally defeated by the container residing in one party's exclusive office, but the distractor lacks an absolute legal word to lock the false rule.
- (c): "Only Kevin constructively possessed the cocaine because he was the undisputed leader..." — wrong because an underling with a key also has constructive possession, but it implies rather than explicitly states the false rule that only a financial owner can possess.
- (d): "Neither man constructively possessed the cocaine because law enforcement executed the decisive headquarters raid when both... were completely physically absent" — wrong because constructive possession specifically applies when defendants are physically absent, though it lacks an absolute word asserting this as a strict legal requirement.
- (e): "the doctrine strictly requires exclusive physical access, which is legally defeated whenever two or more individuals hold matching cabinet keys" — wrong because joint constructive possession is universally recognized; this option successfully locks a false legal claim with "strictly requires."

Recommended fix: SHOULD FIX. Edit (b), (c), and (d) to explicitly state their false legal rules using absolute words. For example, edit (b) to: "Only Steve... because constructive possession categorically vests solely in the occupant of the premises"; edit (c) to: "Only Kevin... because constructive possession legally requires ultimate financial ownership"; and edit (d) to: "Neither man... because the doctrine automatically fails if the defendants are completely physically absent from the premises."
-->
