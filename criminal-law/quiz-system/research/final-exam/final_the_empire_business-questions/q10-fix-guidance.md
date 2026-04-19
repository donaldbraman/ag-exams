# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** The government considers charging Jack with felony murder for Kevin's death, arguing Kevin was killed during the attempted extortion. In a jurisdiction applying the strict "agency rule" limitation on felony murder, will Jack be convicted?

(a) Yes, because Kevin's death was a highly foreseeable consequence of sending him to violently extort an uncooperative business owner under the proximate cause theory.
(b) No, because the fatal shot was fired by Matthew, the victim of the felony, who was not an agent or co-felon of the underlying conspiracy. <!-- correct -->
(c) Yes, because Jack orchestrated the extortion attempt, making him the principal in the first degree for any fatalities resulting from the execution of the crime.
(d) No, because Kevin's status as a co-felon automatically bars application of the felony murder rule regardless of who actually pulled the trigger during the crime.
(e) Yes, because Matthew's lawful use of self-defense establishes the requisite malice aforethought needed to transfer homicidal intent back to Jack's original extortion command.

**Answer:** (b)

**Explanation:** The correct answer is (b). Under the agency rule limitation, the felony murder doctrine applies only if the fatal act is committed by one of the felons or their agents. Because Matthew (the victim) fired the fatal shot, the killing was not committed by an agent of the felony, so Jack is not liable for felony murder. (a) is wrong because it applies the broader "proximate cause" theory, which the prompt explicitly rules out by specifying the jurisdiction applies the "strict agency rule." (c) is wrong because orchestrating the crime does not override the agency rule's requirement that the fatal act be committed by a co-felon. (d) is wrong because the agency rule focuses on the identity of the killer (must be a co-felon), not the identity of the victim. (e) is wrong because lawful self-defense by a victim does not generate malice to be transferred to the felons.

**Tags:** chapters: [9], topics: [felony murder, agency rule, proximate cause], difficulty: hard, cognitive: application

**Grounding:** General Doctrine - Felony Murder (Agency Rule exception)

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: MUST FIX. The question stem is completely missing the underlying fact pattern. It references Jack, Kevin, Matthew, and an "attempted extortion" without ever stating what happened (e.g., that Matthew shot Kevin in self-defense during the extortion). This appears to be an orphaned question severed from a multi-part fact pattern.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Integrate the required facts into the stem. For example: "Jack sent his accomplice, Kevin, to violently extort Matthew, an uncooperative business owner. During the attempted extortion, Matthew fired a gun in self-defense, killing Kevin. The government considers charging Jack with felony murder for Kevin's death. In a jurisdiction applying the strict 'agency rule' limitation on felony murder, will Jack be convicted?"
-->
