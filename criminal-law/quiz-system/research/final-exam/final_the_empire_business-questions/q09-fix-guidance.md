# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** Assume Dominic is guilty of the homicide of Victor. Under standard conspiracy doctrines, can Carmine also be held liable for Victor's death?

(a) Guilty, because the homicide was a reasonably foreseeable consequence of the armed extortion conspiracy and was committed by his co-conspirator in furtherance of that ongoing agreement. <!-- correct -->
(b) Not guilty, because Carmine was not physically present at the restaurant and did not provide any affirmative assistance or direct encouragement for the specific fatal shooting.
(c) Guilty, because organized enterprise owners are strictly liable for any violent crimes committed by their subordinates during the normal scope of their employment for the illicit business.
(d) Not guilty, because the shooting occurred due to Victor's unexpected resistance, breaking the necessary causal chain between Carmine's original extortion instructions and the resulting tragic death.
(e) Guilty, because Carmine directed the laundering of the extortion proceeds, making him an accessory after the fact to any violent crimes committed to obtain the extorted money.

**Answer:** (a)

**Explanation:** Under the Pinkerton doctrine, a conspirator is liable for the substantive offenses committed by co-conspirators if those offenses were committed in furtherance of the conspiracy and were reasonably foreseeable. An armed extortion operation inherently carries the highly foreseeable risk of a fatal shooting. (b) is incorrect because Pinkerton liability does not require the defendant's physical presence or direct assistance in the specific substantive offense, only participation in the underlying conspiracy. (c) is incorrect because there is no strict liability for enterprise owners; liability must be grounded in Pinkerton or accomplice principles. (d) is incorrect because a victim resisting an armed robbery is highly foreseeable and does not break the causal chain. (e) is incorrect because liability for the homicide is based on the conspiracy to commit extortion, not on laundering the proceeds after the fact.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Pinkerton v. United States

