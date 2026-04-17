# Verification Report: Chapter 18 Map

- Chapter: 18 — Accomplice Liability
- Map file: criminal-law/quiz-system/research/chapter-maps/chapter-18.md
- Verified at: 2026-04-14
- Verifier model: claude-sonnet-4-6

---

## 1. Structural Compliance

| Check | Status | Notes |
|-------|--------|-------|
| Has `## Meta` block | PASS | All fields present: chapter, title, source file, source hash, generated at, model |
| Has `## Elements` with three-tier structure | PASS | Prima Facie Elements, Liability Extensions, Liability Limits all present |
| All refinements use kebab-case keys | PASS | Verified: ar-low-threshold, ar-presence-plus, ar-attempt-to-aid, mr-purpose-not-knowledge, mr-underlying-offense, mr-temporal-advance-knowledge, npc-traditional-rule, npc-reform-sb1437, dl-no-crime-principal, dl-personal-defense-no-transfer, dl-justification-vs-excuse, dl-mpc-independent-conviction, ii-gebardi, ii-pino-perez-circumvention, gp-equal-punishment, gp-sentencing-adjustments, gp-accessory-after-fact, tech-concrete-nexus, tech-deliberate-noncooperation, rd-racial-amplification — all kebab-case |
| All refinements include Rule, Source, Difficulty, Pivot fact, Jurisdiction | PASS | Every refinement has all mandatory fields |
| Trap format: "Students [X] because [Y]" | PASS | All traps follow the mandatory format |
| `Practiced` field: only where slide digest confirms | PASS | Practiced fields reference specific slides; gp-accessory-after-fact correctly omits Practiced (not explicitly practiced in slides) |
| `## Clusters` section present | PASS | 7 clusters defined |
| Each cluster has Refinements, Why they cluster, Scenario hook | PASS | All three fields present for each cluster |
| `## Cases` section present | PASS | 12 cases documented |
| Each case has Holding, Reasoning, Facts, Teaches, Source type, Discussion questions | PASS | All fields present for every case |
| `## Coverage Checklist` present as table | PASS | 20 refinement keys listed with section, difficulty, practiced |
| No line-range tables, no statutes section, no hypo seeds | PASS | None present |

---

## 2. Content Accuracy Checks

### Elements Section

**Prima facie elements — actus reus standard:**
Chapter text (p. 3): *State v. Tally* quote: "It is quite sufficient if it facilitated a result that would have transpired without it." Map correctly states no but-for causation required, facilitation sufficient. ✓

**Prima facie elements — purpose requirement:**
Chapter p. 7: "Prosecutors must prove two distinct mental states: first, the accomplice must have the mental state required by the underlying offense; second, in most jurisdictions, the accomplice must *purposefully* aid the principal; mere knowledge that one's actions will facilitate a crime is typically insufficient." Map correctly separates these as two distinct elements. ✓

**Liability Extensions — NPC doctrine:**
Chapter p. 9: "*People v. Luparello*... the defendant enlisted armed associates to extract information from a reluctant witness 'at any cost.'" Map accurately characterizes the traditional NPC doctrine. ✓

**Liability Limits — derivative liability floor:**
Chapter p. 10 (*Hayes*): "Our ruling is that defendant cannot be convicted of burglary and larceny, unless he committed the crimes himself, or was present aiding and abetting another in their commission, that other acting with a felonious intent." Map accurately states the rule. ✓

**Liability Limits — inevitably incident:**
Chapter p. 11: MPC § 2.06(6)(b) quoted; *Gebardi* described accurately. ✓

### Refinements — Accuracy Spot Checks

**ar-low-threshold:** *Tally* holding accurately stated. Map's pivot fact (failed attempt still satisfies MPC attempt-to-aid) is consistent with chapter discussion (p. 2, MPC § 2.06). ✓

**ar-presence-plus / Wilcox:** Map states Wilcox "paid to attend" and published a "laudatory review." Chapter (p. 4): "He paid to go in... out comes his magazine with a most laudatory description." ✓ Map's pivot fact (booing would have negated liability) directly from chapter text: "If he had booed, it might have been some evidence that he was not aiding and abetting." ✓

**mr-purpose-not-knowledge / Gladstone:** Map states no nexus between Gladstone and Kent. Chapter p. 8: "That vital element — a nexus between the accused and the party whom he is charged with aiding and abetting in the commission of a crime — is missing." ✓

**mr-underlying-offense / Wilson:** Map states Wilson lacked "felonious intent" for burglary. Chapter pp. 7–8: Court reversed because the instruction "inferentially placed guilt upon Wilson" without allowing jury to determine whether he acted with felonious intent. ✓

**mr-temporal-advance-knowledge / Rosemond:** Map states "advance knowledge... at a time when he had a meaningful opportunity to walk away." Chapter p. 7: "the defendant must have known a firearm would be used 'at a time when [he] ha[d] a reasonable opportunity to walk away.'" Minor discrepancy: chapter uses "reasonable opportunity," map uses "meaningful opportunity." Both are used in the chapter (p. 7 also uses "meaningful opportunity to disengage"). Both phrasings are accurate. ✓

**dl-no-crime-principal / Hayes:** Map: "Hill entered the store without intent to steal" — Hayes conviction reversed. Chapter pp. 11–12: "Hill did not enter the warehouse with intent to steal... defendant cannot be convicted of burglary and larceny." ✓ Map correctly notes Hayes was guilty of petit larceny for the bacon. ✓

