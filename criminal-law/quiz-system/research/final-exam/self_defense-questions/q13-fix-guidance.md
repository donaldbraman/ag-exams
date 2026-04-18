# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q13.** Assume that Blake is guilty of attempted arson. The prosecution charges Alex as an accomplice to the attempted arson based on the text message: "Burn it all down before the cops come." Alex argues this communication is insufficient. How should the court rule?

(a) Liable as an accomplice, because sending the text successfully encouraged Blake's actions and demonstrated a purpose to promote the arson. <!-- correct -->
(b) Not liable as an accomplice, because Alex was not physically present at the scene to provide material assistance with the gasoline.
(c) Liable as an accomplice, because mere knowledge of a co-conspirator's general propensity for violence satisfies the accomplice mens rea.
(d) Not liable as an accomplice, because a text message cannot legally constitute the actus reus of aiding and abetting without detailed logistical instructions.
(e) Liable as an accomplice, because the *Pinkerton* doctrine automatically treats all written communications between co-conspirators as accomplice liability.

**Answer:** (a)

**Explanation:** Accomplice liability attaches when a person, with the purpose of promoting or facilitating a crime, solicits, commands, or encourages another to commit it. Alex's text explicitly directed the arson, demonstrating the requisite purpose, and Blake acted upon reading it, completing the actus reus of encouragement. (b) is wrong because physical presence is not required; remote encouragement is sufficient. (c) is wrong because accomplice liability requires specific intent (purpose) regarding the crime, not just knowledge of a general propensity. (d) is wrong because the actus reus of accomplice liability is broadly defined and includes verbal or written encouragement; detailed logistical instructions are not required. (e) is wrong because *Pinkerton* addresses co-conspirator liability for substantive offenses, whereas this question tests the distinct doctrine of accomplice liability via direct encouragement.

**Tags:** chapters: [18], topics: [accomplice-liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (Accomplice Liability) - Actus reus (encouragement) and mens rea (purpose) of aiding and abetting.

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: The opening phrase "Assume that Blake is guilty of attempted arson" heavily telegraphs the correct conclusion for Q12 (that Blake's conduct meets the substantial step test for attempt). While framed as an assumption, it gives away the punchline to the prior questions evaluating Blake's inchoate liability. 
Recommended fix: Change the opening sentence to: "Assume for the purposes of this question only that the court finds Blake's conduct went far enough to constitute attempted arson." This brackets the issue without validating Blake's absolute guilt for the previous questions.
-->
