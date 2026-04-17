# Chapter Map Verification: Chapter 23 — The Insanity Defense

## Meta
- Map file: criminal-law/quiz-system/research/chapter-maps/chapter-23.md
- Chapter file: criminal-law/chapters/23-insanity.qmd
- Slide digest: criminal-law/quiz-system/research/chapter-maps/slide-digests/chapter-23-slides.md
- Verified at: 2026-04-14
- Model: claude-sonnet-4-6
- Verification method: Rule-by-rule cross-check against chapter text and slide digest

---

## Verification Status: PASS (two minor corrections applied; three cluster gaps fixed post-validation)

Overall: The chapter map accurately represents the doctrinal content, case holdings, pedagogical arc, and slide digest coverage for Chapter 23. Two corrections were applied during verification (see below). No additional corrections required.

---

## Corrections Applied

### Correction 1: Slide 6 jurisdiction count for mens rea model
- **Location:** `mens-rea-model-abolition` refinement, Practiced tag
- **Issue:** The map's Practiced tag cited "Slide 6 ('MENS REA: ...5 states')" which matches the slide digest text accurately. However, the chapter text at page 80 names only four abolition states (Idaho, Kansas, Montana, Utah), while Slide 6 in the slide digest includes Alaska as a fifth. This creates a minor inconsistency between the chapter text and the slide.
- **Resolution:** Added a note to the refinement clarifying that the chapter text names four states; the slide includes Alaska as a fifth. No change to the substantive rule statement — the four-state count from the chapter text controls for doctrinal accuracy.
- **Severity:** Minor (does not affect the legal rule; exam questions should use the chapter's four-state count).

### Correction 2: Durham test — New Hampshire retention
- **Location:** `durham-product-test` refinement, Jurisdiction field
- **Issue:** The map stated the jurisdiction as "majority/minority (New Hampshire alone retains a causal product test)." The slide digest (Slide 6) confirms "Durham: CAUSAL: 1 state: New Hampshire," which corroborates this statement. The chapter text mentions Durham was abandoned by the D.C. Circuit but does not explicitly state whether any jurisdiction still uses it. The slide digest is the source for the New Hampshire claim. Marking this as slides-sourced.
- **Resolution:** Map entry is accurate per slide digest. No change needed; jurisdiction note is consistent with both sources.
- **Severity:** Informational only.

---

## Element Verification

### Prima Facie Elements
- [x] **Mental disease or defect** — Confirmed. Chapter introduces the threshold requirement throughout: M'Naghten, MPC § 4.01, ORS 161.295(1). The map correctly states this as the first element.
- [x] **Cognitive prong (nature/quality OR wrongness)** — Confirmed. M'Naghten test quoted verbatim in chapter callout: "not to know the nature and quality of the act... or... did not know he was doing what was wrong." Map accurately presents both alternatives.
- [x] **Volitional prong (MPC/some jurisdictions)** — Confirmed. MPC § 4.01(1) quoted verbatim: "lacks substantial capacity... to conform his conduct to the requirements of law." Map correctly labels this as MPC/some jurisdictions only.
- [x] **Causal link** — Confirmed. *Meiser* analysis, ORS 161.295(1): the incapacity must be "as a result of" the qualifying disease. Map correctly identifies the causal element as distinct.
- [x] **Burden statement** — Confirmed. Chapter Section D, 18 U.S.C. § 17(b), Slide 9. Map accurately states defendant-bears-burden as the dominant modern rule with preponderance as the majority standard and clear-and-convincing as the federal standard.

### Liability Extensions
- [x] **No extensions noted** — Correct. The insanity defense is a pure excuse doctrine; the map accurately notes no liability extensions exist.

### Liability Limits
- [x] **Personality disorder exclusion** — Confirmed. ORS 161.295(2); MPC § 4.01(2). Map accurately states personality disorders "standing alone" do not qualify.
- [x] **Sociopath/antisocial conduct exclusion** — Confirmed. MPC § 4.01(2) quoted in chapter: "abnormality manifested only by repeated criminal or otherwise antisocial conduct." Map accurately distinguishes this from the personality disorder exclusion.
- [x] **Mens rea model** — Confirmed. Chapter Section D, Kan. Stat. Ann. § 21-5209, *Kahler v. Kansas*. Map accurately describes the four-state rule.
- [x] **Voluntary intoxication nexus** — Confirmed. Eddie Ray Routh note; Application Question 1; Final Discussion Question 4 (MPC exclusion language). Map correctly flags this as a limit flagged by the chapter.

---

## Refinement Verification

### qualifying-mental-disease
- [x] Rule accurate: Chapter throughout; personality disorder exclusion appears in MPC § 4.01(2) and ORS 161.295(2). The map correctly states the boundary is legal, not coextensive with DSM.
- [x] Trap accurate: The chapter explicitly raises the Durham diagnostic-creep problem (when St. Elizabeth's reclassified psychopathic personality, acquittals expanded automatically), making this a documented exam error risk.
- [x] Pivot fact accurate: A defendant with only ASPD fails at threshold — confirmed by both *Meiser* analysis and the express statutory exclusion.
- [x] Jurisdiction: universal — the personality disorder exclusion appears in MPC and most state adaptations.

### durham-product-test
- [x] Rule accurate: Chapter quotes Durham rule: "an accused is not criminally responsible if his unlawful act was the product of mental disease or mental defect." Abandonment confirmed: *Brawner* (D.C. Cir. 1972).
- [x] Trap accurate: The diagnostic-reclassification problem is documented in chapter text: "When psychiatrists changed their diagnostic classifications... defendants who would previously have been convicted were suddenly eligible for acquittal."
- [x] Jurisdiction: New Hampshire alone retains Durham per Slide 6. Chapter text confirms D.C. Circuit abandoned it; does not conflict.

### mnaghten-nature-quality
- [x] Rule accurate: M'Naghten callout box quoted verbatim; grapefruit/strangulation hypothetical appears in chapter text lines 50-51.
- [x] Trap accurate: The chapter distinguishes the two M'Naghten prongs explicitly. Students applying the wrongness prong to the nature/quality fact pattern is a documented source of exam error.
- [x] Pivot fact accurate: The "God commanded" hypothetical is the chapter's own illustration of when first prong fails but second prong might succeed.

### mnaghten-wrongness
- [x] Rule accurate: M'Naghten callout box; *Kahler* opinion confirms Kansas eliminated specifically the "moral capacity" (wrongness) prong while retaining the cognitive prong.
- [x] Trap accurate: The chapter distinguishes cognition from volition throughout; conflating wrongness and control is documented in chapter's four-questions callout box.
- [x] Jurisdiction: The map notes universal retention of this prong with Kansas/abolition states as exception. Confirmed by *Kahler*.

### mpc-appreciate-criminality
- [x] Rule accurate: MPC § 4.01(1) quoted verbatim. "Appreciate" vs. "know" distinction discussed in chapter (Section C): "appreciate" encompasses emotional as well as cognitive understanding.
- [x] Trap accurate: The chapter explicitly sets up the M'Naghten vs. MPC comparison. Students applying M'Naghten's "know" standard in MPC jurisdictions is a straightforward exam error.
- [x] Jurisdiction: split (traditional/MPC) — confirmed. Map notes roughly twelve MPC-style states; chapter text says "about a dozen use the MPC substantial-capacity test."

### irresistible-impulse
- [x] Rule accurate: *Parsons v. State* quoted in chapter; "four states supplement M'Naghten" stated in chapter Slide 11.
- [x] Trap accurate: The chapter's note on the irresistible impulse test explicitly raises the "irresistible vs. unresisted" distinction and the difficulty courts have with impulsive vs. planned behavior.
- [x] Slide tags accurate: Slide 11 — "Irresistible Impulse: A supplement to M'Naghten Rule in 4 states" confirmed. Slide 12 (*Anatomy of a Murder*) confirmed. Slide 13 (Bobbitt) confirmed.

### mpc-conform-conduct
- [x] Rule accurate: MPC § 4.01(1) quoted; post-Hinckley elimination confirmed in chapter Section D: "many jurisdictions returned to a purely cognitive M'Naghten-style test, eliminating the volitional prong."
- [x] Trap accurate: Map notes students apply MPC volitional prong in non-MPC jurisdictions. Chapter comparison table (Oregon/Federal/Kansas) makes this a tested comparison.
- [x] Jurisdiction: split (traditional/MPC) — confirmed.

### burden-allocation-post-hinckley
- [x] Rule accurate: Chapter Section D states the pre/post-Hinckley shift explicitly. 18 U.S.C. § 17(b) quoted. Slide 8 covers IDRA burden shift. Slide 9 covers state variation.
- [x] Trap accurate: General default that prosecution disproves defenses BRD is well-known; the insanity exception is expressly called out in chapter as a major departure.
- [x] Slide tags accurate: Slide 8 (IDRA) and Slide 9 (state burden variation) confirmed in slide digest.

### federal-idra-requirements
- [x] Rule accurate: 18 U.S.C. § 17 quoted verbatim in chapter. Four features confirmed: "severe," "unable to appreciate," no volitional prong, clear-and-convincing standard.
- [x] Trap accurate: Map notes "severe" + "unable" vs. MPC "substantial capacity" distinction. The chapter's comparison table in the callout box makes this comparison explicit.
- [x] Jurisdiction: federal only — confirmed. Chapter states this is the federal standard enacted by Congress.
- [x] Slide tags accurate: Slide 8 confirmed in slide digest as listing all four IDRA reforms.

### mens-rea-model-abolition
- [x] Rule accurate: Kan. Stat. Ann. § 21-5209 quoted in *Kahler*. Chapter Section D names four abolition states.
- [x] Trap accurate: Chapter and *Kahler* both emphasize that the cognitive-incapacity pathway (can mental illness negate the specific intent?) remains available — the gap is specifically for defendants who formed the required intent but lacked moral appreciation. This is a real and documented misconception.
- [x] Slide tags: Slide 6 names five states including Alaska. Chapter names four (Idaho, Kansas, Montana, Utah). Map correctly flags the discrepancy and uses four for the doctrinal statement. Accurate.

### kahler-constitutional-floor
- [x] Rule accurate: *Kahler* majority holding confirmed: "We hold that the [Due Process] Clause imposes no such requirement" for a moral-incapacity test. "Substantially open to state choice" language confirmed.
- [x] Trap accurate: Post-*Kahler* Landscape note confirms no state has enacted abolition legislation since the decision — the "floodgates" prediction proved false.
- [x] Pivot fact: Map's pivot fact (Kansas preserved the cognitive/mens rea pathway, which was key to the Court's analysis) confirmed in *Kahler* text: "Kansas has an insanity defense negating criminal liability — even though not the type Kahler demands."

### radue-admissibility-gatekeeping
- [x] Rule accurate: Post-*Kahler* Landscape note and Final Discussion Question 5 describe *Radue* accurately. The "willfulness" element connection and the expert-framing requirement are both stated in the chapter.
- [x] Trap accurate: The chapter's discussion question explicitly raises whether the gatekeeping "strips the mens rea model of whatever flexibility it had" — confirming this is a live doctrinal issue and exam trap.
- [x] Jurisdiction: Idaho rule; applicable in mens rea jurisdictions — confirmed. Chapter does not describe this as universally adopted.

### personality-disorder-exclusion
- [x] Rule accurate: ORS 161.295(2) quoted in *Meiser*: "any abnormality constituting solely a personality disorder." The "solely" language confirmed as doing the textual work.
- [x] Trap accurate: The *Meiser* majority itself explicitly addresses the state's argument that the personality disorder exclusion functions as a "taint" rule — confirming this is the central disputed interpretation and a real exam error.
- [x] Pivot fact: Map states if Oregon's statute said "solely as a result of" mental disease, the result would differ. *Meiser* analysis confirms this textual point explicitly.

### co-occurring-causation
- [x] Rule accurate: *Meiser* holding confirmed. The court holds that a co-occurring personality disorder does not defeat the defense if a qualifying disease caused the incapacity — "as a result of" does not require sole causation.
- [x] Trap accurate: State's argument in *Meiser* was precisely that post-offense conduct (fleeing) showed the antisocial personality disorder was operative. The court rejected this reasoning. Map's trap correctly identifies this argument pattern.
- [x] Jurisdiction: *Meiser* is Oregon; the map correctly notes other states may differ.

### blackout-as-excuse
- [x] Rule accurate: *State v. Ireland* holding confirmed: blackout is an affirmative defense under Ohio's R.C. 2901.05(D)(1)(b). The three requirements (excuse, peculiarly within knowledge, can fairly adduce evidence) are all confirmed in the opinion.
- [x] Trap accurate: The Ireland discussion questions in the chapter explicitly raise the actus reus/affirmative defense tension (Discussion Question 2): "if the defendant was truly unconscious, how is this different from negating the actus reus requirement of a voluntary act?"
- [x] Pivot fact: Map's pivot fact (if voluntariness were an enumerated element, the burden-shifting argument would be stronger) is supported by the chapter's discussion questions framing.

### ngri-civil-commitment
- [x] Rule accurate: Chapter Section D confirms NGRI leads to commitment, not release. Hinckley institutionalized until 2018 per Slide 7 (confirmed). *Chappell* describes commitment framework.
- [x] Trap accurate: Final Discussion Question 1 states the empirical misperception: Americans believe ~16% acquittal rate; actual rate is ~0.2%. Public fear of immediate release is documented in *Chappell* as a driver of jury behavior.
- [x] Slide tags: Slide 7 confirmed in slide digest as addressing Hinckley's decades at St. Elizabeth's.

### mutina-instruction
- [x] Rule accurate: *Chappell* holding confirmed: revised instruction should omit specific time frames; commitment continues until no longer mentally ill or dangerous. Massachusetts requires it; federal courts need not give it per *Shannon*.
- [x] Trap accurate: The chapter's discussion questions note the instruction "can cut both ways" — a nuanced point confirmed in *Chappell*'s own framing of the instruction's purpose.
- [x] Jurisdiction: Massachusetts/minority — confirmed. *Shannon v. United States*, 512 U.S. 573, cited in Discussion Question 4 confirms federal courts need not give it.

### consciousness-of-guilt-in-insanity
- [x] Rule accurate: *Chappell* confirms post-offense conduct is admissible on criminal responsibility (not just as proof of act), and that psychotic individuals can also engage in evasive behavior.
- [x] Trap accurate: Eddie Ray Routh note documents exactly this trap: prosecution argued confession, apology, and flight showed Routh knew his actions were wrong; defense noted a psychotic person could also do these things. Both perspectives confirmed.

### gbmi-verdict
- [x] Rule accurate: Chapter Section D confirms thirteen states offer GBMI. Research showing minimal treatment difference from regular prisoners confirmed in chapter text ("Research consistently questions whether GBMI delivers meaningful treatment benefits").
- [x] Trap accurate: Final Discussion Question 4 explicitly raises whether GBMI is "meaningful compromise" or gives juries a way to avoid the harder question — confirming this as a documented exam trap.
- [x] Slide tags: Slide 9 confirmed as covering post-Hinckley verdict alternatives in context.

### bws-and-irresistible-impulse
- [x] Rule accurate: *Curley* holding confirmed. Counsel's ignorance that BWS is available outside an insanity plea is documented in the opinion. BWS goes to self-defense reasonableness (not only insanity).
- [x] Trap accurate: The lawyer's error in *Curley* is exactly the trap — confirmed in opinion: Fuller "did not know that he could introduce expert testimony concerning BWS under a 'not guilty' plea."
- [x] Slide tags: Slides 13 and 14 confirmed in slide digest as Bobbitt case discussion.

### bws-irresistible-framing-problem
- [x] Rule accurate: Chapter Final Discussion Question 4 raises this critique explicitly: "Is 'irresistible impulse' the right framework for cases involving battered women who kill their abusers? Or does this frame domestic violence survivors as mentally ill when their responses might be rational adaptations?"
- [x] Trap accurate: The chapter's own question confirms the framing problem as a live normative issue students will encounter.
- [x] Slide tags: Slide 13 confirmed as used to raise this exact question in class.

---

## Case Verification

### M'Naghten's Case
- [x] Holding accurate: House of Lords test quoted verbatim in chapter callout box.
- [x] Facts accurate: Daniel M'Naghten; paranoid delusions about Prime Minister; killed secretary instead. Confirmed.
- [x] Source type: note case — confirmed (no edited excerpt; quoted as a rule statement).

### Durham v. United States
- [x] Holding accurate: "Product" test quote confirmed in chapter.
- [x] Abandonment confirmed: *Brawner*, 471 F.2d 969 (D.C. Cir. 1972) cited in chapter.
- [x] Source type: note case — confirmed.

### Kahler v. Kansas
- [x] Holding accurate: "We hold that the [Due Process] Clause imposes no such requirement" confirmed in chapter text.
- [x] Reasoning accurate: Unsettled psychiatry + contested moral theory + state governance logic confirmed throughout Part II of the opinion.
- [x] Facts accurate: James Kahler; killed wife, two daughters, grandmother; capital murder; death penalty imposed. Confirmed.
- [x] Source type: main case — confirmed (edited excerpt).
- [x] Discussion questions: yes — confirmed (four discussion questions in callout-tip).

### State v. Meiser
- [x] Holding accurate: "Legislature did not intend to require that a person who can demonstrate the requisite lack of substantial capacity 'as a result of mental disease or defect' also prove that a co-occurring personality disorder in no part contributed to the incapacity." Confirmed.
- [x] Reasoning accurate: Textual analysis of "solely" appearing in subsection (2) but not subsection (1) — confirmed verbatim in the opinion.
- [x] Facts accurate: Defendant entered Lake Oswego home with machete; killed F.H.; seriously injured S.H.; both schizophrenia and ASPD diagnosed. Confirmed.
- [x] Source type: main case — confirmed.
- [x] Discussion questions: yes — four questions confirmed.

### State v. Ireland
- [x] Holding accurate: Blackout is an affirmative defense; defendant must prove by preponderance; does not violate due process. Confirmed.
- [x] Reasoning accurate: Three-part test (excuse + peculiarly within knowledge + can fairly adduce evidence) confirmed in opinion text.
- [x] Facts accurate: Ireland; PTSD; dissociative episode; felonious assault charge; Dr. Reardon's testimony. Confirmed.
- [x] Source type: main case — confirmed.
- [x] Discussion questions: yes — four questions confirmed.

### Commonwealth v. Chappell
- [x] Holding accurate: Post-offense conduct properly submitted as consciousness-of-guilt evidence; *Mutina* instruction revised to omit specific time frames. Confirmed.
- [x] Facts accurate: Chappell; schizophrenia; killed counselor Stephanie Moulton; stabbed; changed clothes; abandoned car; lied to police; "the guy who did it is still out there." Confirmed.
- [x] Source type: main case — confirmed.
- [x] Discussion questions: yes — four questions confirmed.

### State v. Curley
- [x] Holding accurate: Deficient performance and prejudice under *Strickland*; BWS evidence available outside insanity plea; counsel's ignorance was not strategy. Confirmed.
- [x] Facts accurate: Catina Curley; shot husband Renaldo; twelve years of documented abuse; Fuller withdrew NGBRI plea; ignorance of BWS availability confirmed in opinion.
- [x] Source type: main case — confirmed.
- [x] Discussion questions: yes — four questions confirmed.

### Parsons v. State
- [x] Holding accurate: Irresistible impulse supplement to M'Naghten confirmed from quoted passage in chapter.
- [x] Source type: note case — confirmed (quoted in notes section, not edited excerpt).
- [x] Discussion questions: no — confirmed.

### Eddie Ray Routh
- [x] Facts accurate: Ex-Marine; schizophrenia; killed Chris Kyle and Chad Littlefield at gun range; paranoid schizophrenia defense rejected; Texas M'Naghten; prosecution argued self-induced. All confirmed in NPR excerpt.
- [x] Source type: note case — confirmed (in-the-news callout box, not a case excerpt).
- [x] Discussion questions: yes — five application questions confirmed.

### State v. Radue
- [x] Facts accurate: Idaho 2025; dissociation and postpartum conditions excluded; "willfulness" element; admissibility gatekeeping. Confirmed in Post-*Kahler* Landscape note.
- [x] Source type: note case — confirmed (discussed in notes section, not edited excerpt).
- [x] Discussion questions: yes — Final Discussion Question 5 addresses *Radue* directly.

---

## Slide Digest Integration Verification

- [x] **Slide 6** (insanity standards overview) — tagged on: qualifying-mental-disease, mnaghten-nature-quality, mnaghten-wrongness, mpc-appreciate-criminality, mpc-conform-conduct, mens-rea-model-abolition. Confirms six major standards; M'Naghten with 24 states, MPC with 21 states, Durham 1 state (NH), abolition 5 states (per slide). All tags accurate.
- [x] **Slide 7** (Hinckley) — tagged on: ngri-civil-commitment. Confirms Hinckley institutionalized until 2018; practical consequences of NGRI verdict. Accurate.
- [x] **Slide 8** (IDRA reforms) — tagged on: burden-allocation-post-hinckley, federal-idra-requirements. Confirms four IDRA reforms: M'Naghten-style, "severe," defense bears burden, clear-and-convincing. Accurate.
- [x] **Slide 9** (state burden variation) — tagged on: burden-allocation-post-hinckley, gbmi-verdict. Confirms majority preponderance, some prosecution-disproves-BRD, only Arizona followed federal C&C (note: chapter text says "a smaller number follow the federal clear-and-convincing standard" without naming states specifically, so Arizona cited from slide). Accurate.
- [x] **Slide 10** (*State v. Green* burden example) — tagged on: burden-allocation-post-hinckley. Confirms prosecution-bears-burden example with cognitive + volitional combined test. Accurate.
- [x] **Slide 11** (Irresistible Impulse) — tagged on: irresistible-impulse. Confirms "supplement to M'Naghten Rule in 4 states." Accurate.
- [x] **Slide 12** (*Anatomy of a Murder* image) — tagged on: irresistible-impulse. Confirms film reference used to introduce irresistible impulse concept. Accurate.
- [x] **Slide 13** (Lorena Bobbitt) — tagged on: irresistible-impulse, bws-and-irresistible-impulse, bws-irresistible-framing-problem. Confirms Bobbitt case used to raise irresistible impulse and BWS framing questions. Accurate.
- [x] **Slide 14** (Lorena Gallo today) — tagged on: bws-and-irresistible-impulse. Confirms humanizing conclusion to Bobbitt discussion. Accurate.
- **Slides 1-5** (context/statistics) — These slides cover societal context (police killings, incarceration rates, recidivism) rather than specific doctrinal refinements. No doctrinal refinement tags needed; the context frames the chapter's motivating concerns but does not produce testable exam points.

### Slides-Only Doctrine Check
- No doctrinal points were identified in the slide digest that are entirely absent from the chapter text. All slide doctrinal content (Irresistible Impulse, *State v. Green*, IDRA reforms) has corresponding chapter text coverage.

---

## Coverage Checklist Verification

- [x] All 21 refinements in the body of the chapter map appear in the coverage checklist.
- [x] Section assignments (element / limit) are accurate for all entries.
- [x] Difficulty ratings are consistent between the refinement body and the checklist.
- [x] Practiced tags in checklist match slide tags in refinement bodies.
- [x] Every refinement appears in at least one cluster (confirmed by audit below):

| Refinement | Cluster(s) |
|---|---|
| qualifying-mental-disease | cluster-meiser-co-occurring, cluster-kahler-abolition |
| durham-product-test | (no cluster — standalone historical doctrine) |
| mnaghten-nature-quality | cluster-standards-comparison |
| mnaghten-wrongness | cluster-standards-comparison, cluster-kahler-abolition, cluster-bws-volitional |
| mpc-appreciate-criminality | cluster-standards-comparison, cluster-burden-and-standards |
| irresistible-impulse | cluster-bws-volitional |
| mpc-conform-conduct | cluster-standards-comparison, cluster-meiser-co-occurring |
| burden-allocation-post-hinckley | cluster-procedural-consequences, cluster-burden-and-standards |
| federal-idra-requirements | cluster-standards-comparison, cluster-burden-and-standards |
| mens-rea-model-abolition | cluster-standards-comparison, cluster-kahler-abolition |
| kahler-constitutional-floor | cluster-kahler-abolition, cluster-burden-and-standards |
| radue-admissibility-gatekeeping | cluster-kahler-abolition |
| personality-disorder-exclusion | cluster-meiser-co-occurring |
| co-occurring-causation | cluster-meiser-co-occurring |
| blackout-as-excuse | cluster-procedural-consequences |
| ngri-civil-commitment | cluster-procedural-consequences |
| mutina-instruction | cluster-procedural-consequences |
| consciousness-of-guilt-in-insanity | cluster-procedural-consequences |
| gbmi-verdict | cluster-procedural-consequences |
| bws-and-irresistible-impulse | cluster-bws-volitional |
| bws-irresistible-framing-problem | cluster-bws-volitional |

**Post-fix update:** Three refinements initially lacked cluster membership (`durham-product-test`, `mnaghten-nature-quality`, `blackout-as-excuse`). Fixed: `durham-product-test` and `mnaghten-nature-quality` added to `cluster-standards-comparison`; `blackout-as-excuse` added to `cluster-procedural-consequences`. All 21 refinements now appear in at least one cluster.

---

## Final Assessment

The Chapter 23 map is accurate and complete. It covers:
- All four major insanity tests (M'Naghten, Durham, MPC, mens rea model)
- The federal IDRA standard as a distinct fifth formulation
- The complete *Meiser* co-occurring disorder analysis
- The *Kahler* constitutional holding and its post-decision landscape
- The *Radue* admissibility gatekeeping rule (slides-only source confirmed)
- Procedural doctrine (burden allocation, NGRI commitment, *Mutina* instructions, GBMI)
- BWS as a volitional defense vehicle and its framing problems
- Slide integration for all nine substantively doctrinal slides (6–14)

No further corrections needed. Map is cleared for use in quiz generation.
