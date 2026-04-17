# Chapter Map Extraction Prompt

You are analyzing a criminal law casebook chapter to produce a structured chapter map for exam generation. The map catalogs every testable doctrine, case holding, factual lever, and student trap in the chapter.

## Input

The chapter text follows, with line numbers prepended to each line.

## What counts as a doctrine

A **doctrine** is a testable legal question — a rule, standard, test, or distinction that a student could get right or wrong on an exam. Examples: "but-for causation," "Pinkerton liability," "substantial step test."

**Not doctrines:** background policy discussion, historical context, biographical facts about cases, or pedagogical framing — unless they contain an embedded testable rule.

**Doctrine identification tests** (apply all four):
1. **Meta-doctrine test:** When the chapter compares two frameworks (e.g., common law vs. MPC), that comparison is itself a testable doctrine.
2. **Institutional-application test:** When a general concept is applied to a specific context (e.g., conspiracy applied to corporations) and the context changes the analysis, that's a separate doctrine.
3. **Policy-embedded-rule test:** When a policy discussion contains a testable legal rule (e.g., "manufactured conspiracy" doctrine inside a policy section on sting operations), extract the rule as a doctrine. Skip the policy.
4. **Consolidation test:** If two potential doctrines always appear together and testing one necessarily tests the other, consolidate them into one.

**Target:** 12–20 doctrines per chapter. Fewer than 10 means you're being too selective. More than 25 means you're tagging concepts, not doctrines.

## Output format

Produce a single JSON object with this exact structure:

```json
{
  "meta": {
    "chapter": <number>,
    "title": "<chapter title>",
    "source_file": "<filename>",
    "source_hash": "<provided>",
    "generated_at": "<ISO 8601 timestamp>",
    "model": "<your model name>"
  },
  "doctrines": [
    {
      "key": "<kebab-case-key>",
      "rule": "<One sentence stating the testable legal rule. Must be precise enough that a student could apply it to new facts.>",
      "split": "<Where jurisdictions or frameworks disagree on this rule, or null if no split.>",
      "levers": ["<concrete factual variable that changes the legal outcome>"],
      "traps": ["<Students [choose X] because [they confuse Y with Z]. Must describe the specific mistake and its cause.>"],
      "cases": ["<Case Name as it appears in the chapter>"],
      "lines": [[<start>, <end>]],
      "block_count": <number of distinct line-range blocks>,
      "cross_chapter": ["<doctrine-key (Ch. N)>"],
      "exam_lens": "<prosecution | defense | both>"
    }
  ],
  "cases": [
    {
      "name": "<Full case name>",
      "lines": [<first_line>, <last_line>],
      "holding": "<One-sentence holding.>",
      "facts_summary": "<One-sentence facts.>",
      "doctrines": ["<doctrine-key>"]
    }
  ],
  "statutes": [
    {
      "citation": "<e.g., 18 U.S.C. § 371>",
      "lines": [<start>, <end>]
    }
  ],
  "blocks": [
    {
      "lines": [<start>, <end>],
      "type": "<case | doctrine-exposition | hypothetical | statute | introduction | policy>",
      "doctrines": ["<doctrine-key>"],
      "summary": "<One sentence.>"
    }
  ],
  "hypo_seeds": [
    {
      "description": "<What the hypo tests — one sentence.>",
      "doctrines": ["<doctrine-key>"],
      "lines": [<start>, <end>],
      "note": "<Why this is useful for exam design, e.g., 'Students practiced this — exam should vary the facts.'>"
    }
  ]
}
```

## Key requirements

- **kebab-case keys** for all doctrine keys (e.g., `pinkerton-liability`, `substantial-step-test`)
- **Line numbers must be accurate.** Every `lines` field must reference actual line numbers from the input. Verify by checking the content at those line numbers.
- **Trap format is mandatory:** "Students [choose X] because [they confuse Y with Z]." The trap must name the specific wrong answer and explain the cognitive error. "Confusing X and Y" without specifying the wrong choice is insufficient.
- **Block coverage:** Every substantive line in the chapter should appear in at least one block. Gaps in coverage mean you missed something.
- **Cross-chapter links:** Reference doctrine keys from other chapters where the doctrines connect. Use format: `"doctrine-key (Ch. N)"`. Only include links you're confident about based on explicit cross-references in the chapter text.
- **Hypo seeds:** 2-3 per doctrine minimum. These are fact-pattern ideas that could generate exam questions. Focus on facts that exercise the doctrine's levers.

## Chapter text

**Chapter {chapter_number}: {chapter_title}**
**Source file:** {source_file}
**Source hash:** {source_hash}

```
{numbered_chapter_text}
```

Produce the JSON chapter map now. Output only valid JSON — no markdown fencing, no commentary.
