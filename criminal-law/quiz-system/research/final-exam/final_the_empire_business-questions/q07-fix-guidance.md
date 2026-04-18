# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q7.** Assume Dominic is convicted of the fentanyl offense, and the government seeks a mandatory minimum sentence based on the 2-kilogram quantity. Dominic argues the mandatory minimum cannot apply because he did not intend to distribute that specific quantity of fentanyl, as he thought it was heroin. How will the court rule?

(a) The mandatory minimum applies because the statutory sentence floor is triggered by the actual drug weight alone, regardless of his specific intent regarding substance type. <!-- correct -->
(b) The mandatory minimum applies because possessing two kilograms of any controlled substance automatically triggers the highest available federal sentencing enhancements under the guidelines.
(c) The mandatory minimum does not apply because the government must explicitly prove he had the specific intent to distribute at least the threshold amount of fentanyl.
(d) The mandatory minimum does not apply because the Eighth Amendment strictly prohibits imposing severe sentencing enhancements based on entirely unknown factual circumstances.
(e) The mandatory minimum does not apply because the exact drug quantity was not explicitly listed as a material element in the underlying federal charging document.

**Answer:** (a)

**Explanation:** Under 21 U.S.C. § 841(b), federal mandatory minimum sentences are triggered strictly by the actual weight of the drug involved. The prosecution does not need to prove that the defendant intended to distribute that specific quantity or substance type to trigger the enhancement; the penalty floor is based entirely on the objective grams possessed. (b) is wrong because different substances have vastly different quantity thresholds for enhancements. (c) is wrong because intent only applies to the underlying distribution charge, not the weight-based sentencing enhancement. (d) is wrong because courts consistently uphold weight-based mandatory minimums against Eighth Amendment challenges, provided the base offense is proven. (e) is wrong because while drug weight must be charged and proven to a jury under *Apprendi*, the defendant's intent regarding that weight is irrelevant.

**Tags:** chapters: [15], topics: [drugs, mandatory-minimums, quantity], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 15, Federal Weight-Based Mandatory Minimums

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The intended substance and weight (2kg of heroin) triggers the exact same 10-year mandatory minimum under 21 U.S.C. § 841(b)(1)(A) as the actual substance (2kg of fentanyl). This renders Dominic's argument factually moot and weakens the doctrinal test, as a court could reject his defense simply because his intended conduct carried the identical mandatory penalty anyway. 
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Ideally, change Dominic's belief in the global facts to a substance that carries no mandatory minimum at 2kg (e.g., marijuana) to create a true asymmetry. Alternatively, tweak Option A to clarify that the actual drug *type and weight* strictly control the statutory floor, making his specific subjective belief legally irrelevant regardless of what he thought he possessed.
-->

## Issue 3 — argpass-sonnet

**Q7.** Assume Dominic is convicted of the fentanyl offense, and the government seeks a mandatory minimum sentence based on the 2-kilogram quantity. Dominic argues the mandatory minimum cannot apply because he did not intend to distribute that specific quantity of fentanyl, as he thought it was heroin. How will the court rule?

(a) The mandatory minimum applies because the statutory sentence floor is triggered by the actual drug weight alone, regardless of his specific intent regarding substance type. <!-- correct -->
(b) The mandatory minimum applies because possessing two kilograms of any controlled substance automatically triggers the highest available federal sentencing enhancements under the guidelines.
(c) The mandatory minimum does not apply because the government must explicitly prove he had the specific intent to distribute at least the threshold amount of fentanyl.
(d) The mandatory minimum does not apply because the Eighth Amendment strictly prohibits imposing severe sentencing enhancements based on entirely unknown factual circumstances.
(e) The mandatory minimum does not apply because the exact drug quantity was not explicitly listed as a material element in the underlying federal charging document.

**Answer:** (a)

**Explanation:** Under 21 U.S.C. § 841(b), federal mandatory minimum sentences are triggered strictly by the actual weight of the drug involved. The prosecution does not need to prove that the defendant intended to distribute that specific quantity or substance type to trigger the enhancement; the penalty floor is based entirely on the objective grams possessed. (b) is wrong because different substances have vastly different quantity thresholds for enhancements. (c) is wrong because intent only applies to the underlying distribution charge, not the weight-based sentencing enhancement. (d) is wrong because courts consistently uphold weight-based mandatory minimums against Eighth Amendment challenges, provided the base offense is proven. (e) is wrong because while drug weight must be charged and proven to a jury under *Apprendi*, the defendant's intent regarding that weight is irrelevant.

**Tags:** chapters: [15], topics: [drugs, mandatory-minimums, quantity], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 15, Federal Weight-Based Mandatory Minimums

