# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** Assume the jurisdiction follows the Rosemond standard. Is Helen liable as an accomplice to Ian's use of a firearm during the stash house raid?

(a) Yes, she is liable for the firearm use. She knew Ian was bringing a bat to the raid, which demonstrates she had advance knowledge that extreme violence would inevitably occur.
(b) Yes, she is liable for the firearm use. She continued to act as a lookout and successfully facilitated the crime even after Ian secretly drew the concealed weapon inside.
(c) No, she is not liable for the firearm use. She did not know about the handgun in advance at a time when she still had a meaningful opportunity to walk away. <!-- correct -->
(d) No, she is not liable for the firearm use. She did not personally pull the trigger or hold the weapon during the fatal confrontation with the stash house guard.
(e) Yes, she is liable for the firearm use. Accomplices are strictly liable under federal law for any weapons used by their co-conspirators during the commission of a felony.

**Answer:** (c)

**Explanation:** Under the *Rosemond* standard, an accomplice is liable for a co-conspirator's use of a firearm only if they had advance knowledge of the weapon at a time when they had a meaningful opportunity to walk away. Helen did not know about the hidden gun. (a) is wrong because knowledge of a bat does not equate to advance knowledge of a firearm. (b) is wrong because she did not know about the weapon even as she continued to act as a lookout. (d) is wrong because physical handling is not required if the temporal advance knowledge standard is met. (e) is wrong because federal law explicitly requires advance knowledge, rejecting strict liability for accomplices regarding firearms.

**Tags:** chapters: [18], topics: [accomplice liability, temporal advance knowledge, Rosemond], difficulty: hard, cognitive: application

**Grounding:** Chapter 18 - Temporal Advance Knowledge (*Rosemond v. United States*)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: Fails. The stem provides no facts about the "stash house raid," Helen's role, Ian's actions, or what Helen knew. It relies entirely on a missing external fact pattern, making it impossible to answer as a standalone question.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Incorporate the necessary facts into the stem. For example: "Helen acted as a lookout while Ian raided a stash house. Helen knew Ian brought a bat, but Ian also carried a concealed handgun. Once inside, Ian secretly drew the handgun and used it during a fatal confrontation with a guard. Helen did not know about the handgun. Assume the jurisdiction follows the Rosemond standard. Is Helen liable as an accomplice to Ian's use of a firearm?"
-->

## Issue 2 — argpass-sonnet

**Q9.** Assume the jurisdiction follows the Rosemond standard. Is Helen liable as an accomplice to Ian's use of a firearm during the stash house raid?

(a) Yes, she is liable for the firearm use. She knew Ian was bringing a bat to the raid, which demonstrates she had advance knowledge that extreme violence would inevitably occur.
(b) Yes, she is liable for the firearm use. She continued to act as a lookout and successfully facilitated the crime even after Ian secretly drew the concealed weapon inside.
(c) No, she is not liable for the firearm use. She did not know about the handgun in advance at a time when she still had a meaningful opportunity to walk away. <!-- correct -->
(d) No, she is not liable for the firearm use. She did not personally pull the trigger or hold the weapon during the fatal confrontation with the stash house guard.
(e) Yes, she is liable for the firearm use. Accomplices are strictly liable under federal law for any weapons used by their co-conspirators during the commission of a felony.

**Answer:** (c)

**Explanation:** Under the *Rosemond* standard, an accomplice is liable for a co-conspirator's use of a firearm only if they had advance knowledge of the weapon at a time when they had a meaningful opportunity to walk away. Helen did not know about the hidden gun. (a) is wrong because knowledge of a bat does not equate to advance knowledge of a firearm. (b) is wrong because she did not know about the weapon even as she continued to act as a lookout. (d) is wrong because physical handling is not required if the temporal advance knowledge standard is met. (e) is wrong because federal law explicitly requires advance knowledge, rejecting strict liability for accomplices regarding firearms.

**Tags:** chapters: [18], topics: [accomplice liability, temporal advance knowledge, Rosemond], difficulty: hard, cognitive: application

