import asyncio
import json
import logging
import re
import sys
from pathlib import Path

from ag_exams.gemini_client import dispatch_gemini

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MAPS_DIR = PROJECT_ROOT / "criminal-law" / "quiz-system" / "research" / "chapter-maps"

TRAP_REGEX = re.compile(r"(?im)^-\s*\*\*Trap:?\*\*\s*(.+)$")

SYSTEM_PROMPT = """You are a strict formatting engine for law school exam data. 
You will receive a JSON list of "Trap" descriptions.
Your task is to rewrite EVERY trap into this EXACT semantic syntax:
"Students choose [Incorrect Answer] because they confuse [Concept A] with [Concept B]."

Rules:
1. You MUST use the bracket syntax for the three core variables.
2. You MUST use the exact phrasing "Students choose [...] because they confuse [...] with [...]". Do not use "assume", "miss", "forget", or any other phrasing.
3. You MUST retain the exact legal meaning and context of the original trap.
4. Return ONLY a JSON object where the keys are the exact original strings, and the values are your perfectly formatted rewritten strings. Do not include markdown blocks like ```json, just the raw JSON.
"""

async def fix_traps_for_chapter(chapter_num: int) -> None:
    map_path = MAPS_DIR / f"chapter-{chapter_num:02d}.md"
    if not map_path.exists():
        map_path = MAPS_DIR / f"chapter-{chapter_num:02d}.json"
        
    if not map_path.exists():
        print(f"Skipping chapter {chapter_num}: Map not found.")
        return

    content = map_path.read_text()
    
    # Extract traps
    matches = TRAP_REGEX.findall(content)
    if not matches:
        print(f"No traps found in chapter {chapter_num}.")
        return
        
    print(f"Found {len(matches)} traps in chapter {chapter_num}. Sending to Gemini for fixing...")
    
    prompt = json.dumps(matches, indent=2)
    
    try:
        response = await dispatch_gemini(
            prompt=prompt,
            system_instruction=SYSTEM_PROMPT,
            model="gemini-3.1-pro-preview",
            response_mime_type="application/json",
            use_diskcache=False  # We want a fresh rewrite
        )
        
        # Clean the response just in case
        response_text = response.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        replacements = json.loads(response_text)
        
        new_content = content
        fixes_applied = 0
        for old_trap, new_trap in replacements.items():
            if old_trap in new_content:
                new_content = new_content.replace(old_trap, new_trap)
                fixes_applied += 1
            else:
                print(f"  Warning: Old trap not found exactly in text: {old_trap[:50]}...")
                
        if fixes_applied > 0:
            map_path.write_text(new_content)
            print(f"Successfully applied {fixes_applied}/{len(matches)} fixes to chapter {chapter_num}.")
        else:
            print(f"No replacements could be safely applied to chapter {chapter_num}.")
            
    except Exception as e:
        print(f"Error processing chapter {chapter_num}: {e}")

async def run_all(chapters: list[int] | None = None) -> None:
    if not chapters:
        chapters = list(range(1, 24))
    
    for ch in chapters:
        await fix_traps_for_chapter(ch)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fix Trap formatting in Chapter Maps.")
    parser.add_argument("--chapter", "-c", type=int, help="Chapter number to fix")
    parser.add_argument("--all", action="store_true", help="Fix all chapters")
    args = parser.parse_args()
    
    if args.all:
        asyncio.run(run_all())
    elif args.chapter:
        asyncio.run(run_all([args.chapter]))
    else:
        parser.print_help()