<!-- argument-pass: MUST FIX
(a) Argument-for: Under 21 U.S.C. § 841, the statutory maximums and mandatory minimums are determined by the actual type and quantity of the controlled substance. The Supreme Court has held that the mens rea requirement (knowingly or intentionally) applies only to the fact that the defendant is dealing with some controlled substance, not to the specific type or quantity. Therefore, Dominic's mistaken belief that he possessed heroin rather than fentanyl does not save him from the fentanyl mandatory minimum. The strict liability nature of drug quantity and type for sentencing means the actual weight triggers the floor.
(b) Argument-for: A student could argue that possessing a massive quantity of drugs like two kilograms of any Schedule I or II substance indicates high-level trafficking. The Federal Sentencing Guidelines often apply severe base offense levels for large quantities. The student might conclude that a threshold of two kilograms is a universal trigger for top-tier enhancements regardless of the exact substance, making the type irrelevant because the quantity alone maxes out the penalty.
(c) Argument-for: The core of criminal law is that actus reus must be accompanied by mens rea. A student could argue that under general principles of culpability, a defendant cannot be held strictly liable for a sentencing enhancement that drastically increases their punishment. To trigger the fentanyl-specific mandatory minimum, the government should have to prove he had the specific intent to distribute fentanyl in that amount, matching the mens rea to the aggravating circumstance.
(d) Argument-for: The Eighth Amendment prohibits cruel and unusual punishment, which includes grossly disproportionate sentences. A student might argue that imposing a mandatory minimum for a substance and quantity the defendant had no knowledge of offends the Eighth Amendment's proportionality principle. Punishing someone for "entirely unknown factual circumstances" could be seen as inherently arbitrary and thus constitutionally prohibited under modern sentencing jurisprudence.
(e) Argument-for: Under Apprendi and Alleyne, any fact that increases the mandatory minimum sentence must be submitted to a jury and found beyond a reasonable doubt. This means the drug quantity must be explicitly charged in the indictment as a material element. If the charging document merely alleged "a controlled substance" without the exact quantity, the court cannot constitutionally impose the mandatory minimum, making this a procedurally correct reason the enhancement fails.

Head-to-head: (a) correctly states that drug type and quantity operate as strict liability elements under § 841(b) once the base mens rea is met. Distractors (b), (c), and (d) all make explicitly false legal claims regarding sentencing guidelines, specific intent, and Eighth Amendment jurisprudence respectively. However, (e) lacks a falsifiable legal error. Under Alleyne, it is legally true that the quantity must be explicitly listed in the charging document to trigger a mandatory minimum. Option (e) acts as a distractor solely by assuming a fact not provided in the prompt (that the quantity was omitted from the indictment), meaning it tests reading comprehension/factual assumption rather than legal knowledge.

Falsifiable claim per distractor:
- (b): "possessing two kilograms of any controlled substance automatically triggers the highest available federal sentencing enhancements" — wrong because different substances (e.g., marijuana vs. fentanyl) have wildly different quantity thresholds for enhancements.
- (c): "the government must explicitly prove he had the specific intent to distribute at least the threshold amount of fentanyl" — wrong because specific intent is not required for the type or quantity under federal drug sentencing laws.
- (d): "the Eighth Amendment strictly prohibits imposing severe sentencing enhancements based on entirely unknown factual circumstances" — wrong because courts routinely uphold strict liability weight-based mandatory minimums against Eighth Amendment challenges.
- (e): LACKS A FALSE LEGAL CLAIM. The premise that a mandatory minimum fails if the quantity "was not explicitly listed as a material element in the underlying federal charging document" is legally correct under Alleyne. It is only "wrong" here because it assumes a fact not in the prompt.

Recommended fix: Revise (e) to contain a definitively false legal claim. For example: "(e) The mandatory minimum does not apply because federal drug enhancements categorically require the underlying charging document to allege the defendant's specific subjective belief regarding the substance's identity."
-->

## Issue 4 — argpass-opus

**Q7.** Assume Dominic is convicted of the fentanyl offense, and the government seeks a mandatory minimum sentence based on the 2-kilogram quantity. Dominic argues the mandatory minimum cannot apply because he did not intend to distribute that specific quantity of fentanyl, as he thought it was heroin. How will the court rule?

(a) The mandatory minimum applies because the statutory sentence floor is triggered by the actual drug weight alone, regardless of his specific intent regarding substance type. <!-- correct -->
(b) The mandatory minimum applies because possessing two kilograms of any controlled substance automatically triggers the highest available federal sentencing enhancements under the guidelines.
(c) The mandatory minimum does not apply because the government must explicitly prove he had the specific intent to distribute at least the threshold amount of fentanyl.
(d) The mandatory minimum does not apply because the Eighth Amendment strictly prohibits imposing severe sentencing enhancements based on entirely unknown factual circumstances.
(e) The mandatory minimum does not apply because the exact drug quantity was not explicitly listed as a material element in the underlying federal charging document.

