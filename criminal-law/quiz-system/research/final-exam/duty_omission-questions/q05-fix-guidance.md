# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Assume Blake is charged with attempted murder of Chris for complying with Alex and locking the door. Is Blake guilty of attempt?

(a) Guilty, because locking the door created a substantial risk of death that satisfies the mens rea for attempt.
(b) Not guilty, because attempt requires the specific intent to kill, and Blake acted out of terror, not purpose. <!-- correct -->
(c) Guilty, because his contractual duty to act as a medical caretaker replaces the need to prove subjective intent.
(d) Not guilty, because locking a door is merely preparatory and does not constitute a substantial step toward murder.
(e) Not guilty, because Dana's subsequent intervention makes it legally impossible for Blake to be convicted of any attempt.

**Answer:** (b)

**Explanation:** (b) is correct because criminal attempt is a specific intent crime. It requires the purpose to commit the target offense (here, the purpose to cause Chris's death). Even though Blake breached a duty and committed an actus reus, he locked the door out of sheer terror for his own life, lacking the specific intent to kill Chris. (a) is wrong because creating a substantial risk of death is recklessness, which is legally insufficient for attempt liability. (c) is wrong because a contractual duty establishes the actus reus for omission but does not substitute for the required mens rea of attempt. (d) is wrong because locking the door while a person is actively dying is a completed omission and easily satisfies the substantial step requirement. (e) is wrong because intervening causes affect completed homicide liability, not attempt.

**Tags:** chapters: [17], topics: [attempt, specific-intent], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 - Mens Rea for Attempt (Specific Intent)

<!-- audit: MUST FIX
Check 1: fails. The marked answer and explanation conflate motive (terror) with a lack of mens rea (purpose). A person acting under a threat (terror) can still act with the specific intent (purpose) to cause a result as a means of self-preservation. Duress/terror does not automatically negate specific intent.
Check 2: fails. A prepared student could correctly identify that (b) relies on a false dichotomy between terror and purpose. If the missing facts show Blake locked the door intending for Chris to die to appease an attacker, Blake would have the requisite specific intent, making (b) incorrect.
Check 3: fails. The explanation reinforces the false dichotomy, stating he acted out of terror "lacking the specific intent," without clarifying whether his conscious object was Chris's death or merely securing the door with knowledge of the risk to Chris.
Check 4: fails. The question is a child question severed from its parent scenario. It relies on missing facts (Alex, Dana, Chris, a medical contract, locking a door) not provided in the stem.
Check 5: pass.
Check 6: pass.
Check 7: pass.
Recommended fix: Reattach the master fact pattern. Rewrite (b) and the explanation to rely squarely on the purpose vs. knowledge distinction for attempt mens rea (e.g., "Not guilty, because attempt requires the specific intent to kill, and Blake merely knew Chris might die rather than having Chris's death as his conscious object").
-->

## Issue 2 — edge-case

**Q5.** Assume Blake is charged with attempted murder of Chris for complying with Alex and locking the door. Is Blake guilty of attempt?

(a) Guilty, because locking the door created a substantial risk of death that satisfies the mens rea for attempt.
(b) Not guilty, because attempt requires the specific intent to kill, and Blake acted out of terror, not purpose. <!-- correct -->
(c) Guilty, because his contractual duty to act as a medical caretaker replaces the need to prove subjective intent.
(d) Not guilty, because locking a door is merely preparatory and does not constitute a substantial step toward murder.
(e) Not guilty, because Dana's subsequent intervention makes it legally impossible for Blake to be convicted of any attempt.

**Answer:** (b)

**Explanation:** (b) is correct because criminal attempt is a specific intent crime. It requires the purpose to commit the target offense (here, the purpose to cause Chris's death). Even though Blake breached a duty and committed an actus reus, he locked the door out of sheer terror for his own life, lacking the specific intent to kill Chris. (a) is wrong because creating a substantial risk of death is recklessness, which is legally insufficient for attempt liability. (c) is wrong because a contractual duty establishes the actus reus for omission but does not substitute for the required mens rea of attempt. (d) is wrong because locking the door while a person is actively dying is a completed omission and easily satisfies the substantial step requirement. (e) is wrong because intervening causes affect completed homicide liability, not attempt.

**Tags:** chapters: [17], topics: [attempt, specific-intent], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 - Mens Rea for Attempt (Specific Intent)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: Option (b) implies that "terror" and "purpose" are mutually exclusive. Under criminal law, one can have the specific intent to kill even while acting out of terror (e.g., shooting someone because a gun is to your head). Blake lacked the specific intent to kill because his conscious object was merely to lock the door and appease Alex, not because terror conceptually negates purpose. Furthermore, the explanation for (d) contains a blatant doctrinal error by calling "locking the door" a "completed omission." Locking a deadbolt to isolate someone is an affirmative act (commission), whereas his failure to call 911 was the omission.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Revise Option (b) to: "Not guilty, because attempt requires the specific intent to kill, and Blake's purpose was merely to save his own life, not to cause Chris's death." Revise the explanation for (d) to describe locking the door as an "affirmative act preventing rescue" rather than a "completed omission."
-->
