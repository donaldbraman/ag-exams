import asyncio
import os
import sys
from pathlib import Path

# Add src to python path
sys.path.insert(0, os.path.abspath("src"))

from ag_exams.gemini_client import dispatch_gemini
from ag_exams.prompts import build_ambiguity_audit_per_q_prompt
from ag_exams.model_config import get_stage_config

async def test_blocked_question():
    # Load q03 from duty_omission which was previously blocked by ambiguity audit
    q_path = Path("criminal-law/quiz-system/research/final-exam/duty_omission-questions/q03.md")
    q_text = q_path.read_text()
    
    print(f"Testing Ambiguity Audit for {q_path.name}...")
    
    prompt = build_ambiguity_audit_per_q_prompt(q_text)
    
    cfg = get_stage_config("ambiguity_audit_per_q")
    
    try:
        # We disabled diskcache so it actually forces an API call
        print(f"Dispatching to {cfg.model} with BLOCK_ONLY_HIGH...")
        result = await dispatch_gemini(prompt, model=cfg.model, use_diskcache=False)
        print("\n\nSUCCESS! Response received:")
        print("="*40)
        print(result)
        print("="*40)
    except Exception as e:
        print(f"\n\nFAIL: Safety block triggered!")
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_blocked_question())
