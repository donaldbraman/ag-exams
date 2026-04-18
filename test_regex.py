import re
text = """**Q1.** What is 1?
(a)
**Answer:** (d)

**Q2.** What is 2?
(a)
**Answer:** (b)
"""
matches = re.findall(r'\*\*Q(\d+)\.\*\*.*?\*\*Answer:\*\*\s*\(([a-e])\)', text, flags=re.DOTALL)
print(matches)
