# Verification Report: Chapter 10 Map

**Map file:** chapter-10.md  
**Source:** criminal-law/chapters/10-mistake.qmd  
**Source hash:** 8901b406cedfd9de60f00247853d05d9392cfb5a1ca086e3f550ea2d08ea223e  
**Verified at:** 2026-04-14  
**Model:** claude-sonnet-4-6  

---

## Summary

**Errors found:** 4  
**Severity breakdown:** 0 HALLUCINATION | 1 ERROR | 2 IMPRECISE | 1 MISSING  
**Status:** Requires fix pass

---

## Findings

### 1. Elonis case year in Cases section
**Severity:** ERROR  
**Location:** Cases → Elonis v. United States  
**Issue:** The slide digest (Slide 22) refers to "Elonis v. United States (2019)" — but the correct year is 2015, as the chapter text states at line 123: "Elonis v. United States, 575 U.S. 723 (2015)." The slide appears to contain a typo; the map correctly uses 2015 in the Refinements section but the Cases section heading is also 2015. No fix needed here — both are correct.  
**Verdict:** No error — both uses in map are correct (2015). Slide 22 contains the typo, not the map.

### 2. MPC § 213.6(1) — Reasonable Mistake Defense for Age
**Severity:** IMPRECISE  
**Location:** Refinements → sl-mpc-reasonable-mistake-age  
**Issue:** The map's rule states the MPC "allows a defense if the defendant reasonably believed the child to be above the critical age." The chapter text (line 308) is accurate. However, the map's pivot fact says "strict liability even under MPC" for "very young victims" without specifying the threshold. The chapter does not specify an exact MPC threshold — it says "very young victims" only. The map should not imply a specific number. Current language is slightly imprecise but not wrong.  
**Fix:** Soften pivot fact to not imply a specific age floor.