**Grounding:** Chapter 18 - Temporal Advance Knowledge (*Rosemond v. United States*)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that general awareness of impending extreme violence and the presence of *some* weapon (a bat) satisfies the intent requirement for an armed offense. Under natural and probable consequences or foreseeability theories, if an accomplice knows a violent, armed raid is occurring, the escalation to a firearm is highly foreseeable, arguably satisfying the mens rea for the violent enterprise.
(b) Argument-for: A student could argue that ongoing participation constitutes continuous facilitation and ratification of the crime. If Helen stayed at her post as a lookout while the crime was occurring, she aided the crime while the gun was present. A student might mistakenly believe that ongoing physical facilitation of the underlying felony overrides the need for advance knowledge of the specific weapon.
(c) Argument-for: This is the correct rule under *Rosemond v. United States*. The Supreme Court explicitly held that an accomplice must have advance knowledge of the *firearm* itself (not just a generic weapon) at a time when they can still meaningfully withdraw from the criminal enterprise. Because Ian drew the gun "secretly," Helen lacked temporal advance knowledge, making her not liable.
(d) Argument-for: A student could argue that the plain meaning of a firearm "use" enhancement requires the principal actor to physically manipulate the object. An intuitive, layman reading of criminal liability often wrongly assumes that one cannot be punished for a gun crime unless they personally brandished, carried, or fired the weapon themselves.
(e) Argument-for: A student could conflate accomplice liability with strict liability doctrines like the felony-murder rule. Under this theory, they could argue that once Helen intentionally joined the dangerous felony (the stash house raid), she assumed the risk and became strictly liable for any aggravating factors—like firearms—introduced by her co-conspirators.

Head-to-head: (c) perfectly isolates the precise legal standard dictated by *Rosemond*. (a) and (b) apply incorrect interpretations of *Rosemond* to reach false conclusions ("Yes"), but their reasoning clauses lack absolute terminology locking in the false legal rule. (e) contains a clear, explicitly false legal rule ("strictly liable"). (d) is the weakest distractor structurally: it correctly states "No" and follows it with a statement of historical fact ("She did not personally pull the trigger"). Because (d) lacks an absolute word asserting a false legal standard, a clever student could appeal the question by arguing that (d) consists of two entirely true, unfalsifiable statements. 

Falsifiable claim per distractor:
- (a): "Yes, she is liable for the firearm use." — wrong outcome; reasoning contains an implicit false equivalence between a bat and a firearm, but lacks an absolute lock.
- (b): "Yes, she is liable for the firearm use." — wrong outcome; implies ongoing facilitation without actual knowledge ("secretly") triggers liability, but lacks an absolute lock.
- (d): NONE. "She did not personally pull the trigger" is a factually true statement, and "No, she is not liable" is the correct outcome. This distractor fails the close-call standard because it does not explicitly claim physical possession is *categorically required*. 
- (e): "Accomplices are strictly liable under federal law..." — explicitly false legal claim, as *Rosemond* firmly rejected strict liability for confederate firearm use.

Recommended fix: Update distractors (a), (b), and (d) to lock in explicit false legal rules using absolute language:
- (a): Yes, she is liable for the firearm use. Knowing a co-conspirator is bringing a bat **categorically establishes** the requisite advance knowledge for firearm liability.
- (b): Yes, she is liable for the firearm use. Continuing to facilitate the crime **automatically** renders an accomplice liable for any weapon used, **regardless** of whether it was drawn secretly.
- (d): No, she is not liable for the firearm use **solely because** accomplice liability **categorically requires** the defendant to personally pull the trigger or hold the weapon.
-->

## Issue 3 — argpass-opus

**Q9.** Assume the jurisdiction follows the Rosemond standard. Is Helen liable as an accomplice to Ian's use of a firearm during the stash house raid?

(a) Yes, she is liable for the firearm use. She knew Ian was bringing a bat to the raid, which demonstrates she had advance knowledge that extreme violence would inevitably occur.
(b) Yes, she is liable for the firearm use. She continued to act as a lookout and successfully facilitated the crime even after Ian secretly drew the concealed weapon inside.
(c) No, she is not liable for the firearm use. She did not know about the handgun in advance at a time when she still had a meaningful opportunity to walk away. <!-- correct -->
(d) No, she is not liable for the firearm use. She did not personally pull the trigger or hold the weapon during the fatal confrontation with the stash house guard.
(e) Yes, she is liable for the firearm use. Accomplices are strictly liable under federal law for any weapons used by their co-conspirators during the commission of a felony.

**Answer:** (c)

**Explanation:** Under the *Rosemond* standard, an accomplice is liable for a co-conspirator's use of a firearm only if they had advance knowledge of the weapon at a time when they had a meaningful opportunity to walk away. Helen did not know about the hidden gun. (a) is wrong because knowledge of a bat does not equate to advance knowledge of a firearm. (b) is wrong because she did not know about the weapon even as she continued to act as a lookout. (d) is wrong because physical handling is not required if the temporal advance knowledge standard is met. (e) is wrong because federal law explicitly requires advance knowledge, rejecting strict liability for accomplices regarding firearms.

**Tags:** chapters: [18], topics: [accomplice liability, temporal advance knowledge, Rosemond], difficulty: hard, cognitive: application

