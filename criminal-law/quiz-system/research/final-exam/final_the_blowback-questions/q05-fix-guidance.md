# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q5.** Assume that the jurisdiction has adopted the accomplice felony murder limitations of California SB 1437. Is Penelope guilty of felony murder for Wendy's death?

(a) Yes, because her instruction to "Drive! Go, go, go!" legally constitutes aiding and abetting the homicide with the specific intent to kill.
(b) Yes, because anyone who serves as the primary organizer of a felony is strictly liable for any deaths during the immediate flight.
(c) Yes, because by jumping into the getaway car, she became an active co-felon, satisfying the agency theory of homicide liability.
(d) No, because her explicit prohibition of weapons and the unarmed nature of the theft demonstrate she lacked reckless indifference to human life. <!-- correct -->
(e) No, because under the rule of lenity, a non-driving accomplice can never be deemed a major participant in a vehicular homicide.

**Answer:** (d)

**Explanation:** Under California SB 1437 (codifying *Tison*), an accomplice who is not the actual killer can only be convicted of felony murder if they aided with intent to kill or were a "major participant" who acted with "reckless indifference to human life." Although Penelope organized the theft, her explicit instruction of "No weapons, no violence" and the unarmed nature of the crime strongly demonstrate she did not act with reckless indifference to human life. (a) is wrong because yelling "Drive!" to escape does not legally constitute the specific intent to kill the pedestrian. (b) is wrong because SB 1437 eliminated strict liability for major participants; they must also possess reckless indifference. (c) is wrong because SB 1437 limits traditional agency theories by requiring individualized culpability findings. (e) is wrong because a non-driving accomplice *can* be liable if they genuinely satisfy both statutory prongs.

**Tags:** chapters: [14], topics: [felony murder, accomplice liability, major participant, reckless indifference], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14, sb-1437-major-participant; requires a non-killer accomplice to be a major participant acting with reckless indifference to human life.

<!-- GROUNDING-FAIL: California SB 1437 (major participant/reckless indifference) is not in any chapter map. The closest taught doctrines are: None (meta-map artifact is missing). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q5.** Assume that the jurisdiction has adopted the accomplice felony murder limitations of California SB 1437. Is Penelope guilty of felony murder for Wendy's death?

(a) Yes, because her instruction to "Drive! Go, go, go!" legally constitutes aiding and abetting the homicide with the specific intent to kill.
(b) Yes, because anyone who serves as the primary organizer of a felony is strictly liable for any deaths during the immediate flight.
(c) Yes, because by jumping into the getaway car, she became an active co-felon, satisfying the agency theory of homicide liability.
(d) No, because her explicit prohibition of weapons and the unarmed nature of the theft demonstrate she lacked reckless indifference to human life. <!-- correct -->
(e) No, because under the rule of lenity, a non-driving accomplice can never be deemed a major participant in a vehicular homicide.

**Answer:** (d)

**Explanation:** Under California SB 1437 (codifying *Tison*), an accomplice who is not the actual killer can only be convicted of felony murder if they aided with intent to kill or were a "major participant" who acted with "reckless indifference to human life." Although Penelope organized the theft, her explicit instruction of "No weapons, no violence" and the unarmed nature of the crime strongly demonstrate she did not act with reckless indifference to human life. (a) is wrong because yelling "Drive!" to escape does not legally constitute the specific intent to kill the pedestrian. (b) is wrong because SB 1437 eliminated strict liability for major participants; they must also possess reckless indifference. (c) is wrong because SB 1437 limits traditional agency theories by requiring individualized culpability findings. (e) is wrong because a non-driving accomplice *can* be liable if they genuinely satisfy both statutory prongs.

**Tags:** chapters: [14], topics: [felony murder, accomplice liability, major participant, reckless indifference], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14, sb-1437-major-participant; requires a non-killer accomplice to be a major participant acting with reckless indifference to human life.

<!-- audit: MUST FIX
check 1: pass (assuming the missing facts align with the explanation)
check 2: pass
check 3: pass
check 4: fail - The stem is entirely missing the fact pattern describing Penelope, Wendy, the theft, and the getaway car.
check 5: fail - The stem requires students to memorize the substantive contents of "California SB 1437" rather than explicitly providing the rule. This violates the pedagogical principle against testing rote memorization of state-specific statutes or rules.
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Insert the missing factual scenario into the stem. Additionally, explicitly provide the legal rule in the stem (e.g., "Assume the jurisdiction limits felony murder liability for non-killers to those who either aid with the intent to kill, or are major participants in the underlying felony who act with reckless indifference to human life.") instead of relying on memorization of SB 1437.
-->

## Issue 3 — argpass-opus

**Q5.** Assume that the jurisdiction has adopted the accomplice felony murder limitations of California SB 1437. Is Penelope guilty of felony murder for Wendy's death?

