# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Carmine is charged with the murder of Victor. The prosecution's sole theory is that Carmine is liable for Dominic's actions because they were co-conspirators in the extortion enterprise. Is Carmine guilty of the murder under this theory?

(a) Yes, because a co-conspirator is strictly liable for all criminal offenses committed by other members of the enterprise regardless of foreseeability or the original objective.
(b) Yes, because the murder was committed in furtherance of the extortion conspiracy and was a reasonably foreseeable consequence of engaging in an armed robbery operation. <!-- correct -->
(c) No, because Carmine was not physically present at the restaurant during the altercation and did not provide the specific weapon used in the fatal shooting.
(d) No, because Pinkerton liability explicitly requires the prosecution to prove that Carmine specifically intended for Victor to die during the course of the extortion collection.
(e) No, because the murder was an independent, spontaneous act of self-defense by Dominic that legally broke the causal chain of the original extortion conspiracy.

**Answer:** (b)

**Explanation:** Under the *Pinkerton* doctrine, a co-conspirator is criminally liable for the foreseeable substantive offenses committed by other members of the conspiracy in furtherance of the common enterprise. Because armed robbery and a resulting shooting are reasonably foreseeable consequences of an organized extortion operation, Carmine is liable for Victor's murder even though he was not present. (a) is wrong because *Pinkerton* liability strictly requires the crime to be reasonably foreseeable, not just any crime committed. (c) is wrong because physical presence or direct assistance is the standard for accomplice liability, whereas *Pinkerton* relies entirely on the conspiratorial agency relationship. (d) is wrong because *Pinkerton* explicitly allows conviction without the defendant possessing the specific intent for the collateral substantive crime. (e) is wrong because a death during an extortion collection is a foreseeable continuation of the conspiracy, not an independent break in the causal chain.

