# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q11.** Marcus is charged with possession of the 500 grams of cocaine found in the basement safe. Under the doctrine of constructive possession, is the evidence sufficient to convict him?

(a) No, because the safe was located in a communal, unlocked basement, meaning he lacked exclusive spatial control over the area.
(b) Yes, because the key on his nightstand establishes his awareness of the drugs and his power and intent to exercise control over them. <!-- correct -->
(c) No, because he was not physically holding the drugs at the time of his arrest, and constructive possession requires immediate proximity.
(d) Yes, because as the leader of the organization, he is strictly liable for any narcotics found within his apartment building.
(e) No, because the safe was unmarked, preventing the prosecution from proving beyond a reasonable doubt that he knew what was inside it.

**Answer:** (b)

**Explanation:** (b) is correct. Constructive possession requires proof that the defendant had awareness of the contraband and the power and intent to exercise dominion and control over it. Holding the sole key to a locked safe, combined with his leadership of the drug ring and the ledger, firmly establishes this control. (a) is incorrect because control over the container (via the key) establishes constructive possession even if the container is located in a communal area. (c) is incorrect because constructive possession was designed precisely to reach defendants who are not physically holding the contraband. (d) is incorrect because constructive possession requires proven awareness and control, not strict liability based on status. (e) is incorrect because circumstantial evidence (the ledger, his role) sufficiently proves his knowledge of the safe's contents.

**Tags:** chapters: [15], topics: [constructive-possession, awareness, control], difficulty: easy, cognitive: application

**Grounding:** Chapter 15: Drugs and Guns > Refinements > Constructive Possession

