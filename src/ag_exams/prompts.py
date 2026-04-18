"""Prompt builders for exam generation agents."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

AGENTS_DIR = Path(__file__).resolve().parents[2] / ".claude" / "agents"
REPO_ROOT = Path(__file__).resolve().parents[3]
CHAPTER_MAP_DIR = REPO_ROOT / "criminal-law" / "quiz-system" / "research" / "chapter-maps"
META_MAP_PATH = CHAPTER_MAP_DIR / "meta-map.md"
EXAM_EXCLUSIONS_PATH = REPO_ROOT / "criminal-law" / "config" / "exam-exclusions.yml"


def _load_exam_exclusions() -> str:
    """Load exam-exclusions.yml and render it as a prompt block.

    Returns an empty string if the file is missing or has no excluded_topics.
    """
    if not EXAM_EXCLUSIONS_PATH.exists():
        return ""
    data = yaml.safe_load(EXAM_EXCLUSIONS_PATH.read_text()) or {}
    topics = data.get("excluded_topics") or []
    if not topics:
        return ""
    lines = ["## Excluded Topics (HARD CONSTRAINT)", ""]
    lines.append(
        "The professor has committed to students that the following topics will NOT "
        "appear on the exam. You must not reference them — not as the central subject, "
        "not as incidental background, not in distractors, not in explanations."
    )
    lines.append("")
    for topic in topics:
        name = topic.get("name", "")
        rationale = topic.get("rationale", "")
        keywords = topic.get("keywords") or []
        lines.append(f"- **{name}** — {rationale}")
        if keywords:
            lines.append(f"  Flagged keywords: {', '.join(keywords)}")
    lines.append("")
    lines.append(
        "If a candidate fact pattern, question, or distractor touches any excluded "
        "topic, rework it to use an unrelated factual context that tests the same "
        "doctrine. Do not merely swap keywords — remove the topic entirely."
    )
    return "\n".join(lines)


def _load_focus_maps(chapters: list[int]) -> str:
    """Concatenate chapter maps for the scenario's listed chapters.

    Maps are the sole doctrinal reference for every pipeline stage. Chapters
    without a map get an explicit warning line so the agent can flag
    insufficient coverage rather than silently miss it.
    """
    parts: list[str] = []
    for ch in chapters:
        map_path = CHAPTER_MAP_DIR / f"chapter-{ch:02d}.md"
        if map_path.exists():
            parts.append(f"### Chapter {ch} Map\n\n{map_path.read_text()}")
        else:
            parts.append(
                f"### Chapter {ch} Map\n\n"
                f"**WARNING:** No map exists for Ch {ch}. Treat any doctrine that "
                f"would have to come from Ch {ch} as uncovered until the map is "
                f"authored."
            )
    return "\n\n---\n\n".join(parts)


def _load_meta_map() -> str:
    """Return the meta-map (index of all chapter maps with their Refinement tags)."""
    if META_MAP_PATH.exists():
        return META_MAP_PATH.read_text()
    return (
        "**WARNING:** meta-map artifact is missing. Generate it with "
        "`uv run python criminal-law/scripts/generate_meta_map.py` before "
        "running the pipeline."
    )


_MAPS_USAGE_INSTRUCTIONS = """**How to use the maps:**

- The preloaded focus maps below cover the scenario's primary chapters.
- The meta-map is the index of ALL chapter maps with their Refinement tags.
  If a doctrine doesn't appear in the focus maps, Grep the meta-map for
  the doctrine name (e.g., `creation of peril`, `Pinkerton`). Refinement
  tags are grep-friendly (e.g., `creation-of-peril-category`).
- Open any map you need with the Read tool. Never open raw casebook
  chapter `.qmd` files — the maps are the curated reference; the chapters
  contain throwaway discussion and noise.
"""


def _load_agent_body(filename: str) -> str:
    """Load an agent definition file, strip YAML frontmatter, return body."""
    path = AGENTS_DIR / filename
    text = path.read_text()
    # Strip YAML frontmatter (between --- markers)
    match = re.match(r"^---\n.*?\n---\n", text, re.DOTALL)
    if match:
        return text[match.end() :].strip()
    return text.strip()


def build_architect_prompt(
    scenario_brief: str,
    coverage_priorities: list[str],
    chapters: list[int],
    prior_critique: str | None,
    current_package: str | None,
    round_number: int,
) -> str:
    """Build the full prompt for the exam-architect agent."""
    body = _load_agent_body("exam-architect.md")

    focus_map_text = _load_focus_maps(chapters)
    meta_map_text = _load_meta_map()
    priorities_list = "\n".join(f"{i + 1}. {d}" for i, d in enumerate(coverage_priorities))

    exclusions_block = _load_exam_exclusions()
    exclusions_section = f"\n{exclusions_block}\n" if exclusions_block else ""

    prompt = f"""You are the exam architect. \
This is round {round_number} of the collaborative whiteboarding process.

{body}

## Scenario Brief

