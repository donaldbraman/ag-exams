# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Assume that Marcus and Leo formed a conspiracy to commit the arson. Marcus is charged with the watchman's murder under the *Pinkerton* doctrine. Will Marcus be held liable for Leo's act of shooting the watchman?

(a) Yes, because the shooting was a reasonably foreseeable consequence of the conspiracy to burn down a guarded commercial warehouse. <!-- correct -->
(b) Yes, because Pinkerton imposes strict liability on all conspirators for any crime committed by a co-conspirator, regardless of actual foreseeability.
(c) No, because Marcus did not know Leo was armed and therefore could not have specifically intended for the watchman to be killed.
(d) No, because the murder was a substantive offense separate from the agreed-upon arson, requiring a separate bilateral agreement between the parties.
(e) Yes, because Marcus recruited Leo and therefore bears absolute vicarious liability as the organizational leader of the specific criminal enterprise.

**Answer:** (a)

**Explanation:** Under the *Pinkerton* doctrine, a conspirator is liable for any substantive offense committed by a co-conspirator that is reasonably foreseeable and in furtherance of the conspiracy. A watchman being shot during an arson of a guarded warehouse is a reasonably foreseeable consequence of the underlying conspiracy to destroy the property. (b) is wrong because *Pinkerton* requires foreseeability, not absolute strict liability. (c) is wrong because subjective knowledge of the weapon is not required if the violent escalation was objectively foreseeable. (d) is wrong because the entire purpose of *Pinkerton* liability is to hold conspirators liable for unagreed-upon substantive offenses committed in furtherance of the conspiracy. (e) is wrong because criminal liability under *Pinkerton* is based on agency principles among co-conspirators, not vicarious organizational leadership.

**Tags:** chapters: [19], topics: [Pinkerton liability, conspiracy], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 (Conspiracy), pinkerton-doctrine refinement.

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: MUST FIX. The stem uses definite articles ("the arson," "the watchman's murder") and option (a) introduces facts ("guarded commercial warehouse") that do not exist in the stem. This is clearly an orphaned question severed from a larger, missing fact pattern. A student cannot assess foreseeability without these missing facts.
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Bring the missing facts into the stem. Change the stem to: "Assume that Marcus and Leo formed a conspiracy to commit arson at a guarded commercial warehouse. During the operation, Leo encounters a watchman and shoots him. Marcus is charged with the watchman's murder under the Pinkerton doctrine. Will Marcus be held liable for Leo's act of shooting the watchman?"
-->

## Issue 2 — edge-case

**Q4.** Assume that Marcus and Leo formed a conspiracy to commit the arson. Marcus is charged with the watchman's murder under the *Pinkerton* doctrine. Will Marcus be held liable for Leo's act of shooting the watchman?

(a) Yes, because the shooting was a reasonably foreseeable consequence of the conspiracy to burn down a guarded commercial warehouse. <!-- correct -->
(b) Yes, because Pinkerton imposes strict liability on all conspirators for any crime committed by a co-conspirator, regardless of actual foreseeability.
(c) No, because Marcus did not know Leo was armed and therefore could not have specifically intended for the watchman to be killed.
(d) No, because the murder was a substantive offense separate from the agreed-upon arson, requiring a separate bilateral agreement between the parties.
(e) Yes, because Marcus recruited Leo and therefore bears absolute vicarious liability as the organizational leader of the specific criminal enterprise.

**Answer:** (a)

**Explanation:** Under the *Pinkerton* doctrine, a conspirator is liable for any substantive offense committed by a co-conspirator that is reasonably foreseeable and in furtherance of the conspiracy. A watchman being shot during an arson of a guarded warehouse is a reasonably foreseeable consequence of the underlying conspiracy to destroy the property. (b) is wrong because *Pinkerton* requires foreseeability, not absolute strict liability. (c) is wrong because subjective knowledge of the weapon is not required if the violent escalation was objectively foreseeable. (d) is wrong because the entire purpose of *Pinkerton* liability is to hold conspirators liable for unagreed-upon substantive offenses committed in furtherance of the conspiracy. (e) is wrong because criminal liability under *Pinkerton* is based on agency principles among co-conspirators, not vicarious organizational leadership.

**Tags:** chapters: [19], topics: [Pinkerton liability, conspiracy], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 (Conspiracy), pinkerton-doctrine refinement.

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Facts 6 and 7 (Leo hallucinating that the watchman is a "demon") create a severe booby trap for Pinkerton liability. Pinkerton strictly requires that the co-conspirator's substantive crime be committed "in furtherance of" the conspiracy. If Leo shot the watchman due to an independent psychotic delusion rather than to advance the arson, the act falls outside the scope of the conspiracy. 
2. Cross-Doctrine Clashes: The interplay between the insanity defense/mens rea and Pinkerton derivative liability muddies the waters here. If Leo genuinely believed he was shooting a non-human entity, he may lack the mens rea for murder, meaning no substantive murder was technically committed for Marcus to be vicariously liable for.
3. Cross-Question Spoilers: pass
Recommended fix: Add a stipulation to the stem to bypass the hallucination issues and isolate the foreseeability element being tested. For example: "Assume that Marcus and Leo formed a conspiracy to commit the arson, and that Leo committed the murder in furtherance of that conspiracy to eliminate a witness."
-->
