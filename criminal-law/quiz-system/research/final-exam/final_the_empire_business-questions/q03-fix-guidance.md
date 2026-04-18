# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** The U.S. Attorney wants to know if Marcus is liable as an accomplice for the underlying drug distribution. Is Marcus guilty of accomplice liability?

(a) Guilty of accomplice liability, because Marcus knew his routing would facilitate the distribution of narcotics and performed an act that materially aided the principal's crime.
(b) Not guilty of accomplice liability, because Marcus lacked the conscious object or purpose to see the underlying drug trafficking offense successfully completed by the principals. <!-- correct -->
(c) Guilty of accomplice liability, because receiving his regular salary constitutes a financial stake that elevates his knowledge to a true purposeful intent under the law.
(d) Not guilty of accomplice liability, because routing trucks around weigh stations is part of his normal job and therefore cannot constitute a culpable actus reus.
(e) Guilty of accomplice liability, because the model penal code only requires a showing of extreme recklessness when the underlying crime involves highly dangerous controlled substances.

**Answer:** (b)

**Explanation:** Under the traditional rule for accomplice liability, a defendant must have the specific purpose (conscious object) to promote or facilitate the underlying offense. Because Marcus explicitly stated he only wanted his regular salary and had no stake in the drug money, he possessed mere knowledge, not the required purpose. (a) is incorrect because mere knowledge that one's actions will aid a crime is insufficient for accomplice liability in most jurisdictions. (c) is incorrect because receiving a standard, pre-existing salary for normal duties does not constitute a specialized financial stake in the success of the illicit venture. (d) is incorrect because routing trucks is an affirmative act, not an omission. (e) is incorrect because the MPC strictly requires the purpose to promote or facilitate the offense, not recklessness, for accomplice liability.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Accomplice mens rea; Purpose requirement

<!-- audit: MUST FIX
1: pass
2: pass
3: pass
4: FAILS - The entire fact pattern is missing from the question. The stem begins with the call of the question about "Marcus" without providing any facts about who Marcus is, what he did, or his mental state.
5: pass
6: pass
7: pass
Recommended fix: Add the missing fact pattern to the stem, detailing Marcus's actions (routing trucks) and his statements regarding his regular salary and knowledge of the drug distribution.
-->

## Issue 2 — edge-case

**Q3.** The U.S. Attorney wants to know if Marcus is liable as an accomplice for the underlying drug distribution. Is Marcus guilty of accomplice liability?

(a) Guilty of accomplice liability, because Marcus knew his routing would facilitate the distribution of narcotics and performed an act that materially aided the principal's crime.
(b) Not guilty of accomplice liability, because Marcus lacked the conscious object or purpose to see the underlying drug trafficking offense successfully completed by the principals. <!-- correct -->
(c) Guilty of accomplice liability, because receiving his regular salary constitutes a financial stake that elevates his knowledge to a true purposeful intent under the law.
(d) Not guilty of accomplice liability, because routing trucks around weigh stations is part of his normal job and therefore cannot constitute a culpable actus reus.
(e) Guilty of accomplice liability, because the model penal code only requires a showing of extreme recklessness when the underlying crime involves highly dangerous controlled substances.

**Answer:** (b)

