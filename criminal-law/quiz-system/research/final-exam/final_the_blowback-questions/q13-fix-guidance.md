# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q13.** Dom and Leo are charged with constructive possession of the fentanyl found in the console. Which of the following most accurately describes the evidentiary hurdles for proving their possession?

(a) Leo's registered ownership of the car automatically establishes his exclusive constructive possession, precluding any possession charges against his passenger Dom.
(b) Dom's physical proximity to the console and his fingerprints on the latch are sufficient to establish his power and intent to control. <!-- correct -->
(c) Neither can be charged because the opaque, vacuum-sealed nature of the package proves they lacked actual awareness of the specific illicit contents.
(d) Both are strictly liable for the fentanyl because it was discovered in a shared vehicle area during the commission of a separate felony.
(e) Only Leo can be convicted because a mere passenger cannot legally exercise dominion and control over a vehicle's built-in center console compartments.

**Answer:** (b)

**Explanation:** Constructive possession requires the prosecution to prove the defendant had both the power and the intent to exercise dominion and control over the contraband. Dom's physical proximity to the console, combined with his fingerprints on the latch, provides a strong evidentiary nexus establishing this control. Option (a) is wrong because constructive possession can be joint; ownership does not grant exclusive possession. Option (c) is wrong because intent and awareness can be inferred from circumstantial evidence, even if the packaging is sealed. Option (d) is wrong because strict liability does not apply to possession; the prosecution must still prove awareness and intent to control. Option (e) is wrong because passengers can exercise joint dominion and control over areas of a vehicle they can access.

**Tags:** chapters: [15], topics: [constructive possession, awareness, control], difficulty: medium, cognitive: application

**Grounding:** Chapter 15: cp-awareness-control

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The facts establish the fentanyl was "vacuum-sealed" (odorless) and "hidden" inside the console of Leo's car, and Dom was merely a passenger who just jumped in. Because constructive possession requires *awareness* of the contraband, stating that fingerprints on the outside latch and proximity "are sufficient to establish" his intent to control is highly debatable. In many jurisdictions, this evidence alone is legally insufficient to prove a passenger's knowledge of hidden contents.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Soften the language in (b) so it is legally defensible (e.g., change "are sufficient to establish" to "serve as circumstantial evidence the prosecution could use to argue his power and intent to control").
-->
