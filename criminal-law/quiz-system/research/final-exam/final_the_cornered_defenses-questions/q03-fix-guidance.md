# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q3.** Assume the Clerk is charged as an accomplice to the warehouse arson. Will this charge succeed?

(a) Guilty, because he provided the necessary instrumentalities for the arson while harboring a strong suspicion that they would be used for a criminal objective.
(b) Guilty, because commercial vendors have an affirmative legal duty to refuse sales when they suspect the materials will be used to unlawfully destroy property.
(c) Not guilty, because his failure to report the suspicious sale to authorities constituted a legally blameless omission rather than an affirmative act of aiding.
(d) Not guilty, because selling standard goods at market price with mere knowledge or suspicion of illicit use does not establish the purpose to facilitate crime. <!-- correct -->
(e) Guilty, because the sale of explosive precursors automatically triggers strict accomplice liability under the public welfare doctrine regardless of the vendor's actual subjective intent.

**Answer:** (d)

**Explanation:** (d) is correct. Selling standard goods at market price with mere knowledge or suspicion of their illicit use does not satisfy the "purpose" mens rea requirement for accomplice liability (the *Lauria* rule). (a) is wrong because mere suspicion or knowledge is insufficient for standard commercial transactions; the clerk must have a stake in the venture or overcharge to show purpose. (b) is wrong because criminal law generally imposes no affirmative duty on merchants to police their customers absent a specific statute. (c) is wrong because while it correctly identifies the lack of an affirmative act, it misidentifies the core doctrinal failure, which is mens rea (purpose), not actus reus. (e) is wrong because accomplice liability is not strict liability; it requires the specific intent to facilitate the crime.

