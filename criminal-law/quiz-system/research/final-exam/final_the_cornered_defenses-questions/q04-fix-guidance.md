# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q4.** Assume Marcus successfully asserts a duress defense for the conspiracy. Can Dexter raise Marcus's duress as a defense to his own accomplice liability?

(a) Yes, because duress is a justification that renders the underlying act socially desirable, meaning any party who assists shares in the defense.
(b) No, because duress is merely an excuse that protects the coerced actor, not a justification that renders the underlying act lawful for helpers. <!-- correct -->
(c) No, because accomplice liability is strictly determined by the principal's ultimate conviction, regardless of any affirmative defenses the principal raises.
(d) Yes, because the justification/excuse distinction only applies to self-defense claims, allowing duress to extend derivative immunity to external accomplices.
(e) No, because Dexter lacked a reasonable belief that Marcus was under an imminent threat of death or serious bodily injury at the time.

**Answer:** (b)

**Explanation:** Criminal defenses are divided into justifications (which render the act lawful and are shared by accomplices) and excuses (which recognize the act is wrongful but withhold punishment due to the actor's lack of moral culpability). Duress is the paradigmatic excuse. Because it is personal to Marcus, it does not transfer to Dexter. (a) is incorrect because it falsely categorizes duress as a justification. (c) is incorrect because modern law generally allows an accomplice to be convicted even if the principal is excused or acquitted, decoupling their legal fates. (d) is incorrect because the justification/excuse distinction is a fundamental doctrine applying across all affirmative defenses, not just self-defense. (e) is incorrect because an accomplice's subjective belief about the principal's duress is irrelevant to whether the principal's defense transfers to the accomplice.

**Tags:** chapters: [18, 21], topics: [accomplice liability, justification vs excuse], difficulty: medium, cognitive: application

**Grounding:** Chapter 21 - justification-vs-excuse

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: SHOULD FIX. The stem says "Assume Marcus successfully asserts a duress defense for the conspiracy." However, Dexter's derivative accomplice liability would attach to the substantive offense (the attempted arson), not the conspiracy. (There is generally no distinct crime of being an "accomplice to a conspiracy"—one is either a co-conspirator or an accomplice to the target act). 
2. Cross-Doctrine Clashes: pass. (Note: Because Vance's threat was to execute Marcus's entire family, burning an empty warehouse is objectively the "lesser evil," meaning Marcus's act could actually be classified as *justified* under the MPC necessity doctrine. A sharp student might argue Dexter is shielded because the underlying act was justified. However, because the call of the question strictly confines the doctrine to analyzing *Marcus's duress*, the question technically avoids this clash).
3. Cross-Question Spoilers: pass
Recommended fix: Change the first sentence to "Assume Marcus successfully asserts a duress defense for the attempted arson."
-->

## Issue 3 — argpass-sonnet

**Q4.** Assume Marcus successfully asserts a duress defense for the conspiracy. Can Dexter raise Marcus's duress as a defense to his own accomplice liability?

(a) Yes, because duress is a justification that renders the underlying act socially desirable, meaning any party who assists shares in the defense.
(b) No, because duress is merely an excuse that protects the coerced actor, not a justification that renders the underlying act lawful for helpers. <!-- correct -->
(c) No, because accomplice liability is strictly determined by the principal's ultimate conviction, regardless of any affirmative defenses the principal raises.
(d) Yes, because the justification/excuse distinction only applies to self-defense claims, allowing duress to extend derivative immunity to external accomplices.
(e) No, because Dexter lacked a reasonable belief that Marcus was under an imminent threat of death or serious bodily injury at the time.

**Answer:** (b)

**Explanation:** Criminal defenses are divided into justifications (which render the act lawful and are shared by accomplices) and excuses (which recognize the act is wrongful but withhold punishment due to the actor's lack of moral culpability). Duress is the paradigmatic excuse. Because it is personal to Marcus, it does not transfer to Dexter. (a) is incorrect because it falsely categorizes duress as a justification. (c) is incorrect because modern law generally allows an accomplice to be convicted even if the principal is excused or acquitted, decoupling their legal fates. (d) is incorrect because the justification/excuse distinction is a fundamental doctrine applying across all affirmative defenses, not just self-defense. (e) is incorrect because an accomplice's subjective belief about the principal's duress is irrelevant to whether the principal's defense transfers to the accomplice.

**Tags:** chapters: [18, 21], topics: [accomplice liability, justification vs excuse], difficulty: medium, cognitive: application

**Grounding:** Chapter 21 - justification-vs-excuse

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might argue that duress functions as a justification by choosing the lesser of two evils (e.g., committing a crime to save a life), meaning the act itself becomes socially tolerable. If the act is justified, an accomplice aiding the act would share the defense, making (a) correct under this minority or misunderstood view.
(b) Argument-for: This option correctly identifies the core doctrinal distinction: justifications render the act lawful and transfer to accomplices, while excuses concede the act is unlawful but forgive the actor due to a lack of culpability. Because duress is an excuse, it is personal to Marcus and does not shield Dexter. Therefore, (b) is the doctrinally accurate conclusion and rationale.
(c) Argument-for: A student could rely on the strict common-law rule of derivative liability, where an accomplice's fate was tied directly to the principal's conviction. They might mistakenly conclude that the principal's personal defenses legally dictate the accomplice's liability across the board, making this seem like a rigid procedural rule.
(d) Argument-for: A student might recall learning the justification/excuse distinction primarily during the self-defense unit (e.g., perfect vs. imperfect self-defense) and wrongly conclude it is a doctrine exclusive to self-defense. Under this logic, duress would bypass this limitation and grant derivative immunity to accomplices.
(e) Argument-for: A student could focus on the mens rea of the accomplice, reasoning that if Dexter didn't reasonably believe Marcus was in danger, Dexter lacked a defensive or mitigating mindset. Thus, they might conclude Dexter's failure to claim the defense stems factually from his own lack of a reasonable belief about the threat, rendering (e) a plausible factual rationale.

Head-to-head: Option (b) is the clear, doctrinally correct answer based on the fundamental distinction between justification and excuse. Options (a) and (d) fall easily because they rely on explicit misstatements of black-letter law (duress is universally an excuse; the justification/excuse distinction applies to all defenses). Option (c) relies on an outdated common-law rule that modern statutes explicitly reject, and it contradictorily uses this rule to say "No" when strict derivative liability would actually result in a "Yes" if Marcus avoids conviction. Option (e) correctly states the outcome ("No") but relies on an assumed fact not in the prompt (Dexter's reasonable belief) and implies it is the dispositive legal reason. However, (e) lacks the absolute phrasing required by the strict close-call standard to guarantee it constitutes an explicitly falsifiable legal claim rather than just a factual misdirection. 

Falsifiable claim per distractor:
- (a): "duress is a justification" — wrong because duress is categorically recognized as an excuse, not a justification.
- (c): "accomplice liability is strictly determined by the principal's ultimate conviction, regardless of..." — wrong because modern accomplice liability is decoupled from the principal's conviction (an accomplice can be convicted even if the principal is excused or acquitted).
- (d): "the justification/excuse distinction only applies to self-defense claims" — wrong because this doctrinal distinction applies universally to all affirmative defenses.
- (e): "because Dexter lacked a reasonable belief..." — wrong legally but lacks a falsifiable absolute legal claim; it merely asserts an unstated fact as the rationale without locking the proposition.

Recommended fix: Edit (e) to include an absolute legal trigger, such as: "No, solely because an accomplice is categorically barred from asserting a principal's defense unless the accomplice independently shared a reasonable belief in the threat."
-->

## Issue 4 — argpass-opus

**Q4.** Assume Marcus successfully asserts a duress defense for the conspiracy. Can Dexter raise Marcus's duress as a defense to his own accomplice liability?

(a) Yes, because duress is a justification that renders the underlying act socially desirable, meaning any party who assists shares in the defense.
(b) No, because duress is merely an excuse that protects the coerced actor, not a justification that renders the underlying act lawful for helpers. <!-- correct -->
(c) No, because accomplice liability is strictly determined by the principal's ultimate conviction, regardless of any affirmative defenses the principal raises.
(d) Yes, because the justification/excuse distinction only applies to self-defense claims, allowing duress to extend derivative immunity to external accomplices.
(e) No, because Dexter lacked a reasonable belief that Marcus was under an imminent threat of death or serious bodily injury at the time.

**Answer:** (b)

**Explanation:** Criminal defenses are divided into justifications (which render the act lawful and are shared by accomplices) and excuses (which recognize the act is wrongful but withhold punishment due to the actor's lack of moral culpability). Duress is the paradigmatic excuse. Because it is personal to Marcus, it does not transfer to Dexter. (a) is incorrect because it falsely categorizes duress as a justification. (c) is incorrect because modern law generally allows an accomplice to be convicted even if the principal is excused or acquitted, decoupling their legal fates. (d) is incorrect because the justification/excuse distinction is a fundamental doctrine applying across all affirmative defenses, not just self-defense. (e) is incorrect because an accomplice's subjective belief about the principal's duress is irrelevant to whether the principal's defense transfers to the accomplice.

**Tags:** chapters: [18, 21], topics: [accomplice liability, justification vs excuse], difficulty: medium, cognitive: application

**Grounding:** Chapter 21 - justification-vs-excuse

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might analogize duress to a choice of evils, treating it essentially as necessity. Since necessity is a justification that renders the act socially acceptable (e.g., breaking a window to escape a fire), and justifications are generally shared with accomplices, a student could conclude duress operates identically and extends to anyone who assists.
(b) Argument-for: This is the correct application of the fundamental dichotomy between justifications and excuses in criminal law. Duress is universally classified as an excuse because it negates the actor's personal blameworthiness without making the underlying criminal act lawful, meaning accomplices who are not personally coerced cannot derive protection from it.
(c) Argument-for: At traditional common law, an accomplice's liability was strictly derivative of the principal's conviction. A student remembering this historical strict derivation rule might assume that accomplice liability is permanently tethered to the principal's final legal outcome, attempting to apply that rigid standard here (despite the paradoxical wording).
(d) Argument-for: A student might recall learning the justification/excuse distinction primarily in the context of self-defense (e.g., perfect vs. imperfect self-defense) and mistakenly assume the dichotomy is a domain-specific rule unique to self-defense rather than a foundational organizing principle for all affirmative defenses.
(e) Argument-for: Mens rea and subjective beliefs are central to many defenses. A student might reason that an accomplice is only blocked from sharing a defense if they lacked the requisite factual awareness of the circumstances creating the defense, thereby importing a "reasonable belief" requirement from substantive defenses directly into the derivative accomplice liability analysis.

Head-to-head: Option (b) is the clear winner because it correctly articulates the exact doctrinal reason why an excuse like duress does not transfer to an accomplice. Options (a) and (d) provide explicit false legal claims locked with absolute language (misclassifying duress as a justification, and limiting the dichotomy "only" to self-defense). Option (c) relies on an overturned common-law rule using absolute language ("strictly determined"), but its internal logic is contradictory: if liability strictly follows the principal's non-conviction via duress, the answer should be "Yes" (Dexter is acquitted), not "No." Finally, option (e) fails the close-call standard because it merely asserts an unstated factual premise ("Dexter lacked a reasonable belief") rather than articulating an explicitly false, falsifiable legal rule. Because (e) contains an implicit legal error rather than an explicit one, and (c) is logically incoherent, the question merits a SHOULD FIX rating.

Falsifiable claim per distractor:
- (a): "duress is a justification" — wrong because canonical criminal doctrine classifies duress as an excuse.
- (c): "accomplice liability is strictly determined by the principal's ultimate conviction, regardless of any affirmative defenses" — wrong because modern law expressly decouples accomplice liability from the principal's conviction, allowing accomplices to be convicted even if the principal is acquitted via a personal excuse.
- (d): "the justification/excuse distinction only applies to self-defense claims" — wrong because the dichotomy broadly categorizes all criminal defenses, distinguishing personal excuses (like insanity and duress) from universally applicable justifications (like necessity).
- (e): "because Dexter lacked a reasonable belief" — wrong because it relies on an unstated factual assumption, thereby failing to lock an explicit false legal rule. It implies Dexter's belief dictates liability, but the personal nature of an excuse categorically bars transfer regardless of the accomplice's subjective belief.

Recommended fix: Change (c) to: "No, because accomplices are categorically barred from sharing in any of the principal's defenses, whether classified as justifications or excuses." Change (e) to: "No, because the transferability of a duress defense to an accomplice is determined solely by whether the accomplice held a reasonable belief regarding the principal's imminent threat."
-->
