# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** Can Dom successfully assert the defense of voluntary abandonment for the attempted hijacking?

(a) Yes, because he explicitly shouted "the hit is off" and physically relinquished his weapon before any harm occurred.
(b) Yes, because leaving the scene before demanding the keys demonstrates a complete repudiation of the criminal intent.
(c) No, because the defense of voluntary abandonment is categorically unavailable once a defendant satisfies the actus reus for attempt.
(d) No, because his decision to quit was motivated by the sudden appearance of the police cruiser, making it involuntary. <!-- correct -->
(e) No, because he tossed his backpack into the getaway car, proving he intended to return and complete the crime later.

**Answer:** (d)

**Explanation:** Under the MPC, the defense of voluntary abandonment requires that the defendant completely and voluntarily renounce their criminal purpose. An abandonment is not "voluntary" if it is motivated in whole or in part by circumstances that increase the probability of detection or apprehension (MPC § 5.01(4)). Because Dom abandoned the plan only after seeing the marked police cruiser activate its sirens, his withdrawal was legally involuntary. (a) is wrong because verbal repudiation and dropping the weapon do not cure the fact that the withdrawal was externally motivated by law enforcement. (b) is wrong because his motive for leaving was fear of apprehension, not true repudiation. (c) is wrong because the MPC *does* recognize the abandonment defense even after a substantial step is taken, provided it is truly voluntary. (e) is wrong because tossing the backpack into the car does not necessarily prove an intent to return, but regardless, the presence of police is the legally operative fact defeating the defense.

**Tags:** chapters: [17], topics: [attempt, voluntary-abandonment], difficulty: easy, cognitive: application

**Grounding:** Chapter 17: abandonment-mpc

<!-- audit: MUST FIX
check 1: pass
check 2: fail. A well-prepared student could mount a credible challenge for (c) under the common law. The traditional common law rule holds that once the actus reus for attempt is satisfied, the crime is complete and abandonment is no longer available as a defense. Because the question doesn't specify the MPC, (c) is entirely defensible.
check 3: pass
check 4: fail. The question stem contains no fact pattern. It refers to "Dom" and an "attempted hijacking" without providing the contextual narrative, making it unanswerable as a standalone question.
check 5: fail. The stem does not specify the jurisdiction (MPC vs. common law), which is fatal because the two frameworks split directly on the viability of (c) versus (d).
check 6: pass
check 7: pass
Recommended fix: Insert the missing fact pattern into the stem. Additionally, prepend "Under the Model Penal Code," to the question text to safely rule out the common law rule presented in (c).
-->

## Issue 2 — argpass-sonnet

**Q9.** Can Dom successfully assert the defense of voluntary abandonment for the attempted hijacking?

(a) Yes, because he explicitly shouted "the hit is off" and physically relinquished his weapon before any harm occurred.
(b) Yes, because leaving the scene before demanding the keys demonstrates a complete repudiation of the criminal intent.
(c) No, because the defense of voluntary abandonment is categorically unavailable once a defendant satisfies the actus reus for attempt.
(d) No, because his decision to quit was motivated by the sudden appearance of the police cruiser, making it involuntary. <!-- correct -->
(e) No, because he tossed his backpack into the getaway car, proving he intended to return and complete the crime later.

**Answer:** (d)

**Explanation:** Under the MPC, the defense of voluntary abandonment requires that the defendant completely and voluntarily renounce their criminal purpose. An abandonment is not "voluntary" if it is motivated in whole or in part by circumstances that increase the probability of detection or apprehension (MPC § 5.01(4)). Because Dom abandoned the plan only after seeing the marked police cruiser activate its sirens, his withdrawal was legally involuntary. (a) is wrong because verbal repudiation and dropping the weapon do not cure the fact that the withdrawal was externally motivated by law enforcement. (b) is wrong because his motive for leaving was fear of apprehension, not true repudiation. (c) is wrong because the MPC *does* recognize the abandonment defense even after a substantial step is taken, provided it is truly voluntary. (e) is wrong because tossing the backpack into the car does not necessarily prove an intent to return, but regardless, the presence of police is the legally operative fact defeating the defense.

