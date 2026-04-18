# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q2.** Assume Dan is charged as an accomplice to the drug manufacturing. Dan argues that he explicitly disclaimed any share of the profits and only wanted his invoice paid. Which of the following best states whether Dan satisfies the mens rea for accomplice liability?

(a) He does not satisfy the mens rea because his explicit disclaimer proves he lacked the specific knowledge of Albert's criminal intent required for liability.
(b) He does not satisfy the mens rea because an accomplice must actively participate in the physical actus reus of the principal offense to be held liable.
(c) He satisfies the mens rea because mere knowledge of another's criminal intent is always sufficient to establish the purpose required for accomplice liability at common law.
(d) He satisfies the mens rea because his 500% markup allows a jury to infer he had the purpose to facilitate the crime by taking a financial stake in it. <!-- correct -->
(e) He satisfies the mens rea because chemical suppliers are held to a strict liability standard when selling regulated precursors to unlicensed buyers in criminal conspiracies.

**Answer:** (d)

**Explanation:** Under *Lauria*, a supplier who knows of the buyer's illicit purpose can be found to have the purpose to facilitate the crime if they take a financial stake in the venture, such as by charging a grossly inflated price. Dan's 500% markup allows a jury to infer this purpose despite his verbal disclaimer. (a) is incorrect because the disclaimer does not automatically override the inference drawn from the inflated price. (b) is incorrect because an accomplice need only aid or encourage the principal; physical participation in the actus reus is not required. (c) is incorrect because mere knowledge is generally insufficient for accomplice liability without a showing of purpose. (e) is incorrect because accomplice liability requires specific mens rea, not strict liability.

**Tags:** chapters: [18, 19], topics: [accomplice liability, mr-purpose-not-knowledge, Lauria], difficulty: medium, cognitive: application

**Grounding:** Chapter 18, Accomplice Liability — mr-purpose-not-knowledge; Chapter 19, Conspiracy — Lauria

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fail. The stem lacks the critical fact that Dan charged a "500% markup" (and that he was a chemical supplier). While this question was likely divorced from a shared master fact pattern, as a standalone question, option (d) introduces extrinsic facts not in evidence. 
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Import the missing facts directly into the stem. For example: "Assume Dan, a chemical supplier, sold regulated precursors to the operation at a 500% markup. Dan is charged as an accomplice to the drug manufacturing. Dan argues..."
-->