<!-- audit: MUST FIX
check 1: fail (the correct answer cannot be deduced because the facts are missing from the stem)
check 2: pass (N/A due to missing facts)
check 3: pass (the explanation accurately recites the constructive possession standard of awareness plus power/intent to control)
check 4: fail (The stem is missing the entire fact pattern. It omits the key on the nightstand, the ledger, Marcus's role as a leader of the organization, and the details about the safe being locked or unmarked, which are all relied upon by the options and explanation.)
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Insert the missing facts into the stem before the question (e.g., "Police raid an apartment building where Marcus leads a drug organization. In Marcus's bedroom, they find a drug ledger and a single key on his nightstand. The key unlocks an unmarked safe located in the building's communal basement, which contains 500 grams of cocaine.").
-->

## Issue 2 — argpass-sonnet

**Q11.** Marcus is charged with possession of the 500 grams of cocaine found in the basement safe. Under the doctrine of constructive possession, is the evidence sufficient to convict him?

(a) No, because the safe was located in a communal, unlocked basement, meaning he lacked exclusive spatial control over the area.
(b) Yes, because the key on his nightstand establishes his awareness of the drugs and his power and intent to exercise control over them. <!-- correct -->
(c) No, because he was not physically holding the drugs at the time of his arrest, and constructive possession requires immediate proximity.
(d) Yes, because as the leader of the organization, he is strictly liable for any narcotics found within his apartment building.
(e) No, because the safe was unmarked, preventing the prosecution from proving beyond a reasonable doubt that he knew what was inside it.

**Answer:** (b)

**Explanation:** (b) is correct. Constructive possession requires proof that the defendant had awareness of the contraband and the power and intent to exercise dominion and control over it. Holding the sole key to a locked safe, combined with his leadership of the drug ring and the ledger, firmly establishes this control. (a) is incorrect because control over the container (via the key) establishes constructive possession even if the container is located in a communal area. (c) is incorrect because constructive possession was designed precisely to reach defendants who are not physically holding the contraband. (d) is incorrect because constructive possession requires proven awareness and control, not strict liability based on status. (e) is incorrect because circumstantial evidence (the ledger, his role) sufficiently proves his knowledge of the safe's contents.

**Tags:** chapters: [15], topics: [constructive-possession, awareness, control], difficulty: easy, cognitive: application

**Grounding:** Chapter 15: Drugs and Guns > Refinements > Constructive Possession

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Defense counsel routinely argues that finding drugs in a "communal, unlocked basement" is legally insufficient for possession because multiple people have access to the area. If a defendant lacks exclusive spatial control over the environment where drugs are found, a student could argue that the prosecution cannot reliably establish the defendant's exclusive dominion and control, necessitating an acquittal.
(b) Argument-for: Constructive possession requires the power and intent to exercise control over the contraband, along with awareness of its presence. Having the key to the specific locked safe where the drugs are stored directly establishes the "power" to exercise control, overriding the fact that the safe was located in a communal area. This legally grounds an affirmative finding of constructive possession.
(c) Argument-for: While constructive possession expands liability beyond actual possession, a student might mistakenly believe that the doctrine still requires a close spatial or temporal nexus. One could argue that without "immediate proximity" to the contraband, the defendant lacks the present "power" to exercise control, rendering the possession charge legally insufficient.
(d) Argument-for: In cases involving enterprise criminality, leaders who direct an organization hold overarching authority over its operations and premises. A student could argue that this absolute authority essentially translates into vicarious or strict liability for any contraband found within the organization's controlled territory (the apartment building), justifying a conviction based on his leadership status.
(e) Argument-for: Constructive possession requires knowledge of the specific contraband (mens rea). If the safe is completely unmarked, a student could argue there is no direct evidence Marcus knew it contained cocaine as opposed to lawful valuables, and that this absence of physical labeling creates an absolute evidentiary bar preventing the state from proving knowledge beyond a reasonable doubt.

Head-to-head: Option (b) correctly applies the hornbook elements of constructive possession (awareness + power/intent to control). Distractors (c) and (d) are easily defeated by explicit, bright-line false legal rules (immediate proximity requirement and strict liability, respectively). Distractor (e) falsely claims that an unmarked safe creates an absolute evidentiary bar to proving mens rea, which ignores that circumstantial evidence can establish knowledge. Distractor (a), however, relies merely on a factual inference—that lacking exclusive spatial control over the basement defeats possession. Under the strict close-call standard, (a) lacks an explicitly locked, categorically false legal claim, making it a weaker distractor that relies on factual ambiguity rather than a flawed rule of law.

Falsifiable claim per distractor:
- (a): "meaning he lacked exclusive spatial control over the area." — Implicitly wrong because exclusive spatial control over the *room* isn't required if you control the *container*, but this lacks an absolute word to lock it as a false legal rule.
- (c): "constructive possession requires immediate proximity." — Explicitly wrong because constructive possession was specifically designed to apply when the defendant does *not* have immediate proximity/actual possession.
- (d): "he is strictly liable for any narcotics" — Explicitly wrong because constructive possession is never a strict liability offense; it requires proven mens rea (awareness) and control.
- (e): "preventing the prosecution from proving beyond a reasonable doubt" — Explicitly wrong because the state is never "prevented" from proving knowledge merely because a safe is unmarked; circumstantial evidence regularly satisfies this burden.

Recommended fix: Add absolute wording to (a) to formulate an explicitly false legal rule. For example: Change (a) to "No, because constructive possession categorically requires the defendant to maintain exclusive spatial control over the entire room where the drugs are found."
-->

## Issue 3 — argpass-opus

**Q11.** Marcus is charged with possession of the 500 grams of cocaine found in the basement safe. Under the doctrine of constructive possession, is the evidence sufficient to convict him?

(a) No, because the safe was located in a communal, unlocked basement, meaning he lacked exclusive spatial control over the area.
(b) Yes, because the key on his nightstand establishes his awareness of the drugs and his power and intent to exercise control over them. <!-- correct -->
(c) No, because he was not physically holding the drugs at the time of his arrest, and constructive possession requires immediate proximity.
(d) Yes, because as the leader of the organization, he is strictly liable for any narcotics found within his apartment building.
(e) No, because the safe was unmarked, preventing the prosecution from proving beyond a reasonable doubt that he knew what was inside it.

**Answer:** (b)

**Explanation:** (b) is correct. Constructive possession requires proof that the defendant had awareness of the contraband and the power and intent to exercise dominion and control over it. Holding the sole key to a locked safe, combined with his leadership of the drug ring and the ledger, firmly establishes this control. (a) is incorrect because control over the container (via the key) establishes constructive possession even if the container is located in a communal area. (c) is incorrect because constructive possession was designed precisely to reach defendants who are not physically holding the contraband. (d) is incorrect because constructive possession requires proven awareness and control, not strict liability based on status. (e) is incorrect because circumstantial evidence (the ledger, his role) sufficiently proves his knowledge of the safe's contents.

**Tags:** chapters: [15], topics: [constructive-possession, awareness, control], difficulty: easy, cognitive: application

**Grounding:** Chapter 15: Drugs and Guns > Refinements > Constructive Possession

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might choose this option relying on the rule that when contraband is found in a jointly occupied or communal area, mere proximity is insufficient to establish constructive possession. The argument emphasizes that without exclusive spatial control over the communal basement, the prosecution cannot presume Marcus had the power to control the safe's contents. Therefore, the lack of exclusive control over the premises allegedly defeats the constructive possession claim.
(b) Argument-for: Constructive possession requires that a defendant have knowledge of the contraband and the power and intent to exercise dominion and control over it. The fact that Marcus possessed the key on his nightstand demonstrates his direct physical power to access the safe. Combined with circumstantial evidence like his role in the organization, this establishes his awareness and intent, making this the correct application of the doctrine.
(c) Argument-for: A student could argue that possession inherently requires some degree of immediate physical nexus to the contraband to prevent overbroad application of drug laws. Under this view, constructive possession still necessitates that the drugs be within a zone of immediate control or proximity. Because Marcus was not physically holding the drugs and they were in the basement rather than his immediate vicinity, this option claims the proximity element is unsatisfied.
(d) Argument-for: Under theories of vicarious liability, such as the Pinkerton doctrine, a leader of a criminal conspiracy is responsible for the foreseeable substantive crimes committed by co-conspirators in furtherance of the conspiracy. A student might conflate this conspiratorial liability with the elements of constructive possession. Thus, they might reason that his status as an organizational leader automatically imposes strict liability for any drugs stored within the building.
(e) Argument-for: Constructive possession requires proof beyond a reasonable doubt that the defendant knew of the presence and character of the contraband. An unmarked safe in a communal area offers no outward visual indication of its contents. A student might argue that without explicit markings or direct admissions, the physical characteristics of the safe legally preclude the prosecution from ever proving the required mens rea to the requisite standard.

Head-to-head: Option (b) correctly states the legal standard for constructive possession—awareness plus the power and intent to exercise control—and accurately maps the facts (the key) to this standard. Option (c) fails because it asserts constructive possession requires "immediate proximity," which flatly contradicts the doctrine's purpose. Option (d) fails because it applies a "strictly liable" standard based on status, whereas constructive possession requires individualized proof of awareness and control. Option (e) fails because it asserts the unmarked safe "prevent[s]" the prosecution from proving knowledge, ignoring that circumstantial evidence is legally sufficient. Option (a) is the weakest distractor structurally; rather than providing an explicit false legal rule, it merely states a true fact (lacking exclusive spatial control) and implicitly concludes it defeats possession, failing the close-call standard's requirement for a falsifiable claim.

Falsifiable claim per distractor:
- (a): None. The phrase "meaning he lacked exclusive spatial control over the area" is factually true and implicitly relies on a false legal premise, failing to provide an explicit, falsifiable legal claim.
- (c): "constructive possession requires immediate proximity" — wrong because constructive possession applies precisely when the defendant has control without immediate physical proximity.
- (d): "he is strictly liable" — wrong because constructive possession requires proven awareness and intent to control, not strict or vicarious liability based on organizational status.
- (e): "preventing the prosecution from proving beyond a reasonable doubt" — wrong because circumstantial evidence can lawfully prove knowledge of an unmarked container's contents.

Recommended fix: Modify (a) to include an explicit, absolute false legal rule. Change to: "(a) No, because the safe was located in a communal, unlocked basement, and constructive possession categorically requires the defendant to maintain exclusive spatial control over the premises."
-->
