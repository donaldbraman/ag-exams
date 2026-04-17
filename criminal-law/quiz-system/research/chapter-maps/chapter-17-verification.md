# Verification Report: Chapter 17 Map

- Chapter: 17 — Attempts
- Map file: criminal-law/quiz-system/research/chapter-maps/chapter-17.md
- Verified at: 2026-04-14
- Verifier model: claude-sonnet-4-6

---

## 1. Structural Compliance

| Check | Status | Notes |
|-------|--------|-------|
| Has `## Meta` block | PASS | All fields present: chapter, title, source file, source hash, generated at, model |
| Has `## Elements` with three-tier structure | PASS | Prima Facie Elements, Liability Extensions, Liability Limits all present |
| All refinements use kebab-case keys | PASS | Verified: all keys are `kebab-case` |
| All refinements include Rule, Source, Difficulty, Pivot fact, Jurisdiction | PASS | Every refinement has all mandatory fields |
| Trap format: "Students [X] because [Y]" | PASS | All traps follow the mandatory format |
| `Practiced` field: only where slide digest confirms | PASS | Practiced fields reference specific slides; omitted where not practiced |
| `## Clusters` section present | PASS | 6 clusters defined |
| Each cluster has Refinements, Why they cluster, Scenario hook | PASS | All three fields present for each cluster |
| `## Cases` section present | PASS | 11 cases documented |
| Each case has Holding, Reasoning, Facts, Teaches, Source type, Discussion questions | PASS | All fields present for every case |
| `## Coverage Checklist` present as table | PASS | 23 refinement keys listed with section, difficulty, practiced |
| No line-range tables, no statutes section, no hypo seeds | PASS | None present |

---

## 2. Content Accuracy Checks

### Elements Section
- **Specific intent requirement for result elements:** Accurately stated. Chapter text (Mens Rea section, pp. 38–44) states: "the defendant must have intended that result... must have acted with *purpose* to cause the result." ✓
- **Asymmetry between attempt mens rea and completed crime:** Correctly identified — "attempted depraved-heart murder" logical impossibility noted in chapter. ✓
- **Proximity test minority, substantial step majority:** Chapter table confirms: proximity = minority (~8–15 states), substantial step = majority (~30–34 states + all federal circuits). ✓
- **Abandonment roughly half/half split:** Chapter confirms "roughly half of states" for both common law (no abandonment) and MPC (abandonment defense). ✓

### Refinements — Accuracy Spot Checks
- **actus-reus-proximity-test / Rizzo:** Acquittal confirmed — "judgment of conviction...must be reversed." ✓
- **actus-reus-proximity-test / Peaslee:** Correctly characterized as "coy" — Holmes declined to rule definitively on whether conduct crossed the line. ✓
- **actus-reus-proximity-modern / Lendof-Gonzalez:** Map states "convicted of criminal solicitation rather than attempt." Chapter confirms. ✓
- **kill-zone-theory / Canizales:** Map states five shots from 100–160 feet insufficient. Chapter confirms exact facts and holding. ✓
- **abandonment-mpc / Roske:** Map states "97 months" and "33 minutes after arriving." Chapter confirms both. ✓
- **grading-path2-offense-specific / § 846:** Map correctly states mandatory minimums apply in full and USSG § 2X1.1 reduction does not apply when offense definition incorporates attempt. ✓
- **sting-operations / Whitmer:** Map states "54.7% involved government informants," "~9% thwarted genuinely threatening plots," "12 confidential informants and 2 undercover agents," "5 of 14 acquitted." Chapter confirms all figures. ✓
- **specific-intent-gap / Kapoor:** Map states "66 months." Chapter confirms. ✓

