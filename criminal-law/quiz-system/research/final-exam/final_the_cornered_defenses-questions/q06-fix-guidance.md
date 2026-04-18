# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** Is Dexter guilty of accomplice liability for providing the accelerant to Marcus?

(a) Guilty, because his act of price-gouging Marcus establishes that he possessed the required specific intent to commit the target arson.
(b) Guilty, because he sold the materials with full knowledge of how they would be used, satisfying the general intent standard.
(c) Not guilty, because he did not personally participate in loading the accelerant or executing the plan at the target warehouse.
(d) Not guilty, because he merely knew of Marcus's criminal plan and lacked the specific purpose to facilitate the commission of the arson. <!-- correct -->
(e) Not guilty, because commercial vendors are categorically immune from derivative liability regardless of their mental state or the buyer's known intentions.

**Answer:** (d)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the underlying offense. Mere knowledge of the principal's criminal plan is insufficient. Under cases like *Lauria*, while charging a disproportionate price might occasionally serve as circumstantial evidence of a stake in the venture, the facts stipulate Dexter "had no personal stake" and only wanted to profit from the sale, lacking the specific purpose to see the arson succeed. (a) is incorrect because price-gouging alone does not legally establish purpose when the facts explicitly stipulate a lack of personal stake in the target crime. (b) is incorrect because accomplice liability requires specific intent (purpose), not mere knowledge (general intent). (c) is incorrect because physical presence or direct participation in the target actus reus is not required for accomplice liability. (e) is incorrect because there is no categorical immunity for commercial vendors; they can be accomplices if they act with the requisite criminal purpose.