{scenario_brief}

## Coverage Priorities (from SWRR tracker)

{priorities_list}

## Chapter Maps — Focused Scope

{focus_map_text if focus_map_text else "No chapter maps available."}

## Chapter Maps — Meta-Map (index of ALL maps)

{meta_map_text}

{_MAPS_USAGE_INSTRUCTIONS}
{exclusions_section}
## Your Task This Round

"""
    if round_number == 1:
        prompt += """This is the FIRST round. \
Design the initial fact pattern with characters, numbered facts, and question stubs.

Explain your reasoning thoroughly in Markdown. What doctrines are you targeting? Why?

Then, clearly outline the facts, characters, and stubs you are proposing. Do NOT output JSON. Output pure Markdown.
"""
    else:
        prompt += f"""Review the critic's feedback and revise the scenario package. \
Address every fact issue and incorporate accepted suggestions.

## Previous Critique

{prior_critique or "None"}

## Current Scenario Package

{current_package or "Empty"}

Explain your reasoning thoroughly in Markdown. What are you changing and why?

Then, clearly outline the REVISED facts, characters, and stubs. Do NOT output JSON. Output pure Markdown.
"""
    return prompt


def build_architect_extractor_prompt(reasoning: str) -> str:
    """Build the prompt for the architect's JSON extractor."""
    return f"""You are a JSON extractor for the exam architect. \
Extract the proposed scenario package from the architect's reasoning below.

Your output MUST be a valid JSON object matching this exact structure:
```json
{{
  "facts": ["Fact 1 text...", "Fact 2 text..."],
  "characters": [{{"name": "...", "role": "...", "stems": [1], "doctrinal_target": "..."}}],
  "stubs": [{{"id": "Q1", "doctrine": "...", "description": "...", "facts_referenced": [1, 2], "stem": 1, "status": "proposed"}}],
  "doctrines_covered": ["possession-distribution", "accomplice-liability"],
  "boss_requests": ["Your supervisor hands you a case file..."],
  "open_questions": ["Should we add a character for X?"],
  "architect_confidence": 5
}}
```

## Architect Reasoning

{reasoning}
"""


def build_critic_prompt(
    current_package: str,
    coverage_priorities: list[str],
    chapters: list[int],
    round_number: int,
) -> str:
    """Build the full prompt for the exam-critic agent."""
    body = _load_agent_body("exam-critic.md")

    focus_map_text = _load_focus_maps(chapters)
    meta_map_text = _load_meta_map()
    priorities_list = "\n".join(f"{i + 1}. {d}" for i, d in enumerate(coverage_priorities))

    exclusions_block = _load_exam_exclusions()
    exclusions_section = f"\n{exclusions_block}\n" if exclusions_block else ""

    prompt = f"""You are the exam critic. \
This is round {round_number} of the collaborative whiteboarding process.

{body}

## Coverage Priorities (from SWRR tracker)

{priorities_list}

## Chapter Maps — Focused Scope

{focus_map_text if focus_map_text else "No chapter maps available."}

## Chapter Maps — Meta-Map (index of ALL maps)

{meta_map_text}

{_MAPS_USAGE_INSTRUCTIONS}
{exclusions_section}
## Current Scenario Package

{current_package}

## Your Task

Evaluate the architect's proposal. For each stub, verify the referenced facts \
support the doctrinal analysis. Check for missed opportunities. Signal CONVERGED \
only when ALL of these are true:
- Every stub has supporting facts that are doctrinally accurate
- Progressive complexity works within each stem
- Boss-request progression feels natural
- No redundant questions
- Coverage priorities are well-addressed

{
        "On round 10 you MUST signal CONVERGED with any remaining concerns noted."
        if round_number >= 10
        else ""
    }

IMPORTANT: Output pure Markdown reasoning. Discuss what to accept, reject, revise, and add.
Explain your evaluations for each stub and fact.
Do NOT output JSON.
"""
    return prompt


def build_critic_extractor_prompt(reasoning: str) -> str:
    """Build the prompt for the critic's JSON extractor."""
    return f"""You are a JSON extractor for the exam critic. \
Extract the critic's evaluation diffs from the reasoning below.

Output a JSON object:
```json
{{
  "status": "ITERATE or CONVERGED",
  "accepted_stubs": ["Q1", "Q3"],
  "rejected_stubs": [{{"id": "Q2", "reason": "facts don't support Pinkerton analysis"}}],
  "proposed_stubs": [{{"id": "Q15", "doctrine": "...", "description": "...", "facts_referenced": [3, 7], "stem": 2, "status": "proposed"}}],
  "revised_facts": {{"4": "Tyler Chen moved in three weeks before..."}},
  "new_facts": ["Fact 18: Brother B contacts a lawyer to set up..."],
  "fact_issues": [{{"fact_number": 4, "issue": "needs clearer no-knowledge language", "severity": "high"}}],
  "opportunities": ["Could test accomplice by omission using facts 3 and 8"],
  "confidence": 7
}}
```

Field guide:
- `revised_facts`: Only facts you want changed. Key = fact index (0-based), value = new text.
- `new_facts`: Facts to append to the end of the fact list.
- `proposed_stubs`: Only NEW stubs you want added.
- `accepted_stubs` / `rejected_stubs`: Verdict on existing stubs by ID.
- Do NOT include unchanged facts, unchanged stubs, or the full package.

## Critic Reasoning

{reasoning}
"""
    return prompt


