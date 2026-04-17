# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q14.** In a prosecution of Blake for Chris's death, the defense argues that Blake's failure to call 911 was not the factual (but-for) cause of Chris's death. Which of the following facts best supports this argument?

(a) Dana's subsequent injection killed Chris instantly, meaning Chris would have died at that exact moment even if Blake had called 911, so the omission was not a but-for cause. <!-- correct -->
(b) Alex originally handed Chris the untested dose of the opioid, making Alex the sole proximate cause of the death.
(c) Chris had a known history of severe adverse drug reactions, making his collapse an entirely foreseeable event.
(d) Evan helped push the heavy deadbolt shut, meaning Blake was not acting alone in secluding Chris.
(e) Expert testimony established that Chris would have died within ten minutes from the overdose regardless of any intervention.

**Answer:** (a)

**Explanation:** Factual (but-for) causation requires that the result would not have occurred when it did but for the defendant's conduct. Because Dana's injection killed Chris instantly, the failure to call 911 did not actually contribute to the death; emergency services could not have arrived in time to prevent the instant death. (b) is wrong because there can be multiple proximate causes, but the question asks about factual causation. (c) is wrong because foreseeability relates to proximate cause, not but-for causation. (d) is wrong because concurrent sufficient causes do not defeat but-for causation. (e) is wrong because Dana's injection preempted the 10-minute timeline, altering the actual mechanism and timing of death.

**Tags:** chapters: [8], topics: [but-for-test-basic, factual-causation], difficulty: medium, cognitive: application

**Grounding:** Chapter 8, Factual Cause

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: finding (Explanation (d) says "concurrent sufficient causes do not defeat but-for causation." Technically, they *do* defeat the strict but-for test, which is why courts use workarounds to find factual causation anyway. Better phrasing: "do not defeat a finding of factual causation.")
check 4: fails (The stem is missing the entire factual scenario. It introduces Dana, Alex, Evan, an overdose, a deadbolt, and a lethal injection out of nowhere. Students cannot answer this without the missing fact pattern.)
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Prepend the missing fact pattern to the stem (e.g., "Alex gives Chris an untested opioid, causing an overdose. Blake and Evan lock Chris in a room, and Blake fails to call 911. Before Chris dies from the overdose, Dana enters and instantly kills Chris with a lethal injection.") and update explanation (d) to say "do not defeat a finding of factual causation."
-->

## Issue 2 — argpass-sonnet

**Q14.** In a prosecution of Blake for Chris's death, the defense argues that Blake's failure to call 911 was not the factual (but-for) cause of Chris's death. Which of the following facts best supports this argument?

(a) Dana's subsequent injection killed Chris instantly, meaning Chris would have died at that exact moment even if Blake had called 911, so the omission was not a but-for cause. <!-- correct -->
(b) Alex originally handed Chris the untested dose of the opioid, making Alex the sole proximate cause of the death.
(c) Chris had a known history of severe adverse drug reactions, making his collapse an entirely foreseeable event.
(d) Evan helped push the heavy deadbolt shut, meaning Blake was not acting alone in secluding Chris.
(e) Expert testimony established that Chris would have died within ten minutes from the overdose regardless of any intervention.

**Answer:** (a)

**Explanation:** Factual (but-for) causation requires that the result would not have occurred when it did but for the defendant's conduct. Because Dana's injection killed Chris instantly, the failure to call 911 did not actually contribute to the death; emergency services could not have arrived in time to prevent the instant death. (b) is wrong because there can be multiple proximate causes, but the question asks about factual causation. (c) is wrong because foreseeability relates to proximate cause, not but-for causation. (d) is wrong because concurrent sufficient causes do not defeat but-for causation. (e) is wrong because Dana's injection preempted the 10-minute timeline, altering the actual mechanism and timing of death.

**Tags:** chapters: [8], topics: [but-for-test-basic, factual-causation], difficulty: medium, cognitive: application

**Grounding:** Chapter 8, Factual Cause

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Factual causation requires that the prohibited result would not have occurred at the specific time it did but for the defendant's conduct. If Dana’s injection was a preemptive cause that killed Chris "instantly," then the death occurred at that "exact moment" regardless of any action by Blake. Since calling 911 would not have prevented a death that occurred at that precise second, Blake’s omission categorically fails the but-for test. This fact provides the strongest support because it uses specific temporal language to rule out any acceleration of the death by Blake.

