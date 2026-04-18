# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q2.** The police intercept Sal on the highway and discover the fentanyl in the hidden compartment. The prosecution subsequently charges Leo with possession of the drugs, despite him not being in the vehicle. Is Leo guilty of possessing the fentanyl?

(a) Yes, because Leo retained the secondary keys and GPS access, establishing his power and intent to exercise dominion and control over the drugs. <!-- correct -->
(b) Yes, because under the common law, any manager of a criminal enterprise is automatically deemed to possess all contraband held by subordinates.
(c) No, because Leo was not physically present in the vehicle when the stop occurred, precluding a finding of actual or constructive possession.
(d) No, because Leo's instruction to Sal to drive straight to the safehouse transferred exclusive legal control of the shipment entirely to Sal.
(e) No, because constructive possession requires the defendant to be the registered owner of the vehicle where the contraband is discovered by police.

**Answer:** (a)

**Explanation:** Constructive possession requires the power and intent to exercise dominion and control over the contraband. By retaining the secondary keys and GPS access, Leo maintained the ability and intent to control the fentanyl shipment, rendering him liable for possession. (b) fails because the common law does not impose automatic possession on managers without proof of control over the specific items. (c) is wrong because constructive possession explicitly bridges the gap between physical absence and legal liability. (d) is incorrect because delegating physical transport to a subordinate does not sever the manager's constructive possession when control mechanisms are retained. (e) fails because constructive possession is based on actual control and intent, not strict legal vehicle ownership.

**Tags:** chapters: [15], topics: [constructive-possession], difficulty: easy, cognitive: application

**Grounding:** Chapter 15 (Drugs and Guns) - Constructive Possession Doctrine

<!-- audit: MUST FIX
check 1: pass (the legal conclusion in the marked answer is correct based on the facts it references, though they are missing from the stem)
check 2: pass
check 3: pass
check 4: MUST FIX - The stem is completely missing its factual setup. It references "the fentanyl," "the hidden compartment," and introduces "Leo" out of nowhere without explaining who Leo is or his connection to the vehicle (e.g., retaining secondary keys, GPS access, or managing Sal). These critical facts only appear in the answer choices and explanation.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Add the missing facts to the stem. For example: "Leo hires Sal to transport a shipment of fentanyl in a vehicle's hidden compartment. Leo instructs Sal to drive straight to a safehouse, while Leo retains a set of secondary keys and monitors the vehicle's location via GPS. The police intercept Sal on the highway..."
-->
