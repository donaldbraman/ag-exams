import re
text = open("qa_results_round2.md").read()
q03 = re.split(r"## Q03\n", text)[1]
am_sec = q03.split("### Edge Case Audit")[0]
print(am_sec)
