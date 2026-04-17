# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q8.** Assume prosecutors charge Bex as an accomplice to homicide for standing watch while Cody died. Is Bex guilty as an accomplice?

(a) Guilty, because her physical presence at the door and her failure to intervene provided material assistance to Alba's lethal plan.
(b) Guilty, because the natural and probable consequences doctrine automatically transforms any minor assistance into purposeful and actionable facilitation.
(c) Not guilty, because she acted solely out of fear for her own life, establishing knowledge but not the purpose to facilitate. <!-- correct -->
(d) Not guilty, because looking through a peephole does not rise to the level of a substantial step required for accomplice liability.
(e) Not guilty, because she did not physically participate in moving Cody into the bathroom or in striking Dane with the handgun.

**Answer:** (c)

**Explanation:** (c) is correct because common law accomplice liability requires the purpose to facilitate the underlying crime; Bex acting solely out of fear for her life establishes she had knowledge of the crime but lacked the purpose that the crime succeed. (a) is wrong because material assistance satisfies only the actus reus element; she lacks the required mens rea. (b) is wrong because the natural and probable consequences doctrine applies to the scope of liability for a planned crime, not to establish the initial purposeful facilitation. (d) is wrong because "substantial step" is an attempt element, whereas mere presence plus minimal assistance can satisfy accomplice actus reus. (e) is wrong because physical participation is not required if the defendant purposefully aids as a lookout.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 18, mr-purpose-not-knowledge

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: MUST FIX. Option (c) relies on the legally flawed premise that acting under extreme fear (duress) negates the mens rea of "purpose" and reduces it to mere "knowledge." In criminal law doctrine, motive (fear) does not negate intent or purpose; a coerced actor still purposefully facilitates the crime in order to save their own life. This is precisely why duress operates as an affirmative excuse defense rather than a failure of mens rea.
3. Cross-Question Spoilers: MUST FIX. If Q8 correctly establishes that Bex is "Not guilty" because her fear negates her mens rea, she is acquitted of the prima facie case. This completely spoils Q11, which intends to test whether the common law duress-murder bar prevents her from asserting an affirmative duress defense. If she lacks the mens rea for accomplice liability, she never needs to raise the affirmative defense, mooting Q11 entirely.
Recommended fix: Remove the "purpose vs. knowledge" framework from Q8's application to Bex's fear. Rewrite Q8 to test whether Bex's actions satisfy the accomplice actus reus (making a variation of 'a' the correct answer, e.g., "Guilty of the prima facie elements, because acting as a lookout is sufficient affirmative assistance..."), and add an instruction in the prompt to "Disregard any affirmative defenses for this question."
-->

## Issue 3 — argpass-opus

**Q8.** Assume prosecutors charge Bex as an accomplice to homicide for standing watch while Cody died. Is Bex guilty as an accomplice?

(a) Guilty, because her physical presence at the door and her failure to intervene provided material assistance to Alba's lethal plan.
(b) Guilty, because the natural and probable consequences doctrine automatically transforms any minor assistance into purposeful and actionable facilitation.
(c) Not guilty, because she acted solely out of fear for her own life, establishing knowledge but not the purpose to facilitate. <!-- correct -->
(d) Not guilty, because looking through a peephole does not rise to the level of a substantial step required for accomplice liability.
(e) Not guilty, because she did not physically participate in moving Cody into the bathroom or in striking Dane with the handgun.

**Answer:** (c)

**Explanation:** (c) is correct because common law accomplice liability requires the purpose to facilitate the underlying crime; Bex acting solely out of fear for her life establishes she had knowledge of the crime but lacked the purpose that the crime succeed. (a) is wrong because material assistance satisfies only the actus reus element; she lacks the required mens rea. (b) is wrong because the natural and probable consequences doctrine applies to the scope of liability for a planned crime, not to establish the initial purposeful facilitation. (d) is wrong because "substantial step" is an attempt element, whereas mere presence plus minimal assistance can satisfy accomplice actus reus. (e) is wrong because physical participation is not required if the defendant purposefully aids as a lookout.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 18, mr-purpose-not-knowledge

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that Bex's physical presence at the door as a lookout directly enabled the crime. In many contexts, acting as a lookout is the quintessential accomplice actus reus. If she provided material assistance to the lethal plan, her conduct satisfies the objective elements of accomplice liability, leading a student to conclude she is legally guilty based on her affirmative act of assistance.
(b) Argument-for: A student might confuse the natural and probable consequences doctrine—which extends liability for foreseeable collateral crimes—with the baseline mens rea requirement for a target crime. If they believe any minor assistance in a dangerous situation "automatically" triggers liability for whatever crimes unfold, they would select this option.
(c) Argument-for: The correct option accurately states the common law mens rea rule for accomplice liability. A defendant must not merely know of the crime but must possess the purpose to facilitate it. Acting "solely out of fear for her own life" implies duress or a mere desire to survive, which negates the specific intent (purpose) that the principal succeed, rendering Bex a knowing but non-purposeful participant.
(d) Argument-for: A student could confuse the actus reus standard for attempt (substantial step) with the actus reus standard for accomplice liability. Since looking through a peephole might seem trivial compared to a "substantial step," a student applying this incorrect doctrinal test would mistakenly conclude Bex's actions were legally insufficient.
(e) Argument-for: A student might assume that accomplice liability for violent crimes requires actual physical participation or presence during the core violent act itself. Because Bex did not physically move the victim or strike anyone, a student applying an overly narrow, physical-participation requirement to "aid or abet" would choose this option.

Head-to-head: Option (c) is the definitively correct answer because it correctly applies the purpose standard for accomplice liability. However, distractors (a) and (e) fail the close-call standard. Neither contains an explicitly false legal rule; rather, they rely on implicit omissions. Option (a) states she provided material assistance, which may be factually true (actus reus), but it implicitly omits mens rea to conclude guilt. Option (e) states she did not physically participate, which is also factually true, implicitly omitting that non-physical assistance is legally sufficient. To pass the close-call standard, these distractors must explicitly lock their false legal rationales.

Falsifiable claim per distractor:
- (a): "Guilty, because her physical presence... provided material assistance" — wrong implicitly because it omits mens rea, but lacks an explicitly false legal claim. It needs an absolute trigger.
- (b): "automatically transforms any minor assistance into purposeful and actionable facilitation" — wrong because the natural and probable consequences doctrine governs the scope of liability for collateral crimes, not the initial establishment of purpose.
- (d): "substantial step required for accomplice liability" — wrong because "substantial step" is the MPC test for attempt liability, not accomplice liability.
- (e): "because she did not physically participate" — wrong implicitly because physical participation is not required, but lacks an explicitly false legal claim (fails to state physical participation is categorically required).

Recommended fix: Add absolute words to (a) and (e) to lock in explicit false legal claims. 
Edit (a) to: "Guilty, solely because her physical presence at the door and her failure to intervene provided material assistance to Alba's lethal plan."
Edit (e) to: "Not guilty, because physical participation in the core violent acts is categorically required to establish accomplice liability."
-->
