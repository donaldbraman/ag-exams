import json
import glob
import os

files = glob.glob("criminal-law/quiz-system/research/final-exam/*-scenario.md")

for scenario_file in files:
    base = scenario_file.replace("-scenario.md", "")
    questions_file = base + "-questions.md"
    out_file = base + "-full-exam.md"
    
    with open(scenario_file, "r") as f:
        content = f.read().strip()
        
    title = f"# {os.path.basename(base)} Scenario"
    
    try:
        data = json.loads(content)
        
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
    except json.JSONDecodeError as e:
        print(f"Error decoding {scenario_file}: {e}")
        scenario_md = f"{title}\n\n{content}\n\n---\n\n"
        
    with open(questions_file, "r") as f:
        questions_md = f.read()
        
    with open(out_file, "w") as f:
        f.write(scenario_md + questions_md)
        
    print(f"Formatted {out_file}")
