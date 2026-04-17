# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-opus

**Q2.** Assume that, regardless of Chris's liability for the conspiracy itself, Alex is charged with the subsequent shooting. What is Chris's liability for the shooting under the Pinkerton doctrine?

(a) Guilty under Pinkerton, because the shooting of the victim was a reasonably foreseeable consequence of a conspiracy to violently threaten someone with baseball bats.
(b) Guilty under Pinkerton, because he failed to take affirmative steps to physically prevent Alex from continuing to the victim's house to carry out the attack.
(c) Not guilty under Pinkerton, because he effectively communicated his withdrawal from the conspiracy to his co-conspirator before the substantive shooting offense occurred. <!-- correct -->
(d) Not guilty under Pinkerton, because the substantive offense of shooting the victim with a handgun was not the specific agreed-upon target offense of the conspiracy.
(e) Not guilty under Pinkerton, because his mere physical presence during the initial agreement is insufficient to establish purposeful intent to aid the completed shooting.

**Answer:** (c)

**Explanation:** (c) is correct because the Pinkerton doctrine holds conspirators liable for reasonably foreseeable crimes committed by co-conspirators in furtherance of the conspiracy, but an effective withdrawal severs this ongoing liability. By dropping his bat and expressly telling Alex "I'm going home," Chris effectively communicated his withdrawal before the shooting, shielding him from Pinkerton liability. (a) is wrong because it ignores Chris's legally effective withdrawal. (b) is wrong because effective withdrawal under common law only requires clear communication to co-conspirators, not affirmative physical prevention. (d) is wrong because Pinkerton liability extends to any foreseeable substantive offense in furtherance of the conspiracy, not just the exact target offense. (e) is wrong because Chris was an active participant who agreed and committed an overt act, meaning his initial involvement was much more than "mere presence."

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, withdrawal], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 - Conspiracy (Pinkerton liability and the requirements for an effective withdrawal to cut off future substantive liability).

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that shooting a victim is a highly foreseeable consequence of confronting them with baseball bats. Pinkerton liability extends to any substantive crime committed in furtherance of the conspiracy that is reasonably foreseeable. If the student incorrectly believes that withdrawal cannot sever Pinkerton liability once an overt act has occurred and the danger is set in motion, this option provides the legally sound basis for holding Chris liable.
(b) Argument-for: Under the Model Penal Code's renunciation defense to conspiracy, an actor must thwart the success of the conspiracy to avoid liability for the conspiracy itself. A student might confuse common-law withdrawal (which merely severs future Pinkerton liability) with complete renunciation. By doing so, they would argue that Chris needed to affirmatively physically prevent Alex from carrying out the attack to escape liability for the shooting.
(c) Argument-for: This is the correct application of the common law. A conspirator can sever Pinkerton liability for future substantive offenses committed by co-conspirators if they effectively communicate their withdrawal to the other members before those offenses occur. Because Chris dropped his bat and announced his departure to Alex before the shooting, he successfully severed his liability.
(d) Argument-for: A student might conflate Pinkerton liability with strict accomplice liability doctrines that require intent for the specific crime. They could argue that a handgun shooting is such a severe deviation from an agreed-upon bat attack that it falls completely outside the scope of the conspiracy. Under this restricted view, substantive liability is limited strictly to the agreed-upon target offense.
(e) Argument-for: "Mere presence" is a well-known defense to conspiracy and accomplice liability, asserting that simply being at the scene does not establish the requisite mens rea. A student who misreads the facts might argue that Chris was simply present at the agreement and lacked the purposeful intent required to aid a shooting. By concluding his initial involvement was legally insufficient, the student would use this to defeat subsequent Pinkerton liability.

Head-to-head: Option (c) is cleanly correct because it addresses both the rule (Pinkerton liability termination) and the determinative facts (effective communication of withdrawal). However, the distractors fail the strict "close-call standard" because they rely on implicit omissions or factual errors rather than explicit, identifiable false legal claims locked with absolute words. Specifically, Option (a) states a generally true legal premise (foreseeability causes guilt) but implicitly omits the withdrawal defense, meaning it lacks an explicitly false legal claim. Option (e) relies entirely on a factual misrepresentation ("mere physical presence") rather than a false legal rule. Options (b) and (d) imply false rules but lack the absolute phrasing necessary to lock them as unambiguously false legal statements. Because (c) is clearly best but the distractors lack locked falsifiable errors, a fix is strongly recommended.

Falsifiable claim per distractor:
- (a): None. The claim that the shooting "was a reasonably foreseeable consequence" is arguably true; the distractor relies entirely on an implicit omission of the withdrawal defense. 
- (b): "because he failed to take affirmative steps to physically prevent" — implies the false legal rule that physical prevention is required for withdrawal, but lacks absolute locking words.
- (d): "because the substantive offense... was not the specific agreed-upon target offense" — implies the false legal rule that Pinkerton covers only the exact target offense, but lacks absolute locking words.
- (e): "because his mere physical presence... is insufficient" — asserts a legally true statement (mere presence is insufficient) but relies on a false factual premise.

Recommended fix: Rewrite the distractors to contain explicitly false legal claims using absolute language. 
(a) Guilty under Pinkerton, because Pinkerton liability automatically attaches to any reasonably foreseeable consequence of a conspiracy, regardless of any attempted withdrawal.
(b) Guilty under Pinkerton, because severing Pinkerton liability categorically requires taking affirmative steps to physically prevent the co-conspirator from carrying out the attack.
(d) Not guilty under Pinkerton, because Pinkerton liability is exclusively limited to the specific agreed-upon target offense of the conspiracy.
(e) Not guilty under Pinkerton, because the Pinkerton doctrine solely imposes liability when a defendant possesses the purposeful intent to aid the completed substantive offense.
-->