def build_question_writer_prompt(
    scenario_package: str,
    chapters: list[int],
    statutes: str,
    questions_dir: str,
    header_path: str,
) -> tuple[str, str]:
    """Build the full prompt for the exam-question-writer agent.

    Uses the one-file-per-Q resumable pattern: writer emits each question as
    its own markdown file under questions_dir. On retry, the writer globs
    existing files and resumes from the first missing index.
    """
    body = _load_agent_body("exam-question-writer.md")

    focus_map_text = _load_focus_maps(chapters)
    meta_map_text = _load_meta_map()
    exclusions_block = _load_exam_exclusions()
    exclusions_section = f"\n{exclusions_block}\n" if exclusions_block else ""

    system_instruction = f"""You are the exam question writer. Transform the converged scenario \
package into publication-quality multiple-choice exam questions.

{body}

## Federal Statutes (provided to students on the exam)

{statutes}

## Chapter Maps — Focused Scope

{focus_map_text if focus_map_text else "No chapter maps available."}

## Chapter Maps — Meta-Map (index of ALL maps)

{meta_map_text}

{_MAPS_USAGE_INSTRUCTIONS}
{exclusions_section}
## Output Protocol — Markdown Output

Output your questions in pure Markdown. Separate each file using exactly this delimiter format:

---FILE: header.md---
# Scenario Header

The fact pattern...

---FILE: q01.md---
**Q1.** What is the crime?

(a) Option...

**Answer:** (a)

**Explanation:** ...

**Tags:** ...

**Grounding:** ...

Do NOT wrap the entire output in JSON or Markdown code blocks. Just emit the raw file delimiters and content.

**Count discipline**: produce one `---FILE: qNN.md---` block per stub in the scenario package. If the package lists 10 stubs, emit 10 question blocks and STOP.

## Pedagogical Rules

1. **Distractor Falsifiability:** Ensure every distractor contains an explicit, falsifiable legal error. Implicit omissions are not sufficient to make a distractor wrong.
2. **Jurisdictional Rote Memorization (BANNED):** Do not require students to memorize which states or jurisdictions apply which specific doctrines (e.g., do not ask "What is the rule in California?"). Instead, explicitly provide the relevant jurisdictional rules or doctrines directly within the question stem (e.g., "Under the California approach (which recognizes X) versus the New York approach (which rejects X)"), and test the student's ability to logically apply those provided rules to the fact pattern.
3. **Length Parity (Anti-Meta-Gaming):** All five options MUST be roughly the same length. Do not write a long, detailed correct answer alongside terse distractors. To pad distractors, weave in plausible (but legally flawed) rationales or reference non-dispositive facts from the stem. Aim for structural symmetry (e.g., exactly two sentences per option).

## Per-Question Format Rules (applies to the `content` string)

Each question's `content` string must contain exactly:

```markdown
**Q<N>.** <question stem, 2-4 sentences>

(a) <option text>
(b) <option text>
(c) <option text>
(d) <option text>
(e) <option text>

**Answer:** (<letter>)

**Explanation:** <short paragraph on why correct answer is right; then one \
terse sentence per wrong option. ≤ 200 words total.>

**Tags:** <comma-separated tags>

**Grounding:** <chapter + case names>
```

Mark the correct option by appending ` <!-- correct -->` to the end of its \
line (e.g., `(b) <option text> <!-- correct -->`).

**Strict format requirements** — the validator will reject anything else:
- Header: exactly `**Q<N>.**` on its own line (bold, period). Not `## Q1`.
- Answer line: exactly `**Answer:** (<letter>)`.
- Required blocks: `**Explanation:**`, `**Tags:**`, `**Grounding:**`.

**Conciseness budget**:
- Question stem: 2-4 sentences.
- Each option: 1-3 sentences.
- Explanation: ≤ 200 words. Short paragraph + one terse sentence per wrong \
  option. Do NOT write per-option `**Why (X) is wrong:**` blocks.
- Tags: one line.
- Grounding: one line.
"""

    contents = f"""## Converged Scenario Package

{scenario_package}
"""

    return system_instruction, contents