**Grounding:** Chapter 18 - Temporal Advance Knowledge (*Rosemond v. United States*)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might choose this if they confuse general foreseeability of violence with the specific mens rea required for firearm enhancements under *Rosemond*. They could argue that a bat is a deadly weapon, and knowing Ian was bringing one proves Helen embraced an armed, violent confrontation. Under a looser standard like the natural and probable consequences doctrine, knowing about the bat might make the use of a gun foreseeable. This leads the student to conclude that Helen's knowledge of the bat establishes sufficient advance knowledge of extreme violence to make her liable for the firearm use.
(b) Argument-for: A student could select this option by focusing on the ongoing nature of accomplice liability and the actus reus of acting as a lookout. They might reason that because Helen continued to facilitate the crime while the gun was being used, she was actively aiding the armed robbery in real-time. The student may erroneously believe that continued participation alone is enough to legally ratify the co-conspirator's actions. This overlooks the specific *Rosemond* requirement that the accomplice must actually learn about the weapon at a time when they still have a meaningful opportunity to withdraw.
(c) Argument-for: This option correctly applies the Supreme Court's holding in *Rosemond v. United States*. The Court established that accomplice liability for a co-conspirator's use of a firearm requires the defendant to have advance knowledge that a firearm will be used or carried. Critically, this knowledge must arise at a juncture where the accomplice still has a meaningful opportunity to withdraw from the criminal enterprise. Since Helen did not know about the hidden handgun in advance, she lacked the requisite intent to facilitate an armed offense, precluding her liability for the firearm charge.
(d) Argument-for: A student might choose this option if they misunderstand the fundamental mechanics of accomplice liability versus principal liability. They could assume that statutory firearm enhancements strictly require physical possession or direct use of the weapon by the defendant themselves. By focusing on the fact that Ian was the one who pulled the trigger and held the gun, the student might erroneously conclude that Helen cannot be charged with the firearm offense. This ignores the established doctrine that accomplices step into the shoes of the principal and can be liable for actions they do not physically perform.
(e) Argument-for: A student could defend this by incorrectly applying *Pinkerton* liability or broad felony-murder logic directly to the federal firearm statute. They might argue that once an individual agrees to participate in a dangerous felony like a stash house raid, they assume strict legal responsibility for any weapons their co-conspirators choose to bring. Believing that federal law is highly punitive regarding firearms, the student could assume there is a strict liability regime for accomplices to aggressively deter armed violence. This incorrectly dismisses the actual mens rea requirement established by the Supreme Court.

Head-to-head: Option (c) correctly isolates the *Rosemond* standard's dual requirement: advance knowledge of the firearm and a meaningful opportunity to walk away. The distractors attempt to test the boundaries of this rule but mostly fail to lock their false legal premises with absolute phrasing. Option (a) relies on an implicit assumption that knowledge of a bat equates to knowledge of a firearm, phrasing this as a factual deduction. Option (b) implies that ongoing participation overcomes a lack of knowledge, but only states this factually based on her continuing as a lookout. Option (d) incorrectly implies that physical possession is required, framing it merely as a factual excuse rather than an absolute rule. Option (e) successfully includes an explicit legal rule ("strictly liable"), but the other distractors need structural fortification to convert their implicit errors into explicit, falsifiable legal claims as demanded by the close-call standard.

Falsifiable claim per distractor:
- (a): "which demonstrates she had advance knowledge that extreme violence would inevitably occur" — wrong because *Rosemond* requires specific advance knowledge of a firearm, not just general extreme violence or a bat; however, the option lacks an absolute legal rule.
- (b): "She continued to act as a lookout and successfully facilitated the crime even after Ian secretly drew the concealed weapon inside" — wrong because continuing to participate without actual knowledge of the secretly drawn weapon does not satisfy the *Rosemond* standard; lacks an absolute legal claim.
- (d): "She did not personally pull the trigger or hold the weapon" — wrong because accomplice liability does not require the accomplice to physically possess the weapon; lacks an absolute legal rule.
- (e): "Accomplices are strictly liable under federal law for any weapons used" — explicitly false because *Rosemond* rejected strict liability for accomplices regarding firearms, explicitly requiring advance knowledge.

Recommended fix: Fortify distractors (a), (b), and (d) with absolute language to create explicit, falsifiable legal rules.
- Change (a) to: "Yes, she is liable for the firearm use. Advance knowledge of any deadly weapon, such as a bat, automatically satisfies the advance knowledge requirement for firearm liability."
- Change (b) to: "Yes, she is liable for the firearm use. An accomplice is categorically liable for any weapon drawn during a crime as long as they successfully continue to facilitate the underlying offense."
- Change (d) to: "No, she is not liable for the firearm use. Accomplice liability for a firearm enhancement categorically requires the defendant to personally pull the trigger or physically hold the weapon."
-->
