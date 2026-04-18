# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Assume Avon and Marlowe are guilty of conspiracy to distribute narcotics. Is Avon liable for Marlowe's federal felony of storing hazardous chemicals without a permit under the Pinkerton doctrine?

(a) Liable, because he explicitly told Marlowe he did not care how the processing was done, establishing direct participation.
(b) Liable, because storing hazardous chemicals was a reasonably foreseeable consequence of the drug conspiracy and done in furtherance of it. <!-- correct -->
(c) Not liable, because the federal chemical statute requires specific intent, which cannot be imputed through a conspiracy.
(d) Not liable, because he did not personally sign the invoice for the hazardous chemicals purchased by his manager.
(e) Not liable, because chemical storage is a regulatory offense rather than a traditional inherently dangerous common law felony.

**Answer:** (b)

**Explanation:** (b) is correct because under the *Pinkerton* doctrine, a conspirator is vicariously liable for the substantive offenses committed by co-conspirators if those offenses are reasonably foreseeable and committed in furtherance of the conspiracy. Setting up a secret chemical processing lab is foreseeable in a drug distribution network. (a) fails because *Pinkerton* liability is vicarious and does not require direct participation in the target offense. (c) fails because *Pinkerton* imputes liability regardless of the target offense's specific mens rea, provided the conspiracy nexus is met. (d) fails because vicarious liability bypasses the need for personal execution. (e) fails because *Pinkerton* applies to regulatory federal felonies.

**Tags:** chapters: [19], topics: [pinkerton doctrine, vicarious liability, foreseeability], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 19 - Conspiracy (Pinkerton Doctrine)

<!-- audit: MUST FIX
check 1: pass
check 2: A prepared student could point out that without facts establishing Marlowe stored the chemicals *for* the distribution conspiracy rather than for his own separate, independent project, liability cannot be established. Thus, (b) assumes a factual conclusion that isn't supported by the stem.
check 3: pass
check 4: MUST FIX. The stem is entirely missing the factual scenario needed to answer the question. It provides merely one sentence ("Assume Avon and Marlowe..."). Furthermore, distractors (a) ("explicitly told Marlowe") and (d) ("invoice... purchased by his manager") refer to highly specific factual details that are completely absent from the prompt, suggesting this question was orphaned from a broader fact pattern. 
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Provide the full fact pattern in the stem. Detail the nature of Avon and Marlowe's operation, the conversation about "processing" that option (a) references, the invoice/manager dynamic in option (d), and facts demonstrating that the chemical storage was actually done in furtherance of their joint drug enterprise.
-->

## Issue 2 — edge-case

**Q12.** Assume Avon and Marlowe are guilty of conspiracy to distribute narcotics. Is Avon liable for Marlowe's federal felony of storing hazardous chemicals without a permit under the Pinkerton doctrine?

(a) Liable, because he explicitly told Marlowe he did not care how the processing was done, establishing direct participation.
(b) Liable, because storing hazardous chemicals was a reasonably foreseeable consequence of the drug conspiracy and done in furtherance of it. <!-- correct -->
(c) Not liable, because the federal chemical statute requires specific intent, which cannot be imputed through a conspiracy.
(d) Not liable, because he did not personally sign the invoice for the hazardous chemicals purchased by his manager.
(e) Not liable, because chemical storage is a regulatory offense rather than a traditional inherently dangerous common law felony.

**Answer:** (b)

**Explanation:** (b) is correct because under the *Pinkerton* doctrine, a conspirator is vicariously liable for the substantive offenses committed by co-conspirators if those offenses are reasonably foreseeable and committed in furtherance of the conspiracy. Setting up a secret chemical processing lab is foreseeable in a drug distribution network. (a) fails because *Pinkerton* liability is vicarious and does not require direct participation in the target offense. (c) fails because *Pinkerton* imputes liability regardless of the target offense's specific mens rea, provided the conspiracy nexus is met. (d) fails because vicarious liability bypasses the need for personal execution. (e) fails because *Pinkerton* applies to regulatory federal felonies.

