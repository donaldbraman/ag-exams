import json
import glob
import os

files = glob.glob("criminal-law/quiz-system/research/final-exam/*-scenario.md")

for scenario_file in files:
    base = scenario_file.replace("-scenario.md", "")
    questions_file = base + "-questions.md"
    out_file = base + "-full-exam.md"
    
    with open(scenario_file, "r") as f:
        content = f.read()
        
    # The scenario file has a title "# <name> Scenario" then JSON
    lines = content.split("\n")
    title = lines[0]
    json_str = "\n".join(lines[2:])
    
    try:
        data = json.loads(json_str)
        
        md_lines = [title, ""]
        md_lines.append("## Fact Pattern")
        for i, fact in enumerate(data.get("facts", [])):
            md_lines.append(f"{i+1}. {fact}")
            
        md_lines.append("")
        md_lines.append("## Characters")
        for char in data.get("characters", []):
            md_lines.append(f"- **{char['name']}** ({char['role']}): {char['doctrinal_target']}")
            
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
        
        scenario_md = "\n".join(md_lines)
    except json.JSONDecodeError:
        scenario_md = content
        
    with open(questions_file, "r") as f:
        questions_md = f.read()
        
    with open(out_file, "w") as f:
        f.write(scenario_md + questions_md)
        
    print(f"Formatted {out_file}")
