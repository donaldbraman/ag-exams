# Fix Guidance for q16

The QA pipeline flagged this question. Rewrite `q16.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q16.** Assume Trey is charged with possession with intent to distribute the fentanyl found in his vehicle. Will the prosecution be able to establish the required elements of possession and intent?

(a) Trey is guilty of possession with intent to distribute because his exclusive control of the keys establishes constructive possession, and the packaging and ledger support a distribution inference. <!-- correct -->
(b) Trey is guilty of possession with intent to distribute because being parked within twenty feet of a vehicle containing drugs establishes actual physical possession under federal law.
(c) Trey is not guilty of possession because the drugs were hidden in a secret compartment, which categorically defeats the awareness requirement necessary for constructive possession liability.
(d) Trey is not guilty of intent to distribute because 50 grams of fentanyl is legally presumed to be strictly for personal use unless a controlled buy is completed.
(e) Trey is not guilty of either charge because the police failed to secure a full confession explicitly detailing his specific intended distribution network prior to making the arrest.

**Answer:** (a)

**Explanation:** (a) is correct. Constructive possession requires awareness of the contraband and the ability to exercise dominion and control over it. Holding the car keys establishes Trey's control over the vehicle and its hidden compartment. The massive lethal quantity (50 grams of fentanyl), the 25 individual baggies, and the drug ledger provide overwhelmingly sufficient circumstantial evidence for a jury to infer an intent to distribute. (b) is wrong because mere proximity to drugs does not establish actual physical possession; actual possession requires direct physical control on the person. (c) is wrong because the requirement of awareness can be inferred circumstantially (through control of the keys and the ledger) despite the compartment being hidden. (d) is wrong because there is no legal presumption that 50 grams of fentanyl—an extraordinarily large and lethal amount—is strictly for personal use. (e) is wrong because intent to distribute is routinely and legally proven through circumstantial packaging and quantity evidence, never requiring a confession.

**Tags:** chapters: [15], topics: [constructive possession, PWID inferences], difficulty: easy, cognitive: application
**Grounding:** Chapter 15, Constructive Possession and Quantity Inferences

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: fail. The stem completely lacks the factual predicate needed to evaluate the answers. It mentions "the fentanyl found in his vehicle," but omits all the specific facts relied upon by the correct answer and explanation: Trey's exclusive control of the keys, the 50 grams of fentanyl, the 25 individual baggies, the drug ledger, and the secret compartment. This indicates the question was orphaned from a larger macro fact pattern.
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Integrate the missing facts directly into the stem so the question can function as a standalone item. For example: "Assume Trey is found alone in his vehicle with the keys in his pocket. Police search a secret compartment in the vehicle and find 50 grams of fentanyl divided into 25 individual baggies, along with a drug ledger. Trey is charged with possession with intent to distribute..."
-->