def build_grounding_prompt(questions_text: str, chapter_paths: list[str]) -> str:
    """Build the prompt for the grounding verifier."""
    chapters_list = "\n".join(f"- {p}" for p in chapter_paths)
    return f"""You are a grounding verifier for criminal law exam questions. \
Your job is to verify each question against the relevant chapter passages.

For each question:
1. Read the referenced chapter(s)
2. Find the specific passage that supports the correct answer
3. Verify that the explanation accurately represents the doctrine
4. Embed a grounding comment: \
<!-- grounding: "Chapter X, section Y: exact quote or paraphrase" -->
5. Flag any question where the correct answer is not supported by chapter text

## Questions to Verify

{questions_text}

## Chapter Files

{chapters_list}

Output the questions with grounding comments embedded. If a question fails \
grounding, prepend <!-- GROUNDING-FAIL: reason --> to it.
"""


def build_adversarial_prompt(stripped_questions: str) -> str:
    """Build the prompt for the adversarial tester (takes exam blind)."""
    return f"""You are a strong law student taking a criminal law final exam. \
Answer each question to the best of your ability. You have NOT seen the answer key.

For each question:
1. Read the fact pattern carefully
2. Analyze each option
3. Select your answer
4. Explain your reasoning, noting which options you found tempting \
and why you eliminated them

## Exam Questions

{stripped_questions}

Output for each question:
```
Q[N]: Selected answer: (X)
Confidence: high/medium/low
Reasoning: ...
Tempting distractors: (Y) because...
```
"""


def build_argument_pass_prompt(questions_text: str) -> str:
    """Build the prompt for the 5-per-option adversarial argument pass.

    For every option on every question, the agent writes the strongest case
    that the option is correct, then compares them head-to-head and flags
    close calls per the `close_call_standard` in ``exam-constraints.yml``.
    """
    return f"""You are an adversarial argument writer running the final-exam \
QA pipeline's stage A. For each question below, produce the strongest \
legally grounded case that each of the five options is correct — \
even the option that is clearly wrong. Then compare the five \
arguments head-to-head and grade the question.

## Close-call standard (from criminal-law/config/exam-constraints.yml)

A distractor passes only if it contains an explicit, identifiable false \
legal claim. Implicit omissions do not suffice. Lock falsifiable \
propositions with absolute words (always, categorically, automatically, \
regardless, every jurisdiction, solely because).

## Method

For every question Q[N]:
1. Read all five options.
2. For each option (a)–(e), write a 3–6 sentence legal argument explaining \
why a student could defend that option as correct. Cite doctrine by name \
where possible (MPC § X, *Case Name*, common-law rule, etc.).
3. After the five arguments, write a "Head-to-head" paragraph comparing \
them. Explicitly identify the weakest falsifiable claim in each distractor.
4. If any distractor's argument is as strong as (or stronger than) the \
keyed answer's argument, flag MUST FIX. If the keyed answer is \
clearly best but one distractor lacks a falsifiable error, flag SHOULD FIX. \
Otherwise mark CLEAN.

## Severity scale

- **MUST FIX** — a distractor is equally or more defensible than the \
keyed answer on these facts.
- **SHOULD FIX** — a distractor is weaker than the key but contains no \
explicit false claim (fails the close-call standard).
- **CLEAN** — the keyed answer is clearly best and every distractor \
embeds an identifiable false legal claim.

## Questions

{questions_text}

## Output format

```
# Adversarial Argument Pass

## Summary
- Total questions: N
- MUST FIX: N
- SHOULD FIX: N
- CLEAN: N

## Findings

### Q[N] — <one-line headline>
**Verdict:** MUST FIX | SHOULD FIX | CLEAN

**(a) Argument-for:** ...
**(b) Argument-for:** ...
**(c) Argument-for:** ...
**(d) Argument-for:** ...
**(e) Argument-for:** ...

**Head-to-head:** ...

**Falsifiable claim per distractor:**
- (a): "..." — wrong because ...
- (b): "..." — wrong because ...
- ...

**Recommended fix (if any):** ...
```

Emit this block for every question, even the CLEAN ones. Do not \
abbreviate.
"""