**Tags:** chapters: [17], topics: [attempt, voluntary-abandonment], difficulty: easy, cognitive: application

**Grounding:** Chapter 17: abandonment-mpc

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Option (a) appeals to the objective manifestation of withdrawal. By explicitly shouting "the hit is off" and physically dropping his weapon, Dom satisfies the outward act of abandonment before any actual harm or the target offense occurs. A student might argue that such clear, objective, and physical withdrawal terminates his liability for attempt, as he has effectively and measurably reversed his prior substantial steps before consummation.
(b) Argument-for: Option (b) focuses on proximity to the completed crime and the point of no return. Because Dom left before the most crucial act—demanding the keys—he did not execute the final step of the actus reus. A student could argue that voluntarily leaving the scene prior to the ultimate act of the crime objectively demonstrates a complete repudiation of criminal intent, satisfying the defense.
(c) Argument-for: Option (c) relies on the traditional common law rule of attempt. Under strict common law, once the defendant crosses the line into attempt (e.g., via dangerous proximity or a substantial step), the offense is complete and cannot be undone by a change of heart. A student correctly applying this historical doctrine would conclude that abandonment is categorically unavailable post-actus reus.
(d) Argument-for: Option (d) correctly applies the MPC § 5.01(4) standard for voluntary abandonment. The defense requires a complete and voluntary renunciation of criminal purpose. Withdrawal motivated by an unexpected increase in the risk of apprehension—such as the sudden appearance of a police cruiser—is legally involuntary because it reflects fear of capture rather than a genuine change of heart. Thus, Dom's defense fails on the voluntariness element.
(e) Argument-for: Option (e) attacks the "complete renunciation" requirement. Tossing the backpack into the getaway car implies a strategic retreat rather than a genuine abandonment of the plan. A student might argue that this physical action proves Dom was merely postponing the crime or fleeing to avoid immediate capture, which legally defeats the complete renunciation element of the abandonment defense.

Head-to-head: Option (d) is clearly the strongest and keyed correctly because it relies on the dispositive legal rule under the MPC: external motivations (police presence) negate the "voluntary" element of abandonment. Option (c) is a highly attractive distractor based on traditional common law, but it fails under the modern MPC standard, making "categorically unavailable" factually false. Options (a), (b), and (e), however, are weaker distractors. Rather than stating a definitively false legal rule, (a) and (b) fail by implicitly omitting the police presence and offering insufficient facts to support their "Yes" conclusions. Option (e) reaches the correct conclusion ("No") but relies on an unreliable factual inference ("proving he intended to return") rather than a false legal claim. The question is fundamentally sound, but (a), (b), and (e) should be locked with absolute language to ensure they present explicit, falsifiable legal errors rather than factual omissions or inferences.

Falsifiable claim per distractor:
- (a): "Yes, because he explicitly shouted... before any harm occurred." — wrong outcome, but relies on an implicit omission (ignoring the police) rather than an explicit, legally false proposition (e.g., "automatically establishes").
- (b): "...demonstrates a complete repudiation of the criminal intent." — wrong because it draws a false factual conclusion about his state of mind rather than stating a falsifiable legal rule.
- (c): "...categorically unavailable once a defendant satisfies the actus reus for attempt." — wrong because the MPC explicitly created the abandonment defense to be available after the actus reus is satisfied.
- (e): "...proving he intended to return and complete the crime later." — wrong because it asserts a definitive factual proof ("proving") rather than a falsifiable proposition of law.

Recommended fix: Update (a), (b), and (e) with absolute locking words to create explicitly false legal claims.
- Change (a) to: "Yes, because explicitly relinquishing a weapon before harm occurs automatically establishes voluntary abandonment regardless of external motivations."
- Change (b) to: "Yes, because leaving the scene prior to completing the target offense categorically demonstrates a complete repudiation in every jurisdiction."
- Change (e) to: "No, because tossing a backpack into a getaway car legally constitutes a substantial step solely because it shows an intent to return."
-->