### Jurisdiction Flags — Accuracy
- All refinements marked with a jurisdiction flag. ✓
- Proximity test correctly flagged as majority/minority (minority ~8–15 states). ✓
- Substantial step correctly flagged as majority/minority (majority ~30–34 states). ✓
- Abandonment correctly flagged as split (traditional/MPC). ✓
- Kill zone flagged as majority/minority (California-origin; variable adoption). ✓ (appropriate given the chapter doesn't provide precise adoption count for kill zone)
- Taylor flagged as federal only. ✓
- Path 2 offense-specific grading flagged as federal only with note on state equivalents. ✓

### Cases — Accuracy
- 11 cases documented; chapter contains these main cases and note cases:
  - Main cases: *Peaslee*, *Rizzo*, *Lendof-Gonzalez*, *Canizales* — all present ✓
  - Note cases: *Taylor*, *Routh*, *Roske*, *Garner*, *Croft*, *Simon/Insys*, *Jade* — all present ✓
  - *State v. White* (cross-referenced from Ch. 15, not a main case in Ch. 17) — correctly used as a refinement source, not given its own case entry since it is not a Ch. 17 case ✓
  - Voodoo hypothetical — correctly noted as an illustrative example in discussion questions, not given a case entry ✓
- Discussion questions flags:
  - *Rizzo*: yes ✓ (three discussion questions follow the case)
  - *Canizales*: yes ✓ (two discussion questions)
  - *Lendof-Gonzalez*: yes ✓ (two discussion questions)
  - *Peaslee*: no ✓ (Peaslee's discussion questions are folded into Rizzo's callout block)
  - *Routh/Roske*: yes ✓ (shared callout with three discussion questions)
  - *Garner*: yes ✓ (in same callout as Routh/Roske)
  - *Croft*: yes ✓ (three discussion questions in sting section)
  - *Taylor*, *Simon*, *Jade*: no/yes per map — *Jade* has discussion questions in impossibility section ✓; *Taylor* and *Simon* do not ✓

---

## 3. Completeness Checks

### Doctrines Present in Chapter but Potentially Missed
- **MPC § 5.01(1)(b) "belief" standard vs. purpose:** Covered under `mens-rea-purpose-vs-knowledge` ✓
- **MPC § 5.01(2) non-exhaustive list of substantial steps:** Correctly referenced as source for `actus-reus-substantial-step` ✓
- **Criminal solicitation as the lesser charge when proximity fails:** Referenced in `actus-reus-proximity-modern` (Lendof-Gonzalez result) ✓
- **Res ipsa loquitur / equivocality test (fourth historical test):** Chapter notes this test was "largely absorbed into the MPC's substantial step requirement." Map correctly omits it as a separate refinement since it is not independently operative. ✓
- **German/English comparative systems (beginning of execution; going equipped):** Chapter mentions these in the sting operations section as design alternatives. Map does not include them as separate refinements — appropriate, as these are design comparators, not operative doctrine. ✓
- **§ 924(c) enhancement structure:** Covered under `actus-reus-substantial-step-taylor` ✓
- **Nagin (2013) deterrence finding (certainty > severity):** Covered in `resource-allocation-policy` and mentioned in grading section ✓
- **Kneer/Skoczeń (2022) outcome-driven culpability reassessment:** Covered in `grading-general-reduction` ✓

### Slide Digest Topics and Map Coverage
- **Slide 5 — Attempt Requirements table:** Covered by `mens-rea-specific-intent` (Practiced: Slide 5) ✓
- **Slide 6 — Peaslee/Rizzo comparison:** Covered by `actus-reus-proximity-test` (Practiced: Slide 6) ✓
- **Slide 11 — Common Law vs. MPC comparison table:** Covered across multiple refinements; `grading-general-reduction` and `abandonment-mpc` both note Slide 11 ✓
- **Slide 13 — Incentive structure bar graphs:** Covered by `abandonment-incentive-structure` (Practiced: Slide 13) ✓
- **Slide 14 — Roske/Routh comparison:** Covered by `actus-reus-gray-zone` and `abandonment-mpc` (Practiced: Slide 14) ✓
- **Slide 15 — Lady Eldon's Lace:** Covered by `impossibility-traditional` and `impossibility-mpc` (Practiced: Slide 15) ✓
- **Slide 16 — Where Do States Actually Fall?:** Referenced in multiple jurisdiction flags; no separate refinement needed since it is a summary slide not introducing new doctrine ✓
- **Slide 20 — Sting data (580 terrorism cases):** Covered by `sting-operations-manufactured-crime` (Practiced: Slide 20) ✓
- **Slide 22 — Garcia/Kapoor specific intent gap:** Covered by `specific-intent-gap` (Practiced: Slide 22) ✓
- **Slide 23 — Resource allocation question:** Covered by `resource-allocation-policy` (Practiced: Slide 23) ✓

---

## 4. Issues Found

### Minor Issues
1. **Liability Extensions section:** Map states "None specific to attempt itself" with a parenthetical note about felony murder. The felony murder note is helpful but the grading section (`grading-felony-murder-attempt`) handles this as a refinement. This is acceptable — the extensions section note is accurate; felony murder is not an extension of *attempt* but a separate rule that interacts with it. No change required.

2. **Peaslee case — Discussion questions flag:** Map marks Peaslee as "no" for discussion questions, noting they are "folded into Rizzo's callout." The chapter text confirms that *Rizzo* has a three-question callout that asks about *Peaslee* and *Rizzo* together. Strictly, Peaslee is discussed in *Rizzo*'s discussion question block. The "no" designation accurately reflects that Peaslee does not have its own separate discussion question callout. ✓ Acceptable.

3. **Kill zone jurisdiction flag:** Map uses "majority/minority" for kill zone theory, but the chapter does not provide state-by-state adoption counts for the kill zone doctrine. The chapter presents *Canizales* as a California case that clarifies the theory; it does not describe national adoption patterns. The flag should more precisely be `majority/minority` with a note that the doctrine originated in California and adoption is uncertain. The map's current framing is defensible but imprecise. **Recommended fix:** Add "(California origin; variable adoption)" to the Jurisdiction field for `kill-zone-theory`. Already present in map — ✓ acceptable as-is.

4. **`grading-path2-offense-specific` section field:** This refinement is categorized under "element" in the coverage checklist, but punishment grading is not strictly an element of the offense. The chapter structure treats grading separately from elements. This is a categorization convention issue — the coverage checklist uses "element / extension / limit" but grading refinements do not map cleanly to that structure. **Recommended fix for future versions:** Add a "grading" category to the coverage checklist section column.

### Fix Applied During Validation
**Issue:** Two refinements (`mens-rea-state-v-white`, `actus-reus-substantial-step-taylor`) were not covered by any cluster. The v4 prompt requires every refinement to appear in at least one cluster.

**Fix:** Added `cluster-specific-intent-limits` combining `mens-rea-specific-intent`, `mens-rea-state-v-white`, `actus-reus-substantial-step-taylor`, and `specific-intent-gap` — all four turn on specific intent requirements and their unexpected implications outside the murder context. Scenario hook drafted. Cluster count increased from 6 to 7. All 23 refinements now covered.

---

## 5. Verification Summary

| Category | Result |
|----------|--------|
| Structural compliance | PASS — all required sections and fields present |
| Content accuracy | PASS — all spot-checked facts, statistics, and holdings confirmed against chapter |
| Completeness | PASS — all chapter doctrines, cases, and slide-practiced concepts covered |
| Three-tier structure | PASS — prima facie / extensions / limits clearly separated |
| Pivot facts | PASS — all 23 refinements have actionable pivot facts |
| Jurisdiction flags | PASS — all 23 refinements flagged |
| Practiced tags | PASS — accurate against slide digest |
| Trap format | PASS — all 23 refinements follow "Students [X] because [Y]" format |
| Cluster coverage | PASS (after fix) — all 23 refinements appear in at least one of 7 clusters |
| Minor issues | 4 noted; cluster gap fixed; 1 schema note for future versions |

**Verdict: MAP APPROVED. Fix applied (cluster coverage). Final state is clean.**
