# Exam Architect Review: Chapter 19 Sonnet Markdown Map

**Reviewer role:** Exam architect designing multi-question fact-pattern problems
**Map evaluated:** chapter-19-sonnet-markdown.md
**Chapter:** 19 — Conspiracy
**Date:** 2026-04-14

---

## Overall Assessment

This is a strong knowledge layer for exam design. The doctrine-rule-trap-lever-hypo seed structure gives an architect most of what she needs to build multi-issue fact patterns without referencing the source chapter. The main gaps are at the *coordination* level: the map tells me what each doctrine is but gives me limited help deciding which doctrines to pair, what the natural progression of issues is within a single fact pattern, or how hard each doctrine is to resolve. Those are exam architecture decisions, not writing decisions, and the map currently doesn't support them well.

---

## A. Can You Design the Fact Pattern?

**Yes, with moderate effort.**

The hypo seeds are the most immediately useful feature. They are concrete, modern, and varied — web hosting providers, rideshare drivers, drug stings, pharmaceutical companies. Each seed isolates one variable cleanly, which is exactly what you want as a building block. The seeds for `conspiracy-agreement-element` (encrypted messages, silent presence, aware warehouse manager) and `lauria-supplier-intent-inference` (dark-web hosting at 10x rates, ad revenue as stake in venture) are detailed enough that I could expand either into a three-paragraph fact pattern with minimal invention.

The levers are equally useful for fact pattern design. They name the variables that move the legal outcome: whether the supplier had inflated prices, whether communication patterns track criminal events, whether the buyer extended credit. These let me set those variables deliberately — I can design a fact pattern that is close on the Lauria inference by setting ordinary fees but an aggravated crime, or close on the buyer-seller exception by adding fronting but no coded language.

**What's missing:**

The seeds are all single-doctrine. For a multi-question problem, I need to chain two or three doctrines through one fact pattern. Nothing in the map tells me which doctrines *naturally travel together* in a realistic scenario. I know from reading the chapter that agreement-inference, Pinkerton liability, and single-vs-multiple-conspiracies all appear in the Dan Markel narrative, but that connection is not surfaced in the map itself. An `exam combos` or `natural issue clusters` field would let me quickly identify, for example, that a drug distribution ring naturally raises agreement-inference, bilateral-unilateral, Pinkerton, buyer-seller, and drug quantity all at once — and that the first three are central issues while the last two are add-ons.

The fact pattern also needs a setting. The seeds suggest the setting (dark-web platform, pharmaceutical company, rideshare driver) but a multi-issue problem usually benefits from a unified realistic context. Nothing in the map helps me evaluate which settings are exam-ready versus too exotic or too similar to in-class exercises.

---

## B. Can You Design the Questions?

**Yes, largely.**

The traps field is the single most exam-useful field in the map. Each trap is written in the exact form of a student error: "Students say X because they confuse Y with Z." This is precisely the wrong answer I need to write for a multiple-choice distractor or the student mistake I need a short-answer question to expose. For example:

- Doctrine 2 trap: students say knowledge = purpose → distractor: "Lauria is guilty because he knew the women were using his service for prostitution."
- Doctrine 7 trap: students say peripheral conspirator needs direct participation → distractor: "The ringleader is not liable because he did not personally commit the robbery."
- Doctrine 14 trap: students confuse passive non-participation with affirmative withdrawal → distractor: "The conspirator effectively withdrew by moving to another state and not answering calls."

The rules are precise and well-stated. They tell me exactly what the prosecution must prove and what the defense can contest, which maps cleanly onto what question is worth asking.

The `exam lens` field (prosecution/defense/both) is genuinely useful. It tells me which questions should be framed as "can the prosecution prove X?" versus "does the defendant have a defense?" A prosecution-lens doctrine and a defense-lens doctrine pair naturally into a single two-question problem.

**What's missing:**

Difficulty level. All 19 doctrines look equal in the map, but they are not equal exam challenges. The distinction between knowledge and purpose in *Lauria* is harder for students than the bilateral/unilateral split, because the bilateral/unilateral rule is clearly stated while the Lauria inference requires weighing three independent factors. Without a difficulty signal, I might accidentally front-load an exam with five hard questions or make the last question too easy to discriminate.

The traps are all one per doctrine. Some doctrines have multiple common error patterns. For `pinkerton-vicarious-liability`, students also confuse the foreseeability limit with the furtherance requirement — that is a second trap that would generate a different distractor. A `secondary trap` field would capture this without cluttering the primary trap.

The cases section gives holdings and facts but not the reasoning step that is often what the exam question tests. For *Pond*, the exam question is usually not "what is the holding?" but "why does conspiracy require a higher mental state than the completed offense?" The map gives me the holding but not the reasoning chain I'd put in a model answer.

---

## C. Can You Ensure Coverage?

**Partially.**

