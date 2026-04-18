# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q11.** Dominic is charged with attempted murder of Elias based on his actions of buying the rifle, driving to Elias's house, and waiting outside. Under the Model Penal Code (MPC) approach to attempt, is Dominic guilty?

(a) Yes, because his actions strongly corroborate his criminal purpose and constitute a substantial step toward the commission of the murder under the Model Penal Code. <!-- correct -->
(b) Yes, because he came dangerously close to completing the crime and unequivocally crossed the physical line from mere preparation to the actual execution phase.
(c) No, because sitting in a parked car is entirely equivocal conduct that could be reasonably interpreted as non-criminal absent a direct confession of his intent.
(d) No, because the police intervened and arrested him before he acquired a target in his sights, leaving the critical last proximate act incomplete.
(e) No, because he voluntarily and completely abandoned his criminal plan by merely waiting in the car rather than actively approaching the rival gang leader's house.

**Answer:** (a)

**Explanation:** Under the Model Penal Code's approach to attempt, the actus reus is satisfied when the defendant takes a "substantial step" that strongly corroborates their criminal purpose. Buying a sniper rifle, driving to the victim's house, and waiting outside with a loaded weapon clearly constitutes a substantial step corroborating the intent to murder Elias. (b) is wrong because "dangerously close" and "crossing the line from preparation to execution" describe the common law proximity test, not the MPC standard. (c) is wrong because sitting with a loaded sniper rifle outside a target's house is not equivocal under the MPC's corroboration test. (d) is wrong because the MPC does not require the defendant to complete the last proximate act before arrest. (e) is wrong because waiting for the target to emerge is a tactical delay, not a complete and voluntary renunciation of the criminal purpose.

**Tags:** chapters: [17], topics: [attempt, actus-reus, substantial-step, mpc], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, MPC Substantial Step Test

<!-- audit: SHOULD FIX
check 1: pass
check 2: pass
check 3: pass
check 4: The stem fails to establish Dominic's mens rea. Attempted murder requires the specific intent (purpose) to kill. Without this explicitly stipulated in the facts, a strict reading means we cannot definitively conclude he is guilty, as his actions alone could theoretically be for a lesser crime (e.g., assault or terroristic threats). 
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Add "Intending to kill Elias," to the beginning of the prompt. Additionally, in option (e), remove the extraneous phrase "rival gang leader's" which introduces a random fact not present in the stem.
-->

## Issue 2 — argpass-opus

**Q11.** Dominic is charged with attempted murder of Elias based on his actions of buying the rifle, driving to Elias's house, and waiting outside. Under the Model Penal Code (MPC) approach to attempt, is Dominic guilty?

(a) Yes, because his actions strongly corroborate his criminal purpose and constitute a substantial step toward the commission of the murder under the Model Penal Code. <!-- correct -->
(b) Yes, because he came dangerously close to completing the crime and unequivocally crossed the physical line from mere preparation to the actual execution phase.
(c) No, because sitting in a parked car is entirely equivocal conduct that could be reasonably interpreted as non-criminal absent a direct confession of his intent.
(d) No, because the police intervened and arrested him before he acquired a target in his sights, leaving the critical last proximate act incomplete.
(e) No, because he voluntarily and completely abandoned his criminal plan by merely waiting in the car rather than actively approaching the rival gang leader's house.

**Answer:** (a)

**Explanation:** Under the Model Penal Code's approach to attempt, the actus reus is satisfied when the defendant takes a "substantial step" that strongly corroborates their criminal purpose. Buying a sniper rifle, driving to the victim's house, and waiting outside with a loaded weapon clearly constitutes a substantial step corroborating the intent to murder Elias. (b) is wrong because "dangerously close" and "crossing the line from preparation to execution" describe the common law proximity test, not the MPC standard. (c) is wrong because sitting with a loaded sniper rifle outside a target's house is not equivocal under the MPC's corroboration test. (d) is wrong because the MPC does not require the defendant to complete the last proximate act before arrest. (e) is wrong because waiting for the target to emerge is a tactical delay, not a complete and voluntary renunciation of the criminal purpose.

