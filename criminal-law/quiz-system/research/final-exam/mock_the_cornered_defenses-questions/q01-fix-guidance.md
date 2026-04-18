# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — edge-case

**Q1.** Assume Artie is charged with the theft of the nitrogen tanker. Which of the following is the most accurate analysis of his affirmative defenses under traditional common law principles?

(a) He may claim duress because he faced an imminent threat of death, and necessity because averting the explosion clearly outweighed the property theft.
(b) He may claim duress, but not necessity, because the choice-of-evils defense is categorically unavailable when the emergency is created by the defendant's own enterprise.
(c) He may claim necessity, but not duress, because the threat of death from Leo was conditional on his refusal to act rather than a physical compulsion.
(d) He is barred from both defenses because his voluntary participation in a criminal conspiracy negates the requirement that he had no reasonable legal alternative available.
(e) He may claim neither defense because the harm of stealing the tanker was immediate, whereas the threat of the reactor explosion was speculative and distant.

**Answer:** (a)

**Explanation:** Artie can invoke both defenses. Duress requires an imminent threat of death or serious bodily injury that a reasonable person could not resist; Leo explicitly threatened him with immediate death (gun to the head). Necessity (choice of evils) requires choosing a lesser harm to avert a greater, imminent harm; stealing a tanker (property crime) clearly outweighs the destruction of a residential block and multiple lives. (b) is incorrect because the common law "at fault" bar applies to the emergency's creation, but Artie did not cause the mechanical failure. (c) is incorrect because a conditional threat ("do this or die") is the precise definition of duress. (d) is incorrect because general participation in a conspiracy does not automatically extinguish these defenses for independent, supervening emergencies. (e) is incorrect because a twelve-minute countdown to a chemical detonation is sufficiently imminent under necessity doctrine.

**Tags:** chapters: [21], topics: [necessity, duress, choice of evils, imminence], difficulty: medium, cognitive: application

**Grounding:** Chapter 21: necessity-proportionality-standard, duress-threat-threshold

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Artie's voluntary participation in an illicit drug manufacturing operation with armed cartel members (Fact 1) inadvertently triggers the "clean hands" / "at-fault" limitations for both defenses.
2. Cross-Doctrine Clashes: At common law, the duress defense is unavailable if the defendant voluntarily joined a criminal organization or placed themselves in a situation where coercion was probable. Similarly, the necessity defense is generally unavailable if the defendant is at fault in creating the emergency (and courts routinely hold that running an illicit, unregulated chemical drug lab constitutes fault for any resulting chemical fires/explosions). Because of this, choice (a) is likely incorrect under common law, and choice (d) or (b) actually represents the stronger doctrinal outcome. 
3. Cross-Question Spoilers: pass
Recommended fix: If the goal is strictly to test the imminence and proportionality elements, you must neutralize the "at-fault" trap. You can do this by altering Fact 1 to make Artie a kidnapped/coerced chemist rather than a voluntary cartel partner, or by explicitly instructing the student in the Q1 stem: "Assume for this question that the jurisdiction does not bar defenses based on the defendant's prior fault in joining the enterprise."
-->

## Issue 2 — argpass-sonnet

**Q1.** Assume Artie is charged with the theft of the nitrogen tanker. Which of the following is the most accurate analysis of his affirmative defenses under traditional common law principles?

(a) He may claim duress because he faced an imminent threat of death, and necessity because averting the explosion clearly outweighed the property theft. <!-- correct -->
(b) He may claim duress, but not necessity, because the choice-of-evils defense is categorically unavailable when the emergency is created by the defendant's own enterprise.
(c) He may claim necessity, but not duress, because the threat of death from Leo was conditional on his refusal to act rather than a physical compulsion.
(d) He is barred from both defenses because his voluntary participation in a criminal conspiracy negates the requirement that he had no reasonable legal alternative available.
(e) He may claim neither defense because the harm of stealing the tanker was immediate, whereas the threat of the reactor explosion was speculative and distant.

**Answer:** (a)

**Explanation:** Artie can invoke both defenses. Duress requires an imminent threat of death or serious bodily injury that a reasonable person could not resist; Leo explicitly threatened him with immediate death (gun to the head). Necessity (choice of evils) requires choosing a lesser harm to avert a greater, imminent harm; stealing a tanker (property crime) clearly outweighs the destruction of a residential block and multiple lives. (b) is incorrect because the common law "at fault" bar applies to the emergency's creation, but Artie did not cause the mechanical failure. (c) is incorrect because a conditional threat ("do this or die") is the precise definition of duress. (d) is incorrect because general participation in a conspiracy does not automatically extinguish these defenses for independent, supervening emergencies. (e) is incorrect because a twelve-minute countdown to a chemical detonation is sufficiently imminent under necessity doctrine.

