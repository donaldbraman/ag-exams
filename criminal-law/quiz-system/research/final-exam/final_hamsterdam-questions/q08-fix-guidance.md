# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q8.** Assume the jurisdiction recognizes imperfect self-defense. If the jury finds Xavier genuinely feared Yasmin was about to shoot him, but that his fear was objectively unreasonable, what is the effect on his liability?

(a) His honest belief negates the malice element of murder, reducing the charge to voluntary manslaughter. <!-- correct -->
(b) His unreasonable belief completely invalidates his justification defense, making him guilty of first-degree murder.
(c) His honest belief satisfies the subjective prong of perfect self-defense, resulting in a full acquittal.
(d) His unreasonable belief demonstrates extreme recklessness, reducing the charge to involuntary manslaughter.
(e) His honest belief mitigates his culpability only at the sentencing phase, leaving a second-degree murder conviction intact.

**Answer:** (a)

**Explanation:** Imperfect self-defense applies when a defendant honestly but unreasonably believes that deadly force is necessary. In jurisdictions that recognize it (like California), this genuine belief negates the malice required for murder, reducing the homicide to voluntary manslaughter. (b) describes the rule in all-or-nothing jurisdictions that do not recognize imperfect self-defense, contradicting the prompt's assumption. (c) is wrong because perfect self-defense requires both an honest AND an objectively reasonable belief; an unreasonable belief cannot yield a full acquittal. (d) misstates the doctrine; imperfect self-defense mitigates murder to voluntary, not involuntary, manslaughter. (e) fails because imperfect self-defense is a substantive partial defense that changes the grade of the conviction at trial, not merely a sentencing mitigation factor.

**Tags:** chapters: [22], topics: [self-defense, imperfect self-defense], difficulty: foundational, cognitive: application

**Grounding:** Chapter 22, Imperfect Self-Defense (imperfect-self-defense)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem does not state that Xavier killed Yasmin, used deadly force, or was charged with murder. It is impossible to evaluate a charge reduction to voluntary manslaughter without knowing Xavier committed a criminal homicide.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Add the missing actus reus and charge to the stem. Example: "Xavier is charged with murder for shooting and killing Yasmin. Assume the jurisdiction recognizes imperfect self-defense. If the jury finds..."
-->

## Issue 2 — edge-case

**Q8.** Assume the jurisdiction recognizes imperfect self-defense. If the jury finds Xavier genuinely feared Yasmin was about to shoot him, but that his fear was objectively unreasonable, what is the effect on his liability?

(a) His honest belief negates the malice element of murder, reducing the charge to voluntary manslaughter. <!-- correct -->
(b) His unreasonable belief completely invalidates his justification defense, making him guilty of first-degree murder.
(c) His honest belief satisfies the subjective prong of perfect self-defense, resulting in a full acquittal.
(d) His unreasonable belief demonstrates extreme recklessness, reducing the charge to involuntary manslaughter.
(e) His honest belief mitigates his culpability only at the sentencing phase, leaving a second-degree murder conviction intact.

**Answer:** (a)

**Explanation:** Imperfect self-defense applies when a defendant honestly but unreasonably believes that deadly force is necessary. In jurisdictions that recognize it (like California), this genuine belief negates the malice required for murder, reducing the homicide to voluntary manslaughter. (b) describes the rule in all-or-nothing jurisdictions that do not recognize imperfect self-defense, contradicting the prompt's assumption. (c) is wrong because perfect self-defense requires both an honest AND an objectively reasonable belief; an unreasonable belief cannot yield a full acquittal. (d) misstates the doctrine; imperfect self-defense mitigates murder to voluntary, not involuntary, manslaughter. (e) fails because imperfect self-defense is a substantive partial defense that changes the grade of the conviction at trial, not merely a sentencing mitigation factor.

**Tags:** chapters: [22], topics: [self-defense, imperfect self-defense], difficulty: foundational, cognitive: application

**Grounding:** Chapter 22, Imperfect Self-Defense (imperfect-self-defense)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The facts explicitly state that Xavier shoots Yasmin in the shoulder and she survives to flee to a gas station (and later kill a clerk). Because Yasmin does not die from Xavier's gunshot, Xavier cannot be charged with completed murder or voluntary manslaughter for shooting her. 
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change the charges in the prompt and options to "attempted murder" and "attempted voluntary manslaughter" (or aggravated assault) to align with the fact that the victim of Xavier's shooting survived.
-->
