import sys
import os
import re
sys.path.insert(0, os.path.abspath("src"))
from ag_exams.activities import extract_grounding_verdict, extract_audit_verdict, extract_edge_case_verdict, extract_argument_pass_verdict

with open("qa_results_round5.md") as f:
    text = f.read()

questions = re.split(r"## (Q\d+)", text)[1:]
q_names = questions[0::2]
q_texts = questions[1::2]

print("| Q | Grounding | Ambiguity | Edge Case | Sonnet Arg | Opus Arg |")
print("|---|---|---|---|---|---|")

for name, q_text in zip(q_names, q_texts):
    gr = extract_grounding_verdict(q_text)
    
    am_sec = q_text.split("### Edge Case Audit")[0] if "### Edge Case Audit" in q_text else q_text
    am = extract_audit_verdict(am_sec)
    
    ec_sec = q_text.split("### Argument Pass")[0] if "### Argument Pass" in q_text else q_text
    ec = extract_edge_case_verdict(ec_sec)
    
    son_sec = q_text.split("### Argument Pass (Opus)")[0] if "### Argument Pass (Opus)" in q_text else q_text
    son = extract_argument_pass_verdict(son_sec)
    
    op_sec = q_text.split("### Argument Pass (Opus)")[1] if "### Argument Pass (Opus)" in q_text else q_text
    op = extract_argument_pass_verdict(op_sec)
    
    print(f"| {name} | {gr} | {am} | {ec} | {son} | {op} |")