(b) Argument-for: A defendant can avoid liability by establishing that another party's conduct was the "sole proximate cause" of the harm. If Alex provided the untested dose, the defense can argue that Alex’s act was the direct, operational cause that makes all other factors legally irrelevant. By framing Alex as the "sole" cause, the defense argues that Blake’s omission was a mere bystander's failure rather than a necessary link in the causal chain that led to Chris’s death.

(c) Argument-for: This fact supports the defense by suggesting that the death was the "entirely foreseeable" and inevitable result of Chris’s own medical history rather than Blake's omission. If a collapse is a natural and expected consequence of a victim's condition, the defense can argue that the drug reaction was the independent but-for cause of the death. This implies that the outcome was pre-determined by Chris's physiology, making Blake's failure to call 911 a non-contributing factor.

(d) Argument-for: In cases involving multiple actors, a defendant can argue their specific contribution was not a but-for cause if another person's actions were independently sufficient. Since Evan helped push the deadbolt, the defense can argue that "Blake was not acting alone" and that Evan’s actions alone would have secluded Chris. Under a strict but-for interpretation, Blake’s help was not a necessary condition for the harm because the seclusion would have occurred even without Blake’s participation.

(e) Argument-for: For an omission to be a factual cause, the omitted act must have been effective in preventing the harm. If expert testimony establishes that Chris would have died "regardless of any intervention," then Blake’s failure to call 911 was not a cause-in-fact because even the most effective intervention would have failed to save him. This supports the argument by showing that the outcome was inevitable within a ten-minute window regardless of Blake’s choices.

Head-to-head: (a) is the keyed answer because it addresses the timing of death ("at that exact moment"), which is the most precise application of the but-for test (preemption). (b) and (c) are legally flawed because they attempt to use proximate cause concepts (sole cause and foreseeability) to answer a factual cause question. (d) is flawed because the law typically uses the "substantial factor" test to maintain causation for concurrent sufficient causes rather than negate it. (e) is the most dangerous distractor; it is only "wrong" compared to (a) because (a) specifies the death occurred at the "exact moment," whereas (e) allows for the possibility that Blake’s omission accelerated the death within that ten-minute window (and acceleration is still factual causation). However, (e) lacks an explicit false legal claim, and its rejection in the provided explanation relies on facts found only in option (a), constituting a logic leak.

Falsifiable claim per distractor:
- (b): "making Alex the sole proximate cause" — wrong because proximate cause is a distinct doctrine from factual cause and does not negate it; multiple parties can be factual causes.
- (c): "making his collapse an entirely foreseeable event" — wrong because foreseeability is the test for proximate causation, not factual (but-for) causation.
- (d): "meaning Blake was not acting alone" — wrong because being one of multiple sufficient concurrent causes does not negate factual causation (the substantial factor test applies).
- (e): "regardless of any intervention" — wrong because it fails to exclude the possibility of acceleration; if an omission causes a death to occur sooner than it otherwise would have, it is a factual cause even if death was inevitable within ten minutes.

Recommended fix: Add a concluding legal error to (e), such as "...meaning the failure to call 911 is automatically excused by the inevitability of the overdose." Additionally, the explanation for (e) should be updated to explain the acceleration doctrine rather than relying on the facts of option (a).
-->

## Issue 3 — argpass-opus

**Q14.** In a prosecution of Blake for Chris's death, the defense argues that Blake's failure to call 911 was not the factual (but-for) cause of Chris's death. Which of the following facts best supports this argument?

(a) Dana's subsequent injection killed Chris instantly, meaning Chris would have died at that exact moment even if Blake had called 911, so the omission was not a but-for cause. <!-- correct -->
(b) Alex originally handed Chris the untested dose of the opioid, making Alex the sole proximate cause of the death.
(c) Chris had a known history of severe adverse drug reactions, making his collapse an entirely foreseeable event.
(d) Evan helped push the heavy deadbolt shut, meaning Blake was not acting alone in secluding Chris.
(e) Expert testimony established that Chris would have died within ten minutes from the overdose regardless of any intervention.

**Answer:** (a)

**Explanation:** Factual (but-for) causation requires that the result would not have occurred when it did but for the defendant's conduct. Because Dana's injection killed Chris instantly, the failure to call 911 did not actually contribute to the death; emergency services could not have arrived in time to prevent the instant death. (b) is wrong because there can be multiple proximate causes, but the question asks about factual causation. (c) is wrong because foreseeability relates to proximate cause, not but-for causation. (d) is wrong because concurrent sufficient causes do not defeat but-for causation. (e) is wrong because Dana's injection preempted the 10-minute timeline, altering the actual mechanism and timing of death.

