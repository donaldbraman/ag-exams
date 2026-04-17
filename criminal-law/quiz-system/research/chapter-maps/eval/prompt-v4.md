# Chapter Map Extraction Prompt (v4 — Progressive Doctrinal Summary)

You are analyzing a criminal law casebook chapter to produce a **progressive doctrinal summary** for exam generation. The map follows the chapter's pedagogical arc: it states the doctrine's elements in plain language, then shows how the chapter refines each element through cases, distinctions, and complications.

## Inputs

1. The chapter text, with line numbers prepended to each line.
2. A slide digest (if provided) — a Gemini-generated summary of the class slides for this chapter, describing what each slide teaches and what students practiced. Use this to identify concepts students worked with in class.

## What to produce

### 1. Elements and Extensions (plain language)

State the core doctrine of the chapter in plain English. Separate:

- **Prima facie elements** — what the prosecution must prove. These are the parts a student would need to identify and analyze first on an exam.
- **Liability extensions** — doctrines that expand liability beyond the prima facie case (e.g., Pinkerton vicarious liability). These apply *after* the core elements are established.
- **Liability limits** — doctrines that categorically bar or reduce liability (e.g., Wharton's Rule, withdrawal). These are defenses or structural limits the student should check.

Use the language a professor would use in class, not statutory language.

### 2. Refinements (in chapter order)

For each element, extension, or limit, walk through how the chapter develops it. As the chapter introduces cases, distinctions, splits, or complications, summarize them **in the order the student encounters them**. This preserves the pedagogical structure.

For each refinement:
- **Rule** — the rule, distinction, or complication in one or two sentences
- **Source** — the case, statute, or hypothetical that introduces this point
- **Trap** — where students go wrong. Format: "Students [choose X] because [they confuse Y with Z]." Only include where a genuine exam mistake exists.
- **Difficulty** — foundational / intermediate / advanced
- **Pivot fact** — the single factual change that would flip the legal outcome. One sentence.
- **Jurisdiction** — `universal`, `split (traditional/MPC)`, `federal only`, or `majority/minority`
- **Practiced** — if the slide digest shows this concept was practiced in class, note which slide(s). Otherwise omit.

### 3. Clusters (exam design guidance)

Group refinements that would naturally appear together in a single exam fact pattern. Each cluster should name 2-5 refinements and provide a one-sentence scenario hook that would engage all of them. This helps the exam architect design integrated questions rather than testing points in isolation.

### 4. Cases (compact reference)

For each case in the chapter, provide:
- **Holding** — one sentence
- **Reasoning** — WHY the court reached this holding (one sentence)
- **Facts** — one sentence
- **Teaches** — which refinement(s) this case supports
- **Source type** — `main case` (edited excerpt), `note case` (discussed in notes/callouts), or `illustrative` (used as example without formal excerpt)
- **Has discussion questions** — yes/no. Cases with discussion questions in the chapter are the professor's own exam seeds.

### 5. Coverage checklist

A flat list of all refinement keys with their difficulty, section (element/extension/limit), and whether they were practiced in class. This lets the exam architect scan coverage quickly.

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

### Prima Facie Elements

[Numbered list of what the prosecution must prove, in plain language.]

### Liability Extensions

[Doctrines that expand liability beyond the prima facie case. May be empty for some chapters.]

### Liability Limits

[Doctrines that categorically bar or reduce liability. May be empty for some chapters.]

## Refinements

### [Element/Extension/Limit Name]

#### [refinement-key]: [Short Title]
- **Rule:** [One or two sentences]
- **Source:** [Case name, statute, or "chapter hypothetical (line N)"]
- **Trap:** Students [choose X] because [they confuse Y with Z].
- **Difficulty:** foundational | intermediate | advanced
- **Pivot fact:** [Single factual change that flips the outcome]
- **Jurisdiction:** universal | split (traditional/MPC) | federal only | majority/minority
- **Practiced:** [slide N — brief description] (only if in slide digest)

#### [refinement-key]: [Short Title]
...

### [Next Section Name]
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
- **Source type:** main case | note case | illustrative
- **Discussion questions:** yes | no

## Coverage Checklist

| Key | Section | Difficulty | Practiced |
|-----|---------|------------|-----------|
| refinement-key | element / extension / limit | foundational / intermediate / advanced | slide N or — |
```

## Key requirements

- **kebab-case keys** for all refinement and cluster keys
- **Plain language** for elements — write as if explaining to a smart student, not quoting a statute
- **Three-tier structure**: Separate prima facie elements from liability extensions and liability limits. This maps to how exam answers should be organized.
- **Chapter order** for refinements — follow the sequence the chapter uses
- **Trap format is mandatory:** "Students [choose X] because [they confuse Y with Z]." Only where a real exam mistake exists.
- **Pivot facts are mandatory:** Name the single factual change that flips the outcome. If you can't identify one, the refinement may not be testable.
- **Jurisdiction flags are mandatory:** Mark every refinement. This tells the exam architect which refinements produce jurisdiction-comparison questions.
- **Consolidation:** If two refinements make the same point from different angles (e.g., a general inference principle and its specific structural test), merge them into one refinement with sub-points.
- **No clutter:** No line-range tables, no block coverage maps, no statutes section, no hypo seeds. The exam generator creates its own hypotheticals from this map.
- **Difficulty ratings:**
  - **foundational** — core rule every student must know
  - **intermediate** — requires applying a rule to ambiguous facts or distinguishing frameworks
  - **advanced** — requires synthesizing multiple doctrines, recognizing a split, or spotting a subtle distinction
- **Clusters:** Every refinement should appear in at least one cluster. Clusters help the exam architect design integrated scenarios.
- **Slide digest integration:** If a slide digest is provided, use it to:
  - Tag refinements that were practiced in class
  - Identify doctrines taught via slides but absent from the chapter text (add them as refinements, noting the source is slides-only)
  - Flag cases that received extended discussion in slides

## Chapter text

**Chapter {chapter_number}: {chapter_title}**
**Source file:** {source_file}
**Source hash:** {source_hash}

```
{numbered_chapter_text}
```

{slides_section}

Produce the chapter map now. Follow the chapter's own arc — build up the doctrine the way the chapter builds it.