<!-- audit: MUST FIX
check 1: pass (Assuming the implied facts, option (a) correctly applies the Pinkerton doctrine).
check 2: pass (Distractors are well-crafted but not legally correct under Pinkerton and basic causation principles).
check 3: pass (Explanation accurately states the Pinkerton requirements).
check 4: MUST FIX. The question stem is missing the foundational fact pattern. It relies entirely on specific unstated facts (Carmine and Dominic's relationship, an armed extortion conspiracy, a restaurant location, laundering proceeds, unexpected resistance) that are never introduced to the student in this prompt. 
check 5: SHOULD FIX. The phrase "standard conspiracy doctrines" is ambiguous because the Model Penal Code explicitly rejects Pinkerton liability (covered under `pinkerton-mpc-rejection`). A prepared student could argue that the MPC is a "standard" framework. 
check 6: pass
check 7: pass (Pinkerton is covered under `pinkerton-doctrine` in Ch 19).
Recommended fix: Integrate the missing fact pattern into the question stem (or ensure it is clearly attached if this is a sub-question) and clarify the jurisdiction by replacing "standard conspiracy doctrines" with "federal conspiracy doctrines" or "in a jurisdiction that applies the Pinkerton doctrine."
-->

## Issue 2 — argpass-sonnet

**Q9.** Assume Dominic is guilty of the homicide of Victor. Under standard conspiracy doctrines, can Carmine also be held liable for Victor's death?

(a) Guilty, because the homicide was a reasonably foreseeable consequence of the armed extortion conspiracy and was committed by his co-conspirator in furtherance of that ongoing agreement. <!-- correct -->
(b) Not guilty, because Carmine was not physically present at the restaurant and did not provide any affirmative assistance or direct encouragement for the specific fatal shooting.
(c) Guilty, because organized enterprise owners are strictly liable for any violent crimes committed by their subordinates during the normal scope of their employment for the illicit business.
(d) Not guilty, because the shooting occurred due to Victor's unexpected resistance, breaking the necessary causal chain between Carmine's original extortion instructions and the resulting tragic death.
(e) Guilty, because Carmine directed the laundering of the extortion proceeds, making him an accessory after the fact to any violent crimes committed to obtain the extorted money.

**Answer:** (a)

**Explanation:** Under the Pinkerton doctrine, a conspirator is liable for the substantive offenses committed by co-conspirators if those offenses were committed in furtherance of the conspiracy and were reasonably foreseeable. An armed extortion operation inherently carries the highly foreseeable risk of a fatal shooting. (b) is incorrect because Pinkerton liability does not require the defendant's physical presence or direct assistance in the specific substantive offense, only participation in the underlying conspiracy. (c) is incorrect because there is no strict liability for enterprise owners; liability must be grounded in Pinkerton or accomplice principles. (d) is incorrect because a victim resisting an armed robbery is highly foreseeable and does not break the causal chain. (e) is incorrect because liability for the homicide is based on the conspiracy to commit extortion, not on laundering the proceeds after the fact.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Pinkerton v. United States

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the *Pinkerton* doctrine, a conspirator is liable for any substantive offenses committed by co-conspirators if those crimes are in furtherance of the conspiracy and reasonably foreseeable. Armed extortion carries a highly foreseeable risk of violence, including homicide, if the victim resists. Because Dominic committed the homicide while carrying out the extortion agreement, Carmine is liable as a co-conspirator.
(b) Argument-for: A student could argue that Carmine is not guilty because accomplice liability traditionally requires more than mere association; it demands affirmative assistance or encouragement of the specific offense. By pointing out that Carmine was neither physically present nor provided direct assistance for the shooting itself, this option appeals to standard limitations on accomplice liability (e.g., *Pace v. Indiana*).
(c) Argument-for: A student could argue that Carmine is guilty under principles analogous to enterprise liability theories or *respondeat superior*. If Carmine is the boss of an organized criminal enterprise, the argument goes that he holds strict command responsibility for crimes committed by his subordinates acting within the normal scope of their "employment" in the illicit business.
(d) Argument-for: A student could argue that Victor's unexpected resistance was an independent, intervening superseding cause that broke the causal chain between Carmine's instructions and the death. In criminal causation, an unforeseeable intervening act relieves the original actor of liability, and the student might argue Dominic's decision to shoot was a superseding frolic.
(e) Argument-for: A student could argue that by laundering the proceeds of the extortion, Carmine provided after-the-fact aid to the criminal enterprise, which legally constitutes accessory after the fact liability. Under common law principles, assisting a felon to enjoy the fruits of their crime inextricably links the accessory to the violent methods used to obtain those proceeds.

Head-to-head: Option (a) perfectly states the *Pinkerton* doctrine, correctly linking the reasonably foreseeable homicide to the ongoing extortion agreement. Option (b) fails because a co-conspirator need not be physically present or provide direct assistance, though the option lacks absolute phrasing to formally lock this false premise. Option (c) is explicitly wrong because it invents a nonexistent "strict liability" standard for criminal enterprise owners. Option (d) falsely claims that victim resistance breaks the causal chain in an armed extortion, though it also relies on an implicit legal conclusion rather than a locked absolute. Option (e) wrongly conflates being an accessory after the fact to laundering with principal liability for "any violent crimes" committed earlier. Because (b) and (d) rely on implicit legal rules rather than explicit, locked false legal claims, the question should be fixed to align with the rigorous close-call standard.

Falsifiable claim per distractor:
- (b): "because Carmine was not physically present... and did not provide any affirmative assistance" — wrong because *Pinkerton* liability explicitly bypasses the need for physical presence or direct assistance. (Lacks absolute wording like "solely because").
- (c): "strictly liable for any violent crimes" — wrong because criminal law does not recognize strict vicarious liability for enterprise owners absent *Pinkerton* or accomplice elements.
- (d): "breaking the necessary causal chain" — wrong because a victim's resistance during armed extortion is highly foreseeable and legally does not sever the causal chain. (Lacks an absolute word like "automatically").
- (e): "making him an accessory after the fact to any violent crimes" — wrong because laundering money makes one an accessory to the financial crime/extortion, not automatically an accessory to the homicide itself, and accessory after the fact does not create principal liability for the homicide.

Recommended fix: Add absolute words to (b) and (d) to lock the false legal claims. 
Change (b) to: "Not guilty, solely because Carmine was not physically present at the restaurant and did not provide any affirmative assistance..."
Change (d) to: "Not guilty, because the shooting occurred due to Victor's unexpected resistance, automatically breaking the necessary causal chain..."
-->

## Issue 3 — argpass-opus

**Q9.** Assume Dominic is guilty of the homicide of Victor. Under standard conspiracy doctrines, can Carmine also be held liable for Victor's death?

(a) Guilty, because the homicide was a reasonably foreseeable consequence of the armed extortion conspiracy and was committed by his co-conspirator in furtherance of that ongoing agreement. <!-- correct -->
(b) Not guilty, because Carmine was not physically present at the restaurant and did not provide any affirmative assistance or direct encouragement for the specific fatal shooting.
(c) Guilty, because organized enterprise owners are strictly liable for any violent crimes committed by their subordinates during the normal scope of their employment for the illicit business.
(d) Not guilty, because the shooting occurred due to Victor's unexpected resistance, breaking the necessary causal chain between Carmine's original extortion instructions and the resulting tragic death.
(e) Guilty, because Carmine directed the laundering of the extortion proceeds, making him an accessory after the fact to any violent crimes committed to obtain the extorted money.

**Answer:** (a)

**Explanation:** Under the Pinkerton doctrine, a conspirator is liable for the substantive offenses committed by co-conspirators if those offenses were committed in furtherance of the conspiracy and were reasonably foreseeable. An armed extortion operation inherently carries the highly foreseeable risk of a fatal shooting. (b) is incorrect because Pinkerton liability does not require the defendant's physical presence or direct assistance in the specific substantive offense, only participation in the underlying conspiracy. (c) is incorrect because there is no strict liability for enterprise owners; liability must be grounded in Pinkerton or accomplice principles. (d) is incorrect because a victim resisting an armed robbery is highly foreseeable and does not break the causal chain. (e) is incorrect because liability for the homicide is based on the conspiracy to commit extortion, not on laundering the proceeds after the fact.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Pinkerton v. United States

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the widely adopted *Pinkerton* doctrine, a conspirator is vicariously liable for the substantive offenses committed by co-conspirators. This liability attaches if the crime was committed in furtherance of the conspiracy and was a reasonably foreseeable consequence of the unlawful agreement. Because armed extortion inherently carries a high risk of lethal violence, Dominic's homicide of Victor is reasonably foreseeable, establishing Carmine's guilt.
(b) Argument-for: A student could argue that vicarious liability for a substantive crime requires the elements of accomplice liability. In frameworks that reject or restrict *Pinkerton*, a conspirator must aid and abet the specific target offense to be held liable. Because Carmine was not physically present and offered no affirmative assistance for the shooting itself, the student could conclude he lacks the required actus reus to be liable for the homicide.
(c) Argument-for: Drawing on organized crime frameworks like RICO and corporate enterprise liability concepts, a student might argue that illicit business operators bear overarching responsibility for their subordinates' actions. This theory suggests a form of *respondeat superior* in criminal law. The student could incorrectly assume that a boss is automatically guilty of any violent crimes their enforcers commit within the scope of their employment in the extortion enterprise.
(d) Argument-for: Even under standard conspiracy doctrines, the resulting crime must be proximately causally linked to the original agreement. A student could argue that Victor's unexpected physical resistance constitutes an unforeseeable superseding intervening act. Consequently, this unexpected resistance arguably breaks the necessary causal chain between Carmine's original extortion instructions and the ultimate shooting, absolving him of homicide guilt.
(e) Argument-for: A student might recall that interacting with the proceeds of a crime creates secondary criminal liability. Because Carmine directed the laundering of the extortion money, he provided post-offense assistance to the perpetrators. The student could incorrectly argue this translates into accessory-after-the-fact liability for the homicide, providing a direct mechanism to hold him accountable for Victor's death.

Head-to-head: Option (a) correctly applies the *Pinkerton* doctrine, recognizing that a fatal shooting is a reasonably foreseeable consequence of an armed extortion conspiracy. Distractor (b) is incorrect because it falsely claims that physical presence and affirmative assistance are necessary for conspiracy liability, conflating it with strict accomplice liability. Distractor (c) invents a non-existent "strict liability" standard for criminal enterprise owners, bypassing the actual requirements of foreseeability and furtherance. Distractor (d) asserts a false legal conclusion by claiming victim resistance in an armed felony breaks the causal chain, when in reality such resistance is universally deemed foreseeable as a matter of law. Distractor (e) falsely equates accessory-after-the-fact status (a separate, lesser charge) with being held liable for the underlying substantive offense of homicide. 

Falsifiable claim per distractor:
- (b): "because Carmine was not physically present... and did not provide any affirmative assistance" — wrong because under standard conspiracy (*Pinkerton*) doctrine, liability expressly does *not* require physical presence or affirmative assistance for the substantive crime.
- (c): "organized enterprise owners are strictly liable for any violent crimes" — wrong because standard criminal law does not impose strict vicarious liability on enterprise owners; specific criteria like foreseeability and furtherance are legally required.
- (d): "breaking the necessary causal chain" — wrong because victim resistance to an armed felony is legally foreseeable and does not serve as a superseding cause to break proximate causation.
- (e): "making him an accessory after the fact to any violent crimes committed... [thus liable for the death]" — wrong because being an accessory after the fact to money laundering does not make one liable as a principal for the substantive underlying homicide.

Recommended fix: The distractors feature explicitly false legal claims, but to fully comply with the close-call standard's directive to lock falsifiable propositions with absolute words, minor additions are recommended:
- In (b), change "Not guilty, because Carmine..." to "Not guilty, because standard conspiracy liability categorically requires that Carmine be physically present..."
- In (d), change "breaking the necessary causal chain" to "automatically breaking the necessary causal chain". 
-->
