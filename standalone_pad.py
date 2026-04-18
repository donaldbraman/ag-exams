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

PAD_PROMPT = """You are a master criminal law exam question writer. 
The QA pipeline has flagged the following question for an "Option Length Imbalance" vulnerability. 
Students might guess the correct answer based on length heuristics (e.g. by picking the longest answer).

Your job is to rewrite the OPTIONS ONLY to eliminate this vulnerability. 
Pad the shorter options with additional relevant (but still incorrect) reasoning or context so that ALL FIVE options are approximately the same length (+/- 10% character count).
Do NOT change the core substantive meaning, the legal doctrine tested, or the explicit falsifiability of any option.
Do NOT change the correct answer option's length significantly; focus on padding the shorter distractors to match the longest option's length.
Do NOT change the question stem, the explanation, the tags, or the grounding.

## Original Question Block
{original_question}

## Formatting Rules
Output the revised question block in strict Markdown, exactly following the original format:
**Q<N>.** <question stem>

(a) <padded option text>
(b) <padded option text>
(c) <padded option text>
(d) <padded option text>
(e) <padded option text>

**Answer:** (<letter>)

**Explanation:** <explanation>

**Tags:** <comma-separated tags>

**Grounding:** <chapter + case names>

IMPORTANT: Do NOT include any self-check blocks (<!-- Self-check: ... -->) in your output.
Output ONLY the revised question block. Do not wrap in markdown ``` code fences or add extraneous commentary.
"""

def split_questions(text):
    # Splits quiz markdown into individual question blocks.
    # Assumes each question starts with **Q<N>.**
    # But wait, stems are before Qs. We should split by `---` separator.
    blocks = re.split(r"\n---\n", text)
    return [b.strip() for b in blocks if b.strip()]

async def process_padding(sem, block_text):
    # If the block doesn't contain a question (e.g., just the header or overview), return it as is.
    if not re.search(r"^\*\*Q\d+\.\*\*", block_text, re.MULTILINE):
        return block_text

    prompt = PAD_PROMPT.format(original_question=block_text)
    
    cfg = get_stage_config("question_writer")
    
    q_match = re.search(r"\*\*Q(\d+)\.\*\*", block_text)
    q_name = f"Q{q_match.group(1)}" if q_match else "Unknown"
    
    async with sem:
        for attempt in range(3):
            try:
                print(f"Padding {q_name} (Attempt {attempt+1})...")
                result = await dispatch_gemini(prompt, model=cfg.model, use_diskcache=False)
                # Clean up fences
                result = result.strip()
                if result.startswith("```") and result.endswith("```"):
                    result = "\n".join(result.split("\n")[1:-1]).strip()
                print(f"Finished padding {q_name}")
                return result
            except Exception as e:
                print(f"Error on {q_name}: {e}")
                if attempt == 2:
                    print(f"FAILED {q_name} after 3 attempts.")
                    return block_text
                await asyncio.sleep(2)

async def main():
    input_file = Path("quiz-5-fixed-final.md")
    output_file = Path("quiz-5-padded-final.md")
    
    content = input_file.read_text()
    
    blocks = split_questions(content)
    
    sem = asyncio.Semaphore(5)
    
    tasks = []
    for block in blocks:
        tasks.append(process_padding(sem, block))
        
    results = await asyncio.gather(*tasks)
    
    final_output = "\n\n---\n\n".join(results)
    
    output_file.write_text(final_output + "\n")
    print(f"\nSaved padded quiz to {output_file}")

if __name__ == "__main__":
    asyncio.run(main())
