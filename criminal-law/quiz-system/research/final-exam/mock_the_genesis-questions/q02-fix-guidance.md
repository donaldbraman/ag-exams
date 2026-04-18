# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q2.** Assume Dan is charged as an accomplice to the Blue-X manufacturing conspiracy. Can Dan's requisite mental state (purpose to aid the crime) be established based solely on his transaction with Albert?

(a) Purpose to aid the conspiracy can be inferred because Dan charged a grossly inflated 500% markup on the ether while knowing its intended illegal use. <!-- correct -->
(b) Purpose to aid the conspiracy cannot be inferred because Dan explicitly disclaimed any desire to share in the future profits of the Blue-X sales.
(c) Purpose to aid the conspiracy cannot be inferred because ether is a common industrial chemical that possesses widespread legitimate academic applications.
(d) Purpose to aid the conspiracy can be inferred because mere knowledge of a buyer's illegal intent is universally sufficient for accomplice liability.
(e) Purpose to aid the conspiracy cannot be inferred because Dan did not physically assist Albert in transporting or storing the highly volatile precursor chemicals.

**Answer:** (a)

**Explanation:** (a) is correct. Under the *Lauria* standard, when a supplier lacks an explicit stake in the venture, the requisite purpose to facilitate the crime can still be inferred if the supplier charges a grossly inflated price (a 500% markup) for the materials. (b) is wrong because the exorbitant markup serves as an independent basis to infer purpose, overcoming Dan's verbal disclaimer. (c) is wrong because the inflated pricing specific to the illicit use overrides the chemical's general legitimate applications. (d) is wrong because mere knowledge is generally insufficient for accomplice liability without special factors like inflated pricing or a lack of legitimate use. (e) is wrong because physical assistance is not required; supplying the materials is sufficient if the requisite purpose exists.

**Tags:** chapters: [18, 19], topics: [accomplice liability, knowledge vs purpose, lauria], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, People v. Lauria

