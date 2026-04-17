# Chapter 19 Conspiracy — Chapter Map Verification Report

**Verifier:** Claude Sonnet (claude-sonnet-4-20250514)
**Date:** 2026-04-14
**Source chapter:** `criminal-law/chapters/19-conspiracy.qmd` (514 lines)
**Maps verified:**
- Gemini: `chapter-19-gemini-3pass-md.md`
- Opus: `chapter-19-opus-markdown.md`
- Sonnet: `chapter-19-sonnet-markdown.md`

---

## Methodology

Every named case, stated holding, cited line range, and rule claim was checked against the chapter source. Line numbers in the chapter are 1-indexed as read by the Read tool. Errors are classified as:

- **HALLUCINATION** — claim is fabricated or has no support anywhere in the chapter
- **ERROR** — claim is clearly wrong
- **IMPRECISE** — claim is approximately right but meaningfully off
- **DUPLICATE** — two doctrines in the same map represent the same concept

---

## GEMINI MAP VERIFICATION

### Case Claims

**1. Alvarez facts — IMPRECISE**
- Map claims (Case entry, lines 336–340): "A man at an airport nodded and smiled when asked if he would help unload a plane arriving with marijuana and then helped unload household appliances from a truck."
- Chapter says (line 381): Alvarez drove a truck *loaded with household appliances* to the airport. He was asked if he planned to be at the **unloading site when the plane returned** (not whether he would help unload the plane). He then unloaded the *appliances he had brought* — he did not unload any drugs or a plane. The phrasing "help unload a plane" conflates his role with the drug operation.
- Severity: IMPRECISE. The distinction matters because his agreement was to be present at a future event; unloading the appliances was incidental, not the conspiratorial act.

**2. Interstate Circuit characterized as "chain conspiracy" — ERROR**
- Gemini doctrine 11 ("chain-conspiracy", lines 319–344): "In a vertical chain of distribution (e.g., manufacturer to wholesaler to retailer), an agreement is inferred because each party knows their success depends on the performance of the others." This doctrine is tagged to *Interstate Circuit*.
- Chapter says (lines 317, 341): *Interstate Circuit* is about horizontal competitors (film distributors) who each received the same letter, each knew the others were also being asked to comply, and each complied. It is explicitly presented as a case about inferring agreement from **conscious parallelism** and **mutual awareness**, not a vertical chain. The chapter does not use "chain conspiracy" terminology anywhere. There is no vertical distribution chain in *Interstate Circuit*.
- Severity: ERROR. Gemini has mislabeled a horizontal-parallelism case as a vertical chain-conspiracy case. The chain-conspiracy concept does not appear in this chapter as a named doctrine.

**3. Pinkerton dissent attribution — IMPRECISE**
- Gemini Case entry for *Pinkerton* (lines 319–322): "Two brothers conspired to violate tax laws; one brother was in prison when the other committed substantive tax offenses, yet both were held liable."
- Chapter says (lines 255, 275): Daniel was in prison when *some* of Walter's crimes were committed (per the dissent), but the majority opinion does not specifically rely on or mention Daniel being incarcerated. The majority opinion says only "there is no evidence of the affirmative action on the part of Daniel which is necessary to establish his withdrawal." The detail about Daniel being in prison comes from the Rutledge dissent, not the majority.
- Severity: IMPRECISE. The map presents the prison-during-offenses fact as the uncontested basis for the holding, when it is actually the dissent's framing. The majority nowhere mentions imprisonment as the key fact.

**4. Pinkerton — "tax laws" description — IMPRECISE**
- Map says "conspired to violate tax laws." Chapter says "violations of the Internal Revenue Code" / "unlawful possession, transportation, and dealing in whiskey, in fraud of the federal revenues" (line 277). This is more precisely revenue/excise fraud related to liquor, not a broad "tax law" conspiracy.
- Severity: IMPRECISE (minor).

### Doctrine Claims