**dl-personal-defense-no-transfer / Vaden:** Map: "undercover agent had a public authority defense... does not transfer to the accomplice." Chapter p. 12: "even if the agent had a public authority justification defense, that defense was personal to the agent and not transferable to the accomplice." ✓

**dl-justification-vs-excuse:** Map source listed as "Slide 18 — slides-only synthesis." This is correct — the explicit justification/excuse table is from the slides, not from the chapter text directly (chapter text discusses the distinction implicitly through Hayes and Vaden). This is a legitimate slide-derived refinement per v4 prompt instructions. ✓

**ii-gebardi:** Map: "when a legislature punishes only one party to a transaction, it implicitly excludes the other." Chapter p. 11: "we cannot infer that the mere acquiescence of the woman transported was intended to be condemned." ✓

**tech-concrete-nexus / Taamneh:** Map: "arm's length, passive, and largely indifferent." Chapter p. 11: Justice Thomas's opinion characterized platforms' relationship with ISIS as exactly those words. ✓

**rd-racial-amplification:** Map: "34x... 2.5 times the already stark 14:1 disparity." Chapter p. 9: "Black people were thirty-four times as likely as white people to be convicted of accomplice-based felony murder — 2.5 times the already stark fourteen-to-one disparity in principal-liability convictions." ✓ Exact figures confirmed.

### Cases Section — Accuracy Spot Checks

**Wilcox v. Jeffery:** Source type listed as "main case." Chapter uses full excerpt format with case title, citation, and extended excerpt — correct. Discussion questions: yes — two questions present. ✓

**State v. Hayes:** Source type "main case." Full excerpt format present. Discussion questions: yes — three questions present. ✓

**Rosemond v. United States:** Source type "note case." Chapter discusses it in note format (p. 7), no full excerpt. ✓

**People v. Gentile:** Source type "note case." Chapter describes it in the NPC reform note (p. 9), no full excerpt. ✓

**Twitter v. Taamneh:** Source type "note case." Discussed in text (p. 11) without full excerpt. Discussion questions: yes — two questions present. ✓

**Gebardi v. United States:** Discussion questions: "no." Chapter has no discussion questions for Gebardi (it is in a note paragraph without a callout box). ✓

**Luparello:** Source type "note case." Not a full excerpt in chapter. Discussion questions: no. No callout box follows Luparello reference. ✓

### Coverage Checklist — Completeness Check

All 20 refinement keys in the Coverage Checklist match refinement keys defined in the Refinements section. ✓

Section assignments verified:
- ar-*, mr-* → element ✓
- npc-traditional-rule → extension (correct: expands liability) ✓
- npc-reform-sb1437, dl-*, ii-*, gp-sentencing-adjustments, gp-accessory-after-fact, rd-* → limit ✓
- gp-equal-punishment → element (the base rule, not a limit) ✓
- tech-concrete-nexus, tech-deliberate-noncooperation → extension (modern doctrine expanding/clarifying reach) — NOTE: these could reasonably be classified as "limit" (they limit liability in the tech context). The map classifies them as extensions. This is a minor judgment call; the assignments are defensible either way.

**Cluster coverage:** All 20 refinement keys appear in at least one cluster. ✓

---

## 3. Issues Requiring Fix

### Minor Issues (non-blocking)

**Issue 1: tech-concrete-nexus and tech-deliberate-noncooperation section classification**
- Map classifies both as `extension` in the Coverage Checklist.
- Argument for `limit`: Taamneh *limits* accomplice liability for platforms; Durov shows a *potential extension* in other jurisdictions.
- Argument for `extension`: Both discuss doctrines at the expanding frontier of accomplice liability doctrine.
- Recommendation: reclassify `tech-concrete-nexus` as `limit` (it articulates a limiting standard) and `tech-deliberate-noncooperation` as `extension` (it describes an expanding theory). This better maps to how a student should organize an exam answer.

**Issue 2: Rosemond "reasonable" vs. "meaningful" opportunity phrasing**
- Map uses "meaningful opportunity to walk away" (the phrasing from p. 7: "meaningful opportunity to disengage").
- Chapter also uses "reasonable opportunity" (p. 7: "a time when [he] ha[d] a reasonable opportunity to walk away").
- Both phrasings appear in the chapter. The map picks the more commonly cited phrase. No substantive error.
- Recommendation: no change needed; both phrasings are in the source text.

**Issue 3: gp-accessory-after-fact practiced field**
- Map correctly omits Practiced for gp-accessory-after-fact. However, Slide 21 ("Synthesis: Managing the Grading Problem") references sentencing adjustments, judicial narrowing, and legislative specification but does not explicitly name accessory-after-the-fact as a separate offense.
- This is correct — the slide does not practice this specific refinement explicitly.
- No change needed. ✓

### Substantive Issues (none found)

No substantive errors in case holdings, case reasoning, rule statements, jurisdiction flags, or pivot facts were identified.

---

## 4. Fix Recommendation

Apply Issue 1: reclassify `tech-concrete-nexus` section from `extension` to `limit` in the Coverage Checklist.

No other fixes required. The map is accurate, complete, and structurally compliant with the v4 prompt.

---

## 5. Summary

| Category | Count | Status |
|----------|-------|--------|
| Structural checks | 12 | All PASS |
| Content accuracy checks | 17 | All PASS |
| Case accuracy checks | 7 | All PASS |
| Substantive errors found | 0 | — |
| Minor issues found | 1 | Apply fix to section classification |
| Fix applied | yes | tech-concrete-nexus → limit |

**Overall verdict: PASS with minor fix applied.**