def build_name_injection_prompt(
    questions_text: str,
    name_pool_path: str | None = None,
) -> str:
    """Build the prompt for the name injection agent.

    The agent replaces generic placeholder names in the quiz with themed names
    drawn from the name pool, following the assignment rules described there.

    Args:
        questions_text: The full markdown quiz text (post-question-writing).
        name_pool_path: Path to the name pool markdown file.  Defaults to
            ``criminal-law/quiz-system/research/name-pool.md`` relative to
            REPO_ROOT.
    """
    if name_pool_path is None:
        resolved_pool = REPO_ROOT / "criminal-law" / "quiz-system" / "research" / "name-pool.md"
    else:
        resolved_pool = Path(name_pool_path)

    name_pool_text = resolved_pool.read_text()

    return f"""You are the name injection agent. Your job is to replace generic \
placeholder names in criminal law exam questions with vivid, memorable names \
drawn from the name pool below, while preserving every other word in the questions \
exactly as written.

## Name Pool

{name_pool_text}

## Assignment Rules

1. **Defendants, victims, and witnesses** → assign names from the Moral Philosophers, \
Probability Theorists & Statisticians, or Famous Jurists sections (all of which \
include nicknames).
   - Use the full nickname form on first reference within a fact pattern \
(e.g., "Immanuel 'Manny-the-Man' Kant"); use just the nickname on subsequent \
references (e.g., "Manny").
   - Mix categories within each stem so that not all characters come from a single \
pool (e.g., do not use only philosophers or only statisticians in one fact pattern).

2. **Judges** → assign names exclusively from the Women of Computing section \
(e.g., "Judge Hopper"). No first names, no nicknames for judges.

3. **Uniqueness within a quiz** — each name may appear only once across the entire \
quiz. Do not reuse a name that was already assigned to a different character in an \
earlier stem.

4. **Consistency within a fact pattern** — a character introduced in the fact \
pattern keeps the same name in every question that references that character, \
including "Assume that…" bridges.

5. **Do NOT rename real case defendants.** If a question references an actual \
historical defendant (e.g., John Hinckley, Lorena Bobbitt), leave that name \
unchanged.

6. **Do NOT rename generic professionals who are not parties.** Generic references \
like "a psychiatrist," "Dr. Smith (a medical examiner)," or "the arresting officer" \
can remain unchanged unless the original text already uses a placeholder first name \
that clearly marks a fictional character.

## Output Format

First, output a mapping table in this exact format:

```
# Name Injection Mapping

| Original Name | Assigned Name | Category |
|---------------|---------------|----------|
| Alex Chen     | Immanuel "Manny-the-Man" Kant | Moral Philosopher |
| Judge Taylor  | Judge Hopper  | Women of Computing |
```

Then output the complete quiz text with all names replaced, beginning with a \
horizontal rule (`---`) followed by the full quiz markdown. Do not alter any text \
other than character names.

## Questions

{questions_text}
"""


def build_ambiguity_audit_prompt(
    questions_text: str,
    chapter_paths: list[str],
) -> str:
    """Build the prompt for the ambiguity auditor.

    The auditor checks every question for answer defensibility — it is NOT a
    style or formatting check.  It catches questions where a strong student
    could mount a credible argument for a distractor.
    """
    chapters_list = "\n".join(f"- {p}" for p in chapter_paths)
    exclusions_block = _load_exam_exclusions()
    exclusions_section = f"\n{exclusions_block}\n" if exclusions_block else ""
    return f"""You are an ambiguity auditor for criminal law exam questions. \
Your job is answer defensibility AND topic-exclusion compliance — NOT formatting, \
style, or grammar.
{exclusions_section}
For every question, work through these eight checks:

1. **Correct-answer accuracy** — Is the marked correct answer actually correct \
under the doctrine covered in the relevant chapter? Read the chapter passages \
before judging.

2. **Falsifiable-claim test** — For each distractor, attempt to complete this \
sentence: "A student should reject this option because it states [specific \
false proposition], which is wrong because [specific doctrinal reason]." \
If you cannot complete it, flag the distractor. Specific patterns to catch: \
\
- **Independently sufficient**: distractor states correct law and independently \
reaches the same conclusion as the correct answer through a different path. \
SHOULD FIX — students should not rank two correct analyses. \
- **Incomplete but correct**: distractor states correct law addressing only \
some elements, with no affirmative false claim. SHOULD FIX — incompleteness \
alone is not a falsifiable error. \
- **Applicable alternative doctrine**: distractor applies a different doctrine \
whose structural prerequisites ARE met by the facts. SHOULD FIX — this is a \
second correct answer. \
- **"Less optimal" analysis**: distractor reaches the same conclusion through \
correct but "secondary" reasoning. SHOULD FIX — the threshold/secondary \
distinction is a professorial judgment, not a student-identifiable error. \
- **Cross-doctrine import where the imported doctrine could apply**: distractor \
uses another doctrine's standard, but that doctrine's prerequisites are \
plausibly met on these facts. SHOULD FIX — it may be a second correct answer.

3. **Explanation consistency** — Does the explanation accurately describe why \
the correct answer is right AND why each wrong answer is wrong? Flag internal \
contradictions.

4. **Sufficient facts** — Does the fact pattern provide enough information to \
answer the question unambiguously? Flag questions where a key fact is missing or \
assumed but unstated.

5. **Jurisdictional clarity** — Does the question make clear which legal regime \
applies (e.g., MPC vs. common law, federal vs. state)? Flag questions that \
would be answered differently under different regimes without specifying one.

6. **Excluded topics** — Does the question reference any topic listed in the \
"Excluded Topics" block above (as the central subject, incidental background, \
distractor content, or explanation content)? Excluded-topic violations are \
MUST FIX regardless of how well the question tests the target doctrine.

7. **Jurisdictional coherence (doctrinal-combination plausibility)** — Does \
the question require the student to apply a combination of doctrines, statutes, \
or rules that no real jurisdiction actually combines? Pay particular attention \
to pairings that do not reflect either of the two most common doctrinal variants \
taught in the chapter. Flag, for example: \
- Asking a student to apply a state-level insanity test (e.g., MPC § 4.01 or \
  M'Naghten) and the federal Insanity Defense Reform Act (18 U.S.C. § 17) to \
  the same prosecution — § 17 is federal-only. \
- Pairing a state felony-murder reform statute with a federal accomplice \
  doctrine where no state has combined them. \
- Stacking state stand-your-ground provisions with Model Penal Code \
  self-defense rules in a way that no enacted code adopts. \
\
This check is about plausibility, not pedagogy — comparing two regimes as a \
counterfactual ("how would this come out under X vs. Y?") is fine, but asking \
a student to treat both as governing the same case is a legal impossibility. \
Flag as SHOULD FIX if a simple stem reframe (e.g., "assume a counterfactual \
federal prosecution on parallel facts") would resolve it; MUST FIX if the \
question cannot be salvaged without a full rewrite.

8. **Length Parity (Anti-Meta-Gaming)** — Is the marked correct answer \
significantly longer or more detailed than the distractors? If a student \
could guess the correct answer just by picking the longest option, flag it \
as MUST FIX. All options should be roughly symmetrical in length and structure.

## Questions to Audit

{questions_text}

## Relevant Chapter Files (read these before auditing)

{chapters_list}

## Output Format

Output a structured audit report in this exact format:

```
# Ambiguity Audit Report

## Summary
- Total questions audited: N
- MUST FIX: N
- SHOULD FIX: N
- NOTE: N

## Findings

### Q[N]: <one-line description of the issue>
**Severity:** MUST FIX | SHOULD FIX | NOTE
**Check failed:** correct-answer accuracy | defensible distractor | \
explanation consistency | sufficient facts | jurisdictional clarity | \
excluded topics | jurisdictional coherence
**Finding:** <specific description of the problem>
**Recommended fix:** <concrete, actionable change to the question, options, \
or explanation>

[repeat for each finding — omit questions with no findings]

## Questions with No Findings
Q[N], Q[N], ...
```

Severity guide:
- **MUST FIX** — The correct answer is wrong, or a distractor is equally or \
more defensible. The question cannot be used as-is.
- **SHOULD FIX** — The explanation is misleading, a fact is ambiguous, or a \
jurisdictional gap creates meaningful risk of a valid student challenge.
- **NOTE** — Minor ambiguity unlikely to affect a well-prepared student, but \
worth flagging for future revision.
"""


