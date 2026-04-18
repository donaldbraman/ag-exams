# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** Assume Marcus pursues an Equal Protection selective prosecution claim and requests discovery on uncharged white drivers. How will the court rule?

(a) Grant the request, because demonstrating that 90% of stopped drivers are Black establishes a clear prima facie case of systemic discriminatory intent.
(b) Grant the request, because discovery is universally required whenever a defendant alleges structural bias in a municipal law enforcement operation like Operation Sweep.
(c) Deny the request, because Marcus failed to produce credible evidence of similarly situated white drivers who were not stopped or charged by the police. <!-- correct -->
(d) Deny the request, because selective prosecution claims can only be brought against federal prosecutors, not against local police officers conducting traffic stops.
(e) Deny the request, because the Equal Protection Clause does not legally apply to discretionary law enforcement initiatives designed to secure local public safety.

**Answer:** (c)

**Explanation:** The correct answer is (c). Under *United States v. Armstrong*, to obtain discovery for a selective prosecution or selective enforcement claim, a defendant must first produce "credible evidence" showing that similarly situated individuals of a different race could have been prosecuted or stopped but were not. Statistical evidence about who *was* stopped (Fact 5) is insufficient without evidence of the uncharged comparison group.

(a) is incorrect because the Supreme Court explicitly rejected aggregate statistical disparities as a basis for discovery in *Armstrong*.
(b) is incorrect because there is a strong presumption of regularity in law enforcement, and discovery is heavily restricted by the *Armstrong* catch-22 standard.
(d) is incorrect because Equal Protection constraints and the *Armstrong* standard apply to selective enforcement by police as well as selective prosecution by prosecutors.
(e) is incorrect because the Equal Protection Clause absolutely prohibits racially discriminatory enforcement of the law, even in discretionary initiatives.

**Tags:** chapters: [6], topics: [selective-prosecution-standard, armstrong-discovery-catch22], difficulty: medium, cognitive: application

**Grounding:** Chapter 6 - Prosecutors > Armstrong discovery Catch-22

<!-- audit: SHOULD FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem relies on a missing master fact pattern (referencing Marcus, Operation Sweep, and "Fact 5" in the explanation). Without knowing what evidence Marcus submitted with his motion, a student cannot definitively conclude he "failed to produce credible evidence" as required by (c).
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Integrate the necessary facts into the stem so it stands alone or explicitly connects to the fact pattern. Edit the stem to: "Assume Marcus pursues an Equal Protection selective enforcement claim and requests discovery on uncharged white drivers, relying solely on statistical evidence that 90% of stopped drivers are Black. How will the court rule?"
-->