The block counts are useful for identifying where the chapter spends its teaching time. Doctrines with block counts of 2 (agreement inference, mens rea purpose, bilateral/unilateral, overt act, Pinkerton vicarious liability, withdrawal) are the chapter's core teaching targets. Single-block doctrines are secondary. This lets me ensure my exam covers the 2-block doctrines and treats the 1-block doctrines as supporting or add-on questions.

The cross-chapter links help me avoid pretending a doctrine lives only in Chapter 19. `substantial-step-test (Ch. 17)` for the overt act requirement tells me students have already seen this comparison in the attempt chapter — that is a richer exam question because students can be asked to distinguish the two thresholds.

**What's missing:**

The block count is raw content volume, not exam weight. A doctrine can occupy one block and still be the hardest conceptual challenge in the chapter (see `conspiracy-specific-intent-target-elements`, block count 1, which is a genuinely difficult mens rea question). An `exam priority` field (core/secondary/enrichment) would be more useful than block count alone for balancing a problem set.

The blocks table at the bottom of the map is the most structurally informative part of the map, but it is not cross-referenced into the doctrine entries. I have to read the blocks table separately to see that agreement inference gets two major blocks (the Dan Markel narrative at lines 8-31 and the three-case sequence at lines 315-395) while Wharton's Rule gets one brief block. If the doctrine entry said "Primary teaching location: lines 319-395 (three-case agreement sequence)" I could immediately understand the pedagogical context, which shapes what the exam should test.

There is no coverage gap indicator. The map covers 19 doctrines, but does it cover everything in the chapter? I cannot tell from the map alone whether there are doctrines or arguments in the chapter that were not extracted. A `completeness confidence` field or a list of chapter sections not mapped to any doctrine would help me know whether there are blind spots.

---

## D. Can You Avoid Repeating Class Exercises?

**Weakly.**

The hypo seeds are fresh and original relative to the chapter's discussion questions, which is valuable. The seeds are set in modern contexts (dark-web platforms, rideshare drivers, fentanyl distribution) that are clearly different from the chapter's cases. That gives me confidence I can build from the seeds without replicating what students have already analyzed.

**What's missing:**

The map does not explicitly flag which hypo seeds, cases, or discussion problems students have worked in class. The chapter contains a *Pond* problem about the "no guns" robbery (lines 137-143 discussion questions) and a *Lauria* problem about social media platforms (lines 194-240). If I use a gun-in-robbery scenario or a platform-knowledge scenario on the exam, students will recognize the setup. The map captures the seeds but doesn't distinguish "seeds designed to be new" from "seeds that reprise in-class material."

A simple `source` tag on each hypo seed — either `original` (novel) or `chapter-variant` (close to in-class discussion) — would solve this. Right now I have to read the full chapter to check, which defeats the purpose of the map as a standalone exam-design layer.

The discussion questions in the chapter (the Markel application questions, the Pinkerton partnership-analogy questions, the Lauria social-media questions) are especially important to flag because professors routinely use them in Socratic dialog. Anything that appears in a discussion question block is functionally "practiced material" even if students never wrote a formal answer.

---

## E. What Would You ADD?

**1. Issue cluster field.** Which 2-4 doctrines travel together naturally in a single fact pattern? Example for `pinkerton-vicarious-liability`: `natural cluster: [conspiracy-agreement-element, conspiracy-withdrawal, pinkerton-mpc-rejection]`. This is the most important missing field for exam architecture because it eliminates the manual work of figuring out which doctrines compose well.

**2. Exam priority tag.** `core` / `secondary` / `enrichment` — separate from block count. Core doctrines anchor every exam; secondary doctrines appear as supporting questions; enrichment doctrines appear in bonus questions or policy problems. For this chapter: agreement inference, mens rea purpose, and Pinkerton are core; bilateral/unilateral and buyer-seller are secondary; Wharton's Rule and Gebardi are enrichment.

**3. Difficulty signal.** A simple 1-3 scale or a label like `clear-rule application` / `multi-factor balancing` / `competing-framework choice` would help me calibrate exam difficulty. *Pond* (specific intent to all elements) is a multi-factor balancing problem. Wharton's Rule is a clear-rule application. Lauria is a multi-factor balancing with three independent inference pathways.

**4. Practiced-in-class flag on hypo seeds.** A boolean or `class-exercise` / `novel` tag on each seed. This is a small addition but would save significant time when designing take-home or in-class problems.

**5. Key reasoning step.** One sentence (not just the holding) capturing the *why* that the exam question tests. For *Pond*: "The reasoning is that conspiracy is defined by the agreement to achieve a specific criminal result, so the conspirator must intend *that specific result* — a higher standard than the principal who may satisfy a lesser mental state by actually doing the act." This is what goes in the model answer and the grading rubric, and it is currently absent.

**6. Jurisdiction-sensitivity flag.** Several doctrines have outcomes that flip entirely between MPC and traditional jurisdictions (bilateral/unilateral, Pinkerton/MPC rejection, merger/cumulative punishment). The map notes splits, but it would be useful to have a `jurisdiction-sensitive: yes/no` flag that triggers a reminder to the question writer to specify the jurisdiction in the question stem.

