# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q14.** Is Blake's act of locking the door the factual (but-for) cause of Chris's death?

(a) No, because Dana's injection caused a massive cardiac rupture that killed Chris instantly, completely preempting the impending lethal overdose mechanism. <!-- correct -->
(b) Yes, because locking the deadbolt was a necessary step in the continuous sequence of events leading directly to the death.
(c) Yes, because Chris would have received medical assistance and survived if Blake had successfully completed the phone call to 911.
(d) No, because Alex's action of drawing the weapon was the primary cause, rendering Blake's subsequent compliance merely a dependent variable.
(e) No, because Chris's initial voluntary consumption of the untested synthetic opioid fundamentally severs any factual causation attributed to the bystanders.

**Answer:** (a)

**Explanation:** (a) is correct because factual (but-for) causation requires asking: "but for the defendant's act, would the result have occurred when and how it did?" Because Dana's injection caused a massive, immediate cardiac rupture that killed Chris instantly, Chris did not die from the delayed rescue or the overdose. Thus, locking the door was not the but-for cause of the specific death that occurred. (b) is wrong because Dana's action preempted the overdose sequence entirely. (c) is wrong because but-for causation evaluates the actual timeline, and the medical assistance was rendered moot by the sudden rupture. (d) is wrong because multiple actors can be concurrent but-for causes, but here the lethal mechanism changed entirely. (e) is wrong because voluntary consumption does not automatically sever factual causation for subsequent acts.

**Tags:** chapters: [8], topics: [causation, but-for-test], difficulty: medium, cognitive: application

**Grounding:** Chapter 8 - Factual Cause (But-For Test)

