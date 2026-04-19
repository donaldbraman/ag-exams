import re
import os

files = [
    "criminal-law/quiz-system/research/final-exam/mock_master_exam.md",
    "criminal-law/quiz-system/research/final-exam/mock_student_exam.md",
    "criminal-law/quiz-system/research/final-exam/final_master_exam.md",
    "criminal-law/quiz-system/research/final-exam/final_student_exam.md"
]

def post_process(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    
    with open(filepath, 'r') as f:
        text = f.read()

    # 1. fix_quarto_lists logic: Replace `- **a** ` with `a. `
    def replacer(match):
        letter = match.group(1)
        return f"{letter}. "
    text = re.sub(r'^- \*\*([a-e])\*\*\s+', replacer, text, flags=re.MULTILINE)

    # 2. make_lists_loose logic: Add sub-list spacing
    # Add a newline before any numbered list item (except if already preceded by a newline)
    text = re.sub(r'([^\n])\n(\d+\.\s)', r'\1\n\n\2', text)
    # Add a newline before any alphabetical list item a. b. c. d. e.
    text = re.sub(r'([^\n])\n([a-e]\.\s)', r'\1\n\n\2', text)

    with open(filepath, 'w') as f:
        f.write(text)
    print(f"Processed {filepath}")

for f in files:
    post_process(f)
