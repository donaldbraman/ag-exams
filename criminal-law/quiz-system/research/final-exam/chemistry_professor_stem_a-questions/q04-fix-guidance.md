# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

```markdown
<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: finding (The explanation for (b) refers to "Arthur's omission" removing a rescue, but smashing a phone and locking a door are affirmative acts, which the explanation itself correctly notes in the main section. This inconsistency is doctrinally confusing.)
check 4: finding (The stem fails to provide the operative facts. It mentions only a "delay in allowing emergency assistance," but the options and explanation rely on specific facts absent from the prompt: that Arthur smashed a phone, locked a door, and that Julian would have had a 95% chance of survival if paramedics were called.)
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Move the missing facts into the stem (e.g., "Julian collapsed from an overdose. Arthur smashed the phone and locked the door to prevent anyone from calling for help. Experts agree that with immediate paramedic intervention, Julian would have had a 95% chance of survival..."). Simplify option (d) accordingly, and change "omission" to "acts" in the explanation for (b).
-->
```

## Issue 2 — argpass-opus

**Q4.** Assume Arthur is charged with homicide. Arthur argues that the toxic substance itself—not his subsequent delay in allowing emergency assistance—was the factual cause of Julian's death. How will a court apply the but-for test to Arthur's actions after Julian collapsed?

(a) Arthur is not a but-for cause, because the drug had already initiated the fatal arrhythmia before Arthur broke the phone.
(b) Arthur is not a but-for cause, because under the concurrent sufficient causes doctrine, the drug alone was sufficient to cause death.
(c) Arthur is a but-for cause, because he is strictly liable for any death resulting from a Schedule I substance distribution.
(d) Arthur is a but-for cause, because if he had not destroyed the phone and locked the door, paramedics would have been called, giving Julian a 95% chance of survival. <!-- correct -->
(e) Arthur is a but-for cause, because the law presumes that any failure to rescue an overdose victim constitutes the sole factual cause of their death.

**Answer:** (d)

**Explanation:** Factual cause requires asking whether the result would have occurred "but for" the defendant's conduct. Because Julian had a 95% chance of survival if paramedics had been called, Arthur's acts of smashing the phone and locking the door were a necessary condition for the death to occur at that time. (a) is wrong because a defendant can be a factual cause by accelerating or ensuring a death that could have been prevented with timely intervention. (b) is wrong because concurrent sufficient causes apply when two independent forces act simultaneously (e.g., two shooters); here, Arthur's omission removed a high-probability rescue. (c) is wrong because but-for causation is a factual empirical inquiry about necessity, not a strict liability rule. (e) is wrong because the law makes no such presumption; factual causation must always be proven specifically.

**Tags:** chapters: [8], topics: [factual cause, but-for test], difficulty: easy, cognitive: application

**Grounding:** Chapter 8, but-for-test-basic

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that factual causation requires the defendant to be the primary active force that brings about the prohibited result. Because the victim had already ingested the drug and the fatal physiological process (the arrhythmia) had begun prior to Arthur breaking the phone, the drug itself was the actual cause of death. Under this view, Arthur's subsequent actions merely failed to stop an already-initiated death, meaning he cannot be the but-for cause of the underlying fatal condition.
(b) Argument-for: The concurrent sufficient causes doctrine applies when multiple independent forces are sufficient to bring about a result. A student might argue that a lethal dose of a toxic substance is, by definition, sufficient to cause death. Therefore, the drug and Arthur's interference act as concurrent sufficient causes. Because the drug alone was sufficient to kill Julian, Arthur's subsequent acts are not a necessary "but-for" condition for the death.
(c) Argument-for: In cases involving drug distribution, many jurisdictions have strict liability statutes, such as drug-induced homicide laws. A student could argue that when dealing with a Schedule I substance, the law bypasses the standard but-for factual causation analysis. Because the offense is one of strict liability, any death following distribution automatically satisfies the causation requirement, making Arthur a but-for cause as a matter of law based purely on his status as distributor.
(d) Argument-for: The but-for test asks whether the victim's death would have occurred when and how it did "but for" the defendant's acts. The facts establish that Julian had a 95% chance of survival if paramedics had been called. By actively destroying the phone and locking the door, Arthur eliminated this high probability of survival. Therefore, Arthur's conduct was a necessary condition for Julian dying at that specific time, satisfying the factual cause requirement.
(e) Argument-for: Modern statutes increasingly impose duties on individuals to report overdoses (e.g., Good Samaritan laws). A student could argue that the law incorporates a punitive presumption regarding causation when a person fails to rescue an overdose victim. Under this theory, any failure to call for help legally presumes the omission to be the sole factual cause of death to enforce public policy, definitively making Arthur the but-for cause.

Head-to-head:
Option (d) correctly identifies that accelerating a death or removing a high probability of survival satisfies the but-for test, making Arthur's affirmative acts a factual cause. Option (a) incorrectly assumes that a pre-existing fatal condition negates but-for causation; a defendant who accelerates death is still a but-for cause. Option (b) misapplies the concurrent sufficient causes doctrine, which is meant for simultaneous independent forces (like two fatal fires), not sequential acts where one removes a chance of rescue. Option (c) improperly substitutes the mens rea concept of strict liability for the actus reus requirement of factual causation. Option (e) relies on a fabricated legal presumption about failure to rescue. While (d) is clearly the best answer, Options (a) and (b) currently lack absolute modifiers to strictly lock them as explicitly falsifiable statements of law, leaving them slightly vulnerable to interpretive debate.

Falsifiable claim per distractor:
- (a): "because the drug had already initiated the fatal arrhythmia" — wrong because it implies initiating a fatal condition legally precludes subsequent acts from being but-for causes; accelerating death or removing a high probability of survival still satisfies but-for causation.
- (b): "under the concurrent sufficient causes doctrine, the drug alone was sufficient" — wrong because this doctrine applies to simultaneous sufficient causes, and the drug was not practically "sufficient" on its own since intervention would have resulted in a 95% survival rate.
- (c): "he is strictly liable for any death resulting from a Schedule I substance distribution" — wrong because strict liability may apply to the mens rea of an offense, but factual "but-for" causation must still be empirically established as an actus reus element.
- (e): "the law presumes that any failure to rescue an overdose victim constitutes the sole factual cause" — wrong because no such absolute presumption exists; factual causation must always be proven on the specific facts.

Recommended fix: Add absolute words to (a) and (b) to ensure they contain explicit, mathematically falsifiable claims. 
Change (a) to: "Arthur is not a but-for cause, solely because the drug had already initiated the fatal arrhythmia before Arthur broke the phone." 
Change (b) to: "Arthur is not a but-for cause, because under the concurrent sufficient causes doctrine, a lethal dose automatically renders subsequent interference legally irrelevant."
-->
