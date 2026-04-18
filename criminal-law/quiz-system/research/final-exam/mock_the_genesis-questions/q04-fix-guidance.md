# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Assume Albert is charged under the State Public Welfare Chemical Act for storing more than 5 gallons of ether without a permit. The defense argues the prosecution must prove he knew about the permit requirement. How will the court likely rule?

(a) The statute imposes strict liability, because ether is a highly dangerous item, the penalty is minor, and the regulation clearly targets public health and safety. <!-- correct -->
(b) The statute requires proof of knowledge, because the Morissette presumption always mandates a mens rea requirement whenever a criminal statute is entirely silent.
(c) The statute imposes strict liability, because all state criminal codes have explicitly abolished the common law presumption against absolute criminal liability.
(d) The statute requires proof of recklessness, because the Model Penal Code default rule strictly applies to all environmental and commercial chemical safety regulations.
(e) The statute imposes strict liability, because the maximum penalty of thirty days in jail automatically classifies the storage offense as a mere civil infraction.

**Answer:** (a)

**Explanation:** Under the *Morissette* framework, a statute silent on mental state may be construed as a public welfare offense (strict liability) if it regulates dangerous items (ether), carries a minor penalty (30 days in jail), and serves a broad regulatory purpose (fire safety/public welfare) rather than punishing inherently wrongful conduct. (b) is wrong because the *Morissette* presumption against strict liability can be rebutted when the four public welfare factors are satisfied. (c) is wrong because the common law presumption against absolute liability has not been universally abolished; it remains a fundamental baseline. (d) is wrong because the MPC default rule of recklessness applies in MPC jurisdictions, but the prompt asks about the public welfare doctrine specifically, which recognizes strict liability for these exact types of regulations. (e) is wrong because a penalty of 30 days in jail constitutes criminal imprisonment, making it a criminal offense, not a mere civil infraction, even though the penalty is considered "minor" for strict liability purposes.

**Tags:** chapters: [11], topics: [public_welfare_offenses, strict_liability, morissette], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 - Public Welfare Offenses: The Morissette four-factor framework

<!-- audit: MUST FIX
check 1: fail (The question conflates the *Morissette* strict liability doctrine with mistake of law. Albert arguing the prosecution must prove he "knew about the permit requirement" raises a mistake of law defense, which generally fails for almost all crimes under the baseline rule of *ignorantia juris non excusat*. The *Morissette* analysis is designed to determine if a court should dispense with the mens rea for *factual* elements. To properly test the public welfare doctrine, the defense should be arguing a mistake of fact.)
check 2: pass
check 3: fail (The explanation references a "minor penalty (30 days in jail)" which is completely absent from the question stem.)
check 4: fail (The stem omits the statutory penalty. Under the *Morissette/Staples* doctrine, penalty severity is a required factor for public welfare analysis. Without knowing the penalty, a prepared student cannot evaluate Option A's premise that "the penalty is minor.")
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: 1. Add the penalty to the stem (e.g., "Assume Albert is charged under the State Public Welfare Chemical Act, which carries a maximum penalty of 30 days in jail..."). 2. Change the defense's argument to a mistake of fact to properly trigger the public welfare strict liability framework (e.g., "The defense argues the prosecution must prove Albert knew the substance was ether.").
-->

## Issue 2 — edge-case

**Q4.** Assume Albert is charged under the State Public Welfare Chemical Act for storing more than 5 gallons of ether without a permit. The defense argues the prosecution must prove he knew about the permit requirement. How will the court likely rule?

(a) The statute imposes strict liability, because ether is a highly dangerous item, the penalty is minor, and the regulation clearly targets public health and safety. <!-- correct -->
(b) The statute requires proof of knowledge, because the Morissette presumption always mandates a mens rea requirement whenever a criminal statute is entirely silent.
(c) The statute imposes strict liability, because all state criminal codes have explicitly abolished the common law presumption against absolute criminal liability.
(d) The statute requires proof of recklessness, because the Model Penal Code default rule strictly applies to all environmental and commercial chemical safety regulations.
(e) The statute imposes strict liability, because the maximum penalty of thirty days in jail automatically classifies the storage offense as a mere civil infraction.

**Answer:** (a)

**Explanation:** Under the *Morissette* framework, a statute silent on mental state may be construed as a public welfare offense (strict liability) if it regulates dangerous items (ether), carries a minor penalty (30 days in jail), and serves a broad regulatory purpose (fire safety/public welfare) rather than punishing inherently wrongful conduct. (b) is wrong because the *Morissette* presumption against strict liability can be rebutted when the four public welfare factors are satisfied. (c) is wrong because the common law presumption against absolute liability has not been universally abolished; it remains a fundamental baseline. (d) is wrong because the MPC default rule of recklessness applies in MPC jurisdictions, but the prompt asks about the public welfare doctrine specifically, which recognizes strict liability for these exact types of regulations. (e) is wrong because a penalty of 30 days in jail constitutes criminal imprisonment, making it a criminal offense, not a mere civil infraction, even though the penalty is considered "minor" for strict liability purposes.

**Tags:** chapters: [11], topics: [public_welfare_offenses, strict_liability, morissette], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 - Public Welfare Offenses: The Morissette four-factor framework

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: The prompt states the defense argues the prosecution must prove Albert "knew about the permit requirement." This inadvertently triggers the Mistake of Law doctrine (ignorance of the law is no excuse). Even if the statute did require a mens rea (and was not strict liability), the court would reject the defense's specific claim because knowledge of the law is almost never required for this type of offense. This bypasses the intended Morissette analysis, as the defense's argument is flawed on a completely separate doctrinal baseline.
3. Cross-Question Spoilers: Q5 explicitly tests Mistake of Law, so students will be primed to notice that the defense's argument in Q4 fails due to MOL rather than public welfare strict liability. 
Recommended fix: Change "The defense argues the prosecution must prove he knew about the permit requirement." to "The defense argues the court must read a mens rea requirement into the silent statute."
-->