**Explanation:** Under the traditional rule for accomplice liability, a defendant must have the specific purpose (conscious object) to promote or facilitate the underlying offense. Because Marcus explicitly stated he only wanted his regular salary and had no stake in the drug money, he possessed mere knowledge, not the required purpose. (a) is incorrect because mere knowledge that one's actions will aid a crime is insufficient for accomplice liability in most jurisdictions. (c) is incorrect because receiving a standard, pre-existing salary for normal duties does not constitute a specialized financial stake in the success of the illicit venture. (d) is incorrect because routing trucks is an affirmative act, not an omission. (e) is incorrect because the MPC strictly requires the purpose to promote or facilitate the offense, not recklessness, for accomplice liability.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Accomplice mens rea; Purpose requirement

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The fact that Marcus routed the trucks *around state weigh stations* triggers the "tailoring of services" exception for inferring purpose (often taught via *People v. Lauria*). While Marcus lacks a direct financial stake, his affirmative act of altering his service specifically to conceal the criminal activity allows a jury to infer purpose. Furthermore, under federal law (which the "U.S. Attorney" prompt implies), *Rosemond v. United States* holds that active participation with advance knowledge of the crime establishes the requisite intent. This makes (a) a highly defensible—if not the correct—answer in this context.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Q3 structurally spoils Q4. If students learn in Q3 that Marcus is categorically "Not guilty" because a regular salary precludes the mens rea of purpose, he remains completely innocent for the subsequent four months of routing. This renders the duress defense tested in Q4 legally moot, as an affirmative defense is unnecessary if the defendant never met the prima facie mens rea elements of the crime.
Recommended fix: To resolve the booby trap, amend the question stem to clarify the jurisdiction (e.g., "Applying the strict Model Penal Code standard..."). To fix the Q4 spoiler, ensure Q4's future stem begins with: "Assume for the purposes of this question that Marcus's actions satisfy the prima facie elements of accomplice liability..."
-->

## Issue 3 — argpass-sonnet

**Q3.** The U.S. Attorney wants to know if Marcus is liable as an accomplice for the underlying drug distribution. Is Marcus guilty of accomplice liability?

(a) Guilty of accomplice liability, because Marcus knew his routing would facilitate the distribution of narcotics and performed an act that materially aided the principal's crime.
(b) Not guilty of accomplice liability, because Marcus lacked the conscious object or purpose to see the underlying drug trafficking offense successfully completed by the principals. <!-- correct -->
(c) Guilty of accomplice liability, because receiving his regular salary constitutes a financial stake that elevates his knowledge to a true purposeful intent under the law.
(d) Not guilty of accomplice liability, because routing trucks around weigh stations is part of his normal job and therefore cannot constitute a culpable actus reus.
(e) Guilty of accomplice liability, because the model penal code only requires a showing of extreme recklessness when the underlying crime involves highly dangerous controlled substances.

**Answer:** (b)

**Explanation:** Under the traditional rule for accomplice liability, a defendant must have the specific purpose (conscious object) to promote or facilitate the underlying offense. Because Marcus explicitly stated he only wanted his regular salary and had no stake in the drug money, he possessed mere knowledge, not the required purpose. (a) is incorrect because mere knowledge that one's actions will aid a crime is insufficient for accomplice liability in most jurisdictions. (c) is incorrect because receiving a standard, pre-existing salary for normal duties does not constitute a specialized financial stake in the success of the illicit venture. (d) is incorrect because routing trucks is an affirmative act, not an omission. (e) is incorrect because the MPC strictly requires the purpose to promote or facilitate the offense, not recklessness, for accomplice liability.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Accomplice mens rea; Purpose requirement

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that under certain common law precedents (e.g., the serious-felony exception in *People v. Lauria* or the standard applied in *Backun*), mere knowledge that one's actions will materially assist a serious offense like drug distribution is legally sufficient to establish the mens rea for accomplice liability. Since the question does not specify a jurisdiction or limit the analysis to the majority purpose standard, the facts legally support a guilty verdict under the minority rule.
(b) Argument-for: A student could argue that under both the Model Penal Code and the traditional majority common-law rule, an accomplice must act with the conscious object or specific purpose to promote or facilitate the crime. Because Marcus only wanted his regular salary and had no stake in the venture, his mere knowledge does not rise to the required purpose, rendering him not guilty.
(c) Argument-for: A student might recall that under *Lauria*, a financial stake in an illicit venture can elevate mere knowledge to purpose. They could argue that because Marcus is receiving a salary for work that he knows involves routing around weigh stations to shield drugs, his continued employment effectively constitutes a "financial stake" that satisfies the elevated mens rea standard.
(d) Argument-for: A student could argue that the actus reus of a crime generally must involve inherently wrongful conduct. Because routing trucks is Marcus's standard, legitimate job duty, performing his everyday employment obligations cannot be classified as a culpable affirmative act for the purposes of criminal complicity. 
(e) Argument-for: A student could argue that while the Model Penal Code typically requires purpose, there is a sliding scale for mens rea when extreme public dangers are involved. They might falsely recall an MPC carve-out where highly dangerous crimes (like distributing large quantities of controlled substances) lower the complicity threshold to extreme recklessness.

