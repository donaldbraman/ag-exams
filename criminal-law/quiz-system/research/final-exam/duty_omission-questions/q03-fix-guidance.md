# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** Assume prosecutors charge Bex with Alba's assault on Dane. Is Bex guilty of the assault under the *Pinkerton* doctrine?

(a) Guilty, because Alba's use of violence to protect the operation was a reasonably foreseeable consequence of an armed drug distribution conspiracy. <!-- correct -->
(b) Guilty, because the doctrine imposes strict liability on all co-conspirators for any crime committed in the same physical location.
(c) Not guilty, because Bex did not explicitly agree to assault neighbors when she entered the initial distribution conspiracy.
(d) Not guilty, because Alba's specific intent to knock Dane unconscious was not shared by Bex during the confrontation.
(e) Not guilty, because Alba committed the assault after the primary drug transaction with Cody had already been concluded.

**Answer:** (a)

**Explanation:** (a) is correct because under the *Pinkerton* doctrine, a conspirator is liable for the substantive offenses committed by a co-conspirator that are reasonably foreseeable and in furtherance of the conspiracy; using a weapon brought to protect the drug operation meets this standard. (b) is wrong because *Pinkerton* requires foreseeability and furtherance, not strict location-based liability. (c) is wrong because explicit agreement to the specific substantive crime is not required, only foreseeability. (d) is wrong because *Pinkerton* liability relies on agency principles, dispensing with the need for the co-conspirator to share the specific intent of the perpetrator. (e) is wrong because the conspiracy was ongoing and the assault was in furtherance of protecting the operation from exposure.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, pinkerton-doctrine

<!-- audit: SHOULD FIX
Check 1: pass (The correct answer accurately applies the two-part *Pinkerton* test of foreseeability and furtherance).
Check 2: pass (Distractors represent common misunderstandings of conspiracy liability; (e) correctly tests the ongoing nature of the conspiracy).
Check 3: pass (The explanation correctly cites both the foreseeability and furtherance prongs).
Check 4: fails (The stem refers to specific actors—Bex, Alba, Dane, Cody—and events like "the primary drug transaction" without supplying the underlying fact pattern. It relies entirely on a missing shared scenario. If this is presented as a standalone question, it is unanswerable).
Check 5: pass (The stem explicitly specifies "under the Pinkerton doctrine," safely sidestepping MPC jurisdictions that reject it).
Check 6: pass (No excluded topics).
Check 7: pass (Pinkerton doctrine is explicitly grounded in Chapter 19 map tags).
Recommended fix: If this question is drawn from a shared fact pattern on the exam, ensure the LMS platform rigidly pairs it with the master scenario. If it must stand alone, inject a one-sentence factual summary into the stem (e.g., "Assume Bex and Alba are in an armed drug distribution conspiracy. While Bex is completing a transaction with Cody, Alba assaults Dane to protect the operation. Prosecutors charge Bex..."). 
-->

## Issue 2 — edge-case

**Q3.** Assume prosecutors charge Bex with Alba's assault on Dane. Is Bex guilty of the assault under the *Pinkerton* doctrine?

(a) Guilty, because Alba's use of violence to protect the operation was a reasonably foreseeable consequence of an armed drug distribution conspiracy. <!-- correct -->
(b) Guilty, because the doctrine imposes strict liability on all co-conspirators for any crime committed in the same physical location.
(c) Not guilty, because Bex did not explicitly agree to assault neighbors when she entered the initial distribution conspiracy.
(d) Not guilty, because Alba's specific intent to knock Dane unconscious was not shared by Bex during the confrontation.
(e) Not guilty, because Alba committed the assault after the primary drug transaction with Cody had already been concluded.

**Answer:** (a)

**Explanation:** (a) is correct because under the *Pinkerton* doctrine, a conspirator is liable for the substantive offenses committed by a co-conspirator that are reasonably foreseeable and in furtherance of the conspiracy; using a weapon brought to protect the drug operation meets this standard. (b) is wrong because *Pinkerton* requires foreseeability and furtherance, not strict location-based liability. (c) is wrong because explicit agreement to the specific substantive crime is not required, only foreseeability. (d) is wrong because *Pinkerton* liability relies on agency principles, dispensing with the need for the co-conspirator to share the specific intent of the perpetrator. (e) is wrong because the conspiracy was ongoing and the assault was in furtherance of protecting the operation from exposure.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, pinkerton-doctrine

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The chronological facts establish that Bex attempted to dial 911, and Alba drew her weapon to physically trap Bex *before* Dane breached the door and was assaulted. This sequence creates a very strong argument that Bex effectively withdrew from the conspiracy (taking an affirmative act inconsistent with the conspiracy and communicating it to her co-conspirator) or that the conspiratorial agreement had completely broken down into a hostage situation. This makes finding her "Guilty" under Pinkerton highly debatable without a caveat.
2. Cross-Doctrine Clashes: The doctrine of Withdrawal from a Conspiracy directly clashes with the ongoing Pinkerton liability tested here, potentially rendering the intended correct answer legally false.
3. Cross-Question Spoilers: pass
Recommended fix: Add a clarifying assumption to the prompt to shield the question from the withdrawal defense: "Assume for this question that Bex's actions did not constitute a legal withdrawal from the conspiracy. Is Bex guilty..."
-->

## Issue 3 — argpass-opus

