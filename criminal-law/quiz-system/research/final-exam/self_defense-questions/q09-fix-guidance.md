# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q9.** Assume that Blake had a reasonable belief he was in imminent danger of deadly harm in a retreat jurisdiction. The prosecution argues Blake lost the right to self-defense because he was standing next to a wide-open back door and failed to safely retreat. How does the castle doctrine affect this case?

(a) No duty to retreat, because the castle doctrine universally eliminates the duty to retreat when a defendant is attacked inside their own dwelling. <!-- correct -->
(b) Duty to retreat, because the castle doctrine exception does not apply when the attacker was explicitly invited into the home for a commercial transaction.
(c) No duty to retreat, because the true man doctrine requires a retreat only when the defendant is positioned entirely outside the physical footprint of the home.
(d) Duty to retreat, because Blake's immediate proximity to the wide-open door provided an objectively safe avenue of escape that legally mandated a retreat.
(e) No duty to retreat, because the duty to retreat only applies when the defendant is the initial aggressor in the physical altercation.

**Answer:** (a)

**Explanation:** The "castle doctrine" is a universal exception to the duty to retreat. Even in jurisdictions that generally require a defendant to retreat before using deadly force, a person attacked in their own home has no legal duty to flee before defending themselves. (b) is wrong because the castle doctrine applies within the home even if the attacker is an invitee (though some jurisdictions complicate this if the attacker is a co-occupant, Chris was just a visitor). (c) is wrong because the "true man" doctrine eliminates the duty to retreat *everywhere*, not just outside the home. (d) is wrong because the existence of a safe escape route (the open door) is legally irrelevant inside one's own dwelling. (e) is wrong because initial aggressors generally lose the right to self-defense entirely, while the duty to retreat applies to innocent victims in public spaces.

**Tags:** chapters: [22], topics: [castle-doctrine-scope], difficulty: easy, cognitive: application

**Grounding:** Chapter 22 (Self-Defense) - Castle doctrine exception to the duty to retreat.

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The facts establish Blake is actively engaged in a drug trafficking felony. In many modern jurisdictions, engaging in a felony strips the defendant of Castle Doctrine / Stand Your Ground protections entirely. Furthermore, the use of the word "universally" in option (a) makes the correct answer technically false, as the explanation itself acknowledges exceptions (like co-occupants) and ignores the felony-exception. 
2. Cross-Doctrine Clashes: Pass.
3. Cross-Question Spoilers: Pass.
Recommended fix: Remove the word "universally" from option (a) and the explanation. Revise (a) to: "No duty to retreat, because the castle doctrine generally eliminates the duty to retreat when a non-aggressor defendant is attacked inside their own dwelling."
-->

## Issue 3 — argpass-opus

**Q9.** Assume that Blake had a reasonable belief he was in imminent danger of deadly harm in a retreat jurisdiction. The prosecution argues Blake lost the right to self-defense because he was standing next to a wide-open back door and failed to safely retreat. How does the castle doctrine affect this case?

(a) No duty to retreat, because the castle doctrine universally eliminates the duty to retreat when a defendant is attacked inside their own dwelling. <!-- correct -->
(b) Duty to retreat, because the castle doctrine exception does not apply when the attacker was explicitly invited into the home for a commercial transaction.
(c) No duty to retreat, because the true man doctrine requires a retreat only when the defendant is positioned entirely outside the physical footprint of the home.
(d) Duty to retreat, because Blake's immediate proximity to the wide-open door provided an objectively safe avenue of escape that legally mandated a retreat.
(e) No duty to retreat, because the duty to retreat only applies when the defendant is the initial aggressor in the physical altercation.

**Answer:** (a)

**Explanation:** The "castle doctrine" is a universal exception to the duty to retreat. Even in jurisdictions that generally require a defendant to retreat before using deadly force, a person attacked in their own home has no legal duty to flee before defending themselves. (b) is wrong because the castle doctrine applies within the home even if the attacker is an invitee (though some jurisdictions complicate this if the attacker is a co-occupant, Chris was just a visitor). (c) is wrong because the "true man" doctrine eliminates the duty to retreat *everywhere*, not just outside the home. (d) is wrong because the existence of a safe escape route (the open door) is legally irrelevant inside one's own dwelling. (e) is wrong because initial aggressors generally lose the right to self-defense entirely, while the duty to retreat applies to innocent victims in public spaces.