**Answer:** (a)

**Explanation:** Under 21 U.S.C. § 841(b), federal mandatory minimum sentences are triggered strictly by the actual weight of the drug involved. The prosecution does not need to prove that the defendant intended to distribute that specific quantity or substance type to trigger the enhancement; the penalty floor is based entirely on the objective grams possessed. (b) is wrong because different substances have vastly different quantity thresholds for enhancements. (c) is wrong because intent only applies to the underlying distribution charge, not the weight-based sentencing enhancement. (d) is wrong because courts consistently uphold weight-based mandatory minimums against Eighth Amendment challenges, provided the base offense is proven. (e) is wrong because while drug weight must be charged and proven to a jury under *Apprendi*, the defendant's intent regarding that weight is irrelevant.

**Tags:** chapters: [15], topics: [drugs, mandatory-minimums, quantity], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 15, Federal Weight-Based Mandatory Minimums

<!-- argument-pass: MUST FIX
(a) Argument-for: This tracks established federal jurisprudence under 21 U.S.C. § 841(b). The mens rea requirement (knowledge) applies only to the fact that the substance is *some* controlled substance. Once the base offense is proven, the penalty enhancements—including mandatory minimums—operate as strict liability factors based entirely on the actual type and quantity of the drugs involved. 
(b) Argument-for: A student might reason that two kilograms is an objectively massive quantity of narcotics. They could conclude that under the federal sentencing scheme, possessing such a large commercial quantity of *any* drug is severely punished, thus "automatically" triggering maximum enhancements across the board.
(c) Argument-for: Relying on general principles of mens rea and the Supreme Court’s ruling in *Alleyne v. United States* (which made mandatory minimum triggers elements of the offense rather than mere sentencing factors), a student could argue that specific intent must logically attach to all material elements, meaning the government must prove Dominic intended the specific threshold quantity.
(d) Argument-for: A student might invoke the Eighth Amendment's prohibition on cruel and unusual punishment and its embedded proportionality principle. They could argue that imposing a severe mandatory minimum based on an "entirely unknown factual circumstance" (fentanyl disguised as heroin) creates a grossly disproportionate sentence relative to Dominic's subjective culpability.
(e) Argument-for: Under *Apprendi* and *Alleyne*, any fact that increases the statutory maximum or mandatory minimum must be charged in the indictment and proven to a jury. Since the prompt merely states Dominic was "convicted of the fentanyl offense" without specifying that the 2-kilogram quantity was explicitly charged, a student might assume this mandatory procedural step was missed, thereby invalidating the enhancement.

Head-to-head: (a) is the clearly correct legal standard, but (e) creates a fatal structural issue. Distractor (e) does not assert a false legal rule; rather, it asserts a factual condition ("was not explicitly listed") that is neither confirmed nor contradicted by the prompt. If a student assumes this fact is true because the prompt omitted it, (e) becomes legally correct under *Alleyne*. Furthermore, the provided explanation for (e) attacks a legal premise ("defendant's intent regarding that weight") that does not actually appear in the text of option (e). This disconnect, combined with the fact that (e) could be correct if its factual assumption is granted, elevates this to a MUST FIX.

Falsifiable claim per distractor:
- (b): "possessing two kilograms of any controlled substance automatically triggers the highest available federal sentencing enhancements" — wrong because quantity thresholds vary wildly by substance (e.g., 2kg of marijuana does not trigger the highest enhancement).
- (c): "government must explicitly prove he had the specific intent to distribute at least the threshold amount" — wrong because § 841(b) mandatory minimums operate as strict liability regarding the exact quantity and type, once general mens rea for distribution is established.
- (d): "Eighth Amendment strictly prohibits imposing severe sentencing enhancements based on entirely unknown factual circumstances" — wrong because courts categorically uphold strict liability weight/type enhancements against Eighth Amendment disproportionality challenges.
- (e): Lacks a falsifiable legal error. "because the exact drug quantity was not explicitly listed..." makes a factual assertion about the prompt's unstated background rather than presenting a false legal rule. 

Recommended fix: Rewrite (e) so it makes a false legal claim that aligns with the current explanation. 
Change (e) to: "The mandatory minimum does not apply because the Sixth Amendment right to a jury trial categorically requires the government to prove the defendant explicitly knew the exact weight of the drugs."
-->
