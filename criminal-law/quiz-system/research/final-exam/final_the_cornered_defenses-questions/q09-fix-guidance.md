# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q9.** Is Marcus liable for the murder of the watchman under the *Pinkerton* doctrine?

(a) Liable, because shooting an investigating watchman is always considered a reasonably foreseeable consequence when two co-conspirators load dangerous accelerants for an arson.
(b) Not liable, because Leo's act of shooting a perceived monster was the product of a psychotic break, not an act in furtherance of the conspiracy. <!-- correct -->
(c) Liable, because the Pinkerton doctrine imposes strict liability for any homicide that occurs during the physical commission of an underlying predicate felony.
(d) Not liable, because Marcus successfully withdrew from the criminal conspiracy by definitively fleeing the scene just moments after the watchman's unexpected death.
(e) Liable, because Marcus was physically present at the scene when Leo's severe psychotic episode initially began to manifest and trigger the deadly violence.

**Answer:** (b)

**Explanation:** The *Pinkerton* doctrine holds conspirators vicariously liable for substantive crimes committed by co-conspirators if those crimes are committed in furtherance of the conspiracy, fall within its scope, and are reasonably foreseeable. Leo shot the watchman because he genuinely believed he was shooting a "non-human monster from hell" due to a severe psychotic break. This hallucination-driven killing was not an act designed or intended to further the arson conspiracy. (a) is incorrect because it ignores the "in furtherance" requirement, which fails on these specific facts. (c) is incorrect because it conflates *Pinkerton* liability with the felony-murder rule; *Pinkerton* is not a strict liability standard. (d) is incorrect because Marcus fled *after* the shooting occurred, meaning he had not withdrawn prior to the commission of the crime. (e) is incorrect because mere physical presence is irrelevant to *Pinkerton* derivative liability, which relies exclusively on the agency principles of the conspiracy agreement.

**Tags:** chapters: [19], topics: [Pinkerton liability, scope of conspiracy], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 19 - pinkerton-doctrine

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the *Pinkerton* doctrine, co-conspirators are liable for reasonably foreseeable crimes committed within the scope of the conspiracy. When conspirators undertake a dangerous felony like arson, encountering and neutralizing a watchman is a highly predictable event. Courts routinely hold that violence against guards is foreseeable in such contexts. Because Marcus loaded dangerous accelerants with Leo for this exact arson, the resulting violence against an investigating watchman could be argued as a natural and probable consequence of their agreement, making him liable.
(b) Argument-for: The *Pinkerton* doctrine requires that the substantive offense be committed "in furtherance of the conspiracy." If Leo shot the watchman because he genuinely believed the watchman was a "monster from hell" due to a severe psychotic break, he was not acting to promote the arson or protect the conspiracy. His motive was entirely divorced from the conspiratorial objective. Because this specific mens rea requirement of *Pinkerton* fails, Marcus cannot be held vicariously liable for the murder.
(c) Argument-for: A student could argue that *Pinkerton* is effectively a strict liability mechanism when a foreseeable crime occurs during the conspiracy. Because murder occurring during a dangerous predicate felony generally triggers strict liability under the felony-murder rule, a student might conflate the two doctrines. Since arson is a classic predicate felony, any resulting death during its commission would impose liability on all co-felons. Therefore, Marcus is strictly liable under *Pinkerton* for the homicide that occurred during the physical commission of the arson.
(d) Argument-for: Withdrawal from a conspiracy cuts off liability for subsequent substantive crimes committed by co-conspirators. If Marcus fled the scene, a student could argue this constituted a definitive abandonment of the criminal enterprise. Fleeing demonstrates a complete severing of ties from Leo's unilateral and unexpected psychotic violence. Since Marcus ran away the moment the plan deviated from arson to murder, he successfully withdrew and avoided *Pinkerton* liability.
(e) Argument-for: Physical presence during a crime, coupled with a prior agreement, strongly supports accomplice or *Pinkerton* liability. Marcus was right there when Leo's psychotic episode manifested and triggered the violence, meaning he had the opportunity to intervene or stop the shooting but failed to do so. A student might argue that presence during the escalating violence establishes a continuing tacit agreement to the new crime. Thus, his presence makes him liable under the circumstances.

Head-to-head: The keyed answer (b) accurately applies the law: *Pinkerton* requires the substantive crime to be "in furtherance" of the conspiracy, and a purely psychotic hallucination killing falls outside this scope. Distractor (a) uses the absolute "always," ignoring that reasonable foreseeability is a fact question and that the "in furtherance" prong must also be met. Distractor (c) explicitly misstates the doctrine, falsely claiming *Pinkerton* imposes "strict liability" (conflating it with felony murder). Distractor (d) contains a clear legal error by asserting one can "successfully withdraw" moments *after* the target crime's commission. Distractor (e) incorrectly relies on "physical presence" as the basis for liability, but it lacks an absolute word to strictly lock the falsifiable claim.

Falsifiable claim per distractor:
- (a): "always considered a reasonably foreseeable consequence" — wrong because foreseeability is a fact-dependent inquiry, not an absolute, categorical rule.
- (c): "the Pinkerton doctrine imposes strict liability for any homicide" — wrong because *Pinkerton* is not a strict liability doctrine; it requires the act to be reasonably foreseeable and in furtherance of the conspiracy.
- (d): "successfully withdrew... by definitively fleeing the scene just moments after" — wrong because a legally effective withdrawal must occur prior to the commission of the substantive offense, not after it.
- (e): "Liable, because Marcus was physically present" — wrong because *Pinkerton* liability is based on the conspiracy agreement rather than physical presence, though the phrasing would be stronger with an absolute modifier.

Recommended fix: Change (e) to "Liable, solely because Marcus was physically present at the scene when Leo's severe psychotic episode initially began to manifest and trigger the deadly violence."
-->
