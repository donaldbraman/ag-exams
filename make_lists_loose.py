import re

filepath = '/Users/donaldbraman/Documents/GitHub/ag-exams/criminal-law/quiz-system/research/final-exam/master_exam.md'
with open(filepath, 'r') as f:
    text = f.read()

# Add a newline before any numbered list item (except if already preceded by a newline)
text = re.sub(r'([^\n])\n(\d+\.\s)', r'\1\n\n\2', text)

# Add a newline before any alphabetical list item a. b. c. d. e.
text = re.sub(r'([^\n])\n([a-e]\.\s)', r'\1\n\n\2', text)

with open(filepath, 'w') as f:
    f.write(text)

print("Inserted blank lines to create loose lists!")
