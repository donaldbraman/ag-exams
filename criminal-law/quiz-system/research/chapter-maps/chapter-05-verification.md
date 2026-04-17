# Verification Report: Chapter 05 — Legislatures and Courts

**Map file:** criminal-law/quiz-system/research/chapter-maps/chapter-05.md
**Source:** criminal-law/chapters/05-legislatures-courts.qmd
**Verified at:** 2026-04-15
**Verifier model:** claude-sonnet-4-6

---

## Verification Findings

### Case Verification

#### Finding 1
- **What the map claims:** *State v. Palendrano* (1972) is described as a "main case (discussed at length in text, not excerpted but extensively quoted)"
- **What the source says:** The chapter does not present *Palendrano* as an excerpted main case. It is discussed in narrative prose with extensive quotation, more consistent with a "note case" treatment. No formal case-title header (`.case-title`) appears for it.
- **Severity:** IMPRECISE
- **Fix:** Change source type to `note case` (extensively discussed in text).

#### Finding 2
- **What the map claims:** *Robertson* — "Discussion questions: no (callout note, not discussion questions block)"
- **What the source says:** Correct. The callout after *Robertson* is a `{.callout-note}` (Legislative Response), not a `{.callout-tip}` Discussion Questions block.
- **Severity:** CLEAN

#### Finding 3
- **What the map claims:** *Skilling* — "Discussion questions: yes (discussion questions block at lines 255–265)"
- **What the source says:** The discussion questions at lines 255–265 are tied to the corruption case study section, not specifically to *Skilling* alone. They appear after the full corruption case study and reference all the cases. Attributing them to *Skilling* specifically is imprecise but not wrong — *Skilling* is Question 1.
- **Severity:** IMPRECISE
- **Fix:** Change to "yes (discussion questions follow the corruption case study, covering McNally through Snyder)"

#### Finding 4
- **What the map claims:** *Snyder* — "Discussion questions: yes (discussion questions block at lines 255–265)"
- **What the source says:** Same issue as Finding 3 — discussion questions are for the full corruption section, not *Snyder* alone.
- **Severity:** IMPRECISE (same fix as Finding 3 — note they belong to the case study section)

#### Finding 5
- **What the map claims:** *Bearden* — "Discussion questions: yes (discussion questions block at lines 335–347)"
- **What the source says:** The chapter has a `{.callout-tip}` Discussion Questions block after the Bearden/private probation section at lines 335–347. This is accurate.
- **Severity:** CLEAN

#### Finding 6
- **What the map claims:** *McNally* — facts: "kickback scheme involving insurance commissions" from Kentucky
- **What the source says:** Chapter text (lines 160–161): "Petitioners Gray, a former Kentucky official, and McNally were convicted of defrauding Kentucky citizens of their 'intangible right' to honest government through a kickback scheme involving insurance commissions." Accurate.
- **Severity:** CLEAN

#### Finding 7
- **What the map claims:** *Snyder* — "Mayor of Portage, Indiana received $13,000 from Peterbilt after his city had purchased five trash trucks"
- **What the source says:** Chapter text (lines 229–230): "In 2014, Peterbilt cut a $13,000 check to James Snyder, who was the mayor of Portage..." and the city purchased five trash trucks for ~$1.1 million in 2013. Accurate.
- **Severity:** CLEAN

#### Finding 8
- **What the map claims:** *McDonnell* — "Governor Bob McDonnell had received over $175,000 in gifts"
- **What the source says:** Chapter text (line 211): "Governor Bob McDonnell had received over $175,000 in gifts from a businessman while promoting the businessman's products to state officials." Accurate.
- **Severity:** CLEAN

#### Finding 9
- **What the map claims:** *Kelly* — "New Jersey officials ordered closure of bridge lanes as political retaliation against a mayor who declined to endorse Governor Christie"
- **What the source says:** The chapter (lines 212–213) says the defendants "closing bridge lanes as political retaliation" but does not mention Governor Christie by name or describe the retaliation target as a mayor who declined endorsement. This detail is accurate historically but not in the chapter text.
- **Severity:** IMPRECISE
- **Fix:** Limit facts to what the chapter states: "New Jersey officials ordered closure of bridge lanes as political retaliation; charged with wire fraud."

#### Finding 10
- **What the map claims:** *Ciminelli* — "Defendant rigged a state bidding process so a preferred company received contracts"
- **What the source says:** Chapter text (line 214): "rejecting the 'right to control' theory, holding that depriving a victim of 'potentially valuable economic information' about rigged bidding did not constitute fraud." The chapter does not describe specific facts about who rigged what; this is inferred from the holding description.
- **Severity:** IMPRECISE
- **Fix:** Change facts to "Defendants charged with wire fraud for rigging a bidding process; prosecution argued victims were deprived of their 'right to control' economic decisions."

