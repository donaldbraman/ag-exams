# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q13.** The DA charges Avon with the homicide of Inspector Greggs under the *Pinkerton* doctrine, based on the conspiracy between Avon and Marlowe to operate the drug lab. Which of the following best describes the application of *Pinkerton* to these facts?

(a) Avon is guilty only if he purposefully intended for Inspector Greggs to die in the fire as a direct consequence of the drug lab operations.
(b) Avon is guilty because any death that occurs during the chronological timeline of a conspiracy is strictly imputed to all participating co-conspirators.
(c) Avon is guilty if the lethal chemical fire was a reasonably foreseeable consequence of the conspiracy to operate the illicit drug manufacturing lab. <!-- correct -->
(d) Avon is not guilty because *Pinkerton* liability strictly requires the co-conspirator to be physically present when the substantive offense is actually committed.
(e) Avon is not guilty because *Pinkerton* liability only applies to the specific target crimes of the conspiracy, not to collateral offenses like homicide.

**Answer:** (c)

**Explanation:** Under the *Pinkerton* doctrine, a co-conspirator is criminally liable for the substantive offenses committed by other co-conspirators if those crimes were committed in furtherance of the conspiracy and were reasonably foreseeable consequences of the agreement. A massive chemical fire and resulting deaths are arguably foreseeable consequences of operating an illicit, unregulated drug lab. (a) fails because *Pinkerton* does not require purposeful intent for the collateral crime, only foreseeability. (b) fails because strict temporal imputation is incorrect; the crime must be in furtherance of the conspiracy and foreseeable. (d) fails because physical presence is entirely irrelevant to *Pinkerton* vicarious liability. (e) fails because the primary purpose of *Pinkerton* is precisely to impute liability for collateral foreseeable crimes committed by co-conspirators.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 (pinkerton-doctrine)

<!-- audit: MUST FIX
check 1: fail. Option (c) is legally incomplete. *Pinkerton* requires that a co-conspirator actually commit a substantive offense in furtherance of the conspiracy. Option (c) states Avon is guilty merely if the fire was a foreseeable consequence, omitting the absolute requirement that his co-conspirator (Marlowe) committed the underlying crime (e.g., recklessly causing the fire) in furtherance of the agreement.
check 2: pass. The distractors are clearly doctrinally incorrect.
check 3: pass. The explanation accurately states the full *Pinkerton* rule (including the "in furtherance" requirement that option (c) drops).
check 4: fail. The stem completely omits the factual scenario. It asks how the doctrine applies to "these facts," but provides no facts about a chemical fire, who started it, or how Inspector Greggs died. The student is forced to hallucinate the scenario based on the answer choices.
check 5: pass.
check 6: pass.
check 7: pass.
Recommended fix: Add the missing facts to the stem (e.g., "While cooking drugs, Marlowe recklessly causes a chemical fire that kills Inspector Greggs."). Revise (c) to correctly capture the full rule: "Avon is guilty if Marlowe causing the lethal fire was an act in furtherance of the conspiracy and a reasonably foreseeable consequence of operating the lab."
-->

## Issue 2 — edge-case

**Q13.** The DA charges Avon with the homicide of Inspector Greggs under the *Pinkerton* doctrine, based on the conspiracy between Avon and Marlowe to operate the drug lab. Which of the following best describes the application of *Pinkerton* to these facts?

(a) Avon is guilty only if he purposefully intended for Inspector Greggs to die in the fire as a direct consequence of the drug lab operations.
(b) Avon is guilty because any death that occurs during the chronological timeline of a conspiracy is strictly imputed to all participating co-conspirators.
(c) Avon is guilty if the lethal chemical fire was a reasonably foreseeable consequence of the conspiracy to operate the illicit drug manufacturing lab. <!-- correct -->
(d) Avon is not guilty because *Pinkerton* liability strictly requires the co-conspirator to be physically present when the substantive offense is actually committed.
(e) Avon is not guilty because *Pinkerton* liability only applies to the specific target crimes of the conspiracy, not to collateral offenses like homicide.

**Answer:** (c)

**Explanation:** Under the *Pinkerton* doctrine, a co-conspirator is criminally liable for the substantive offenses committed by other co-conspirators if those crimes were committed in furtherance of the conspiracy and were reasonably foreseeable consequences of the agreement. A massive chemical fire and resulting deaths are arguably foreseeable consequences of operating an illicit, unregulated drug lab. (a) fails because *Pinkerton* does not require purposeful intent for the collateral crime, only foreseeability. (b) fails because strict temporal imputation is incorrect; the crime must be in furtherance of the conspiracy and foreseeable. (d) fails because physical presence is entirely irrelevant to *Pinkerton* vicarious liability. (e) fails because the primary purpose of *Pinkerton* is precisely to impute liability for collateral foreseeable crimes committed by co-conspirators.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 (pinkerton-doctrine)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The termite rot in Fact 6 ("weakened entirely by decades of termite rot rather than the fire") strongly invites an independent superseding cause defense. Because Pinkerton liability is strictly derivative, if the underlying homicide fails on proximate causation due to this bizarre coincidental weakness, no homicide was legally committed, meaning Avon cannot be vicariously guilty. 
2. Cross-Doctrine Clashes: Option (c) states Avon "is guilty if" the fire was foreseeable. This absolute condition creates a false sufficiency: it ignores the requirement that the underlying crime be committed "in furtherance" of the conspiracy, and completely bypasses the proximate causation hurdle for the death. Additionally, a "chemical fire" is an event, not a substantive offense.
3. Cross-Question Spoilers: Q2 directly tests the proximate causation of Greggs's death. If a student concludes in Q2 that the freak termite rot breaks proximate cause for the principal, they are left with no valid correct option in Q13, as (c) forces a guilty verdict simply based on the foreseeability of the fire.
Recommended fix: Soften the absolute phrasing and correct the doctrine in (c) by changing it to: "(c) Avon may be held liable for the homicide if the resulting death was a reasonably foreseeable consequence of acts committed in furtherance of the drug conspiracy."
-->
