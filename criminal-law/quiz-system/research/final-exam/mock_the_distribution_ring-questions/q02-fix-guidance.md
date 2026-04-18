# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q2.** Assume that it is established that Ben formed the requisite intent to distribute the stimulants. Under the Model Penal Code's substantial step test versus the traditional common law dangerous proximity test, has Ben committed the actus reus of attempted distribution when he parks at the drop location?

(a) Ben satisfied the actus reus under the substantial step test because driving to the designated drop location corroborates his criminal purpose, but he likely failed the dangerous proximity test because he never exited the car or approached the buyer. <!-- correct -->
(b) Ben satisfied the actus reus under the dangerous proximity test because parking 50 feet away is dangerously near completion, but failed the substantial step test because he did not cross the physical threshold of the car.
(c) Ben satisfied the actus reus under both tests because driving to a planned crime scene is universally recognized as the commencement of the consummated offense across all jurisdictions.
(d) Ben failed the actus reus under both tests because he never saw the buyer, meaning the crime could not logically be completed under either the MPC or the common law.
(e) Ben satisfied the actus reus under the substantial step test because he accepted the drugs from Artie, which immediately completed the attempt, rendering his subsequent drive irrelevant.

**Answer:** (a)

**Explanation:** The MPC substantial step test requires conduct strongly corroborative of criminal purpose, explicitly listing traveling to the contemplated scene as sufficient. The traditional dangerous proximity test requires the defendant to come dangerously near completion, which often fails if the target has not yet been located or approached. (a) correctly applies both tests. (b) reverses the thresholds, as dangerous proximity is harder to satisfy than substantial step. (c) is wrong because the proximity test routinely excludes mere arrival at a general location if the buyer is absent. (d) is wrong because the MPC test draws the liability line much earlier and does not require encountering the buyer. (e) is wrong because mere acceptance of the drugs is preparatory; driving to the scene is the substantial step.

**Tags:** chapters: [17], topics: [attempt, actus_reus, substantial_step], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 (Attempts), actus-reus-substantial-step and actus-reus-proximity-test

<!-- audit: MUST FIX
check 1: pass (Assuming the missing background facts, option (a) accurately differentiates the doctrinal thresholds of the two tests).
check 2: pass (Option (e) offers a plausible alternative timing for the substantial step, but fails to address the dangerous proximity test requested in the prompt, making (a) definitively better).
check 3: SHOULD FIX. The explanation claims the MPC "explicitly list[s] traveling to the contemplated scene as sufficient." The MPC does not explicitly list "traveling"; it lists "reconnoitering the place" and "possession of materials... at or near the place" (MPC 5.01(2)(c) and (f)). The explanation's paraphrase should be tightened to match the statute.
check 4: MUST FIX. The stem completely lacks the foundational facts needed to answer the question. It refers to "the stimulants" and "the drop location," while the options introduce new facts like "the buyer," "Artie," and "parking 50 feet away." If this is a standalone question, it is unanswerable without the accompanying narrative.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Integrate the missing narrative facts directly into the stem (e.g., "Ben accepted stimulants from Artie, drove to a designated drop location, and parked his car 50 feet away, but never exited the vehicle or saw the buyer. Assume that it is established..."). Additionally, revise the explanation to cite "possession of materials at or near the place" or "reconnoitering" rather than mere "traveling."
-->
