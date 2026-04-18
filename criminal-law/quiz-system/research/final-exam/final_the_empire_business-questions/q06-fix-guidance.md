# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** Assume Dominic is charged with possession of fentanyl with intent to distribute. How does his genuine belief that the substance was heroin affect his liability?

(a) Guilty of fentanyl possession, because the government only needs to prove he knew the substance was a controlled substance, not its precise chemical identity or type. <!-- correct -->
(b) Not guilty of fentanyl possession, because a genuine mistake of fact regarding the specific identity of the drug completely negates the required mens rea for that element.
(c) Guilty of fentanyl possession, because drug trafficking is a strict liability offense where the defendant bears the full legal risk of any adulteration in the drug supply.
(d) Not guilty of fentanyl possession, because he can only be held liable for attempting to possess heroin, which was his actual specific intent during the transaction.
(e) Guilty of fentanyl possession, because his failure to chemically test the narcotics constitutes gross criminal negligence regarding the true dangerous nature of the illicit substance.

**Answer:** (a)

**Explanation:** Under McFadden v. United States, the mens rea for drug possession is satisfied if the defendant knew the substance was a controlled substance (its general nature). Dominic knew he was trading illegal drugs, so his mistaken belief that it was heroin rather than fentanyl is no defense to fentanyl possession. (b) is incorrect because the government need not prove knowledge of the specific chemical identity, only its general illicit nature. (c) is incorrect because drug possession is not a pure strict liability offense; it requires knowledge of the substance's general nature, even though it imposes strict liability as to the exact type. (d) is incorrect because the general-nature rule allows conviction for the actual substance possessed, not just the one intended. (e) is incorrect because the standard is actual knowledge of illicit nature, not a negligence standard for failing to test.

**Tags:** chapters: [10, 15], topics: [mens rea, drug type, McFadden, fentanyl substitution], difficulty: medium, cognitive: application

**Grounding:** McFadden v. United States; Fentanyl substitution problem

<!-- audit: MUST FIX
Check 1: pass (accurately reflects the federal McFadden rule).
Check 2: A prepared student could successfully argue for (b) or (d) by applying Chapter 10's MPC element-matching rules (`mof-element-matching`). If the crime is literally titled "possession of fentanyl" (as the stem and options state), default statutory interpretation dictates that "knowingly" applies to the material element of "fentanyl." A genuine belief it was heroin would negate that specific mens rea.
Check 3: pass
Check 4: The stem lacks the specific statutory text needed to rule out a standard Chapter 10 element-matching argument. 
Check 5: Fails. The explanation relies on the specific statutory structure of the federal Controlled Substances Act (interpreted in *McFadden*), where the base element is simply "a controlled substance" rather than the specific drug. The stem does not specify the federal jurisdiction or provide this critical statutory wording, improperly relying on students to assume the federal statutory structure. 
Check 6: pass
Check 7: pass
Recommended fix: Modify the stem to explicitly provide the statutory structure so students aren't tricked by default MPC rules. E.g., "Assume Dominic is charged under a jurisdiction's drug statute that criminalizes 'knowingly possessing a controlled substance,' with enhanced penalties if the substance is fentanyl. How does his genuine belief..." Also, change the options from "Guilty of fentanyl possession" to "Guilty of the charged offense" or "Liable for the fentanyl enhancement."
-->
