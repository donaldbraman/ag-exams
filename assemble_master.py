#!/usr/bin/env python3
import json
import os
import re

SCENARIOS = [
    "mock_the_genesis",
    "mock_the_distribution_ring",
    "mock_the_empire_business",
    "mock_the_blowback",
    "mock_the_cornered_defenses"
]

BASE_DIR = "criminal-law/quiz-system/research/final-exam"
OUTPUT_FILE = os.path.join(BASE_DIR, "master_exam.md")

def format_options(text: str) -> str:
    """Format (a) options to alphabetical list items `a.` and make them loose."""
    # Convert `(a) ` to `a. `
    text = re.sub(r'^\(([a-e])\)\s+(.*)$', r'\1. \2', text, flags=re.MULTILINE)
    
    # Add a newline before any numbered list item (except if already preceded by a newline)
    text = re.sub(r'([^\n])\n(\d+\.\s)', r'\1\n\n\2', text)

    # Add a newline before any alphabetical list item a. b. c. d. e.
    text = re.sub(r'([^\n])\n([a-e]\.\s)', r'\1\n\n\2', text)
    
    return text

def main():
    print(f"Assembling {OUTPUT_FILE}...")
    
    # YAML Frontmatter
    md_lines = [
        "---",
        "format:",
        "  pdf:",
        "    include-in-header:",
        "      text: |",
        "        \\usepackage{enumitem}",
        "        \\setlist{itemsep=0.25em}",
        "---"
    ]
    
    for idx, scenario_name in enumerate(SCENARIOS, start=1):
        # Format the title, stripping 'Mock'
        # mock_the_genesis -> The Genesis
        base_title = scenario_name.replace("mock_", "").replace("_", " ").title()
        # Fix words like 'The' if needed, though .title() works fine here for 'The Genesis'
        title = f"# Scenario {idx}: {base_title}"
        md_lines.append(title)
        md_lines.append("")
        
        # Read the scenario JSON
        scenario_file = os.path.join(BASE_DIR, f"{scenario_name}-scenario.md")
        try:
            with open(scenario_file, "r") as f:
                content = f.read().strip()
                data = json.loads(content)
                
                md_lines.append("### Facts")
                md_lines.append("")
                for i, fact in enumerate(data.get("facts", [])):
                    md_lines.append(f"{i+1}. {fact}")
                    md_lines.append("")
                    
                md_lines.append("### Characters")
                md_lines.append("")
                for char in data.get("characters", []):
                    md_lines.append(f"- **{char['name']}** ({char['role']}): {char['doctrinal_target']}")
                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")
                
        except json.JSONDecodeError as e:
            print(f"Error decoding {scenario_file}: {e}")
            continue
            
        # Read the randomized questions
        questions_file = os.path.join(BASE_DIR, f"{scenario_name}-questions-randomized.md")
        try:
            with open(questions_file, "r") as f:
                q_text = f.read()
                md_lines.append(q_text)
                if not q_text.endswith("\n"):
                    md_lines.append("")
        except FileNotFoundError:
            print(f"Warning: {questions_file} not found. Skipping questions for {scenario_name}.")
            
    full_text = "\n".join(md_lines)
    
    # Apply formatting
    formatted_text = format_options(full_text)
    
    with open(OUTPUT_FILE, "w") as f:
        f.write(formatted_text)
        
    print("Assembly complete! Run `quarto render` to build the PDF.")

if __name__ == "__main__":
    main()