Head-to-head:
Option (b) correctly applies the majority common law and MPC standard that accomplice liability requires the specific purpose to promote or facilitate the offense. Option (c) relies on a falsifiable claim about what legally constitutes a financial stake under *Lauria*. Option (d) contains a falsifiable claim about actus reus, wrongly asserting that everyday job duties cannot constitute an actus reus. Option (e) is readily falsifiable because the MPC does not contain an "extreme recklessness" exception for controlled substances in its complicity statute. Option (a), however, relies entirely on the minority/alternative standard (where knowledge + material aid suffices for serious felonies). Because the prompt does not specify the jurisdiction and the option does not contain absolute language (e.g., "in every jurisdiction"), (a) technically contains a legally true statement under minority common law, lacking a clear falsifiable error. 

Falsifiable claim per distractor:
- (a): None. Option (a) asserts liability based on knowledge and material aid. This is a valid minority rule (e.g., for serious felonies) and the option lacks absolute modifiers (like "categorically" or "always") to render it explicitly false across the board.
- (c): "...receiving his regular salary constitutes a financial stake that elevates his knowledge to a true purposeful intent under the law." — wrong because receiving a standard, pre-existing salary for ordinary duties does not legally constitute the kind of specialized financial stake (like a premium or percentage of illicit profits) required to elevate knowledge to purpose.
- (d): "...and therefore cannot constitute a culpable actus reus." — wrong because otherwise lawful, everyday job duties absolutely can constitute an actus reus for complicity if performed with the requisite mens rea.
- (e): "...because the model penal code only requires a showing of extreme recklessness when the underlying crime involves highly dangerous controlled substances." — wrong because the MPC complicity provisions strictly require the purpose of promoting or facilitating the offense and do not lower the standard to recklessness specifically for dangerous controlled substances.

Recommended fix: Edit (a) to include a categorically false legal claim. For example: "(a) Guilty of accomplice liability, because under the traditional common-law rule, mere knowledge that an act will facilitate a crime is categorically sufficient for accomplice liability in every jurisdiction." Alternatively, add "Under the majority rule..." to the question stem.
-->

## Issue 4 — argpass-opus

**Q3.** The U.S. Attorney wants to know if Marcus is liable as an accomplice for the underlying drug distribution. Is Marcus guilty of accomplice liability?

(a) Guilty of accomplice liability, because Marcus knew his routing would facilitate the distribution of narcotics and performed an act that materially aided the principal's crime.
(b) Not guilty of accomplice liability, because Marcus lacked the conscious object or purpose to see the underlying drug trafficking offense successfully completed by the principals. <!-- correct -->
(c) Guilty of accomplice liability, because receiving his regular salary constitutes a financial stake that elevates his knowledge to a true purposeful intent under the law.
(d) Not guilty of accomplice liability, because routing trucks around weigh stations is part of his normal job and therefore cannot constitute a culpable actus reus.
(e) Guilty of accomplice liability, because the model penal code only requires a showing of extreme recklessness when the underlying crime involves highly dangerous controlled substances.

**Answer:** (b)

