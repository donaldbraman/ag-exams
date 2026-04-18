# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q9.** Silas is charged with the attempted murder of the pedestrian he struck while firing blindly down the alley. Under prevailing specific intent requirements for attempt, is he guilty?

(a) Yes, because his reckless disregard for human life satisfies the specific intent requirement for attempted murder.
(b) No, because attempt requires the specific purpose to cause the death of the victim, and Silas fired blindly without aiming at anyone. <!-- correct -->
(c) Yes, under the kill-zone theory, because firing a gun in an alley creates a zone of fatal harm that transfers intent to anyone within it.
(d) No, because the pedestrian was not killed, and attempted murder requires actual severe injury to demonstrate the required intent.
(e) Yes, because the transferred intent doctrine automatically transfers his specific intent to kill Dexter to the pedestrian he actually struck.

**Answer:** (b)

**Explanation:** (b) is correct. Attempt requires the specific intent (purpose) to cause the result element of the target offense. Even if a completed murder can be committed via recklessness (depraved heart), attempted murder requires a specific purpose to kill. Silas fired blindly to deter pursuit, lacking this purpose. (a) is incorrect because recklessness is insufficient for attempt. (c) is incorrect because the kill-zone theory requires intent to kill *everyone* in a specific zone to ensure a primary target's death, which doesn't apply to blind firing. (d) is incorrect because attempt does not require any actual injury. (e) is incorrect because transferred intent generally applies to completed crimes, not inchoate attempts where specific intent as to the victim is required.

**Tags:** chapters: [17], topics: [attempt, mens-rea, specific-intent, kill-zone], difficulty: hard, cognitive: application

**Grounding:** Chapter 17: Attempts > Refinements > Prima Facie Element 1 & 2: Mens Rea > The Specific Intent Requirement

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could point to the fact that for the completed crime of murder, extreme reckless disregard for human life (depraved heart) satisfies the mens rea. They could argue that attempt tracks the mens rea of the target offense, concluding that extreme recklessness is therefore legally sufficient to satisfy the mens rea for attempted murder. Thus, they would conclude Silas is guilty based on his highly dangerous blind firing.
(b) Argument-for: Attempted murder requires the specific intent—or purpose—to cause the death of another human being, regardless of whether the completed crime of murder could be satisfied by a lesser mens rea like recklessness. Because Silas fired blindly without aiming at anyone, he merely acted with reckless disregard, completely lacking the specific purpose to kill required for an attempt conviction. Thus, he is not guilty of attempted murder.
(c) Argument-for: The kill-zone theory holds that when a defendant uses lethal force designed to ensure the death of everyone in a particular area, they possess concurrent intent to kill anyone in that zone. A student might argue that firing blindly down an enclosed alley inherently creates exactly this kind of fatal zone. Consequently, they would conclude intent is legally transferred or concurrently applied to anyone within the alley, rendering Silas guilty of attempt for hitting the pedestrian.
(d) Argument-for: A student might argue that because specific intent is difficult to prove when a defendant fires blindly, the law requires some objective manifestation of that intent to prevent punishing mere recklessness as attempted murder. Under this view, only an actual severe injury to the pedestrian would legally suffice to demonstrate the specific intent necessary to elevate the blind firing to an attempt. Since the pedestrian wasn't killed, they would conclude the required intent cannot be established without severe injury.
(e) Argument-for: The doctrine of transferred intent provides that a defendant's intent to harm one victim transfers to the actual victim harmed. A student might assume that Silas was shooting at a specific pursuer (named Dexter in this option) and argue that this specific intent automatically transfers to the pedestrian he struck. They would conclude this perfectly satisfies the specific intent mens rea for the attempted murder of the pedestrian.

Head-to-head: Option (b) correctly states the universally tested rule: attempt requires the specific purpose to complete the target crime. Option (a) fails because recklessness categorically never satisfies the specific intent for attempt. Option (c) is false because the kill-zone theory establishes concurrent intent based on targeting a primary victim, not a blanket transfer of intent merely from creating a dangerous zone while firing blindly. Option (d) fails because inchoate crimes like attempt categorically do not require actual completed injury to prove intent. Option (e) relies on the legally false claim that transferred intent automatically applies to attempts, but it also references a phantom character ("Dexter") completely absent from the stem.

Falsifiable claim per distractor:
- (a): "reckless disregard for human life satisfies the specific intent requirement" — wrong because attempt always requires specific intent (purpose), never mere recklessness.
- (c): "creates a zone of fatal harm that transfers intent to anyone within it" — wrong because the kill-zone theory requires a primary target and establishes concurrent intent, not a transfer of intent to anyone in a blindly fired area.
- (d): "attempted murder requires actual severe injury" — wrong because attempt is an inchoate crime that categorically never requires actual injury.
- (e): "automatically transfers his specific intent to kill Dexter to the pedestrian" — wrong because transferred intent generally does not apply to inchoate attempts to transfer intent to an unintended victim, and "Dexter" is an undefined phantom fact.

