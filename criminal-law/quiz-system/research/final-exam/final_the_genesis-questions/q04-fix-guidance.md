# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Marlowe is charged under the federal statute that penalizes anyone who "knowingly stores hazardous chemicals without a permit." He argues that he genuinely believed Acetone-FX was a harmless water-based cleaner. Does this mistake provide a valid defense?

(a) No, because mistake of law is never a valid criminal defense, and Marlowe should have independently verified the city's building and chemical storage codes.
(b) Yes, because his actual belief negates the specific mental state of "knowingly" required by the statute for the material element of storing hazardous chemicals. <!-- correct -->
(c) No, because public welfare offenses automatically impose strict liability on the defendant, rendering any mistaken factual beliefs about the chemicals entirely irrelevant.
(d) Yes, but only if the jury ultimately determines that his mistaken belief about the harmless nature of the cleaner was objectively reasonable under the circumstances.
(e) No, because Marlowe was engaged in manufacturing illicit drugs, which is morally suspect conduct that strips him of all mistake defenses under the malum in se doctrine.

**Answer:** (b)

**Explanation:** (b) is correct because the statute explicitly includes the mens rea "knowingly." Under the *Morissette* presumption and MPC § 2.02(4), this requires the prosecution to prove Marlowe knew the chemicals were hazardous; his honest factual mistake negates that required mental state. (a) is wrong because his error concerns the physical properties of the chemicals (a mistake of fact), not the existence of the law. (c) is wrong because the explicit mens rea term defeats any public welfare strict liability presumption. (d) is wrong because "knowledge" is a subjective standard, meaning an honest mistake defeats the element even if objectively unreasonable. (e) is wrong because the *Prince* malum in se limitation applies to strict liability or ambiguous statutes, not to explicit knowledge requirements.

**Tags:** chapters: [10], topics: [mistake of fact, mens rea, Morissette presumption, MPC one-for-all], difficulty: medium, cognitive: application

**Grounding:** mof-mental-state-negation / mpc-one-for-all

<!-- audit: SHOULD FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: Option (e) introduces a hallucinated fact. The stem never mentions Marlowe "manufacturing illicit drugs," but (e) treats it as a factual premise. This makes the distractor confusing and trivially excludable for students tracking the facts.
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: In option (e), replace the hallucinated drug facts with conduct actually in the stem (e.g., "No, because storing unverified industrial chemicals without a permit is morally suspect conduct that strips him...").
-->

## Issue 2 — argpass-opus

**Q4.** Marlowe is charged under the federal statute that penalizes anyone who "knowingly stores hazardous chemicals without a permit." He argues that he genuinely believed Acetone-FX was a harmless water-based cleaner. Does this mistake provide a valid defense?

(a) No, because mistake of law is never a valid criminal defense, and Marlowe should have independently verified the city's building and chemical storage codes.
(b) Yes, because his actual belief negates the specific mental state of "knowingly" required by the statute for the material element of storing hazardous chemicals. <!-- correct -->
(c) No, because public welfare offenses automatically impose strict liability on the defendant, rendering any mistaken factual beliefs about the chemicals entirely irrelevant.
(d) Yes, but only if the jury ultimately determines that his mistaken belief about the harmless nature of the cleaner was objectively reasonable under the circumstances.
(e) No, because Marlowe was engaged in manufacturing illicit drugs, which is morally suspect conduct that strips him of all mistake defenses under the malum in se doctrine.

**Answer:** (b)

**Explanation:** (b) is correct because the statute explicitly includes the mens rea "knowingly." Under the *Morissette* presumption and MPC § 2.02(4), this requires the prosecution to prove Marlowe knew the chemicals were hazardous; his honest factual mistake negates that required mental state. (a) is wrong because his error concerns the physical properties of the chemicals (a mistake of fact), not the existence of the law. (c) is wrong because the explicit mens rea term defeats any public welfare strict liability presumption. (d) is wrong because "knowledge" is a subjective standard, meaning an honest mistake defeats the element even if objectively unreasonable. (e) is wrong because the *Prince* malum in se limitation applies to strict liability or ambiguous statutes, not to explicit knowledge requirements.