**5. MPC overt act split stated backwards — ERROR**
- Gemini doctrine 3 ("overt-act-requirement"), Split field: "MPC 5.03(5) waives the overt act requirement for first and second-degree felonies."
- Chapter says (MPC § 5.03(5), line 44): "No person may be convicted of conspiracy to commit a crime, **other than a felony of the first or second degree**, unless an overt act... is alleged and proved." This means the MPC *requires* an overt act for crimes *below* first/second degree felonies, and *waives* the requirement only for first/second degree felonies.
- The Gemini statement "waives the overt act requirement for first and second-degree felonies" is technically correct as stated but the framing is misleading in context: the split field suggests this is an unusual feature, but the chapter presents it as the MPC rule — the overt act *is not required* for first- and second-degree felonies. This is correctly stated.
- On further review: this entry is accurate. **Withdraw error finding — no error.**

**6. Doctrine 11 ("chain-conspiracy") — HALLUCINATION**
- The chapter does not contain or discuss the "chain conspiracy" doctrine by name. "Chain conspiracy" as a distinct doctrine (vertical distribution chain with inferred interdependence) does not appear anywhere in chapter 19. The concept referenced is *Interstate Circuit*'s inference of agreement among horizontal competitors, which is a distinct doctrine.
- Severity: HALLUCINATION. The doctrine itself — as a named concept — is invented and applied incorrectly to *Interstate Circuit*.

**7. Withdrawal doctrine — IMPRECISE line range**
- Gemini doctrine 15 ("withdrawal-and-renunciation"), Lines field: `[[261, 281, 480]]`. This is not a valid line-range format (three numbers in one array). The intended meaning is presumably lines 261–281 and also line 480. Lines 261–281 are the Pinkerton dissent (which discusses withdrawal). Line 480 is from the comparison table (line 480: "Withdrawal | Affirmative steps to defeat conspiracy + communication to coconspirators | Withdrawal terminates future liability"). Both references exist and are relevant. The formatting is simply malformed.
- Severity: IMPRECISE (formatting error, not a content error).

**8. Blocks table: Markel case study lines 9–32 — IMPRECISE**
- Blocks table lists block `9-32` but the chapter Markel section ends at line 31 (line 32 is blank). Minor.

**9. Blocks table: `411–439` assigned to "inferring-agreement" — IMPRECISE**
- The blocks table assigns lines 411–439 (the Purdue Pharma section) to `["inferring-agreement", "coconspirator-hearsay-exception"]`. The chapter discussion at these lines concerns **corporate conspiracy** and the gap between entity and individual liability. The agreement-inference discussion is only tangentially raised in the discussion questions (line 436). The primary doctrine is corporate conspiracy, not inferring-agreement.
- Severity: IMPRECISE.

**10. Duplicate doctrines 2 and 5 — DUPLICATE**
- Gemini doctrines 2 ("conspiracy-mens-rea-purpose") and 5 ("intent-to-target-elements") both concern the mental state required for conspiracy. Doctrine 2 states "the defendant must act with the specific purpose of promoting or facilitating the commission of the object crime." Doctrine 5 states "A conspirator must specifically intend that every element of the planned offense be accomplished."
- These are distinct issues in the chapter: doctrine 2 is about the general purpose requirement (knowledge vs. purpose to agree), while doctrine 5 is specifically about *Pond*'s holding that each *element* of the target offense must be intended. They are related but not identical. The chapter itself treats them at different locations (lines 59–60 vs. lines 84–132).
- Severity: IMPRECISE (over-splitting rather than true duplication, but the boundary is blurry enough to cause student confusion).

### Missing Content

**11. *Krulewitch v. United States* — MISSING**
- The chapter discusses *Krulewitch v. United States*, 336 U.S. 440 (1949) (Jackson, J., concurring) at lines 487–489, with a quoted warning about the dangers of conspiracy trials. None of the maps include *Krulewitch* as a case. (All three maps miss this, addressed in the cross-map section below.)

---

## OPUS MAP VERIFICATION

### Case Claims

