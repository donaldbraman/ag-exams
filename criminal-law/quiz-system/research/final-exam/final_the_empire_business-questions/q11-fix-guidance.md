# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q11.** The state prosecutor charges Matthew with murder for shooting Kevin. Matthew claims he acted in self-defense. Which of the following best explains why Matthew's self-defense claim will fail?

(a) Because Matthew's face was flushed and his hands were trembling, his subjective fear was empirically unreasonable compared to the objective standard of a reasonable person.
(b) Because Matthew stepped out the back door anticipating the attack, he became the initial aggressor and completely forfeited his legal right to assert self-defense.
(c) Because Kevin had a concealed 9mm handgun in his pocket, Matthew's use of a shotgun constituted an excessive and disproportionate escalation of defensive force.
(d) Because Matthew failed to fire a warning shot before pulling the trigger, he breached the common law duty to retreat before utilizing lethal defensive force.
(e) Because Kevin dropped the crowbar and was fleeing, Matthew faced no imminent threat of unlawful force at the moment he fired the fatal shotgun blast. <!-- correct -->

**Answer:** (e)

**Explanation:** The correct answer is (e). A successful claim of self-defense requires that the defendant face an *imminent* threat of unlawful force. Because Kevin had dropped his weapon, turned around, and was sprinting away, he no longer posed an imminent threat when Matthew shot him in the back. (a) is wrong because trembling hands and a flushed face indicate genuine subjective fear, and do not logically prove that his fear was objectively unreasonable. (b) is wrong because preparing to defend one's property against a known attacker does not legally make one an initial aggressor. (c) is wrong because Matthew did not know about the concealed handgun, and self-defense is evaluated based on the circumstances as they reasonably appeared to the defendant; furthermore, shooting a fleeing person is invalid regardless of what was in the person's pocket. (d) is wrong because warning shots are not required, and the duty to retreat concerns escaping safely, not firing warning shots. 

**Tags:** chapters: [11], topics: [self-defense, imminence requirement, fleeing threat], difficulty: easy, cognitive: application

**Grounding:** General Doctrine - Self-Defense (Imminence limit on defensive force)

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: FAIL. The stem is missing the factual scenario entirely. It only states that Matthew shot Kevin, but the answer options and explanation rely on specific facts (Kevin wielding and then dropping a crowbar and fleeing, Matthew stepping out the back door, Matthew's lack of knowledge of a concealed handgun) that are nowhere to be found in the prompt. A student cannot answer the question without these facts.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Insert the missing fact pattern into the question stem (e.g., detailing Kevin's initial approach with a crowbar, Matthew stepping out the back door, Kevin dropping the crowbar and fleeing, and Matthew subsequently shooting him in the back).
-->

## Issue 2 — argpass-opus

**Q11.** The state prosecutor charges Matthew with murder for shooting Kevin. Matthew claims he acted in self-defense. Which of the following best explains why Matthew's self-defense claim will fail?

(a) Because Matthew's face was flushed and his hands were trembling, his subjective fear was empirically unreasonable compared to the objective standard of a reasonable person.
(b) Because Matthew stepped out the back door anticipating the attack, he became the initial aggressor and completely forfeited his legal right to assert self-defense.
(c) Because Kevin had a concealed 9mm handgun in his pocket, Matthew's use of a shotgun constituted an excessive and disproportionate escalation of defensive force.
(d) Because Matthew failed to fire a warning shot before pulling the trigger, he breached the common law duty to retreat before utilizing lethal defensive force.
(e) Because Kevin dropped the crowbar and was fleeing, Matthew faced no imminent threat of unlawful force at the moment he fired the fatal shotgun blast. <!-- correct -->

**Answer:** (e)

**Explanation:** The correct answer is (e). A successful claim of self-defense requires that the defendant face an *imminent* threat of unlawful force. Because Kevin had dropped his weapon, turned around, and was sprinting away, he no longer posed an imminent threat when Matthew shot him in the back. (a) is wrong because trembling hands and a flushed face indicate genuine subjective fear, and do not logically prove that his fear was objectively unreasonable. (b) is wrong because preparing to defend one's property against a known attacker does not legally make one an initial aggressor. (c) is wrong because Matthew did not know about the concealed handgun, and self-defense is evaluated based on the circumstances as they reasonably appeared to the defendant; furthermore, shooting a fleeing person is invalid regardless of what was in the person's pocket. (d) is wrong because warning shots are not required, and the duty to retreat concerns escaping safely, not firing warning shots. 

