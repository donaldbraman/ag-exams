# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q8.** Silas is charged with the murder of Dexter. He claims he acted in self-defense because Dexter lunged at him with a machete. Will Silas's self-defense claim succeed?

(a) Yes, because Dexter's use of a machete constituted a threat of imminent deadly force, legally justifying Silas's use of a firearm.
(b) No, because Silas was the initial aggressor in an armed robbery, which categorically bars him from claiming self-defense against the victim's lawful resistance. <!-- correct -->
(c) Yes, because Silas did not brandish the firearm until Dexter lunged at him, meaning Dexter was the first to threaten deadly force.
(d) No, because Silas had a duty to retreat by running out the door before using deadly force, regardless of whether he was the initial aggressor.
(e) Yes, because Dexter's role as a guard in an illegal drug operation strips him of the right to use deadly force in defense of property.

**Answer:** (b)

**Explanation:** (b) is correct. A defendant who is the initial aggressor—especially one committing a violent felony like armed robbery—cannot claim self-defense against the victim's lawful use of defensive force unless the aggressor completely withdraws and communicates that withdrawal. (a) is incorrect because the initial aggressor bar supersedes the general rule justifying deadly force against deadly threats. (c) is incorrect because initiating the robbery makes Silas the aggressor, even if his weapon was concealed initially. (d) is incorrect because the initial aggressor bar is the primary disqualifier here; duty to retreat only applies to those who otherwise have the right to self-defense. (e) is incorrect because the legality of Dexter's drug operation does not grant Silas a license to rob him or strip Dexter of basic self-defense rights.

**Tags:** chapters: [22], topics: [self-defense, initial-aggressor, felony-murder], difficulty: medium, cognitive: application

**Grounding:** Chapter 22: Self-Defense > Refinements > Initial Aggressor Bar

<!-- audit: MUST FIX
check 1: Fails. The correct answer asserts Silas was the initial aggressor in an armed robbery, but these facts are completely missing from the stem.
check 2: pass (none of the answers logically flow from the stem as currently written, as they all reference facts not in evidence).
check 3: pass (the explanation accurately describes the doctrine, but references facts the drafter forgot to put in the prompt).
check 4: Fails entirely. The stem lacks the core facts needed to answer the question. It never mentions an armed robbery, Silas's use of a firearm, or Dexter's drug operation.
check 5: pass.
check 6: pass.
check 7: pass (initial aggressor bar is covered in Ch 22).
Recommended fix: Rewrite the stem to include the missing factual scenario. For example: "Silas enters an illegal drug operation guarded by Dexter and initiates a robbery. Before Silas can brandish his concealed firearm, Dexter lunges at him with a machete. Silas draws his gun and shoots Dexter, killing him. Silas is charged with murder..."
-->

## Issue 2 — argpass-sonnet

**Q8.** Silas is charged with the murder of Dexter. He claims he acted in self-defense because Dexter lunged at him with a machete. Will Silas's self-defense claim succeed?

(a) Yes, because Dexter's use of a machete constituted a threat of imminent deadly force, legally justifying Silas's use of a firearm.
(b) No, because Silas was the initial aggressor in an armed robbery, which categorically bars him from claiming self-defense against the victim's lawful resistance. <!-- correct -->
(c) Yes, because Silas did not brandish the firearm until Dexter lunged at him, meaning Dexter was the first to threaten deadly force.
(d) No, because Silas had a duty to retreat by running out the door before using deadly force, regardless of whether he was the initial aggressor.
(e) Yes, because Dexter's role as a guard in an illegal drug operation strips him of the right to use deadly force in defense of property.

**Answer:** (b)

**Explanation:** (b) is correct. A defendant who is the initial aggressor—especially one committing a violent felony like armed robbery—cannot claim self-defense against the victim's lawful use of defensive force unless the aggressor completely withdraws and communicates that withdrawal. (a) is incorrect because the initial aggressor bar supersedes the general rule justifying deadly force against deadly threats. (c) is incorrect because initiating the robbery makes Silas the aggressor, even if his weapon was concealed initially. (d) is incorrect because the initial aggressor bar is the primary disqualifier here; duty to retreat only applies to those who otherwise have the right to self-defense. (e) is incorrect because the legality of Dexter's drug operation does not grant Silas a license to rob him or strip Dexter of basic self-defense rights.

**Tags:** chapters: [22], topics: [self-defense, initial-aggressor, felony-murder], difficulty: medium, cognitive: application

