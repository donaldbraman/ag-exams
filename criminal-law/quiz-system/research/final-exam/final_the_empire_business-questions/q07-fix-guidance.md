# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Assume Dominic is convicted of possessing the fentanyl with intent to distribute. How does the 2-kilogram quantity affect his sentence?

(a) The mandatory minimum applies only if the prosecution separately proves beyond a reasonable doubt that Dominic explicitly intended to distribute that specific two-kilogram quantity of drugs.
(b) The mandatory minimum applies automatically based on the exact drug weight alone, regardless of what the prosecution proves about his specific intent to distribute the narcotics. <!-- correct -->
(c) The mandatory minimum does not apply because Dominic genuinely believed he was distributing heroin, which carries a much higher weight threshold for triggering mandatory federal sentences.
(d) The mandatory minimum applies because the jury is allowed to use a permissive inference that anyone possessing two kilograms inherently intends to distribute the entire amount.
(e) The mandatory minimum does not apply unless the government can prove that Dominic specifically knew the weight of the illicit substance exceeded the statutory federal threshold.

**Answer:** (b)

**Explanation:** Under 21 U.S.C. § 841(b), mandatory minimum sentences are triggered purely by the weight of the drugs involved. The prosecution must prove the intent to distribute, but the weight itself operates as a strict liability sentencing factor. (a) is incorrect because the government does not need to prove the defendant intended to distribute the specific quantity, only that he possessed the quantity and had an overall intent to distribute. (c) is incorrect because knowledge of the specific substance type or its corresponding thresholds is not required; possessing the threshold weight of fentanyl triggers the penalty regardless of his mistaken belief. (d) is incorrect because while quantity can be circumstantial evidence of intent, the mandatory minimum itself is triggered directly by weight, not through a permissive inference of intent. (e) is incorrect because knowledge of the exact drug weight is not a required mens rea element.

**Tags:** chapters: [15], topics: [drug offenses, mandatory minimums, drug weight strict liability], difficulty: medium, cognitive: analysis

**Grounding:** Federal weight-based mandatory minimums; 21 U.S.C. 841(b)

<!-- audit: MUST FIX
check 1: finding - Option (b) is technically incorrect as written. It states the mandatory minimum applies "regardless of what the prosecution proves about his specific intent to distribute the narcotics." The prosecution absolutely must prove specific intent to distribute to trigger a PWID mandatory minimum; if they prove nothing about his specific intent, he cannot be subjected to the sentence. The option likely meant "intent to distribute the *entire quantity*," but is written too broadly. A prepared student would eliminate (b) because of this overstatement.
check 2: pass
check 3: finding - Explanation consistency fails. The explanation accurately states "The prosecution must prove the intent to distribute...", which directly contradicts the text of correct option (b) ("regardless of what the prosecution proves about his specific intent").
check 4: finding - Soft fail on facts: Option (c) is a structurally weak distractor because 2kg exceeds the 10-year mandatory minimum threshold for *both* fentanyl (400g) and heroin (1kg). A student aware of the statutory thresholds could eliminate (c) without knowing the strict liability doctrine simply because his mistaken belief wouldn't mathematically change the applicable minimum. 
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Revise option (b) to: "The mandatory minimum applies automatically based on the exact drug weight alone, regardless of whether the prosecution proves he intended to distribute that entire specific quantity or knew the actual drug type." Additionally, consider changing the drug quantity in the stem to 600 grams (which clears the 400g fentanyl threshold but falls short of the 1kg heroin threshold) to make (c) legally and mathematically viable as a distractor.
-->

## Issue 2 — edge-case

**Q7.** Assume Dominic is convicted of possessing the fentanyl with intent to distribute. How does the 2-kilogram quantity affect his sentence?

(a) The mandatory minimum applies only if the prosecution separately proves beyond a reasonable doubt that Dominic explicitly intended to distribute that specific two-kilogram quantity of drugs.
(b) The mandatory minimum applies automatically based on the exact drug weight alone, regardless of what the prosecution proves about his specific intent to distribute the narcotics. <!-- correct -->
(c) The mandatory minimum does not apply because Dominic genuinely believed he was distributing heroin, which carries a much higher weight threshold for triggering mandatory federal sentences.
(d) The mandatory minimum applies because the jury is allowed to use a permissive inference that anyone possessing two kilograms inherently intends to distribute the entire amount.
(e) The mandatory minimum does not apply unless the government can prove that Dominic specifically knew the weight of the illicit substance exceeded the statutory federal threshold.

