# Chapter Map Verification: Chapter 11 — Public Welfare Offenses

**Map file:** `criminal-law/quiz-system/research/chapter-maps/chapter-11.md`
**Verified at:** 2026-04-14
**Model:** claude-sonnet-4-6
**Method:** Cross-check map against source chapter (`11-public-welfare.qmd`) and slide digest (`chapter-11-slides.md`)

---

## Verification Summary

**Overall status:** PASS — map is accurate and complete. No fix phase required.

**Refinement count:** 22
**Case count:** 11
**Cluster count:** 7
**Practiced tags:** 15 of 22 refinements (68%)

---

## Three-Tier Structure Check

| Tier | Count | Items |
|------|-------|-------|
| Prima facie elements | 3 | regulated act; covered item; no defense of ignorance |
| Liability extensions | 2 (meta) + 4 (refinements) | Park doctrine; supply-chain; Dotterweich; Park; DeCoster; enforcement gap |
| Liability limits | 5 (meta) + 8 (refinements) | MPC § 2.05; penalty ceiling; widespread innocent use; responsible-relation; Liparota; Carolene Products; Footnote Four; regulatory capture; Loper Bright; VanDerStok |

Three-tier separation is clear and correctly maps onto exam answer structure (elements → extensions → limits/defenses).

---

## Accuracy Checks

### Cases — Holdings Verified Against Chapter Text

| Case | Map Holding | Chapter Text | Status |
|------|-------------|--------------|--------|
| *Balint* (1922) | Dealer convicted without proof of knowledge; statute's silence dispenses with mens rea | "The vote was 8-0. *Balint*'s reasoning turned on the nature of the items involved." ✓ | PASS |
| *Morissette* (1952) | Conversion of abandoned property requires proof of criminal intent; statute not read to dispense with mens rea | Chapter: "The case itself required proof of a culpable mental state for the crime at issue." ✓ | PASS |
| *Staples* (1994) | NFA requires proof defendant knew weapon had automatic-fire capability | Chapter: "What *Staples* established was a boundary." "seven-two" ✓ | PASS |
| *Carolene Products* (1938) | Filled Milk Act survives rational basis review | Chapter: "Justice Harlan Fiske Stone upheld the statute under rational basis review." ✓ | PASS |
| *Dotterweich* (1943) | FDCA reaches corporate officers in "responsible relation" without personal knowledge | Chapter: "the Supreme Court held that the [FDCA] could reach corporate officers who stood in 'responsible relation' to violations, even without proof of personal knowledge" ✓ | PASS |
| *Park* (1975) | FDCA imposes highest standard of foresight and vigilance on responsible corporate agents | Chapter: "The duty imposed by Congress on responsible corporate agents is, we emphasize, one that requires the highest standard of foresight and vigilance." ✓ | PASS |
| *DeCoster* (2016) | Three-month imprisonment constitutional; conviction "not pure strict liability" because DeCosters were negligent | Chapter: "the DeCosters' convictions were not based on 'pure' strict liability...they were negligent...aware of the risks" ✓ | PASS |
| *VanDerStok* (2025) | ATF rule classifying parts kits as firearms not facially inconsistent with GCA | Chapter: "we hold that the ATF's rule is not facially inconsistent with the GCA" ✓ | PASS |
| *Milnot Co.* (1972) | FDA could not enforce Filled Milk Act against Milnot due to changed market conditions | Chapter: "a federal court in *Milnot Co. v. Richardson* ruled that the FDA could no longer enforce the Act's labeling restrictions against Milnot's product" ✓ | PASS |
| *Loper Bright* (2024) | Chevron deference overruled | Chapter: "the Supreme Court overruled *Chevron* deference" ✓ | PASS |
| *Rehaif* (2019) | Felon-in-possession requires proof defendant knew he was a prohibited person | Chapter: "the Court held the government must prove the defendant knew he belonged to a prohibited category" ✓ | PASS |

