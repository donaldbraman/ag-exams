import re
text = open("quiz-5-fixed-v2.md").read()
stem_blocks = list(re.finditer(r"(## Stem \d+.*?(?=### Questions))", text, re.DOTALL))
print("Stems found:", len(stem_blocks))
for i, sb in enumerate(stem_blocks):
    print(f"Stem {i} length: {len(sb.group(1))}")
    print(f"Stem {i} snippet: {sb.group(1)[:100]}...\n")

q_matches = list(re.finditer(r"(\*\*Q\d+\.\*\*.*?(?=\*\*Q\d+\.\*\*|---|\Z|## Coverage Summary))", text, re.DOTALL))
print("Questions found:", len(q_matches))
if q_matches:
    print(f"Q1 length: {len(q_matches[0].group(1))}")
    print(f"Q1 snippet: {q_matches[0].group(1)[:100]}...\n")