**Grounding:** Chapter 22: Self-Defense > Refinements > Initial Aggressor Bar

<!-- argument-pass: MUST FIX
(a) Argument-for: Based purely on the facts provided in the question stem, this option is entirely correct. The stem states only that Dexter lunged at Silas with a machete, which constitutes an objective threat of imminent deadly force. Under core self-defense doctrine, facing an unprovoked machete attack legally justifies the proportional use of deadly force (such as a firearm) to protect oneself.
(b) Argument-for: If one assumes the hidden facts implied by this option (that Silas was robbing Dexter), (b) correctly states the initial aggressor rule. An individual who initiates an armed robbery categorically forfeits the right to claim self-defense against the victim's lawful resistance. This bar remains absolute unless the initial aggressor completely withdraws and communicates that withdrawal, which did not occur here.
(c) Argument-for: A student might argue that the timeline of brandishing dictates who the initial aggressor for deadly force purposes is. If Silas kept his firearm concealed and did not explicitly threaten Dexter until Dexter lunged with the machete, one could argue Dexter escalated the encounter. Under this strict timeline approach, Dexter was the first to threaten deadly force, theoretically validating Silas's self-defense claim.
(d) Argument-for: In a duty-to-retreat jurisdiction, a defendant must retreat if it is perfectly safe to do so before using deadly force. A student could argue that failing to run out the door is an absolute bar to self-defense that operates independently of other doctrines. Thus, the duty to retreat applies "regardless" of the initial aggressor analysis, making this the correct dispositive reason for the claim's failure.
(e) Argument-for: A student could rely on the "clean hands" doctrine or broad public policy arguments to support this option. They might reason that a guard in an illegal drug operation cannot lawfully use force to protect illicit contraband or an illegal enterprise. Under this theory, Dexter's use of the machete was categorically unlawful, preserving Silas's right to defend himself.

Head-to-head: This question is fundamentally broken because the fact pattern is completely missing from the stem. The stem never mentions an armed robbery, an illegal drug operation, a concealed firearm, or a door. Based strictly on the text provided to the student, (a) is the objectively correct answer, while the keyed answer (b) relies on phantom facts. If the missing facts were restored, (b) would be clearly correct, and distractors (c), (d), and (e) would function properly by presenting falsifiable misapplications of the initial aggressor doctrine, the duty to retreat, and the defense of illegal operations. Because a crucial omission makes the intended right answer ungrounded and a distractor factually correct, this is a severe MUST FIX.

Falsifiable claim per distractor:
- (a): "legally justifying Silas's use of a firearm." — Currently NOT wrong based on the stem; however, it becomes falsifiable if the stem establishes Silas as the initial aggressor.
- (c): "meaning Dexter was the first to threaten deadly force." — Falsifiable (assuming facts are added) because committing an armed robbery automatically makes one the initial aggressor for deadly force purposes, regardless of who brandishes a weapon first.
- (d): "regardless of whether he was the initial aggressor." — Wrong because the initial aggressor doctrine is a primary bar to self-defense that completely strips the right, meaning the duty to retreat does not apply "regardless" of aggressor status; an aggressor has no self-defense right to begin with.
- (e): "strips him of the right to use deadly force in defense of property." — Wrong because participating in an illegal enterprise does not automatically strip a person of their basic human right to self-defense against a lethal threat (like an armed robber).

Recommended fix: Add the missing fact pattern to the question stem. For example: "Silas entered an illegal drug operation to commit an armed robbery. He kept his firearm concealed. Dexter, acting as a guard, realized Silas was trying to rob the operation and lunged at Silas with a machete. Silas then drew his firearm, shot Dexter, and killed him. Silas is charged with the murder of Dexter. He claims he acted in self-defense. Will Silas's self-defense claim succeed?"
-->

## Issue 3 — argpass-opus

**Q8.** Silas is charged with the murder of Dexter. He claims he acted in self-defense because Dexter lunged at him with a machete. Will Silas's self-defense claim succeed?

(a) Yes, because Dexter's use of a machete constituted a threat of imminent deadly force, legally justifying Silas's use of a firearm.
(b) No, because Silas was the initial aggressor in an armed robbery, which categorically bars him from claiming self-defense against the victim's lawful resistance. <!-- correct -->
(c) Yes, because Silas did not brandish the firearm until Dexter lunged at him, meaning Dexter was the first to threaten deadly force.
(d) No, because Silas had a duty to retreat by running out the door before using deadly force, regardless of whether he was the initial aggressor.
(e) Yes, because Dexter's role as a guard in an illegal drug operation strips him of the right to use deadly force in defense of property.