**Tags:** chapters: [11], topics: [self-defense, imminence requirement, fleeing threat], difficulty: easy, cognitive: application

**Grounding:** General Doctrine - Self-Defense (Imminence limit on defensive force)

<!-- argument-pass: MUST FIX
(a) Argument-for: Option (a) suggests that Matthew's acute physiological panic—flushed face and trembling hands—prevented him from acting as an objectively reasonable person. A student could argue that if a defendant's fear stems purely from an irrational or overwhelming physical panic attack rather than a rational assessment of the threat, the objective prong of the self-defense standard fails. Under the "reasonable person" standard, subjective terror that blinds a defendant to reality makes the use of force empirically unreasonable.
(b) Argument-for: Option (b) posits that Matthew forfeited his self-defense claim under the initial aggressor doctrine by stepping out the back door to anticipate the attack. A student could argue that by voluntarily leaving a place of safety and deliberately positioning himself to confront an attacker, Matthew escalated the situation or engaged in mutual combat. Consequently, his affirmative act to meet the threat head-on legally categorized him as the initial aggressor.
(c) Argument-for: Option (c) relies on the proportionality limitation of self-defense, arguing that using a shotgun against a concealed 9mm handgun is excessive. A student could argue that self-defense strictly limits the defender to using only the amount of force necessary to repel the attack. Because a shotgun is vastly more destructive at close range than a small 9mm pistol, the defender's choice of weapon constituted a disproportionate escalation of deadly force.
(d) Argument-for: Option (d) invokes the common law duty to retreat, suggesting Matthew was required to fire a warning shot before using lethal force. A student could argue that in a minority "duty to retreat" jurisdiction, a defender must exhaust all possible non-lethal alternatives before shooting to kill. A warning shot serves as a de-escalation tactic that could force the attacker to flee, meaning the failure to fire one violates the obligation to avoid lethal force when possible.
(e) Argument-for: Option (e) correctly identifies that self-defense requires an imminent threat of unlawful deadly force. A student would recognize that when an attacker drops their weapon and flees, the threat immediately dissipates. Once the threat of harm is no longer imminent, any subsequent use of force becomes retaliatory rather than defensive, rendering Matthew's self-defense claim legally invalid under universally accepted doctrine.

Head-to-head: Option (e) applies correct legal doctrine (the imminence requirement) to logically explain why the defense fails. The distractors contain explicit false legal rules: (a) incorrectly equates physiological fear with objective unreasonableness; (b) incorrectly broadens the "initial aggressor" doctrine to include merely anticipating an attack by stepping outside; (c) incorrectly assesses proportionality using unknown facts (a "concealed" gun) and falsely frames shotgun vs. handgun as disproportionate; and (d) invents a legal duty to fire a warning shot. However, the paramount issue with the question is that the entire factual scenario (the crowbar, stepping outside, fleeing, shooting in the back) is completely missing from the question stem. Students cannot evaluate "Which of the following best explains..." without knowing what actually happened, making the question fundamentally unanswerable as drafted.

Falsifiable claim per distractor:
- (a): "his subjective fear was empirically unreasonable compared to the objective standard" — wrong because physiological signs of subjective fear do not legally negate the objective reasonableness of the belief in a threat.
- (b): "Because Matthew stepped out the back door anticipating the attack, he became the initial aggressor" — wrong because mere anticipation and positioning do not satisfy the legal requirement of an affirmative unlawful act or provocation necessary to become an initial aggressor.
- (c): "Matthew's use of a shotgun constituted an excessive and disproportionate escalation" — wrong because self-defense is evaluated based on the circumstances as they reasonably appeared to the defendant (who could not perceive a concealed weapon), and deadly force is proportionate against a deadly threat regardless of the specific firearm used.
- (d): "failed to fire a warning shot... he breached the common law duty to retreat" — wrong because the duty to retreat requires safe physical withdrawal, not firing a warning shot (which many jurisdictions treat as an unjustified use of deadly force itself).

Recommended fix: Add the missing fact pattern to the question stem. E.g., "Matthew, inside his home, saw Kevin approaching the back door with a crowbar. Anticipating an attack, Matthew grabbed his shotgun and stepped out the back door. Upon seeing the shotgun, Kevin dropped the crowbar, turned, and sprinted away. Matthew, without warning, fired the shotgun, killing Kevin by shooting him in the back. It was later discovered Kevin had a concealed 9mm handgun in his pocket."
-->
