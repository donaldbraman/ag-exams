# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q7.** Under 18 U.S.C. § 666 (Federal Program Bribery) and the Supreme Court's ruling in *Snyder v. United States*, does Vance's $50,000 payment to Judge Caldwell constitute a criminal violation?

(a) Yes, because the payment was intended to influence a future official act, as established by the corrupt agreement formed prior to the suppression hearing.
(b) Yes, because Section 666 criminalizes both bribes given before an official act and gratuities given afterward to reward an official for a favorable past action.
(c) No, because the Supreme Court ruled that Section 666 criminalizes only bribes involving a quid pro quo and does not cover after-the-fact gratuities. <!-- correct -->
(d) No, because a state trial judge does not qualify as an agent of an organization receiving federal funds unless those specific funds are tied to the case.
(e) No, because the $50,000 payment does not meet the jurisdictional monetary threshold required to trigger federal prosecution under the federal program bribery statute.

**Answer:** (c)

**Explanation:** In *Snyder v. United States*, the Supreme Court held that 18 U.S.C. § 666 criminalizes bribes (payments made with a corrupt intent to influence an official act before it occurs) but does not criminalize after-the-fact gratuities (payments rewarding past actions without a prior corrupt agreement). Since the $50,000 was a "thank you" gift prepared three weeks after the ruling with no evidence of a prior agreement, it is an uncriminalized gratuity under the statute (Fact 4). (c) is correct. (a) is wrong on the facts; there is no evidence of a corrupt agreement formed prior to the suppression hearing. (b) is wrong because *Snyder* explicitly held that § 666 does not cover gratuities. (d) is wrong because § 666 covers agents of state agencies receiving >$10k in federal funds generally; a strict nexus to the specific case is not required. (e) is wrong because the $50,000 payment easily exceeds the $5,000 value threshold of § 666.

**Tags:** chapters: [8], topics: [federal-program-bribery, snyder, gratuity], difficulty: medium, cognitive: recall

**Grounding:** Snyder v. United States, 144 S. Ct. 1947 (2024)

<!-- GROUNDING-FAIL: Federal Program Bribery / Snyder v. United States is not in any chapter map. The closest taught doctrines are: None (meta-map artifact missing). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q7.** Under 18 U.S.C. § 666 (Federal Program Bribery) and the Supreme Court's ruling in *Snyder v. United States*, does Vance's $50,000 payment to Judge Caldwell constitute a criminal violation?

(a) Yes, because the payment was intended to influence a future official act, as established by the corrupt agreement formed prior to the suppression hearing.
(b) Yes, because Section 666 criminalizes both bribes given before an official act and gratuities given afterward to reward an official for a favorable past action.
(c) No, because the Supreme Court ruled that Section 666 criminalizes only bribes involving a quid pro quo and does not cover after-the-fact gratuities. <!-- correct -->
(d) No, because a state trial judge does not qualify as an agent of an organization receiving federal funds unless those specific funds are tied to the case.
(e) No, because the $50,000 payment does not meet the jurisdictional monetary threshold required to trigger federal prosecution under the federal program bribery statute.

**Answer:** (c)

**Explanation:** In *Snyder v. United States*, the Supreme Court held that 18 U.S.C. § 666 criminalizes bribes (payments made with a corrupt intent to influence an official act before it occurs) but does not criminalize after-the-fact gratuities (payments rewarding past actions without a prior corrupt agreement). Since the $50,000 was a "thank you" gift prepared three weeks after the ruling with no evidence of a prior agreement, it is an uncriminalized gratuity under the statute (Fact 4). (c) is correct. (a) is wrong on the facts; there is no evidence of a corrupt agreement formed prior to the suppression hearing. (b) is wrong because *Snyder* explicitly held that § 666 does not cover gratuities. (d) is wrong because § 666 covers agents of state agencies receiving >$10k in federal funds generally; a strict nexus to the specific case is not required. (e) is wrong because the $50,000 payment easily exceeds the $5,000 value threshold of § 666.

**Tags:** chapters: [8], topics: [federal-program-bribery, snyder, gratuity], difficulty: medium, cognitive: recall

**Grounding:** Snyder v. United States, 144 S. Ct. 1947 (2024)

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass (distractors are legally well-crafted given the intended facts)
Check 3: pass
Check 4: FAIL. The stem is completely missing the fact pattern needed to answer the question. It abruptly refers to "Vance's $50,000 payment to Judge Caldwell," and the explanation references "Fact 4", a "suppression hearing," and a "thank you" gift made "three weeks after the ruling." Without these facts, a student cannot distinguish between option (a) (a prior corrupt agreement) and option (c) (an after-the-fact gratuity).
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Insert the missing fact pattern into the question stem (or ensure it is explicitly tethered to a shared, multi-question fact pattern document).
-->
