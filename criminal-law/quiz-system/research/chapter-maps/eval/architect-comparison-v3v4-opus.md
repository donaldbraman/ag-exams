# Exam Architect Comparison: Chapter 19 Map v3 vs. v4

**Reviewer role:** Exam architect agent designing multi-issue fact-pattern exam problems
**Maps evaluated:** chapter-19-sonnet-v3.md (v3) vs. chapter-19-sonnet-v4.md (v4)
**Prior review:** architect-review-v3-opus.md
**Source chapter:** 19-conspiracy.qmd
**Date:** 2026-04-14
**Model:** claude-opus-4-6

---

## 1. Which v3 Recommendations Were Addressed?

### Pivot facts
**Fully addressed.** Every v4 refinement includes a "Pivot fact" field. The pivot facts are well-chosen and operationally useful. For example, `mens-rea-purpose-required` gives "If Lauria had charged inflated prices to his prostitute clients (reflecting a premium for criminal dealing), that stake in the venture would support an inference of purpose." That is the exact factual toggle I would use in a fact pattern. The `agreement-bilateral-vs-unilateral` pivot ("if the undercover agent had genuinely intended to participate, the bilateral requirement would be satisfied") correctly identifies the factual hinge. This was my highest-priority format recommendation and v4 delivers it cleanly.

### Cross-refs
**Not addressed.** No refinement in v4 contains a cross-reference to another chapter. The chapter explicitly connects conspiracy to attempt (Ch. 17, substantial step and entrapment), accomplice liability (Ch. 18, Pinkerton rejection links to MPC accomplice doctrine), and the broader enforcement themes running through the casebook. The `system-architecture-manufactured` refinement mentions "the substantial step test for attempt" but does not formally link to Ch. 17. For multi-chapter exam design, I still have to reconstruct these connections from memory.

### Jurisdiction flags
**Fully addressed.** Every v4 refinement includes a "Jurisdiction" field. The values are well-calibrated: `universal` for doctrines like agreement-inference and Lauria; `split (traditional/MPC)` for bilateral-vs-unilateral, Pinkerton, and withdrawal; `federal law` for the system-architecture refinements. This immediately tells me which refinements generate jurisdiction-comparison questions and which do not.

### Coverage checklist
**Fully addressed.** V4 includes a coverage checklist appendix with key, section type, difficulty, and a "Practiced" column showing slide references. This is exactly the flat-list format I requested. The addition of slide-reference data in the checklist is a bonus -- I can see at a glance which refinements students have encountered in lecture and which are reading-only.

### Composes-with
**Not addressed.** No refinement includes a "Composes with" field listing which other refinements naturally co-occur in a fact pattern. The clusters partially serve this function, but the clusters are coarser -- they group 3-4 refinements, whereas composes-with would capture pairwise relationships (e.g., `pinkerton-vicarious-scope` composes with `scope-single-vs-multiple` because the scope question is a prerequisite for Pinkerton analysis). This remains a gap for rapid fact-pattern assembly.

### Split pinkerton-quantity-sentencing
**Fully addressed.** V3's single `pinkerton-quantity-sentencing` refinement, which conflated quantity attribution, mandatory minimums, the girlfriend problem, and the cooperation escape valve, has been split. V4 has `pinkerton-girlfriend-problem` (quantity attribution + mandatory minimums + peripheral-participant sentencing) as a distinct refinement separate from `pinkerton-vicarious-scope` (the core Pinkerton rule and foreseeability). The girlfriend problem is still somewhat compound -- it covers both the quantity-attribution mechanism and the cooperation escape valve -- but the split is a meaningful improvement. A rubric can now separately grade "does the student identify Pinkerton's quantity-attribution effect" and "does the student identify the foreseeability limit on Pinkerton."

### Exam blueprint
**Not addressed.** V4 has no introductory paragraph summarizing total refinement count, difficulty distribution, highest-value clusters, or mandatory-test doctrines. The coverage checklist partially substitutes (I can count and scan), but the quick-orientation paragraph I requested is absent.

### Score summary

| Recommendation | Status |
|----------------|--------|
| Pivot facts | Fully addressed |
| Cross-refs | Not addressed |
| Jurisdiction flags | Fully addressed |
| Coverage checklist | Fully addressed |
| Composes-with | Not addressed |
| Split pinkerton-quantity-sentencing | Fully addressed |
| Exam blueprint | Not addressed |