# ---------------------------------------------------------------------------
# Per-Q QA prompts (maps-as-authority, structured severity output)
# ---------------------------------------------------------------------------


def build_grounding_per_q_prompt(q_text: str) -> str:
    """Grounding verification for a SINGLE Q against the full chapter-map corpus.

    Uses progressive context disclosure: the agent starts with the meta-map
    (index of all chapter maps + their Refinement tags) and Greps to locate
    the doctrine. The Q's own chapter tags are not trusted — the agent
    discovers grounding independently against the whole corpus. If the
    doctrine appears in ANY map's Refinements, the Q is grounded; if not,
    GROUNDING FAIL.
    """
    meta_map_text = _load_meta_map()
    return f"""You are a grounding verifier for a single criminal law exam question. \
Your sole authority is the chapter-map corpus — the curated inventory of \
doctrines the professor actually taught. Do NOT consult raw chapter text or \
outside knowledge. Do NOT trust the Q's own chapter tags; verify independently.

## The Question

{q_text}

## Chapter Maps — Meta-Map (index of ALL maps)

{meta_map_text}

{_MAPS_USAGE_INSTRUCTIONS}

## Your Task

For this single question:
1. Identify the doctrine the correct answer relies on (e.g., "creation of \
peril", "Pinkerton liability", "voluntary assumption of care").
2. Grep the meta-map for that doctrine. Refinement tags are grep-friendly \
(e.g., `creation-of-peril`, `pinkerton-foreseeable`). Search for both the \
human-readable name AND likely tag forms.
3. If a matching Refinement tag appears in the meta-map, Read that chapter \
map and verify the explanation accurately paraphrases the map's stated Rule.
4. If NO Refinement matches, the Q is GROUNDING FAIL — even if the doctrine \
is legally real. Students were not taught it.
5. Also check distractor framing: if a distractor aligns with a map's \
identified Trap for this doctrine, note it as supportive of the Q's craft.

## Output

Append ONE of the following blocks to the bottom of the Q as-is. Do NOT \
rewrite the Q itself; append only the grounding block.

If grounded:
```
<!-- grounding: GROUNDED — <doctrine name>, Ch <N>, Refinement \
`<refinement-tag>`. Rule paraphrased accurately. -->
```

If grounded with caveat (doctrine present but explanation slightly overstates \
or the Q applies doctrine in a way not explicitly covered):
```
<!-- grounding: GROUNDED-WITH-CAVEAT — <doctrine name>, Ch <N>, Refinement \
`<refinement-tag>`. Caveat: <specific issue>. -->
```

If grounding fails (doctrine not in any map Refinement, after searching the \
full meta-map):
```
<!-- GROUNDING-FAIL: <doctrine name> is not in any chapter map. The closest \
taught doctrines are: <list nearest Refinement tags from adjacent chapters>. \
Correct answer must rely on one of those instead. -->
```

Output the complete Q (verbatim) with the grounding block appended at the end.
"""


