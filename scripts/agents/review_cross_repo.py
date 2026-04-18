import asyncio
import sys
from pathlib import Path
import glob

# Add src to path so we can import ag_exams
sys.path.append('/Users/donaldbraman/Documents/GitHub/ag-exams/src')
from ag_exams.gemini_client import dispatch_gemini

async def main():
    base_dir = Path('/Users/donaldbraman/Documents/GitHub/cross-repo')
    guides_dir = base_dir / ".claude" / "guides"
    
    files_to_read = [base_dir / "CLAUDE.md"]
    files_to_read.extend(Path(p) for p in glob.glob(str(guides_dir / "*.md")))
    
    context = ""
    for file_path in files_to_read:
        if file_path.exists():
            context += f"\n\n--- [FILE: {file_path.name}] ---\n\n"
            try:
                context += file_path.read_text()
            except Exception as e:
                print(f"Could not read {file_path.name}: {e}")

    # Read current Rosetta Stone
    rosetta_path = Path('/Users/donaldbraman/Documents/GitHub/ag-exams/.antigravity/knowledge/antigravity_workflow_patterns/artifacts/workflow_patterns.md')
    current_rosetta = rosetta_path.read_text()

    prompt = f"""
    You are a Principal AI Architect. We have a foundational "Rosetta Stone" document that translates master cross-repo engineering principles (originally written for terminal-based CLI agents like Claude Code) into the specific operational paradigm of the Antigravity + Gemini AI agent, which operates natively inside the IDE using UI artifacts, conversational brain logs, and Temporal workflows.
    
    Here is the current draft of the Rosetta Stone:
    {current_rosetta}
    
    Below is the massive context dump containing all 35 organizational guides from the "cross-repo":
    {context}
    
    YOUR TASK:
    Deep read the massive context dump. Identify every other major engineering principle, workflow loop, or architectural standard that is highly relevant to `ag-exams` and general Antigravity operations (e.g., iterative review loops, fact-checking, swarm operations, Github label schemas, agent messaging).
    
    For every relevant principle you find, you must adapt it to the Antigravity paradigm.
    Example adaptation pattern:
    **Cross-Repo Goal:** [The goal]
    **Antigravity Implementation:** [How Antigravity achieves this natively without brittle bash scripts, terminal worktrees, or redundant files]
    
    Output the final, comprehensive Markdown document. It should start with `# Antigravity Workflow Patterns` and contain both the existing principles and all the new ones you discover. Return ONLY the markdown. Be brutally rigorous and actionable.
    """
    
    print("Dispatching to gemini-3.1-pro-preview...")
    result = await dispatch_gemini(
        prompt=prompt,
        system_instruction="You are a Principal AI Architect writing the master Rosetta Stone.",
        model="gemini-3.1-pro-preview",
    )
    
    # Strip any ```markdown codeblock wrapping if it exists
    if result.startswith("```markdown"):
        result = result[11:]
        if result.endswith("```"):
            result = result[:-3]
    
    rosetta_path.write_text(result.strip())
    print("Analysis complete. Rosetta Stone updated.")

if __name__ == "__main__":
    asyncio.run(main())