**Q3.** Assume prosecutors charge Bex with Alba's assault on Dane. Is Bex guilty of the assault under the *Pinkerton* doctrine?

(a) Guilty, because Alba's use of violence to protect the operation was a reasonably foreseeable consequence of an armed drug distribution conspiracy. <!-- correct -->
(b) Guilty, because the doctrine imposes strict liability on all co-conspirators for any crime committed in the same physical location.
(c) Not guilty, because Bex did not explicitly agree to assault neighbors when she entered the initial distribution conspiracy.
(d) Not guilty, because Alba's specific intent to knock Dane unconscious was not shared by Bex during the confrontation.
(e) Not guilty, because Alba committed the assault after the primary drug transaction with Cody had already been concluded.

**Answer:** (a)

**Explanation:** (a) is correct because under the *Pinkerton* doctrine, a conspirator is liable for the substantive offenses committed by a co-conspirator that are reasonably foreseeable and in furtherance of the conspiracy; using a weapon brought to protect the drug operation meets this standard. (b) is wrong because *Pinkerton* requires foreseeability and furtherance, not strict location-based liability. (c) is wrong because explicit agreement to the specific substantive crime is not required, only foreseeability. (d) is wrong because *Pinkerton* liability relies on agency principles, dispensing with the need for the co-conspirator to share the specific intent of the perpetrator. (e) is wrong because the conspiracy was ongoing and the assault was in furtherance of protecting the operation from exposure.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton liability, foreseeability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, pinkerton-doctrine

<!-- argument-pass: SHOULD FIX
(a) Argument-for: *Pinkerton* liability holds conspirators vicariously liable for the substantive crimes of their co-conspirators if the crimes are in furtherance of the conspiracy and reasonably foreseeable. In an armed drug distribution conspiracy, violence used to protect the enterprise or effectuate escape is classically foreseeable. Since Alba assaulted Dane to protect the drug operation, Bex is liable for this reasonably foreseeable consequence of their criminal agreement.
(b) Argument-for: A student could argue that this option attempts to capture the practical application of *Pinkerton* in enclosed physical spaces. If conspirators are actively operating a drug distribution site, any crime committed within that perimeter is functionally treated as "in furtherance" of the enterprise. Under this reading, the doctrine creates a strict-liability zone for co-conspirators present at the crime scene, making Bex guilty because she was at the location of the conspiracy's execution.
(c) Argument-for: *Pinkerton* liability is bounded by the scope of the conspiratorial agreement. A student could argue that an unprovoked or sudden assault on a neighbor deviates so significantly from the core objective of selling drugs that it constitutes an independent frolic. Under this theory, unless Bex explicitly agreed to include neighborhood assaults within the scope of the conspiracy, Alba's act falls outside the bounds of foreseeable furtherance.
(d) Argument-for: Fundamental principles of criminal law generally require a defendant to possess the requisite *mens rea* for a crime. A student could argue that while *Pinkerton* imputes the *actus reus* of a co-conspirator, it cannot constitutionally bypass the specific intent required for the substantive offense (here, the intent to knock Dane unconscious). Thus, Bex cannot be guilty because she did not share the specific intent for the assault.
(e) Argument-for: A conspiracy legally terminates once its central objectives have been achieved or abandoned. A student could argue that because the primary drug transaction with Cody had concluded, the main objective of the conspiracy was complete. Once a conspiracy terminates, *Pinkerton* liability does not extend to subsequent independent crimes, absolving Bex of liability for Alba's post-transaction assault.

Head-to-head: Option (a) correctly applies the core *Pinkerton* elements of foreseeability and furtherance. Distractor (b) is easily falsifiable because it explicitly invokes "strict liability... for any crime." However, distractors (c), (d), and (e) rely on implied false legal standards (e.g., that explicit agreement or shared intent is required, or that completing a primary transaction ends liability). While substantively wrong, they fail the strict "close-call standard" because they lack absolute locking words (like "solely," "categorically," or "automatically") to render the underlying legal propositions explicitly falsifiable.

Falsifiable claim per distractor:
- (b): "imposes strict liability on all co-conspirators for any crime committed in the same physical location." — wrong because *Pinkerton* requires the substantive offense to be reasonably foreseeable and in furtherance of the conspiracy, not merely geographically proximate.
- (c): "because Bex did not explicitly agree" — wrong because *Pinkerton* explicitly dispenses with the need for agreement to the specific substantive crime, requiring only foreseeability based on the broader conspiracy.
- (d): "because Alba's specific intent... was not shared by Bex" — wrong because *Pinkerton* imputes both the act and the requisite intent via agency principles; shared specific intent for the substantive offense is not required.
- (e): "because Alba committed the assault after the primary drug transaction... had already been concluded." — wrong because the completion of a single transaction does not automatically terminate an ongoing distribution conspiracy, especially when acts of concealment or protection follow.

Recommended fix: Add absolute words to (c), (d), and (e) to lock in the false legal rules.
Edit (c) to: "Not guilty, solely because Bex did not explicitly agree to assault neighbors when she entered the initial distribution conspiracy."
Edit (d) to: "Not guilty, because Pinkerton categorically requires that the specific intent of the perpetrator be shared by the co-conspirator."
Edit (e) to: "Not guilty, because Pinkerton liability automatically terminates once the primary drug transaction concludes."
-->
