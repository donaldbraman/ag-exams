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
STUDENT_OUTPUT_FILE = os.path.join(BASE_DIR, "student_mock_exam.md")

def format_options(text: str) -> str:
    """Format (a) options to alphabetical list items `a.` and make them loose."""
    # Convert `(a) ` to `a. `
    text = re.sub(r'^\(([a-e])\)\s+(.*)$', r'\1. \2', text, flags=re.MULTILINE)
    pass
    
    return text

def main():
    print(f"Assembling {OUTPUT_FILE}...")
    
    global_q_num = 1
    answer_key = []

    # YAML Frontmatter
    md_lines = [
        "---",
        "format:",
        "  pdf:",
        "    geometry:",
        "      - top=1in",
        "      - bottom=1in",
        "      - left=1.25in",
        "      - right=1.25in",
        "    include-in-header:",
        "      text: |",
        "        \\usepackage{enumitem}",
        "        \\setlist{itemsep=0.0em}",
        "        \\def\\tightlist{}",
        "        \\usepackage{multicol}",
        "---"
    ]
    student_md_lines = list(md_lines)
    
    for idx, scenario_name in enumerate(SCENARIOS, start=1):
        # Format the title, stripping 'Mock'
        # mock_the_genesis -> The Genesis
        base_title = scenario_name.replace("mock_", "").replace("_", " ").title()
        # Fix words like 'The' if needed, though .title() works fine here for 'The Genesis'
        title = f"# Scenario {idx}: {base_title}"
        md_lines.append(title)
        md_lines.append("")
        student_md_lines.append(title)
        student_md_lines.append("")
        
        # Read the scenario JSON
        scenario_file = os.path.join(BASE_DIR, f"{scenario_name}-scenario.md")
        try:
            with open(scenario_file, "r") as f:
                content = f.read().strip()
                data = json.loads(content)
                
                md_lines.append("### Facts")
                md_lines.append("")
                student_md_lines.append("### Facts")
                student_md_lines.append("")
                for i, fact in enumerate(data.get("facts", [])):
                    md_lines.append(f"{i+1}. {fact}")
                    md_lines.append("")
                    student_md_lines.append(f"{i+1}. {fact}")
                    student_md_lines.append("")
                    
                md_lines.append("### Characters")
                md_lines.append("")
                student_md_lines.append("### Characters")
                student_md_lines.append("")
                for char in data.get("characters", []):
                    char_line = f"- **{char['name']}** ({char['role']}): {char['doctrinal_target']}"
                    md_lines.append(char_line)
                    student_md_lines.append(char_line)
                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")
                student_md_lines.append("")
                student_md_lines.append("---")
                student_md_lines.append("")
                
        except json.JSONDecodeError as e:
            print(f"Error decoding {scenario_file}: {e}")
            continue
            
        # Read the randomized questions
        questions_file = os.path.join(BASE_DIR, f"{scenario_name}-questions-randomized.md")
        try:
            with open(questions_file, "r") as f:
                q_text = f.read()
                
                # Make question numbers sequential
                def replace_q_num(match):
                    nonlocal global_q_num
                    rep = f"**Q{global_q_num}.**"
                    global_q_num += 1
                    return rep
                
                q_text = re.sub(r'\*\*Q\d+\.\*\*', replace_q_num, q_text)
                
                # Remove Tags lines
                q_text = re.sub(r'^\*\*Tags:\*\*.*(?:\n|$)', '', q_text, flags=re.MULTILINE)
                
                # Remove Grounding lines
                q_text = re.sub(r'^\*\*Grounding:\*\*.*(?:\n|$)', '', q_text, flags=re.MULTILINE)
                
                md_lines.append(q_text)
                if not q_text.endswith("\n"):
                    md_lines.append("")
                
                # Create student version of q_text
                student_q_text = re.sub(r'^\*\*Answer:\*\*.*(?:\n|$)', '', q_text, flags=re.MULTILINE)
                student_q_text = re.sub(r'^\*\*Explanation:\*\*.*(?:\n|$)', '', student_q_text, flags=re.MULTILINE)
                student_q_text = re.sub(r'\s*<!--\s*correct\s*-->', '', student_q_text)
                
                student_md_lines.append(student_q_text)
                if not student_q_text.endswith("\n"):
                    student_md_lines.append("")
                
                # Extract answers for the answer key
                matches = re.findall(r'\*\*Q(\d+)\.\*\*.*?\*\*Answer:\*\*\s*\(([a-e])\)', q_text, flags=re.DOTALL)
                scenario_answers = []
                for q_num, ans in matches:
                    scenario_answers.append((int(q_num), ans.upper()))
                if scenario_answers:
                    answer_key.append({"title": title, "answers": scenario_answers})
        except FileNotFoundError:
            print(f"Warning: {questions_file} not found. Skipping questions for {scenario_name}.")
            
    if answer_key:
        answer_key_lines = [
            "\\newpage",
            "# Answer Key",
            ""
        ]
        for scenario in answer_key:
            s_title = scenario["title"].lstrip("# ")
            answer_key_lines.append(f"### {s_title}")
            answer_key_lines.append("")
            answer_key_lines.append("\\begin{multicols}{4}")
            answer_key_lines.append("\\noindent")
            
            scenario_answers = sorted(scenario["answers"], key=lambda x: x[0])
            for q_num, ans in scenario_answers:
                answer_key_lines.append(f"\\textbf{{{q_num}.}} {ans}\\\\")
                
            answer_key_lines.append("\\end{multicols}")
            answer_key_lines.append("")
            
        md_lines.extend(answer_key_lines)
        student_md_lines.extend(answer_key_lines)

    full_text = "\n".join(md_lines)
    student_full_text = "\n".join(student_md_lines)
    
    # Apply formatting
    formatted_text = format_options(full_text)
    student_formatted_text = format_options(student_full_text)
    
    with open(OUTPUT_FILE, "w") as f:
        f.write(formatted_text)
        
    with open(STUDENT_OUTPUT_FILE, "w") as f:
        f.write(student_formatted_text)
        
    print(f"Assembly complete! Run `quarto render` to build the PDFs.")

if __name__ == "__main__":
    main()