**Tags:** chapters: [17], topics: [attempt, actus-reus, substantial-step, mpc], difficulty: medium, cognitive: application

**Grounding:** Chapter 17, MPC Substantial Step Test

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Option (a) correctly applies the Model Penal Code's "substantial step" test for the actus reus of attempt. Under MPC § 5.01, an attempt requires an act constituting a substantial step in a course of conduct planned to culminate in the crime's commission, and this conduct must "strongly corroborate" the actor's criminal purpose. The MPC specifically provides that "lying in wait, searching for or following the contemplated victim" is legally sufficient conduct. Therefore, buying a rifle, driving to Elias's house, and waiting outside meets the MPC requirements perfectly.
(b) Argument-for: A student might choose Option (b) by concluding that Dominic's actions objectively satisfy the most stringent attempt standards. The argument would be that driving to the victim's house and waiting outside with a rifle is so close to execution that it satisfies the "dangerously close" physical proximity test and the "unequivocality" test. Because it satisfies these stricter common law tests, a student might reason that it *a fortiori* proves guilt, making the statement factually true regarding his progression along the timeline of the crime.
(c) Argument-for: Option (c) can be defended by arguing that without an explicit confession or an overt act like aiming the weapon, sitting in a parked car is ambiguous. A student could argue that under the equivocality test (res ipsa loquitur), the act itself must show criminal intent on its face. They could further argue that even under the MPC, the lack of an overt act of execution means the conduct is not "strongly corroborative" enough of a specific intent to kill, remaining mere preparation.
(d) Argument-for: Option (d) appeals to the strict "last proximate act" test. A student could argue that a true attempt requires the defendant to perform the absolute final act within their control necessary to complete the crime. Because the police intervened before Dominic aimed or fired the weapon, he had not performed the critical last proximate act. The student might mistakenly believe the MPC retains this requirement to distinguish attempt from mere preparation, thereby concluding he is not guilty.
(e) Argument-for: Option (e) relies on the MPC affirmative defense of complete and voluntary renunciation. Under MPC § 5.01(4), an actor is not guilty of attempt if they abandon their effort under circumstances manifesting a complete and voluntary renunciation of their criminal purpose. A student could argue that the phrase "merely waiting in the car" implies Dominic chose to halt his approach, legally abandoning the attempt before commission.

Head-to-head: 
Option (a) is the only option that applies the correct MPC doctrine (the "substantial step" and "strongly corroborative" test) requested by the prompt. Option (b) reaches the right conclusion but justifies it with common law tests ("dangerously close," "unequivocally crossed"), rendering the legal rationale false under the MPC. Option (c) relies on the rejected "equivocality" test and erroneously claims lying in wait is entirely equivocal, contradicting the explicit text of the MPC. Option (d) incorrectly applies the "last proximate act" test, which the MPC categorically rejects. Option (e) incorrectly characterizes tactical lying in wait as an affirmative voluntary abandonment, but it also hallucinates a "rival gang leader" not present in the prompt. 

Falsifiable claim per distractor:
- (b): "because he came dangerously close... and unequivocally crossed the physical line" — wrong because it relies solely on common law physical proximity and equivocality standards to establish liability, whereas the prompt explicitly tests the MPC's substantial step rationale.
- (c): "sitting in a parked car is entirely equivocal conduct" — wrong because under the MPC, lying in wait is explicitly listed as a substantial step that strongly corroborates criminal intent; it is not entirely equivocal.
- (d): "leaving the critical last proximate act incomplete" — wrong because the MPC expressly rejects the requirement that a defendant must reach the last proximate act to be guilty of attempt.
- (e): "voluntarily and completely abandoned his criminal plan by merely waiting in the car" — wrong because waiting to ambush a victim is lying in wait, categorically failing the requirement for a voluntary and complete renunciation.

Recommended fix: Option (e) hallucinates a fact not in the prompt. Change "the rival gang leader's house" to "Elias's house" to ensure the distractor remains cleanly tied to the fact pattern.
-->
