# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q13.** Assume the jurisdiction has abolished the affirmative defense of insanity (the mens rea model), but allows mental illness evidence to negate specific intent. Can Yasmin be convicted of felony murder based on the robbery of the car keys?

(a) No, because her delusion that she was escaping demons negates the specific intent to steal required for the underlying robbery predicate. <!-- correct -->
(b) Yes, because taking the car keys after killing the clerk satisfies the strict liability requirement for establishing a felony murder charge.
(c) No, because the mens rea model categorically prohibits prosecuting mentally ill defendants for strict liability offenses like felony murder.
(d) Yes, because her voluntary intoxication automatically substitutes for the requisite mental state of the underlying predicate felony charge.
(e) No, because the clerk was an innocent bystander, breaking the proximate cause chain necessary for a standard felony murder conviction.

**Answer:** (a)

**Explanation:** In abolition states (the mens rea model), evidence of mental illness is admissible if it directly negates the specific intent element of the charged offense. Robbery requires the specific intent to steal (animus furandi). Yasmin's delusion that she was taking the keys to escape demons (Fact 13) negates the intent to permanently deprive the owner for criminal gain. Without the underlying predicate felony of robbery, the felony murder charge fails. (b) is wrong because felony murder requires the prosecution to first prove all elements of the underlying predicate felony, including its mens rea. (c) is false; the mens rea model allows prosecution for any crime, provided the defendant actually formed the required intent. (d) is incorrect; while voluntary intoxication can sometimes negate specific intent, it does not "substitute" for it to aid the prosecution. (e) is legally incoherent; killing an innocent bystander during a robbery is the quintessential application of felony murder, not a break in causation.

**Tags:** chapters: [23, 15], topics: [insanity defense, mens rea model, felony murder], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 23, Mens Rea Model Abolition (mens-rea-model-abolition) and Radue Gatekeeping

<!-- audit: MUST FIX
Check 1: fail. Under the strict mens rea model, a delusion that one is escaping demons provides a bizarre motive but does NOT logically negate the specific intent to steal (the intent to permanently deprive). To negate mens rea, the delusion must prevent the defendant from forming the required intent (e.g., a delusion that the keys were her own property). Motive does not negate mens rea. Thus, (a) is doctrinally flawed.
Check 2: pass. The distractors are clearly incorrect, though since (a) is legally flawed, the question currently has no technically correct answer.
Check 3: fail. The explanation claims robbery requires an intent to permanently deprive "for criminal gain." The "criminal gain" (lucri causa) element is an antiquated common law concept abandoned by modern jurisdictions; robbery merely requires the intent to permanently deprive. Furthermore, the explanation improperly conflates motive with mens rea.
Check 4: fail. The stem relies on external facts (referencing "Yasmin", "the robbery", "Fact 13", and the "clerk") that are missing from the standalone prompt.
Check 5: pass. The stub explicitly defines the jurisdiction's specific rules regarding the insanity defense and mens rea.
Check 6: pass. No excluded topics are present.
Check 7: pass. The mens rea model and felony murder are standard criminal law concepts.
Check 8: pass. The answer options exhibit good length parity and structural symmetry.
Recommended fix: Change the delusion in the facts and option (a) to one that actually negates the mens rea of robbery (e.g., "her delusion that the car keys were her own property"). Remove the phrase "for criminal gain" from the explanation. Ensure the necessary facts are included in the prompt if this question is not part of a shared fact-pattern block.
-->

## Issue 2 — edge-case

**Q13.** Assume the jurisdiction has abolished the affirmative defense of insanity (the mens rea model), but allows mental illness evidence to negate specific intent. Can Yasmin be convicted of felony murder based on the robbery of the car keys?

(a) No, because her delusion that she was escaping demons negates the specific intent to steal required for the underlying robbery predicate. <!-- correct -->
(b) Yes, because taking the car keys after killing the clerk satisfies the strict liability requirement for establishing a felony murder charge.
(c) No, because the mens rea model categorically prohibits prosecuting mentally ill defendants for strict liability offenses like felony murder.
(d) Yes, because her voluntary intoxication automatically substitutes for the requisite mental state of the underlying predicate felony charge.
(e) No, because the clerk was an innocent bystander, breaking the proximate cause chain necessary for a standard felony murder conviction.

**Answer:** (a)

**Explanation:** In abolition states (the mens rea model), evidence of mental illness is admissible if it directly negates the specific intent element of the charged offense. Robbery requires the specific intent to steal (animus furandi). Yasmin's delusion that she was taking the keys to escape demons (Fact 13) negates the intent to permanently deprive the owner for criminal gain. Without the underlying predicate felony of robbery, the felony murder charge fails. (b) is wrong because felony murder requires the prosecution to first prove all elements of the underlying predicate felony, including its mens rea. (c) is false; the mens rea model allows prosecution for any crime, provided the defendant actually formed the required intent. (d) is incorrect; while voluntary intoxication can sometimes negate specific intent, it does not "substitute" for it to aid the prosecution. (e) is legally incoherent; killing an innocent bystander during a robbery is the quintessential application of felony murder, not a break in causation.

**Tags:** chapters: [23, 15], topics: [insanity defense, mens rea model, felony murder], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 23, Mens Rea Model Abolition (mens-rea-model-abolition) and Radue Gatekeeping

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Facts 12 and 13 establish that Yasmin killed the clerk to "slay the beast" (a divine command) and took the keys afterward to escape. This inadvertently triggers the "afterthought robbery" (or res gestae) limitation: a killing motivated by reasons independent of a felony, where the theft is a mere afterthought to facilitate escape, cannot support a felony murder conviction. This breaks the felony murder charge independently of the mens rea issue.
2. Cross-Doctrine Clashes: Option A's legal rationale is heavily flawed under the strict Mens Rea Model. A delusional motive (escaping demons) explains *why* she took the keys, but it does not negate the specific intent *to take the keys* (animus furandi). Under the mens rea model, if she intended to permanently deprive the owner of the keys/car to escape, she legally formed the requisite specific intent to steal regardless of her bizarre psychotic motive. 
3. Cross-Question Spoilers: Q11 evaluates if her voluntary intoxication-induced psychosis qualifies as a mental disease. If it is legally classified as mere voluntary intoxication rather than a mental illness, Q13's premise regarding "mental illness evidence" creates a minor legal terminology clash for the student.
Recommended fix: Change the facts so she kills the clerk specifically *to* get the keys (e.g., "she hallucinates the keys are a divine relic necessary to lock the gates of hell, and kills the clerk to obtain them"), and update Option A's rationale so the delusion actually negates an element of robbery (e.g., "No, because she hallucinated the keys were her own divine property, negating the specific intent to steal the property of another").
-->
