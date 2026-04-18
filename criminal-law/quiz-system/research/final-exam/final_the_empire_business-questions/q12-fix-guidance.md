# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Dominic was arrested outside Elias's home. Assume the jurisdiction follows the MPC substantial step test. Is Dominic guilty of attempted murder?

(a) Yes, because taking a concealed firing position and tracking the target strongly corroborates his criminal purpose and constitutes a substantial step toward the intended killing. <!-- correct -->
(b) No, because he had not yet pulled the trigger, meaning he could have still voluntarily abandoned his effort before any actual physical harm was inflicted upon Elias.
(c) Yes, because the mere purchase of the sniper rifle with the specific premeditated intent to kill Elias is legally sufficient to satisfy the substantial step requirement.
(d) No, because the sudden FBI intervention made it factually impossible for him to complete the crime, which provides a complete defense under the modern Model Penal Code.
(e) Yes, because his previous success in killing Victor demonstrates a pattern of violence that satisfies the objective requirements of the attempt actus reus element for the current charge.

**Answer:** (a)

**Explanation:** Under the MPC's substantial step test, taking a concealed firing position and tracking the target through a scope strongly corroborates Dominic's criminal purpose and easily constitutes a substantial step. (b) is incorrect because the MPC does not require the defendant to reach the "last act," and while abandonment is a defense, it must be completely voluntary, not thwarted by police intervention. (c) is incorrect because mere preparation, such as buying a weapon, is typically insufficient even under the MPC's broader standard unless accompanied by acts closer to the crime. (d) is incorrect because the MPC explicitly rejects factual impossibility as a defense to attempt. (e) is incorrect because a defendant's past criminal history is not an actus reus element of the current attempt charge.

**Tags:** chapters: [17], topics: [attempt, actus reus, substantial step, MPC], difficulty: easy, cognitive: application

**Grounding:** MPC 5.01; Substantial step test

<!-- audit: MUST FIX
Check 1: pass (Assuming the facts existed in the stem, the legal conclusion accurately applies the MPC substantial step test).
Check 2: pass
Check 3: pass
Check 4: FAILS. The stem is entirely missing the factual scenario. It only states that Dominic was arrested outside Elias's home. The options and explanation reference facts that are nowhere in the stem (e.g., taking a concealed firing position, tracking the target through a scope, buying a sniper rifle, FBI intervention, and previously killing Victor). A student cannot answer this without the facts.
Check 5: pass
Check 6: pass
Check 7: pass (MPC substantial step is covered in Ch 17).
Recommended fix: Insert the missing factual scenario into the stem (e.g., "Dominic bought a sniper rifle, went to Elias's home, took a concealed firing position, and was tracking Elias through the scope when the FBI suddenly intervened and arrested him...").
-->
