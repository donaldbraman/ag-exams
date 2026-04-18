# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q14.** Assume Benny is charged with delivering the Blue-X to the drop point. He raises a duress defense based on Kev's threat. Can Benny establish the required element of imminence?

(a) The imminence requirement is satisfied because Kev's initial threat with the shotgun legally extends until the entire drug delivery is successfully completed.
(b) The imminence requirement is satisfied because a reasonable person in the drug trade would assume Kev would violently track the delivery vehicle.
(c) The imminence requirement fails because once Benny left the stash house, the immediate threat dissipated and he had an opportunity to seek police assistance. <!-- correct -->
(d) The imminence requirement fails because the underlying crime of drug distribution is a malum in se offense that categorically precludes any duress excuse.
(e) The imminence requirement is satisfied because Kev's specific and furious demand constituted adequate provocation to justify Benny's subsequent criminal conduct.

**Answer:** (c)

**Explanation:** (c) is correct. The imminence requirement of duress demands that the threat be immediate and unavoidable. Once Benny left the stash house, he had safely escaped Kev's physical presence and had the opportunity to contact police, dissipating the imminence. (a) is wrong because the law requires actual proximity and lack of escape; threats do not conceptually "carry over" once the defendant is free to seek help. (b) is wrong because general assumptions about future retaliation do not satisfy the strict imminence threshold. (d) is wrong because only murder is categorically excluded from the duress defense, not drug distribution. (e) is wrong because adequate provocation applies to voluntary manslaughter, not the excuse of duress.

**Tags:** chapters: [21], topics: [duress, imminence], difficulty: hard, cognitive: application

**Grounding:** Chapter 21, Duress / Imminence

