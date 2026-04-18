# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q13.** Assume instead that the jurisdiction follows the common-law dangerous proximity test. Is Dominic guilty of attempted murder?

(a) Yes, because tracking Elias through the scope with his finger on the trigger left him with essentially no more acts to complete the intended murderous offense. <!-- correct -->
(b) No, because he had not yet fired the weapon, meaning he had not yet come within dangerous proximity to the successful completion of the intended violent crime.
(c) Yes, because driving to the rival's house placed him close enough to the scene to satisfy the physical proximity requirement, regardless of his subsequent actions with the rifle.
(d) No, because he was unaware of the FBI's presence, meaning he did not have the requisite proximate control over the surrounding environment to successfully complete the homicide.
(e) Yes, because the dangerous proximity test only requires that the defendant's preparatory acts demonstrate a clear intent to commit a violent felony in the very near future.

**Answer:** (a)

**Explanation:** Under the common-law dangerous proximity test, a defendant must come very close to the successful completion of the crime, leaving almost no acts remaining. By tracking the target in the scope with his finger on the trigger, Dominic was in dangerous proximity to completing the murder. (b) is incorrect because the test does not require the absolute last act (firing the weapon) to be completed. (c) is incorrect because merely driving to the location would be insufficient preparation under the proximity test, which requires coming much closer to the act itself. (d) is incorrect because factual impossibility or unawareness of police intervention does not negate attempt liability if the acts themselves were sufficiently proximate. (e) is incorrect because demonstrating clear intent is insufficient under the proximity test without extreme physical proximity to the harm.

**Tags:** chapters: [17], topics: [attempt, actus reus, dangerous proximity test], difficulty: medium, cognitive: application

**Grounding:** Common-law attempt doctrine

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The question completely lacks a fact pattern. It begins with "Assume instead..." and refers to Dominic, Elias, and the FBI without introducing them or detailing what actually happened. As a standalone question, it is unanswerable.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Integrate the base fact pattern into the stem. Remove "Assume instead that" and replace it with the full scenario: "Dominic drove to his rival Elias's house, unaware the FBI was watching. Dominic set up a rifle, tracked Elias through the scope, and put his finger on the trigger before the FBI intervened. In a jurisdiction that follows the common-law dangerous proximity test, is Dominic guilty of attempted murder?"
-->

## Issue 2 — argpass-sonnet

**Q13.** Assume instead that the jurisdiction follows the common-law dangerous proximity test. Is Dominic guilty of attempted murder?

(a) Yes, because tracking Elias through the scope with his finger on the trigger left him with essentially no more acts to complete the intended murderous offense. <!-- correct -->
(b) No, because he had not yet fired the weapon, meaning he had not yet come within dangerous proximity to the successful completion of the intended violent crime.
(c) Yes, because driving to the rival's house placed him close enough to the scene to satisfy the physical proximity requirement, regardless of his subsequent actions with the rifle.
(d) No, because he was unaware of the FBI's presence, meaning he did not have the requisite proximate control over the surrounding environment to successfully complete the homicide.
(e) Yes, because the dangerous proximity test only requires that the defendant's preparatory acts demonstrate a clear intent to commit a violent felony in the very near future.

**Answer:** (a)

**Explanation:** Under the common-law dangerous proximity test, a defendant must come very close to the successful completion of the crime, leaving almost no acts remaining. By tracking the target in the scope with his finger on the trigger, Dominic was in dangerous proximity to completing the murder. (b) is incorrect because the test does not require the absolute last act (firing the weapon) to be completed. (c) is incorrect because merely driving to the location would be insufficient preparation under the proximity test, which requires coming much closer to the act itself. (d) is incorrect because factual impossibility or unawareness of police intervention does not negate attempt liability if the acts themselves were sufficiently proximate. (e) is incorrect because demonstrating clear intent is insufficient under the proximity test without extreme physical proximity to the harm.

**Tags:** chapters: [17], topics: [attempt, actus reus, dangerous proximity test], difficulty: medium, cognitive: application

**Grounding:** Common-law attempt doctrine

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under Justice Holmes's dangerous proximity test from *Peaslee* and *Rizzo*, the actus reus for attempt requires the defendant's acts to come dangerously close to success, leaving very few steps remaining. Tracking the victim with a finger on the trigger satisfies this strict standard. Dominic has essentially reached the "last act" stage, surpassing mere preparation and entering the zone of dangerous proximity where completion is imminent.
(b) Argument-for: A student might argue that the dangerous proximity test is extraordinarily strict, sometimes practically requiring the last act to be initiated before liability attaches. Since Dominic had not fired the weapon, he arguably retained the opportunity to change his mind and had not yet unleashed the deadly force. Under this view, mere aiming remains within the realm of preparation because the actual physical danger of the bullet has not materialized.
(c) Argument-for: One could argue that physical proximity to the scene is the core metric of the dangerous proximity test (as opposed to the MPC's substantial step test). By successfully driving to the rival's house and locating his target, Dominic satisfied the spatial requirements of the test. A student might conclude that arriving armed at the intended location is sufficient to cross the proximity threshold.
(d) Argument-for: The dangerous proximity test evaluates the probability of the crime's successful completion and the gravity of the potential harm. If the FBI was present and effectively controlled the situation, making success factually impossible, Dominic's actions were arguably not "dangerously proximate" to actual completion. An argument can be made that police intervention neutralized the danger, so he lacked the capacity to complete the homicide.
(e) Argument-for: Under a broader understanding of attempt law, a clear manifestation of intent coupled with a preparatory act is sufficient. A student might conflate dangerous proximity with the *res ipsa loquitur* (equivocality) test or the MPC substantial step test, arguing that the acts performed clearly demonstrate his intent and thus satisfy the requirement for attempt.

Head-to-head: Option (a) correctly applies the dangerous proximity standard, recognizing that aiming with a finger on the trigger leaves almost no acts remaining, thus satisfying the test. Option (b) fails because it asserts a legally false rule that dangerous proximity requires the weapon to be fired, but it lacks an absolute word to lock the falsifiability perfectly. Option (c) fails due to the absolute phrase "regardless of his subsequent actions," as subsequent actions are essential under a proximity analysis (mere arrival is just preparation). Option (d) invents a fake element ("proximate control") and incorrectly implies that factual impossibility negates attempt liability. Option (e) uses the absolute word "only" to incorrectly define dangerous proximity as an equivocality or intent-based test.

Falsifiable claim per distractor:
- (b): "meaning he had not yet come within dangerous proximity" (deduced strictly from "he had not yet fired") — wrong because the dangerous proximity test does not strictly require the firing of the weapon; aiming is sufficiently proximate. (Would be stronger with an absolute word).
- (c): "regardless of his subsequent actions with the rifle" — wrong because under the dangerous proximity test, actions at the scene are critical; mere arrival is almost always deemed mere preparation.
- (d): "meaning he did not have the requisite proximate control over the surrounding environment" — wrong because "proximate control" is a fabricated element, and factual impossibility (FBI presence) does not negate attempt liability.
- (e): "only requires that the defendant's preparatory acts demonstrate a clear intent" — wrong because this explicitly defines the equivocality test, not the dangerous proximity test, which requires extreme physical proximity to success.

Recommended fix: In (b), add an absolute word to lock the falsifiable claim. Change (b) to: "No, because the dangerous proximity test categorically requires the weapon to be fired, meaning he had not yet come within dangerous proximity to the successful completion of the intended violent crime."
-->