<!-- audit: MUST FIX
check 1: pass (assuming the missing facts align with the explanation).
check 2: finding - Without the fact pattern, a student could argue that if locking the door trapped Chris inside with Dana, then locking the door *enabled* Dana to inject Chris. If so, locking the door *is* a but-for cause of the actual death (Dana's injection). 
check 3: pass
check 4: MUST FIX - The question entirely lacks a fact pattern. It references a complex scenario involving Blake locking a door, Alex drawing a weapon, Chris voluntarily taking an opioid, and Dana injecting Chris with a lethal substance, none of which is established in a prompt. 
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Provide the missing fact pattern. Additionally, when writing the facts, explicitly ensure that Blake locking the door did *not* facilitate Dana's injection (e.g., make it clear Dana was already inside and would have injected Chris regardless of the lock); otherwise, locking the door actually would be a but-for cause under standard doctrine.
-->

## Issue 2 — edge-case

**Q14.** Is Blake's act of locking the door the factual (but-for) cause of Chris's death?

(a) No, because Dana's injection caused a massive cardiac rupture that killed Chris instantly, completely preempting the impending lethal overdose mechanism. <!-- correct -->
(b) Yes, because locking the deadbolt was a necessary step in the continuous sequence of events leading directly to the death.
(c) Yes, because Chris would have received medical assistance and survived if Blake had successfully completed the phone call to 911.
(d) No, because Alex's action of drawing the weapon was the primary cause, rendering Blake's subsequent compliance merely a dependent variable.
(e) No, because Chris's initial voluntary consumption of the untested synthetic opioid fundamentally severs any factual causation attributed to the bystanders.

**Answer:** (a)

**Explanation:** (a) is correct because factual (but-for) causation requires asking: "but for the defendant's act, would the result have occurred when and how it did?" Because Dana's injection caused a massive, immediate cardiac rupture that killed Chris instantly, Chris did not die from the delayed rescue or the overdose. Thus, locking the door was not the but-for cause of the specific death that occurred. (b) is wrong because Dana's action preempted the overdose sequence entirely. (c) is wrong because but-for causation evaluates the actual timeline, and the medical assistance was rendered moot by the sudden rupture. (d) is wrong because multiple actors can be concurrent but-for causes, but here the lethal mechanism changed entirely. (e) is wrong because voluntary consumption does not automatically sever factual causation for subsequent acts.

**Tags:** chapters: [8], topics: [causation, but-for-test], difficulty: medium, cognitive: application

**Grounding:** Chapter 8 - Factual Cause (But-For Test)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The facts inadvertently create a valid argument that locking the door WAS a but-for cause. Because the door was locked, Evan broke the back window to escape, which Dana then used to enter. This allowed her to bypass the front door where an armed Alex and Blake were standing guard. If the door had been unlocked, Dana would have had to enter through the front door, likely encountering the guards who were ordered to block "outside assistance," potentially preventing her from injecting Chris. This arguably makes locking the door a but-for cause of her successful preemptive injection, complicating intended answer (A).
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Q14’s correct legal logic (that Dana’s lethal injection completely preempted the overdose, meaning "Chris did not die from the delayed rescue") severely structurally clashes with Q9 and Q13. Q9 and Q13 ask the student to evaluate full murder liability based on Alex "blocking the rescue" and Blake’s "omission causing Chris's death." If Q14 teaches the student that the delayed rescue didn't factually cause the death, Q9 and Q13 are spoiled because the underlying murder charges would fail on basic causation before extreme indifference or duress are even analyzed.
Recommended fix: Change Q14 to test whether Alex's initial act of supplying the opioid is the factual cause of Chris’s death (Answer: Yes, because it caused the overdose that triggered Dana’s dependent intervention). Alternatively, adjust the stems of Q9 and Q13 to explicitly analyze *Attempted* Murder so they align with Q14’s conclusion that the delayed rescue did not actually cause the death.
-->

## Issue 3 — argpass-opus

**Q14.** Is Blake's act of locking the door the factual (but-for) cause of Chris's death?

(a) No, because Dana's injection caused a massive cardiac rupture that killed Chris instantly, completely preempting the impending lethal overdose mechanism. <!-- correct -->
(b) Yes, because locking the deadbolt was a necessary step in the continuous sequence of events leading directly to the death.
(c) Yes, because Chris would have received medical assistance and survived if Blake had successfully completed the phone call to 911.
(d) No, because Alex's action of drawing the weapon was the primary cause, rendering Blake's subsequent compliance merely a dependent variable.
(e) No, because Chris's initial voluntary consumption of the untested synthetic opioid fundamentally severs any factual causation attributed to the bystanders.

**Answer:** (a)

**Explanation:** (a) is correct because factual (but-for) causation requires asking: "but for the defendant's act, would the result have occurred when and how it did?" Because Dana's injection caused a massive, immediate cardiac rupture that killed Chris instantly, Chris did not die from the delayed rescue or the overdose. Thus, locking the door was not the but-for cause of the specific death that occurred. (b) is wrong because Dana's action preempted the overdose sequence entirely. (c) is wrong because but-for causation evaluates the actual timeline, and the medical assistance was rendered moot by the sudden rupture. (d) is wrong because multiple actors can be concurrent but-for causes, but here the lethal mechanism changed entirely. (e) is wrong because voluntary consumption does not automatically sever factual causation for subsequent acts.

**Tags:** chapters: [8], topics: [causation, but-for-test], difficulty: medium, cognitive: application

**Grounding:** Chapter 8 - Factual Cause (But-For Test)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Factual causation requires the defendant's act to be a necessary condition for the result occurring when and as it did. Because Dana's injection caused an immediate cardiac rupture that preempted the overdose sequence entirely, Blake's act of locking the door was not a but-for cause of the specific death that occurred. The lethal mechanism changed completely, making Dana's act the preemptive factual cause and rendering Blake's act causally moot. Therefore, (a) correctly applies the but-for test to preemptive causation.
(b) Argument-for: Factual causation evaluates the continuous sequence of events leading to the harm. A student could argue that locking the deadbolt trapped Chris or delayed external intervention, creating the environment in which Dana's injection occurred. If Blake's locking of the door was a necessary step that allowed Dana to administer the injection, it would satisfy the factual causation threshold. This logic asserts that Blake's act was an indispensable link in the chain of events leading directly to the death.
(c) Argument-for: Factual causation often involves counterfactual analysis of omissions. If Blake's failure to complete the 911 call prevented life-saving medical intervention, a student could argue that but for this omission, Chris would have survived. The argument hinges on the factual premise that medical assistance would have arrived in time to alter the outcome. Assuming this counterfactual, Blake's incomplete call is framed as a direct but-for cause of Chris's death.
(d) Argument-for: Under causation principles, an overwhelming primary force can overshadow subsequent dependent acts. Alex drawing a weapon and forcing Blake's compliance implies Blake acted under duress, rendering his action an involuntary dependent variable. A student could argue that because Blake's act was completely controlled by Alex's primary act, factual causation flows exclusively to the primary actor. This would legally sever attribution to the coerced party, making Alex the sole factual cause.
(e) Argument-for: The doctrine of causation must account for the victim's own initiating actions. Chris's voluntary consumption of the untested synthetic opioid set the hazardous scenario into motion. A student could argue that such a highly reckless and voluntary initial act functions as a fundamental superseding event. This perspective asserts that the victim's voluntary ingestion categorically severs the causal chain for all subsequent bystander actions, assigning sole factual causation to Chris.

Head-to-head: Option (a) correctly identifies that Dana's instant lethal injection acts as a preemptive cause, rendering Blake's actions causally irrelevant to the death as it actually occurred. The distractors fail because they either rely on incorrect factual inferences or misstate causation doctrine. Option (b) factually assumes the lock was a necessary step, ignoring that the preemptive injection broke the required continuous sequence. Option (c) incorrectly relies on a counterfactual where medical help arrives, which is factually mooted by the instant rupture. Option (d) presents a false legal claim by asserting that a 'primary cause' inherently negates the factual causation of dependent acts, conflating culpability with factual causation. Option (e) falsely claims that a victim's voluntary act 'fundamentally severs any factual causation,' improperly applying proximate cause superseding rules to the but-for test. Distractors (b) and (c) rely on factual counterfactuals rather than explicit false legal claims, failing the close-call standard.

Falsifiable claim per distractor:
- (b): "locking the deadbolt was a necessary step in the continuous sequence of events" — wrong because Dana's preemptive injection broke the causal sequence, making it factually incorrect; however, it lacks an explicitly false legal claim locked with an absolute.
- (c): "Chris would have received medical assistance and survived" — wrong because medical assistance was rendered factually moot by the instant rupture; it relies on a factual counterfactual rather than a categorically false legal rule.
- (d): "rendering Blake's subsequent compliance merely a dependent variable" — wrong because an act being a dependent variable or coerced does not negate its status as a concurrent factual cause.
- (e): "fundamentally severs any factual causation attributed to the bystanders" — wrong because a victim's voluntary consumption may impact proximate causation but does not categorically sever factual (but-for) causation.

Recommended fix: To strictly adhere to the close-call standard requiring explicit false legal claims locked with absolute words, revise distractors (b), (c), and (d):
- Change (b) to: "Yes, because any deliberate act that precedes a criminal harm is automatically deemed a necessary step in the factual sequence, regardless of subsequent preemptive causes."
- Change (c) to: "Yes, because failing to complete a 911 call categorically establishes factual causation for any subsequent death."
- Change (d) to: "No, because the presence of a primary coerced cause automatically negates the factual causation of all subsequent dependent actions."
- Change (e) to: "No, because a victim's voluntary consumption of illegal drugs categorically severs all factual causation attributed to the subsequent acts of others."
-->