**Answer:** (b)

**Explanation:** Under 21 U.S.C. § 841(b), mandatory minimum sentences are triggered purely by the weight of the drugs involved. The prosecution must prove the intent to distribute, but the weight itself operates as a strict liability sentencing factor. (a) is incorrect because the government does not need to prove the defendant intended to distribute the specific quantity, only that he possessed the quantity and had an overall intent to distribute. (c) is incorrect because knowledge of the specific substance type or its corresponding thresholds is not required; possessing the threshold weight of fentanyl triggers the penalty regardless of his mistaken belief. (d) is incorrect because while quantity can be circumstantial evidence of intent, the mandatory minimum itself is triggered directly by weight, not through a permissive inference of intent. (e) is incorrect because knowledge of the exact drug weight is not a required mens rea element.

**Tags:** chapters: [15], topics: [drug offenses, mandatory minimums, drug weight strict liability], difficulty: medium, cognitive: analysis

**Grounding:** Federal weight-based mandatory minimums; 21 U.S.C. 841(b)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Option (b)'s phrasing "regardless of what the prosecution proves about his specific intent to distribute the narcotics" is technically legally incorrect as written; the prosecution *must* prove his general intent to distribute the narcotics to secure the underlying § 841(a) conviction. The option likely meant to say "intent to distribute that exact quantity." Additionally, the explanation refers to drug weight as a "strict liability sentencing factor." Post-Alleyne v. United States (2013), any fact that increases a mandatory minimum is an *element* of the aggravated offense that must be submitted to the jury and proven beyond a reasonable doubt, not a sentencing factor.
3. Cross-Question Spoilers: pass
Recommended fix: Change (b) to: "The mandatory minimum applies based on the proven drug weight, regardless of whether Dominic specifically intended to distribute that exact quantity or knew its precise weight." Update the explanation to clarify that while weight operates as a strict liability *element* regarding mens rea, it must still be proven to the jury beyond a reasonable doubt (removing the obsolete "sentencing factor" phrasing).
-->

## Issue 3 — argpass-sonnet

**Q7.** Assume Dominic is convicted of possessing the fentanyl with intent to distribute. How does the 2-kilogram quantity affect his sentence?

(a) The mandatory minimum applies only if the prosecution separately proves beyond a reasonable doubt that Dominic explicitly intended to distribute that specific two-kilogram quantity of drugs.
(b) The mandatory minimum applies automatically based on the exact drug weight alone, regardless of what the prosecution proves about his specific intent to distribute the narcotics. <!-- correct -->
(c) The mandatory minimum does not apply because Dominic genuinely believed he was distributing heroin, which carries a much higher weight threshold for triggering mandatory federal sentences.
(d) The mandatory minimum applies because the jury is allowed to use a permissive inference that anyone possessing two kilograms inherently intends to distribute the entire amount.
(e) The mandatory minimum does not apply unless the government can prove that Dominic specifically knew the weight of the illicit substance exceeded the statutory federal threshold.

**Answer:** (b)

**Explanation:** Under 21 U.S.C. § 841(b), mandatory minimum sentences are triggered purely by the weight of the drugs involved. The prosecution must prove the intent to distribute, but the weight itself operates as a strict liability sentencing factor. (a) is incorrect because the government does not need to prove the defendant intended to distribute the specific quantity, only that he possessed the quantity and had an overall intent to distribute. (c) is incorrect because knowledge of the specific substance type or its corresponding thresholds is not required; possessing the threshold weight of fentanyl triggers the penalty regardless of his mistaken belief. (d) is incorrect because while quantity can be circumstantial evidence of intent, the mandatory minimum itself is triggered directly by weight, not through a permissive inference of intent. (e) is incorrect because knowledge of the exact drug weight is not a required mens rea element.

**Tags:** chapters: [15], topics: [drug offenses, mandatory minimums, drug weight strict liability], difficulty: medium, cognitive: analysis

