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
from ag_exams.prompts import (
    build_grounding_per_q_prompt,
    build_ambiguity_audit_per_q_prompt,
    build_edge_case_audit_per_q_prompt,
    build_argument_pass_per_q_prompt,
)

async def dispatch_with_sem(sem, prompt, model, use_diskcache):
    async with sem:
        try:
            return await dispatch_gemini(prompt, model=model, use_diskcache=use_diskcache)
        except Exception as e:
            return f"Error: {e}"

async def process_question(sem, q_text, scenario_text, q_name):
    # 1. Grounding
    cfg_gr = get_stage_config("grounding_per_q")
    t1 = dispatch_with_sem(sem, build_grounding_per_q_prompt(q_text), cfg_gr.model, cfg_gr.cache)
    
    # 2. Ambiguity
    cfg_am = get_stage_config("ambiguity_audit_per_q")
    t2 = dispatch_with_sem(sem, build_ambiguity_audit_per_q_prompt(q_text), cfg_am.model, cfg_am.cache)
    
    # 3. Edge Case
    cfg_ec = get_stage_config("edge_case_audit_per_q")
    t3 = dispatch_with_sem(sem, build_edge_case_audit_per_q_prompt(q_text, scenario_text), cfg_ec.model, cfg_ec.cache)
    
    # 4. Arg Pass Sonnet
    cfg_son = get_stage_config("argument_pass_sonnet")
    t4 = dispatch_with_sem(sem, build_argument_pass_per_q_prompt(q_text), cfg_son.model, cfg_son.cache)
    
    # 5. Arg Pass Opus
    cfg_op = get_stage_config("argument_pass_opus")
    t5 = dispatch_with_sem(sem, build_argument_pass_per_q_prompt(q_text), cfg_op.model, cfg_op.cache)
    
    res = await asyncio.gather(t1, t2, t3, t4, t5)
    print(f"Finished processing {q_name}")
    return q_name, res

async def run_qa(quiz_file: str, output_file: str):
    print(f"Reading quiz from {quiz_file}...")
    text = Path(quiz_file).read_text(encoding="utf-8")
    
    stem_blocks = list(re.finditer(r"(## Stem \d+.*?(?=### Questions))", text, re.DOTALL))
    q_matches = list(re.finditer(r"(\*\*Q\d+\.\*\*.*?(?=\*\*Q\d+\.\*\*|---|\Z|## Coverage Summary))", text, re.DOTALL))
    
    if not q_matches:
        print("No questions found.")
        return

    print(f"Found {len(q_matches)} questions. Processing concurrently...")
    
    sem = asyncio.Semaphore(15)  # Max 15 concurrent requests to Gemini
    tasks = []
    
    for idx, qm in enumerate(q_matches, 1):
        q_start = qm.start()
        q_text = qm.group(1).strip()
        
        scenario_text = "No scenario found"
        for sb in reversed(stem_blocks):
            if sb.start() < q_start:
                scenario_text = sb.group(1).strip()
                break
                
        q_num_match = re.search(r"\*\*Q(\d+)\.\*\*", q_text)
        # Pad with 0 for proper sorting (e.g. Q01 instead of Q1)
        q_num_str = q_num_match.group(1).zfill(2) if q_num_match else str(idx).zfill(2)
        q_name = f"Q{q_num_str}"
        
        tasks.append(process_question(sem, q_text, scenario_text, q_name))
        
    results = await asyncio.gather(*tasks)
    
    out = open(output_file, "w", encoding="utf-8")
    out.write(f"# QA Results for {os.path.basename(quiz_file)}\n\n")
    
    # Sort results by Q number so they appear in order
    for q_name, (res_gr, res_am, res_ec, res_son, res_op) in sorted(results, key=lambda x: x[0]):
        out.write(f"## {q_name}\n\n")
        out.write("### Grounding\n\n" + res_gr + "\n\n")
        out.write("### Ambiguity Audit\n\n" + res_am + "\n\n")
        out.write("### Edge Case Audit\n\n" + res_ec + "\n\n")
        out.write("### Argument Pass (Sonnet)\n\n" + res_son + "\n\n")
        out.write("### Argument Pass (Opus)\n\n" + res_op + "\n\n")
        out.write("---\n\n")
        
    out.close()
    print(f"\nDone! Results written to {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Standalone QA script for running the exam pipeline audits against an existing quiz file.")
    parser.add_argument("quiz_file", help="Path to the markdown file containing the quiz")
    parser.add_argument("--out", default="qa_results.md", help="Output markdown file")
    args = parser.parse_args()
    
    asyncio.run(run_qa(args.quiz_file, args.out))