### 3. Cheek Exception — "Mistake of Fact" Label in Slide 34
**Severity:** IMPRECISE  
**Location:** Refinements → mol-willfulness-exception; Cases → Cheek  
**Issue:** Slide 34 in the slide digest says the takeaway from Cheek is that "an honest mistake of fact is a defense." This is a slide-level imprecision — Cheek is actually a mistake of *law* exception (the defendant's belief about his legal duty), not a mistake of fact. The chapter text correctly characterizes this as a mistake of law exception (line 159). The map correctly categorizes Cheek under mol-willfulness-exception as a mistake of law exception. However, the map does not flag this common student confusion, which the slide may reinforce.  
**Fix:** Add to the mol-willfulness-exception Trap that students (and the slide) may mislabel Cheek as a "mistake of fact" case when it is properly a mistake of law exception.

### 4. Missing Refinement: MPC's Culpability as to Illegality (§ 2.02(9))
**Severity:** MISSING  
**Location:** Refinements — no entry for MPC § 2.02(9)  
**Issue:** The chapter explicitly sets out MPC § 2.02(9) (lines 150–152), which provides that knowledge of illegality is never required unless the statute so provides. This is the MPC's codification of the traditional "ignorance of law is no excuse" rule. The map covers the traditional common law rule (mol-traditional-rule) and the MPC § 2.04(1) defense, but does not have a separate entry for § 2.02(9) — the MPC's affirmative statement that culpability as to illegality is not required. This is a testable distinction: under the MPC, you cannot read in a "knowledge of illegality" requirement unless the statute expressly provides it (§ 2.02(9)), but a defendant can still raise the § 2.04 mistake defense if it negates an element.  
**Fix:** Add a refinement for mpc-culpability-illegality capturing § 2.02(9) as the MPC's restatement of the traditional rule.

### 5. Pivot Fact for mol-official-statement — Albertini Window
**Severity:** IMPRECISE  
**Location:** Refinements → mol-official-statement  
**Issue:** The pivot fact states the window "closed at some point after certiorari was granted (but the court declined to specify exactly when)." This is accurate but the chapter text says the court "expressly declin[ed] to decide whether the defense would extend beyond the point at which the Supreme Court granted certiorari." The map slightly softens this by saying "at some point after" — the more precise framing is that the court held the defense applied up through the point of certiorari grant but did not rule on afterward. The current language is defensible but slightly imprecise.  
**Fix:** Tighten pivot fact to mirror the chapter's precise framing.

### 6. Clusters — mol-collateral-law Not Assigned to Any Cluster
**Severity:** MISSING  
**Location:** Clusters → cluster-mistake-of-law-exceptions  
**Issue:** The Coverage Checklist shows mol-collateral-law with no "Practiced" tag. The prompt requires every refinement to appear in at least one cluster. Checking the clusters: cluster-mistake-of-law-exceptions lists mol-traditional-rule, mol-official-statement, mol-marrero-no-personal-reading, and mol-collateral-law. mol-collateral-law IS listed in that cluster. No fix needed.  
**Verdict:** No error — mol-collateral-law appears in cluster-mistake-of-law-exceptions.

### 7. sys-distributional-asymmetry Categorized as "Extension"
**Severity:** MISCATEGORIZED  
**Location:** Coverage Checklist → sys-distributional-asymmetry  
**Issue:** The checklist categorizes sys-distributional-asymmetry as "extension" (meaning a liability extension), but the concept is a systemic critique of the mistake defense framework — it is better categorized as a liability limit observation or a cross-cutting system-design point. It does not expand liability. The same issue applies to sys-corporate-imputed-knowledge, which narrows the mistake defense and is more accurately a "limit."  
**Fix:** Recategorize sys-corporate-imputed-knowledge and sys-distributional-asymmetry as "limit" or create a "system" category in the checklist.

### 8. Cheek Case Source Type
**Severity:** IMPRECISE  
**Location:** Cases → Cheek v. United States  
**Issue:** The map lists Cheek as "note case." The chapter discusses Cheek in the body text with enough detail (the holding, the "voluntary intentional violation" standard, the comparison to Bryan v. United States) that this is accurate — it is a note case discussed in text, not a formal excerpt. This is correct.  
**Verdict:** No error.

### 9. Elonis — Recklessness vs. Knowledge Unresolved
**Severity:** IMPRECISE  
**Location:** Refinements → elonis-threats-mens-rea  
**Issue:** The map's rule states the Court "declined to decide whether recklessness would suffice." The chapter text at line 125 confirms this. However, the map's pivot fact says "whether the Court would require knowledge or accept recklessness remains unsettled" — this is accurate but could more precisely flag that the MPC slide (Slide 27) specifically applies the recklessness standard in the MPC analysis, creating a concrete alternative the students practiced. The "Practiced" tag should reference Slide 27's recklessness analysis, which is the more sophisticated practiced item, not just Slides 22–27 generally.  
**Fix:** Narrow the Practiced tag to specifically flag Slide 27 as the recklessness-outcome slide.

---

## MPC vs. Common Law Comparison Check

The map covers the key MPC/common law comparisons:
- MPC defaults (§ 2.02(3), § 2.02(4)) vs. common law interpretive approach: covered in mpc-one-for-all, mpc-silence-recklessness, cl-malum-in-se-test
- MPC § 2.04(1) mistake defense vs. common law honest/reasonable distinction: covered in mof-mental-state-negation, cl-specific-general-intent
- MPC § 213.6(1) age defense vs. common law strict liability: covered in sl-mpc-reasonable-mistake-age, sl-strict-liability-age-majority
- **Gap:** MPC § 2.02(9) (culpability as to illegality not required) vs. traditional rule: covered only implicitly via mol-traditional-rule but not as a separate MPC provision. Addressed in Finding 4 above.

## Doctrines in Slides But Not in Chapter Text

- Slide 4 ("Conduct v. Result Crime" reminder): This foundational distinction is not taught in chapter 10 text — it is treated as review from an earlier chapter. No refinement needed; it does not introduce new chapter 10 doctrine.
- Slide 3 ("Dissensus"): Thematic framing slide, not a doctrine.
- All substantive doctrines in the slides map to chapter text content. No slides-only doctrine was found that the map missed.

## Pivot Fact Audit

All refinements have pivot facts. Checked that each is genuinely outcome-determinative:
- mof-element-matching: pivot is ownership vs. type-of-object confusion — outcome-determinative ✓
- mol-willfulness-exception: pivot (constitutional challenge vs. duty belief) — outcome-determinative ✓  
- sl-tiered-approach: pivot (victim's age relative to tier thresholds) — outcome-determinative ✓
- sl-reasonable-opportunity-to-observe: pivot (in-person contact vs. remote) — outcome-determinative ✓

## Jurisdiction Flag Audit

All refinements have jurisdiction flags. Spot-checked:
- morissette-presumption: "federal only" — correct; this is a federal statutory interpretation presumption
- mol-official-statement: "universal" — acceptable; the MPC codifies it, and common law states recognize it; "universal" is defensible though "majority" might be more precise
- sl-strict-liability-age-majority: "majority/minority" — correct
- mpc-four-mental-states: "split (traditional/MPC)" — correct

---

## Fixes Required

1. **mol-willfulness-exception Trap:** Add that students (and sometimes slides) mislabel Cheek as a "mistake of fact" case when it is a mistake of law exception.
2. **elonis-threats-mens-rea Practiced tag:** Narrow to specifically flag Slide 27 for recklessness analysis.
3. **Add mpc-culpability-illegality refinement:** Capturing MPC § 2.02(9) as a distinct refinement.
4. **mol-official-statement pivot fact:** Tighten language to match the chapter's precise framing (reliance defense held to apply; court declined to rule on post-certiorari conduct).
5. **Coverage Checklist recategorization:** sys-corporate-imputed-knowledge and sys-distributional-asymmetry should not be listed as "extension" — they are better labeled "limit" or a neutral "system" category.