**1. Alvarez facts — ACCURATE**
- Opus case entry (lines 277–280): "Day laborer Alvarez drove a truck to an airport where others arranged a marijuana importation flight; he nodded, smiled, and asked if an undercover agent was going on the plane, then unloaded appliances." This accurately captures the chapter's account.

**2. *Kotteakos* — loans described as "home improvements or purchases" — ACCURATE**
- Chapter (line 356): "The loans were made to finance home improvements or purchases." Opus (line 273): "fraudulent FHA loans." Accurate at the level stated.

**3. *Pinkerton* — prison detail placed in dissent — ACCURATE**
- Opus fact statement (lines 296–298): "Brothers Walter and Daniel Pinkerton conspired to commit revenue fraud; Walter committed substantive offenses while Daniel was in prison; Daniel was convicted of the substantive offenses based solely on the ongoing conspiracy." The prison detail is stated as fact, which technically appears only in the Rutledge dissent, not the majority opinion. However, this is a minor imprecision (the prison fact is acknowledged by the dissent in describing what happened) rather than a fabrication.
- Severity: IMPRECISE (same issue as Gemini above).

**4. *Hyde v. United States* characterized as dissent holding — ACCURATE**
- Opus case entry (lines 337–338): "Holmes dissent: 'it does not matter how remote the act may be from accomplishing the purpose, if done to effect it' — establishing the minimal nature of the overt act requirement." This accurately reflects the chapter's presentation (line 61–62): Holmes's dissent is cited for this proposition.

**5. *Krulewitch* — ACCURATE but limited**
- Opus includes *Krulewitch* (lines 342–346) with an accurate holding summary and assigns it to [single-vs-multiple-conspiracies]. However, the chapter uses *Krulewitch* in the "Conspiracy as System Architecture" section (lines 487–489) in the context of the general dangers of conspiracy trials, not specifically in the single-vs-multiple context. This is a minor misclassification of doctrine assignment.
- Severity: IMPRECISE.

### Doctrine Claims

**6. Doctrine 1 ("conspiracy-agreement") Split field — IMPRECISE**
- Opus Split: "Traditional approach allows broad inference from parallel conduct; MPC requires actual agreement."
- Chapter (line 476 table): The Traditional vs. MPC comparison table states "Agreement | Can be inferred from coordinated conduct | Requires actual agreement." This matches Opus's claim. However, the chapter nowhere explicitly states "MPC requires actual agreement" as a named rule in the text itself — this only appears in the comparison table. The split as stated is a fair reading of the table.
- Severity: IMPRECISE (low).

**7. Doctrine 10 ("tacit-agreement-inference") and Doctrine 1 ("conspiracy-agreement") — DUPLICATE**
- Both concern how agreement can be inferred from conduct. Doctrine 1 rule: "agreement need not be express and can be inferred from coordinated conduct." Doctrine 10 rule: "Agreement can be inferred from parallel conduct when each party knew concerted action was contemplated and invited."
- The chapter does not treat these as separate doctrines; it discusses *Interstate Circuit* as part of the agreement chapter. The Opus map is over-splitting a single doctrine (inferring agreement) into two. The chapter presents *Interstate Circuit* as applying the same agreement-inference doctrine, not a distinct "tacit agreement" doctrine.
- Severity: DUPLICATE.

**8. Doctrine 9 ("single-vs-multiple-conspiracies") lines — IMPRECISE**
- Opus Lines: `[[315, 317], [346, 391]]`. The section runs to line 391 in the chapter (which includes the discussion questions at lines 387–391). But the *Alvarez* note (lines 379–386) is listed under this doctrine. The chapter's introduction (lines 315–317) presents *Alvarez* as the third case in a sequence about inferring agreement, not specifically about single vs. multiple conspiracies. Assigning the Alvarez note primarily to single-vs-multiple is a stretch.
- Severity: IMPRECISE.

