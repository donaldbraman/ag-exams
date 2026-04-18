# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q14.** Assume that, whether or not Albert is guilty under the common law, the jurisdiction applies the Model Penal Code's "substantial step" test for attempt. How would this standard likely affect the outcome of his attempted manufacturing charge compared to the dangerous proximity test?

(a) It would make conviction less likely because the MPC requires the defendant's conduct to be the absolute last proximate act before the completion of the crime.
(b) It would make conviction more likely because possessing materials at the planned site of the crime strongly corroborates his criminal purpose, satisfying the test. <!-- correct -->
(c) It would guarantee an acquittal because the MPC categorically exempts preparatory acts involving legal precursor chemicals from attempt liability, regardless of the defendant's intent.
(d) It would shift the burden of proof to Albert to prove by a preponderance of the evidence that he genuinely intended to completely abandon the effort.
(e) It would have no effect on the outcome because the substantial step test and the dangerous proximity test require identical factual elements to establish the actus reus.

**Answer:** (b)

**Explanation:** The MPC's substantial step test requires an act that strongly corroborates the actor's criminal purpose. Gathering materials and possessing them at the planned site of the crime (the laboratory) typically satisfies this standard, making conviction more likely than under the strict proximity test. (a) is incorrect because the "last proximate act" requirement is a strict common law standard that the MPC explicitly rejected. (c) is incorrect because the MPC does not categorically exempt the use of legal precursor chemicals if their possession corroborates a criminal purpose. (d) is incorrect because while abandonment is an affirmative defense, the MPC does not shift the burden on proving the actus reus elements of attempt. (e) is incorrect because the substantial step test reaches further back into preparatory conduct than the dangerous proximity test.

**Tags:** chapters: [17], topics: [attempt, actus-reus-substantial-step, MPC vs Common Law], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, Attempts — actus-reus-substantial-step

<!-- audit: MUST FIX
Check 1: pass (Assuming the facts involve possessing materials at a lab site, (b) is doctrinally correct under MPC 5.01(2)(c)).
Check 2: pass
Check 3: pass
Check 4: fail (The stem refers to Albert and his "attempted manufacturing charge," but provides absolutely no facts about what Albert did. This appears to be an orphaned question separated from a shared fact pattern. The student has no way to know Albert possessed materials at a planned site unless they reverse-engineer the facts from option b).
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Provide the missing fact pattern within the question stem (e.g., "Albert was arrested at a warehouse he had rented, in possession of legal precursor chemicals he planned to use to manufacture illegal drugs. Assume that...").
-->

## Issue 2 — argpass-opus

**Q14.** Assume that, whether or not Albert is guilty under the common law, the jurisdiction applies the Model Penal Code's "substantial step" test for attempt. How would this standard likely affect the outcome of his attempted manufacturing charge compared to the dangerous proximity test?

(a) It would make conviction less likely because the MPC requires the defendant's conduct to be the absolute last proximate act before the completion of the crime.
(b) It would make conviction more likely because possessing materials at the planned site of the crime strongly corroborates his criminal purpose, satisfying the test. <!-- correct -->
(c) It would guarantee an acquittal because the MPC categorically exempts preparatory acts involving legal precursor chemicals from attempt liability, regardless of the defendant's intent.
(d) It would shift the burden of proof to Albert to prove by a preponderance of the evidence that he genuinely intended to completely abandon the effort.
(e) It would have no effect on the outcome because the substantial step test and the dangerous proximity test require identical factual elements to establish the actus reus.

**Answer:** (b)

**Explanation:** The MPC's substantial step test requires an act that strongly corroborates the actor's criminal purpose. Gathering materials and possessing them at the planned site of the crime (the laboratory) typically satisfies this standard, making conviction more likely than under the strict proximity test. (a) is incorrect because the "last proximate act" requirement is a strict common law standard that the MPC explicitly rejected. (c) is incorrect because the MPC does not categorically exempt the use of legal precursor chemicals if their possession corroborates a criminal purpose. (d) is incorrect because while abandonment is an affirmative defense, the MPC does not shift the burden on proving the actus reus elements of attempt. (e) is incorrect because the substantial step test reaches further back into preparatory conduct than the dangerous proximity test.

**Tags:** chapters: [17], topics: [attempt, actus-reus-substantial-step, MPC vs Common Law], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, Attempts — actus-reus-substantial-step

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue this if they misremember the MPC's attempt provisions. If one erroneously equates the MPC's "substantial step" with the strictest common law tests (like the "last act" test originally formulated in some early English cases), they could conclude the MPC requires the absolute last proximate act, making conviction less likely.
(b) Argument-for: This is the correct answer. The MPC's substantial step test (§ 5.01(1)(c)) expands attempt liability by pushing it further back into the preparatory stages. Specifically, § 5.01(2) explicitly lists "possession of materials to be employed in the commission of the crime, at or near the place contemplated for its commission" as conduct that satisfies the test if it strongly corroborates the actor's criminal purpose.
(c) Argument-for: A student might falsely believe that the MPC categorically exempts wholly legal preparatory acts (like buying legal precursor chemicals) from general attempt liability to avoid overcriminalizing everyday commerce. If legal items cannot constitute an attempt, they might conclude this would guarantee an acquittal.
(d) Argument-for: The MPC notably introduces the affirmative defense of voluntary and complete renunciation of criminal purpose (§ 5.01(4)). A student could argue that applying the MPC standard changes the outcome specifically because it formalizes this defense, meaning the standard itself shifts the burden of proof to Albert to prove his complete abandonment of the effort.
(e) Argument-for: A student might argue that courts often conflate attempt standards in practice, treating "substantial step" and "dangerous proximity" as semantic variations of the same underlying constitutional requirement. Under this view, both tests functionally require identical factual elements to establish the actus reus.

Head-to-head: (b) is the clear, correct application of MPC § 5.01(2). Distractors (a), (c), and (e) are firmly locked with absolute language ("absolute last proximate act", "categorically exempts", "identical factual elements") that makes them explicitly false. Distractor (d) is factually incorrect because the substantial step test defines the prima facie actus reus and does not itself shift the burden of proof to prove abandonment (renunciation is a separate affirmative defense). However, (d) lacks an absolute locking word, making it slightly vulnerable to interpretation if students conflate adopting the MPC attempt test with automatically adopting the MPC's burden-shifting for affirmative defenses.

Falsifiable claim per distractor:
- (a): "requires the defendant's conduct to be the absolute last proximate act" — wrong because the MPC explicitly rejected the last act test in favor of the substantial step test.
- (c): "categorically exempts preparatory acts involving legal precursor chemicals... regardless of the defendant's intent" — wrong because the MPC does not exempt legal precursors if their possession strongly corroborates criminal purpose.
- (d): "shift the burden of proof to Albert to prove... genuinely intended to completely abandon" — wrong because the substantial step test itself relates to the prima facie case and does not shift the burden of proof, even if the MPC separately allows an affirmative defense of renunciation.
- (e): "require identical factual elements to establish the actus reus" — wrong because the substantial step test reaches further back into preparation than the dangerous proximity test.

Recommended fix: Change (d) to include an absolute word to lock the false claim: "(d) It would automatically shift the burden of proof to Albert to prove by a preponderance of the evidence that he genuinely intended to completely abandon the effort."
-->