<!-- audit: SHOULD FIX
check 1: pass (accurately states the standard rule that leaving the physical presence of the threat and having a safe opportunity to escape defeats imminence)
check 2: pass (distractors are plausible but not legally defensible under the imminence requirement)
check 3: pass (explanation matches doctrine and marked answer perfectly)
check 4: pass, assuming this question is part of a series with a master fact pattern. If this were a standalone question, it would fail because crucial facts (e.g., the shotgun, the stash house, Benny's isolation) are missing from the stem.
check 5: fails (jurisdictional clarity). The prompt asks about "the required element of imminence." Because the MPC (taught via `reasonable-firmness-objective`) famously abandons the strict imminence requirement for duress, a well-prepared student could be confused or argue the question is flawed. The stem needs to explicitly situate the question in a jurisdiction that requires imminence.
check 6: pass (no excluded topics)
check 7: pass (grounded in Chapter 21 `duress-imminence-proximity` and `duress-murder-bar` tags)
check 8: pass (options are symmetric in length and structure)
Recommended fix: Add "Under the common law," to the prompt. Example: "Under the common law, can Benny establish the required element of imminence?"
-->

## Issue 2 — argpass-sonnet

**Q14.** Assume Benny is charged with delivering the Blue-X to the drop point. He raises a duress defense based on Kev's threat. Can Benny establish the required element of imminence?

(a) The imminence requirement is satisfied because Kev's initial threat with the shotgun legally extends until the entire drug delivery is successfully completed.
(b) The imminence requirement is satisfied because a reasonable person in the drug trade would assume Kev would violently track the delivery vehicle.
(c) The imminence requirement fails because once Benny left the stash house, the immediate threat dissipated and he had an opportunity to seek police assistance. <!-- correct -->
(d) The imminence requirement fails because the underlying crime of drug distribution is a malum in se offense that categorically precludes any duress excuse.
(e) The imminence requirement is satisfied because Kev's specific and furious demand constituted adequate provocation to justify Benny's subsequent criminal conduct.

**Answer:** (c)

**Explanation:** (c) is correct. The imminence requirement of duress demands that the threat be immediate and unavoidable. Once Benny left the stash house, he had safely escaped Kev's physical presence and had the opportunity to contact police, dissipating the imminence. (a) is wrong because the law requires actual proximity and lack of escape; threats do not conceptually "carry over" once the defendant is free to seek help. (b) is wrong because general assumptions about future retaliation do not satisfy the strict imminence threshold. (d) is wrong because only murder is categorically excluded from the duress defense, not drug distribution. (e) is wrong because adequate provocation applies to voluntary manslaughter, not the excuse of duress.

**Tags:** chapters: [21], topics: [duress, imminence], difficulty: hard, cognitive: application

**Grounding:** Chapter 21, Duress / Imminence

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might defend this option by appealing to continuous offense theories or the idea that a coercer's control over a situation can conceptually span the duration of a task. They could argue that if the threat of death is explicitly conditioned on the successful completion of the delivery, the legal imminence of the threat "extends" until the condition is met. This attempts to stretch the temporal boundaries of the threat to align with the ongoing nature of the coerced act, arguing that Benny was under continuous psychological duress.
(b) Argument-for: A student could defend (b) by drawing on the Model Penal Code's broader duress standard, which abandons strict common-law imminence in favor of asking whether a person of reasonable firmness would be unable to resist. Under this view, they might argue that an objective assumption of violent tracking in the drug trade functionally establishes unavoidability. They would mistakenly conclude that this general assumption of future harm satisfies the "imminence requirement" by rendering escape practically impossible.
(c) Argument-for: This is the correct application of the traditional common law duress doctrine. To establish duress, the threat of death or serious bodily harm must be present, immediate, and impending. Crucially, the defendant must have no reasonable opportunity to escape the threatened harm. Once Benny physically departed the stash house, the spatial and temporal separation dissipated the strict imminence of Kev's threat and provided a window to seek police assistance.
(d) Argument-for: A student might mistakenly believe that all serious or inherently dangerous felonies are excluded from the duress defense. They would analogize drug distribution to the traditional common law rule that categorically precludes duress as an excuse for intentional murder. Believing drug distribution to be a malum in se offense of high severity, they could erroneously conclude that the law absolutely bars Benny from raising duress.
(e) Argument-for: A student could defend (e) by severely conflating distinct criminal law doctrines—namely duress, justification, and provocation. They might reason that a "specific and furious demand" from an armed drug dealer is a form of legally cognizable provocation that "justifies" the resulting criminal act. This misapplies the partial excuse of adequate provocation (which mitigates murder to voluntary manslaughter) as a full justification for non-homicide conduct.

Head-to-head: Option (c) is clearly correct because it accurately applies the traditional common law rule that duress requires an immediate threat and a lack of reasonable opportunity to escape. Distractor (a) posits a non-existent legal doctrine where threats "legally extend" throughout an uncompleted transaction. Distractor (d) correctly identifies an absolute legal bar but applies it to the wrong crime (drug distribution instead of murder). Distractor (e) fatally conflates provocation (mitigation) with justification. Distractor (b) is the weakest link structurally; while substantively wrong because general assumptions of future harm don't satisfy strict imminence, it relies on a factual assumption rather than a hard, falsifiable legal rule locked by an absolute word.

Falsifiable claim per distractor:
- (a): "legally extends until the entire drug delivery is successfully completed" — wrong because imminence requires continuous physical proximity and immediate danger, not just an ongoing uncompleted task.
- (b): "a reasonable person in the drug trade would assume Kev would violently track" — wrong because an assumption of future tracking does not legally satisfy strict imminence, though it lacks an absolute locking word to make the legal falsity explicit.
- (d): "categorically precludes any duress excuse" — wrong because only intentional murder is categorically excluded from the duress defense at common law.
- (e): "constituted adequate provocation to justify" — wrong because adequate provocation is a partial excuse for homicide, not a justification defense.

Recommended fix: Change (b) to lock in a false legal rule: "(b) The imminence requirement is satisfied because an objective fear of future retaliation automatically overrides the need for physical proximity."
-->
