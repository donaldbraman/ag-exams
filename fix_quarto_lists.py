import re

filepath = '/Users/donaldbraman/Documents/GitHub/ag-exams/criminal-law/quiz-system/research/final-exam/master_exam.md'
with open(filepath, 'r') as f:
    text = f.read()

# Replace `- **a** ` with `a. `
def replacer(match):
    letter = match.group(1)
    return f"{letter}. "

# The regex looks for line start, dash, space, bold letter, space
new_text = re.sub(r'^- \*\*([a-e])\*\*\s+', replacer, text, flags=re.MULTILINE)

with open(filepath, 'w') as f:
    f.write(new_text)
print("Updated to alphabetical ordered lists!")
