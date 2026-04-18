#!/usr/bin/env python3
import asyncio
import os
import sys
import re
from pathlib import Path

# Add src to path so we can import ag_exams modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from ag_exams.model_config import get_stage_config
from ag_exams.gemini_client import dispatch_gemini

FIX_PROMPT = """You are a master criminal law exam question writer. 
The QA pipeline has flagged the following question with 'MUST FIX' or 'SHOULD FIX' errors.

Your job is to rewrite the question to fix the specific issues raised in the QA feedback.
Do NOT change the core doctrine tested unless necessary to fix the issue. 
Ensure the distractors have explicit falsifiable errors and the correct answer is unambiguously correct.

**PEDAGOGICAL PRINCIPLE:** Do not require students to memorize which states or jurisdictions apply which specific doctrines (e.g., do not ask "What is the rule in California?"). Instead, explicitly provide the relevant jurisdictional rules or doctrines directly within the question stem (e.g., "Under the California approach (which recognizes X) versus the New York approach (which rejects X)"), and test the student's ability to logically apply those provided rules to the fact pattern.

**OPTION LENGTH BALANCING:** You MUST ensure that ALL FIVE options are approximately the same length (+/- 10% character count). Do NOT make the correct answer predictably longer or shorter than the distractors. Pad shorter options with additional relevant reasoning if necessary.

## Scenario Stem Facts
{scenario_text}

## Original Question
{original_question}

## QA Feedback (Issues to Fix)
{feedback}

## Formatting Rules
Output the revised question in strict Markdown, exactly following this format:
**Q<N>.** <question stem, 2-4 sentences>

(a) <option text>
(b) <option text>
(c) <option text>
(d) <option text>
(e) <option text>

**Answer:** (<letter>)

**Explanation:** <short paragraph on why correct answer is right; then one terse sentence per wrong option. ≤ 200 words total.>

**Tags:** <comma-separated tags>

**Grounding:** <chapter + case names>

IMPORTANT: Mark the correct option by appending ` <!-- correct -->` to the end of its line.
Output ONLY the revised question block. Do not wrap in markdown ``` code fences or add extraneous commentary.
"""

def extract_qa_blocks(text):
    # Splits qa_results.md into sections
    # Returns dict of Q name -> QA text
    q_sections = re.split(r"## (Q\d+)\n", text)[1:]
    return {q_sections[i]: q_sections[i+1] for i in range(0, len(q_sections), 2)}

def extract_fix_reasons(qa_text):
    reasons = []
    # Ambiguity
    am_match = re.search(r"### Ambiguity Audit.*?(?=### Edge Case Audit)", qa_text, re.DOTALL)
    if am_match and re.search(r"(MUST FIX|SHOULD FIX)", am_match.group(0)):
        reasons.append(("Ambiguity Audit", am_match.group(0).strip()))
        
    ec_match = re.search(r"### Edge Case Audit.*?(?=### Argument Pass)", qa_text, re.DOTALL)
    if ec_match and re.search(r"(MUST FIX|SHOULD FIX)", ec_match.group(0)):
        reasons.append(("Edge Case Audit", ec_match.group(0).strip()))
        
    son_match = re.search(r"### Argument Pass \(Sonnet\).*?(?=### Argument Pass \(Opus\))", qa_text, re.DOTALL)
    if son_match and re.search(r"(MUST FIX|SHOULD FIX)", son_match.group(0)):
        reasons.append(("Argument Pass (Sonnet)", son_match.group(0).strip()))
        
    op_match = re.search(r"### Argument Pass \(Opus\).*?(?=\Z|---)", qa_text, re.DOTALL)
    if op_match and re.search(r"(MUST FIX|SHOULD FIX)", op_match.group(0)):
        reasons.append(("Argument Pass (Opus)", op_match.group(0).strip()))
        
    return reasons