**4 of 7 recommendations fully addressed; 0 partially addressed; 3 not addressed.**

---

## 2. Three-Tier Structure (Elements / Extensions / Limits)

V3 used a five-element flat structure: Agreement, Mens Rea, Scope, Vicarious Liability (Pinkerton), Structural Limits. V4 restructures into three tiers: Prima Facie Elements (agreement, mens rea, overt act), Liability Extensions (Pinkerton), and Liability Limits (Wharton's, Gebardi, withdrawal, MPC merger, buyer-seller exception).

**The three-tier structure is a clear improvement for exam design.** Here is why:

1. **It mirrors analytical sequence.** When grading an exam, I check: (a) are the prima facie elements met? (b) does Pinkerton extend liability? (c) do any limits apply? The three tiers correspond to this three-step rubric. V3's five elements were sound, but the analytical hierarchy between "scope" and "structural limits" was ambiguous -- both involve questions about whether liability extends, but at different stages of analysis. V4 makes the hierarchy explicit.

2. **Overt act is promoted to element status.** V3 treated overt act as a refinement under "Agreement." V4 treats it as its own prima facie element. This is correct for exam purposes: the overt act question is analytically distinct from the agreement question, and students who skip it lose points. Giving it element-level visibility ensures rubrics include it.

3. **Limits are consolidated.** V3 scattered the limit doctrines: Wharton's and Gebardi were Element 5, but withdrawal was missing entirely, merger was absent, and the buyer-seller exception was filed under Agreement. V4 collects all five limiting doctrines under "Liability Limits." This is the right grouping for exam design because all five function the same way: they are categorical bars or defenses that a student should check after establishing prima facie elements and extensions. Having them in one section means I can write a checklist-style rubric item: "Did the student identify and analyze applicable liability limits?"

4. **One minor concern.** Buyer-seller exception appears in v4 both as a refinement under Agreement (`agreement-buyer-seller`) and as a Liability Limit in the Elements section. This dual listing is slightly confusing. It is defensible -- the buyer-seller exception is both a limit on when an agreement exists and a categorical bar on conspiracy charges -- but for rubric clarity, I would want it in one place. On balance, the Agreement placement is more natural because the buyer-seller question is really "was there an agreement to distribute, or just a sale?"

**Verdict: The three-tier structure is better. It maps to how I build rubrics and how students should organize answers.**

---

## 3. Slide Integration

V4 incorporated a Gemini-generated slide digest to tag which refinements were "practiced" in lecture slides and to add slides-only doctrines.

### What it added

1. **"Practiced" tags on refinements.** Eleven of twenty refinements have slide references (e.g., "Practiced: Slides 12-20" on `agreement-explicit-vs-inferred`). This is genuinely useful. When designing an exam, I want to weight tested concepts toward material students have seen in both readings and lecture. The "Practiced" field lets me distinguish between reinforced concepts (reading + lecture) and reading-only concepts. For difficulty calibration, a concept that was practiced in slides is fairer to test at a lower difficulty than one that appeared only in reading.

2. **Withdrawal refinement.** This was the highest-priority missing doctrine in my v3 review. V4 adds `withdrawal-requirements` with a clear two-prong rule (affirmative steps + communication), the correct traditional/MPC split, and a useful pivot fact. The slide tags indicate this was covered in Slides 9-11 with a "Brad-gets-cold-feet" hypothetical. The slide digest may have surfaced this doctrine (it appears in the chapter's comparison table but was not prominent enough for v3 to capture it). Regardless of the cause, having withdrawal in the map is a significant improvement.

3. **MPC merger.** Also missing from v3, now present as Liability Limit #4. The rule is stated concisely: "Under the MPC, conspiracy merges with the completed offense so that a defendant cannot be punished for both the conspiracy and the substantive crime." This enables the jurisdiction-comparison question I described in the v3 review (traditional: conspiracy + substantive offense; MPC: only one).

4. **System architecture refinements.** V4 adds two policy-layer refinements -- `system-architecture-manufactured` (manufactured conspiracies) and `system-architecture-racial-disparities` (enforcement asymmetry). These capture the chapter's final major section, which v3 largely ignored. The `system-architecture-manufactured` refinement correctly identifies the doctrinal interaction (unilateral rule + substantial step + forfeiture) and has a strong pivot fact (removing forfeiture incentive eliminates the financial driver even if doctrine remains unchanged). The racial-disparities refinement captures the Purdue comparison. These are testable as policy questions.

### What is noise

1. **Some slide references are thin.** `agreement-interstate-mutual-awareness` is tagged "Slide 28 (movie theater image as case introduction)." A single image slide is not meaningful "practice." The tag suggests the concept was briefly introduced visually but not worked through. Tagging this the same way as `agreement-explicit-vs-inferred` (Slides 12-20, extended treatment) overstates the lecture coverage. A binary "practiced/not practiced" flag would be more honest than the current format, which implies equivalent coverage regardless of depth.

2. **The Lauria inferences refinement is new and partially redundant.** V3 had separate `purpose-not-knowledge` and `aggravated-crime-inference` refinements. V4 collapses these into `mens-rea-purpose-required` (the Lauria holding) and `mens-rea-lauria-inferences` (the three circumstances: stake, no legitimate use, aggravated crime). The v4 version is arguably better organized -- it separates the core rule from the inferential tools -- but the "no legitimate use" factor was not a v3 refinement and its addition comes from the slide digest's emphasis on the Silk Road comparison (Slide 25). This is useful new content, not noise: a fact pattern where the defendant's product has no legitimate use triggers a different Lauria analysis than one where the product is dual-use.

### Verdict: Slide integration added real value.
The withdrawal and merger additions alone justify the slide-integration step. The practiced tags are useful for difficulty calibration. The noise level is low -- one or two thin slide references, easily corrected.

---

## 4. New Gaps or Regressions

### Regressions from v3

1. **Refinement key naming changed.** V3 used concise, memorable keys: `purpose-not-knowledge`, `aggravated-crime-inference`, `alvarez-nod`, `buyer-seller-exception`. V4 uses longer, more systematic keys: `mens-rea-purpose-required`, `mens-rea-lauria-inferences`, `agreement-alvarez-minimal-conduct`, `agreement-buyer-seller`. The v4 naming is more self-documenting (you can tell the section from the prefix), but the v3 keys were easier to remember and faster to type when building rubrics. This is a mild regression -- systematic naming is probably better for machine processing, but worse for human recall.

2. **The Lauria suppliers cluster was restructured.** V3 had a dedicated `cluster-lauria-suppliers` with a payment-processor scenario hook (gambling operation, standard fees, money laundering financing a violent cartel). V4's `cluster-mens-rea-supplier` covers similar ground but with a warehouse-operator scenario. The v3 scenario was stronger because it layered three distinct Lauria analyses: (a) knowledge vs. purpose for the gambling itself, (b) the aggravated-crime inference via the violent cartel, and (c) the buyer-seller question about whether a payment processor is a supplier or a coconspirator. V4's warehouse-operator scenario triggers (a) and (b) but not (c). The payment-processor hook was a better exam question.

3. **The undercover-operations cluster lost pinkerton-quantity-sentencing.** V3's `cluster-undercover-operations` included `bilateral-vs-unilateral`, `pinkerton-quantity-sentencing`, and `buyer-seller-exception` -- a tight cluster that forced students to analyze the sting scenario from agreement through sentencing consequences. V4's `cluster-undercover-agent` replaces the Pinkerton/quantity component with `withdrawal-requirements` and `system-architecture-manufactured`. The new cluster is more policy-oriented and less black-letter. For a doctrinally focused exam, the v3 cluster was more useful; for a policy essay, the v4 cluster is better. This is a trade-off, not a pure regression.

### New gaps

1. **Corporate conspiracy still absent as a refinement.** V4 addresses the Purdue material through `system-architecture-racial-disparities`, which discusses enforcement asymmetry between corporate and street-level defendants. But there is no refinement on the intracorporate conspiracy doctrine itself (can a corporation conspire with its own employees?). The chapter raises this question implicitly. For a full-coverage exam, I would want a refinement on corporate conspiracy.

2. **Procedural consequences remain under-developed.** V3 and v4 both mention coconspirator hearsay, joint trial, and relaxed venue in passing (within `scope-single-vs-multiple`), but neither gives the procedural consequences their own refinement. As I noted in the v3 review, these are deeply testable: a fact pattern can ask whether a coconspirator's statement is admissible, whether severance should be granted, or whether venue is proper. This gap persists.

3. **Source type tags on cases.** V4 adds "Source type" and "Discussion questions" fields to the Cases section. This was one of my v3 format recommendations (item 7). V4 delivers it: cases are tagged as "main case," "note case," or "note case (illustrative)," and discussion-question availability is flagged. This is not a gap -- it is an improvement I should acknowledge. It helps me know which cases students read closely (main cases with discussion questions) versus encountered briefly (note cases without).

### Net assessment: No significant regressions. Two persistent gaps (corporate conspiracy, procedural consequences). Several improvements.

---

## 5. Bottom Line: v3 or v4?

**V4 is the better map. I would use v4.**

The reasons are cumulative:

1. **V4 has 20 refinements to v3's 17.** The three additions -- withdrawal, merger (embedded in the Limits section), and the two system-architecture refinements -- fill genuine gaps. Withdrawal alone was my single most important missing-doctrine complaint about v3.

2. **V4 has pivot facts and jurisdiction flags on every refinement.** These are the two fields that most directly accelerate fact-pattern construction. With v3, I had to infer the pivoting detail and look up jurisdiction splits from memory. With v4, I can scan the pivot facts to find ambiguous-fact-pattern opportunities and filter by jurisdiction to design comparison questions. This is a substantial time savings.

3. **The three-tier structure is superior for rubric construction.** V3's five-element flat organization was sound, but v4's elements/extensions/limits hierarchy maps directly to how an exam answer should be organized: establish prima facie case, check for extensions, check for limits.

4. **The coverage checklist enables quick gap-checking.** After writing a fact pattern, I can scan the checklist to verify coverage. V3 required reading through five sections.

5. **Slide-practiced tags improve difficulty calibration.** I can weight exam questions toward material that was reinforced in lecture, which is fairer to students.

6. **The policy-layer refinements expand the question space.** V3 was almost exclusively black-letter. V4 adds `system-architecture-manufactured` and `system-architecture-racial-disparities`, which let me design policy-essay questions that test the chapter's final major section. A comprehensive conspiracy exam should include at least one policy question.

**What v3 does better:**

- Concise refinement keys (easier to remember for rubric-building)
- The Lauria-suppliers cluster scenario hook (payment processor) was stronger than v4's warehouse operator
- The undercover-operations cluster was tighter for black-letter testing

**What remains missing from both:**

- Cross-chapter references (Ch. 17 attempt/entrapment, Ch. 18 accomplice liability)
- Composes-with fields for pairwise refinement relationships
- Exam blueprint paragraph
- Corporate conspiracy as a standalone refinement
- Procedural consequences as a standalone refinement

**If I could have one more revision,** I would add cross-chapter references and the exam blueprint. The composes-with field is lower priority now that the clusters exist and the coverage checklist enables quick scanning. The remaining gaps are manageable -- I can fill them from the source chapter. But v4 as it stands gives me approximately 90-92% of what I need to design a multi-issue conspiracy exam, up from the 85-90% I estimated for v3.

---

## Summary Table

| Dimension | v3 | v4 | Winner |
|-----------|-----|-----|--------|
| Refinement count | 17 | 20 | v4 |
| Withdrawal coverage | absent | present | v4 |
| Merger coverage | absent | present (in Limits) | v4 |
| Pivot facts | absent | present on all | v4 |
| Jurisdiction flags | absent | present on all | v4 |
| Coverage checklist | absent | present with slide tags | v4 |
| Cross-chapter refs | absent | absent | tie |
| Composes-with | absent | absent | tie |
| Exam blueprint | absent | absent | tie |
| Element structure | five-element flat | three-tier hierarchy | v4 |
| Refinement key naming | concise, memorable | systematic, longer | v3 (minor) |
| Cluster quality | 6 clusters, strong hooks | 6 clusters, mixed hooks | v3 (minor) |
| Policy coverage | minimal | two refinements | v4 |
| Case metadata | basic | source type + discussion flags | v4 |
| Slide integration | none | practiced tags on 11/20 | v4 |
| **Overall** | **85-90%** | **90-92%** | **v4** |