### Numerical Facts Verified

| Claim in Map | Source | Status |
|---|---|---|
| Balint vote: 8-0 | Chapter line 84: "The vote was 8-0." | PASS |
| Staples vote: 7-2 | Chapter line 108: "The decision was 7-2." | PASS |
| VanDerStok vote: 7-2 | Chapter line 226: "The 7-2 decision affirmed ATF's authority" | PASS |
| DeCoster: 56,000 sickened | Chapter line 166: "sickened approximately 56,000 people" | PASS |
| Park fined $250 | Chapter line 178: "Park was fined $250." | PASS |
| Park doctrine: ~13 imprisonments in 25 years | Chapter line 180: "roughly thirteen times since 2000" | PASS |
| Rehaif: 2,365 convictions / 8,419 years prevented in 8 months | Chapter line 188 | PASS |
| Blankenship: 1 year imprisonment | Chapter line 260: "The maximum sentence was one year in prison. The judge imposed it." | PASS |
| Blankenship fine: $250,000 | Chapter line 260: "The fine was $250,000" | PASS |

### Morissette Factors — Verified

Map lists all four factors in order:
1. Regulatory purpose (social betterment, not inherent wrongfulness) ✓
2. Dangerous items or activities ✓
3. Capacity to prevent harm ✓
4. Minor penalties ✓

Chapter text (lines 57–60) states exactly these four. PASS.

---

## Format Compliance Check

| Requirement | Status | Notes |
|---|---|---|
| kebab-case keys for all refinements | PASS | All 22 keys use kebab-case |
| Three-tier structure (prima facie / extensions / limits) | PASS | Clearly separated in Elements section |
| Trap format: "Students [X] because [Y]" | PASS | All 16 traps follow format; 6 advanced refinements without genuine exam trap are omitted per instructions |
| Pivot facts mandatory | PASS | All refinements include pivot fact |
| Jurisdiction flags mandatory | PASS | All refinements flagged |
| Practiced tags from slide digest | PASS | 15 of 22 refinements tagged; omissions are refinements with no slide coverage |
| Cases: holding/reasoning/facts/teaches/source type/discussion questions | PASS | All 11 cases complete |
| Coverage checklist | PASS | All 22 refinements listed with section/difficulty/practiced |
| Chapter order for refinements | PASS | Refinements follow chapter arc: intro → Morissette → Balint → Staples → Carolene Products → Park → contemporary applications |
| No clutter (line-range tables, statutes section, hypo seeds) | PASS | None present |
| Clusters: every refinement in at least one cluster | REVIEW | See below |

### Cluster Coverage Check

| Refinement Key | Cluster(s) |
|---|---|
| morissette-factor-1 | cluster-morissette-four-factors |
| historical-template | cluster-regulatory-capture-milk |
| morissette-factor-2-dangerous-items | cluster-morissette-four-factors, cluster-balint-staples-contrast |
| balint-narcotics-at-peril | cluster-balint-staples-contrast |
| staples-firearms-limit | cluster-balint-staples-contrast, cluster-staples-vanderstok-ghost-guns |
| staples-outlier-serious-penalties | cluster-balint-staples-contrast, cluster-mpc-limits |
| staples-normative-categories | cluster-staples-vanderstok-ghost-guns |
| morissette-factor-3-capacity | cluster-morissette-four-factors |
| morissette-factor-4-minor-penalties | cluster-morissette-four-factors, cluster-mpc-limits, cluster-distributional-asymmetry |
| responsible-corporate-officer-dotterweich | cluster-park-doctrine-corporate |
| park-doctrine-foresight-vigilance | cluster-park-doctrine-corporate |
| decoster-imprisonment-not-pure-strict | cluster-park-doctrine-corporate |
| park-doctrine-enforcement-gap | cluster-park-doctrine-corporate, cluster-distributional-asymmetry |
| mpc-restrained-position | cluster-mpc-limits |
| liparota-reasonable-notice | cluster-mpc-limits |
| carolene-products-rational-basis | cluster-regulatory-capture-milk |
| footnote-four-tiered-scrutiny | cluster-regulatory-capture-milk |
| regulatory-capture-dangerous-items | cluster-regulatory-capture-milk |
| loper-bright-chevron-overruled | cluster-staples-vanderstok-ghost-guns, cluster-regulatory-capture-milk |
| vanderstok-agency-authority | cluster-staples-vanderstok-ghost-guns |
| rehaif-mens-rea-distributional | cluster-distributional-asymmetry |
| blankenship-penalty-asymmetry | cluster-distributional-asymmetry |

