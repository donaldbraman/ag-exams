# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** Assume, whether or not Silas is convicted, Dante is charged with the murder of Vargas under the *Pinkerton* doctrine. Is Dante legally liable for the homicide?

(a) Guilty, because Silas's specific act of shooting an armed rival dealer to protect the operation was a reasonably foreseeable consequence of the drug conspiracy. <!-- correct -->
(b) Guilty, because the Pinkerton doctrine imposes absolute strict liability on all co-conspirators for any independent criminal acts committed by other members of the enterprise.
(c) Not guilty, because Silas's acute psychotic delusion constituted an independent intervening cause that fundamentally severed the causal chain of extended co-conspirator liability.
(d) Not guilty, because Dante was physically absent from the warehouse during the shooting and had no prior explicit knowledge of Vargas's impending arrival.
(e) Not guilty, because Dante's individual role was strictly limited to distributing the finished product, legally insulating him from the conspiracy's perimeter security operations.

**Answer:** (a)

**Explanation:** Under the *Pinkerton* doctrine, a co-conspirator is liable for the substantive offenses committed by other members if those offenses are committed in furtherance of the conspiracy and are a reasonably foreseeable consequence of the agreement. Shooting a rival dealer who attempts to hijack a high-value synthetic opioid lab is entirely foreseeable within an armed drug trafficking conspiracy. (b) is incorrect because *Pinkerton* liability is not absolute strict liability; it requires the acts to be reasonably foreseeable and in furtherance of the conspiracy. (c) is incorrect because Silas shot Vargas while actively guarding the stash ("protect the castle"), meaning the act was in furtherance of the conspiracy regardless of his internal psychotic framing. (d) is incorrect because physical presence and prior knowledge of the specific substantive offense are explicitly not required under *Pinkerton*. (e) is incorrect because conspirators are liable for the acts of their co-conspirators regardless of how the group divides labor or roles.

**Tags:** chapters: [19], topics: [pinkerton liability, conspiracy, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19: pinkerton-doctrine

<!-- audit: MUST FIX
check 1: pass (The legal standard applied to option A is accurate for Pinkerton liability.)
check 2: pass (The distractors correctly apply incorrect rules or misapply elements of Pinkerton.)
check 3: pass (The explanation properly tracks the elements of the Pinkerton doctrine.)
check 4: fail (The question completely lacks a factual stem. It introduces specific characters—Silas, Dante, Vargas—and scenarios like a warehouse shooting and an acute psychotic delusion without any preceding fact pattern. It is an orphaned sub-question.)
check 5: pass (The prompt explicitly directs the student to apply the Pinkerton doctrine, resolving any MPC/common law jurisdictional split issues.)
check 6: pass (No excluded topics present.)
check 7: pass (Pinkerton doctrine is explicitly covered in Chapter 19.)
check 8: pass (Options are symmetrical in length and structure.)
Recommended fix: Either reintegrate this question with its master fact pattern (if part of a scenario block) or write a complete, self-contained factual stem for it (e.g., "Dante and Silas agree to distribute drugs. Silas guards their stash warehouse. During a shift, Silas experiences an acute psychotic delusion but shoots Vargas, an armed rival dealer, specifically to protect the operation. Assume...")
-->

## Issue 2 — edge-case

**Q6.** Assume, whether or not Silas is convicted, Dante is charged with the murder of Vargas under the *Pinkerton* doctrine. Is Dante legally liable for the homicide?

(a) Guilty, because Silas's specific act of shooting an armed rival dealer to protect the operation was a reasonably foreseeable consequence of the drug conspiracy. <!-- correct -->
(b) Guilty, because the Pinkerton doctrine imposes absolute strict liability on all co-conspirators for any independent criminal acts committed by other members of the enterprise.
(c) Not guilty, because Silas's acute psychotic delusion constituted an independent intervening cause that fundamentally severed the causal chain of extended co-conspirator liability.
(d) Not guilty, because Dante was physically absent from the warehouse during the shooting and had no prior explicit knowledge of Vargas's impending arrival.
(e) Not guilty, because Dante's individual role was strictly limited to distributing the finished product, legally insulating him from the conspiracy's perimeter security operations.

**Answer:** (a)

**Explanation:** Under the *Pinkerton* doctrine, a co-conspirator is liable for the substantive offenses committed by other members if those offenses are committed in furtherance of the conspiracy and are a reasonably foreseeable consequence of the agreement. Shooting a rival dealer who attempts to hijack a high-value synthetic opioid lab is entirely foreseeable within an armed drug trafficking conspiracy. (b) is incorrect because *Pinkerton* liability is not absolute strict liability; it requires the acts to be reasonably foreseeable and in furtherance of the conspiracy. (c) is incorrect because Silas shot Vargas while actively guarding the stash ("protect the castle"), meaning the act was in furtherance of the conspiracy regardless of his internal psychotic framing. (d) is incorrect because physical presence and prior knowledge of the specific substantive offense are explicitly not required under *Pinkerton*. (e) is incorrect because conspirators are liable for the acts of their co-conspirators regardless of how the group divides labor or roles.

**Tags:** chapters: [19], topics: [pinkerton liability, conspiracy, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19: pinkerton-doctrine

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Silas's acute delusion that he was shooting a "monster made of smoke" (Fact 7) prevents him from forming the specific intent to kill a human being. If Silas lacks the *mens rea* for murder, no substantive crime of murder was committed by him. Under the *Pinkerton* doctrine, a defendant can only be vicariously liable for substantive crimes *actually committed* by a co-conspirator. 
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Q5 explicitly tests the "mens rea model" for Silas, confirming that the exam architect is aware Silas may lack the specific intent for murder. If Silas's delusion negates his mens rea, it completely nullifies Dante's *Pinkerton* exposure in Q6, rendering the "correct" answer (a) legally false.
Recommended fix: Add a stipulation to the Q6 stem to seal the loophole. For example: "Assume, for the purposes of this question, that Silas's conduct satisfied the legal elements of murder. Under the *Pinkerton* doctrine, is Dante legally liable for the homicide?"
-->
