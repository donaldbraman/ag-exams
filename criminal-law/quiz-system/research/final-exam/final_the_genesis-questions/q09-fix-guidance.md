# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q9.** The DA charges Stringer as an accomplice to the illicit drug manufacturing. Stringer knew Marlowe would use the Acetone-FX to make drugs, but he sold it at standard market rates and had no stake in the profits. Is Stringer liable as an accomplice under the traditional common law standard?

(a) Yes, because Stringer's provision of a necessary chemical with knowledge of its illicit use inherently satisfies the mens rea for common law accomplice liability.
(b) Yes, because Stringer committed an overt act in furtherance of the crime by successfully delivering the Acetone-FX directly to the illicit warehouse.
(c) No, because providing a standard commodity at market rates without a stake in the venture does not establish the purposeful intent required to facilitate the crime. <!-- correct -->
(d) No, because Acetone-FX is a legal, multi-use product, making it legally impossible for Stringer to be charged as an accomplice to its subsequent misuse.
(e) No, because accomplice liability stringently requires that the defendant be physically present at the scene of the crime when the principal commits the offense.

**Answer:** (c)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the underlying offense. Supplying ordinary goods at standard prices, even with knowledge of their intended illicit use, generally fails to establish this purposeful intent. (a) fails because mere knowledge is insufficient; purpose is the required standard for facilitation. (b) fails because an overt act without the requisite purposeful mens rea does not create accomplice liability. (d) fails because it is entirely possible to be an accomplice using legal goods (e.g., selling a legal firearm specifically to aid a murder). (e) fails because physical presence is not required; an accessory before the fact can be held liable without being at the scene.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (mr-purpose-not-knowledge)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might recall that under certain modern interpretations or specific severe-crime exceptions (like *Fountain*), knowledge can sometimes suffice for liability if the provided good is essential. If Acetone-FX is seen as highly dangerous or strictly necessary, a student might incorrectly conclude that knowing provision "inherently satisfies" the common law mens rea.
(b) Argument-for: A student could focus heavily on the actus reus component of accomplice liability. Since Stringer didn't just sell the goods but actively delivered them "directly to the illicit warehouse," this looks like a substantial overt act of facilitation. The student might believe that this affirmative step materially aiding the crime is enough to trigger liability, disregarding the mental state.
(c) Argument-for: This aligns perfectly with the classic *United States v. Peoni* and *People v. Lauria* standards. A merchant selling ordinary goods at market prices without a financial stake in the illicit venture lacks the "purpose" to facilitate the crime. Mere knowledge of the buyer's criminal intent is historically insufficient for traditional common law accomplice liability.
(d) Argument-for: A student might confuse the law of accomplice liability with doctrines of strict product liability or dual-use technologies (like the *Sony Betamax* standard). They could assume that because a product is broadly available and multi-use, the law categorically shields the seller from criminal liability to prevent chilling commerce.
(e) Argument-for: A student might conflate general accomplice liability with the specific historic category of a "principal in the second degree." Since principals in the second degree required physical or constructive presence at the scene, a student might erroneously think all accomplice liability stringently requires physical presence.

Head-to-head:
Option (c) correctly identifies the standard merchant rule: knowledge without a stake does not establish purpose. Options (a), (d), and (e) are highly effective distractors because they provide the wrong answer while relying on explicitly falsifiable legal claims ("inherently satisfies", "legally impossible", "stringently requires"). However, Option (b) reaches the wrong conclusion ("Yes") but justifies it using a factually true statement (he did commit an overt act) without explicitly stating a false legal rule. It relies on the implicit omission of the mens rea requirement. Under the close-call standard, implicit omissions do not suffice, so (b) should be revised to include an explicitly false absolute claim. 

Falsifiable claim per distractor:
- (a): "inherently satisfies the mens rea for common law accomplice liability" — wrong because traditional common law requires purpose (or a stake in the venture), not mere knowledge, for ordinary merchants.
- (b): Lacks an explicitly false legal rule. It relies on an implicit omission (ignoring the missing mens rea) to falsely conclude "Yes."
- (d): "making it legally impossible for Stringer to be charged" — wrong because a merchant can absolutely be an accomplice using legal, multi-use goods if they act with the requisite purposeful intent.
- (e): "accomplice liability stringently requires that the defendant be physically present" — wrong because accessories before the fact can be liable without physical presence.

Recommended fix: Change (b) to "Yes, because committing an overt act that successfully furthers the crime automatically triggers accomplice liability regardless of the defendant's mens rea."
-->

## Issue 3 — argpass-opus

**Q9.** The DA charges Stringer as an accomplice to the illicit drug manufacturing. Stringer knew Marlowe would use the Acetone-FX to make drugs, but he sold it at standard market rates and had no stake in the profits. Is Stringer liable as an accomplice under the traditional common law standard?