(a) Yes, because her instruction to "Drive! Go, go, go!" legally constitutes aiding and abetting the homicide with the specific intent to kill.
(b) Yes, because anyone who serves as the primary organizer of a felony is strictly liable for any deaths during the immediate flight.
(c) Yes, because by jumping into the getaway car, she became an active co-felon, satisfying the agency theory of homicide liability.
(d) No, because her explicit prohibition of weapons and the unarmed nature of the theft demonstrate she lacked reckless indifference to human life. <!-- correct -->
(e) No, because under the rule of lenity, a non-driving accomplice can never be deemed a major participant in a vehicular homicide.

**Answer:** (d)

**Explanation:** Under California SB 1437 (codifying *Tison*), an accomplice who is not the actual killer can only be convicted of felony murder if they aided with intent to kill or were a "major participant" who acted with "reckless indifference to human life." Although Penelope organized the theft, her explicit instruction of "No weapons, no violence" and the unarmed nature of the crime strongly demonstrate she did not act with reckless indifference to human life. (a) is wrong because yelling "Drive!" to escape does not legally constitute the specific intent to kill the pedestrian. (b) is wrong because SB 1437 eliminated strict liability for major participants; they must also possess reckless indifference. (c) is wrong because SB 1437 limits traditional agency theories by requiring individualized culpability findings. (e) is wrong because a non-driving accomplice *can* be liable if they genuinely satisfy both statutory prongs.

**Tags:** chapters: [14], topics: [felony murder, accomplice liability, major participant, reckless indifference], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 14, sb-1437-major-participant; requires a non-killer accomplice to be a major participant acting with reckless indifference to human life.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that directing a getaway driver to "Go, go, go!" during a high-stress escape foreseeably commands the driver to plow through obstacles, including pedestrians. By giving the explicit instruction to drive aggressively in a dangerous setting, Penelope took ownership of the vehicle's lethal trajectory. Thus, her instruction legally amounts to aiding and abetting the resulting homicide, manifesting the specific intent to kill anyone in the car's path to effectuate the escape.
(b) Argument-for: A student could argue that "primary organizers" bear ultimate responsibility for the execution of the crime, including the escape. Because Penelope planned the felony and initiated the flight, traditional felony murder doctrines treat the mastermind as strictly liable for deaths occurring during the res gestae. Under this view, her status as the ringleader supersedes SB 1437's granular mens rea requirements, imposing strict liability for the botched getaway.
(c) Argument-for: A student could defend this option by relying on the traditional agency theory of felony murder. By jumping into the getaway car, Penelope actively participated in the immediate flight, making the driver her agent. Because the driver's lethal act was committed in furtherance of their shared escape, Penelope is vicariously liable as an active co-felon, which arguably satisfies the foundational requirements of homicide liability.
(d) Argument-for: A student would correctly argue that under California SB 1437 (incorporating the *Tison* standard), a non-killer accomplice must be a major participant who acts with reckless indifference to human life. The *Banks/Clark* factors used to evaluate this standard specifically look at the defendant's efforts to minimize violence. Penelope’s explicit prohibition of weapons ("No weapons, no violence") and the unarmed nature of the theft provide overwhelmingly strong evidence that she lacked the requisite reckless indifference, shielding her from liability.
(e) Argument-for: A student could argue that vehicular homicides involve spontaneous, split-second decisions by the driver that a passenger cannot control. Therefore, the rule of lenity dictates that ambiguous statutory terms like "major participant" should be construed narrowly to exclude mere passengers. Under this strict construction, a non-driving accomplice categorically cannot be held liable for a driver's independent vehicular manslaughter.

Head-to-head: Option (d) is clearly the strongest because it directly applies the correct legal standard (reckless indifference under SB 1437) to the specific exculpatory facts presented in the prompt (banning weapons). Option (a) fails because yelling "drive" does not meet the high bar for specific intent to kill. Option (b) fails because SB 1437 expressly abolished strict liability for non-killer accomplices. Option (e) fails because it invents a categorical rule of lenity exemption that does not exist. Option (c) is factually tempting but legally incorrect under SB 1437, which overrides common law agency theory; however, (c) lacks an absolute locking word to make its falsehood explicitly categorical.

Falsifiable claim per distractor:
- (a): "legally constitutes aiding and abetting the homicide with the specific intent to kill" — wrong because commanding a driver to flee is, at most, recklessness, not specific intent to kill.
- (b): "is strictly liable" — wrong because SB 1437 explicitly abolished strict liability for non-killer accomplices in felony murder, requiring reckless indifference instead.
- (c): "satisfying the agency theory" — wrong because SB 1437 statutorily overrides the common law agency theory with individualized mens rea requirements (though it lacks an absolute word).
- (e): "can never be deemed a major participant" — wrong because non-driving accomplices can be major participants if they satisfy the requisite statutory factors.

Recommended fix: Add an absolute word to (c) to firmly lock the falsifiable proposition. Change (c) to: "Yes, because by jumping into the getaway car, she automatically satisfies the agency theory of homicide liability."
-->