Recommended fix: Change "Dexter" in option (e) to "a pursuer" to align with the explanation and remove the phantom fact from the option.
-->

## Issue 3 — argpass-opus

**Q9.** Silas is charged with the attempted murder of the pedestrian he struck while firing blindly down the alley. Under prevailing specific intent requirements for attempt, is he guilty?

(a) Yes, because his reckless disregard for human life satisfies the specific intent requirement for attempted murder.
(b) No, because attempt requires the specific purpose to cause the death of the victim, and Silas fired blindly without aiming at anyone. <!-- correct -->
(c) Yes, under the kill-zone theory, because firing a gun in an alley creates a zone of fatal harm that transfers intent to anyone within it.
(d) No, because the pedestrian was not killed, and attempted murder requires actual severe injury to demonstrate the required intent.
(e) Yes, because the transferred intent doctrine automatically transfers his specific intent to kill Dexter to the pedestrian he actually struck.

**Answer:** (b)

**Explanation:** (b) is correct. Attempt requires the specific intent (purpose) to cause the result element of the target offense. Even if a completed murder can be committed via recklessness (depraved heart), attempted murder requires a specific purpose to kill. Silas fired blindly to deter pursuit, lacking this purpose. (a) is incorrect because recklessness is insufficient for attempt. (c) is incorrect because the kill-zone theory requires intent to kill *everyone* in a specific zone to ensure a primary target's death, which doesn't apply to blind firing. (d) is incorrect because attempt does not require any actual injury. (e) is incorrect because transferred intent generally applies to completed crimes, not inchoate attempts where specific intent as to the victim is required.

**Tags:** chapters: [17], topics: [attempt, mens-rea, specific-intent, kill-zone], difficulty: hard, cognitive: application

**Grounding:** Chapter 17: Attempts > Refinements > Prima Facie Element 1 & 2: Mens Rea > The Specific Intent Requirement

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that in some jurisdictions, "depraved heart" or extreme recklessness suffices for the mens rea of murder. Because the target crime can be satisfied by recklessness, one might argue that attempted murder would logically allow the same mens rea. Therefore, Silas's reckless disregard for human life when firing down the alley satisfies the intent requirement.
(b) Argument-for: This is the correct rule. Attempt is a specific intent crime that requires the explicit purpose to commit the target offense, even if the completed offense (like murder) can be committed with a lesser mens rea such as recklessness. Because Silas fired blindly without aiming, he lacked the specific purpose to kill the pedestrian, making him not guilty of attempted murder.
(c) Argument-for: The kill-zone theory allows an inference of specific intent to kill when a defendant uses lethal force designed to kill everyone in an area. A student could argue that firing a gun blindly down a narrow alley inherently creates a "kill zone," transferring or inferring intent to anyone caught within it. Thus, striking the pedestrian falls within this zone, satisfying the specific intent requirement.
(d) Argument-for: A student could argue that without a confession, specific intent must be inferred from the surrounding circumstances and the severity of the act. If Silas was firing blindly, the only way to objectively demonstrate the specific intent to kill rather than mere recklessness or intent to frighten would be if the shot caused actual severe injury. Therefore, without severe injury, intent cannot be proven.
(e) Argument-for: Under the doctrine of transferred intent, if a defendant intends to kill one person but accidentally strikes another, the intent "transfers." Assuming Silas was shooting at a pursuer (Dexter), a student could argue that his specific intent to kill Dexter automatically transfers to the pedestrian he actually struck, fulfilling the mens rea for attempted murder.

Head-to-head: 
Option (b) correctly states the universally accepted rule that attempt requires the specific purpose to commit the target offense. Option (a) incorrectly equates reckless disregard with specific intent. Option (c) misstates the kill-zone theory, which requires the creation of a zone to ensure a primary target's death, not merely firing blindly. Option (d) invents a false requirement that attempted murder needs "actual severe injury." Option (e) incorrectly applies transferred intent to an inchoate attempt and improperly introduces a character ("Dexter") absent from the prompt. Because the prompt is missing vital factual context (Dexter and the pursuit) that the explanation and option (e) rely upon, the question is structurally broken.

Falsifiable claim per distractor:
- (a): "reckless disregard for human life satisfies the specific intent requirement for attempted murder" — wrong because attempt universally requires purpose (specific intent) to commit the target crime, not recklessness.
- (c): "firing a gun in an alley creates a zone of fatal harm that transfers intent to anyone within it" — wrong because the kill-zone theory requires an intent to kill a primary target and everyone around them, not merely firing blindly.
- (d): "attempted murder requires actual severe injury to demonstrate the required intent" — wrong because attempt requires only an overt act and intent; no actual injury is ever strictly required.
- (e): "transferred intent doctrine automatically transfers his specific intent to kill Dexter" — wrong because transferred intent generally does not apply to attempt, and Dexter is completely absent from the fact pattern.

Recommended fix: Add the missing factual context to the prompt so option (e) and the explanation make sense (e.g., "Silas, while fleeing from his rival Dexter, fired blindly down the alley to deter pursuit, but struck a pedestrian. Silas is charged...").
-->
