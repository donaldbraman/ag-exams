# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Assume Dante is charged with the murder of Hector. Dante claims self-defense, arguing he genuinely believed Hector was about to shoot him. Under the traditional common law rule, how will the court evaluate the imminence of the threat?

(a) It was imminent because Hector's explicit threat to execute Dante upon the crew's arrival within five minutes fully satisfies the strict temporal proximity threshold.
(b) It was imminent only if a reasonable person in Dante's specific circumstances would have perceived Hector as drawing the revolver to attack him immediately. <!-- correct -->
(c) It was categorically not imminent because Hector's hands were resting behind his head, meaning Dante faced no immediate physical danger as a matter of law.
(d) It was categorically not imminent because the primary threat of execution relied upon the future arrival of the crew, which completely defeats the immediacy element.
(e) It was imminent because Dante's sincere, subjective panic that Hector was about to shoot him totally overrides the baseline requirement for objective temporal proximity.

**Answer:** (b)

**Explanation:** The traditional common law requires an imminent threat, meaning immediate physical danger. Imminence is tied to the reasonableness of the defendant's belief. Although Hector said execution would happen in five minutes, Dante perceived Hector's movements as an immediate draw. The defense survives only if a reasonable person in Dante's situation would have shared that perception. (a) is incorrect because a threat conditioned on an event five minutes away is generally considered a future threat, failing traditional imminence. (c) is incorrect because if a reasonable person *would* interpret Hector's movement (even with hands behind his head) as drawing a weapon, the issue goes to the jury; it is not categorically barred as a matter of law. (d) is incorrect because Dante is reacting to his belief that Hector is drawing the weapon *now*, not waiting for the crew. (e) is incorrect because self-defense requires both an honest *and* objectively reasonable belief; subjective panic alone cannot satisfy the imminence requirement.

**Tags:** chapters: [22], topics: [self-defense, imminence, objective reasonableness], difficulty: hard, cognitive: application

**Grounding:** Chapter 22: imminence-requirement, objective-reasonableness-standard

<!-- audit: MUST FIX
<check 1>: pass
<check 2>: pass
<check 3>: pass
<check 4>: MUST FIX. The stem is missing the core factual scenario. The answer choices and explanation refer to highly specific facts (Hector's 5-minute threat, the crew arriving, Hector's hands resting behind his head, Dante perceiving Hector drawing a revolver) that do not appear anywhere in the stem. A student cannot possibly answer this question without those facts.
<check 5>: pass
<check 6>: pass
<check 7>: pass
<check 8>: pass
Recommended fix: Restore the missing factual scenario to the stem (e.g., "Prior to the shooting, Hector explicitly threatened to execute Dante when his crew arrived in five minutes. While Hector's hands were resting behind his head, Dante claims he perceived Hector making a sudden movement to draw a revolver...").
-->

## Issue 2 — argpass-opus

**Q10.** Assume Dante is charged with the murder of Hector. Dante claims self-defense, arguing he genuinely believed Hector was about to shoot him. Under the traditional common law rule, how will the court evaluate the imminence of the threat?

(a) It was imminent because Hector's explicit threat to execute Dante upon the crew's arrival within five minutes fully satisfies the strict temporal proximity threshold.
(b) It was imminent only if a reasonable person in Dante's specific circumstances would have perceived Hector as drawing the revolver to attack him immediately. <!-- correct -->
(c) It was categorically not imminent because Hector's hands were resting behind his head, meaning Dante faced no immediate physical danger as a matter of law.
(d) It was categorically not imminent because the primary threat of execution relied upon the future arrival of the crew, which completely defeats the immediacy element.
(e) It was imminent because Dante's sincere, subjective panic that Hector was about to shoot him totally overrides the baseline requirement for objective temporal proximity.

**Answer:** (b)

**Explanation:** The traditional common law requires an imminent threat, meaning immediate physical danger. Imminence is tied to the reasonableness of the defendant's belief. Although Hector said execution would happen in five minutes, Dante perceived Hector's movements as an immediate draw. The defense survives only if a reasonable person in Dante's situation would have shared that perception. (a) is incorrect because a threat conditioned on an event five minutes away is generally considered a future threat, failing traditional imminence. (c) is incorrect because if a reasonable person *would* interpret Hector's movement (even with hands behind his head) as drawing a weapon, the issue goes to the jury; it is not categorically barred as a matter of law. (d) is incorrect because Dante is reacting to his belief that Hector is drawing the weapon *now*, not waiting for the crew. (e) is incorrect because self-defense requires both an honest *and* objectively reasonable belief; subjective panic alone cannot satisfy the imminence requirement.