async def process_rewrite(sem, q_name, original_question, scenario_text, reasons):
    feedback_text = "\n\n".join([f"### {r[0]}\n{r[1]}" for r in reasons])
    prompt = FIX_PROMPT.format(
        scenario_text=scenario_text,
        original_question=original_question,
        feedback=feedback_text
    )
    
    # We use question_writer stage config (usually gemini-3.1-pro) for rewriting
    cfg = get_stage_config("question_writer")
    
    async with sem:
        for attempt in range(2):
            try:
                print(f"Rewriting {q_name} (Attempt {attempt+1})...")
                result = await dispatch_gemini(prompt, model=cfg.model, use_diskcache=False)
                print(f"Finished rewriting {q_name}")
                return q_name, result
            except Exception as e:
                if "empty or blocked" in str(e).lower() and attempt == 0:
                    print(f"Safety block on {q_name}. Self-healing retry...")
                    prompt += "\n\nCRITICAL INSTRUCTION: Your previous attempt to respond was blocked by safety filters. Please try again. To avoid safety blocks, abstract away any graphic, violent, sexual, or sensitive details in your question text. Focus purely on the legal doctrine."
                else:
                    print(f"Error rewriting {q_name}: {e}")
                    return q_name, original_question # fallback

async def main():
    qa_file = Path("qa_results_padded_final_v2.md")
    quiz_file = Path("quiz-5-padded-final-fixed.md")
    out_path = "quiz-5-padded-final-fixed.md"
    
    qa_text = qa_file.read_text(encoding="utf-8")
    quiz_text = quiz_file.read_text(encoding="utf-8")
    
    qa_dict = extract_qa_blocks(qa_text)
    
    # Parse out questions from quiz
    stem_blocks = list(re.finditer(r"(## Stem \d+.*?(?=### Questions))", quiz_text, re.DOTALL))
    q_matches = list(re.finditer(r"(\*\*Q\d+\.\*\*.*?(?=\*\*Q\d+\.\*\*|---|\Z|## Coverage Summary))", quiz_text, re.DOTALL))
    
    must_fix_tasks = []
    sem = asyncio.Semaphore(5)
    
    q_data = [] # stores list of (q_name, text, is_must_fix, reasons, scenario)
    
    for idx, qm in enumerate(q_matches, 1):
        q_start = qm.start()
        q_text = qm.group(1).strip()
        
        scenario_text = "No scenario found"
        for sb in reversed(stem_blocks):
            if sb.start() < q_start:
                scenario_text = sb.group(1).strip()
                break
                
        q_num_match = re.search(r"\*\*Q(\d+)\.\*\*", q_text)
        q_name = f"Q{q_num_match.group(1).zfill(2)}" if q_num_match else f"Q{str(idx).zfill(2)}"
        
        # Check if MUST FIX or SHOULD FIX
        qa_block = qa_dict.get(q_name, "")
        reasons = extract_fix_reasons(qa_block)
        
        if reasons:
            must_fix_tasks.append(process_rewrite(sem, q_name, q_text, scenario_text, reasons))
            q_data.append({"name": q_name, "original": q_text, "rewrite": True})
        else:
            q_data.append({"name": q_name, "original": q_text, "rewrite": False})
            
    if not must_fix_tasks:
        print("No questions found needing fixes.")
        return
        
    print(f"Found {len(must_fix_tasks)} questions needing fixes. Starting rewrites...")
    results = await asyncio.gather(*must_fix_tasks)
    rewrite_dict = dict(results)
    
    # Reconstruct quiz file
    new_quiz_text = quiz_text
    for q in q_data:
        if q["rewrite"]:
            revised = rewrite_dict.get(q["name"], q["original"])
            # Strip markdown fences if any
            revised = re.sub(r"^```markdown\s*\n(.*?)\n```$", r"\1", revised, flags=re.DOTALL|re.MULTILINE).strip()
            revised = re.sub(r"^```\s*\n(.*?)\n```$", r"\1", revised, flags=re.DOTALL|re.MULTILINE).strip()
            
            # Since q["original"] was extracted directly from quiz_text, replace will match exactly
            new_quiz_text = new_quiz_text.replace(q["original"], revised)
            
    Path(out_path).write_text(new_quiz_text, encoding="utf-8")
    print(f"Done! Saved rewritten quiz to {out_path}")

if __name__ == "__main__":
    asyncio.run(main())