def build_ambiguity_audit_per_q_prompt(q_text: str) -> str:
    """Seven-check ambiguity audit for a SINGLE Q using the chapter-map corpus.

    Runs as Opus with high effort. Uses progressive context disclosure: starts
    with the meta-map and Greps/Reads the relevant chapter maps as needed.
    Does not trust the Q's chapter tags. Audits defensibility — different lens
    than grounding (which checks doctrine existence in the casebook).
    """
    meta_map_text = _load_meta_map()
    return f"""You are an ambiguity auditor for a single criminal law exam question. \
Your role is to surface cases where a smart, well-prepared student could \
mount a credible challenge to the marked answer — you MUST second-guess \
the doctrinal analysis and catch defensibility failures before students do. Do NOT \
trust the Q's own chapter tags; verify against the full chapter-map corpus.

## The Question

{q_text}

## Chapter Maps — Meta-Map (index of ALL maps)

{meta_map_text}

{_MAPS_USAGE_INSTRUCTIONS}

## Eight Checks (run each and report findings)

Grep the meta-map for the doctrine(s) at issue; Read the relevant chapter \
maps with the Read tool before forming your verdict.

1. **Correct-answer accuracy.** Is the marked answer actually correct under \
the doctrine at issue, as stated in the chapter map? If the doctrine admits \
jurisdictional variation, does the stem stipulate a jurisdiction?
2. **Defensible distractor.** Could a prepared student construct a credible \
legal argument that a non-marked option is correct? If yes, identify which \
option and the argument.
3. **Explanation consistency.** Does the explanation's stated reasoning match \
the chapter map's formulation of the doctrine? Flag misparaphrases.
4. **Sufficient facts.** Does the stem provide the facts needed to answer \
without requiring assumptions beyond the stem?
5. **Jurisdictional clarity.** If the doctrine splits across jurisdictions \
(e.g., merger, FM limiting doctrines), does the stem or stub resolve the \
split cleanly? **PEDAGOGICAL PRINCIPLE:** The question MUST NOT require students to memorize which states apply which doctrines. Instead, the relevant jurisdictional rules must be explicitly provided in the stem, testing the student's ability to apply those rules to the facts. Flag any question that relies on rote memorization of state names as MUST FIX.
6. **Excluded-topic bleed.** Does any part of the Q touch DV, sexual assault, \
or other topics the map should not exercise?
7. **Coverage mismatch.** Is the correct answer's doctrine actually in some \
chapter map's Refinements, or is the Q reaching outside what was taught? \
(Don't assume — Grep the meta-map.)
8. **Length Parity (Anti-Meta-Gaming).** Is the marked correct answer \
significantly longer or more detailed than the distractors? If a student \
could guess the correct answer just by picking the longest option, flag it \
as MUST FIX. All options should be roughly symmetrical in length and structure.

## Output

Append ONE of the following blocks to the bottom of the Q as-is. Do NOT \
rewrite the Q itself; append only the audit block.

```
<!-- audit: <VERDICT>
<check 1>: <finding or "pass">
<check 2>: <finding or "pass">
<check 3>: <finding or "pass">
<check 4>: <finding or "pass">
<check 5>: <finding or "pass">
<check 6>: <finding or "pass">
<check 7>: <finding or "pass">
<check 8>: <finding or "pass">
Recommended fix: <concrete edit, if applicable>
-->
```

Where VERDICT is:
- **CLEAN** — all eight checks pass; no student challenge foreseeable.
- **SHOULD FIX** — at least one check reveals a weakness; explanation drift, \
soft distractor, or jurisdictional ambiguity. Ship-able with edits.
- **MUST FIX** — a prepared student could reasonably argue a non-marked \
answer is correct; correct-answer accuracy fails; or coverage mismatch means \
students weren't taught the doctrine.

Output the complete Q (verbatim) with the audit block appended at the end.
"""


