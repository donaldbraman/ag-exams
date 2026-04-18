# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q4.** Assume Darius is guilty of attempted murder. Under the traditional *Pinkerton* doctrine, is Marcus guilty of Darius's attempted murder?

(a) Yes, because attempted murder was a reasonably foreseeable consequence of Marcus ordering his crew to "beat them down by any means necessary" to defend the turf. <!-- correct -->
(b) No, because Marcus ordered them to "beat them down," meaning Darius's unilateral intent to kill exceeded the scope of the conspiratorial agreement.
(c) Yes, because as the leader of the conspiracy, Marcus is strictly liable for any and all crimes committed by his subordinates, regardless of foreseeability.
(d) No, because Marcus was not present at the scene and did not provide the specific weapon Darius used in the attempted murder.
(e) Yes, because under the MPC's rejection of *Pinkerton*, Marcus's purpose to facilitate an assault automatically transfers to the attempted murder.

**Answer:** (a)

**Explanation:** (a) is correct. Under the traditional *Pinkerton* doctrine, a conspirator is vicariously liable for the foreseeable substantive crimes of co-conspirators committed in furtherance of the conspiracy. An attempted murder is a foreseeable escalation of an order to defend drug turf "by any means necessary." (b) is incorrect because *Pinkerton* extends liability to foreseeable acts that further the conspiracy, even if they exceed the explicit terms of the initial agreement. (c) is incorrect because *Pinkerton* requires foreseeability and furtherance of the conspiracy, not strict liability for all acts. (d) is incorrect because physical presence and direct facilitation are not required for *Pinkerton* liability. (e) is incorrect because the MPC rejects *Pinkerton* entirely, requiring traditional accomplice liability for substantive offenses.