**Answer:** (b)

**Explanation:** (b) is correct. A defendant who is the initial aggressor—especially one committing a violent felony like armed robbery—cannot claim self-defense against the victim's lawful use of defensive force unless the aggressor completely withdraws and communicates that withdrawal. (a) is incorrect because the initial aggressor bar supersedes the general rule justifying deadly force against deadly threats. (c) is incorrect because initiating the robbery makes Silas the aggressor, even if his weapon was concealed initially. (d) is incorrect because the initial aggressor bar is the primary disqualifier here; duty to retreat only applies to those who otherwise have the right to self-defense. (e) is incorrect because the legality of Dexter's drug operation does not grant Silas a license to rob him or strip Dexter of basic self-defense rights.

**Tags:** chapters: [22], topics: [self-defense, initial-aggressor, felony-murder], difficulty: medium, cognitive: application

**Grounding:** Chapter 22: Self-Defense > Refinements > Initial Aggressor Bar

<!-- argument-pass: MUST FIX
(a) Argument-for: Under basic self-defense doctrine, a person may use deadly force if they reasonably believe they are facing an imminent threat of deadly force. The prompt states Dexter lunged at Silas with a machete, which constitutes an imminent deadly threat. Therefore, Silas was legally justified in using a firearm to defend himself, making this option arguably correct based strictly on the plain text of the abbreviated prompt.
(b) Argument-for: The initial aggressor rule bars a defendant from claiming self-defense if they provoked the conflict. Option (b) states Silas was the initial aggressor in an armed robbery. An armed robber categorically forfeits the right to self-defense against a victim's lawful resistance (unless the robber clearly withdraws). Thus, if Silas was an armed robber, his self-defense claim fails, making (b) legally accurate.
(c) Argument-for: Even an initial aggressor can sometimes regain the right to self-defense if the victim drastically escalates the encounter to deadly force without justification. If Silas did not brandish a firearm until Dexter lunged with a machete, one could argue Dexter escalated the conflict to deadly force first, thereby reviving Silas's right to self-defense against the machete.
(d) Argument-for: In minority jurisdictions, a defendant has a duty to retreat before using deadly force if they can do so safely. Option (d) asserts Silas had a duty to retreat by running out the door. If Silas failed to fulfill this duty, his self-defense claim fails, validating this option under retreat-rule principles.
(e) Argument-for: Public policy and the illegality of the enterprise might be argued to strip a participant of certain privileges. If Dexter was guarding an illegal drug operation, one could argue he had no lawful right to use deadly force to defend the illegal property or enterprise, rendering Dexter's use of force unlawful and validating Silas's defensive response.

Head-to-head: The glaring issue with this question is that the fact pattern is missing almost all the essential facts required to answer it. The prompt only mentions Silas, Dexter, and a machete. It entirely omits the armed robbery, the concealed firearm, the door, and the drug operation. Without these facts, (a) is actually the best answer because it relies solely on the provided fact (the machete lunge). The keyed answer (b) introduces the critical fact of the "armed robbery" out of nowhere. A student cannot determine that (b) is correct without assuming facts not in evidence. This makes the question unanswerable as written.

Falsifiable claim per distractor:
- (a): "legally justifying Silas's use of a firearm" — wrong because (assuming the intended full fact pattern where Silas is an armed robber) the initial aggressor doctrine overrides the general rule of self-defense against deadly force.
- (c): "meaning Dexter was the first to threaten deadly force" — wrong because (assuming the intended facts) committing an armed robbery inherently threatens deadly force, meaning Silas was the first.
- (d): "regardless of whether he was the initial aggressor" — wrong because the initial aggressor bar independently and categorically defeats self-defense; duty to retreat only applies to a defendant who is not the initial aggressor, so the duty does not apply "regardless" of that status.
- (e): "strips him of the right to use deadly force in defense of property" — wrong because self-defense against an armed robber is primarily defense of person, and illegal employment does not strip one's fundamental right to self-defense of person.

Recommended fix: Add the missing facts to the prompt. Example: "Silas entered an illegal drug operation to commit an armed robbery. His gun was concealed. Dexter, a guard, suspected Silas's intent and lunged at him with a machete. Silas then pulled his firearm and shot Dexter, killing him. Silas is charged with the murder of Dexter. He claims he acted in self-defense because Dexter lunged at him with a machete. Will Silas's self-defense claim succeed?"
-->