**9. *Krulewitch* doctrine assignment — IMPRECISE**
- Opus assigns *Krulewitch* to [single-vs-multiple-conspiracies]. The chapter uses *Krulewitch* for the point about guilt by association in conspiracy trials — a general prejudice concern, not specifically about the single/multiple conspiracy question.
- Severity: IMPRECISE.

**10. Doctrine 14 ("corporate-conspiracy") — IMPRECISE rule**
- Opus Rule: "Corporations can be charged with conspiracy because they act through their agents... however, conspiracy charges against corporate executives remain rare and often result in penalties disproportionate to harm."
- Chapter (line 411): "conspiracy charges against corporations and their executives remain surprisingly rare, and when they do occur, the resulting penalties often seem disproportionate to the harm caused." The chapter is describing penalties as disproportionately *small* (the penalties seem insufficient given the harm). Opus's phrasing "disproportionate to harm" is ambiguous and could be read either way.
- Severity: IMPRECISE (minor ambiguity).

**11. Doctrine 16 ("conspiracy-withdrawal") Split — ERROR**
- Opus Split: "Traditional approach requires affirmative steps to thwart the conspiracy plus communication; MPC allows withdrawal to terminate future liability more easily."
- Chapter comparison table (line 480): "Withdrawal | Affirmative steps to defeat conspiracy + communication to coconspirators | Withdrawal terminates future liability." This matches Opus's framing. However, the chapter does not say the MPC "allows withdrawal... more easily" in any further developed way. The chapter's note on the MPC at line 302–305 does not discuss withdrawal at all; only the table mentions it. There is nothing in the chapter establishing that the MPC is more lenient on withdrawal than the traditional rule — the table entry just says "Withdrawal terminates future liability" without comparison. The Opus split claim about MPC leniency goes beyond what the chapter supports.
- Severity: IMPRECISE (minor elaboration beyond chapter).

### Missing Content

**12. *Falcone* — present but brief**
- *United States v. Falcone* (line 172) appears in the chapter and Opus includes it. Accurate.

**13. Purdue Pharma executive names — PRESENT in chapter, not in Opus map**
- The chapter (line 431) names the three 2007 executives: Michael Friedman (President), Howard Udell (General Counsel), Paul Goldenheim (Chief Scientific Officer). Opus's Purdue entry (lines 362–364) omits these names. This is a completeness issue, not an error, but represents detail that could matter for exam questions about individual liability.
- Severity: not an error; noted for completeness.

---

## SONNET MAP VERIFICATION

### Case Claims

**1. *State v. Pond* line range — IMPRECISE**
- Sonnet Case entry, Lines: `[78, 131]`. The chapter's *Pond* case section begins at line 79 (the case title header) and ends at line 132. Line 78 is a blank line following the section introduction. This is a 1-line off-by-one.
- Severity: IMPRECISE (trivial).

**2. *Interstate Circuit* holding — ACCURATE**
- Sonnet holding (lines 342–344): "An inference of agreement among competing distributors can be drawn when each party knew all others were being asked to join a coordinated scheme and each adhered to the scheme with knowledge that concerted action was contemplated, even without direct evidence of an agreement among themselves." This closely tracks the chapter's language at line 341.

**3. *Pinkerton* lines — IMPRECISE**
- Sonnet Case entry, Lines: `[246, 281]`. The case section begins at line 247 (the case title header). Line 246 is a blank line before the header. One-line off-by-one.
- Severity: IMPRECISE (trivial).

**4. *Alvarez* lines — IMPRECISE**
- Sonnet Case entry, Lines: `[379, 385]`. The Alvarez note ends at line 385 (the dissent quotation). But lines 387–391 contain discussion questions tied directly to the Alvarez note. The Sonnet map's blocks table (line 439) separately lists `[379, 391]` for the Alvarez block, so this is an inconsistency within the Sonnet map rather than a chapter error.
- Severity: IMPRECISE (internal inconsistency).

