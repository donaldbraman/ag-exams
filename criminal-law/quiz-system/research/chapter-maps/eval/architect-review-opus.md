# Exam Architect Review: Chapter 19 Map (sonnet-markdown)

**Reviewer role:** Exam architect agent designing multi-question fact-pattern exam problems
**Map evaluated:** chapter-19-sonnet-markdown.md
**Source chapter:** 19-conspiracy.qmd

---

## A. Can I Design the Fact Pattern?

**Verdict: Yes, with high confidence.**

The map gives me what I need to construct a rich, multi-paragraph scenario. Specifically:

1. **Doctrines section provides the building blocks.** The 19 doctrine entries each contain a rule statement precise enough to build around. For example, doctrine #4 (lauria-supplier-intent-inference) gives me the three-prong test (direct evidence, special interest, aggravated crime) -- I can design a fact pattern that implicates all three prongs at different levels of strength.

2. **Levers are the best feature for exam design.** The "Levers" field in each doctrine tells me exactly which factual dials to turn. For conspiracy-agreement-element, the levers are: innocent explanation, communication patterns linked to criminal events, financial flows, knowledge of others joining. I can set each lever to a different position across my three questions, creating genuine ambiguity. This is exactly the data an exam architect needs.

3. **Hypo seeds provide scenario scaffolding.** The three seeds per doctrine give me concrete starting points. The encrypted-messages-spiking-around-fraud-dates seed (doctrine #1) and the web-hosting-provider-at-10x-rates seed (doctrine #4) could be combined into a single fact pattern about a tech company whose employees coordinate through encrypted channels while a third-party service provider profits from the arrangement. The seeds are specific enough to be useful but general enough that I would not be repeating a classroom exercise verbatim.

4. **Cross-chapter links help me plant secondary issues.** Doctrine #7 (pinkerton-vicarious-liability) links to accomplice-liability (Ch. 18), and doctrine #1 links to substantial-step-test (Ch. 17). This tells me I can embed an attempt or accomplice issue in the fact pattern and it would be fair game -- students have seen these connections.

**What is missing:**

- **No character archetypes or role taxonomy.** For a conspiracy fact pattern, I need to assign roles: ringleader, peripheral member, supplier, buyer, unwitting participant, government agent. The map does not organize its doctrines by the *role* each doctrine most naturally tests. I can infer this (Lauria tests the supplier, Pinkerton tests the peripheral member, bilateral/unilateral tests the target of a sting), but a "Roles Tested" field on each doctrine would save inference time and reduce the chance I misalign the fact pattern.

- **No indication of which doctrines pair well together in a single fact pattern.** Doctrines #1 (agreement), #4 (Lauria supplier), and #7 (Pinkerton) naturally compose into a single scenario (a supplier who is arguably part of a conspiracy whose members commit foreseeable crimes). But nothing in the map tells me which doctrines are compositionally compatible. A "Composes With" field linking doctrines that can coexist in one scenario would be valuable.

---

## B. Can I Design the Questions?

**Verdict: Yes. The traps are the most valuable field for question design.**

1. **Traps map directly to wrong-answer construction.** Each trap follows the pattern: "Students say X because they confuse Y with Z." This is a ready-made distractor for multiple-choice questions and a ready-made "common error" for issue-spotter grading rubrics. For example, trap #2 (conspiracy-mens-rea-purpose): "Students say knowledge of criminal use is enough because they confuse knowledge with purpose." I can write a question where the most tempting wrong answer is "guilty of conspiracy because he knew about the criminal use" and the correct answer requires distinguishing knowledge from purpose under Lauria.

2. **Rules are precise enough for grading rubrics.** The rule statements are formulated as legal standards with the key terms italicized or explicitly defined. The Pinkerton rule statement includes the three limiting conditions (in furtherance, reasonably foreseeable, no withdrawal) -- these become the required elements a student must address.

3. **Exam lens field is useful but underspecified.** The "prosecution" / "defense" / "both" tag tells me which side the doctrine naturally advantages. This helps me frame questions: "Evaluate the strongest argument the defense can make" versus "What must the prosecution prove?" But the field does not tell me *why* the doctrine favors that side, which would help me calibrate difficulty.

**What is missing:**

- **No difficulty rating.** Doctrine #6 (overt-act-requirement) is relatively straightforward -- students mostly get this right. Doctrine #3 (specific-intent-to-all-elements, the Pond issue) is genuinely tricky because students resist the idea that conspiracy imposes a *higher* mental state than the completed crime. I need to know which doctrines are hard so I can calibrate the exam to test both baseline competence and advanced analysis. A difficulty rating (e.g., 1-3 scale, or "foundational" / "intermediate" / "advanced") would help.

- **No "threshold vs. nuanced" distinction.** Some doctrines have bright-line rules (overt act: any act suffices). Others have multi-factor balancing tests (Lauria: three inference prongs). The former are good for testing whether students know the rule; the latter are good for testing whether students can apply it. The map does not flag this distinction.

- **No model answer sketches or key phrases.** When I write a grading rubric, I need to know what a correct answer looks like. The map gives me the rule, but not the *application* -- what a student should say when the facts are ambiguous. Even a one-sentence model application per doctrine ("A strong answer would note that X but distinguish Y") would improve rubric generation.

---

## C. Can I Ensure Coverage?

**Verdict: Mostly yes, but the block-count data is not useful for this purpose.**

1. **Doctrine count is the right unit for coverage.** With 19 doctrines, I know I cannot test all of them in 3 questions. The exam lens field lets me filter: 5 are prosecution-only, 7 are defense-only, 7 are both. If I want balanced coverage, I should pick one from each camp.

2. **Cross-chapter links are valuable.** The links to Ch. 17 (attempt/substantial step) and Ch. 18 (accomplice liability) tell me what prior material I can expect students to integrate. This lets me write a fact pattern that rewards students who connect conspiracy to adjacent doctrines.

3. **Block count is noise for exam design.** The fact that doctrine #1 spans 2 blocks and doctrine #3 spans 1 block tells me about the *chapter's* allocation of space, not the doctrine's importance for exam purposes. I do not need to know how many paragraphs the textbook devotes to a doctrine to decide whether to test it. What I would want instead is a *pedagogical weight* field: how central is this doctrine to the course learning objectives?

4. **Line numbers are irrelevant to exam design.** The "Lines" field on each doctrine and in the Blocks table points back to the source chapter. As an exam architect, I never need to look up line 315 in the .qmd file. These are useful for provenance/verification but are pure noise for my role.

---

## D. Can I Avoid Repeating Class Exercises?

**Verdict: Partially. The hypo seeds show what students have *seen*, but not what they have *practiced*.**

1. **The Hypo Seeds table at the bottom is good.** It aggregates all seeds with their line references and brief descriptions. I can scan this to see what scenarios students have already encountered. The "Note" column sometimes explains the pedagogical purpose ("Directly modeled on Markel case; students should apply circumstantial inference doctrine"), which is helpful.

2. **But hypo seeds conflate two things:** (a) hypotheticals posed as discussion questions in the chapter text, and (b) new seeds generated by the map-building process for potential exam use. Looking at the data, some seeds are clearly drawn from the chapter's own "Discussion Questions" callout boxes (e.g., the Purdue Pharma application of Lauria, the bank robbery Pinkerton hypothetical). Others appear to be newly generated (the encrypted-messages seed, the web-hosting seed). I cannot reliably distinguish which ones students have actually discussed in class.

**What is missing:**

- **A "source" field on each hypo seed.** Mark each seed as either "chapter-exercise" (appears in the text as a discussion question or callout) or "generated" (created by the map builder for exam inspiration). This is the single most important missing field for avoiding repetition. Without it, I risk either (a) recycling a classroom exercise verbatim or (b) being overly cautious and avoiding good scenarios that were actually never discussed.

- **No indication of whether hypos were actually assigned or discussed.** A chapter may contain 8 discussion questions, but the instructor may only have used 3 in class. The map cannot capture this (it is runtime information, not chapter information), but flagging this as a gap in the pipeline would be useful -- perhaps the exam architect should receive a supplementary "class session log" alongside the map.

---

## E. What Would I Add?

1. **Difficulty rating per doctrine.** Scale of 1-3 or "foundational / intermediate / advanced." Essential for calibrating a 3-question exam that tests across difficulty levels.

2. **"Composes With" field per doctrine.** Which other doctrines in this chapter naturally co-occur in a single fact pattern? Example: agreement-element composes with single-vs-multiple-conspiracies composes with procedural-advantages. This would dramatically accelerate fact-pattern construction.

3. **Source tag on hypo seeds.** "chapter-exercise" vs. "generated" -- critical for avoiding repetition.

4. **Role taxonomy.** For each doctrine, which conspiratorial role does it most naturally test? (ringleader, peripheral member, supplier, buyer, unwitting participant, undercover target). This helps me assign character roles in the fact pattern.

5. **Key distinguishing facts.** For each doctrine, what single factual change flips the outcome? Example: for Lauria, the flip is "charges inflated prices" vs. "charges standard rates." This is partially captured by levers, but the levers list multiple factors without identifying the decisive one.

6. **Doctrine interaction warnings.** Where two doctrines create tension or apparent contradiction when combined. Example: Pinkerton (broad vicarious liability) vs. MPC rejection (narrow accomplice-only liability) -- a fact pattern set in an MPC jurisdiction negates Pinkerton issues entirely. The map should flag which doctrines are jurisdiction-dependent and which are universal.

---

## F. What Would I Remove?

1. **Line numbers.** The "Lines" field on doctrines and the entire "Blocks" table exist for provenance and verification. They are valuable for the map-building pipeline (to trace claims back to source text) but are pure noise for exam design. I would move them to a separate "provenance" section or a companion file, keeping the main map lean.

2. **Block count.** As noted above, the number of text blocks a doctrine occupies in the chapter does not inform exam design. Remove or relocate.

3. **Source hash and model metadata.** The "Meta" section's source hash and model name are pipeline metadata, not exam-design inputs. These belong in a header comment or companion metadata file.

4. **Statutes table.** The statutes are already embedded in the doctrine rule statements where relevant (e.g., "18 U.S.C. Section 371 requires an overt act"). A separate table listing them with line numbers adds nothing I would use. If statute text is needed, it should be inlined in the doctrine rule statement itself.

---

## G. What Would I Restructure?

1. **Group doctrines by exam-design function, not by chapter order.** The current ordering (1-19) follows the chapter's expository sequence. For exam design, I would prefer grouping by function:
   - **Core elements** (agreement, mens rea, overt act) -- the building blocks of any conspiracy question
   - **Scope doctrines** (single vs. multiple, Pinkerton, MPC rejection, withdrawal) -- how far liability extends
   - **Special contexts** (Lauria supplier, buyer-seller, bilateral/unilateral, Wharton's, Gebardi) -- situational modifiers
   - **Policy/systemic** (drug quantity, manufactured conspiracy, forfeiture, corporate liability, MPC merger) -- policy-layer issues

   This grouping would let me quickly pick one doctrine from each tier to ensure the exam tests elements, scope, and application.

2. **Merge the two hypo-seed locations.** Currently, seeds appear twice: once inline under each doctrine, and again aggregated in the "Hypo Seeds" table at the bottom. The bottom table adds "Note" and reformulated "Description" fields that the inline seeds lack. Pick one location and enrich it. I would keep the bottom table (scannable, has notes) and remove the inline seeds, replacing them with a cross-reference like "Seeds: see #1, #2, #3 in Hypo Seeds table."

3. **Elevate the Cases section into a lookup table keyed by doctrine.** The current Cases section repeats information already in the doctrine entries (which cases go with which doctrine). Instead of a flat list of cases, I would want a cross-reference matrix: rows = doctrines, columns = cases, cells = role of case (establishes rule / illustrates application / provides counterpoint). This would let me quickly see which cases a student needs to know for each doctrine and design questions that test case application.

4. **Add an "Exam Blueprint" summary section at the top.** Before the detailed doctrines, I would want a 5-line summary: total doctrine count, difficulty distribution, recommended coverage for a 3-question exam (e.g., "test at minimum: one core-element doctrine, one scope doctrine, one special-context doctrine"), and a list of the 3-4 highest-value doctrine clusters for fact-pattern integration.

---

## Summary Assessment

The chapter map is a strong foundation for exam design. The doctrine entries with their rule/split/levers/traps structure provide roughly 80% of what I need. The traps field is exceptionally well designed for generating wrong answers and grading rubrics. The levers field is the key input for constructing ambiguous fact patterns.

The main gaps are:

| Gap | Impact | Fix Effort |
|-----|--------|------------|
| No difficulty rating | High -- cannot calibrate exam difficulty | Low (add 1 field per doctrine) |
| No "composes with" links | High -- slows fact-pattern construction | Medium (requires editorial judgment) |
| No source tag on hypo seeds | High -- risk of repeating class exercises | Low (add 1 field per seed) |
| Line numbers / block counts as noise | Low -- just clutters the view | Low (move to appendix) |
| No role taxonomy | Medium -- must infer character assignments | Low (add 1 field per doctrine) |
| No exam blueprint summary | Medium -- must read all 19 doctrines before planning | Medium (requires synthesis) |

The format works. With the additions above, it would be excellent.
