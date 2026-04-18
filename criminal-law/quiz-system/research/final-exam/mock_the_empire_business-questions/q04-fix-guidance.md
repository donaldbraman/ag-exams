# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Assuming 18 U.S.C. § 922(g) requires the defendant to "knowingly" possess a firearm while having the status of a convicted felon, is Locke guilty of being a felon in possession?

(a) No, because Locke genuinely believed his conviction was a misdemeanor, which negates the required knowledge of his prohibited status. <!-- correct -->
(b) Yes, because ignorance of the law is never an excuse, so Locke's mistaken belief regarding his felony status is entirely legally irrelevant.
(c) Yes, because Locke knew he possessed the 9mm handgun, which satisfies the entire mens rea requirement for the federal firearms statute.
(d) No, because Locke's reliance on a probation officer triggers the Cheek exception, which applies to all federal criminal statutes.
(e) Yes, because the mistake of law defense only applies if the defendant formally consults a licensed attorney, rather than a state probation officer.

**Answer:** (a)

**Explanation:** Under *Rehaif v. United States*, the word "knowingly" in § 922(g) applies to both the possession of the firearm and the defendant's prohibited status. Locke's genuine belief that he was a misdemeanant negates his knowledge of his felony status. (b) is wrong because *Rehaif* created a specific statutory exception to the "ignorance of the law" maxim for the status element in this statute. (c) is wrong because knowing possession of the firearm is only half the mens rea requirement; the government must also prove knowledge of status. (d) is wrong because the *Cheek* exception (requiring a known legal duty) applies specifically to the word "willfully" in tax offenses, not to all federal statutes. (e) is wrong because *Rehaif* focuses on whether the defendant actually knew their status as a factual matter, not whether they met the requirements for an "advice of counsel" defense.

**Tags:** chapters: [10, 15], topics: [mistake of law, Rehaif, felon in possession], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 10 - Rehaif v. United States (Scienter for Status Elements)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: FAIL. The stem completely lacks a fact pattern. There is no information about Locke, his prior conviction, his possession of a 9mm handgun, his interaction with a probation officer, or his belief about his criminal record. All of these necessary facts appear out of nowhere in the answer options.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Add a short fact pattern to the stem. For example: "Locke previously pleaded guilty to a state offense. His state probation officer incorrectly told him the conviction was a misdemeanor. Locke later bought a 9mm handgun. Assuming 18 U.S.C. § 922(g)..."
-->
