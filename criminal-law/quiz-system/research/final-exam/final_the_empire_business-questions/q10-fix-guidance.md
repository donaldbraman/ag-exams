# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Assume the state charges Dominic with felony murder for Victor's death based on the underlying armed extortion. Can Dominic be convicted of felony murder?

(a) Yes, because he caused a death during the commission or attempted commission of an inherently dangerous enumerated felony like armed robbery or armed extortion. <!-- correct -->
(b) No, because he only returned fire after Victor shot at him, meaning the death was a justifiable result of self-defense rather than a direct result of the felony.
(c) Yes, because any death that occurs while a defendant is armed with an illegal weapon automatically qualifies as first-degree felony murder in all American legal jurisdictions.
(d) No, because he did not enter the restaurant with the specific premeditated intent to kill Victor, which is required for a first-degree homicide conviction under traditional rules.
(e) Yes, because the agency rule dictates that a defendant is strictly liable even if a third party or the victim actually fires the fatal gunshot during the crime.

**Answer:** (a)

**Explanation:** Dominic can be convicted of felony murder because he caused Victor's death during the commission of an inherently dangerous enumerated felony (armed extortion/robbery). Under traditional felony murder rules, the intent to commit the felony substitutes for the malice required for murder. (b) is incorrect because a defendant cannot claim self-defense against a victim who is lawfully resisting the defendant's violent felony. (c) is incorrect because mere possession of an illegal weapon is not universally an enumerated predicate for first-degree felony murder. (d) is incorrect because the felony murder rule specifically dispenses with the need to prove premeditated intent to kill. (e) is incorrect because Dominic personally fired the fatal shot, making the agency rule (which deals with third-party killings) irrelevant to establishing his direct liability.

**Tags:** chapters: [14], topics: [felony murder, self-defense limitation], difficulty: easy, cognitive: application

**Grounding:** Traditional felony murder elements; Initial aggressor bar to self-defense

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fail (The question references a fact pattern that is entirely missing from the prompt. It assumes knowledge of Dominic, Victor, a restaurant, an armed extortion, and a shootout without establishing those facts.)
check 5: fail (Option (a) asserts that armed extortion is an enumerated felony. Because enumerated predicates vary widely by state, the stem must explicitly stipulate the jurisdiction's statute rather than relying on assumed knowledge of which felonies are enumerated.)
check 6: pass
check 7: pass
Recommended fix: Insert the missing fact pattern into the stem describing the restaurant extortion and shootout. Additionally, explicitly stipulate the applicable law in the stem (e.g., "Assume the jurisdiction's felony murder statute enumerates armed extortion...").
-->

## Issue 2 — edge-case

**Q10.** Assume the state charges Dominic with felony murder for Victor's death based on the underlying armed extortion. Can Dominic be convicted of felony murder?

(a) Yes, because he caused a death during the commission or attempted commission of an inherently dangerous enumerated felony like armed robbery or armed extortion. <!-- correct -->
(b) No, because he only returned fire after Victor shot at him, meaning the death was a justifiable result of self-defense rather than a direct result of the felony.
(c) Yes, because any death that occurs while a defendant is armed with an illegal weapon automatically qualifies as first-degree felony murder in all American legal jurisdictions.
(d) No, because he did not enter the restaurant with the specific premeditated intent to kill Victor, which is required for a first-degree homicide conviction under traditional rules.
(e) Yes, because the agency rule dictates that a defendant is strictly liable even if a third party or the victim actually fires the fatal gunshot during the crime.

**Answer:** (a)

**Explanation:** Dominic can be convicted of felony murder because he caused Victor's death during the commission of an inherently dangerous enumerated felony (armed extortion/robbery). Under traditional felony murder rules, the intent to commit the felony substitutes for the malice required for murder. (b) is incorrect because a defendant cannot claim self-defense against a victim who is lawfully resisting the defendant's violent felony. (c) is incorrect because mere possession of an illegal weapon is not universally an enumerated predicate for first-degree felony murder. (d) is incorrect because the felony murder rule specifically dispenses with the need to prove premeditated intent to kill. (e) is incorrect because Dominic personally fired the fatal shot, making the agency rule (which deals with third-party killings) irrelevant to establishing his direct liability.

**Tags:** chapters: [14], topics: [felony murder, self-defense limitation], difficulty: easy, cognitive: application

**Grounding:** Traditional felony murder elements; Initial aggressor bar to self-defense

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Distractor (b) and the explanation in Q10 explicitly state that Dominic cannot claim self-defense because he was committing a violent felony. This completely spoils Q8, which is dedicated to testing the initial-aggressor-bar for this exact shooting. Furthermore, Option (a) confirms armed robbery/extortion works as a predicate, which partially spoils Q11's independent felonious purpose (merger) test.
Recommended fix: Change distractor (b) to test causation instead of self-defense (e.g., "No, because Victor's unexpected decision to fire first constituted an independent superseding cause") and remove the self-defense discussion from the explanation to preserve Q8.
-->
