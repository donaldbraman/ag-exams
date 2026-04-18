# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q9.** Assume Dominic is charged with intentional murder for Victor's death and asserts a self-defense claim, arguing that Victor lunged at him with a lethal weapon. Will Dominic be permitted to claim self-defense?

(a) Yes, because Victor escalated the physical encounter by introducing a deadly weapon into the conflict, which restores Dominic's right to use lethal force in response.
(b) Yes, because Dominic had an objective and subjectively reasonable fear of imminent death or great bodily harm when Victor lunged at him with the knife.
(c) No, because Dominic failed to safely retreat from the restaurant premises before using deadly force against Victor, strictly violating the traditional duty to retreat.
(d) No, because Dominic is completely barred from claiming self-defense as the initial aggressor who provoked the deadly conflict by pulling a gun to rob Victor. <!-- correct -->
(e) No, because the affirmative defense of self-defense is categorically unavailable as a matter of law to members of an organized and violent criminal enterprise.

**Answer:** (d)

**Explanation:** A defendant who initiates a deadly conflict or provokes the encounter with the intent to cause harm loses the right to claim self-defense. By pulling a gun to rob Victor, Dominic became the initial aggressor. Even though Victor escalated the encounter by lunging with a knife, Dominic's status as the initial armed aggressor completely bars his self-defense claim. (a) is wrong because an initial aggressor cannot regain the right to self-defense unless they clearly communicate withdrawal, which Dominic did not do. (b) is wrong because an objective fear of death does not legally restore the defense to an initial aggressor. (c) is wrong because the initial aggressor bar strictly precludes the defense before the duty to retreat is even analyzed. (e) is wrong because gang membership does not categorically strip a person of self-defense rights in unrelated encounters.

**Tags:** chapters: [22], topics: [self-defense, initial-aggressor, duty-to-retreat], difficulty: easy, cognitive: application

**Grounding:** Chapter 22, Initial Aggressor Bar

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might choose this option relying on the escalation exception to the initial aggressor rule. If an initial aggressor uses non-deadly force and the victim escalates to deadly force, the initial aggressor regains the right to self-defense. If the student incorrectly views Victor's lunge with a knife as the first introduction of a deadly weapon, they could argue that Victor's escalation legally restored Dominic's right to use lethal force.
(b) Argument-for: The core elements of any self-defense claim are an honest and reasonable belief in the imminent threat of death or great bodily harm. When Victor lunged at Dominic with a knife, Dominic possessed this subjective and objective fear. A student could argue that satisfying these foundational elements is legally sufficient to justify the use of lethal force, concluding that his fear validates the defense regardless of how the conflict began.
(c) Argument-for: Even if a defendant has a reasonable fear of death, jurisdictions following the traditional duty to retreat require the defendant to step back if it can be done with complete safety. A student might believe that Dominic had an avenue of safe retreat from the restaurant premises. Therefore, they could argue that his failure to retreat operates as an independent and strict bar to his self-defense claim.
(d) Argument-for: This option directly applies the initial aggressor doctrine. By pulling a gun to rob Victor, Dominic initiated the encounter with deadly force. Because he provoked the conflict and never clearly communicated withdrawal, he is completely barred as a matter of law from asserting self-defense, regardless of Victor's subsequent actions. This accurately identifies the dispositive legal bar to Dominic's claim.
(e) Argument-for: A student might apply an overly broad interpretation of equitable doctrines like "clean hands" or assume a statutory bar applies to gang members. They could argue that the law categorically denies affirmative defenses to individuals actively engaged in a violent criminal enterprise, reasoning that public policy strictly prevents organized criminals from justifying their violence.

Head-to-head: Option (d) is clearly the strongest argument because it applies the dispositive initial aggressor rule: one who initiates a conflict with deadly force cannot claim self-defense without first withdrawing. Option (a) is factually and legally flawed; Dominic initiated with deadly force, so Victor didn't "introduce" a deadly weapon, and Dominic's right isn't restored. Option (b) states the subjective/objective fear elements but relies on an implicit omission of the initial aggressor bar, lacking an explicit false legal rule. Option (c) relies on the duty to retreat, but the initial aggressor bar precludes the defense before retreat is even reached. Option (e) invents a non-existent categorical rule stripping self-defense rights based on gang membership. Option (b) fails the close-call standard because it lacks an explicitly false, absolute legal claim.

Falsifiable claim per distractor:
- (a): "restores Dominic's right to use lethal force in response" — wrong because Dominic was the initial deadly aggressor, so the right is not restored without withdrawal.
- (b): "Yes, because Dominic had an objective and subjectively reasonable fear..." — wrong in its legal conclusion given the facts, but operates via an implicit omission of the initial aggressor doctrine rather than stating an explicitly false, absolute legal rule.
- (c): "strictly violating the traditional duty to retreat" — wrong because the initial aggressor doctrine bars the defense outright (making duty to retreat legally moot), and retreat is not universally required.
- (e): "categorically unavailable as a matter of law to members of an organized and violent criminal enterprise" — wrong because no jurisdiction categorically strips self-defense rights solely for gang membership in unrelated encounters.

Recommended fix: Revise (b) to contain an absolute false legal claim. For example: "(b) Yes, because an objective and subjectively reasonable fear of imminent death categorically overrides the initial aggressor bar."
-->

## Issue 3 — argpass-opus

**Q9.** Assume Dominic is charged with intentional murder for Victor's death and asserts a self-defense claim, arguing that Victor lunged at him with a lethal weapon. Will Dominic be permitted to claim self-defense?

