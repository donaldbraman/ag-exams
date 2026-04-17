# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Is Silas liable under the *Pinkerton* doctrine for Arthur's actions in locking the door and preventing the 911 call?

(a) Yes, because Arthur's actions were reasonably foreseeable efforts to conceal the drug distribution and avoid police detection, which were done in furtherance of the ongoing conspiracy. <!-- correct -->
(b) Yes, because the Pinkerton doctrine imposes strict criminal liability on all co-conspirators for any crime committed by a confederate, regardless of its foreseeability or specific purpose.
(c) No, because acts of concealment committed after the completion of the core objective of the drug sale fall strictly outside the temporal scope of Pinkerton liability.
(d) No, because Silas verbally protested leaving the motel room, which legally severed his connection to Arthur's subsequent independent acts of knocking the phone and locking the door.
(e) No, because Pinkerton liability only applies to crimes that the conspirators expressly agreed to commit at the explicit formation of the original criminal agreement.

**Answer:** (a)

**Explanation:** (a) is correct. Under the *Pinkerton* doctrine, a conspirator is liable for all reasonably foreseeable substantive crimes committed by co-conspirators in furtherance of the conspiracy. Arthur explicitly stated his motive was to avoid police detection to protect the enterprise and his job. Acts to conceal the crime or escape detection immediately following the core offense are typically considered foreseeable acts in furtherance of the conspiracy. (b) is incorrect because *Pinkerton* is not strict liability; it requires the substantive crime to be foreseeable and in furtherance of the conspiracy. (c) is incorrect because the conspiracy does not instantly terminate the moment money and drugs change hands; immediate escape and concealment are within its scope. (d) is incorrect because a mere verbal protest without effectively thwarting the crime or withdrawing does not sever *Pinkerton* liability. (e) is incorrect because *Pinkerton* explicitly covers crimes that were not expressly agreed upon, provided they were foreseeable consequences of executing the agreement.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, scope of conspiracy], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 - The Pinkerton Doctrine

<!-- audit: MUST FIX
check 1: pass (Assuming standard facts that match the explanation, the application of Pinkerton to immediate acts of concealment/escape is correct.)
check 2: pass (Distractors represent common misunderstandings of Pinkerton, though they cannot be fully evaluated without the facts.)
check 3: pass (The explanation's formulation of the doctrine matches standard rules and the Chapter 19 map.)
check 4: MUST FIX. The fact pattern is entirely missing. The question starts directly with the stub ("Is Silas liable..."), making it impossible for a student to assess foreseeability, furtherance, or the nature of Silas's protest without the narrative context.
check 5: pass (The stub explicitly specifies "under the Pinkerton doctrine," safely avoiding the MPC's rejection of the doctrine.)
check 6: pass (No excluded-topic bleed is apparent from the text provided.)
check 7: pass (Pinkerton liability and withdrawal requirements are covered in the Ch 19 meta-map tags.)
Recommended fix: Insert the missing fact pattern detailing Arthur and Silas's drug transaction, the motel room setup, the 911 call, and Silas's specific actions/protest.
-->

## Issue 2 — edge-case

**Q7.** Is Silas liable under the *Pinkerton* doctrine for Arthur's actions in locking the door and preventing the 911 call?

(a) Yes, because Arthur's actions were reasonably foreseeable efforts to conceal the drug distribution and avoid police detection, which were done in furtherance of the ongoing conspiracy. <!-- correct -->
(b) Yes, because the Pinkerton doctrine imposes strict criminal liability on all co-conspirators for any crime committed by a confederate, regardless of its foreseeability or specific purpose.
(c) No, because acts of concealment committed after the completion of the core objective of the drug sale fall strictly outside the temporal scope of Pinkerton liability.
(d) No, because Silas verbally protested leaving the motel room, which legally severed his connection to Arthur's subsequent independent acts of knocking the phone and locking the door.
(e) No, because Pinkerton liability only applies to crimes that the conspirators expressly agreed to commit at the explicit formation of the original criminal agreement.

**Answer:** (a)

**Explanation:** (a) is correct. Under the *Pinkerton* doctrine, a conspirator is liable for all reasonably foreseeable substantive crimes committed by co-conspirators in furtherance of the conspiracy. Arthur explicitly stated his motive was to avoid police detection to protect the enterprise and his job. Acts to conceal the crime or escape detection immediately following the core offense are typically considered foreseeable acts in furtherance of the conspiracy. (b) is incorrect because *Pinkerton* is not strict liability; it requires the substantive crime to be foreseeable and in furtherance of the conspiracy. (c) is incorrect because the conspiracy does not instantly terminate the moment money and drugs change hands; immediate escape and concealment are within its scope. (d) is incorrect because a mere verbal protest without effectively thwarting the crime or withdrawing does not sever *Pinkerton* liability. (e) is incorrect because *Pinkerton* explicitly covers crimes that were not expressly agreed upon, provided they were foreseeable consequences of executing the agreement.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, scope of conspiracy], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 - The Pinkerton Doctrine

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The act of "preventing the 911 call" is factually established as Arthur knocking the phone out of Silas's hand and destroying it. Silas is the victim of these specific acts (battery/criminal mischief). A defendant cannot be vicariously liable under Pinkerton for a crime of which he is the direct victim. Asking if Silas is liable for "Arthur's actions in... preventing the 911 call" inadvertently asks if Silas is liable for his own assault/property victimization. 
2. Cross-Doctrine Clashes: The victim-exclusion principle in accomplice/vicarious liability clashes with applying Pinkerton to crimes committed against a co-conspirator. Also, Pinkerton creates liability for *crimes*, not just "actions."
3. Cross-Question Spoilers: pass
Recommended fix: Specify the substantive crime directed at the third party (Julian). Change the prompt to: "Is Silas liable under the Pinkerton doctrine for the false imprisonment (or homicide) of Julian resulting from Arthur locking the motel room door?" and remove references in the options to the acts committed against Silas.
-->
