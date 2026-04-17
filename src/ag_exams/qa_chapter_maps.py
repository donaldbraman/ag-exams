import asyncio
import logging
import sys
from pathlib import Path

from ag_exams.gemini_client import dispatch_gemini

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHAPTERS_DIR = PROJECT_ROOT / "criminal-law" / "chapters"
MAPS_DIR = PROJECT_ROOT / "criminal-law" / "quiz-system" / "research" / "chapter-maps"
REPORTS_DIR = MAPS_DIR / "qa-reports"
SLIDE_DIGESTS_DIR = MAPS_DIR / "slide-digests"

# Same mapping as write-assist for convenience
CHAPTER_FILES = {
    1: "index.qmd",
    2: "02-why-how-punish.qmd",
    3: "03-what-we-punish.qmd",
    4: "04-jury.qmd",
    5: "05-legislatures-courts.qmd",
    6: "06-prosecutors.qmd",
    7: "07-voluntary-act.qmd",
    8: "08-causation.qmd",
    9: "09-omissions.qmd",
    10: "10-mistake.qmd",
    11: "11-public-welfare.qmd",
    12: "12-intentional-homicide.qmd",
    13: "13-unintentional-homicide.qmd",
    14: "14-felony-murder-misdemeanor-manslaughter.qmd",
    15: "15-reform-drugs-guns.qmd",
    16: "16-reform-dv-sexual-assault.qmd",
    17: "17-attempts.qmd",
    18: "18-accomplice.qmd",
    19: "19-conspiracy.qmd",
    20: "20-rico.qmd",
    21: "21-necessity-duress.qmd",
    22: "22-self-defense.qmd",
    23: "23-insanity.qmd",
}

QA_SYSTEM_PROMPT = """You are an expert law professor performing a Quality Assurance review of a Chapter Map extracted from a course textbook chapter.
Your task is to compare the provided Chapter Text (and Slide Digest, if available) against the Chapter Map and produce a detailed Markdown report identifying errors, omissions, and hallucinations.

Please evaluate the map against the following strict criteria:
1. **Completeness**: Note that these maps intentionally exclude non-core materials to focus exclusively on core doctrines taught in class (as outlined in the Slide Digest). Do not penalize the map for omitting tangential or non-core topics. Only flag an omission if a truly fundamental, core doctrine from the chapter text AND slide digest is missing.
2. **Hallucination**: Does the map include cases, doctrines, or "traps" that are NOT actually present or taught in the chapter text?
3. **Trap Formatting**: Traps MUST follow this exact semantic format: "Students choose [Incorrect Answer] because they confuse [Concept A] with [Concept B]." Identify any vague traps or those breaking this pattern.
4. **Seed Generativity**: Are the hypo seeds sufficiently complex to serve as the basis for a law school exam question, or are they trivial variations?

Output a structured Markdown report with the following sections:
- **Summary Verdict**: (Pass / Needs Revision) and a 1-sentence summary.
- **Omissions**: (List missing critical elements, or write "None detected")
- **Hallucinations / Inaccuracies**: (List items in the map not in the text, or write "None detected")
- **Trap Format Violations**: (Quote non-conforming traps and suggest fixes, or write "All conform")
- **Hypo Seed Feedback**: (Qualitative assessment of the seeds)
"""

async def run_qa_for_chapter(chapter_num: int) -> None:
    filename = CHAPTER_FILES.get(chapter_num)
    if not filename:
        print(f"Error: Unknown chapter number: {chapter_num}")
        return

    chapter_path = CHAPTERS_DIR / filename
    map_path = MAPS_DIR / f"chapter-{chapter_num:02d}.md"
    slide_digest_path = SLIDE_DIGESTS_DIR / f"chapter-{chapter_num:02d}-slides.md"
    
    # Fallback to json if md doesn't exist
    if not map_path.exists():
        map_path = MAPS_DIR / f"chapter-{chapter_num:02d}.json"

    if not chapter_path.exists():
        print(f"Error: Chapter file not found: {chapter_path}")
        return
        
    if not map_path.exists():
        print(f"Error: Chapter map not found for chapter {chapter_num} at {map_path.parent}")
        return

    print(f"Running QA for Chapter {chapter_num}...")
    chapter_text = chapter_path.read_text()
    map_text = map_path.read_text()
    slide_digest_text = slide_digest_path.read_text() if slide_digest_path.exists() else ""
    
    prompt = f"### CHAPTER TEXT ###\n{chapter_text}\n\n"
    if slide_digest_text:
        prompt += f"### SLIDE DIGEST (CLASS OVERLAP) ###\n{slide_digest_text}\n\n"
    prompt += f"### EXTRACTED CHAPTER MAP ###\n{map_text}\n\nProvide the QA Report."

    try:
        report = await dispatch_gemini(
            prompt=prompt,
            system_instruction=QA_SYSTEM_PROMPT,
            model="gemini-3.1-pro-preview",
            response_mime_type="text/plain",
            use_diskcache=True
        )
        
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        report_out = REPORTS_DIR / f"qa-report-chapter-{chapter_num:02d}.md"
        report_out.write_text(report)
        print(f"Successfully generated QA report: {report_out}")
    except Exception as e:
        print(f"Failed to run QA for chapter {chapter_num}: {e}")

async def run_all(chapters: list[int] | None = None) -> None:
    if not chapters:
        chapters = list(CHAPTER_FILES.keys())
    
    for ch in chapters:
        await run_qa_for_chapter(ch)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="QA Chapter Maps against Chapters.")
    parser.add_argument("--chapter", "-c", type=int, help="Chapter number to QA")
    parser.add_argument("--all", action="store_true", help="QA all chapters")
    args = parser.parse_args()
    
    if args.all:
        asyncio.run(run_all())
    elif args.chapter:
        asyncio.run(run_all([args.chapter]))
    else:
        parser.print_help()