(a) Yes, because Victor escalated the physical encounter by introducing a deadly weapon into the conflict, which restores Dominic's right to use lethal force in response.
(b) Yes, because Dominic had an objective and subjectively reasonable fear of imminent death or great bodily harm when Victor lunged at him with the knife.
(c) No, because Dominic failed to safely retreat from the restaurant premises before using deadly force against Victor, strictly violating the traditional duty to retreat.
(d) No, because Dominic is completely barred from claiming self-defense as the initial aggressor who provoked the deadly conflict by pulling a gun to rob Victor. <!-- correct -->
(e) No, because the affirmative defense of self-defense is categorically unavailable as a matter of law to members of an organized and violent criminal enterprise.

**Answer:** (d)

**Explanation:** A defendant who initiates a deadly conflict or provokes the encounter with the intent to cause harm loses the right to claim self-defense. By pulling a gun to rob Victor, Dominic became the initial aggressor. Even though Victor escalated the encounter by lunging with a knife, Dominic's status as the initial armed aggressor completely bars his self-defense claim. (a) is wrong because an initial aggressor cannot regain the right to self-defense unless they clearly communicate withdrawal, which Dominic did not do. (b) is wrong because an objective fear of death does not legally restore the defense to an initial aggressor. (c) is wrong because the initial aggressor bar strictly precludes the defense before the duty to retreat is even analyzed. (e) is wrong because gang membership does not categorically strip a person of self-defense rights in unrelated encounters.

**Tags:** chapters: [22], topics: [self-defense, initial-aggressor, duty-to-retreat], difficulty: easy, cognitive: application

**Grounding:** Chapter 22, Initial Aggressor Bar

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might select this option by attempting to apply the escalation exception to the initial aggressor rule. General self-defense doctrine allows an initial non-deadly aggressor to regain the right to use defensive force if the victim escalates the conflict to a deadly level. A student could mistakenly interpret Victor's use of a knife as a legal escalation. By focusing solely on Victor's lethal weapon, the student might falsely conclude that Dominic's right to self-defense was fully restored, justifying his lethal response.
(b) Argument-for: A student could argue that the foundational elements of any self-defense claim are an objectively and subjectively reasonable fear of imminent death or great bodily harm. Because Victor lunged at him with a lethal weapon, Dominic genuinely feared for his life in that exact moment. A student might believe this immediate, reasonable fear is legally sufficient to grant the defense. They might erroneously conclude that the presence of an imminent deadly threat outweighs or cures any prior provocation by the defendant.
(c) Argument-for: A student studying duty-to-retreat jurisdictions might focus on the location of the altercation to determine the outcome. Because the conflict happened in a restaurant, which is a public place rather than the defendant's home, the student might conclude that Dominic was legally required to attempt a safe retreat. Since Dominic used deadly force without retreating, a student could argue this constitutes a strict violation of the traditional duty to retreat, leading to the correct "No" conclusion but through the wrong legal mechanism.
(d) Argument-for: A student correctly applying the initial aggressor rule would identify that Dominic provoked the deadly conflict by initiating an armed robbery. The law dictates that an individual who starts a deadly confrontation loses the right to claim self-defense. Because Dominic was the initial deadly aggressor, he is completely barred from asserting the defense unless he effectively withdrew from the encounter. Since he did not communicate withdrawal, his claim is legally precluded, making this the correct answer.
(e) Argument-for: A student might erroneously believe that being a member of an organized criminal enterprise globally strips an individual of equitable or affirmative defenses like self-defense. They could draw false analogies to statutes targeting organized crime or the "unclean hands" doctrine in equity. The argument would assert that criminals engaged in violent organized crime forfeit their right to self-defense when participating in criminal activities, relying on a fabricated categorical rule rather than the specific conduct in the immediate encounter.

Head-to-head:
Option (d) correctly identifies the core legal doctrine: an initial aggressor who provokes a deadly conflict completely loses the right to self-defense. Option (a) incorrectly claims Victor's response "restores" Dominic's rights, legally and factually ignoring that Dominic initiated the deadly threat first. Option (b) relies on the presence of reasonable fear but fails to account for the initial aggressor bar, though it lacks an absolute word to make its legal proposition strictly falsifiable. Option (c) wrongly applies the duty to retreat as the primary bar, but also lacks an absolute lock to make it clearly falsifiable across all jurisdictions. Option (e) successfully deploys an absolute lock on a fabricated, categorical rule about criminal enterprise members.

Falsifiable claim per distractor:
- (a): "which restores Dominic's right to use lethal force in response" — wrong because Dominic initiated the deadly conflict, so Victor fighting back did not legally restore Dominic's self-defense rights.
- (b): "Yes, because Dominic had an objective and subjectively reasonable fear" — wrong in outcome, but relies on an implicit omission of the initial aggressor bar rather than an explicit, locked false legal claim.
- (c): "strictly violating the traditional duty to retreat" — wrong reasoning since the initial aggressor bar applies first, but fails the close-call standard by lacking an absolute word stating that retreat is universally required in all jurisdictions.
- (e): "categorically unavailable as a matter of law to members of an organized and violent criminal enterprise" — wrong because there is no such categorical legal exception stripping gang members of self-defense rights.

Recommended fix: Add absolute modifiers to distractors (b) and (c) to pass the close-call standard. For (b), change to: "Yes, solely because Dominic had an objective and subjectively reasonable fear of imminent death when Victor lunged at him with the knife." For (c), change to: "No, because the law categorically requires a defendant to safely retreat from public premises before using deadly force in every jurisdiction."
-->
