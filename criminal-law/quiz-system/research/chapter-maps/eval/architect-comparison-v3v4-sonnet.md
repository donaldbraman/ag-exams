# Architect Comparison: Chapter 19 Map v3 vs. v4

**Reviewer role:** Exam architect
**Map files:** `chapter-19-sonnet-v3.md` (v3), `chapter-19-sonnet-v4.md` (v4)
**Prior review:** `architect-review-v3-sonnet.md`
**Review date:** 2026-04-14

---

## 1. Which v3 Recommendations Were Addressed?

### Recommendation 1: Separate prima facie elements from consequential doctrines

**Fully addressed.**

v3 had five numbered "elements" that mixed prima facie requirements (agreement, mens rea, overt act) with post-conviction doctrines (Pinkerton vicarious liability) and limiting rules (structural limits). v4 replaces this with a three-tier structure: **Prima Facie Elements** (agreement, mens rea, overt act), **Liability Extensions** (Pinkerton), and **Liability Limits** (Wharton's Rule, Gebardi, withdrawal, MPC merger, buyer-seller exception).

This is the most important structural improvement in v4. A student or rubric keyed to v3 might treat Pinkerton as something the prosecution must prove alongside agreement. That error is now impossible with v4's structure.

### Recommendation 2: Add jurisdiction flags to each refinement

**Fully addressed.**

Every refinement in v4 includes a `Jurisdiction:` field. Coverage is accurate and appropriately granular: `universal`, `split (traditional/MPC)`, `federal law`, `majority`, or `majority (federal and most traditional states); MPC and most reformed codes reject it`. This is one of v4's most practically useful additions for exam design — a question writer can immediately see which refinements require a jurisdictional choice and which apply everywhere.

### Recommendation 3: Add a Connections field

**Not addressed.**

v4 still has no `Connections:` field linking refinements that commonly co-appear in exam questions. This was the most actionable format addition recommended — a question writer designing a single multi-issue question needs to know at a glance that `pinkerton-vicarious-scope` + `pinkerton-mpc-rejection` + `pinkerton-girlfriend-problem` + `scope-single-vs-multiple` cluster together. v4's cluster section provides partial coverage, but clusters are scenario-level groupings, not per-refinement co-appearance flags. The Connections field was intended to operate at the refinement level and is still absent.

### Recommendation 4: Add a fact-pattern trigger to each refinement

**Substantially addressed — via Pivot Fact.**

The recommendation called for a one-line trigger describing the specific fact pattern feature that puts the issue in play. v4 implements this as a `Pivot fact:` field. The pivot fact is sometimes better than a trigger and sometimes worse. For `agreement-bilateral-vs-unilateral`, the pivot fact ("if the undercover agent had genuinely intended to participate, the bilateral requirement would be satisfied") is a counterfactual that clarifies the holding rather than a trigger. The trigger the review requested was: "Trigger: defendant agrees with someone who turns out to be an undercover officer or informant." That is what a question writer needs to know to put the issue in play. Pivot facts are analytically useful but not identical to triggers. This is a 75% solution.

### Recommendation 5: Consolidate overlapping refinements (inference-limits + wheel-and-spoke; cluster-mens-rea-purpose + cluster-lauria-suppliers)

**Partially addressed.**

The `inference-limits` + `wheel-and-spoke` overlap is fixed. v3 had two separate refinements making the same point about *Kotteakos*; v4 consolidates to a single `agreement-wheel-without-rim` refinement covering both the structural rim/spoke test and the general inference principle. Good.

The cluster-level overlap between `cluster-mens-rea-purpose` and `cluster-lauria-suppliers` is partially fixed. v4 creates a single `cluster-mens-rea-supplier` that integrates *Lauria* purpose doctrine with *Pond* element-specific intent. This is cleaner. However, `agreement-buyer-seller` still appears in `cluster-structural-limits` as a categorical bar rather than with the Lauria supplier analysis where it arguably belongs — the buyer-seller exception is, substantively, an application of the purpose-not-knowledge rule to the drug sale context. This placement confusion is a minor residual issue.

### Recommendation 6: Add a Withdrawal section

**Fully addressed.**

v4 adds `withdrawal-requirements` as a standalone refinement under Liability Limits, with accurate rule statement (affirmative steps + communication, or disclosure to law enforcement), correct jurisdiction flag (split: traditional vs. MPC), and a pivot fact distinguishing the two approaches. The refinement draws on both the *Pinkerton* text ("no evidence of affirmative action") and the slide content. This was the second most significant gap in v3 and is now well-covered.

The Liability Limits section also adds **MPC merger** (cumulative punishment vs. merger), which was identified as the most significant gap in the v3 review. It appears as a one-line element summary rather than a full refinement, which is undersized given that merger is a routine bar exam issue. But its presence is a clear improvement over v3's omission.

### Recommendation 7: Flag cases with chapter discussion questions

**Fully addressed.**

v4 adds a `Discussion questions: yes/no` field to every case entry. The flags are accurate: *Kotteakos*, *Pond*, *Lauria*, and *Pinkerton* are all correctly flagged as having discussion questions, consistent with the source chapter. This is a simple but high-value addition — these are the professor's exam seeds and the flags make that explicit.

---

## 2. Did the Three-Tier Structure Improve the Map?

Yes, unambiguously. The three-tier structure (prima facie elements → liability extensions → liability limits) solves the conceptual problem that afflicted v3's five-element flat structure.

In v3, numbering Pinkerton as Element 4 implies it is something the prosecution proves as part of the prima facie case, alongside agreement and mens rea. It is not — it is a consequential doctrine that applies once the conspiracy is established. A student building an IRAC analysis from v3's element list would place Pinkerton in the wrong analytical slot.

Similarly, v3 called structural limits "Element 5" when they are defenses or categorical bars, not prosecution burdens. Placing Wharton's Rule and Gebardi as elements in the prima facie case is analytically backwards — they are reasons the prima facie case does not lead to liability.

v4's three-tier structure corrects both errors and creates a map whose architecture mirrors how a lawyer actually analyzes a conspiracy problem: prove the prima facie case first, then determine whether extensions apply (who else is liable), then check whether limits defeat the charge or narrow the punishment.

The only cost of the new structure is that it disperses content across more sections, making the map somewhat longer to navigate. This is a minor readability tradeoff for a significant analytical improvement.

---

## 3. Did Slide Integration Add Value?

Mostly yes, with one important qualification.

**Value added:**

The `Practiced:` field and slide references in v4 add concrete, useful information for exam design. Knowing that `withdrawal-requirements` was covered extensively in slides 9–11 (Brad-gets-cold-feet hypothetical, two-prong test, "withdrawal: allowed but demanding") confirms that withdrawal is a live exam issue — the professor allocated dedicated slide time to it. Similarly, knowing that `agreement-explicit-vs-inferred` received slides 12–20, including the Dan Markel case study, flags it as a chapter centerpiece worth significant exam weight.

The coverage checklist at the end is a direct benefit of slide integration. It gives a quick view of which refinements were classroom-practiced (and thus exam-likely) and which were reading-only. The three unpracticed policy refinements (`system-architecture-manufactured` and `system-architecture-racial-disparities`) are correctly marked — slide 39–40 covered them, so they are practiced, though the coverage checklist correctly notes that `system-architecture-racial-disparities` lacks a Practiced entry. That appears to be an oversight in the checklist rather than a substantive error.

The new `system-architecture-manufactured` and `system-architecture-racial-disparities` refinements appear to derive substantially from slide content (Slides 39–40 are explicitly cited). These are genuine additions — v3 mentioned that the systemic critique was a gap, and v4 fills it with two refinements that are more analytically developed than what v3 provided.

The withdrawal section, which was the most significant v3 gap, is confirmed by slide content as practiced material. Without slide integration, a map generator working only from the chapter text might have missed the three-slide sequence (Slides 9–11) that establishes withdrawal as a class priority.

**Qualification — noise from slide-only doctrines:**

The buyer-seller exception now appears in the Liability Limits section of the Elements tier, likely because the slides treated it there. But doctrinally it belongs with the mens rea / purpose-not-knowledge analysis: the reason a buyer-seller relationship is not a conspiracy is that the parties lack a shared *purpose* to further distribution, not that the agreement is categorically barred by a structural rule like Wharton's Rule. Placing it under Liability Limits alongside Wharton's Rule and Gebardi slightly misrepresents the doctrine's analytical location.

Overall, slide integration produced more signal than noise. The withdrawal section alone justifies it.

---

## 4. New Gaps or Regressions?

**What v4 lost from v3:**

One refinement was dropped that had value: v3's `aggravated-crime-inference` was a standalone refinement that could anchor a trap question precisely (when does knowledge of a grave crime, standing alone, permit an inference of purpose?). v4 integrates this into `mens-rea-lauria-inferences` as one of three factors, which is more accurate doctrinally (the three factors are not really independent rules — they are listed together in *Lauria*), but slightly reduces the standalone testability. A question focused specifically on the gravity-of-the-crime inference is marginally harder to build from v4's structure. This is a minor tradeoff.

**What v4 added that v3 had as gaps:**

- Withdrawal: now present and well-developed
- MPC merger / cumulative punishment: present in the Liability Limits element summary (stub-level, not full refinement)
- Corporate conspiracy: partially addressed via `system-architecture-racial-disparities`, which makes the Purdue Pharma comparison explicit, but there is still no standalone refinement titled "corporate conspiracy" that would anchor an exam question asking students to apply the inference-of-agreement arc to corporate actors
- Systemic architecture: two new policy refinements, both useful
- Discussion question flags: added to all cases
- Pivot facts: added to all refinements
- Jurisdiction flags: added to all refinements

**New gaps in v4:**

*Connections field:* Still missing (as noted above).

*MPC merger is underdeveloped:* It appears as a one-liner in the Liability Limits element summary ("Under the MPC, conspiracy merges with the completed offense so that a defendant cannot be punished for both the conspiracy and the substantive crime") but there is no full refinement for it with rule, trap, jurisdiction flag, or pivot fact. This is a significant omission. Cumulative punishment vs. merger is a classic exam multi-issue issue — a student who correctly identifies a completed conspiracy in a traditional jurisdiction must then ask whether the substantive offense can be charged on top. The doctrinal contrast (traditional: stacks; MPC: merges) is exam-ready material that deserves a full refinement.

*Corporate conspiracy:* The chapter's full section on this topic, including the explicit invitation to apply the inference-of-agreement arc to Purdue Pharma executives, is surfaced only through the `system-architecture-racial-disparities` policy refinement. A dedicated `corporate-conspiracy-agreement-inference` refinement would be more useful for exam design, enabling a question writer to build a fact pattern that tests whether coordinated corporate conduct satisfies *Interstate Circuit* standards.

*The Alvarez three-case arc is partially reconstructed but not explicit:* The review flagged that v3's `alvarez-nod` refinement should note that *Alvarez* is the limit case in a three-case arc (*Interstate Circuit* → *Kotteakos* → *Alvarez*). v4 puts these three cases in sequence in `cluster-agreement-inference-progression` but no individual refinement's Teaches section notes the arc relationship. This is minor but worth noting.

---

## 5. Bottom Line: v3 or v4?

**Use v4.**

v4 is a meaningfully better exam design tool than v3 on every dimension that matters for building a multi-issue conspiracy exam.

The three-tier structure alone justifies the upgrade. An exam architect working from v3 has to mentally reconstruct which "elements" are prima facie requirements versus consequential doctrines versus categorical limits. v4 does that work in the map itself. A rubric keyed to v4's structure will be analytically correct; a rubric keyed to v3's five-element structure risks sending students down wrong analytical paths.

The jurisdiction flags are the second major improvement. A multi-issue conspiracy question typically requires the exam taker to spot and resolve a jurisdictional choice — federal vs. state, traditional vs. MPC — and v4's per-refinement jurisdiction flags make the relevant choices immediately visible to the question writer.

The addition of withdrawal, discussion question flags, and the policy refinements on systemic architecture all represent genuine content gains.

The remaining gaps (Connections field, full MPC merger refinement, corporate conspiracy standalone refinement) are real but do not undermine v4's usability. An exam architect using v4 will need to supplement in those areas; an architect using v3 would need to supplement in those areas plus withdrawal plus jurisdiction flags plus structural organization.

**For a multi-issue conspiracy exam specifically:** v4's `cluster-pinkerton-scope` scenario hook (girlfriend drives partner to one deal, charged in single conspiracy, 10 kilos total, federal vs. MPC jurisdiction) is exam-ready as written. v3 had nothing comparable that clearly integrated the scope question, the vicarious liability question, the quantity attribution question, and the jurisdictional split in a single testable scenario. v4's cleaner structure makes this kind of multi-issue scenario construction straightforward.

**What would make v4 excellent:** Add a full `merger-cumulative-punishment` refinement; add a `corporate-conspiracy-inference` refinement; add a Connections field to each refinement; upgrade the MPC merger entry from one-liner to full refinement. These four additions would close all remaining gaps from the v3 review and produce a map with no significant missing content.

---

*Comparison complete.*
