# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-opus

**Q3.** Assume that, regardless of prior conclusions, Carmine asserts a claim of self-defense. If the jurisdiction recognizes the doctrine of imperfect self-defense, how will Carmine's genuine but unreasonable belief that Paulie was drawing a weapon affect his criminal liability?

(a) He will be fully acquitted of all homicide charges because he genuinely believed he was in imminent danger of death or serious bodily harm.
(b) He will be convicted of voluntary manslaughter because imperfect self-defense mitigates a killing when the defendant genuinely but unreasonably believes deadly force is necessary. <!-- correct -->
(c) He will be convicted of second-degree murder because the doctrine of imperfect self-defense applies only when the defendant was the initial physical aggressor.
(d) He will be convicted of involuntary manslaughter because his unreasonable belief constitutes a gross deviation from the standard of care required in confrontations.
(e) He will be convicted of first-degree murder because self-defense requires an objectively reasonable fear, and an unreasonable fear provides no legal mitigation whatsoever.

**Answer:** (b)

**Explanation:** Imperfect self-defense applies when a defendant actually and genuinely believes that deadly force is necessary to prevent imminent death or great bodily harm, but that belief is objectively unreasonable. This incomplete defense mitigates what would otherwise be murder to voluntary manslaughter. (b) is correct because Carmine genuinely believed Paulie was drawing a weapon, but the facts stipulate this belief was unreasonable. (a) fails because a completely unreasonable belief does not provide a full justification for acquittal. (c) fails because imperfect self-defense primarily applies to unreasonable beliefs, not just to initial aggressors who attempt to withdraw. (d) fails because imperfect self-defense yields a voluntary manslaughter conviction (an intentional killing without malice), not involuntary manslaughter (a reckless or negligent killing). (e) fails because recognizing imperfect self-defense expressly allows for mitigation based on a subjective but unreasonable fear.

**Tags:** chapters: [22], topics: [self-defense, imperfect self-defense, mitigation], difficulty: medium, cognitive: application

**Grounding:** Chapter 22: imperfect-self-defense

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might argue that if a belief is genuinely held, the defendant lacks the subjective mens rea for any crime, thereby meriting a full acquittal. Under a purely subjective theory of culpability, punishing someone for a genuine mistake might be seen as conflicting with the requirement of moral blameworthiness, leading them to believe the doctrine fully acquits.
(b) Argument-for: This option correctly identifies the core mechanism of the doctrine of imperfect self-defense. When a defendant subjectively and genuinely believes that deadly force is necessary to repel an imminent deadly threat, but this belief is objectively unreasonable, the doctrine acts as a partial defense that negates malice aforethought, mitigating murder to voluntary manslaughter.
(c) Argument-for: Imperfect self-defense can indeed apply when the defendant is the initial non-deadly aggressor who is then met with deadly force but fails to perfectly withdraw. A student might remember this specific application and incorrectly assume it is the *only* scenario where the doctrine applies, concluding Carmine is guilty of second-degree murder.
(d) Argument-for: A student could argue that an unreasonable belief conceptually maps onto recklessness or criminal negligence, which are the typical mens rea states for involuntary manslaughter. Under Model Penal Code concepts, an unreasonable belief can yield a conviction for reckless or negligent homicide, so a student might mistakenly assume the common-law term "imperfect self-defense" leads to involuntary manslaughter.
(e) Argument-for: A student might argue that self-defense fundamentally requires an objectively reasonable fear of imminent harm. Even if a jurisdiction ostensibly recognizes the doctrine, a student could incorrectly conclude that a completely unreasonable fear entirely invalidates any mitigation, making him fully liable for first-degree murder.

Head-to-head: 
Option (b) is the clear, correct application of the traditional doctrine of imperfect self-defense, which mitigates an intentional killing to voluntary manslaughter. Option (a) incorrectly asserts a full acquittal. Option (c) is easily falsifiable because it uses the absolute word "only" to restrict the doctrine to initial aggressors. Option (e) contradicts the explicit premise of the prompt by stating an unreasonable fear "provides no legal mitigation whatsoever." Option (d) asserts the conviction will be involuntary manslaughter. While this is legally false under the named doctrine (which mitigates malice, resulting in voluntary manslaughter), adding an absolute word to (d)'s reasoning would fully lock it against edge-case arguments invoking MPC-style reckless manslaughter. 

Falsifiable claim per distractor:
- (a): "fully acquitted of all homicide charges" — wrong because imperfect self-defense is categorically a partial defense that mitigates, rather than a full justification that acquits.
- (c): "applies only when the defendant was the initial physical aggressor" — wrong because the absolute word "only" excludes the primary formulation of the doctrine (genuine but unreasonable belief).
- (d): "He will be convicted of involuntary manslaughter" — wrong because the doctrine of imperfect self-defense mitigates an intentional killing to voluntary manslaughter, but the distractor lacks an absolute word locking the legal rationale.
- (e): "provides no legal mitigation whatsoever" — wrong because it directly contradicts the definition of the doctrine, which exists explicitly to provide mitigation.

Recommended fix: Change (d) to lock the rationale with an absolute word. Example: "(d) He will be convicted of involuntary manslaughter because the doctrine of imperfect self-defense categorically mitigates murder to an unintentional homicide."
-->
