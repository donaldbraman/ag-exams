# Chapter Map Verification Report: Chapter 3

- Chapter: 3
- Title: What We Punish
- Map file: criminal-law/quiz-system/research/chapter-maps/chapter-03.md
- Verified at: 2026-04-15
- Model: claude-sonnet-4-6

---

## Phase 0: Slide Digest

**Result:** SKIPPED — No slides registered for Chapter 3 (slide_digest.py reports Chapter 3 not in available chapters list: [7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23]). All concepts tagged as unpracticed per pipeline instructions.

---

## Structural Verification

| Check | Result |
|-------|--------|
| Meta fields present (6/6) | PASS |
| Three-tier structure (Prima Facie / Extensions / Limits) | PASS |
| Refinement count (27, target 15-25) | WARN — 27 above target; acceptable for rich theory chapter |
| All keys kebab-case | PASS |
| Trap field present on all refinements | PASS |
| Trap format "Students X because Y" | PASS |
| Pivot fact present on all refinements | PASS |
| Jurisdiction flag present on all refinements | PASS |
| Difficulty present on all refinements | PASS |
| All refinements in at least one cluster | PASS |
| Coverage checklist sync (27/27 rows match refinements) | PASS |
| Source hash present | PASS |
| Cases documented | PASS (11 cases) |
| Clusters present | PASS (6 clusters) |

**Errors: 0**
**Warnings: 1** (refinement count 27 vs. target max 25 — justified by chapter complexity)

---

## Content Verification

### Chapter Coverage Assessment

Chapter 3 is a policy/theory chapter organized around four parts:
- Part I: Core criminal law offenses (consensus + limits of consensus)
- Part II: System-involvement offenses (FTA, license suspension, technical violations, homelessness) + Ferguson case study
- Part III: Contested domains (motivated cognition framework; abortion, firearms, gambling, drugs)
- Part IV: Drug policy as evidence-based case study (MAT, naloxone, LEAD, Oregon)

**Coverage mapping:**

| Chapter Section | Refinements Generated | Coverage |
|----------------|-----------------------|----------|
| Part I: Core offenses | core-offense-consensus, three-offense-families | Adequate — Part I is an orientation, not a doctrinal deep-dive |
| Evidence methodology | bayesian-policy-standard, evidence-grade-hierarchy | Full |
| FTA | fta-reminders-evidence, cash-bail-fta-failure | Full |
| License suspension | debt-suspension-ineffective, debt-suspension-racial-disparity | Full |
| Technical violations | technical-violations-incarceration, hope-program-failure, supervision-violations-scale | Full |
| Homelessness | criminalization-homelessness-ineffective, housing-first-evidence, grants-pass-context | Full |
| Ferguson | ferguson-revenue-machine, ferguson-racial-disparities, keilee-fant-story | Full |
| Motivated cognition | motivated-cognition-mechanism, numeracy-paradox, science-curiosity-remedy | Full |
| Contested domains | cultural-cognition-guns, contested-domains-hollowed-common-ground | Adequate — abortion and gambling are discussed but as illustrations of the same motivated-cognition framework; separate refinements would be redundant |
| Drug policy | criminalization-drug-use-weak, mat-evidence-gap, lead-deflection, oregon-implementation-failure | Full |
| System-involvement scale | system-involvement-scale | Full |

**Notable omissions and justifications:**
- Abortion domain: Not given a separate refinement because the chapter uses abortion as an illustration of motivated cognition and cultural cognition patterns already captured in motivated-cognition-mechanism and contested-domains-hollowed-common-ground. A separate abortion refinement would be repetitive.
- Gambling: Similarly treated as illustrative of the state-complicity/regulatory-capture point; brief in the chapter and well-covered by the contested domains cluster.
- Naloxone and needle exchange: Discussed in Part IV but as supporting evidence for harm reduction approaches captured under mat-evidence-gap and lead-deflection. The chapter does not develop them as independent testable points.

### Three-Tier Adaptation

This chapter required adapting the three-tier structure (prima facie / extensions / limits) because it does not teach traditional doctrine. The adaptation used:
- **Prima Facie Elements:** Core analytical framework (offense category identification, evidence-based analysis, evidence-practice gap assessment, motivated cognition recognition)
- **Liability Extensions:** Secondary analytical tools (motivated cognition as a framework, HCD logic)
- **Liability Limits:** Structural constraints on evidence-based analysis (irreducible moral disagreement, implementation failure)

This adaptation is appropriate and consistent with the v4 prompt's intent (three tiers mapping to how exam answers should be organized).

### Trap Format Compliance

All 27 refinements use the mandatory format: "Students [choose X] because [they confuse Y with Z]." The bracket notation captures both the student error and the underlying confusion, enabling the exam architect to design distractors directly from the trap text.

### Jurisdiction Flag Compliance

All 27 refinements carry jurisdiction flags. Flags used:
- **universal** (14 refinements) — points applicable across jurisdictions
- **majority/minority** (3 refinements) — points where most but not all jurisdictions share a practice
- **split (traditional/MPC)** (1 refinement) — cash bail vs. risk-based assessment
- **federal only** (4 refinements) — *Grants Pass* constitutional holding, HOPE NIJ study, federal MAT restrictions, Oregon state experiment

### Pivot Fact Compliance

All 27 refinements include a pivot fact. This chapter's policy/theory nature required careful pivot fact design: most pivot facts identify the single factual condition whose absence would undermine the chapter's empirical claim (e.g., "if Portugal's decriminalization had been accompanied by reduced treatment investment, use might have increased" — isolating the treatment infrastructure variable).

---

## Cluster Coverage

| Cluster | Refinements | All Covered? |
|---------|------------|--------------|
| cluster-ferguson-system-involvement | 5 | Yes |
| cluster-evidence-policy-gap | 8 | Yes |
| cluster-motivated-cognition-contested-domains | 5 | Yes |
| cluster-drug-policy-evidence | 5 | Yes |
| cluster-homelessness-criminalization | 3 | Yes |
| cluster-core-offense-limits | 3 | Yes |

Every refinement appears in at least one cluster. The overlap between cluster-evidence-policy-gap and cluster-ferguson-system-involvement (debt-suspension-racial-disparity and supervision-violations-scale appear in both) is intentional: Ferguson is a case study in evidence-practice gaps, so the clusters naturally share refinements.

---

## Verification Status

**PASSED** — Zero structural errors. Map is ready for use by exam architect.

The single warning (27 vs. target 25 refinements) reflects the chapter's unusual breadth across four major parts and eleven distinct policy domains. Consolidating to 25 would require merging either the Ferguson analysis or the evidence-methodology framework, both of which serve distinct pedagogical purposes. Recommend accepting 27 for this chapter.