**Tags:** chapters: [8], topics: [but-for-test-basic, factual-causation], difficulty: medium, cognitive: application

**Grounding:** Chapter 8, Factual Cause

<!-- argument-pass: MUST FIX
(a) Argument-for: Option (a) accurately applies the rule of preemptive causation to an omission. The but-for test requires asking whether the victim would have died "when and as he did" if the defendant had acted. Because Dana's injection killed Chris instantly, even a prompt 911 call by Blake would not have brought emergency services in time to prevent the death. Therefore, Blake's failure to call 911 was not a but-for cause of the death that actually occurred, making this fact the strongest support for the defense's argument.
(b) Argument-for: A student might choose option (b) by reasoning that if Alex is the "sole proximate cause" of the death, this necessarily absolves Blake of all causal responsibility. If another individual's act of handing over untested opioids completely overtakes the causal chain, it essentially renders any subsequent omissions irrelevant. Thus, establishing Alex as the exclusive legal cause would strongly support a defense argument that Blake's failure to call 911 cannot be a legally cognizable factual or proximate cause.
(c) Argument-for: Option (c) highlights Chris's preexisting condition and the foreseeability of his collapse. A student could argue that if the collapse was an entirely foreseeable result of Chris's own voluntary actions and known medical history, Chris ultimately caused his own death. Under this logic, the primary factual cause of death is the adverse reaction itself, and the foreseeability of the event shifts the causal burden away from Blake's mere failure to act, thereby supporting the argument that Blake was not the but-for cause.
(d) Argument-for: Option (d) introduces Evan as a concurrent actor in secluding Chris. A student might argue that if two people jointly lock a deadbolt, neither individual's action is the "but-for" cause under a strict sine qua non test, since the door might still have been locked by the other actor. By asserting that Blake was not acting alone, the defense could attempt to muddy the waters of factual causation, arguing that Blake's individual omission to rescue is inseparable from Evan's actions, thereby negating Blake's solo but-for causation.
(e) Argument-for: Option (e) provides the classic legal defense to omission liability. For a failure to act to be a but-for cause of death, the omitted action must have been capable of saving the victim's life. If expert testimony establishes that Chris would have died within ten minutes "regardless of any intervention," then calling 911 would not have altered the outcome. This fact directly and conclusively proves that Blake's omission was not a but-for cause, perfectly supporting the defense's argument.

Head-to-head:
Option (a) correctly uses the preemptive cause doctrine to negate but-for causation for an omission. However, option (e) is equally compelling and legally correct. In criminal law, if a victim would have died regardless of the defendant's omitted intervention (e.g., calling 911), the omission cannot be a but-for cause. The explanation dismisses (e) by relying on facts outside the option text ("Dana's injection preempted the 10-minute timeline"), but standing alone as an option, (e) contains no explicit false legal claim and perfectly supports the defense's argument, rendering the question double-keyed. Distractor (b) incorrectly relies on proximate cause to address a question explicitly about factual cause. Distractor (c) confuses foreseeability (a proximate cause concept) with factual causation. Distractor (d) relies on the presence of a joint actor, which legally does not defeat individual but-for causation. Because (e) presents a legally valid basis for negating factual causation without any internal falsifiable error, the question requires a fix.

Falsifiable claim per distractor:
- (b): "making Alex the sole proximate cause" — wrong because proximate cause doctrines do not logically support an argument specifically disputing factual (but-for) causation, and multiple actors can share causation.
- (c): "making his collapse an entirely foreseeable event" — wrong because foreseeability relates to proximate causation, not factual but-for causation.
- (d): "meaning Blake was not acting alone" — wrong because the presence of a concurrent actor does not defeat but-for causation.
- (e): "regardless of any intervention" — lacks a falsifiable claim. If true, this fact legally establishes that the omission was not a but-for cause, making it a correct answer to the question asked.

Recommended fix: Edit (e) to introduce a clear legal error regarding how omissions relate to the timing of death. For example: "(e) Expert testimony established that a 911 call would have prolonged Chris's life by only ten minutes, meaning the omission was not a but-for cause of his death." (This creates a falsifiable error, as shortening a life by even ten minutes legally satisfies but-for causation).
-->