def build_edge_case_audit_per_q_prompt(q_text: str, scenario_package: str) -> str:
    """Three-check deep legal reasoning audit for Edge Cases on a SINGLE Q.

    Checks for Fact Pattern Booby Traps, Cross-Doctrine Clashes, and
    Cross-Question Spoilers. Uses the full scenario package as context to catch
    spoilers from other questions.
    """
    return f"""You are a specialized Edge-Case Auditor for criminal law exam questions. \
Your sole job is to catch deep legal reasoning traps that structural QA might miss. \
You must hunt for scenarios where the given facts inadvertently trigger unintended \
defenses, or where questions spoil one another.

## The Full Scenario Package (For Context)
Review this to understand what facts other questions rely on or establish:
{scenario_package}

## The Target Question to Audit
{q_text}

## The Three Edge-Case Checks

1. **Fact Pattern Booby Traps**: Scan the Target Question and the stem for extreme modifiers \
(e.g., "only key", "triple-normal dose", "completely physically impossible"). \
Do these extreme adjectives inadvertently trigger an un-tested limiting doctrine \
(like independent superseding cause, physical impossibility, or involuntary act) \
that destroys the intended legal outcome of this specific question?

2. **Cross-Doctrine Clashes**: Does the defendant's underlying conduct simultaneously \
trigger a distinct limiting doctrine (e.g., Legal Wrong Doctrine, Merger, Wharton's Rule, \
or grading exceptions) that would override the tested doctrine and alter the ultimate legal conclusion?

3. **Cross-Question Spoilers**: Read the Full Scenario Package context. Does the premise, \
fact establishment, or forced legal conclusion of *another* question in this package \
spoil, conflict with, or alter the correct legal analysis of the Target Question? \
(e.g., if Q1 tests a rule in a vacuum, but Q12 establishes a 10-year penalty that overrides it).

## Output

Append ONE of the following blocks to the bottom of the Q as-is. Do NOT \
rewrite the Q itself; append only the audit block.

```
<!-- edge-case-audit: <VERDICT>
1. Fact Pattern Booby Traps: <finding or "pass">
2. Cross-Doctrine Clashes: <finding or "pass">
3. Cross-Question Spoilers: <finding or "pass">
Recommended fix: <concrete edit, if applicable>
-->
```

Where VERDICT is:
- **CLEAN** — all checks pass.
- **SHOULD FIX** — there is a mild clash or edge case that makes the answer debatable, but not entirely broken.
- **MUST FIX** — an extreme fact, clashing doctrine, or spoiler from another question makes the marked answer legally incorrect or introduces a second completely valid answer.

Output the complete Q (verbatim) with the edge-case-audit block appended at the end.
"""


def build_argument_pass_per_q_prompt(q_text: str) -> str:
    """5-per-option argument pass for a SINGLE Q.

    Separate from the multi-Q ``build_argument_pass_prompt`` — this version
    fits the per-Q fan-out pattern with its own Temporal activity per Q.
    Output uses the MUST FIX / SHOULD FIX / CLEAN severity scale.
    """
    return f"""You are an adversarial argument writer running the final-exam \
QA pipeline's 5-per-option argument pass on a single question. For the \
question below, produce the strongest legally grounded case that each of the \
five options is correct — even the option that is clearly wrong. Then \
compare the five arguments head-to-head and grade the question.

## Close-call standard

A distractor passes only if it contains an explicit, identifiable false \
legal claim. Implicit omissions do not suffice. Lock falsifiable propositions \
with absolute words (always, categorically, automatically, regardless, every \
jurisdiction, solely because).

## The Question

{q_text}

## Method

1. Read all five options.
2. For each option (a)-(e), write a 3-6 sentence legal argument explaining \
why a student could defend that option as correct. Cite doctrine by name \
where possible.
3. After the five arguments, write a "Head-to-head" paragraph comparing them. \
Explicitly identify the weakest falsifiable claim in each distractor.
4. If any distractor's argument is as strong as (or stronger than) the keyed \
answer's argument, flag MUST FIX. If the keyed answer is clearly best but one \
distractor lacks a falsifiable error, flag SHOULD FIX. Otherwise mark CLEAN.

## Output

Append the following block to the bottom of the Q as-is. Do NOT rewrite the \
Q itself; append only the argument-pass block.

```
<!-- argument-pass: <VERDICT>
(a) Argument-for: <3-6 sentences>
(b) Argument-for: <3-6 sentences>
(c) Argument-for: <3-6 sentences>
(d) Argument-for: <3-6 sentences>
(e) Argument-for: <3-6 sentences>

Head-to-head: <comparison>

Falsifiable claim per distractor:
- (X): "<quoted phrase>" — wrong because ...
- (Y): "<quoted phrase>" — wrong because ...
- ...

Recommended fix: <concrete edit or "none">
-->
```

VERDICT is MUST FIX | SHOULD FIX | CLEAN per the severity scale above.

Output the complete Q (verbatim) with the argument-pass block appended at \
the end.
"""


def build_blind_take_prompt(stripped_questions: str) -> str:
    """Handicapped-Haiku floor check. Model=haiku, effort=low, max_turns=1.

    The reader sees ONLY stems and options (no answers, no explanations, no
    tags, no grounding). Picks one letter per Q. Used as a floor signal: if
    handicapped Haiku scores too high, the Qs are probably too easy.
    """
    return f"""You are taking a criminal law final exam. For each question \
below, pick the single best option (a-e). You have NOT seen any answer key, \
explanations, or hints.

Output ONLY the letter answers, one per line, in this exact format:

Q1: a
Q2: b
Q3: c
...

No reasoning. No hedging. Just the letter. If uncertain, pick your best guess.

## Exam

{stripped_questions}
"""