**Tags:** chapters: [18], topics: [accomplice-liability, purpose-vs-knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18; Lauria rule requiring purpose rather than mere knowledge for merchant liability

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might recall the *Lauria* dicta suggesting that for severe crimes, the mens rea for complicity could potentially be satisfied by knowledge alone. Since arson is a dangerous felony, a student could argue that providing the necessary tools while harboring a strong suspicion crosses the threshold into complicity, making the merchant guilty for facilitating a serious offense.
(b) Argument-for: A student could believe that in modern criminal law, commercial vendors dealing in dangerous or explosive materials operate under a public welfare or special relationship duty. If such a duty existed, the failure to refuse a sale when suspecting illicit property destruction would breach an affirmative legal duty, establishing liability.
(c) Argument-for: A student might focus on the actus reus requirement, recalling that a mere omission (like failing to report a crime) generally cannot form the basis of accomplice liability absent a special duty. By framing the clerk’s involvement purely as a failure to call the authorities, the student could conclude he is not guilty because his conduct was legally a blameless omission.
(d) Argument-for: This directly applies the *Lauria* standard for merchant accomplice liability. Selling standard goods at market price with mere knowledge or suspicion does not establish the requisite "purpose" to facilitate the crime. Without an overcharge, lack of legitimate use, or stake in the venture, the merchant lacks the specific intent required for complicity.
(e) Argument-for: A student familiar with the "public welfare offense" doctrine might confuse its strict liability application for primary offenses (like selling regulated goods) with accomplice liability. They could argue that because explosive precursors are heavily regulated, any sale contributing to an explosion automatically triggers strict accomplice liability, bypassing the mens rea requirement entirely.

Head-to-head:
Option (d) is the unequivocally correct application of the *Lauria* rule, requiring "purpose" for commercial transactions. Option (a) is incorrect because "strong suspicion" does not satisfy the mens rea for complicity, but it lacks absolute language to lock the falsifiable rule. Option (b) explicitly but falsely invents an "affirmative legal duty" for merchants to refuse sales based on mere suspicion. Option (c) relies on an implicit omission by focusing solely on the failure to report while ignoring the affirmative act of the sale, failing the close-call standard. Option (e) explicitly asserts an incorrect legal rule by applying strict liability ("automatically triggers") to complicity via the public welfare doctrine.

Falsifiable claim per distractor:
- (a): "Guilty, because he provided the necessary instrumentalities... while harboring a strong suspicion" — wrong because it implies suspicion is legally sufficient for accomplice liability, which violates the *Lauria* purpose requirement.
- (b): "commercial vendors have an affirmative legal duty to refuse sales when they suspect..." — wrong because no such categorical affirmative duty exists.
- (c): "failure to report... constituted a legally blameless omission rather than an affirmative act" — wrong because it ignores the affirmative act of the sale, making its error an implicit factual omission rather than an explicitly false legal claim.
- (e): "automatically triggers strict accomplice liability... regardless of... actual subjective intent" — wrong because accomplice liability requires mens rea and cannot be strict liability.

Recommended fix: Add absolute words to (a) and (c) to lock their false legal propositions. For (a): "Guilty, because providing necessary instrumentalities with a strong suspicion of a criminal objective automatically satisfies the mens rea for accomplice liability." For (c): "Not guilty, solely because completing a commercial transaction is categorically treated as a legally blameless omission rather than an affirmative act of aiding."
-->

## Issue 3 — argpass-opus

**Q3.** Assume the Clerk is charged as an accomplice to the warehouse arson. Will this charge succeed?

(a) Guilty, because he provided the necessary instrumentalities for the arson while harboring a strong suspicion that they would be used for a criminal objective.
(b) Guilty, because commercial vendors have an affirmative legal duty to refuse sales when they suspect the materials will be used to unlawfully destroy property.
(c) Not guilty, because his failure to report the suspicious sale to authorities constituted a legally blameless omission rather than an affirmative act of aiding.
(d) Not guilty, because selling standard goods at market price with mere knowledge or suspicion of illicit use does not establish the purpose to facilitate crime. <!-- correct -->
(e) Guilty, because the sale of explosive precursors automatically triggers strict accomplice liability under the public welfare doctrine regardless of the vendor's actual subjective intent.

**Answer:** (d)

**Explanation:** (d) is correct. Selling standard goods at market price with mere knowledge or suspicion of their illicit use does not satisfy the "purpose" mens rea requirement for accomplice liability (the *Lauria* rule). (a) is wrong because mere suspicion or knowledge is insufficient for standard commercial transactions; the clerk must have a stake in the venture or overcharge to show purpose. (b) is wrong because criminal law generally imposes no affirmative duty on merchants to police their customers absent a specific statute. (c) is wrong because while it correctly identifies the lack of an affirmative act, it misidentifies the core doctrinal failure, which is mens rea (purpose), not actus reus. (e) is wrong because accomplice liability is not strict liability; it requires the specific intent to facilitate the crime.

**Tags:** chapters: [18], topics: [accomplice-liability, purpose-vs-knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18; Lauria rule requiring purpose rather than mere knowledge for merchant liability

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that providing instrumentalities completes the actus reus of aiding, and that a "strong suspicion" satisfies the mens rea for serious crimes, drawing on exceptions (like the *Fountain* rule) where knowledge suffices for major felonies.
(b) Argument-for: A student might conflate civil tort duties with criminal omission liability, arguing that vendors dealing in dangerous goods have a special relationship or public duty to prevent harm, making their failure to refuse the sale a culpable omission.
(c) Argument-for: A student could correctly recall that failing to report a crime is generally a blameless omission rather than an affirmative act of aiding. By mistakenly isolating this post-sale omission and ignoring the sale itself, they would conclude the clerk is legally blameless.
(d) Argument-for: This applies the core *Lauria* rule: a merchant selling standard goods at market prices must have a "purpose" to facilitate the crime (e.g., a stake in the venture or overcharging). Mere knowledge or suspicion of illicit use is legally insufficient.
(e) Argument-for: A student might incorrectly extend the public welfare offense doctrine—which allows strict liability for regulatory crimes involving dangerous materials—into the accomplice liability framework, arguing that explosive precursors bypass normal mens rea requirements.

Head-to-head: Option (d) is the clear, correct application of the *Lauria* doctrine. Option (e) explicitly and falsely applies strict liability to the accomplice doctrine, and option (b) explicitly invents a nonexistent blanket "affirmative legal duty." However, option (a) lacks absolute words and borders on minority rules for serious felonies, failing to lock a definitively false claim. Worse, option (c) relies entirely on a legally true statement—that failing to report is a blameless omission—and only serves as a distractor by implicitly ignoring the affirmative act of the sale. Because (c) lacks an explicit false legal claim, it violates the standard against implicit omissions.

Falsifiable claim per distractor:
- (a): "harboring a strong suspicion... [leads to guilt]" — lacks absolute locking words and is debatable under minority rules for serious crimes.
- (b): "commercial vendors have an affirmative legal duty to refuse sales" — wrong because criminal law generally imposes no such duty absent a specific statute.
- (c): NONE — "failure to report... constituted a legally blameless omission" is a legally true statement; the option incorrectly assumes this omission is the only basis for liability, relying on an implicit omission of the sale itself.
- (e): "automatically triggers strict accomplice liability... regardless of the vendor's actual subjective intent" — explicitly wrong because accomplice liability requires specific intent/purpose, not strict liability.

Recommended fix: Edit (a) to lock the false rule: "Guilty, solely because providing standard instrumentalities with a strong suspicion of criminal use categorically satisfies the mens rea for accomplice liability." Edit (c) to include an explicit false claim about the actus reus: "Not guilty, because completing a commercial sale categorically cannot constitute the affirmative act of aiding required for accomplice liability."
-->
