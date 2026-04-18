# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q11.** After the trial, Sal files a civil lawsuit for damages against DA Paula under 42 U.S.C. § 1983. He alleges that her instruction to the police evidence custodian to destroy the dashcam footage during trial preparation violated his constitutional rights. Will Paula's claim of absolute civil immunity succeed?

(a) Yes, because absolute immunity shields prosecutors from civil liability for acts intimately associated with the judicial phase, including instructing the destruction of evidence. <!-- correct -->
(b) Yes, because prosecutors are protected by qualified immunity whenever their actions are tangentially related to a pending criminal investigation or administrative duty.
(c) No, because absolute immunity is immediately forfeited when a prosecutor engages in conduct that fundamentally violates established state bar professional ethics rules.
(d) No, because ordering the destruction of evidence is considered an investigative police function, limiting her protection exclusively to standard qualified immunity.
(e) No, because absolute immunity applies solely to statements made in open court and does not extend to pretrial evidentiary preparation or management.

**Answer:** (a)

**Explanation:** Under *Price v. Montgomery County* and *Imbler v. Pachtman*, prosecutors possess absolute civil immunity for conduct intimately associated with the judicial phase of the criminal process. This immunity applies even to ethically reprehensible acts like instructing the destruction of evidence during trial preparation. (b) is wrong because prosecutors receive absolute immunity, not merely qualified immunity, for acts tied to the judicial phase. (c) fails because absolute immunity cannot be forfeited by violating state bar ethics rules; the protection covers the function, regardless of misconduct. (d) is incorrect because managing evidence during trial preparation is considered a judicial phase function, not a mere investigative police act. (e) is wrong because absolute immunity extends to trial preparation and out-of-court conduct directly tied to the judicial process.

**Tags:** chapters: [6], topics: [absolute-immunity-scope], difficulty: medium, cognitive: application

**Grounding:** Chapter 6 (Prosecutors) - Price v. Montgomery County

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: MUST FIX. The question relies on the premise that a prosecutor's "instruction to destroy evidence" is protected by absolute immunity. However, under established § 1983 jurisprudence (e.g., *Yarris v. County of Delaware*, 465 F.3d 129), while *withholding* exculpatory evidence (a *Brady* violation) is protected by absolute immunity as an advocacy function, the physical *destruction* of evidence is almost universally classified as an administrative or investigatory act that receives only qualified immunity. This makes the intended answer (a) legally incorrect and inadvertently makes (d) the correct legal conclusion.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change DA Paula's action in the facts and the question from "instructing the destruction of evidence" to "intentionally withholding the exculpatory dashcam footage from the defense during trial." Update options (a) and (d), and the explanation, to reflect that *withholding* evidence falls squarely under the advocacy function protected by *Imbler*.
-->