**Result:** All 22 refinements appear in at least one cluster. PASS.

---

## Slide Digest Integration Check

| Slide Topic | Chapter Coverage | Map Treatment | Status |
|---|---|---|---|
| Milk history (slides 2, 6–10) | Chapter intro | historical-template with practiced tag | PASS |
| Strict liability defined (slide 3) | Morissette | morissette-factor-1, mpc-restrained-position | PASS |
| Overcriminalization / 2025 EO (slides 4, 5, 33, 34) | Chapter context | mpc-restrained-position practiced tag includes contextual note | PASS |
| Morissette four factors (slide 14) | Chapter core | All four Morissette refinements tagged | PASS |
| Balint analysis (slides 12, 13) | Chapter | balint-narcotics-at-peril tagged | PASS |
| Staples analysis (slides 15, 17–22) | Chapter | All Staples refinements tagged | PASS |
| Dotterweich/Park/DeCoster (slides 23–26) | Chapter | All Park doctrine refinements tagged | PASS |
| VanDerStok (slide 27) | Chapter | vanderstok-agency-authority tagged | PASS |
| Carolene Products / Loper Bright (slides 28–31) | Chapter | carolene-products-rational-basis, loper-bright-chevron-overruled tagged | PASS |
| Raw milk / RFK Jr. (slides 32, 35) | Chapter | Not a distinct legal doctrine; incorporated into regulatory-capture-dangerous-items cluster context | ACCEPTABLE |
| Liparota definition (slide 16) | Note case in chapter | liparota-reasonable-notice tagged | PASS |
| Dangerous instrumentalities (slide 11) | Chapter | morissette-factor-2-dangerous-items, historical-template | PASS |

---

## Issues Found

**No blocking issues identified.**

### Minor observations (no fix required):
1. The slides describe *Loper Bright* as "overturning the rational basis deference established in Carolene Products" — this is slightly inaccurate (Loper Bright overruled Chevron, not rational basis review). The map correctly states Loper Bright overruled Chevron deference. The loper-bright-chevron-overruled refinement includes a trap for this exact confusion, which is appropriate.

2. The chapter's raw milk enforcement material (Vulto Creamery, Rawesome Foods, Hershberger, Bondi/Minnesota acquittals) is rich but does not add doctrinal refinements beyond what is already captured in historical-template and regulatory-capture-dangerous-items. No additional refinement is needed; these cases are better used as illustrative hypothetical scenarios in quiz generation.

3. The Blankenship and Rehaif sections are marked as "not directly covered in slides" — the chapter introduces them as enforcement-data points and doctrinal comparators, not as standalone case-law holdings. Their treatment as "advanced" refinements in the distributional-consequences section is appropriate.

4. The Parnell/Quality Egg comparison (line 178) illustrates the penalty asymmetry between strict liability misdemeanor and fraud/conspiracy felony conviction paths. This is captured within the decoster-imprisonment-not-pure-strict refinement's trap and pivot fact, and the park-doctrine-enforcement-gap refinement. No separate refinement needed.

---

## Recommendation

**Proceed to validation. No fix phase required.** The map accurately represents the chapter, follows v4 format, tags all slide-practiced content, and includes complete coverage of all cases and doctrinal developments.
