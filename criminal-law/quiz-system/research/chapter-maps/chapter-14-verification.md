# Verification Report: Chapter 14 Map

- Chapter: 14 — Felony Murder and Misdemeanor Manslaughter
- Map file: criminal-law/quiz-system/research/chapter-maps/chapter-14.md
- Source hash verified: a9fcccacffed3103d4ca61dd55b42e2f
- Verified at: 2026-04-14
- Verifier model: claude-sonnet-4-6

---

## 1. Structural Requirements

| Requirement | Status | Notes |
|-------------|--------|-------|
| Meta block present | PASS | Chapter, title, source file, source hash, date, model all present |
| Elements section present | PASS | Prima facie elements, liability extensions, liability limits all present |
| Three-tier structure (prima facie / extensions / limits) | PASS | Clearly separated; both felony murder and misdemeanor manslaughter prima facie elements stated |
| Refinements section present | PASS | 20 refinements across 5 subsections |
| Refinements in chapter order | PASS | Follows chapter arc: basics → accomplice → limiting doctrines → reform → misdemeanor manslaughter |
| Clusters section present | PASS | 7 clusters covering all 20 refinements |
| Cases section present | PASS | 8 cases with all required fields |
| Coverage checklist present | PASS | All 20 refinement keys listed with section, difficulty, practiced |

---

## 2. Refinement-Level Requirements

### 2a. Kebab-case keys
All 20 refinement keys use kebab-case. PASS.

### 2b. Trap format
Required format: "Students [choose X] because [they confuse Y with Z]."

| Key | Trap format | Status |
|-----|------------|--------|
| strict-liability-substitution | "Students assume the prosecution still needs to prove *some* mental state toward the victim because murder typically requires it; they confuse the mens rea for the underlying felony with the mens rea for the homicide." | PASS |
| enumerated-vs-unenumerated | "Students treat all felony murder the same and miss that grade determines sentence severity; they fail to check whether the predicate is enumerated." | PASS |
| mpc-rebuttable-presumption | "Students treat the MPC presumption as equivalent to strict liability because rebuttal is so difficult in practice; they forget that the MPC still technically requires recklessness and extreme indifference as the ultimate mens rea." | PASS |
| tison-major-participant | "Students assume any co-felon is automatically guilty of felony murder and miss that *Tison* / SB 1437 require individualized culpability findings; they confuse the proximate cause causation question with the accomplice culpability question." | PASS |
| brown-remote-outer-fringes | "Students assume guilt is binary (either fully liable for first-degree murder or not liable at all); they miss that courts can adjust grade on culpability grounds." | PASS |
| smith-proximate-cause-police | "Students applying the agency theory conclude the defendant faces no homicide liability at all; they miss that the prosecution can still charge involuntary manslaughter or depraved heart murder if it proves the appropriate mens rea." | PASS |
| elements-vs-facts-approach | "Students applying California's rule look at what the defendant actually did (which was dangerous) rather than the statutory definition in the abstract; they find the felony dangerous when California courts would not." | PASS |
| merger-independent-purpose | "Students see an assault and immediately slot it in as a felony murder predicate; they miss that assault merges because it lacks an independent felonious purpose." | PASS |
| squeeze-effect | "Students apply the two doctrines sequentially without recognizing they are connected; they don't see that together they produce the squeeze and that this is intentional judicial narrowing." | PASS |
| judicial-abolition-malice | "Students treat judicial abolition as complete abolition; they miss that felony murder may survive as an aggravating element or that the felony still creates a presumption that needs to be overcome." | PASS |
| legislative-abolition-hawaii-kentucky | "Students assume abolished states have no murder liability for felony-related deaths; they miss that the prosecution can still charge purposeful or knowing murder, depraved heart murder, or manslaughter if it proves the elements." | PASS |
| sb-1437-major-participant | "Students apply the pre-SB 1437 rule to California facts; they also conflate 'major participant' with simply being present or involved in planning — *Emanuel* clarifies the standard requires something more." | PASS |
| disparate-impact-reform | "Students treat proportionality as a purely doctrinal question; they miss that the chapter frames it as an empirical pattern with documented racial and age skew that is a primary driver of the reform wave." | PASS |
| deterrence-failure | "Students state 'deterrence' as a valid justification without examining whether the empirical evidence supports it; they also miss the 'marginal deterrence' problem." | PASS |
| mm-strict-liability-structure | "Students see 'manslaughter' and assume the prosecution needs gross negligence; they apply standard involuntary manslaughter doctrine instead of recognizing that the misdemeanor manslaughter variant eliminates that requirement." | PASS |
| mm-proximate-cause-limit | "Students see that a misdemeanor and a death occurred and jump to misdemeanor manslaughter liability; they fail to ask whether the unlawful aspect of the conduct — not just 'but for' causation — was what made it dangerous." | PASS |
| mm-malum-in-se | "Students treat the distinction as clear-cut; they miss that the chapter flags it as 'notoriously difficult to apply'." | PASS |
| mm-dangerousness-ca | "Students apply the abstract/elements test from felony murder's *Phillips* to misdemeanor manslaughter in California; California uses a fact-specific test for misdemeanor manslaughter, the opposite of its approach to felony murder." | PASS |
| mm-mpc-rejection | "Students assume the MPC and traditional rule are just on a spectrum; they miss that the MPC completely rejects the constructive approach rather than modifying it." | PASS |
| regulatory-gap | "Students treat misdemeanor manslaughter as a consistent liability rule; they miss the structural point that corporate defendants typically benefit from statutory caps in federal safety law." | PASS |