#### Finding 11
- **What the map claims:** *Johnson v. United States* — "Johnson challenged his enhanced sentence under the Armed Career Criminal Act's residual clause"
- **What the source says:** Chapter text (line 49): cited as "*Johnson v. United States*, 576 U.S. 591 (2015) (ACCA residual clause unconstitutionally vague)." The chapter only provides the parenthetical; the facts in the map are accurate but drawn from outside the chapter text.
- **Severity:** IMPRECISE (minor — the map expands a citation parenthetical into a fact description, which is accurate but technically beyond what the chapter text provides)
- **Fix:** Change facts to "Defendant challenged sentence enhancement; ACCA residual clause held vague." or note source is parenthetical citation only.

### Refinement Verification

#### Finding 12
- **What the map claims:** `legality-no-retroactivity` — "Courts cannot punish conduct by expanding a statute's meaning after the fact"
- **What the source says:** The chapter discusses legality primarily in terms of legislative enactment (lines 51–52): "Legality embodies the principle that only legislatures can create crimes. Courts may not expand criminal statutes to cover conduct not clearly within the legislative text." The chapter frames this as textual expansion, not retroactivity per se. The map's framing is correct in principle but slightly over-reads the chapter — the chapter does not explicitly address retroactivity as a separate issue.
- **Severity:** IMPRECISE
- **Fix:** Narrow rule to match chapter: "Courts may not expand criminal statutes to cover conduct not clearly within the legislative text. New judicial constructions expanding a statute's reach cannot be applied to conduct that preceded the expansion."

#### Finding 13
- **What the map claims:** `desuetude-prolonged-nonenforcement` cites *Stowell* as "declining to invalidate" and notes "last prosecuted 1829" for D.C. common scold
- **What the source says:** Chapter text (line 55): *Stowell* "acknowledging adultery statute had fallen into 'comprehensive desuetude' but declining to invalidate it." D.C. common scold last prosecuted 1829 is stated in the chapter (line 21). Both accurate.
- **Severity:** CLEAN

#### Finding 14
- **What the map claims:** `honest-services-mcnally-narrowing` — "Before Congress enacted § 1346, the 'honest services' theory of fraud was invalid"
- **What the source says:** Accurate. Chapter (lines 171–172): Congress responded within 18 months, enacting § 1346 to restore honest services doctrine *McNally* eliminated.
- **Severity:** CLEAN

#### Finding 15
- **What the map claims:** `corruption-bribe-vs-gratuity` — "Federal § 666 covers only bribes" citing *Snyder*
- **What the source says:** Chapter (lines 225–233) through the *Snyder* excerpt: "§ 666—like § 201(b)—is a bribery statute, not a gratuities statute." Accurate.
- **Severity:** CLEAN

#### Finding 16
- **What the map claims:** `bearden-circumvention-fees-not-fines` — "Supervision fees were administrative costs of monitoring compliance"
- **What the source says:** Chapter (lines 302–304): "supervision fees were administrative costs of monitoring compliance. *Bearden* addressed what happens when defendants cannot pay fines. It did not directly address supervision fees." Accurate.
- **Severity:** CLEAN

#### Finding 17 — MISSING content check
- **What the map claims:** No refinement addresses the *Reform Commissions* callout note (Illinois CLEAR Commission success; D.C. Criminal Code Reform Commission failure)
- **What the source says:** Chapter (lines 130–140) discusses reform commissions as a legislative response mechanism, with two case studies. This is a substantive pedagogical point about how legislatures attempt to correct accumulated criminal code errors — and it is tested territory (discussion question: "Why do you think some commissions succeed while others fail?"). The callout is a `{.callout-note}` not a `{.callout-tip}` but contains a genuine discussion prompt.
- **Severity:** MISSING
- **Fix:** Add refinement `reform-commissions-mixed-results` under Asymmetric Correction Principle or a new section.

#### Finding 18 — MISSING content check
- **What the map claims:** No refinement specifically addresses the Bentham quote on asymmetric error in punishment, which the chapter presents as a historical antecedent to the asymmetric correction principle
- **What the source says:** Chapter (lines 120–124) quotes Bentham on errors of under-punishment being easier to remedy than over-punishment. The chapter explicitly connects this to statutory interpretation. This is a testable synthesis point — students may be asked to apply Bentham's analysis to a modern case.
- **Severity:** MISSING (minor — subsumed within `asymmetric-correction-under-over-inclusive`, but the Bentham historical grounding is a distinct pedagogical point the chapter emphasizes)
- **Fix:** Add to existing refinement's rule, or note Bentham as a source for `asymmetric-correction-under-over-inclusive`.