**Tags:** chapters: [19], topics: [conspiracy, pinkerton-doctrine, vicarious-liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19: Conspiracy > Liability Extensions > Pinkerton Doctrine

<!-- argument-pass: SHOULD FIX
(a) Argument-for: The *Pinkerton* doctrine holds conspirators vicariously liable for the foreseeable substantive crimes committed by co-conspirators in furtherance of the conspiracy. Marcus agreed to defend the turf and explicitly ordered his crew to do so "by any means necessary." An attempted murder is a natural, reasonably foreseeable consequence of a violent, unrestricted turf defense. Because Darius committed the act while executing Marcus’s broad directive, Marcus is liable. This makes (a) a direct and correct application of black-letter law to the facts.

(b) Argument-for: A student could argue that *Pinkerton* liability is strictly bounded by the explicit scope of the original agreement. Marcus's order to "beat them down" typically contemplates a battery or assault, not a specific-intent crime like attempted murder. By forming a unilateral intent to kill, Darius engaged in an independent frolic that fundamentally changed the nature of the crime. Therefore, vicarious liability should not attach to this unforeseen and unauthorized escalation.

(c) Argument-for: A student might conflate *Pinkerton* liability with broader concepts of strict liability for enterprise ringleaders. Since Marcus is the leader who ordered the crew to violently defend the turf, he is the ultimate factual and proximate cause of the resulting bloodshed. The argument goes that a leader issuing a "by any means necessary" command assumes total responsibility for all resulting actions of his subordinates. Thus, he would be strictly liable for the attempted murder.

(d) Argument-for: This option appeals to students who confuse *Pinkerton* vicarious liability with traditional accomplice liability. To be an accomplice, one typically must aid, abet, or encourage the specific crime, which often implies direct involvement or facilitation. A student could argue that Marcus's general order from afar is insufficiently direct for liability to attach to the specific attempted murder. Without physical presence or providing the specific murder weapon, the causal chain under this erroneous view is simply too attenuated.

(e) Argument-for: The Model Penal Code explicitly rejects the broad reach of the traditional *Pinkerton* doctrine, leading a student to search for alternative theories of vicarious liability. Under this view, a student might mistakenly believe that the MPC replaces *Pinkerton* with a doctrine of "transferred intent" for natural consequences. The argument is that Marcus's specific purpose to facilitate the underlying assault is legally transferred to the resulting attempted murder, satisfying the MPC's requirements through an automatic proxy.

Head-to-head: Option (a) is definitively the best answer because it correctly applies the twin pillars of *Pinkerton* liability: furtherance of the conspiracy and foreseeability. Distractor (c) correctly identifies Marcus's guilt but uses the explicitly false premise of strict liability locked by the absolute word "regardless." Distractor (e) incorrectly relies on the MPC (which rejects *Pinkerton*) and falsely claims intent "automatically transfers." Distractors (b) and (d), however, rely on implicit omissions rather than locked, falsifiable absolute claims. Option (b) argues the act "exceeded the scope," which is factually arguable and lacks an absolute word stating that exceeding the explicit agreement *automatically* defeats liability. Option (d) similarly lacks an absolute word like "solely because." 

Falsifiable claim per distractor:
- (b): "meaning Darius's unilateral intent to kill exceeded the scope of the conspiratorial agreement" — wrong because *Pinkerton* covers foreseeable escalations beyond the explicit agreement, but this distractor lacks an absolute word to strictly lock it as a false legal rule rather than a factual dispute.
- (c): "strictly liable... regardless of foreseeability" — wrong because *Pinkerton* explicitly requires foreseeability and furtherance, categorically rejecting strict liability.
- (d): "because Marcus was not present at the scene and did not provide the specific weapon" — wrong because *Pinkerton* does not require presence or specific facilitation, but it lacks a locking absolute word.
- (e): "automatically transfers" — wrong because the MPC rejects *Pinkerton* and does not automatically transfer purpose from an assault to an attempted murder.

Recommended fix: Add absolute words to (b) and (d) to ensure they fail the strict close-call standard. 
Change (b) to: "No, because Darius's unilateral intent to kill exceeded the explicit agreement, which categorically defeats *Pinkerton* liability."
Change (d) to: "No, solely because Marcus was not present at the scene and did not provide the specific weapon Darius used."
-->

## Issue 3 — argpass-opus

**Q4.** Assume Darius is guilty of attempted murder. Under the traditional *Pinkerton* doctrine, is Marcus guilty of Darius's attempted murder?

(a) Yes, because attempted murder was a reasonably foreseeable consequence of Marcus ordering his crew to "beat them down by any means necessary" to defend the turf. <!-- correct -->
(b) No, because Marcus ordered them to "beat them down," meaning Darius's unilateral intent to kill exceeded the scope of the conspiratorial agreement.
(c) Yes, because as the leader of the conspiracy, Marcus is strictly liable for any and all crimes committed by his subordinates, regardless of foreseeability.
(d) No, because Marcus was not present at the scene and did not provide the specific weapon Darius used in the attempted murder.
(e) Yes, because under the MPC's rejection of *Pinkerton*, Marcus's purpose to facilitate an assault automatically transfers to the attempted murder.

**Answer:** (a)

**Explanation:** (a) is correct. Under the traditional *Pinkerton* doctrine, a conspirator is vicariously liable for the foreseeable substantive crimes of co-conspirators committed in furtherance of the conspiracy. An attempted murder is a foreseeable escalation of an order to defend drug turf "by any means necessary." (b) is incorrect because *Pinkerton* extends liability to foreseeable acts that further the conspiracy, even if they exceed the explicit terms of the initial agreement. (c) is incorrect because *Pinkerton* requires foreseeability and furtherance of the conspiracy, not strict liability for all acts. (d) is incorrect because physical presence and direct facilitation are not required for *Pinkerton* liability. (e) is incorrect because the MPC rejects *Pinkerton* entirely, requiring traditional accomplice liability for substantive offenses.

**Tags:** chapters: [19], topics: [conspiracy, pinkerton-doctrine, vicarious-liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19: Conspiracy > Liability Extensions > Pinkerton Doctrine

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the traditional *Pinkerton* doctrine, a co-conspirator is vicariously liable for the substantive crimes committed by other conspirators if those crimes are in furtherance of the conspiracy and reasonably foreseeable. Here, Marcus explicitly ordered his crew to defend their turf "by any means necessary." Given the inherent violence of this directive, a subordinate escalating the confrontation to attempted murder is a reasonably foreseeable consequence of the agreement. Thus, Marcus is liable for Darius's attempted murder under *Pinkerton*.
(b) Argument-for: A student might focus on the literal words "beat them down" to argue the conspiracy was strictly limited to a simple or aggravated assault. Under *Pinkerton*, a co-conspirator is not liable for substantive crimes that fall entirely outside the scope of the conspiratorial agreement. A student could argue that Darius's specific intent to kill was a unilateral frolic that substantively departed from the agreed-upon "beat down," thereby breaking the chain of vicarious liability.
(c) Argument-for: *Pinkerton* liability is notoriously broad, effectively holding conspirators liable for acts they neither directly participated in nor explicitly agreed to. A student might misunderstand the extent of this breadth, conflating vicarious liability with strict liability. They could argue that because Marcus was the leader and gave the initial order, the doctrine automatically holds him absolutely responsible for any and all subsequent crimes committed by his subordinates, regardless of foreseeability.
(d) Argument-for: A student might confuse *Pinkerton* liability with traditional accomplice liability, which generally requires some form of active aiding, abetting, or encouragement of the specific substantive crime. Because Marcus was absent from the scene and did not supply the attempted murder weapon, he lacked the direct actus reus typically associated with physical participation. Therefore, the student could conclude that his mere status as an absent conspirator is legally insufficient for liability.
(e) Argument-for: A student could misread the question's premise or misunderstand the Model Penal Code's approach to conspiracy. Even recognizing that the MPC rejects *Pinkerton*, the student might erroneously believe the MPC replaces it with a doctrine of automatic transferred intent for foreseeable escalations. They could argue that Marcus's purpose to facilitate the assault automatically translates to liability for the attempted murder under a misapplied MPC standard.

Head-to-head: (a) is the strongest argument and the correct answer because it accurately applies the *Pinkerton* requirements of foreseeability and furtherance to the given facts. (c) and (e) contain explicit, falsifiable legal errors: (c) incorrectly claims *Pinkerton* is strict liability "regardless of foreseeability," while (e) incorrectly claims the MPC "automatically transfers" liability. However, (b) and (d) rely on implicit false legal claims rather than explicit ones. They argue "No, because [facts]," applying fact-based reasoning to reach an incorrect conclusion, but they fail to state a categorically false rule of law. Because they lack absolute phrasing locking in a legal error, they fail the strict close-call standard for falsifiability.

Falsifiable claim per distractor:
- (b): "meaning Darius's unilateral intent to kill exceeded the scope" — wrong legally in this context, but framed merely as a factual conclusion; lacks an explicitly false legal rule or absolute word.
- (c): "strictly liable for any and all crimes... regardless of foreseeability" — wrong because *Pinkerton* explicitly requires reasonable foreseeability and furtherance.
- (d): "because Marcus was not present at the scene and did not provide the specific weapon" — relies on an implicit false legal premise that presence or a weapon is required; lacks absolute words like "solely because."
- (e): "under the MPC's rejection of Pinkerton... automatically transfers" — wrong because the MPC rejects vicarious liability for substantive crimes and requires traditional accomplice liability, meaning liability does not "automatically transfer."

Recommended fix: Edit (b) and (d) to include absolute legal claims. For (b): "No, because under *Pinkerton*, a conspirator is categorically never liable for crimes requiring a higher mens rea than the target crime of the conspiracy." For (d): "No, solely because *Pinkerton* liability legally requires a co-conspirator to be physically present at the scene of the substantive offense."
-->
