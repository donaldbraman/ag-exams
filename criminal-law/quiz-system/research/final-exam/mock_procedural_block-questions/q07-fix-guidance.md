# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Assume the trial proceeds and Thorne formally files a motion for discovery on selective prosecution. Under the *Armstrong* standard, will Thorne succeed in obtaining discovery?

(a) No, because he must first produce credible evidence that similarly situated individuals of a different race could have been prosecuted but were not. <!-- correct -->
(b) Yes, because a 95% disparate impact constitutes overwhelming statistical proof of discriminatory intent, shifting the burden of production to the prosecution.
(c) No, because selective prosecution claims can only be raised during post-conviction proceedings and are explicitly barred from the pretrial discovery phase.
(d) Yes, because defense attorneys have an absolute right to prosecutorial records whenever a disparate impact claim is formally alleged during a criminal trial.
(e) No, because statistical evidence of racial disparity must be exclusively handled through the Batson framework rather than through selective prosecution motions.

**Answer:** (a)

**Explanation:** (a) is correct because under *Armstrong*, a defendant seeking discovery for selective prosecution must provide credible evidence that similarly situated individuals of a different race could have been prosecuted but were not; aggregate statistical impact alone is insufficient. (b) is incorrect because *McCleskey* and *Armstrong* explicitly reject aggregate statistics as sufficient proof of individual discriminatory intent. (c) is incorrect because selective prosecution claims can be raised pretrial if the demanding evidentiary threshold is met. (d) is incorrect because there is no absolute right to prosecutorial records; the presumption of regularity protects prosecutors absent threshold evidence. (e) is incorrect because *Batson* applies only to jury selection, while *Armstrong* governs selective prosecution claims.

**Tags:** chapters: [6], topics: [selective prosecution, Armstrong, discovery], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 6 - United States v. Armstrong; armstrong-discovery-catch22

<!-- audit: MUST FIX
<check 1>: pass
<check 2>: pass
<check 3>: pass
<check 4>: fails. The question relies on a missing vignette ("Assume the trial proceeds and Thorne..."). Without knowing what evidence Thorne actually submitted, we cannot definitively conclude he will fail to obtain discovery. If the missing vignette established he *did* provide comparator evidence, (a) would be incorrect in outcome. 
<check 5>: pass
<check 6>: pass
<check 7>: pass
<check 8>: pass
Recommended fix: Add the necessary factual premise to the stem to make it standalone. E.g., "Thorne, relying solely on a study showing a 95% racial disparate impact in charging, formally files a motion for discovery on selective prosecution. Under the Armstrong standard, will Thorne succeed in obtaining discovery?"
-->

## Issue 2 — edge-case

**Q7.** Assume the trial proceeds and Thorne formally files a motion for discovery on selective prosecution. Under the *Armstrong* standard, will Thorne succeed in obtaining discovery?

(a) No, because he must first produce credible evidence that similarly situated individuals of a different race could have been prosecuted but were not. <!-- correct -->
(b) Yes, because a 95% disparate impact constitutes overwhelming statistical proof of discriminatory intent, shifting the burden of production to the prosecution.
(c) No, because selective prosecution claims can only be raised during post-conviction proceedings and are explicitly barred from the pretrial discovery phase.
(d) Yes, because defense attorneys have an absolute right to prosecutorial records whenever a disparate impact claim is formally alleged during a criminal trial.
(e) No, because statistical evidence of racial disparity must be exclusively handled through the Batson framework rather than through selective prosecution motions.

**Answer:** (a)

**Explanation:** (a) is correct because under *Armstrong*, a defendant seeking discovery for selective prosecution must provide credible evidence that similarly situated individuals of a different race could have been prosecuted but were not; aggregate statistical impact alone is insufficient. (b) is incorrect because *McCleskey* and *Armstrong* explicitly reject aggregate statistics as sufficient proof of individual discriminatory intent. (c) is incorrect because selective prosecution claims can be raised pretrial if the demanding evidentiary threshold is met. (d) is incorrect because there is no absolute right to prosecutorial records; the presumption of regularity protects prosecutors absent threshold evidence. (e) is incorrect because *Batson* applies only to jury selection, while *Armstrong* governs selective prosecution claims.

**Tags:** chapters: [6], topics: [selective prosecution, Armstrong, discovery], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 6 - United States v. Armstrong; armstrong-discovery-catch22

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The phrase "Assume the trial proceeds" chronologically places a pretrial discovery motion during the trial phase. While the distractors focus on the substantive *Armstrong* standard, a sharp student might be distracted by the procedural timing anomaly. Furthermore, the question should explicitly specify that Thorne is relying on the statistical data mentioned in the fact pattern.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change "Assume the trial proceeds and Thorne formally files a motion for discovery on selective prosecution." to "Assume that prior to trial, Thorne formally files a motion for discovery on selective prosecution based on the leaked statistical data."
-->
