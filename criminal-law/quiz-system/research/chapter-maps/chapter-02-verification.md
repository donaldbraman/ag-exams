# Verification Report: Chapter 02 Map

## Meta
- Map file: criminal-law/quiz-system/research/chapter-maps/chapter-02.md
- Chapter file: criminal-law/chapters/02-why-how-punish.qmd
- Verified at: 2026-04-15
- Verifier model: claude-sonnet-4-6

## Summary

**Status: PASS with minor notes**

All 21 refinements and 12 cases were verified against the source chapter. No HALLUCINATIONs or ERRORs found. Two minor notes below.

---

## Refinement Verification

| Key | Verdict | Notes |
|-----|---------|-------|
| deterrence-rational-actor | PASS | Bentham text supports; rational actor assumption stated at line 17 |
| deterrence-four-limits | PASS | Exact four conditions stated in Bentham excerpt, lines 32-33 |
| deterrence-specific-general-incapacitation | PASS | Three modes named explicitly in chapter note, lines 37-38 |
| retribution-categorical-imperative | PASS | Kant excerpt lines 48-54; medical experiment and dissolving society hypotheticals confirmed lines 54, 59 |
| retribution-proportionality | PASS | Chapter note lines 61-62 explicitly states proportionality requirement |
| expression-insult-message | PASS | Hampton 1992 excerpt lines 72-79; Murphy quote confirmed |
| expression-proportionality-value | PASS | Hampton 1988 excerpt lines 86-91 |
| expression-community-signal | PASS | Chapter note lines 97-98 |
| rehabilitation-martinson-nothing-works | PASS | Lines 103-104; 1974 date, 231 studies confirmed |
| rehabilitation-modern-evidence | PASS | Lines 105-107; RAND 43%, Norway NBER, Canadian 19%, Lancet therapeutic community — all confirmed |
| accountability-passive-vs-active | PASS | Sered excerpt lines 214-226 |
| accountability-community-demand | PASS | Braman excerpt lines 163-191; Londa's case confirmed |
| accountability-extends-all-three | PASS | Braman lines 180-191; three subsections (fairness, welfare, expressive) confirmed |
| restorative-justice-theory | PASS | Lines 232-239 |
| restorative-justice-dv-rct | PASS | Lines 241-251; 53% fewer arrests, 52% lower severity, 24-month follow-up, 222 offenders confirmed |
| restorative-justice-expressive-overdetermination | PASS | Line 239; "expressive overdetermination" exact phrase confirmed |
| corporate-theory-mismatch | PASS | Lines 285-286, 299-300; Braman & Gabaldon confirmed |
| corporate-charter-restructuring | PASS | Lines 302-305, 308-327; Purdue restructuring confirmed |
| legitimacy-equal-application | PASS | Lines 346-350 |
| legitimacy-attention-economy | PASS | Lines 358-365; 20% spread figure, 4.8× out-group hostility confirmed |
| legitimacy-mass-incarceration-scale | PASS | Lines 125-128; 20% of world's prisoners, 2 million incarcerated, 1 in 3 Black boys confirmed; Natapoff 75% figure confirmed line 142 |

---

## Case Verification

| Case | Verdict | Notes |
|------|---------|-------|
| Bentham — Rationale of Punishment (1830) | PASS | Lines 19-26; source title confirmed |
| Bentham — Introduction to Principles (IPML) | PASS | Lines 27-33 |
| Kant — Philosophy of Law (Hastie trans.) | PASS | Lines 43-55; 194-98 citation confirmed |
| Hampton — Expressive Theory of Retribution (1992) | PASS | Lines 67-79; Murphy quote included |
| Hampton — The Retributive Idea (1988) | PASS | Lines 81-91 |
| Natapoff — Punishment Without Crime (2018) | PASS | Lines 131-143 |
| Braman — Punishment and Accountability (2006) | PASS | Lines 159-191; UCLA L. Rev. 53 confirmed |
| Sered — Until We Reckon (2019) | PASS | Lines 193-227 |
| Mills et al. — DV RCT, Nature Hum. Behav. (2019) | PASS | Lines 243-251 |
| Braman & Gabaldon — Charter for Justice (2025) | PASS | Lines 289-305; 59 U.C. Davis L. Rev. 429 confirmed |
| In the News: Purdue Pharma (2025) | PASS | Lines 307-327; all key facts confirmed (2007 settlement, 2020 plea, 2025 restructuring, $7.4B, Knoa Pharma, Sackler $10.7B withdrawal) |
| In the News: Officer Crews / Ashley Hall (2021) | PASS | Lines 257-271; Ladue Police Department, Schnucks grocery, $2M settlement, Seema Gajwani confirmed |

---

## Issues Found

**None — no HALLUCINATIONs, ERRORs, DUPLICATEs, or MISSINGs.**

### Minor Notes (not requiring fixes)

1. **Rehabilitation chapter** — The map's `rehabilitation-martinson-nothing-works` refinement characterizes Martinson's finding as "widely interpreted as concluding rehabilitation does not reduce recidivism." The chapter says it "was widely interpreted as concluding that 'nothing works.'" These are consistent; no change needed.

2. **Braman & Gabaldon death toll figures** — The map's corporate case entry uses bracketed numbers "[1,300]" and "[nearly 24,000]" as in the original excerpt (lines 296-297). These are confirmed as appearing in the source text, which itself uses brackets to indicate updated figures. The map correctly reproduces the bracketed notation in the case holding.

---

## Structural Checks

- [x] File exists at correct path
- [x] Meta section complete
- [x] Three-tier structure present (Prima Facie Elements / Liability Extensions / Liability Limits)
- [x] Refinements in chapter order: Part I (deterrence → retribution → expressive → rehabilitation → accountability → restorative) → Part II (corporate) → Part III (legitimacy)
- [x] All refinements have: Rule, Source, Trap, Difficulty, Pivot fact, Jurisdiction
- [x] Trap format correct ("Students [choose X] because [they confuse Y with Z]") for all 21 refinements
- [x] Jurisdiction flags present for all 21 refinements
- [x] Pivot facts present for all 21 refinements
- [x] Refinement count: 21 (within 15-25 target range)
- [x] All refinements appear in at least one cluster (7 clusters covering all 21)
- [x] Cases section includes all major sources
- [x] Coverage checklist present with all 21 refinements
- [x] No "Practiced" tags (correct — no slides for chapter 2)

## Verdict

**PASS. No Phase 3 fixes required.**