**Tags:** chapters: [21], topics: [necessity, duress, choice of evils, imminence], difficulty: medium, cognitive: application

**Grounding:** Chapter 21: necessity-proportionality-standard, duress-threat-threshold

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Option (a) accurately tracks the common law requirements for both defenses. Duress applies because Artie faced an imminent threat of death or serious bodily injury (a gun to his head) that overcame his will. Necessity applies because the objective harm of the tanker theft is vastly outweighed by the impending destruction of a residential block by a reactor explosion. Finding both defenses applicable is legally sound when the distinct elements for each are met.
(b) Argument-for: Under the common law, the necessity defense is generally barred if the defendant is at fault for creating the exigent circumstances. Option (b) correctly identifies this "clean hands" limitation, reasoning that since Artie was part of the criminal enterprise operating the reactor, his involvement in the enterprise itself spawned the emergency. Therefore, necessity is categorically unavailable, leaving duress as his only recourse.
(c) Argument-for: This option draws a strict line between necessity and duress. Necessity requires an objective choice of evils, which is present here. However, under a strict reading of the common law, one could argue that true duress requires an overwhelming of the defendant's physical will (compulsion), whereas a conditional threat ("do this or else") leaves the defendant with a choice, thus negating true duress and leaving only the necessity defense.
(d) Argument-for: Affirmative defenses like necessity and duress are traditionally unavailable to defendants who willingly place themselves in unlawful situations where coercion or emergencies are foreseeable. Option (d) captures this limitation, arguing that Artie’s voluntary participation in a criminal conspiracy inherently negates his ability to claim he had no reasonable legal alternative. Having joined the conspiracy, he assumes the risk of its emergencies.
(e) Argument-for: Both duress and necessity strictly require the threatened harm to be imminent and immediate. Option (e) points out that stealing the tanker is a present, immediate act of harm, whereas a twelve-minute countdown is prospective. During those twelve minutes, intervening events could occur, rendering the explosion threat legally speculative and distant. Thus, neither defense is available.

Head-to-head: Option (a) correctly applies the common law tests for both defenses. Option (b) is a strong distractor but asserts that necessity is "categorically" unavailable due to enterprise creation, whereas the common law at-fault bar requires the defendant to be at fault for creating the *specific emergency*, not just the enterprise. Option (c) wrongly claims duress requires "physical compulsion," conflating the lack of a voluntary act with the coercion of a conditional threat. Option (d) asserts that voluntary participation in a conspiracy negates the specific requirement of lacking reasonable legal alternatives; however, to be strictly falsifiable, it should include an absolute word to clarify that general participation automatically bars the defense. Option (e) relies on the factually and legally false claim that a twelve-minute countdown is "speculative and distant," contradicting standard imminence doctrine.

Falsifiable claim per distractor:
- (b): "the choice-of-evils defense is categorically unavailable when the emergency is created by the defendant's own enterprise" — wrong because the at-fault bar applies to causing the specific emergency, not merely participating in the enterprise.
- (c): "rather than a physical compulsion" — wrong because duress applies precisely to conditional threats; physical compulsion negates the actus reus entirely rather than acting as a defense.
- (d): "his voluntary participation in a criminal conspiracy negates the requirement" — lacks an absolute word to strictly lock the falsifiability; general participation does not completely bar the defense for independent supervening emergencies. 
- (e): "the threat of the reactor explosion was speculative and distant" — wrong because a defined twelve-minute countdown to an explosion is legally imminent, not distant.

Recommended fix: In option (d), change "negates the requirement" to "automatically negates the requirement".
-->

## Issue 3 — argpass-opus

**Q1.** Assume Artie is charged with the theft of the nitrogen tanker. Which of the following is the most accurate analysis of his affirmative defenses under traditional common law principles?

(a) He may claim duress because he faced an imminent threat of death, and necessity because averting the explosion clearly outweighed the property theft. <!-- correct -->
(b) He may claim duress, but not necessity, because the choice-of-evils defense is categorically unavailable when the emergency is created by the defendant's own enterprise.
(c) He may claim necessity, but not duress, because the threat of death from Leo was conditional on his refusal to act rather than a physical compulsion.
(d) He is barred from both defenses because his voluntary participation in a criminal conspiracy negates the requirement that he had no reasonable legal alternative available.
(e) He may claim neither defense because the harm of stealing the tanker was immediate, whereas the threat of the reactor explosion was speculative and distant.

**Answer:** (a)