**Tags:** chapters: [22], topics: [castle-doctrine-scope], difficulty: easy, cognitive: application

**Grounding:** Chapter 22 (Self-Defense) - Castle doctrine exception to the duty to retreat.

<!-- argument-pass: MUST FIX
(a) Argument-for: This option correctly identifies the core principle of the castle doctrine, which exempts individuals from the duty to retreat when they are inside their own dwelling. Even if an objectively safe escape route like an open door is immediately available, the home provides a special legal sanctuary where the duty to retreat is waived.
(b) Argument-for: A student could argue that the castle doctrine's protections are meant primarily for defending against intruders or trespassers. If the attacker was explicitly invited into the home for a commercial transaction, the defendant might revert to the standard duty to retreat since the attacker had a lawful presence and the privacy expectation was lowered.
(c) Argument-for: A student might conflate the true man doctrine with the spatial boundaries of the castle doctrine. They could argue that the true man doctrine allows standing one's ground inside, but imposes a duty to retreat once the defendant crosses outside the physical footprint of the home.
(d) Argument-for: In a strict retreat jurisdiction, the paramount policy goal is the preservation of human life. A student could reason that the castle doctrine only forgives retreat when it is dangerous or impractical, but an open door right next to the defendant creates an undeniably safe escape route that supersedes the exception.
(e) Argument-for: A student could mistakenly believe that the duty to retreat is a penalty imposed only on those who start fights. Under this logic, innocent victims never have to retreat anywhere, and the duty to retreat strictly governs initial aggressors who must attempt to withdraw before escalating to deadly force.

Head-to-head: Option (a) correctly concludes that the castle doctrine negates the duty to retreat despite the open door. However, (a) asserts that the doctrine "universally" eliminates this duty, which is technically false (e.g., many jurisdictions require retreat from co-occupants, and the MPC requires retreat if the defender was the initial aggressor). Furthermore, the question stem completely omits the crucial fact that Blake is inside his own home, making (a)'s conclusion unsupported by the facts provided. Options (b), (c), (d), and (e) all contain explicit false claims. (b) falsely invents a commercial-invitee exception. (c) misstates the true man doctrine, which eliminates the duty to retreat everywhere. (d) wrongly claims an open door overrides the castle doctrine. (e) falsely states that the duty to retreat applies only to initial aggressors. Because the keyed option (a) uses an absolute term that makes it legally false and relies on an omitted fact in the stem, the question earns a MUST FIX.

Falsifiable claim per distractor:
- (b): "the castle doctrine exception does not apply when the attacker was explicitly invited into the home for a commercial transaction." — wrong because the castle doctrine broadly applies against invitees in most jurisdictions, and there is no blanket commercial-transaction exception.
- (c): "the true man doctrine requires a retreat only when the defendant is positioned entirely outside the physical footprint of the home." — wrong because the true man doctrine categorically eliminates the duty to retreat *everywhere*, not just outside the home.
- (d): "immediate proximity to the wide-open door provided an objectively safe avenue of escape that legally mandated a retreat." — wrong because the castle doctrine's express purpose is to eliminate the duty to retreat inside the home, regardless of how safe or immediate the escape route is.
- (e): "the duty to retreat only applies when the defendant is the initial aggressor in the physical altercation." — wrong because the duty to retreat applies to non-aggressors in retreat jurisdictions; initial aggressors generally lose the right to self-defense entirely unless they effectively withdraw.

Recommended fix: In the question stem, change "Assume that Blake had a reasonable belief" to "Assume that Blake, while inside his own home, had a reasonable belief". In option (a), change "universally eliminates" to "generally eliminates" to account for jurisdictional differences regarding co-occupants or initial aggressors.
-->
