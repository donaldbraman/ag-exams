# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q7.** Under the two major tests for attempt actus reus, how should a court evaluate Marcus's conduct of loading the accelerant into his car two miles from the target warehouse?

(a) Guilty under the common law proximity test because obtaining accelerant is dangerously close, but not guilty under the MPC without reaching the scene.
(b) Guilty under the MPC substantial step test because loading accelerant corroborates intent, but not guilty under proximity because he was two miles away. <!-- correct -->
(c) Guilty under both tests because procuring the specific chemical means for an arson categorically satisfies both the proximity and substantial step requirements.
(d) Not guilty under both tests because mere preparation is never sufficient for attempt liability until the perpetrator reaches the immediate target location.
(e) Guilty under the MPC substantial step test, but his liability under the common law proximity test is completely negated by his subjective fear.

**Answer:** (b)

**Explanation:** The common law "dangerous proximity" test requires the defendant to be physically and temporally close to completing the crime. Being two miles away in a parking lot is generally considered mere preparation under proximity. Conversely, the Model Penal Code (MPC) "substantial step" test focuses on whether the conduct strongly corroborates the actor's criminal purpose; loading specialized accelerant into a vehicle satisfies this standard because it confirms the intent to commit the crime, moving the liability line much earlier. (a) completely reverses the doctrines. (c) is incorrect because the proximity test rarely treats logistical preparation far from the scene as sufficiently proximate. (d) is incorrect because the MPC explicitly designed the substantial step test to criminalize conduct long before the perpetrator reaches the immediate target location. (e) is incorrect because while his fear caused abandonment, abandonment is an affirmative defense rather than something that legally negates the completed actus reus element under the proximity test.

**Tags:** chapters: [17], topics: [attempt actus reus, substantial step, proximity test], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 - actus-reus-proximity-test, actus-reus-substantial-step

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: The use of the word "Guilty" in the options creates a severe clash. Under the facts, Marcus arguably has a valid duress defense (established in Stem 1) which would make him ultimately not guilty of attempted arson, regardless of whether the actus reus test is met. 
3. Cross-Question Spoilers: Q5 tests duress and Q8 tests abandonment. Declaring Marcus definitively "Guilty" in Q7's correct answer ignores these affirmative defenses. A sharp student who correctly spots that Marcus's duress precludes ultimate guilt might wrongly eliminate (b) or get stuck. 
Recommended fix: Change "Guilty" and "not guilty" in the options to "Satisfies the actus reus under..." and "fails under..." (or similar), so the question cleanly isolates the actus reus element without making a technically false claim about ultimate guilt.
-->
