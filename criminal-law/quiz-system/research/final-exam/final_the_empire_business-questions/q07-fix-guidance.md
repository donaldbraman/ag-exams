# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q7.** The government charges Jack with RICO conspiracy under § 1962(d) based on the November 1 written agreement to launch the "Tri-State Waste" syndicate the following year. Jack moves to dismiss, arguing that because "Tri-State" had no operations and did not yet exist, there was no enterprise to conspire about. How should the court rule?

(a) Grant the motion, because a RICO conspiracy charge requires the prosecution to prove that the targeted enterprise was fully operational at the time of agreement.
(b) Deny the motion, because an agreement to associate with and participate in a yet-to-be-formed future racketeering enterprise constitutes a completed RICO conspiracy offense. <!-- correct -->
(c) Grant the motion, because Jack and Kevin had not yet committed the minimum of two predicate racketeering acts required to establish the conspiracy's pattern.
(d) Deny the motion, but only because the previous operations of Empire Waste can be legally imputed to the future Tri-State Waste organization.
(e) Grant the motion, because punishing an agreement to form a future enterprise violates the constitutional prohibition against criminalizing mere gang membership.

**Answer:** (b)

**Explanation:** The correct answer is (b). Under *United States v. Rich*, an agreement to associate with and participate in a future, yet-to-be-formed racketeering enterprise satisfies the enterprise element for a RICO conspiracy. (a) is wrong because the enterprise need not presently exist; the offense of conspiracy targets the illicit agreement to commit future substantive offenses. (c) is wrong because under *Salinas*, a defendant need not personally commit (or have already committed) two predicate acts to be guilty of RICO conspiracy, as long as they agree to an endeavor that would satisfy the elements. (d) is wrong because the government does not need to impute Empire Waste's operations to Tri-State; the agreement to form the new enterprise is sufficient on its own. (e) is wrong because RICO conspiracy punishes the agreement to participate in an enterprise through racketeering activity, which is distinct from punishing mere status or gang membership (*State v. O.C.*).

**Tags:** chapters: [20], topics: [RICO conspiracy, future enterprise], difficulty: hard, cognitive: application

**Grounding:** Chapter 20, RICO Conspiracy (rich-future-enterprise; United States v. Rich)

<!-- GROUNDING-FAIL: United States v. Rich (future enterprise) is not in any chapter map. The closest taught doctrines are: none available (meta-map missing). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q7.** The government charges Jack with RICO conspiracy under § 1962(d) based on the November 1 written agreement to launch the "Tri-State Waste" syndicate the following year. Jack moves to dismiss, arguing that because "Tri-State" had no operations and did not yet exist, there was no enterprise to conspire about. How should the court rule?

(a) Grant the motion, because a RICO conspiracy charge requires the prosecution to prove that the targeted enterprise was fully operational at the time of agreement.
(b) Deny the motion, because an agreement to associate with and participate in a yet-to-be-formed future racketeering enterprise constitutes a completed RICO conspiracy offense. <!-- correct -->
(c) Grant the motion, because Jack and Kevin had not yet committed the minimum of two predicate racketeering acts required to establish the conspiracy's pattern.
(d) Deny the motion, but only because the previous operations of Empire Waste can be legally imputed to the future Tri-State Waste organization.
(e) Grant the motion, because punishing an agreement to form a future enterprise violates the constitutional prohibition against criminalizing mere gang membership.

**Answer:** (b)

**Explanation:** The correct answer is (b). Under *United States v. Rich*, an agreement to associate with and participate in a future, yet-to-be-formed racketeering enterprise satisfies the enterprise element for a RICO conspiracy. (a) is wrong because the enterprise need not presently exist; the offense of conspiracy targets the illicit agreement to commit future substantive offenses. (c) is wrong because under *Salinas*, a defendant need not personally commit (or have already committed) two predicate acts to be guilty of RICO conspiracy, as long as they agree to an endeavor that would satisfy the elements. (d) is wrong because the government does not need to impute Empire Waste's operations to Tri-State; the agreement to form the new enterprise is sufficient on its own. (e) is wrong because RICO conspiracy punishes the agreement to participate in an enterprise through racketeering activity, which is distinct from punishing mere status or gang membership (*State v. O.C.*).

**Tags:** chapters: [20], topics: [RICO conspiracy, future enterprise], difficulty: hard, cognitive: application

**Grounding:** Chapter 20, RICO Conspiracy (rich-future-enterprise; United States v. Rich)

<!-- audit: SHOULD FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: Factual leak/omission. Distractor (c) suddenly references "Kevin," and distractor (d) references "Empire Waste," but neither Kevin nor Empire Waste is mentioned anywhere in the stem. 
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Update the stem to include these missing details so the distractors make sense. E.g., "The government charges Jack with RICO conspiracy... based on his November 1 written agreement with Kevin to close their existing company, Empire Waste, and launch the 'Tri-State Waste' syndicate the following year."
-->

## Issue 3 — argpass-sonnet

**Q7.** The government charges Jack with RICO conspiracy under § 1962(d) based on the November 1 written agreement to launch the "Tri-State Waste" syndicate the following year. Jack moves to dismiss, arguing that because "Tri-State" had no operations and did not yet exist, there was no enterprise to conspire about. How should the court rule?

