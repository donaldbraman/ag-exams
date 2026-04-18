# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** Can Marcus be convicted of conspiracy to commit arson with Leo, despite Marcus acting under Vance's coercion?

(a) Yes, because Marcus's conduct constituted a unilateral agreement, which is automatically sufficient under traditional common law rules.
(b) No, because Marcus's participation was coerced, negating the specific intent necessary to form a valid conspiratorial agreement.
(c) Yes, because Marcus and Leo genuinely agreed to commit the arson together, satisfying the bilateral agreement requirement. <!-- correct -->
(d) No, because an agreement requires shared financial motivation, which Marcus lacked due to Vance's threats against his family.
(e) Yes, because the overt act of obtaining accelerant retroactively cures any defect in the underlying coerced conspiratorial agreement.

**Answer:** (c)

**Explanation:** Conspiracy requires a genuine agreement to commit a crime. While Marcus was coerced by Vance, duress is an affirmative defense that excuses criminal liability; it does not negate the underlying *mens rea* (intent) required to form the agreement (*Dixon v. United States*). Marcus intentionally and explicitly agreed with Leo to commit the arson. (a) is incorrect because the traditional common law requires a bilateral agreement (two actual, willing minds), not a unilateral one. (b) is incorrect because duress functions as an excuse, not a mechanism that legally negates the specific intent element of the offense. (d) is incorrect because conspiracy law does not require conspirators to share the same underlying personal or financial motive, only the intent to achieve the shared criminal objective. (e) is incorrect because an overt act cannot retroactively create an agreement where none legally existed.

**Tags:** chapters: [19, 21], topics: [conspiracy agreement, duress, mens rea], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 19 - bilateral-unilateral; Chapter 21 - burden-of-proof-duress (Dixon principle that duress excuses rather than negates intent)

<!-- audit: MUST FIX
<check 1>: Fails. The question asks if Marcus can be *convicted*, and (c) answers "Yes." However, if Marcus has a valid duress defense, it serves as a complete affirmative defense that excuses liability, meaning he *cannot* be convicted. 
<check 2>: Pass. The distractors are legally incorrect, but a well-prepared student would be paralyzed by the realization that (c) is legally false regarding the ultimate conviction.
<check 3>: Fails. The explanation suffers from a fatal internal contradiction: it explicitly states that duress "excuses criminal liability," but uses this to justify an option that affirms Marcus can be convicted. 
<check 4>: Fails. The stem simply states Marcus acted under "Vance's coercion" without providing the factual predicates (e.g., imminent threat of death or severe bodily injury) to assess whether the coercion legally qualifies as duress.
<check 5>: Pass. Tests the common law bilateral agreement requirement cleanly.
<check 6>: Pass. No excluded topics present.
<check 7>: Pass. The *Dixon* principle (mens rea vs. excuse) and bilateral agreement doctrines are firmly grounded in the provided maps.
Recommended fix: Change the prompt from asking about ultimate conviction to asking about the elements/prima facie case. E.g., "Does Vance's coercion prevent Marcus from satisfying the elements of conspiracy to commit arson with Leo?" Modify (c) to: "No, because Marcus and Leo genuinely agreed to commit the arson together, and coercion functions as an affirmative defense rather than negating conspiratorial intent."
-->

## Issue 2 — edge-case

**Q3.** Can Marcus be convicted of conspiracy to commit arson with Leo, despite Marcus acting under Vance's coercion?

(a) Yes, because Marcus's conduct constituted a unilateral agreement, which is automatically sufficient under traditional common law rules.
(b) No, because Marcus's participation was coerced, negating the specific intent necessary to form a valid conspiratorial agreement.
(c) Yes, because Marcus and Leo genuinely agreed to commit the arson together, satisfying the bilateral agreement requirement. <!-- correct -->
(d) No, because an agreement requires shared financial motivation, which Marcus lacked due to Vance's threats against his family.
(e) Yes, because the overt act of obtaining accelerant retroactively cures any defect in the underlying coerced conspiratorial agreement.

**Answer:** (c)

**Explanation:** Conspiracy requires a genuine agreement to commit a crime. While Marcus was coerced by Vance, duress is an affirmative defense that excuses criminal liability; it does not negate the underlying *mens rea* (intent) required to form the agreement (*Dixon v. United States*). Marcus intentionally and explicitly agreed with Leo to commit the arson. (a) is incorrect because the traditional common law requires a bilateral agreement (two actual, willing minds), not a unilateral one. (b) is incorrect because duress functions as an excuse, not a mechanism that legally negates the specific intent element of the offense. (d) is incorrect because conspiracy law does not require conspirators to share the same underlying personal or financial motive, only the intent to achieve the shared criminal objective. (e) is incorrect because an overt act cannot retroactively create an agreement where none legally existed.

**Tags:** chapters: [19, 21], topics: [conspiracy agreement, duress, mens rea], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 19 - bilateral-unilateral; Chapter 21 - burden-of-proof-duress (Dixon principle that duress excuses rather than negates intent)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The question asks if Marcus can be "convicted." Because Marcus is acting under a severe threat to his family's life, he likely has a valid affirmative defense of duress (which is the explicit doctrinal target of Q5). If a student correctly identifies that duress will excuse his conduct, they will accurately conclude he *cannot* be convicted, making the "Yes" in option (c) factually problematic despite its correct analysis of the *prima facie* agreement element.
2. Cross-Doctrine Clashes: Duress acts as an excuse. Asking about ultimate conviction tangles the *mens rea* / actus reus of conspiracy with the affirmative defense of excuse. 
3. Cross-Question Spoilers: Q5 explicitly tests Marcus's duress defense. Asking if he can be "convicted" in Q3 spoils or depends on the outcome of Q5. 
Recommended fix: Change the question stem to isolate the formation of the agreement, removing the word "convicted". For example: "Can Marcus's coerced participation satisfy the agreement element for a conspiracy charge with Leo?"
-->