**Grounding:** Federal weight-based mandatory minimums; 21 U.S.C. 841(b)

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that under *Alleyne v. United States*, any fact that increases a mandatory minimum is an element of the offense. Because the base offense requires the mens rea of "intent to distribute," the prosecution must arguably prove that the defendant's specific intent encompassed the aggravating element (the 2-kilogram quantity). Thus, without explicit intent regarding the specific threshold amount, the minimum cannot constitutionally apply.
(b) Argument-for: As the keyed answer, (b) relies on established federal doctrine under 21 U.S.C. § 841(b). Once the base offense (possession with intent to distribute) is proven, the drug quantity operates as a strict-liability factor. The defendant's subjective intent or knowledge concerning the specific quantity is legally irrelevant to the application of the statutory minimum, which is driven purely by the objective weight of the substance.
(c) Argument-for: A student might argue that the mens rea must attach to the facts that dictate the severity of the offense. In *McFadden v. United States*, the Supreme Court held that the government must prove the defendant knew he was dealing with a controlled substance. If Dominic genuinely believed he possessed heroin (which has a 1-kg threshold for a 10-year minimum, unlike fentanyl's 400-gram threshold), punishing him under fentanyl's stricter schedule without the requisite knowledge violates fundamental mens rea principles.
(d) Argument-for: A student could defend (d) by focusing on how intent is practically established in drug cases. Possession of a commercial quantity of narcotics routinely permits a jury to infer an intent to distribute, as the volume is wildly inconsistent with personal use. Therefore, the mandatory minimum is effectively triggered because the sheer volume of the drugs provides the permissive inference that satisfies the intent element for the entire amount.
(e) Argument-for: Much like the arguments derived from *Apprendi* and *Rehaif v. United States*, a student could argue that the presumption of mens rea requires a defendant to know the facts that make his conduct subject to severe penalties. Therefore, to trigger a weight-based mandatory minimum, Dominic must have actually known that the weight exceeded the statutory federal threshold.

Head-to-head: 
(b) correctly identifies that drug weight is a strict-liability factor under federal law. However, (b)'s phrasing—"regardless of what the prosecution proves about his specific intent to distribute the narcotics"—is dangerously broad and legally problematic. If the prosecution actively proves that Dominic possessed 2 kilograms but specifically intended to distribute only 10 grams (keeping the rest for personal use), several federal circuits hold that the personal-use quantity is excluded from the mandatory minimum calculation for a possession-with-intent-to-distribute (PWID) conviction. Thus, stating the minimum applies "regardless of what the prosecution proves about his specific intent" is potentially false. Furthermore, (d) lacks a sharp falsifiable error, as it merely conflates the evidentiary permissive inference of the base offense with the automatic statutory mechanism of the penalty.

Falsifiable claim per distractor:
- (a): "only if the prosecution separately proves beyond a reasonable doubt that Dominic explicitly intended to distribute that specific two-kilogram quantity" — wrong because § 841(b) operates as strict liability regarding the quantity; specific intent to distribute the exact threshold amount is not required.
- (c): "The mandatory minimum does not apply because Dominic genuinely believed he was distributing heroin" — wrong because federal law imposes strict liability for the actual drug type and weight; mistake of fact regarding the controlled substance type does not defeat the minimum.
- (d): "The mandatory minimum applies because the jury is allowed to use a permissive inference..." — wrong because the mandatory minimum does not apply *because* of an evidentiary inference; it applies by direct statutory operation of the objective weight itself once the base conviction is secured.
- (e): "unless the government can prove that Dominic specifically knew the weight... exceeded the statutory federal threshold" — wrong because knowledge of the drug weight is strictly not a required mens rea element.

Recommended fix: Revise (b) to remove the legally fraught "regardless of" clause. Change (b) to: "The mandatory minimum applies based on the actual drug weight involved, because federal law treats the drug quantity triggering the penalty as a strict-liability factor once the base offense is proven." Also, tweak (d) to introduce a clearer error: "(d) The mandatory minimum applies solely because a jury must categorically presume that possessing two kilograms proves an intent to distribute the entire amount."
-->
