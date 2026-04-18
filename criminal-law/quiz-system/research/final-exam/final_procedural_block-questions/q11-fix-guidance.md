# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q11.** Assume Senator Sterling is charged with federal bribery for accepting the $25,000 and contacting the zoning official. Is he guilty of bribery?

(a) Yes, because receiving significant money from a known criminal syndicate creates an irrebuttable legal presumption of corrupt legislative intent under federal law.
(b) Yes, because a campaign donation combined with informal lobbying assistance constitutes a formal official act under the strict federal corruption statute.
(c) No, because the payment was a post-act gratuity rather than a pre-act quid pro quo, and making an informal phone call does not constitute a formal official act. <!-- correct -->
(d) No, because his zoning vote was a core legislative function protected by absolute immunity, shielding him from any criminal corruption charges whatsoever.
(e) No, because the $25,000 was explicitly characterized as a token of appreciation, which officially triggers the safe harbor provision for routine political contributions.

**Answer:** (c)

**Explanation:** The correct answer is (c). Federal bribery law has been strictly narrowed. First, under *Snyder*, a payment received *after* the vote as a "token of appreciation" is a gratuity, not a bribe, because bribery requires a pre-act quid pro quo agreement. Second, under *McDonnell*, making phone calls or informally expediting matters does not constitute a formal "official act" within the meaning of the federal corruption statutes (Fact 8).

(a) is incorrect because the source of the funds (a syndicate) does not alter the doctrinal distinction between a bribe and a gratuity under federal law.
(b) is incorrect because *McDonnell* explicitly held that informal lobbying, arranging meetings, or making phone calls falls outside the definition of an "official act."
(d) is incorrect because legislative immunity does not shield a senator from bribery charges based on corruptly selling their vote.
(e) is incorrect because characterizing cash as a "token of appreciation" does not create a safe harbor; rather, the timing indicates it is a gratuity, which falls outside the bribery statute under *Snyder*.

**Tags:** chapters: [5], topics: [corruption-bribe-vs-gratuity, corruption-official-acts-narrowing], difficulty: hard, cognitive: application

**Grounding:** Chapter 5 - Legislatures and Courts > Corruption bribe vs gratuity & Official acts narrowing

<!-- GROUNDING-FAIL: Federal bribery / bribe vs. gratuity (Snyder) / official acts (McDonnell) is not in any chapter map. The closest taught doctrines are: Legality, Vagueness, Lenity, Equal protection, and Desuetude (Ch 5). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 3 — edge-case

**Q11.** Assume Senator Sterling is charged with federal bribery for accepting the $25,000 and contacting the zoning official. Is he guilty of bribery?

(a) Yes, because receiving significant money from a known criminal syndicate creates an irrebuttable legal presumption of corrupt legislative intent under federal law.
(b) Yes, because a campaign donation combined with informal lobbying assistance constitutes a formal official act under the strict federal corruption statute.
(c) No, because the payment was a post-act gratuity rather than a pre-act quid pro quo, and making an informal phone call does not constitute a formal official act. <!-- correct -->
(d) No, because his zoning vote was a core legislative function protected by absolute immunity, shielding him from any criminal corruption charges whatsoever.
(e) No, because the $25,000 was explicitly characterized as a token of appreciation, which officially triggers the safe harbor provision for routine political contributions.

**Answer:** (c)

**Explanation:** The correct answer is (c). Federal bribery law has been strictly narrowed. First, under *Snyder*, a payment received *after* the vote as a "token of appreciation" is a gratuity, not a bribe, because bribery requires a pre-act quid pro quo agreement. Second, under *McDonnell*, making phone calls or informally expediting matters does not constitute a formal "official act" within the meaning of the federal corruption statutes (Fact 8).

(a) is incorrect because the source of the funds (a syndicate) does not alter the doctrinal distinction between a bribe and a gratuity under federal law.
(b) is incorrect because *McDonnell* explicitly held that informal lobbying, arranging meetings, or making phone calls falls outside the definition of an "official act."
(d) is incorrect because legislative immunity does not shield a senator from bribery charges based on corruptly selling their vote.
(e) is incorrect because characterizing cash as a "token of appreciation" does not create a safe harbor; rather, the timing indicates it is a gratuity, which falls outside the bribery statute under *Snyder*.

**Tags:** chapters: [5], topics: [corruption-bribe-vs-gratuity, corruption-official-acts-narrowing], difficulty: hard, cognitive: application

**Grounding:** Chapter 5 - Legislatures and Courts > Corruption bribe vs gratuity & Official acts narrowing

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The correct answer choice (c) relies on a misstated fact ("making an informal phone call") that directly contradicts Fact 8 ("formally contacted a city zoning official"). A sharp student might erroneously eliminate (c) because it inaccurately quotes the fact pattern. 
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change "making an informal phone call" in option (c) and the explanation to "merely contacting another official" to ensure it aligns perfectly with Fact 8 while preserving the McDonnell doctrine application.
-->