**Tags:** chapters: [19], topics: [pinkerton doctrine, vicarious liability, foreseeability], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 19 - Conspiracy (Pinkerton Doctrine)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Calling the chemical storage "Marlowe's federal felony" as a definitive noun phrase implicitly confirms that Marlowe committed the offense. This spoils Q3 (which tests whether the silent federal statute requires mens rea under Morissette and whether Marlowe's mistaken belief exculpates him) and Q7 (felony murder based on the underlying chemical felony). 
Recommended fix: Explicitly make Marlowe's guilt part of the assumption to avoid confirming it for the student. Change the stem to: "Assume Avon and Marlowe are guilty of conspiracy to distribute narcotics, and assume Marlowe's chemical storage constitutes a federal felony. Is Avon liable for the storage offense under the Pinkerton doctrine?"
-->

## Issue 3 — argpass-sonnet

**Q12.** Assume Avon and Marlowe are guilty of conspiracy to distribute narcotics. Is Avon liable for Marlowe's federal felony of storing hazardous chemicals without a permit under the Pinkerton doctrine?

(a) Liable, because he explicitly told Marlowe he did not care how the processing was done, establishing direct participation.
(b) Liable, because storing hazardous chemicals was a reasonably foreseeable consequence of the drug conspiracy and done in furtherance of it. <!-- correct -->
(c) Not liable, because the federal chemical statute requires specific intent, which cannot be imputed through a conspiracy.
(d) Not liable, because he did not personally sign the invoice for the hazardous chemicals purchased by his manager.
(e) Not liable, because chemical storage is a regulatory offense rather than a traditional inherently dangerous common law felony.

**Answer:** (b)

**Explanation:** (b) is correct because under the *Pinkerton* doctrine, a conspirator is vicariously liable for the substantive offenses committed by co-conspirators if those offenses are reasonably foreseeable and committed in furtherance of the conspiracy. Setting up a secret chemical processing lab is foreseeable in a drug distribution network. (a) fails because *Pinkerton* liability is vicarious and does not require direct participation in the target offense. (c) fails because *Pinkerton* imputes liability regardless of the target offense's specific mens rea, provided the conspiracy nexus is met. (d) fails because vicarious liability bypasses the need for personal execution. (e) fails because *Pinkerton* applies to regulatory federal felonies.

**Tags:** chapters: [19], topics: [pinkerton doctrine, vicarious liability, foreseeability], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 19 - Conspiracy (Pinkerton Doctrine)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might argue that Avon's reckless delegation or authorization constitutes direct participation, making him liable. They could mistakenly believe that Pinkerton liability requires direct involvement or authorization in the specific act, viewing this option as a correct synthesis of factual complicity and the doctrine.
(b) Argument-for: Under the Pinkerton doctrine, a co-conspirator is vicariously liable for the substantive offenses of other conspirators if those crimes are reasonably foreseeable and committed in furtherance of the conspiracy. Processing narcotics requires chemicals, making Marlowe’s storage of them a foreseeable consequence of the drug conspiracy, thus perfectly satisfying the Pinkerton elements.
(c) Argument-for: A student might argue that specific intent crimes require the defendant to personally hold the requisite mens rea. They could conclude that while Pinkerton imputes the actus reus for general intent crimes, it categorically cannot impute a specific mens rea for regulatory felonies without direct proof of the defendant's state of mind.
(d) Argument-for: A student might focus on the physical actus reus requirement, arguing that for specific regulatory offenses like unpermitted chemical storage, personal action is necessary. By noting Avon did not personally sign the invoice, the student argues he lacks the necessary physical involvement, defeating Pinkerton liability.
(e) Argument-for: A student could argue that Pinkerton, as a common law doctrine, was uniquely designed to impute liability for traditional, inherently dangerous felonies like robbery or murder. They might conclude that extending this vicarious liability to modern statutory or regulatory offenses stretches the doctrine beyond its limits, rendering it inapplicable here.

Head-to-head: Option (b) correctly identifies the core elements of Pinkerton liability (foreseeability and in furtherance of the conspiracy). Option (a) incorrectly attributes liability to "direct participation," which directly contradicts the vicarious nature of Pinkerton, and it introduces facts absent from the prompt. Option (c) contains an explicit false legal claim about the inability to impute specific intent. Option (d) offers an irrelevant factual negative ("did not personally sign") without explicitly locking in the false legal premise it relies upon. Option (e) provides a clear, falsifiable legal distinction regarding regulatory versus common law offenses. Because options (a) and (d) rely on implicit legal errors or unstated facts rather than explicit, absolute legal claims, the question falls short of the strict close-call standard and should be fixed.

Falsifiable claim per distractor:
- (a): "establishing direct participation" — wrong because Pinkerton creates vicarious liability, not direct participation liability; additionally, it relies on fabricated facts about what Avon "explicitly told" Marlowe rather than an absolute legal rule.
- (c): "specific intent, which cannot be imputed through a conspiracy" — wrong because Pinkerton explicitly permits imputing the required mens rea of foreseeable substantive offenses committed in furtherance of the conspiracy, including specific intent.
- (d): "because he did not personally sign the invoice" — wrong because it relies on an implicitly false legal assumption (that personal acts are required) rather than stating an explicit, absolute claim; under Pinkerton, personal execution is categorically unnecessary.
- (e): "because chemical storage is a regulatory offense rather than a traditional inherently dangerous common law felony" — wrong because Pinkerton applies equally to federal statutory and regulatory offenses, not just traditional common law felonies.

Recommended fix: Revise (a) and (d) to remove fabricated facts and lock in explicit false legal claims. Change (a) to: "Liable, solely because Pinkerton categorically applies to any crime committed by a co-conspirator, regardless of foreseeability." Change (d) to: "Not liable, because Pinkerton liability categorically requires the defendant to personally participate in the actus reus of the target offense."
-->

## Issue 4 — argpass-opus

**Q12.** Assume Avon and Marlowe are guilty of conspiracy to distribute narcotics. Is Avon liable for Marlowe's federal felony of storing hazardous chemicals without a permit under the Pinkerton doctrine?

(a) Liable, because he explicitly told Marlowe he did not care how the processing was done, establishing direct participation.
(b) Liable, because storing hazardous chemicals was a reasonably foreseeable consequence of the drug conspiracy and done in furtherance of it. <!-- correct -->
(c) Not liable, because the federal chemical statute requires specific intent, which cannot be imputed through a conspiracy.
(d) Not liable, because he did not personally sign the invoice for the hazardous chemicals purchased by his manager.
(e) Not liable, because chemical storage is a regulatory offense rather than a traditional inherently dangerous common law felony.

**Answer:** (b)

**Explanation:** (b) is correct because under the *Pinkerton* doctrine, a conspirator is vicariously liable for the substantive offenses committed by co-conspirators if those offenses are reasonably foreseeable and committed in furtherance of the conspiracy. Setting up a secret chemical processing lab is foreseeable in a drug distribution network. (a) fails because *Pinkerton* liability is vicarious and does not require direct participation in the target offense. (c) fails because *Pinkerton* imputes liability regardless of the target offense's specific mens rea, provided the conspiracy nexus is met. (d) fails because vicarious liability bypasses the need for personal execution. (e) fails because *Pinkerton* applies to regulatory federal felonies.

**Tags:** chapters: [19], topics: [pinkerton doctrine, vicarious liability, foreseeability], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 19 - Conspiracy (Pinkerton Doctrine)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might choose this option if they conflate *Pinkerton* liability with accomplice liability. They could argue that Avon’s alleged instruction that he "did not care" how the processing was done provides the requisite authorization to establish direct participation. Because they mistakenly believe direct participation is required or sufficient for this specific doctrine, they would view this factual assumption as the strongest basis for liability.
(b) Argument-for: This option perfectly encapsulates the core elements of the *Pinkerton* doctrine. A co-conspirator is vicariously liable for the substantive crimes of their co-conspirators if those offenses are reasonably foreseeable and committed in furtherance of the conspiracy. Given that narcotics distribution requires chemical processing, storing hazardous chemicals is a reasonably foreseeable act in furtherance of the conspiracy.
(c) Argument-for: A student could defend this by arguing that specific intent offenses require a specialized mens rea that vicarious liability doctrines cannot satisfy. They might believe that while general intent crimes can be imputed, specific intent crimes demand the defendant personally harbor the intent. Therefore, they would conclude that the conspiracy alone cannot impute the necessary mental state for this offense.
(d) Argument-for: A student might defend this option by viewing the chemical storage felony as an administrative or paperwork offense. They might argue that criminal liability for failing to sign an invoice strictly requires the defendant to be the party responsible for the administrative process. Thus, Avon's lack of personal involvement in signing the paperwork seemingly shields him from vicarious liability.
(e) Argument-for: A student could argue that the *Pinkerton* doctrine is a common law concept historically limited to inherently dangerous felonies like robbery or murder. They might conclude that applying vicarious liability to a modern regulatory or strict-liability offense overextends the doctrine beyond its historical boundaries. Thus, they would select this option under the belief that *Pinkerton* categorically excludes regulatory administrative felonies.

Head-to-head:
Option (b) is the only correct statement of the law, properly applying the *Pinkerton* foreseeability standard. Options (a) and (d) introduce phantom facts (an explicit instruction, an invoice signed by a manager) not present in the brief prompt, making them procedurally flawed. Legally, (a) incorrectly equates *Pinkerton* with direct participation, while (d) implies personal execution is required. Options (c) and (e) offer explicitly false legal rules: (c) claims specific intent cannot be imputed, and (e) implies the doctrine is restricted to common law felonies. Because (a) and (d) rely on unstated facts and several distractors lack absolute locking words, a fix is recommended to tighten the options.

Falsifiable claim per distractor:
- (a): "establishing direct participation" — wrong because *Pinkerton* imposes vicarious liability, rendering direct participation legally irrelevant to the application of the doctrine.
- (c): "which cannot be imputed through a conspiracy" — wrong because *Pinkerton* explicitly allows the imputation of the requisite mens rea, including specific intent, for substantive offenses.
- (d): "because he did not personally sign the invoice" — wrong because *Pinkerton* imposes vicarious liability precisely when the defendant did not personally execute the actus reus.
- (e): "rather than a traditional inherently dangerous common law felony" — wrong because *Pinkerton* liability applies fully to federal regulatory and statutory felonies and is not restricted to common law crimes.

Recommended fix: Integrate the missing facts into the prompt (e.g., "Avon told Marlowe he didn't care how the processing was done, and Marlowe's manager purchased the chemicals without Avon signing the invoice"). To enforce the close-call standard with absolute words, revise (a) to end with "establishing direct participation, which is categorically required," revise (d) to start with "Not liable solely because...", and revise (e) to read "Not liable, because Pinkerton categorically excludes regulatory offenses..."
-->