(a) Grant the motion, because a RICO conspiracy charge requires the prosecution to prove that the targeted enterprise was fully operational at the time of agreement.
(b) Deny the motion, because an agreement to associate with and participate in a yet-to-be-formed future racketeering enterprise constitutes a completed RICO conspiracy offense. <!-- correct -->
(c) Grant the motion, because Jack and Kevin had not yet committed the minimum of two predicate racketeering acts required to establish the conspiracy's pattern.
(d) Deny the motion, but only because the previous operations of Empire Waste can be legally imputed to the future Tri-State Waste organization.
(e) Grant the motion, because punishing an agreement to form a future enterprise violates the constitutional prohibition against criminalizing mere gang membership.

**Answer:** (b)

**Explanation:** The correct answer is (b). Under *United States v. Rich*, an agreement to associate with and participate in a future, yet-to-be-formed racketeering enterprise satisfies the enterprise element for a RICO conspiracy. (a) is wrong because the enterprise need not presently exist; the offense of conspiracy targets the illicit agreement to commit future substantive offenses. (c) is wrong because under *Salinas*, a defendant need not personally commit (or have already committed) two predicate acts to be guilty of RICO conspiracy, as long as they agree to an endeavor that would satisfy the elements. (d) is wrong because the government does not need to impute Empire Waste's operations to Tri-State; the agreement to form the new enterprise is sufficient on its own. (e) is wrong because RICO conspiracy punishes the agreement to participate in an enterprise through racketeering activity, which is distinct from punishing mere status or gang membership (*State v. O.C.*).

**Tags:** chapters: [20], topics: [RICO conspiracy, future enterprise], difficulty: hard, cognitive: application

**Grounding:** Chapter 20, RICO Conspiracy (rich-future-enterprise; United States v. Rich)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under 18 U.S.C. § 1962(c), a defendant must associate with an "enterprise engaged in... interstate or foreign commerce." Since the conspiracy provision (§ 1962(d)) targets agreements to violate substantive RICO provisions, a student could argue that the statutory text inherently demands an existing enterprise with an actual commerce nexus. Without a fully operational enterprise, it is legally impossible to agree to participate in its affairs. Therefore, the charge must be dismissed.
(b) Argument-for: The core of a conspiracy charge is the illicit agreement itself, not the completion of the substantive offense. Under federal precedent, a RICO conspiracy under § 1962(d) is established when defendants agree to form a future racketeering enterprise and participate in its affairs through a pattern of racketeering activity. The enterprise does not need to exist at the moment of the agreement. Thus, the court should deny the motion.
(c) Argument-for: The hallmark of any RICO charge is the "pattern of racketeering activity," which requires at least two predicate acts. A student could argue that until Jack (and his co-conspirators) actually commit these two requisite acts, the pattern element remains unsatisfied and the conspiracy remains an unpunishable inchoate thought. Because no predicate acts have been committed to manifest the agreement, the motion to dismiss should be granted.
(d) Argument-for: A court might be hesitant to recognize a purely prospective, nonexistent enterprise under RICO due to jurisdictional requirements. However, a student could argue that the indictment survives solely through the continuity of operations doctrine. If the future entity is factually a successor to a prior syndicate (e.g., "Empire Waste"), the predecessor's operations provide the necessary legal foundation. Thus, the motion is denied, but *only* because of this legal imputation.
(e) Argument-for: The Constitution prohibits criminalizing mere status, association, or gang membership under First Amendment principles and cases like *Scales v. United States*. A student could argue that prosecuting an agreement to form a syndicate that has no operations and has committed no crimes is tantamount to criminalizing the mere intent to associate with unsavory individuals. This violates constitutional protections against punishing pure gang membership, requiring dismissal.

Head-to-head: Option (b) is the correct application of *United States v. Rich* and *Salinas v. United States*, correctly noting that a RICO conspiracy charge does not require a currently existing enterprise, only an agreement to form one and commit racketeering acts. Option (a) is definitively false because it adds an absolute requirement that the enterprise be "fully operational," contradicting conspiracy doctrine. Option (c) asserts that defendants must have "committed the minimum of two predicate racketeering acts," which violates the core holding of *Salinas* that conspiracy does not require the completion of substantive predicates. Option (d) uses the absolute phrase "but only because" to falsely claim that the enterprise element can exclusively be met via imputation from a past entity. Option (e) makes the false legal claim that prosecuting a RICO conspiracy "violates the constitutional prohibition against criminalizing mere gang membership," whereas an active agreement to commit racketeering crimes is distinct from mere status. However, options (c) and (d) introduce a character ("Kevin") and an entity ("Empire Waste") that are completely absent from the question stem. This factual leak makes the question technically flawed and confusing, mandating a fix.

Falsifiable claim per distractor:
- (a): "requires the prosecution to prove that the targeted enterprise was fully operational at the time of agreement" — wrong because RICO conspiracy requires only an agreement to associate with a future enterprise, not a fully operational one.
- (c): "had not yet committed the minimum of two predicate racketeering acts required to establish the conspiracy's pattern" — wrong because under *Salinas*, a defendant need not personally commit any predicate acts to be guilty of RICO conspiracy, only agree that the pattern will be committed.
- (d): "but only because the previous operations of Empire Waste can be legally imputed" — wrong because the phrase "only because" makes imputation a strict legal necessity, whereas an agreement to form a new enterprise is sufficient on its own.
- (e): "violates the constitutional prohibition against criminalizing mere gang membership" — wrong because criminalizing an explicit agreement to commit racketeering acts through an enterprise penalizes conduct (the agreement), not mere status or gang membership.

Recommended fix: SHOULD FIX. Remove the ghost references to unmentioned facts in options (c) and (d). Change (c) to "...because Jack and his co-conspirators had not yet committed..." and change (d) to "...but only because the previous operations of a predecessor syndicate can be legally imputed...".
-->