**Tags:** chapters: [10], topics: [mistake of fact, mens rea, Morissette presumption, MPC one-for-all], difficulty: medium, cognitive: application

**Grounding:** mof-mental-state-negation / mpc-one-for-all

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might argue that ignorance of whether a chemical is regulated under a permit scheme is effectively a mistake of law. Since the baseline rule is that "ignorance of the law is no excuse," Marlowe's failure to verify the city's building and storage codes cannot shield him from liability. This option correctly reflects the strict approach to legal duties often expected in regulatory contexts.
(b) Argument-for: A student would argue that the statute includes the explicit mens rea term "knowingly." Under standard federal interpretation (e.g., *Morissette*) and MPC rules, this term travels down the statute to modify the material elements, including the nature of the chemicals as "hazardous." If Marlowe subjectively and honestly believed the cleaner was harmless, he did not "knowingly" store a hazardous chemical, meaning his mistake of fact directly negates the required mental state.
(c) Argument-for: A student might argue that storing hazardous chemicals without a permit is a classic public welfare offense, meant to protect the community from serious danger. Under the *Balint* or *Dotterweich* lines of cases, public welfare offenses dispense with mens rea. Therefore, the court would impose strict liability, making Marlowe's subjective beliefs about the chemicals irrelevant to his guilt.
(d) Argument-for: A student could argue that while a mistake of fact can be a defense, many jurisdictions require that the mistake be objectively reasonable to excuse the conduct. Because the statute involves dangerous materials, the law demands that the defendant's belief about the chemical's harmlessness meet a baseline of reasonableness. If the jury finds his belief was reckless or negligent, the defense fails, making objective reasonableness a strict prerequisite.
(e) Argument-for: A student might recall the "moral wrong" or "malum in se" doctrine from cases like *Regina v. Prince*. If Marlowe's underlying conduct was part of an illicit enterprise (drug manufacturing), his morally culpable baseline behavior strips him of the ability to claim an innocent mistake of fact. Because he was already engaged in a wrongful act, he assumes the risk of the attendant circumstances, neutralizing any mistake defense.

Head-to-head: (b) is the clear winner because the presence of an explicit "knowingly" requirement establishes a subjective standard for the material elements, allowing an honest mistake of fact to serve as a complete defense. (a) fails legally by falsely stating mistake of law is "never" a defense, and fundamentally mischaracterizes a mistake about a chemical's physical properties as a mistake of law. (c) wrongly claims public welfare offenses "automatically" impose strict liability, ignoring that an explicit statutory mens rea overrides this presumption. (d) fails legally because it imports a false "objectively reasonable" requirement into a purely subjective "knowingly" standard. (e) fails legally by claiming the moral wrong doctrine overrides explicit statutory knowledge elements, but more problematically, it hallucinates a fact not present in the prompt (manufacturing illicit drugs). 

Falsifiable claim per distractor:
- (a): "mistake of law is never a valid criminal defense" — wrong because mistake of law can sometimes be a valid defense (e.g., when it negates specific intent/knowledge, or via reasonable reliance on official interpretations).
- (c): "automatically impose strict liability" — wrong because an explicitly drafted mens rea like "knowingly" precludes automatic strict liability, even in a public welfare context.
- (d): "only if ... objectively reasonable" — wrong because "knowledge" is a subjective mental state, meaning an honest but unreasonable mistake is legally sufficient to negate the element.
- (e): "strips him of all mistake defenses" — wrong because the moral wrong/malum in se doctrine does not override an explicit statutory "knowledge" requirement; it also contains factually false information by inventing the drug-manufacturing scenario.

Recommended fix: Edit (e) so it relies on the facts provided rather than inventing a new scenario, to prevent a student from eliminating it solely on test-taking logic. Change (e) to: "No, because storing hazardous chemicals is morally suspect conduct, which categorically strips defendants of all mistake defenses under the malum in se doctrine regardless of statutory phrasing."
-->