**Explanation:** Artie can invoke both defenses. Duress requires an imminent threat of death or serious bodily injury that a reasonable person could not resist; Leo explicitly threatened him with immediate death (gun to the head). Necessity (choice of evils) requires choosing a lesser harm to avert a greater, imminent harm; stealing a tanker (property crime) clearly outweighs the destruction of a residential block and multiple lives. (b) is incorrect because the common law "at fault" bar applies to the emergency's creation, but Artie did not cause the mechanical failure. (c) is incorrect because a conditional threat ("do this or die") is the precise definition of duress. (d) is incorrect because general participation in a conspiracy does not automatically extinguish these defenses for independent, supervening emergencies. (e) is incorrect because a twelve-minute countdown to a chemical detonation is sufficiently imminent under necessity doctrine.

**Tags:** chapters: [21], topics: [necessity, duress, choice of evils, imminence], difficulty: medium, cognitive: application

**Grounding:** Chapter 21: necessity-proportionality-standard, duress-threat-threshold

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under traditional common law, duress applies when a defendant acts under an imminent threat of death or serious bodily harm. Leo's explicit threat with a gun to the head perfectly satisfies this requirement. Necessity requires choosing a lesser evil to prevent a greater, imminent harm. Averting a catastrophic reactor explosion that threatens a residential block clearly outweighs the property crime of stealing a tanker. Thus, Artie can plausibly claim both affirmative defenses.
(b) Argument-for: A student could argue that while duress fits the human threat, necessity is barred by the "clean hands" or "at-fault" exception. Under common law, if a defendant is at fault for creating the emergency, the choice-of-evils defense may be restricted. Because Artie was part of the enterprise that led to the reactor emergency, a student could argue the defense is categorically unavailable to him, barring the necessity claim.
(c) Argument-for: Necessity clearly applies to stealing the tanker to prevent a massive explosion. However, a student might argue that true common-law duress requires present physical compulsion that overrides the defendant's volition entirely. Because Leo merely issued a conditional threat ("do this or die") and left Artie to voluntarily perform the physical act of theft, a student could incorrectly argue this constitutes a choice of evils (necessity) rather than the physical coercion required for a duress defense.
(d) Argument-for: Both necessity and duress generally require that the defendant not have recklessly placed himself in a situation where coercion or emergencies were probable. A student could argue that by voluntarily participating in a criminal conspiracy, Artie forfeited these defenses. His illicit involvement arguably taints his actions and negates the requirement that he was an innocent actor with no reasonable legal alternatives available, thereby barring both defenses.
(e) Argument-for: Common law strictly requires that the threat of harm in both duress and necessity be immediately impending. A student could argue that while the theft was an immediate, completed crime, the reactor explosion was still a speculative future event based on a 12-minute countdown. Because intervening events could potentially prevent the explosion during those 12 minutes, the harm was too distant to legally justify the immediate commission of a felony.

Head-to-head: 
Option (a) correctly synthesizes traditional doctrine, accurately mapping duress to the imminent human threat and necessity to the averting of the reactor explosion. Distractor (b) misapplies the at-fault bar; while creating the *specific emergency* can bar necessity, mere participation in an enterprise does not make the defense categorically unavailable. Distractor (c) relies on a fundamental misunderstanding of duress, falsely equating it with physical compulsion (which negates actus reus) rather than acknowledging that conditional threats are the exact basis of duress. Distractor (d) claims that voluntary participation in a conspiracy generally negates the lack of alternatives, but common law requires reckless placement in the *specific* coercive situation. Distractor (e) mischaracterizes a 12-minute countdown to a catastrophic explosion as "speculative and distant," contradicting standard imminence doctrine where 12 minutes to a detonation is universally deemed imminent.

Falsifiable claim per distractor:
- (b): "the choice-of-evils defense is categorically unavailable when the emergency is created by the defendant's own enterprise" — wrong because fault in necessity doctrine applies to creating the specific emergency, not categorical preclusion simply due to enterprise involvement.
- (c): "conditional on his refusal to act rather than a physical compulsion" — wrong because conditional threats ("do this or die") are the precise definition of duress, whereas physical compulsion negates the voluntary act entirely.
- (d): "his voluntary participation in a criminal conspiracy negates the requirement" — wrong because generalized participation in a conspiracy does not automatically extinguish defenses for independent, supervening emergencies.
- (e): "the threat of the reactor explosion was speculative and distant" — wrong because a twelve-minute countdown to a detonation legally establishes imminence, not a speculative/distant threat.

Recommended fix: In (d), modify the phrase to explicitly lock the absolute legal claim: change "negates the requirement" to "automatically negates the requirement".
-->
