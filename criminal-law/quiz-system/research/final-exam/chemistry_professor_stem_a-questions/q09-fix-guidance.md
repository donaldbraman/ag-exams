# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** The prosecution charges Chloe with conspiracy to distribute Compound Y. Which of the following best supports Chloe's conviction for conspiracy?

(a) Her mere presence at the scene when Arthur handed the drugs to Marcus, which implies her tacit consent to the sale.
(b) Her subjective knowledge that Arthur intended to manufacture and distribute a controlled substance, regardless of her actual involvement.
(c) Her agreement to split the profits, combined with her overt acts of acquiring the van and arranging buyer meetings. <!-- correct -->
(d) Her failure to report Arthur's illegal manufacturing operation to law enforcement, which constitutes passive participation in the crime.
(e) Her status as Arthur's former student and ongoing associate, which creates a legal presumption of an ongoing criminal enterprise.

**Answer:** (c)

**Explanation:** Conspiracy requires an agreement to commit a crime and, in most jurisdictions, an overt act in furtherance of the agreement. Chloe's agreement to split profits satisfies the agreement element, and acquiring the van and arranging meetings satisfy the overt act requirement. (a) is wrong because mere presence is legally insufficient to establish a conspiracy. (b) is wrong because mere knowledge without an agreement to participate or further the objective is insufficient. (d) is wrong because failure to report a crime does not constitute an agreement to commit it. (e) is wrong because prior relationships do not create legal presumptions of criminal conspiracy.

**Tags:** chapters: [19], topics: [conspiracy, agreement, overt act], difficulty: easy, cognitive: application

**Grounding:** conspiracy-agreement

<!-- audit: SHOULD FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: FAIL. The stem lacks a fact pattern. The options refer to "Arthur," "Marcus," "the scene," and "the van," indicating this is an orphan question that was separated from a shared fact scenario. 
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Incorporate the missing factual context directly into the stem (e.g., "Chloe was present when Arthur handed Compound Y to Marcus. She had previously acquired the van used for the sale, arranged buyer meetings, and agreed to split the profits with Arthur. The prosecution charges...").
-->