## Issue 3 — argpass-opus

**Q3.** Can Marcus be convicted of conspiracy to commit arson with Leo, despite Marcus acting under Vance's coercion?

(a) Yes, because Marcus's conduct constituted a unilateral agreement, which is automatically sufficient under traditional common law rules.
(b) No, because Marcus's participation was coerced, negating the specific intent necessary to form a valid conspiratorial agreement.
(c) Yes, because Marcus and Leo genuinely agreed to commit the arson together, satisfying the bilateral agreement requirement. <!-- correct -->
(d) No, because an agreement requires shared financial motivation, which Marcus lacked due to Vance's threats against his family.
(e) Yes, because the overt act of obtaining accelerant retroactively cures any defect in the underlying coerced conspiratorial agreement.

**Answer:** (c)

**Explanation:** Conspiracy requires a genuine agreement to commit a crime. While Marcus was coerced by Vance, duress is an affirmative defense that excuses criminal liability; it does not negate the underlying *mens rea* (intent) required to form the agreement (*Dixon v. United States*). Marcus intentionally and explicitly agreed with Leo to commit the arson. (a) is incorrect because the traditional common law requires a bilateral agreement (two actual, willing minds), not a unilateral one. (b) is incorrect because duress functions as an excuse, not a mechanism that legally negates the specific intent element of the offense. (d) is incorrect because conspiracy law does not require conspirators to share the same underlying personal or financial motive, only the intent to achieve the shared criminal objective. (e) is incorrect because an overt act cannot retroactively create an agreement where none legally existed.

**Tags:** chapters: [19, 21], topics: [conspiracy agreement, duress, mens rea], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 19 - bilateral-unilateral; Chapter 21 - burden-of-proof-duress (Dixon principle that duress excuses rather than negates intent)

<!-- argument-pass: MUST FIX
(a) Argument-for: A student might argue that because Marcus's co-conspirator Leo was uncoerced and willing, Marcus's actions form a unilateral agreement. Some modern statutes apply unilateral approaches to ensnare willing parties even when the other party lacks true intent. The student might mistakenly attribute this modern Model Penal Code approach to traditional common law, concluding that it is "automatically sufficient" to secure a conviction here.
(b) Argument-for: A student could reason that conspiracy requires the specific intent to agree to commit a crime. Since Marcus acted under Vance's coercion, his participation was not an exercise of free will, which practically overrides his autonomous choices. The student could logically but incorrectly conclude that this coercion negates the specific intent necessary to form a genuine conspiratorial agreement, thus preventing a conviction.
(c) Argument-for: Relying on the *Dixon v. United States* principle, a student would recognize that duress acts as an affirmative defense excusing criminal liability, rather than negating the *mens rea* elements of the crime. Because Marcus intentionally agreed with Leo, the bilateral agreement requirement is satisfied from a strict element-checking perspective. The student would select this option believing the question focuses solely on whether the elements of conspiracy were met, overlooking the fact that a successful affirmative defense bars conviction.
(d) Argument-for: Conspiracy requires a shared criminal purpose and a genuine meeting of the minds. A student might argue that if Marcus lacked the same motivation (e.g., financial gain) as Leo and only participated due to threats against his family, there is no true shared objective. This would lead them to incorrectly conclude that the agreement is legally defective because it lacks a shared financial motivation.
(e) Argument-for: Conspiracy often requires both an agreement and an overt act in furtherance of the conspiracy. A student might argue that obtaining the accelerant was a definitive step that ratified any prior coerced agreement. They could reason that this overt act retroactively cures any defect in the initial agreement, effectively locking in the conspiracy and making it punishable.

Head-to-head: 
The distractors all contain explicitly falsifiable legal claims. Distractor (a) misstates traditional common law (which requires bilateral, not unilateral, agreements). Distractor (b) misstates the legal effect of duress under *Dixon*, wrongly claiming it negates specific intent rather than acting as an excuse. Distractor (d) invents a false requirement for shared financial motivation. Distractor (e) invents a false doctrine that an overt act can retroactively cure a missing or defective agreement. However, the keyed answer (c) is highly problematic. The stem asks, "Can Marcus be convicted...?" Keyed answer (c) says "Yes." But as the explanation itself notes, duress "excuses criminal liability." If Marcus's liability is excused by duress, he *cannot* be convicted. Thus, (c) asserts a false legal conclusion based on the facts provided, while (b) asserts the correct ultimate conclusion ("No") using incorrect reasoning. This creates a severe trap for a knowledgeable student who knows duress precludes conviction. 

Falsifiable claim per distractor:
- (a): "automatically sufficient under traditional common law rules" — wrong because traditional common law strictly requires a bilateral agreement, not a unilateral one.
- (b): "negating the specific intent necessary to form a valid conspiratorial agreement" — wrong because duress functions as an affirmative defense that excuses conduct; it does not legally negate the specific intent (*mens rea*) to agree.
- (d): "requires shared financial motivation" — wrong because conspiracy only requires an intent to achieve the shared criminal objective, regardless of divergent underlying personal motives.
- (e): "retroactively cures any defect in the underlying coerced conspiratorial agreement" — wrong because an overt act is a separate element and cannot legally substitute for or retroactively create the underlying agreement.

Recommended fix: Change the question stem to target the intent element directly, avoiding the ultimate conviction conclusion: "Does Vance's coercion negate the agreement element of Marcus's conspiracy charge?" Adjust the options to match this yes/no structure (e.g., change (c) to "No, because Marcus and Leo genuinely agreed to commit the arson together, satisfying the bilateral agreement requirement").
-->
