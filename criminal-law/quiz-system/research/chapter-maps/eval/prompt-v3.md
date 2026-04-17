# Chapter Map Extraction Prompt (v3 — Progressive Doctrinal Summary)

You are analyzing a criminal law casebook chapter to produce a **progressive doctrinal summary** for exam generation. Unlike a flat catalog, this map follows the chapter's own pedagogical arc: it states the elements of the core doctrine in plain language, then shows how the chapter refines each element through cases, distinctions, and complications.

## Inputs

1. The chapter text, with line numbers prepended to each line.
2. The class slides for this chapter (if provided). These show what students have already practiced.

## What to produce

### 1. Elements (plain language)

State the core doctrine of the chapter in plain English. Break it into its elements — the parts a student would need to identify and analyze on an exam. Use the language a professor would use in class, not statutory language.

### 2. Refinements (in chapter order)

For each element, walk through how the chapter develops it. As the chapter introduces cases, distinctions, splits, or complications, summarize them **in the order the student encounters them**. This preserves the pedagogical structure.

For each refinement:
- **What the chapter teaches** — the rule, distinction, or complication in one or two sentences
- **The case or source** — what case (or statute, or hypothetical) introduces this point
- **The trap** — where students go wrong. Format: "Students [choose X] because [they confuse Y with Z]." Only include traps where a genuine exam mistake exists.
- **Difficulty** — foundational / intermediate / advanced

### 3. Clusters (exam design guidance)

Group refinements that would naturally appear together in a single exam fact pattern. Each cluster should name 2-5 refinements and provide a one-sentence scenario hook that would engage all of them. This helps the exam architect design integrated questions rather than testing points in isolation.

### 4. Cases (compact reference)

For each case in the chapter, provide:
- **Holding** — one sentence
- **Reasoning** — WHY the court reached this holding (one sentence)
- **Facts** — one sentence
- **Teaches** — which refinement(s) this case supports

## Output format

Produce well-structured **markdown**. Follow this structure:

```markdown
# Chapter Map: [Title]

## Meta
- Chapter: N
- Title: ...
- Source file: ...
- Source hash: ...
- Generated at: [ISO date]
- Model: ...

## Elements

[State the core doctrine in plain language. Break it into numbered elements. This is the skeleton the rest of the map hangs on.]

## Refinements

### [Element Name]

#### [refinement-key]: [Short Title]
- **Rule:** [What the chapter teaches — one or two sentences]
- **Source:** [Case name, statute, or "chapter hypothetical (line N)"]
- **Trap:** Students [choose X] because [they confuse Y with Z].
- **Difficulty:** foundational | intermediate | advanced

#### [refinement-key]: [Short Title]
...

### [Next Element Name]

#### [refinement-key]: [Short Title]
...

## Clusters

### [cluster-name]
- **Refinements:** [list of refinement keys]
- **Why they cluster:** [one sentence]
- **Scenario hook:** [one sentence fact pattern that engages all listed refinements]

## Cases

### [Case Name]
- **Holding:** ...
- **Reasoning:** ...
- **Facts:** ...
- **Teaches:** [refinement keys]
```

## Key requirements

- **kebab-case keys** for all refinement and cluster keys
- **Plain language** for elements — write as if explaining to a smart student, not quoting a statute
- **Chapter order** for refinements — follow the sequence the chapter uses
- **Trap format is mandatory:** "Students [choose X] because [they confuse Y with Z]." Only where a real exam mistake exists.
- **No clutter:** No line-range tables, no block coverage maps, no statutes section, no hypo seeds. The exam generator creates its own hypotheticals from this map.
- **Difficulty ratings:**
  - **foundational** — core rule every student must know
  - **intermediate** — requires applying a rule to ambiguous facts or distinguishing frameworks
  - **advanced** — requires synthesizing multiple doctrines, recognizing a split, or spotting a subtle distinction
- **Clusters:** Every refinement should appear in at least one cluster. Clusters help the exam architect design integrated scenarios.

## Chapter text

**Chapter {chapter_number}: {chapter_title}**
**Source file:** {source_file}
**Source hash:** {source_hash}

```
{numbered_chapter_text}
```

{slides_section}

Produce the chapter map now. Follow the chapter's own arc — build up the doctrine the way the chapter builds it.