**5. *Valigura* holding — ACCURATE**
- Sonnet (lines 372–374): "The unilateral conspiracy theory does not further the public policy concern of preventing group criminal activity; a conspiracy charge was dismissed where the only co-conspirator was an undercover agent." Chapter line 73–74: "the unilateral theory 'does nothing to further the public policy concern of preventing group criminal activity.' *United States v. Valigura*, 54 M.J. 187 (C.A.A.F. 2000)." Accurate.

**6. *Pacheco* lines — IMPRECISE**
- Sonnet Case entry, Lines: `[66, 66]`. Chapter line 67: "*State v. Pacheco*, 882 P.2d 183 (Wash. 1994)." Line 66 contains "Traditional jurisdictions take a *bilateral* approach..." and *Pacheco* is cited at the end of that sentence on line 67. Off by one.
- Severity: IMPRECISE (trivial).

### Doctrine Claims

**7. Doctrine 5 ("bilateral-unilateral-conspiracy") Split field — IMPRECISE**
- Sonnet Split: "Traditional jurisdictions follow the bilateral rule; the MPC and a majority of reformed state codes adopt unilateral; **federal circuits mostly follow bilateral for completed conspiracy but allow unilateral in attempt-to-conspire**."
- The chapter does not mention or support the claim about federal circuits distinguishing "completed conspiracy" from "attempt-to-conspire" (lines 63–74). This distinction is not found in the chapter text.
- Severity: IMPRECISE (elaboration not supported by chapter).

**8. Doctrine 6 ("overt-act-requirement") Split field — IMPRECISE**
- Sonnet Split: "Federal law (18 U.S.C. § 371) requires an overt act; the MPC requires an overt act only for lower-grade felonies and misdemeanors; **the common law historically did not require an overt act**."
- The chapter does not address the common law historical rule on overt acts. The claim about common law not requiring an overt act is not found in or supported by the chapter.
- Severity: IMPRECISE (claim beyond chapter scope — could be accurate law but is not sourced from this chapter).

**9. Doctrine 6 ("overt-act-requirement") Lines — ERROR**
- Sonnet Lines: `[[37, 60], [43, 52]]`. These two ranges overlap. Range `[43, 52]` is entirely within range `[37, 60]`. This is a formatting error; the second range appears to be an erroneous duplicate sub-range.
- Severity: ERROR (formatting/structural error).

**10. Doctrine 15 ("conspiracy-drug-quantity-mandatory-minimums") — IMPRECISE**
- Sonnet Split: "Some courts limit quantity attribution to reasonably foreseeable quantities; others apply strict Pinkerton-style total attribution."
- The chapter does not describe this as a doctrinal split between courts. The chapter (lines 441–459) presents quantity attribution as a consequence of conspiracy doctrine without identifying a circuit split on how to apply it.
- Severity: IMPRECISE (presents an undescribed split as a known doctrinal divergence).

**11. Doctrine 18 ("conspiracy-mpc-merger-no-cumulative-punishment") Cases — IMPRECISE**
- Sonnet Cases: "MPC comparison table (lines 472–481)." The comparison table in the chapter is at lines 472–485 (the table header, rows, and closing latex environment). Line 472 is the table caption/start. Citing a table as a "case" is an unusual entry but not factually wrong.
- Severity: IMPRECISE (table cited as a case reference).

**12. Doctrine 19 ("civil-asset-forfeiture-conspiracy-incentive") — HALLUCINATION (partial)**
- Sonnet Rule includes: "the federal Equitable Sharing Program permits local agencies to transfer seizures to federal authorities and receive up to 80% of proceeds back, bypassing state-law restrictions."
- Chapter (line 507): "The federal Equitable Sharing Program allows local agencies to transfer seized assets to federal authorities for forfeiture under more permissive federal law, then receive **up to 80%** of the proceeds back." This is accurate.
- No hallucination here. Withdraw finding.