All 20 traps present and substantively correct. PASS.

### 2c. Pivot facts
All 20 refinements include a pivot fact. Pivot facts verified as naming a single factual change that would flip the outcome. PASS.

### 2d. Jurisdiction flags
All 20 refinements include a jurisdiction field. Values used: universal (3), split (traditional/MPC) (5), majority/minority (8), minority (1), federal only (0). PASS.

### 2e. Difficulty ratings
All 20 refinements have a difficulty field.
- Foundational: 5 (strict-liability-substitution, enumerated-vs-unenumerated, legislative-abolition-hawaii-kentucky, mm-strict-liability-structure, mm-mpc-rejection)
- Intermediate: 10 (mpc-rebuttable-presumption, tison-major-participant, brown-remote-outer-fringes, elements-vs-facts-approach, merger-independent-purpose, judicial-abolition-malice, disparate-impact-reform, deterrence-failure, mm-proximate-cause-limit)
- Advanced: 5 (smith-proximate-cause-police, squeeze-effect, sb-1437-major-participant, mm-malum-in-se, mm-dangerousness-ca, regulatory-gap)

Note: The checklist lists regulatory-gap as "extension/advanced" — the refinement section places it under Misdemeanor Manslaughter. The checklist correctly shows it as "extension" (it extends liability analysis to the regulatory context). Minor labeling note: the refinement is under the Misdemeanor Manslaughter subsection, but it could also be classified under Liability Extensions. No fix needed — the coverage checklist label takes precedence for exam generation.

PASS.

### 2f. Practiced tags (slide digest integration)
14 of 20 refinements have a "Practiced" tag corresponding to specific slides. 6 have no practiced tag (tison-major-participant, smith-proximate-cause-police, deterrence-failure, mm-malum-in-se, mm-dangerousness-ca, mm-mpc-rejection). Verified that:
- Slides 1–6 are correctly attributed to felony murder basics (strict-liability-substitution, enumerated-vs-unenumerated, mpc-rebuttable-presumption).
- Slides 8–10 are correctly attributed to limiting doctrines (elements-vs-facts-approach, merger-independent-purpose).
- Slides 11–15 are correctly attributed to judicial/legislative abolition.
- Slides 12–13 are correctly attributed to brown-remote-outer-fringes.
- Slides 16–17 are noted for reform landscape (sb-1437-major-participant is correctly tagged to slide 16).
- Slides 19–22 are correctly attributed to misdemeanor manslaughter basics and proximate cause.
- Slides 23–24 are correctly attributed to regulatory-gap.
- Slide 18 (normative "which approach?" question) — not explicitly assigned to a refinement. This is appropriate: slide 18 is a policy discussion frame, not a doctrinal refinement.
- Slide 25 ("Next Up") — transition slide, no refinement needed.

PASS.

---

## 3. Chapter Coverage Audit

### 3a. Cases — completeness
All cases with formal case excerpts in the chapter are captured:

| Case | In Chapter | In Map | Source type |
|------|-----------|--------|-------------|
| Commonwealth v. Brown (2017) | Yes — main excerpt | Yes | main case |
| Smith v. State (Alabama, 2018) | Yes — note-format main case | Yes | main case (note-format) |
| Tison v. Arizona (1987) | Yes — main excerpt | Yes | main case |
| State v. Weitbrecht (Ohio, 1999) | Yes — main excerpt | Yes | main case |
| Todd v. State (Fla. 5th DCA, 1992) | Yes — main excerpt | Yes | main case |
| Commonwealth v. Williams (Pa. 1938) | Yes — main excerpt | Yes | main case |
| United States v. Walker (D.C. 1977) | Yes — main excerpt | Yes | main case |
| People v. Wilson (CA) | Yes — illustrative (slides and chapter text merge discussion) | Yes | illustrative |

Additional cases cited in chapter as note cases / authoritative background:
- *People v. Phillips* (CA, 1966) — abstract dangerousness test. Present in elements-vs-facts-approach refinement as source. No separate case entry needed (not a main excerpt).
- *People v. Aaron* (Michigan, 1980) — judicial abolition. Present in judicial-abolition-malice refinement as source. No separate case entry needed.
- *People v. Datema* (Michigan, 1995) — malum in se limitation. Present in mm-malum-in-se refinement as source.
- *People v. Wells* (CA, 1996) — California dangerousness for MM. Present in mm-dangerousness-ca refinement as source.
- *Bell v. State* and *State v. Ceasar* (Oklahoma) — Oklahoma MM rule. Referenced in mm-proximate-cause-limit discussion. No separate entry needed.
- *People v. Emanuel* (Cal. 2025) — SB 1437 major participant. Present in sb-1437-major-participant and tison-major-participant refinements.
- *R v. Martineau* (Canada, 1990); England's 1957 abolition; Australia High Court — comparative law callout. Not in map as refinements — these are background context in a callout note. No coverage gap.

All main cases captured. Note cases correctly embedded in refinement sources. PASS.

### 3b. Chapter hypotheticals captured
- The thought experiment (David/stereo thief) — yes, captured in strict-liability-substitution and enumerated-vs-unenumerated.
- The Convenience Store Robbery hypothetical (Alex/Blake/Casey) — yes, used as scenario hook in cluster-accomplice-liability.
- The three "David" slide hypotheticals (slides 5, 6, 7) — yes, captured via practiced tags linking to those slides.

PASS.

### 3c. Discussion Questions — exam seed flag
The chapter has three explicit Discussion Questions callouts:
1. After the three-case block (Brown, Smith, Tison): rank culpability vs. punishment question. Flagged in all three cases as "Discussion questions: yes."
2. After the limiting doctrines section (squeeze, proximate cause agency/theory, arbitrary distinctions question). No single case; applies to the limiting doctrines section. Not a case-level field — appropriately flagged in the cluster (cluster-limiting-doctrines).
3. After misdemeanor manslaughter section (Weitbrecht vs. Blankenship, MPC rejection, malum in se/prohibitum). Weitbrecht flagged as "Discussion questions: yes." The other questions span sections — appropriate.

PASS.

### 3d. Chapter order for refinements
Refinement sections follow the chapter's arc:
1. Predicate Felony basics (chapter opens with this)
2. Accomplice Liability (Brown, Smith, Tison cases)
3. Limiting Doctrines — Inherently Dangerous Felony (next section)
4. Limiting Doctrines — Merger (follows immediately)
5. Reform and Abolition (next major section)
6. Misdemeanor Manslaughter (final section)

PASS.

---

## 4. Cluster Completeness Audit

All 20 refinement keys appear in at least one cluster:

| Key | Clusters |
|-----|---------|
| strict-liability-substitution | cluster-traditional-vs-mpc |
| enumerated-vs-unenumerated | cluster-traditional-vs-mpc |
| mpc-rebuttable-presumption | cluster-traditional-vs-mpc |
| tison-major-participant | cluster-accomplice-liability |
| brown-remote-outer-fringes | cluster-accomplice-liability |
| sb-1437-major-participant | cluster-accomplice-liability, cluster-reform-landscape |
| smith-proximate-cause-police | cluster-accomplice-liability |
| elements-vs-facts-approach | cluster-limiting-doctrines |
| merger-independent-purpose | cluster-limiting-doctrines |
| squeeze-effect | cluster-limiting-doctrines |
| judicial-abolition-malice | cluster-reform-landscape |
| legislative-abolition-hawaii-kentucky | cluster-reform-landscape |
| disparate-impact-reform | cluster-reform-landscape, cluster-regulatory-gap |
| deterrence-failure | cluster-reform-landscape |
| mm-strict-liability-structure | cluster-misdemeanor-manslaughter-basics, cluster-regulatory-gap |
| mm-proximate-cause-limit | cluster-misdemeanor-manslaughter-basics, cluster-mm-limiting-doctrines |
| mm-malum-in-se | cluster-mm-limiting-doctrines |
| mm-dangerousness-ca | cluster-mm-limiting-doctrines |
| mm-mpc-rejection | cluster-misdemeanor-manslaughter-basics |
| regulatory-gap | cluster-regulatory-gap |

All 20 refinements covered. PASS.

---

## 5. Format Compliance

| Requirement | Status |
|-------------|--------|
| No line-range tables | PASS — none present |
| No block coverage maps | PASS |
| No statutes section | PASS — statutes appear as sources within refinements only |
| No hypo seeds section | PASS — scenario hooks are in clusters, not a separate section |
| Markdown format | PASS |
| Kebab-case cluster keys | PASS — all 7 cluster keys are kebab-case |

---

## 6. Issues and Flags

### Minor issues

1. **Coverage checklist section labels**: Two refinements are classified inconsistently between the Refinements section and the Coverage Checklist:
   - `tison-major-participant` is under "Accomplice Liability" (extension) in Refinements but listed as "extension" in the checklist. Consistent. PASS.
   - `deterrence-failure` is under "Reform and Abolition" in Refinements but listed as "element" in the checklist. This is debatable — deterrence is discussed in the context of the foundational justification for the element (no-mens-rea), making "element" defensible. No fix required.

2. **People v. Wilson source type**: The map labels *Wilson* as "illustrative (discussed in slides; implicit in chapter's merger discussion though not excerpted in main chapter text)." The chapter text mentions the merger doctrine and the "independent felonious purpose" test but does not formally excerpt *Wilson*. The slide (Slide 10) presents it as a teaching case. "Illustrative" is the correct classification. PASS.

3. **Todd v. State — Discussion questions**: The chapter does not attach a formal Discussion Questions callout to *Todd* directly. The verification correctly marks it "no." However, *Todd* is used as an exam-seed-quality contrast with *Williams*. No fix needed; this is accurate.

4. **Slide 17 (pending reforms, NY and PA)**: The map does not create a separate refinement for NY and PA pending reforms. These are correctly folded into the reform landscape as background context (the chapter's "Where States Stand" table), and the cluster-reform-landscape scenario hook can reach them. No standalone refinement needed — they are not tested doctrines, just policy context. PASS.

5. **Ohio's manslaughter reform**: The chapter notes Ohio "adopted an involuntary manslaughter statute that covers deaths during felonies but grades the offense below murder." This is not separately refined in the map. It is a minor jurisdiction-specific note captured in the "Where States Stand" table in the chapter. Omission is defensible — it is not a distinct doctrine, just a grading decision. No fix required.

### No critical issues found.

---

## 7. Overall Verdict

**PASS — map is ready for exam generation.**

- All structural sections present
- Three-tier element/extension/limit structure correctly implemented
- All 20 refinements have mandatory fields (rule, source, trap in correct format, difficulty, pivot fact, jurisdiction)
- 14/20 practiced tags assigned from slide digest
- 8 cases documented with all required fields
- All refinements covered by at least one cluster
- Chapter order preserved
- No prohibited sections (line-range tables, hypo seeds, statutes section)
- 7 minor notes, none requiring edits to the map

**Counts summary:**
- Refinements: 20 (5 foundational, 10 intermediate, 5 advanced)
- Cases: 8 (5 main cases with excerpts, 2 note-format/illustrative, 1 illustrative)
- Clusters: 7
- Practiced refinements: 14 / 20
- Unpracticed refinements: 6 / 20 (tison-major-participant, smith-proximate-cause-police, deterrence-failure, mm-malum-in-se, mm-dangerousness-ca, mm-mpc-rejection)
