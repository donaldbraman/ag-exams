# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q5.** Assume George is guilty of attempted murder. Can Felix be held liable for attempted murder under the Pinkerton doctrine?

(a) Yes, Felix can be held liable under Pinkerton. George's escalation to attempted murder was a foreseeable act committed in furtherance of the conspiracy to defend the turf by any means necessary. <!-- correct -->
(b) Yes, Felix can be held liable under Pinkerton. The doctrine holds all organized crew leaders strictly liable for their subordinates' violent acts regardless of foreseeability or furtherance.
(c) No, Felix cannot be held liable under Pinkerton. He explicitly instructed George only to fire into the air, which strictly defeats the furtherance requirement of the doctrine.
(d) No, Felix cannot be held liable under Pinkerton. The doctrine requires that the defendant personally participate in the target offense or provide substantial physical aid at the scene.
(e) Yes, Felix can be held liable under Pinkerton. Because he provided the weapon, he is directly liable as a principal rather than vicariously liable through the conspiracy.

**Answer:** (a)

**Explanation:** Under the *Pinkerton* doctrine, a conspirator is vicariously liable for the foreseeable substantive offenses committed by co-conspirators in furtherance of the ongoing conspiracy. George's escalation to attempted murder was a foreseeable consequence of an armed mission to defend drug turf. (b) is wrong because *Pinkerton* requires foreseeability and furtherance, not strict liability for all acts. (c) is wrong because an act can be in furtherance of the general conspiracy even if the specific escalation was not explicitly authorized. (d) is wrong because *Pinkerton* specifically replaces the need for personal participation or substantial aid. (e) is wrong because providing the weapon makes Felix an accomplice to the assault, but his liability for the *murder attempt* specifically relies on *Pinkerton*.

**Tags:** chapters: [19], topics: [Pinkerton liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 - Pinkerton Vicarious Liability Doctrine (*Pinkerton v. United States*)

<!-- GROUNDING-FAIL: Pinkerton liability is not in any chapter map. The closest taught doctrines are: none (meta-map missing from prompt context). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q5.** Assume George is guilty of attempted murder. Can Felix be held liable for attempted murder under the Pinkerton doctrine?

(a) Yes, Felix can be held liable under Pinkerton. George's escalation to attempted murder was a foreseeable act committed in furtherance of the conspiracy to defend the turf by any means necessary. <!-- correct -->
(b) Yes, Felix can be held liable under Pinkerton. The doctrine holds all organized crew leaders strictly liable for their subordinates' violent acts regardless of foreseeability or furtherance.
(c) No, Felix cannot be held liable under Pinkerton. He explicitly instructed George only to fire into the air, which strictly defeats the furtherance requirement of the doctrine.
(d) No, Felix cannot be held liable under Pinkerton. The doctrine requires that the defendant personally participate in the target offense or provide substantial physical aid at the scene.
(e) Yes, Felix can be held liable under Pinkerton. Because he provided the weapon, he is directly liable as a principal rather than vicariously liable through the conspiracy.

**Answer:** (a)

**Explanation:** Under the *Pinkerton* doctrine, a conspirator is vicariously liable for the foreseeable substantive offenses committed by co-conspirators in furtherance of the ongoing conspiracy. George's escalation to attempted murder was a foreseeable consequence of an armed mission to defend drug turf. (b) is wrong because *Pinkerton* requires foreseeability and furtherance, not strict liability for all acts. (c) is wrong because an act can be in furtherance of the general conspiracy even if the specific escalation was not explicitly authorized. (d) is wrong because *Pinkerton* specifically replaces the need for personal participation or substantial aid. (e) is wrong because providing the weapon makes Felix an accomplice to the assault, but his liability for the *murder attempt* specifically relies on *Pinkerton*.

**Tags:** chapters: [19], topics: [Pinkerton liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 - Pinkerton Vicarious Liability Doctrine (*Pinkerton v. United States*)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: FAIL. The stem completely lacks a fact pattern. The answer options and explanation reference facts that are never established (e.g., George and Felix's conspiracy, defending turf, Felix providing a weapon, and an instruction to only fire into the air). A student cannot evaluate foreseeability or furtherance without these facts.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Insert the missing scenario into the question stem before asking if Felix can be held liable (e.g., "Felix, the leader of a drug crew, gave George a gun and told him to defend their turf by firing into the air to scare off rivals..."). 
-->

## Issue 3 — edge-case

**Q5.** Assume George is guilty of attempted murder. Can Felix be held liable for attempted murder under the Pinkerton doctrine?

(a) Yes, Felix can be held liable under Pinkerton. George's escalation to attempted murder was a foreseeable act committed in furtherance of the conspiracy to defend the turf by any means necessary. <!-- correct -->
(b) Yes, Felix can be held liable under Pinkerton. The doctrine holds all organized crew leaders strictly liable for their subordinates' violent acts regardless of foreseeability or furtherance.
(c) No, Felix cannot be held liable under Pinkerton. He explicitly instructed George only to fire into the air, which strictly defeats the furtherance requirement of the doctrine.
(d) No, Felix cannot be held liable under Pinkerton. The doctrine requires that the defendant personally participate in the target offense or provide substantial physical aid at the scene.
(e) Yes, Felix can be held liable under Pinkerton. Because he provided the weapon, he is directly liable as a principal rather than vicariously liable through the conspiracy.

**Answer:** (a)

**Explanation:** Under the *Pinkerton* doctrine, a conspirator is vicariously liable for the foreseeable substantive offenses committed by co-conspirators in furtherance of the ongoing conspiracy. George's escalation to attempted murder was a foreseeable consequence of an armed mission to defend drug turf. (b) is wrong because *Pinkerton* requires foreseeability and furtherance, not strict liability for all acts. (c) is wrong because an act can be in furtherance of the general conspiracy even if the specific escalation was not explicitly authorized. (d) is wrong because *Pinkerton* specifically replaces the need for personal participation or substantial aid. (e) is wrong because providing the weapon makes Felix an accomplice to the assault, but his liability for the *murder attempt* specifically relies on *Pinkerton*.

**Tags:** chapters: [19], topics: [Pinkerton liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 - Pinkerton Vicarious Liability Doctrine (*Pinkerton v. United States*)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The explanation for (e) asserts Felix is an "accomplice to the assault," but George was arrested three blocks away and never committed an assault (merely an attempt).
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: The explanation for (e) claims Felix's liability for the attempt "specifically relies on Pinkerton," which implicitly resolves the accomplice mens rea issue tested in Q3. If a student concludes in Q3 that Felix has accomplice mens rea (due to supplying the gun and the "by any means" speech), they will find this explanation debatable. 
Recommended fix: Modify the explanation for (e) to remove the reference to "assault," and simply clarify that Pinkerton provides a valid, independent basis for vicarious liability, rendering the mutually exclusive "rather than" phrasing in option (e) incorrect.
-->
