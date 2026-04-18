import re
import os

filepath = '/Users/donaldbraman/Documents/GitHub/ag-exams/criminal-law/quiz-system/research/final-exam/master_exam.md'
with open(filepath, 'r') as f:
    text = f.read()

# Pattern to find lines starting with (a), (b), (c), (d), (e) at the beginning of a line
# and format them as bullet points with bolded letters.
# We'll use a regex that matches: ^(\([a-e]\)) (.*)$ and replaces with: - **\1** \2
# We also want to ensure they are parsed correctly even if there's trailing space.

def replacer(match):
    letter = match.group(1)
    content = match.group(2).strip()
    return f"- **{letter}** {content}"

new_text = re.sub(r'^\(([a-e])\)\s+(.*)$', replacer, text, flags=re.MULTILINE)

with open(filepath, 'w') as f:
    f.write(new_text)
print("Updated master_exam.md options layout!")