**Explanation:** Under the traditional rule for accomplice liability, a defendant must have the specific purpose (conscious object) to promote or facilitate the underlying offense. Because Marcus explicitly stated he only wanted his regular salary and had no stake in the drug money, he possessed mere knowledge, not the required purpose. (a) is incorrect because mere knowledge that one's actions will aid a crime is insufficient for accomplice liability in most jurisdictions. (c) is incorrect because receiving a standard, pre-existing salary for normal duties does not constitute a specialized financial stake in the success of the illicit venture. (d) is incorrect because routing trucks is an affirmative act, not an omission. (e) is incorrect because the MPC strictly requires the purpose to promote or facilitate the offense, not recklessness, for accomplice liability.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Accomplice mens rea; Purpose requirement

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that Marcus is guilty under the knowledge standard used in a minority of jurisdictions. Some courts have held that providing material assistance with knowledge of the criminal nature of the enterprise is sufficient for accomplice liability, particularly for serious crimes. The option accurately states the factual premise—Marcus had knowledge and materially aided the crime—which would arguably satisfy the elements of accomplice liability in those specific jurisdictions.
(b) Argument-for: This option perfectly captures the traditional specific intent standard for accomplice liability, as established in cases like *United States v. Peoni* and adopted by the Model Penal Code. To be an accomplice, the defendant must act with the "conscious object" or purpose to promote or facilitate the underlying offense. Because Marcus merely wanted his regular salary and lacked the conscious object to see the drug trafficking succeed, he lacked the requisite purpose, making this the correct legal conclusion.
(c) Argument-for: A student might select this option by attempting to apply the *People v. Lauria* standard, which allows an inference of purposeful intent from mere knowledge if the defendant has a "stake in the venture." The student could argue that because Marcus receives his livelihood from an operation engaged in illicit activities, his continued salary operates as a financial stake that legally elevates his knowledge to purposeful intent.
(d) Argument-for: A student could defend this option by arguing that the actus reus for accomplice liability requires conduct outside one's ordinary, innocent employment duties. Because routing trucks is his standard job description, a student might assert that performing a routine employment obligation is legally insufficient to constitute a culpable affirmative act.
(e) Argument-for: A student might argue this by conflating the *Lauria* dictum—that intent might be inferred from knowledge for inherently dangerous felonies—with the Model Penal Code's specific mens rea standards. The student could incorrectly recall that the MPC expressly lowers the mens rea requirement to extreme recklessness when the underlying offense involves highly dangerous controlled substances.

Head-to-head: Option (b) is the strongest because it correctly identifies the prevailing federal and majority rule requiring purposeful intent (conscious object) for accomplice liability, which appropriately answers the "U.S. Attorney" prompt. Option (c) fails because it legally mischaracterizes a regular salary as a "stake in the venture." Option (d) invents a false categorical rule that ordinary job duties cannot satisfy the actus reus requirement. Option (e) relies on an explicitly fabricated MPC rule regarding extreme recklessness. However, Option (a) presents a slight issue: while it is incorrect under the federal/majority rule, it merely states that Marcus is guilty because he knew his routing would facilitate the crime and aided it. Because it lacks absolute phrasing to lock in a universal legal falsehood, it could be argued as factually accurate in jurisdictions that apply a minority knowledge standard. The keyed answer (b) is clearly best, but (a) needs a falsifiable claim to pass the close-call standard.

Falsifiable claim per distractor:
- (a): Lacks a clearly falsifiable legal claim. It merely states a factual application ("because Marcus knew... and performed an act") that is legally sufficient in a minority of jurisdictions. It needs absolute wording to be demonstrably false.
- (c): "receiving his regular salary constitutes a financial stake that elevates his knowledge to a true purposeful intent under the law" — wrong because under *Lauria*, a normal salary or standard pricing explicitly does not constitute a "stake in the venture."
- (d): "is part of his normal job and therefore cannot constitute a culpable actus reus" — wrong because ordinary job duties absolutely can constitute the actus reus for accomplice liability if performed with the requisite mens rea.
- (e): "the model penal code only requires a showing of extreme recklessness when the underlying crime involves highly dangerous controlled substances" — wrong because the MPC categorically requires purpose to promote or facilitate the offense, not extreme recklessness.

Recommended fix: Edit (a) to include an absolute falsifiable claim. For example: "(a) Guilty of accomplice liability, because knowledge that one's actions will facilitate a crime is categorically sufficient to establish accomplice mens rea regardless of the jurisdiction."
-->