**Tags:** chapters: [19], topics: [conspiracy, pinkerton-liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, Pinkerton v. United States

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem is entirely missing the fact pattern needed to answer the question. It refers only to an "extortion enterprise," but the options and explanation assume unstated facts about a restaurant, an armed robbery operation, a fatal shooting, and a claim of self-defense. Without these facts, a student cannot eliminate fact-based distractors like (e).
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Insert the missing factual scenario into the stem (describing the extortion collection at the restaurant, the armed robbery/altercation, and Dominic's shooting of Victor).
-->

## Issue 2 — edge-case

**Q10.** Carmine is charged with the murder of Victor. The prosecution's sole theory is that Carmine is liable for Dominic's actions because they were co-conspirators in the extortion enterprise. Is Carmine guilty of the murder under this theory?

(a) Yes, because a co-conspirator is strictly liable for all criminal offenses committed by other members of the enterprise regardless of foreseeability or the original objective.
(b) Yes, because the murder was committed in furtherance of the extortion conspiracy and was a reasonably foreseeable consequence of engaging in an armed robbery operation. <!-- correct -->
(c) No, because Carmine was not physically present at the restaurant during the altercation and did not provide the specific weapon used in the fatal shooting.
(d) No, because Pinkerton liability explicitly requires the prosecution to prove that Carmine specifically intended for Victor to die during the course of the extortion collection.
(e) No, because the murder was an independent, spontaneous act of self-defense by Dominic that legally broke the causal chain of the original extortion conspiracy.

**Answer:** (b)

**Explanation:** Under the *Pinkerton* doctrine, a co-conspirator is criminally liable for the foreseeable substantive offenses committed by other members of the conspiracy in furtherance of the common enterprise. Because armed robbery and a resulting shooting are reasonably foreseeable consequences of an organized extortion operation, Carmine is liable for Victor's murder even though he was not present. (a) is wrong because *Pinkerton* liability strictly requires the crime to be reasonably foreseeable, not just any crime committed. (c) is wrong because physical presence or direct assistance is the standard for accomplice liability, whereas *Pinkerton* relies entirely on the conspiratorial agency relationship. (d) is wrong because *Pinkerton* explicitly allows conviction without the defendant possessing the specific intent for the collateral substantive crime. (e) is wrong because a death during an extortion collection is a foreseeable continuation of the conspiracy, not an independent break in the causal chain.

**Tags:** chapters: [19], topics: [conspiracy, pinkerton-liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, Pinkerton v. United States

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Fact 8 in the Scenario Package is a stray drafting note ("Change phrasing from 'extortion run' to 'collection run' or 'robbery'...") rather than the actual substantive facts of Victor's death. Because the facts of the encounter are literally missing, students cannot accurately analyze foreseeability or Pinkerton liability. Furthermore, Q10's stem refers to an "extortion enterprise," while the correct option (b) jumps to an "armed robbery operation"—a factual and legal disconnect that the missing facts were supposed to bridge.
2. Cross-Doctrine Clashes: Pass.
3. Cross-Question Spoilers: Pass.
Recommended fix: Replace the Fact 8 drafting note with the actual narrative of Dominic committing the armed robbery against Victor and the subsequent fatal shooting. Ensure Q10's stem and Option (b) use consistent terminology (e.g., changing "extortion enterprise" in the stem to "armed robbery/collection enterprise" to match the correct answer).
-->

## Issue 3 — argpass-sonnet

**Q10.** Carmine is charged with the murder of Victor. The prosecution's sole theory is that Carmine is liable for Dominic's actions because they were co-conspirators in the extortion enterprise. Is Carmine guilty of the murder under this theory?

(a) Yes, because a co-conspirator is strictly liable for all criminal offenses committed by other members of the enterprise regardless of foreseeability or the original objective.
(b) Yes, because the murder was committed in furtherance of the extortion conspiracy and was a reasonably foreseeable consequence of engaging in an armed robbery operation. <!-- correct -->
(c) No, because Carmine was not physically present at the restaurant during the altercation and did not provide the specific weapon used in the fatal shooting.
(d) No, because Pinkerton liability explicitly requires the prosecution to prove that Carmine specifically intended for Victor to die during the course of the extortion collection.
(e) No, because the murder was an independent, spontaneous act of self-defense by Dominic that legally broke the causal chain of the original extortion conspiracy.

**Answer:** (b)

**Explanation:** Under the *Pinkerton* doctrine, a co-conspirator is criminally liable for the foreseeable substantive offenses committed by other members of the conspiracy in furtherance of the common enterprise. Because armed robbery and a resulting shooting are reasonably foreseeable consequences of an organized extortion operation, Carmine is liable for Victor's murder even though he was not present. (a) is wrong because *Pinkerton* liability strictly requires the crime to be reasonably foreseeable, not just any crime committed. (c) is wrong because physical presence or direct assistance is the standard for accomplice liability, whereas *Pinkerton* relies entirely on the conspiratorial agency relationship. (d) is wrong because *Pinkerton* explicitly allows conviction without the defendant possessing the specific intent for the collateral substantive crime. (e) is wrong because a death during an extortion collection is a foreseeable continuation of the conspiracy, not an independent break in the causal chain.

**Tags:** chapters: [19], topics: [conspiracy, pinkerton-liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, Pinkerton v. United States

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue this if they misremember the scope of conspiracy liability, believing that the mutual agency of a conspiracy makes co-conspirators strictly liable for any and all crimes committed by members, effectively confusing Pinkerton liability with an absolute strict liability standard.
(b) Argument-for: This is the keyed answer. A student would choose this because it correctly identifies the two prongs of Pinkerton liability: the substantive crime was committed in furtherance of the conspiracy and was a reasonably foreseeable consequence of the criminal agreement. 
(c) Argument-for: A student might choose this by confusing Pinkerton conspiracy liability with accomplice liability (aiding and abetting), incorrectly believing that actual physical presence or direct provision of an instrumentality (the weapon) is legally required to be convicted of the substantive crime.
(d) Argument-for: A student could select this if they believe that a defendant cannot be convicted of a specific intent crime like murder without personally possessing the requisite specific intent, thereby misunderstanding Pinkerton's rule that foreseeability substitutes for the mens rea of the collateral offense.
(e) Argument-for: A student might argue that a spontaneous act by a co-conspirator constitutes a "frolic and detour" that falls outside the scope of the conspiracy, reasoning that an independent act of self-defense severs the legal causation required to hold a co-conspirator liable.

Head-to-head: Option (b) correctly identifies the Pinkerton standard (furtherance and foreseeability) but contains a glaring factual mismatch with the prompt, referring to an "armed robbery operation" instead of the "extortion enterprise" established in the question stem. Option (a) is definitively wrong because it explicitly asserts strict liability "regardless of foreseeability." Option (c) is incorrect because it implies presence is legally necessary. Option (d) contains an explicitly false claim that Pinkerton "explicitly requires" specific intent. Option (e) relies on an incorrect legal conclusion regarding causal chains in the context of inherently dangerous felonies like extortion. Due to the factual mismatch in the keyed answer (b) introducing unstated facts about an armed robbery, this question explicitly requires an edit to be valid.

Falsifiable claim per distractor:
- (a): "regardless of foreseeability or the original objective" — wrong because Pinkerton liability explicitly requires the substantive offense to be a reasonably foreseeable consequence of the conspiracy.
- (c): "No, because Carmine was not physically present... and did not provide the specific weapon" — wrong because Pinkerton liability does not require physical presence or direct assistance, unlike accomplice liability.
- (d): "explicitly requires the prosecution to prove that Carmine specifically intended" — wrong because Pinkerton explicitly allows conviction for foreseeable substantive crimes committed by co-conspirators without requiring specific intent for those collateral crimes.
- (e): "legally broke the causal chain of the original extortion conspiracy" — wrong because violence or death resulting from an extortion operation is legally considered a foreseeable consequence in furtherance of the conspiracy, not a superseding break in the causal chain.

Recommended fix: In option (b), change "engaging in an armed robbery operation" to "engaging in an extortion enterprise" to align with the prompt's established facts.
-->

## Issue 4 — argpass-opus

**Q10.** Carmine is charged with the murder of Victor. The prosecution's sole theory is that Carmine is liable for Dominic's actions because they were co-conspirators in the extortion enterprise. Is Carmine guilty of the murder under this theory?

(a) Yes, because a co-conspirator is strictly liable for all criminal offenses committed by other members of the enterprise regardless of foreseeability or the original objective.
(b) Yes, because the murder was committed in furtherance of the extortion conspiracy and was a reasonably foreseeable consequence of engaging in an armed robbery operation. <!-- correct -->
(c) No, because Carmine was not physically present at the restaurant during the altercation and did not provide the specific weapon used in the fatal shooting.
(d) No, because Pinkerton liability explicitly requires the prosecution to prove that Carmine specifically intended for Victor to die during the course of the extortion collection.
(e) No, because the murder was an independent, spontaneous act of self-defense by Dominic that legally broke the causal chain of the original extortion conspiracy.

**Answer:** (b)

**Explanation:** Under the *Pinkerton* doctrine, a co-conspirator is criminally liable for the foreseeable substantive offenses committed by other members of the conspiracy in furtherance of the common enterprise. Because armed robbery and a resulting shooting are reasonably foreseeable consequences of an organized extortion operation, Carmine is liable for Victor's murder even though he was not present. (a) is wrong because *Pinkerton* liability strictly requires the crime to be reasonably foreseeable, not just any crime committed. (c) is wrong because physical presence or direct assistance is the standard for accomplice liability, whereas *Pinkerton* relies entirely on the conspiratorial agency relationship. (d) is wrong because *Pinkerton* explicitly allows conviction without the defendant possessing the specific intent for the collateral substantive crime. (e) is wrong because a death during an extortion collection is a foreseeable continuation of the conspiracy, not an independent break in the causal chain.

**Tags:** chapters: [19], topics: [conspiracy, pinkerton-liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, Pinkerton v. United States

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that once a conspiracy is established, all members bear responsibility for the substantive crimes committed by any co-conspirator. Under a broad or misremembered interpretation of conspiratorial agency, a student might believe this acts as a form of strict liability for any crime committed by a member of the enterprise, rendering foreseeability irrelevant.
(b) Argument-for: A student could argue that this option correctly applies the *Pinkerton* doctrine. Under *Pinkerton v. United States*, a conspirator is liable for substantive offenses committed by a co-conspirator if they are in furtherance of the conspiracy and reasonably foreseeable. Escalation into violence, including robbery and murder, is a foreseeable consequence of an extortion enterprise.
(c) Argument-for: A student might argue from the perspective of jurisdictions (like those following the Model Penal Code) that reject *Pinkerton*. In such jurisdictions, mere conspiracy is insufficient for liability on the substantive crime; the prosecution must prove accomplice liability, which generally requires physical presence, aiding, or abetting—none of which Carmine provided.
(d) Argument-for: A student might argue that a conviction for a specific-intent crime like murder requires the prosecution to prove the defendant actually possessed that specific intent. Some students might conflate accomplice liability requirements with *Pinkerton* and assume that vicarious liability requires specific intent for the collateral substantive crime.
(e) Argument-for: A student could argue that if Dominic acted independently and spontaneously in self-defense, the act was not in furtherance of the conspiracy. Under *Pinkerton*, crimes that fall outside the scope of the conspiracy's objectives do not trigger vicarious liability, meaning an independent act severs the causal chain.

Head-to-head:
The fatal flaw in this question is that the stem is completely missing the underlying fact pattern. As "Q10", it was likely part of a fact-pattern cluster. The prompt mentions only an "extortion enterprise," yet the options reference a wealth of missing facts: an "armed robbery operation" (b), "the restaurant" and a "specific weapon" (c), and a "spontaneous act of self-defense" (e). Because the keyed answer (b) and multiple distractors rely heavily on these missing facts to determine whether the murder was in furtherance of the conspiracy or reasonably foreseeable, the question is impossible to answer in its current isolated state. Without the facts, (e) is legally plausible, as an independent act outside the scope of the conspiracy would indeed defeat *Pinkerton* liability.

Falsifiable claim per distractor:
- (a): "regardless of foreseeability or the original objective" — wrong because *Pinkerton* explicitly requires the substantive crime to be both reasonably foreseeable and in furtherance of the conspiracy's objective.
- (c): "because Carmine was not physically present at the restaurant" — wrong because *Pinkerton* liability categorically does not require physical presence or direct assistance (accomplice acts).
- (d): "Pinkerton liability explicitly requires the prosecution to prove that Carmine specifically intended for Victor to die" — wrong because *Pinkerton* substitutes reasonable foreseeability for the specific intent of the substantive collateral offense.
- (e): "murder was an independent, spontaneous act of self-defense" — wrong factually (assuming the missing fact pattern establishes it was a foreseeable act in furtherance of the conspiracy), but lacks a standalone false legal claim without the context of the missing facts.

Recommended fix: MUST FIX. Insert the missing shared fact pattern into the question stem describing the extortion operation, the restaurant altercation, the armed robbery, and the shooting. Otherwise, the question is unanswerable.
-->
