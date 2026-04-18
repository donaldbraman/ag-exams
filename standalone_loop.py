#!/usr/bin/env python3
import asyncio
import os
import sys
import re
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from standalone_qa import process_question
from standalone_fix import process_rewrite, extract_fix_reasons, extract_qa_blocks

async def loop_question(sem, q_name, original_q_text, scenario_text, initial_reasons):
    current_q_text = original_q_text
    reasons = initial_reasons
    
    for iteration in range(10):
        print(f"\n[{q_name}] ========== Iteration {iteration+1}/10 ==========")
        
        # 1. Problem Solver: Rewrite based on reasons
        print(f"[{q_name}] Solver rewriting based on {len(reasons)} issues...")
        _, new_q_text = await process_rewrite(sem, q_name, current_q_text, scenario_text, reasons)
        
        # Clean up markdown fences
        new_q_text = re.sub(r"^```markdown\s*\n(.*?)\n```$", r"\1", new_q_text, flags=re.DOTALL|re.MULTILINE).strip()
        new_q_text = re.sub(r"^```\s*\n(.*?)\n```$", r"\1", new_q_text, flags=re.DOTALL|re.MULTILINE).strip()
        
        current_q_text = new_q_text
        
        # 2. Critic: Run 5-stage QA
        print(f"[{q_name}] Critic analyzing the new draft...")
        _, results = await process_question(sem, current_q_text, scenario_text, q_name)
        res_gr, res_am, res_ec, res_son, res_op = results
        
        qa_block = f"### Grounding\n{res_gr}\n### Ambiguity Audit\n{res_am}\n### Edge Case Audit\n{res_ec}\n### Argument Pass (Sonnet)\n{res_son}\n### Argument Pass (Opus)\n{res_op}"
        
        # 3. Evaluate Critic's Feedback
        reasons = extract_fix_reasons(qa_block)
        
        if not reasons:
            print(f"[{q_name}] SUCCESS! Converged (0 issues) on iteration {iteration+1}!")
            return q_name, current_q_text, True
            
        print(f"[{q_name}] Critic found {len(reasons)} issues remaining.")
        
    print(f"\n[{q_name}] FAILED to converge after 10 iterations.")
    return q_name, current_q_text, False

async def main():
    qa_path = "qa_results.md"
    quiz_path = "quiz-5-fixed-v3.md"
    out_path = "quiz-5-fixed-final.md"
    
    qa_text = Path(qa_path).read_text(encoding="utf-8")
    quiz_text = Path(quiz_path).read_text(encoding="utf-8")
    
    qa_dict = extract_qa_blocks(qa_text)
    
    stem_blocks = list(re.finditer(r"(## Stem \d+.*?(?=### Questions))", quiz_text, re.DOTALL))
    q_matches = list(re.finditer(r"(\*\*Q\d+\.\*\*.*?(?=\*\*Q\d+\.\*\*|---|\Z|## Coverage Summary))", quiz_text, re.DOTALL))
    
    # We will use a smaller semaphore because each targeted Q spawns 1 writer + 5 parallel QA calls
    # 5 concurrent questions = 25 parallel API calls max
    sem = asyncio.Semaphore(5)
    
    loop_tasks = []
    q_data = [] 
    
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
        
        qa_block = qa_dict.get(q_name, "")
        reasons = extract_fix_reasons(qa_block)
        
        if reasons:
            loop_tasks.append(loop_question(sem, q_name, q_text, scenario_text, reasons))
            q_data.append({"name": q_name, "original": q_text, "rewrite": True})
        else:
            q_data.append({"name": q_name, "original": q_text, "rewrite": False})
            
    if not loop_tasks:
        print("No questions found needing fixes.")
        return
        
    print(f"Found {len(loop_tasks)} stubborn questions. Starting localized Solver/Critic loops...")
    results = await asyncio.gather(*loop_tasks)
    
    # Reconstruct quiz file
    rewrite_dict = {res[0]: res[1] for res in results}
    
    new_quiz_text = quiz_text
    for q in q_data:
        if q["rewrite"]:
            revised = rewrite_dict.get(q["name"], q["original"])
            new_quiz_text = new_quiz_text.replace(q["original"], revised)
            
    Path(out_path).write_text(new_quiz_text, encoding="utf-8")
    
    # Summarize final convergence
    converged_count = sum(1 for res in results if res[2])
    print(f"\nDone! {converged_count}/{len(loop_tasks)} targeted questions successfully converged.")
    print(f"Saved finalized quiz to {out_path}")

if __name__ == "__main__":
    asyncio.run(main())