**Tags:** chapters: [18], topics: [accomplice liability, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - mr-purpose-not-knowledge

<!-- audit: MUST FIX
1: pass
2: Defensibility failure. If the (missing) facts state that Dexter price-gouged Marcus, a prepared student would mount a strong challenge for (a). Under *People v. Lauria*, charging an inflated price for goods known to be used illegally is one of the primary ways a vendor demonstrates a "stake in the venture," which allows the legal inference of specific intent/purpose. 
3: Explanation drift. The explanation fundamentally mischaracterizes *Lauria* by contrasting price-gouging with "only want[ing] to profit from the sale." Under *Lauria*, seeking an inflated profit *is* the personal stake that elevates mere knowledge to purpose. A fact pattern cannot stipulate "price-gouging" and "no personal stake" simultaneously without creating a doctrinal contradiction.
4: Missing facts. The question stem completely omits the fact pattern. It references Dexter, Marcus, the accelerant, and the arson, but provides no factual setup to evaluate Dexter's actions, pricing, or mental state. 
5: pass
6: pass
7: pass (Note: *Lauria* is technically mapped to Ch 19 Conspiracy, but it applies perfectly to the Ch 18 Accomplice `mr-purpose-not-knowledge` tag).
Recommended fix: Provide the missing scenario in the stem. In the facts, explicitly state that Dexter charged standard market rates (no price-gouging) to cleanly avoid the *Lauria* "stake in the venture" inference. Revise option (a) and the explanation to reflect that standard pricing removes the inference of purpose.
-->

## Issue 2 — edge-case

**Q6.** Is Dexter guilty of accomplice liability for providing the accelerant to Marcus?

(a) Guilty, because his act of price-gouging Marcus establishes that he possessed the required specific intent to commit the target arson.
(b) Guilty, because he sold the materials with full knowledge of how they would be used, satisfying the general intent standard.
(c) Not guilty, because he did not personally participate in loading the accelerant or executing the plan at the target warehouse.
(d) Not guilty, because he merely knew of Marcus's criminal plan and lacked the specific purpose to facilitate the commission of the arson. <!-- correct -->
(e) Not guilty, because commercial vendors are categorically immune from derivative liability regardless of their mental state or the buyer's known intentions.

**Answer:** (d)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the underlying offense. Mere knowledge of the principal's criminal plan is insufficient. Under cases like *Lauria*, while charging a disproportionate price might occasionally serve as circumstantial evidence of a stake in the venture, the facts stipulate Dexter "had no personal stake" and only wanted to profit from the sale, lacking the specific purpose to see the arson succeed. (a) is incorrect because price-gouging alone does not legally establish purpose when the facts explicitly stipulate a lack of personal stake in the target crime. (b) is incorrect because accomplice liability requires specific intent (purpose), not mere knowledge (general intent). (c) is incorrect because physical presence or direct participation in the target actus reus is not required for accomplice liability. (e) is incorrect because there is no categorical immunity for commercial vendors; they can be accomplices if they act with the requisite criminal purpose.

**Tags:** chapters: [18], topics: [accomplice liability, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - mr-purpose-not-knowledge

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The facts state Dexter charged "triple the usual price to profit off the crime." Under the classic *People v. Lauria* standard, charging an inflated price legally establishes a "stake in the venture," which allows purpose to be inferred from mere knowledge. Additionally, the target offense is arson (a serious, aggravated felony), which is another *Lauria* category where knowledge alone can satisfy the intent requirement. The author's attempt to stipulate he "had no personal stake" directly contradicts the legal significance of charging triple, making (a) a completely valid (and arguably more doctrinally accurate) answer. 
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Modify the underlying fact pattern to state that Dexter simply charged his "standard, customary price" to eliminate the *Lauria* inflated-price exception, OR change the question to make (a) the correct answer by fully embracing the *Lauria* exception.
-->

## Issue 3 — argpass-sonnet

**Q6.** Is Dexter guilty of accomplice liability for providing the accelerant to Marcus?

(a) Guilty, because his act of price-gouging Marcus establishes that he possessed the required specific intent to commit the target arson.
(b) Guilty, because he sold the materials with full knowledge of how they would be used, satisfying the general intent standard.
(c) Not guilty, because he did not personally participate in loading the accelerant or executing the plan at the target warehouse.
(d) Not guilty, because he merely knew of Marcus's criminal plan and lacked the specific purpose to facilitate the commission of the arson. <!-- correct -->
(e) Not guilty, because commercial vendors are categorically immune from derivative liability regardless of their mental state or the buyer's known intentions.

**Answer:** (d)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the underlying offense. Mere knowledge of the principal's criminal plan is insufficient. Under cases like *Lauria*, while charging a disproportionate price might occasionally serve as circumstantial evidence of a stake in the venture, the facts stipulate Dexter "had no personal stake" and only wanted to profit from the sale, lacking the specific purpose to see the arson succeed. (a) is incorrect because price-gouging alone does not legally establish purpose when the facts explicitly stipulate a lack of personal stake in the target crime. (b) is incorrect because accomplice liability requires specific intent (purpose), not mere knowledge (general intent). (c) is incorrect because physical presence or direct participation in the target actus reus is not required for accomplice liability. (e) is incorrect because there is no categorical immunity for commercial vendors; they can be accomplices if they act with the requisite criminal purpose.

**Tags:** chapters: [18], topics: [accomplice liability, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - mr-purpose-not-knowledge

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under cases like *People v. Lauria*, an intent to facilitate a crime can sometimes be inferred if the provider has a "stake in the venture." Charging an inflated price (price-gouging) for materials known to be used for a criminal purpose is one of the specific ways a seller demonstrates a stake in the venture. By extracting a premium based on the illicit use, Dexter acquires a financial interest in the transaction's completion, which a student could argue establishes the specific intent required for accomplice liability.
(b) Argument-for: While the majority rule requires specific intent (purpose), some jurisdictions and older common law precedents have occasionally allowed "knowledge" of a serious felony to suffice for liability. By selling dangerous accelerants with full knowledge of the arson plot, Dexter provided material assistance to a dangerous felony. Under this minority view, knowledge of the impending harm satisfies the mental state requirement for facilitation, rendering it akin to a general intent standard.
(c) Argument-for: Accomplice liability requires actual assistance or encouragement. A student could argue that merely selling a dual-use good without any physical participation or presence at the crime scene renders Dexter's connection too attenuated to constitute the actus reus of aiding and abetting. Since he did not partake in the actual execution, his acts fall short of the active participation they might believe is required to be held liable for the target act.
(d) Argument-for: The standard rule for accomplice liability, as articulated by the Model Penal Code and majority common law, requires that the accomplice act with the "purpose of promoting or facilitating" the offense. Mere knowledge that a product will be used in a crime is insufficient, especially for commercial vendors in ordinary transactions. Because Dexter only intended to complete the sale for profit and lacked the specific purpose to see the arson succeed, he lacks the requisite mens rea.
(e) Argument-for: One could argue that public policy strongly protects the stream of commerce, leading to a de facto immunity for commercial vendors selling ordinary goods. If vendors were held liable for the subsequent acts of their buyers, commerce would be severely chilled. Thus, an argument exists that the law categorically insulates commercial vendors from derivative liability based on the buyer's actions, regardless of the vendor's collateral knowledge.

Head-to-head: Option (d) correctly states the majority rule that purpose is required for accomplice liability and applies it accurately. Option (e) is well-locked with "categorically immune." Option (b) contains a clear false claim ("satisfying the general intent standard"), as accomplice liability is a specific intent crime. However, Options (a) and (c) are insufficiently locked and fail the strict close-call standard. Option (a) claims price-gouging "establishes" specific intent; a student could argue this just means "provides sufficient evidence to establish in this instance" rather than asserting a false categorical rule. Option (c) states Dexter is not guilty "because he did not personally participate," which implies a legal requirement but does not explicitly state it as an absolute rule. These distractors should be locked with absolute words.

Falsifiable claim per distractor:
- (a): "establishes that he possessed the required specific intent" — wrong because under *Lauria*, price gouging may support an inference of a stake in the venture, but it does not conclusively establish specific intent as a matter of law, particularly if rebutted by facts showing no actual purpose.
- (b): "satisfying the general intent standard" — wrong because accomplice liability requires specific intent (purpose), not general intent.
- (c): "because he did not personally participate in loading the accelerant or executing the plan" — wrong (as an implied legal rule) because physical presence or direct execution of the target actus reus is categorically not required for accomplice liability.
- (e): "commercial vendors are categorically immune... regardless of their mental state" — wrong because there is no categorical immunity; vendors are liable if they act with the purpose of facilitating the crime.

Recommended fix: Change (a) to: "Guilty, because charging an inflated price automatically establishes the specific intent to commit the target crime regardless of his actual purpose." Change (c) to: "Not guilty, solely because physical participation in the target crime's execution is categorically required for accomplice liability."
-->

## Issue 4 — argpass-opus

**Q6.** Is Dexter guilty of accomplice liability for providing the accelerant to Marcus?

(a) Guilty, because his act of price-gouging Marcus establishes that he possessed the required specific intent to commit the target arson.
(b) Guilty, because he sold the materials with full knowledge of how they would be used, satisfying the general intent standard.
(c) Not guilty, because he did not personally participate in loading the accelerant or executing the plan at the target warehouse.
(d) Not guilty, because he merely knew of Marcus's criminal plan and lacked the specific purpose to facilitate the commission of the arson. <!-- correct -->
(e) Not guilty, because commercial vendors are categorically immune from derivative liability regardless of their mental state or the buyer's known intentions.

**Answer:** (d)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the underlying offense. Mere knowledge of the principal's criminal plan is insufficient. Under cases like *Lauria*, while charging a disproportionate price might occasionally serve as circumstantial evidence of a stake in the venture, the facts stipulate Dexter "had no personal stake" and only wanted to profit from the sale, lacking the specific purpose to see the arson succeed. (a) is incorrect because price-gouging alone does not legally establish purpose when the facts explicitly stipulate a lack of personal stake in the target crime. (b) is incorrect because accomplice liability requires specific intent (purpose), not mere knowledge (general intent). (c) is incorrect because physical presence or direct participation in the target actus reus is not required for accomplice liability. (e) is incorrect because there is no categorical immunity for commercial vendors; they can be accomplices if they act with the requisite criminal purpose.

**Tags:** chapters: [18], topics: [accomplice liability, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 - mr-purpose-not-knowledge

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under *People v. Lauria*, charging a disproportionate price for goods known to be used in a crime can serve as circumstantial evidence of a "stake in the venture." A student could argue that Dexter's price-gouging crossed the line from a purely indifferent commercial transaction to one where he possessed a vested financial interest in the illicit use. Thus, the argument asserts that this act of price-gouging legally establishes the specific intent required for accomplice liability.
(b) Argument-for: A student could point to the fact that Dexter had "full knowledge" of the arson plan when he sold the accelerant. In some older contexts or for extremely serious felonies, courts have sometimes blurred the lines between knowledge and purpose. The argument would be that knowingly providing the precise means for a dangerous crime satisfies a general intent standard that is sufficient for complicity in this specific jurisdiction.
(c) Argument-for: Accomplice liability requires an actus reus of aiding, abetting, or encouraging the principal. A student could argue that merely selling a product, without being present or physically executing the plan at the warehouse, constitutes mere preparation rather than actionable assistance. Therefore, without personal participation in the immediate execution of the arson, Dexter's conduct is too remote to incur derivative liability.
(d) Argument-for: This correctly applies the prevailing modern and Model Penal Code standard for complicity. Accomplice liability requires that the defendant act with the specific intent or purpose of promoting or facilitating the target crime. Mere knowledge of the buyer's criminal intent—without a shared purpose or true personal stake in the successful commission of the crime—is legally insufficient to make a vendor an accomplice. 
(e) Argument-for: To protect everyday commerce, the law places a high barrier on holding vendors criminally liable for their customers' autonomous acts. A student could argue that public policy demands a categorical immunity for commercial vendors selling lawful, dual-use goods. Under this theory, imposing a duty to police buyers' intentions would paralyze trade, meaning vendors are shielded regardless of their subjective mental state.

Head-to-head: Option (d) is clearly the best answer because it states the universally tested majority rule: accomplice liability requires specific purpose, not mere knowledge. Option (b) fails by explicitly invoking a non-existent "general intent standard" for accomplice liability. Option (e) fails by explicitly inventing a "categorical" vendor immunity. Options (a) and (c) are strong distractors, but currently they lack the absolute terminology required to lock them as legally false per the strict close-call standard; (a) relies on the word "establishes" (which is arguably falsifiable but could be read colloquially as "proves in this instance"), and (c) merely gives a factual reason ("because he did not personally participate") without cementing it as a false absolute legal requirement. 

Falsifiable claim per distractor:
- (a): "establishes that he possessed the required specific intent" — wrong because price-gouging is merely potential circumstantial evidence of intent, not an automatic establishment of specific intent as a matter of law.
- (b): "satisfying the general intent standard" — wrong because accomplice liability requires specific intent (purpose).
- (c): "because he did not personally participate" — wrong because it relies on the implicit, false legal premise that physical participation in the target actus reus is required to be an accomplice.
- (e): "categorically immune from derivative liability regardless of their mental state" — wrong because vendors absolutely can be liable if they act with the explicit purpose of facilitating the crime.

Recommended fix: Add absolute words to lock in the legal falsity of (a) and (c). 
Change (a) to: "Guilty, because his act of price-gouging Marcus automatically establishes as a matter of law that he possessed..."
Change (c) to: "Not guilty, because physical participation at the target crime scene is always required to establish the actus reus of accomplice liability."
-->