**13. Doctrine 2 ("conspiracy-mens-rea-purpose") Levers — IMPRECISE**
- Sonnet Levers include: "Whether the defendant had a financial stake in the criminal enterprise; whether the defendant took steps beyond a routine commercial transaction; whether the crime is of an aggravated or serious nature."
- These levers are drawn from *Lauria*, not from the general purpose/knowledge distinction. The general purpose requirement (lines 58–60) does not cite financial stakes or aggravated crime nature as levers for the mens rea question. These *Lauria*-specific levers are imported into a doctrine that is supposed to be about the general conspiracy purpose requirement.
- Severity: IMPRECISE (conflates *Lauria* supplier context with general mens rea rule).

**14. Doctrines 2 and 4 — DUPLICATE**
- Doctrine 2 ("conspiracy-mens-rea-purpose") Rule: "Conspiracy requires the defendant to act with *purpose* — not merely knowledge — that the object crime be committed."
- Doctrine 4 ("lauria-supplier-intent-inference") Rule: "A supplier... can be held as a conspirator only if intent to participate is shown by: (1) direct evidence of intent, (2) a special interest... or (3) the aggravated nature of the crime."
- Both address knowledge vs. purpose for conspiracy liability. While *Lauria* is a specific application, the chapter presents it as the primary vehicle for the knowledge/purpose distinction (lines 146–149 introduce *Lauria* as illustrating this very question). The chapter treats *Lauria* as the leading case for conspiracy mens rea in the supplier context, but the two doctrines do overlap significantly and could be confusing to students.
- Severity: IMPRECISE (over-splitting; related but the specific supplier context makes the split defensible).

### Missing Content

**15. *Falcone* — present in chapter, absent from Sonnet cases list**
- *United States v. Falcone* appears at line 172 of the chapter. The Sonnet map does not list it as a case. The Sonnet doctrine 4 rule references "stake in the venture" but does not cite *Falcone*.
- Severity: IMPRECISE (missing case).

---

## CROSS-MAP ISSUES: CONTENT MISSED BY ALL THREE MAPS

**1. *Krulewitch v. United States* — MISSING from Gemini and Sonnet**
- Chapter lines 487–489 quote Justice Jackson's concurrence in *Krulewitch v. United States*, 336 U.S. 440, 453 (1949) on the dangers of guilt by association in conspiracy trials. Opus correctly identifies this case. Gemini and Sonnet omit it entirely.
- Gemini and Sonnet: IMPRECISE (missing content).

**2. *United States v. Falcone* — MISSING from Sonnet**
- Cited at chapter line 172 for the "stake in the venture" standard. Opus and Gemini include it. Sonnet omits it.

**3. The Purdue Pharma comparison table (lines 216–229)**
- The chapter includes an explicit comparison table: "Lauria Applied: Silk Road vs. Social Media." All three maps mention this discussion in their blocks tables, so they capture it. No issue.

**4. Conspiracy statistics**
- Chapter lines 5, 445–449 contain empirical data: "More than one-quarter of all federal criminal prosecutions involve conspiracy charges"; "the DEA alone maintained over 18,000 active informants between 2010 and 2015, paying more than $237 million"; racial disparity statistics ("at least 91% of defendants convicted in ATF reverse-sting operations were racial or ethnic minorities"). These policy/empirical facts appear in the chapter but are not captured as doctrine or case facts in any of the three maps. All three maps address the policy sections in their blocks tables but do not extract the specific statistics as levers. This is expected for map format but noted.

---

## SUMMARY TABLE

| Error Type | Gemini | Opus | Sonnet |
|------------|--------|------|--------|
| HALLUCINATION | 1 | 0 | 0 |
| ERROR | 1 | 0 | 1 |
| IMPRECISE | 6 | 7 | 8 |
| DUPLICATE | 1 | 1 | 1 |
| **TOTAL** | **9** | **8** | **10** |

### Error Detail by Map