#### Finding 19
- **What the map claims:** `bearden-hb310-adaptation` — "Courts began routinely imposing additional conditions—online classes, drug testing—which restarted the clock"
- **What the source says:** Chapter (lines 329–330): "Courts began routinely imposing additional conditions—online classes, drug testing—which restarted the clock." Accurate verbatim.
- **Severity:** CLEAN

#### Finding 20
- **What the map claims:** `notice-rationale-fiction` — cites "Anne Royall did not check common scold law; Marion Palendrano did not research reception of English common law"
- **What the source says:** Chapter (lines 71–73): "Did Anne Royall check whether 'quarrelsome speech' was criminal before criticizing the Presbyterians? Did Marion Palendrano research New Jersey's reception of English common law before her altercation with Margaret Maguire?" Accurate.
- **Severity:** CLEAN

### Structural Checks

#### Finding 21
- **What the map claims:** All refinement keys are kebab-case
- **Verification:** Checked all 24 keys — all use lowercase letters and hyphens only, no underscores, spaces, or capitals.
- **Severity:** CLEAN

#### Finding 22
- **What the map claims:** All required sections present (## Elements, ## Refinements, ## Clusters, ## Cases, ## Coverage Checklist)
- **Verification:** All five sections present.
- **Severity:** CLEAN

#### Finding 23
- **What the map claims:** Coverage checklist has 24 rows matching 24 refinements
- **Verification:** `#### ` heading count = 24; coverage checklist rows = 24 (confirmed by reviewing both). Match confirmed.
- **Severity:** CLEAN

#### Finding 24
- **What the map claims:** All refinements have Trap, Pivot fact, and Jurisdiction
- **Verification:** Spot-checked all 24 refinements — all contain `**Trap:**`, `**Pivot fact:**`, and `**Jurisdiction:**` fields.
- **Severity:** CLEAN

#### Finding 25
- **What the map claims:** Trap format follows "Students [X] because [Y]"
- **Verification:** All traps reviewed — all follow the required format.
- **Severity:** CLEAN

#### Finding 26 — DUPLICATE check
- **What the map claims:** `lenity-harsher-reading-requires-clear-congress` and `lenity-genuine-ambiguity-required` are separate refinements
- **What the source says:** These are distinct enough: `lenity-genuine-ambiguity-required` addresses the threshold condition (genuine ambiguity must exist before lenity applies); `lenity-harsher-reading-requires-clear-congress` addresses the standard (harsher reading requires clear congressional statement). They overlap but are not duplicates — the first is a trigger condition, the second is the substantive rule.
- **Severity:** CLEAN

#### Finding 27
- **What the map claims:** `asymmetric-correction-notice-liberty-instrumental` and `notice-rationale-fiction` / `legislative-supremacy-overcrimination` are separate
- **What the source says:** These address different aspects: `asymmetric-correction-notice-liberty-instrumental` (notice/liberty as instrumental rather than intrinsic, from the asymmetric correction section); `notice-rationale-fiction` (the empirical critique that defendants don't actually consult statutes); `legislative-supremacy-overcrimination` (broad statutes delegate lawmaking to prosecutors). All three points are explicitly distinguished in the chapter text (lines 62–75 vs. lines 126–128). Not duplicates.
- **Severity:** CLEAN

---

## Summary

| Severity | Count |
|----------|-------|
| HALLUCINATION | 0 |
| ERROR | 0 |
| DUPLICATE | 0 |
| MISSING | 2 (Finding 17, 18) |
| IMPRECISE | 7 (Findings 1, 3, 4, 9, 10, 11, 12) |

**Total findings requiring action:** 9
**Blocking issues (HALLUCINATION/ERROR/DUPLICATE):** 0
**Advisory (MISSING/IMPRECISE):** 9

### Recommended Fixes

1. **Finding 1:** Change *Palendrano* source type from `main case` to `note case`
2. **Findings 3–4:** Update *Skilling* and *Snyder* discussion questions note to reference the full corruption case study
3. **Finding 9:** Trim *Kelly* facts to what the chapter actually states (remove Governor Christie and "declined to endorse" — not in chapter text)
4. **Finding 10:** Trim *Ciminelli* facts to chapter-sourced description
5. **Finding 11:** Trim *Johnson* facts to parenthetical-only content
6. **Finding 12:** Narrow `legality-no-retroactivity` rule to match chapter's actual framing (textual expansion, not temporal retroactivity)
7. **Finding 17 (MISSING):** Add `reform-commissions-mixed-results` refinement for the reform commission callout (Illinois CLEAR success vs. D.C. failure)
8. **Finding 18 (MISSING):** Add Bentham as source to `asymmetric-correction-under-over-inclusive` or add a sub-point about the historical grounding