<!-- audit: SHOULD FIX
check 1: pass
check 2: pass. (b) is a defensible but correctly beatable distractor (the verbal disclaimer of future profits does not negate the immediate "stake in the venture" established by the 500% markup).
check 3: The explanation misparaphrases the *Lauria* doctrine. It states "when a supplier lacks an explicit stake... purpose... can still be inferred if the supplier charges a grossly inflated price." Under *Lauria*, charging an inflated price *is* the classic example of acquiring a stake in the venture, rather than acting as an alternative inference when a stake is lacking.
check 4: Pass (assuming a master fact pattern provides the factual details of Dan's transaction with Albert). However, the phrasing "accomplice to the... conspiracy" is doctrinally messy. A sharp student might be distracted by debating whether one can legally aid and abet a conspiracy, rather than focusing on the supplier mens rea issue.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Update the explanation to accurately reflect that the 500% markup *constitutes* a stake in the venture under *Lauria*. In the stem, consider changing the charge to either "an accomplice to the manufacture of Blue-X" or "a co-conspirator" to avoid the hybrid "accomplice to a conspiracy" framing.
-->

## Issue 2 — edge-case

**Q2.** Assume Dan is charged as an accomplice to the Blue-X manufacturing conspiracy. Can Dan's requisite mental state (purpose to aid the crime) be established based solely on his transaction with Albert?

(a) Purpose to aid the conspiracy can be inferred because Dan charged a grossly inflated 500% markup on the ether while knowing its intended illegal use.
(b) Purpose to aid the conspiracy cannot be inferred because Dan explicitly disclaimed any desire to share in the future profits of the Blue-X sales.
(c) Purpose to aid the conspiracy cannot be inferred because ether is a common industrial chemical that possesses widespread legitimate academic applications.
(d) Purpose to aid the conspiracy can be inferred because mere knowledge of a buyer's illegal intent is universally sufficient for accomplice liability.
(e) Purpose to aid the conspiracy cannot be inferred because Dan did not physically assist Albert in transporting or storing the highly volatile precursor chemicals.

**Answer:** (a)

**Explanation:** (a) is correct. Under the *Lauria* standard, when a supplier lacks an explicit stake in the venture, the requisite purpose to facilitate the crime can still be inferred if the supplier charges a grossly inflated price (a 500% markup) for the materials. (b) is wrong because the exorbitant markup serves as an independent basis to infer purpose, overcoming Dan's verbal disclaimer. (c) is wrong because the inflated pricing specific to the illicit use overrides the chemical's general legitimate applications. (d) is wrong because mere knowledge is generally insufficient for accomplice liability without special factors like inflated pricing or a lack of legitimate use. (e) is wrong because physical assistance is not required; supplying the materials is sufficient if the requisite purpose exists.

**Tags:** chapters: [18, 19], topics: [accomplice liability, knowledge vs purpose, lauria], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, People v. Lauria

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: The phrase "accomplice to the... conspiracy" conflates two distinct forms of inchoate/derivative liability. While the *Lauria* factors (like inflated markup) apply to establish the "purpose" mens rea for both accomplice liability and conspiracy, charging someone as an "accomplice to a conspiracy" is doctrinally messy and unrecognized in many jurisdictions.
3. Cross-Question Spoilers: pass
Recommended fix: Change the prompt to either "charged as an accomplice to the manufacture of Blue-X" (and update the answer choices to say "Purpose to aid the crime") OR change it to "charged as a co-conspirator in the Blue-X manufacturing conspiracy" to ensure doctrinal precision.
-->

## Issue 3 — argpass-sonnet

**Q2.** Assume Dan is charged as an accomplice to the Blue-X manufacturing conspiracy. Can Dan's requisite mental state (purpose to aid the crime) be established based solely on his transaction with Albert?

(a) Purpose to aid the conspiracy can be inferred because Dan charged a grossly inflated 500% markup on the ether while knowing its intended illegal use. <!-- correct -->
(b) Purpose to aid the conspiracy cannot be inferred because Dan explicitly disclaimed any desire to share in the future profits of the Blue-X sales.
(c) Purpose to aid the conspiracy cannot be inferred because ether is a common industrial chemical that possesses widespread legitimate academic applications.
(d) Purpose to aid the conspiracy can be inferred because mere knowledge of a buyer's illegal intent is universally sufficient for accomplice liability.
(e) Purpose to aid the conspiracy cannot be inferred because Dan did not physically assist Albert in transporting or storing the highly volatile precursor chemicals.

**Answer:** (a)

**Explanation:** (a) is correct. Under the *Lauria* standard, when a supplier lacks an explicit stake in the venture, the requisite purpose to facilitate the crime can still be inferred if the supplier charges a grossly inflated price (a 500% markup) for the materials. (b) is wrong because the exorbitant markup serves as an independent basis to infer purpose, overcoming Dan's verbal disclaimer. (c) is wrong because the inflated pricing specific to the illicit use overrides the chemical's general legitimate applications. (d) is wrong because mere knowledge is generally insufficient for accomplice liability without special factors like inflated pricing or a lack of legitimate use. (e) is wrong because physical assistance is not required; supplying the materials is sufficient if the requisite purpose exists.

**Tags:** chapters: [18, 19], topics: [accomplice liability, knowledge vs purpose, lauria], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, People v. Lauria

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under *People v. Lauria*, an intent or purpose to aid a conspiracy can be inferred from a supplier's knowledge of the illegal use if the supplier has a "stake in the venture." Charging a grossly inflated price (e.g., a 500% markup) is explicitly recognized in *Lauria* as establishing such a stake. Therefore, Dan's purpose to aid the crime can be legally inferred from his specific pricing structure, making this option correct.
(b) Argument-for: Accomplice liability requires the specific intent to facilitate the crime. A student could argue that Dan's explicit verbal disclaimer of any desire to share in the future profits directly negates the requisite "purpose" to further the conspiracy. If Dan explicitly rejects a stake in the downstream success of the venture, he operates merely as a knowing supplier, meaning his purpose to aid cannot be legally inferred.
(c) Argument-for: *Lauria* explicitly notes that supplying goods with widespread legitimate uses (like a telephone answering service) does not normally support an inference of purpose, unlike supplying goods with no legitimate use (like loaded dice). Because ether is a common industrial chemical with legitimate academic applications, a student could argue that the "no legitimate use" prong of *Lauria* fails, barring any inference of purpose.
(d) Argument-for: A student might argue that under alternative MPC approaches or for highly dangerous felonies, the line between knowledge and purpose blurs, meaning that a supplier's mere knowledge of the buyer's illegal intent is universally sufficient to establish accomplice liability. Since Dan knew of the intended illegal use, this option would correctly conclude that liability attaches based on knowledge alone.
(e) Argument-for: The actus reus of accomplice liability requires meaningful assistance or encouragement. A student could argue that merely executing a commercial sale, without physically assisting in the dangerous transport or storage of the volatile chemicals, amounts to mere preparation rather than actionable assistance. Consequently, an inference of purpose to aid is legally invalid without physical involvement in the crime's execution.

Head-to-head: 
Option (a) correctly applies the exact holding of *Lauria*, which identifies charging an inflated price as a definitive way to establish a stake in the venture, thereby allowing the inference of purpose. Option (b) fails because a verbal disclaimer of *future* profits does not negate the immediate stake in the venture gained through the 500% upfront markup. Option (c) fails because, while ether has legitimate uses, the inflated price offers an independent ground to infer purpose. Option (d) contains an explicit absolute ("universally sufficient") which makes it definitively false, as *Lauria* establishes that mere knowledge is generally insufficient. Option (e) falsely assumes physical assistance is a legal prerequisite for liability. While all distractors are conceptually incorrect, (b), (c), and (e) lack the explicit absolute lock words required by the strict close-call standard to prevent students from arguing that these factors *might* weigh against the inference in a totality-of-the-circumstances balancing test.

Falsifiable claim per distractor:
- (b): "cannot be inferred because Dan explicitly disclaimed" — wrong because under *Lauria*, an inflated upfront price establishes a stake in the venture that legally permits the inference of purpose regardless of a disclaimer of future profits.
- (c): "cannot be inferred because ether is a common industrial chemical" — wrong because the presence of legitimate uses does not legally preclude the inference of purpose when an independent basis (inflated price) establishes a stake in the venture.
- (d): "mere knowledge ... is universally sufficient" — wrong because mere knowledge of a buyer's illegal intent is the classic baseline of what is legally *insufficient* for accomplice liability absent special factors.
- (e): "cannot be inferred because Dan did not physically assist" — wrong because the act of selling/supplying the materials constitutes sufficient actus reus for accomplice liability; physical transport/storage is not legally required.

Recommended fix: Add absolute lock words to (b), (c), and (e) to make their legal claims explicitly and unconditionally false. 
- Change (b) to: "A verbal disclaimer of future profits categorically precludes the inference of a purpose to aid the conspiracy."
- Change (c) to: "Purpose to aid the conspiracy automatically cannot be inferred whenever the supplied good has widespread legitimate academic applications."
- Change (e) to: "Accomplice liability is always defeated if the supplier does not physically assist Albert in transporting or storing the highly volatile precursor chemicals."
-->