**Gemini (9 issues)**
1. HALLUCINATION — "chain-conspiracy" doctrine invented and misapplied to *Interstate Circuit*
2. ERROR — *Interstate Circuit* labeled as vertical chain conspiracy; it is a horizontal parallelism case
3. IMPRECISE — Alvarez facts: "help unload a plane" conflates his role
4. IMPRECISE — Pinkerton prison detail presented as majority holding when it comes from the dissent
5. IMPRECISE — "tax laws" description for Pinkerton (minor)
6. IMPRECISE — Blocks table assigns Purdue Pharma section to inferring-agreement doctrine
7. IMPRECISE — Withdrawal line format malformed (three integers in one array)
8. IMPRECISE — Markel block listed as lines 9–32 when section ends at 31
9. DUPLICATE — Doctrines 2 (conspiracy-mens-rea-purpose) and 5 (intent-to-target-elements) are close but the chapter treats them as distinct questions

**Opus (8 issues)**
1. IMPRECISE — Pinkerton prison detail presented as uncontested fact; only in the dissent
2. IMPRECISE — *Krulewitch* assigned to single-vs-multiple-conspiracies; chapter uses it for general trial prejudice
3. IMPRECISE — Doctrine 9 assigns *Alvarez* note to single-vs-multiple; chapter presents it as an agreement-inference case
4. IMPRECISE — Doctrine 10 tacit-agreement-inference assigned to *Interstate Circuit*; chapter does not distinguish this as a separate doctrine from agreement-inference
5. IMPRECISE — Doctrine 1 Split claims "MPC requires actual agreement" which appears only in the comparison table, not as a developed textual rule
6. IMPRECISE — Doctrine 16 withdrawal split claims MPC is "more lenient" — goes beyond chapter
7. IMPRECISE — Doctrine 14 corporate conspiracy "disproportionate to harm" is ambiguous
8. DUPLICATE — Doctrines 1 (conspiracy-agreement) and 10 (tacit-agreement-inference) both address inferring agreement from conduct

**Sonnet (10 issues)**
1. ERROR — Doctrine 6 lines `[[37, 60], [43, 52]]` is structurally invalid (second range entirely within first)
2. IMPRECISE — Doctrine 5 Split claims federal circuits distinguish completed conspiracy from attempt-to-conspire; not in chapter
3. IMPRECISE — Doctrine 6 Split claims common law historically did not require overt act; not in chapter
4. IMPRECISE — Doctrine 15 Split presents quantity attribution as a known circuit split; chapter does not describe it that way
5. IMPRECISE — Doctrine 2 Levers import *Lauria* factors into the general purpose-requirement doctrine
6. IMPRECISE — *State v. Pond* case entry lines off by one (78 vs. 79)
7. IMPRECISE — *Pinkerton* case entry lines off by one (246 vs. 247)
8. IMPRECISE — *Alvarez* case entry line range (379–385) inconsistent with blocks table (379–391)
9. IMPRECISE — *Falcone* missing from cases list
10. DUPLICATE — Doctrines 2 (conspiracy-mens-rea-purpose) and 4 (lauria-supplier-intent-inference) overlap significantly on the knowledge/purpose distinction

---

## KEY FINDINGS

1. **Gemini's most serious error** is the "chain-conspiracy" doctrine (#11 in its doctrine list). This doctrine does not exist in the chapter by that name, and *Interstate Circuit* is a horizontal-parallelism case, not a vertical chain case. A student learning from this map would have a fundamentally incorrect understanding of what *Interstate Circuit* stands for.

2. **All three maps** have the Pinkerton facts slightly wrong in the same direction: the prison detail (Daniel being incarcerated when Walter committed the crimes) appears only in the Rutledge dissent, not the majority. All three maps treat it as an uncontested fact of the case rather than the dissent's framing.

3. **Sonnet map has the most line-number errors** (off-by-ones in four case entries) and one structural error in a line range. These are mechanical, not substantive.

4. **Opus is the most accurate** map overall, with no hallucinations and no outright errors. Its issues are primarily over-splitting (tacit-agreement-inference as a separate doctrine) and minor imprecisions.

5. **All three maps** omit *Krulewitch v. United States* (Gemini, Sonnet) or misclassify it (Opus). This case is used for an important systemic critique of conspiracy trials and could generate exam questions about the dangers of guilt by association.
