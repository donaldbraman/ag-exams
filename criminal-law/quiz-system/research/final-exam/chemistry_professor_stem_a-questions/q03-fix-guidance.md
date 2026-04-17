# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — edge-case

**Q3.** Assume Arthur is charged with criminal homicide based specifically on his omission (failing to call 911 and preventing rescue). He claims he owed no legal duty to aid Julian. Which theory best establishes Arthur's duty to act?

(a) He had a duty based on a special relationship, because the seller-buyer dynamic imposes fiduciary obligations of care under the common law.
(b) He had a duty based on a contractual agreement, because the implied terms of a drug transaction include emergency medical support.
(c) He had a duty based on creation of peril and seclusion, because he provided the dangerous substance and then isolated Julian to prevent others from rendering aid. <!-- correct -->
(d) He had a duty based on a statutory mandate, because all jurisdictions have Good Samaritan laws requiring bystanders to summon medical assistance for overdose victims.
(e) He had no legal duty to act, because Julian's overdose was self-induced and Arthur did not force him to consume the substance.

**Answer:** (c)

**Explanation:** Arthur falls under two recognized categories of legal duty: the creation of peril (providing the lethal substance) and voluntary assumption of care combined with seclusion (taking charge by locking Julian in a room with no phone, preventing others from helping). (a) is wrong because a commercial buyer-seller relationship does not qualify as a traditional status relationship (like parent-child) triggering an affirmative duty to rescue. (b) is wrong because illegal drug sales do not create enforceable contractual duties of care. (d) is wrong because only a few jurisdictions have general Good Samaritan duties, and the common law baseline is generally no duty to rescue. (e) is wrong because Arthur's active role in supplying the drug and secluding the victim squarely trigger exceptions to the no-duty baseline.

**Tags:** chapters: [9], topics: [omissions, legal duty, creation of peril, seclusion], difficulty: medium, cognitive: application

**Grounding:** Chapter 9, creation-of-peril-category, voluntary-assumption-plus-seclusion

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The facts establish that Silas took the two grams from Arthur's backpack (Fact 5). It is unclear from the facts whether Arthur directly provided the substance to Julian, or if Silas handled the transfer. Option (c) states Arthur "provided the dangerous substance," which might slightly clash with Silas being the one who physically took the drugs to distribute. 
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change option (c) to "because he contributed to creating the peril and then isolated Julian to prevent others from rendering aid." Make a matching adjustment in the explanation.
-->
