# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q13.** Thorne delivered $20,000 to Senator Vance three days before the bill's introduction. Under federal anti-corruption law (*Snyder v. United States*), how is this payment properly classified?

(a) It is a bribe, because the payment was made prior to the official act specifically to influence Vance's agreement to sponsor the pending legislation. <!-- correct -->
(b) It is a gratuity, because Thorne explicitly characterized the transfer as a standard campaign contribution rather than an illicit quid pro quo exchange.
(c) It is a bribe, because any cash payment to a sitting state legislator exceeding ten thousand dollars automatically triggers federal bribery statutes.
(d) It is a gratuity, because Senator Vance had not yet formally introduced the legislation, meaning no official action had been fully completed at that time.
(e) It is neither, because state legislators are exclusively governed by state ethics rules and cannot be prosecuted under federal anti-corruption statutes.

**Answer:** (a)

**Explanation:** Under 18 U.S.C. § 666 and *Snyder v. United States*, the temporal relationship to the official act defines the offense. A bribe is a payment made *before* an official act with the corrupt intent to influence it. A gratuity is a payment made *after* an act as appreciation. Because Thorne paid Vance before the bill was introduced to secure his sponsorship, it is a bribe. (b) is wrong because labeling a bribe a "campaign contribution" does not legally reclassify an explicit quid pro quo exchange. (c) is wrong because there is no automatic $10,000 threshold that converts any payment into a bribe; the quid pro quo intent is required. (d) is wrong because bribery specifically targets the *future* performance of an official act. (e) is wrong because § 666 explicitly applies to state and local officials whose agencies receive federal funding.

**Tags:** chapters: [5], topics: [corruption-bribe-vs-gratuity, federal-corruption, bribery], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 5, Section: Honest Services Fraud (*Snyder v. United States*)

<!-- GROUNDING-FAIL: Bribery vs. Gratuity (Snyder v. United States) is not in any chapter map. The closest taught doctrines are: Chapter 5 covers only Legality, Vagueness, Lenity, Equal Protection, and Desuetude; nearest tags in Chapter 6 are `code-expansion-one-way-ratchet` and `batchelder-overlapping-statutes`. Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q13.** Thorne delivered $20,000 to Senator Vance three days before the bill's introduction. Under federal anti-corruption law (*Snyder v. United States*), how is this payment properly classified?

(a) It is a bribe, because the payment was made prior to the official act specifically to influence Vance's agreement to sponsor the pending legislation. <!-- correct -->
(b) It is a gratuity, because Thorne explicitly characterized the transfer as a standard campaign contribution rather than an illicit quid pro quo exchange.
(c) It is a bribe, because any cash payment to a sitting state legislator exceeding ten thousand dollars automatically triggers federal bribery statutes.
(d) It is a gratuity, because Senator Vance had not yet formally introduced the legislation, meaning no official action had been fully completed at that time.
(e) It is neither, because state legislators are exclusively governed by state ethics rules and cannot be prosecuted under federal anti-corruption statutes.

**Answer:** (a)

**Explanation:** Under 18 U.S.C. § 666 and *Snyder v. United States*, the temporal relationship to the official act defines the offense. A bribe is a payment made *before* an official act with the corrupt intent to influence it. A gratuity is a payment made *after* an act as appreciation. Because Thorne paid Vance before the bill was introduced to secure his sponsorship, it is a bribe. (b) is wrong because labeling a bribe a "campaign contribution" does not legally reclassify an explicit quid pro quo exchange. (c) is wrong because there is no automatic $10,000 threshold that converts any payment into a bribe; the quid pro quo intent is required. (d) is wrong because bribery specifically targets the *future* performance of an official act. (e) is wrong because § 666 explicitly applies to state and local officials whose agencies receive federal funding.

**Tags:** chapters: [5], topics: [corruption-bribe-vs-gratuity, federal-corruption, bribery], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 5, Section: Honest Services Fraud (*Snyder v. United States*)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The stem lacks sufficient facts to establish mens rea (corrupt intent/quid pro quo). It simply states Thorne delivered money before the bill's introduction. Without specifying Thorne's intent, the payment cannot automatically be classified as a bribe. Option (a) assumes facts not provided in the stem ("specifically to influence Vance's agreement").
check 5: pass
check 6: pass
check 7: MUST FIX. Coverage mismatch. *Snyder v. United States*, 18 U.S.C. § 666, and federal bribery/gratuity doctrines are entirely absent from the Meta-Map. Chapter 5 covers Legality, Vagueness, Lenity, Equal Protection, and Desuetude. This question tests a topic outside the scope of the curriculum.
check 8: pass
Recommended fix: Delete the question entirely, as the doctrine is not taught in the course. If the topic were in bounds, the stem would still need to be rewritten to explicitly state Thorne's corrupt intent to establish the required quid pro quo exchange.
-->

## Issue 3 — argpass-sonnet

**Q13.** Thorne delivered $20,000 to Senator Vance three days before the bill's introduction. Under federal anti-corruption law (*Snyder v. United States*), how is this payment properly classified?

