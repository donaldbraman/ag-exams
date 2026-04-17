# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — edge-case

**Q12.** Assume that Bex is charged with both intentional murder and felony murder for Cody's death. She raises the defense of duress based on Alba's threat to shoot her. How does the common law analyze this defense?

(a) Bex is categorically barred from raising duress to intentional murder, but may raise it against felony murder if the defense applies to the underlying predicate felony. <!-- correct -->
(b) Bex may raise duress against intentional murder because Alba's threat of immediate death from a loaded handgun overcomes the traditional categorical murder bar.
(c) Bex is categorically barred from raising duress to any homicide charge, including felony murder, because human life cannot be balanced against another under any circumstances.
(d) Bex may raise duress against any homicide charge because she was merely an intimidated bystander who did not actively inflict the fatal harm upon the victim.
(e) Bex is categorically barred from raising duress to any charge because she was initially at fault for voluntarily engaging in the illegal drug conspiracy.

**Answer:** (a)

**Explanation:** Under the common law, the defense of duress is categorically unavailable for intentional murder. However, several jurisdictions recognize an exception for felony murder, allowing the defense if the defendant was coerced into committing the underlying predicate felony. (b) is wrong because the common law murder bar is absolute and is not overcome by the imminence or severity of the threat. (c) is wrong because several states have explicitly carved out a felony-murder exception to the traditional bar. (d) is wrong because being an intimidated bystander does not bypass the strict legal limits of the murder bar. (e) is wrong because engaging in a conspiracy does not automatically foreclose duress for subsequent, unrelated coerced acts.

**Tags:** chapters: [21], topics: [duress-murder-bar, felony-murder-duress-exception], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 21 — Necessity and Duress: Duress Murder Bar and Felony Murder Exception

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The predicate felony in this scenario (fentanyl distribution) occurred *before* the duress (the gun threat). Therefore, duress factually cannot apply to negate her predicate felony. Option (a) forces the student to endorse an abstract rule that has no factual footing in Bex's actual felony murder charge.
2. Cross-Doctrine Clashes: The "At-Fault" limitation on duress. Under common law, a defendant who voluntarily joins a criminal enterprise (like a fentanyl distribution conspiracy) is generally barred from raising a duress defense for subsequent coercion by co-conspirators. This arguably triggers the exact rationale in Option (e), making (e) a legally viable answer and creating a multiple-correct-answer flaw. 
3. Cross-Question Spoilers: Q13 establishes the felony murder charge is based on the initial drug distribution (Facts 1-3), locking in the fact that the predicate felony occurred prior to the duress (Facts 5-6).
Recommended fix: Rewrite Option (a) to explicitly apply the rule to her facts (e.g., "...though it would fail here because her predicate felony was completed prior to the threat"). To fix the Option (e) clash, change its rationale to something legally fictitious rather than the actual common law "at-fault" rule (e.g., "because she was the primary tenant of the apartment where the crime occurred").
-->