**Tags:** chapters: [22], topics: [self-defense, imminence, objective reasonableness], difficulty: hard, cognitive: application

**Grounding:** Chapter 22: imminence-requirement, objective-reasonableness-standard

<!-- argument-pass: MUST FIX
(a) Argument-for: Under the traditional common law, imminence requires an immediate threat of harm. A student could argue that if a crew is arriving within five minutes to execute Dante, the threat process has already begun and escape might be impossible, effectively creating an imminent threat under a broader reading of temporal proximity. Furthermore, the explicit nature of the threat to execute makes the danger sufficiently certain to warrant preemptive protective action.
(b) Argument-for: This option directly applies the traditional common law standard for self-defense, which requires an objectively reasonable belief that an unlawful, deadly attack is imminent. By stating that the imminence element turns on whether a "reasonable person in Dante's specific circumstances" would perceive Hector as attacking "immediately," this accurately tracks the common law's objective reasonableness and temporal immediacy requirements. It correctly identifies that Dante's perception of the specific physical movement (drawing the revolver) is what creates the imminent threat.
(c) Argument-for: A student could argue that if a victim's hands are resting behind their head, there is no physical act or overt movement constituting an immediate threat as a matter of law. Traditional common law strictly requires an overt act indicating immediate physical danger. Therefore, without an aggressive physical movement, words or prior threats alone are insufficient, rendering the threat categorically not imminent.
(d) Argument-for: Traditional common law distinguishes strictly between present and future threats. A threat conditioned on the future arrival of a crew in five minutes is a future threat, not an imminent one. A student could argue that because the primary danger is contingent on an event that has not yet occurred (the crew's arrival), it legally defeats the immediacy element, since Dante had five minutes to retreat or seek help.
(e) Argument-for: A student might confuse perfect self-defense with imperfect self-defense, arguing that Dante's sincere subjective panic satisfies the imminence requirement to mitigate murder to manslaughter. Alternatively, they might erroneously rely on subjective jurisdictional outliers to argue that if Dante genuinely believed Hector was about to shoot him, his subjective perception of imminence totally overrides objective baselines.

Head-to-head: Option (b) is the only legally correct statement, accurately defining the common law standard of objective reasonableness for imminence. However, the question stem completely omits the factual predicate that the options and explanation rely upon. The stem mentions nothing about a five-minute timeline, an arriving crew, Hector's hands behind his head, or a revolver being drawn. Because these crucial facts are entirely missing from the prompt, the student cannot possibly know which of the factual interpretations applies, making the question unanswerable as drafted. The distractors successfully rely on strictly falsifiable absolute claims, but the missing facts force a MUST FIX verdict.

Falsifiable claim per distractor:
- (a): "fully satisfies the strict temporal proximity threshold" — wrong because traditional common law strictly requires immediate danger; a five-minute conditional future threat routinely fails this threshold.
- (c): "categorically not imminent... meaning Dante faced no immediate physical danger as a matter of law" — wrong because whether a specific movement (even from behind the head) constitutes an imminent threat is generally a question of fact for the jury based on the totality of circumstances, not a categorical bar as a matter of law.
- (d): "completely defeats the immediacy element" — wrong because Dante is reacting to his contemporaneous belief that Hector is drawing a weapon *right now*, which legally supersedes the future conditional threat of the crew.
- (e): "totally overrides the baseline requirement for objective temporal proximity" — wrong because the traditional common law explicitly requires the defendant's belief in the imminent threat to be objectively reasonable; subjective panic cannot stand alone.

Recommended fix: Insert the missing factual predicate into the question stem. For example: "Assume Dante is charged with the murder of Hector. Hector, with his hands resting behind his head, explicitly threatened to execute Dante upon his crew's arrival in five minutes. Dante claims self-defense, arguing that he saw Hector suddenly shift his hands and genuinely believed Hector was drawing a revolver to shoot him immediately. Under the traditional common law..."
-->
