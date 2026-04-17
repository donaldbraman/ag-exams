# Chapter Map Extraction Prompt (v2)

You are analyzing a criminal law casebook chapter to produce a structured chapter map for exam generation. The map catalogs every testable doctrine, case holding, factual lever, student trap, and exam-design metadata.

## Inputs

1. The chapter text, with line numbers prepended to each line.
2. The class slides for this chapter (if provided). These show what students have already practiced.

## What counts as a doctrine

A **doctrine** is a testable legal question — a rule, standard, test, or distinction that a student could get right or wrong on an exam.

**Not doctrines:** background policy discussion, historical context, biographical facts about cases, or pedagogical framing — unless they contain an embedded testable rule.

**Doctrine identification tests** (apply all four):
1. **Meta-doctrine test:** When the chapter compares two frameworks (e.g., common law vs. MPC), that comparison is itself a testable doctrine.
2. **Institutional-application test:** When a general concept is applied to a specific context and the context changes the analysis, that's a separate doctrine.
3. **Policy-embedded-rule test:** When a policy discussion contains a testable legal rule, extract the rule. Skip the policy.
4. **Consolidation test:** If two potential doctrines always appear together and testing one necessarily tests the other, consolidate them.

**Target:** 12–20 doctrines per chapter.

## Output format

Produce well-structured **markdown** (not JSON). Follow this structure exactly:

```markdown
# Chapter Map: [Title]

## Meta
- Chapter: N
- Title: ...
- Source file: ...
- Source hash: ...
- Generated at: [ISO date]
- Model: ...

## Doctrine Clusters

Group doctrines that naturally travel together in a fact pattern. A cluster is a set of 2-5 doctrines that a single exam scenario could test simultaneously.

### Cluster: [descriptive-name]
- **Doctrines:** [list of doctrine keys]
- **Why they cluster:** [one sentence explaining why these doctrines co-occur in a realistic scenario]
- **Sample scenario hook:** [one sentence describing a fact pattern that would engage all doctrines in this cluster]

## Doctrines

### 1. kebab-case-key
- **Rule:** [One sentence stating the testable legal rule.]
- **Split:** [Where jurisdictions disagree, or null.]
- **Difficulty:** [foundational | intermediate | advanced]
- **Levers:** [concrete factual variables that change the outcome]
- **Traps:** Students [choose X] because [they confuse Y with Z].
- **Cases:** [case names as they appear in the chapter]
- **Lines:** [[start, end], ...]
- **Block count:** N
- **Cross-chapter:** [doctrine-key (Ch. N)]
- **Exam lens:** prosecution | defense | both
- **Hypo seeds:**
  - [fact pattern idea] — **[novel]** or **[practiced: slide N]**
  - ...

## Cases

### Case Name
- **Lines:** [start, end]
- **Holding:** [one sentence]
- **Reasoning:** [one sentence — WHY the court reached this holding]
- **Facts:** [one sentence]
- **Doctrines:** [doctrine keys]

## Statutes

### Citation
- **Lines:** [start, end]

## Blocks

| Lines | Type | Doctrines | Summary |
|-------|------|-----------|---------|
| ... | case / doctrine-exposition / hypothetical / statute / introduction / policy | ... | ... |

## Hypo Seeds

| Doctrines | Description | Source | Note |
|-----------|-------------|-------|------|
| ... | ... | novel / practiced (slide N) / chapter-exercise (line N) | ... |
```

## Key requirements

- **kebab-case keys** for all doctrine keys
- **Line numbers must be accurate.** Verify by checking content at those lines.
- **Trap format is mandatory:** "Students [choose X] because [they confuse Y with Z]."
- **Block coverage:** Every substantive line should appear in at least one block.
- **Cross-chapter links:** Only include links based on explicit cross-references in the chapter text.
- **Hypo seeds:** 2-3 per doctrine minimum. Tag each as:
  - **novel** — not practiced in class (safe for exam)
  - **practiced: slide N** — appears in class slides (vary facts for exam)
  - **chapter-exercise: line N** — appears in chapter discussion questions (vary facts for exam)
- **Difficulty ratings:**
  - **foundational** — core rule that every student must know (e.g., elements of conspiracy)
  - **intermediate** — requires applying a rule to ambiguous facts or distinguishing frameworks
  - **advanced** — requires synthesizing multiple doctrines, recognizing a split, or spotting a policy-embedded rule
- **Doctrine clusters:** Group doctrines that would naturally appear together in a multi-question exam fact pattern. Every doctrine should appear in at least one cluster. Clusters help the exam architect design integrated scenarios rather than testing doctrines in isolation.

## Chapter text

**Chapter {chapter_number}: {chapter_title}**
**Source file:** {source_file}
**Source hash:** {source_hash}

```
{numbered_chapter_text}
```

{slides_section}

Produce the chapter map now in markdown. Be thorough: list every doctrine, case, statute, block, and hypo seed.