**7. Chapter discussion question inventory.** A brief list of the questions students have already encountered in the chapter, so the exam architect knows what is off-limits without reading the full chapter. Format: `class-exercises: [Pond gun-in-robbery, Lauria social-media platform, Pinkerton bank-robbery hypothetical, Markel Sigfredo Garcia application]`.

---

## F. What Would You REMOVE?

**1. Source hash.** The SHA-style hash in the Meta section is useful for the pipeline (to detect when the source chapter changes and the map needs regeneration) but is noise for an exam architect. It should stay in the data layer but not render in a human-facing review format.

**2. Raw line numbers in doctrine entries.** The `Lines` field in each doctrine entry is useful for the build pipeline but creates visual clutter in an exam-design workflow. The blocks table at the bottom already provides a cleaner structural view. Line numbers in the per-doctrine entries could be collapsed into a `See blocks:` reference or moved to a metadata field not shown in the exam architect view.

**3. Statute entries as standalone section.** The statutes section (MPC § 5.03, 18 U.S.C. § 371, etc.) largely duplicates information already captured in the doctrine entries. For exam design, I care about the rule, not the statutory citation format. The statute section could be collapsed into doctrine cross-references rather than listed separately.

**4. Some duplicate hypo seed coverage.** Several hypo seeds across doctrines overlap significantly. The bilateral/unilateral seeds (undercover drug deal, unilateral jurisdiction) and the manufactured-conspiracy/sting seeds cover nearly identical scenarios. Consolidating would reduce noise without reducing coverage.

---

## G. What Would You RESTRUCTURE?

**1. Lead with the issue cluster map, not the individual doctrines.**

The current structure is: doctrine by doctrine in a flat list. For exam architecture, the more useful structure starts with a matrix of which doctrines combine into exam-ready issue clusters, then drops into individual doctrine detail as needed. Something like:

```
## Issue Clusters
| Cluster | Doctrines | Natural Fact Pattern Setting | Exam Priority |
|---------|-----------|------------------------------|---------------|
| Agreement inference chain | 1, 9, 10 | multi-defendant business or drug operation | core |
| Supplier liability spectrum | 2, 4, 13 | platform, pharmacy, or dealer context | core |
| Vicarious liability contrast | 7, 8 | co-conspirator commits unexpected crime | core |
| Manufactured conspiracy | 5, 15, 16 | government sting operation | secondary |
| Structural limits | 11, 12 | two-party offense or protected class | enrichment |
```

This would let me design a three-question problem in 10 minutes by picking a cluster, checking the individual doctrine entries for rules and traps, and drawing from the hypo seeds.

**2. Separate the policy-rich doctrines from the black-letter doctrines.**

Doctrines 15-19 (drug quantity mandatory minimums, manufactured conspiracy, corporate liability gap, MPC merger, civil asset forfeiture) are primarily policy analysis doctrines. They are important and well-mapped, but they are qualitatively different exam material from doctrines 1-14. A policy exam question looks different from a rule-application question, requires different grading rubrics, and should appear in a different part of an exam. Grouping doctrines into `black-letter` and `policy` sections — or tagging them — would make the map more directly actionable.

**3. Move the blocks table to the top, not the bottom.**

The blocks table is the best structural overview of the chapter. It shows the teaching sequence, the relative weight of each doctrine, and which blocks are cases versus exposition versus hypotheticals. Currently it appears at line 415, after all 19 doctrines, 9 cases, and 5 statutes. As the first thing an architect reads, it would immediately orient the exam design work: here is what the chapter teaches, in what order, with what emphasis.

**4. Consolidate the cases section with the doctrine entries.**

Currently the map has per-doctrine case citations and a separate cases section with fuller holdings and facts. For exam design, I want the case holding and key facts close to the doctrine rule, not in a separate section I have to cross-reference. The cases section as a standalone adds navigation overhead. A better structure embeds the one-sentence holding and key facts directly in the doctrine entry under a `key case` subfield, and reserves the separate cases section only for cases that are taught as primary readings (full opinion excerpts in the chapter) rather than note cases.

---

## Summary Table

| Evaluation Dimension | Rating | Key Finding |
|----------------------|--------|-------------|
| Fact pattern design | Strong | Levers and seeds provide excellent building blocks; no issue-cluster guidance |
| Question design | Strong | Traps map directly to distractors; missing difficulty signal and secondary traps |
| Coverage balance | Moderate | Block counts help but conflate volume with weight; no coverage gap indicator |
| Avoiding repetition | Weak | No class-exercise flags; requires reading full chapter to confirm novelty |
| Most valuable field | — | `traps` — immediately actionable for distractor writing |
| Highest-priority addition | — | `natural issue clusters` — eliminates main architect workflow gap |
| Highest-priority restructure | — | Lead with issue cluster matrix; move blocks table to top |
