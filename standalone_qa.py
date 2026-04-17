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

async def run_qa(quiz_file: str, output_file: str):
    print(f"Reading quiz from {quiz_file}...")
    text = Path(quiz_file).read_text(encoding="utf-8")
    
    # 1. Parse out the stems/scenarios
    # This regex looks for "## Stem X..." up to "### Questions"
    stem_blocks = list(re.finditer(r"(## Stem \d+.*?(?=### Questions))", text, re.DOTALL))
    
    # 2. Parse out the questions
    # A question block starts with **Q\d+.** and ends at the next **Q\d+.** or --- or ## Coverage Summary
    # We use a pattern that captures everything for a single Q.
    q_matches = list(re.finditer(r"(\*\*Q\d+\.\*\*.*?(?=\*\*Q\d+\.\*\*|---|\Z|## Coverage Summary))", text, re.DOTALL))
    
    if not q_matches:
        print("No questions found in the file. Make sure they start with **Q[number].**")
        return

    print(f"Found {len(q_matches)} questions.")
    
    out = open(output_file, "w", encoding="utf-8")
    out.write(f"# QA Results for {os.path.basename(quiz_file)}\n\n")
    
    for idx, qm in enumerate(q_matches, 1):
        q_start = qm.start()
        q_text = qm.group(1).strip()
        
        # Find the stem that precedes this question
        scenario_text = "No scenario found"
        for sb in reversed(stem_blocks):
            if sb.start() < q_start:
                scenario_text = sb.group(1).strip()
                break
                
        q_num_match = re.search(r"\*\*Q(\d+)\.\*\*", q_text)
        q_name = f"Q{q_num_match.group(1)}" if q_num_match else f"Question {idx}"
        
        # Log progress
        preview = q_text.splitlines()[0]
        if len(preview) > 60: preview = preview[:60] + "..."
        print(f"\nProcessing {q_name}: {preview}")
        
        # 1. Grounding
        print("  - Running Grounding Audit...")
        cfg = get_stage_config("grounding_per_q")
        prompt = build_grounding_per_q_prompt(q_text)
        try:
            res_grounding = await dispatch_gemini(prompt, model=cfg.model, use_diskcache=cfg.cache)
        except Exception as e:
            res_grounding = f"Error: {e}"
            
        # 2. Ambiguity
        print("  - Running Ambiguity Audit...")
        cfg = get_stage_config("ambiguity_audit_per_q")
        prompt = build_ambiguity_audit_per_q_prompt(q_text)
        try:
            res_ambiguity = await dispatch_gemini(prompt, model=cfg.model, use_diskcache=cfg.cache)
        except Exception as e:
            res_ambiguity = f"Error: {e}"
            
        # 3. Edge Case
        print("  - Running Edge Case Audit...")
        cfg = get_stage_config("edge_case_audit_per_q")
        prompt = build_edge_case_audit_per_q_prompt(q_text, scenario_text)
        try:
            res_edge_case = await dispatch_gemini(prompt, model=cfg.model, use_diskcache=cfg.cache)
        except Exception as e:
            res_edge_case = f"Error: {e}"
            
        # 4. Argument Pass (Sonnet equivalent)
        print("  - Running Argument Pass (Sonnet)...")
        cfg = get_stage_config("argument_pass_sonnet")
        prompt = build_argument_pass_per_q_prompt(q_text)
        try:
            res_arg_sonnet = await dispatch_gemini(prompt, model=cfg.model, use_diskcache=cfg.cache)
        except Exception as e:
            res_arg_sonnet = f"Error: {e}"
            
        # 5. Argument Pass (Opus equivalent)
        print("  - Running Argument Pass (Opus)...")
        cfg = get_stage_config("argument_pass_opus")
        prompt = build_argument_pass_per_q_prompt(q_text)
        try:
            res_arg_opus = await dispatch_gemini(prompt, model=cfg.model, use_diskcache=cfg.cache)
        except Exception as e:
            res_arg_opus = f"Error: {e}"
            
        # Write to file
        out.write(f"## {q_name}\n\n")
        out.write("### Grounding\n\n" + res_grounding + "\n\n")
        out.write("### Ambiguity Audit\n\n" + res_ambiguity + "\n\n")
        out.write("### Edge Case Audit\n\n" + res_edge_case + "\n\n")
        out.write("### Argument Pass (Sonnet)\n\n" + res_arg_sonnet + "\n\n")
        out.write("### Argument Pass (Opus)\n\n" + res_arg_opus + "\n\n")
        out.write("---\n\n")
        out.flush()

    out.close()
    print(f"\nDone! Results written to {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Standalone QA script for running the exam pipeline audits against an existing quiz file.")
    parser.add_argument("quiz_file", help="Path to the markdown file containing the quiz")
    parser.add_argument("--out", default="qa_results.md", help="Output markdown file")
    args = parser.parse_args()
    
    asyncio.run(run_qa(args.quiz_file, args.out))