(a) Yes, because Stringer's provision of a necessary chemical with knowledge of its illicit use inherently satisfies the mens rea for common law accomplice liability.
(b) Yes, because Stringer committed an overt act in furtherance of the crime by successfully delivering the Acetone-FX directly to the illicit warehouse.
(c) No, because providing a standard commodity at market rates without a stake in the venture does not establish the purposeful intent required to facilitate the crime. <!-- correct -->
(d) No, because Acetone-FX is a legal, multi-use product, making it legally impossible for Stringer to be charged as an accomplice to its subsequent misuse.
(e) No, because accomplice liability stringently requires that the defendant be physically present at the scene of the crime when the principal commits the offense.

**Answer:** (c)

**Explanation:** Accomplice liability requires that the defendant act with the *purpose* of promoting or facilitating the underlying offense. Supplying ordinary goods at standard prices, even with knowledge of their intended illicit use, generally fails to establish this purposeful intent. (a) fails because mere knowledge is insufficient; purpose is the required standard for facilitation. (b) fails because an overt act without the requisite purposeful mens rea does not create accomplice liability. (d) fails because it is entirely possible to be an accomplice using legal goods (e.g., selling a legal firearm specifically to aid a murder). (e) fails because physical presence is not required; an accessory before the fact can be held liable without being at the scene.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (mr-purpose-not-knowledge)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under some early or minority views (such as the rationale explored in *Backun v. United States*), providing a necessary instrument for a crime with knowledge of its illicit purpose might be construed as sufficient for liability. A student could argue that by supplying the crucial chemical, Stringer crossed the line from passive bystander to active facilitator. From this perspective, the student could argue that his knowledge "inherently satisfies" the mens rea, effectively equating his knowing provision with intentional facilitation of the crime.
(b) Argument-for: Actus reus for accomplice liability requires an overt act that assists or encourages the underlying crime. Stringer successfully delivering the Acetone-FX directly to the illicit warehouse is an undeniable, tangible act of assistance. A student focusing strictly on this physical contribution might argue that completing such a significant overt act in furtherance of the crime suffices to establish full liability. Thus, they could defend (b) by prioritizing actus reus over mens rea.
(c) Argument-for: Under the dominant common law rule established in cases like *United States v. Peoni* and *People v. Lauria*, mere knowledge is insufficient for accomplice liability when selling standard goods at market rates. The prosecution must prove the supplier had a "stake in the venture" or a purposeful intent to facilitate the offense. Because Stringer sold the chemical at standard rates and had no stake in the profits, he lacks the requisite purpose. Therefore, this option correctly applies the established legal standard to absolve Stringer.
(d) Argument-for: A student might argue that the law cannot criminalize the ordinary stream of commerce for standard, dual-use products without creating boundless liability. They could reason that because Acetone-FX is perfectly legal to sell, holding a merchant liable for its subsequent misuse is beyond the scope of criminal law. Based on this policy concern, a student could conclude that it is "legally impossible" to charge a merchant as an accomplice under these specific circumstances.
(e) Argument-for: Under the strictest traditional common law categorizations, a "principal in the second degree" required actual or constructive presence at the scene of the crime. A student might confuse the general umbrella term "accomplice" with this highly specific historical category. By mistakenly applying the requirements of a principal in the second degree, the student could argue that without physical presence, Stringer cannot be held liable as an accomplice.

Head-to-head: Option (c) is the correct application of the traditional common law rule regarding merchants selling dual-use goods. Option (a) incorrectly states that knowledge "inherently satisfies" the mens rea. Option (d) relies on the absolute falsity that it is "legally impossible" to be an accomplice with legal goods. Option (e) relies on the absolute falsity that physical presence is "stringently require[d]." However, Option (b) argues for liability based merely on the commission of an overt act. While concluding "Yes" is ultimately incorrect, the rationale relies on an implicit omission of the mens rea rather than an explicitly locked false claim. This violates the strict standard that distractors must contain a locked, explicit false legal proposition. 

Falsifiable claim per distractor:
- (a): "inherently satisfies the mens rea" — wrong because traditional common law requires purpose, not mere knowledge, especially for suppliers of ordinary goods.
- (b): Lacks an explicit falsifiable claim (implicit omission). It states an overt act was committed, which is factually true, but reaches a false conclusion without explicitly stating that the act *alone* is sufficient.
- (d): "making it legally impossible" — wrong because providing legal goods can definitely lead to accomplice liability if the requisite purposeful intent is present.
- (e): "stringently requires that the defendant be physically present" — wrong because accomplices (e.g., accessories before the fact) can be liable without physical presence at the scene.

Recommended fix: In (b), lock the false claim by using an absolute word to explicitly negate the mens rea requirement. Change (b) to: "Yes, because committing an overt act in furtherance of the crime automatically establishes accomplice liability, regardless of the defendant's mens rea."
-->