(a) It is a bribe, because the payment was made prior to the official act specifically to influence Vance's agreement to sponsor the pending legislation. <!-- correct -->
(b) It is a gratuity, because Thorne explicitly characterized the transfer as a standard campaign contribution rather than an illicit quid pro quo exchange.
(c) It is a bribe, because any cash payment to a sitting state legislator exceeding ten thousand dollars automatically triggers federal bribery statutes.
(d) It is a gratuity, because Senator Vance had not yet formally introduced the legislation, meaning no official action had been fully completed at that time.
(e) It is neither, because state legislators are exclusively governed by state ethics rules and cannot be prosecuted under federal anti-corruption statutes.

**Answer:** (a)

**Explanation:** Under 18 U.S.C. § 666 and *Snyder v. United States*, the temporal relationship to the official act defines the offense. A bribe is a payment made *before* an official act with the corrupt intent to influence it. A gratuity is a payment made *after* an act as appreciation. Because Thorne paid Vance before the bill was introduced to secure his sponsorship, it is a bribe. (b) is wrong because labeling a bribe a "campaign contribution" does not legally reclassify an explicit quid pro quo exchange. (c) is wrong because there is no automatic $10,000 threshold that converts any payment into a bribe; the quid pro quo intent is required. (d) is wrong because bribery specifically targets the *future* performance of an official act. (e) is wrong because § 666 explicitly applies to state and local officials whose agencies receive federal funding.

**Tags:** chapters: [5], topics: [corruption-bribe-vs-gratuity, federal-corruption, bribery], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 5, Section: Honest Services Fraud (*Snyder v. United States*)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under *Snyder v. United States* and 18 U.S.C. § 666, the critical distinction between a bribe and a gratuity is the temporal arrangement and the presence of a *quid pro quo*. Because the payment was made *prior* to the official act (introduction of the bill), it strongly infers a forward-looking corrupt intent to influence. Option (a) accurately aligns the ex ante timing with the legal definition of bribery, making it the most doctrinally sound choice.
(b) Argument-for: Under *McCormick v. United States*, campaign contributions walk a fine line with bribery and require an explicit *quid pro quo* to be criminalized. A student could argue that if Thorne characterized the payment as a standard contribution—and the prompt lacks explicit facts proving a corrupt bargain—the payment cannot be a bribe. Therefore, it might be classified as a gratuity or a lawful contribution, respecting the presumption against criminalizing standard political donations.
(c) Argument-for: Federal anti-corruption law under 18 U.S.C. § 666 contains specific jurisdictional dollar thresholds (e.g., $10,000 in federal funding, $5,000 transaction value). A student might plausibly confuse these jurisdictional triggers with a strict-liability substantive threshold, concluding that a $20,000 cash payment to a legislator is so large that it automatically constitutes a bribe as a matter of law, bypassing the need for subjective intent.
(d) Argument-for: Bribery requires an agreement regarding an official act. A student could argue that because the bill had not yet been formally introduced, the "official act" was not yet ripe or completed. Therefore, the payment could only be considered a gratuity (a reward for general preliminary support or drafting) rather than a bribe for a completed, definitively agreed-upon official act. 
(e) Argument-for: *Snyder v. United States* (2024) heavily emphasized federalism, warning against interpreting federal statutes in a way that would subject state and local officials to federal prosecution for run-of-the-mill state ethics violations. A student could extrapolate from this holding that the Supreme Court categorically exempted state legislators from federal anti-corruption statutes, leaving them "exclusively governed by state ethics rules."

Head-to-head: Option (a) is the only choice that correctly identifies the forward-looking *quid pro quo* intent as the hallmark of a bribe. However, the question stem is flawed: the prompt itself does not contain the facts establishing Thorne's intent (the *quid pro quo*), meaning option (a) supplies the necessary facts ("specifically to influence Vance's agreement") rather than just stating a legal conclusion derived from the prompt. Despite this drafting flaw, the distractors all fail due to explicitly false claims of law. (b) falsely claims that a donor's subjective characterization controls the legal classification. (c) falsely relies on an "automatic trigger." (d) fails because the incomplete nature of an act actually points *away* from a gratuity (which is typically an ex post reward for a completed act). (e) falsely relies on a categorical exemption for state officials. 

Falsifiable claim per distractor:
- (b): "because Thorne explicitly characterized the transfer as a standard campaign contribution" — wrong because a defendant's subjective label or characterization does not legally preclude a transaction from being classified as a bribe if a *quid pro quo* exists.
- (c): "automatically triggers federal bribery statutes" — wrong because federal bribery requires corrupt intent (*mens rea*); no dollar amount functions as a strict-liability automatic trigger.
- (d): "It is a gratuity, because Senator Vance had not yet formally introduced the legislation" — wrong because a gratuity is a reward for a *past* act; the fact that the action was not yet completed is indicative of a forward-looking bribe, not a gratuity.
- (e): "exclusively governed by state ethics rules and cannot be prosecuted under federal anti-corruption statutes" — wrong because 18 U.S.C. § 666 explicitly applies to state and local officials whose agencies receive over $10,000 in federal funds.

Recommended fix: Add the *mens rea* / intent to the prompt so option (a) does not have to invent facts. Change the first sentence to: "Thorne delivered $20,000 to Senator Vance three days before the bill's introduction, pursuant to an agreement that Vance would sponsor the legislation."
-->
