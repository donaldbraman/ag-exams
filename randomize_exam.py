#!/usr/bin/env python3
import sys
import re
import random
from pathlib import Path

def randomize_exam_options(questions_text: str) -> str:
    """Randomize the options of all questions in the exam text to ensure an even distribution of answer keys."""
    blocks = re.split(r'\n---\n', questions_text)
    
    valid_blocks = []
    for i, b in enumerate(blocks):
        # Find blocks that start with **Q<number>.**
        if re.search(r"^\*\*Q\d+\.\*\*", b.strip(), re.MULTILINE):
            valid_blocks.append((i, b.strip()))
            
    num_qs = len(valid_blocks)
    if num_qs == 0:
        print("No valid questions found in the file.")
        return questions_text
        
    # Create an even pool of target answers
    targets = []
    letters = ['a', 'b', 'c', 'd', 'e']
    for i in range(num_qs):
        targets.append(letters[i % 5])
        
    # Shuffle the target answers to distribute them randomly across the exam
    random.shuffle(targets)
    
    for idx, (original_i, block_text) in enumerate(valid_blocks):
        target_ans = targets[idx]
        options = {}
        
        # Match (a) through (e) options precisely
        opt_matches = list(re.finditer(r'^\(([a-e])\)\s+(.+?)(?=\n\n|\n\(|\n\*\*Answer|\Z)', block_text, re.MULTILINE | re.DOTALL))
        if len(opt_matches) != 5:
            continue
            
        for m in opt_matches:
            options[m.group(1)] = m.group(2).strip()
            
        ans_match = re.search(r'\*\*Answer:\*\*\s*\(([a-e])\)', block_text)
        if not ans_match:
            continue
            
        current_ans = ans_match.group(1)
        if current_ans not in options:
            continue
            
        correct_text = options[current_ans]
        distractors = [options[k] for k in options if k != current_ans]
        
        # Shuffle the distractors so their relative order is random
        random.shuffle(distractors)
        
        new_options = {}
        dist_idx = 0
        for l in letters:
            if l == target_ans:
                new_options[l] = correct_text
            else:
                new_options[l] = distractors[dist_idx]
                dist_idx += 1
                
        # Splice the new options back into the text block
        start_opt = opt_matches[0].start()
        end_opt = opt_matches[-1].end()
        new_opt_text = "\n".join([f"({l}) {new_options[l]}" for l in letters])
        new_block = block_text[:start_opt] + new_opt_text + block_text[end_opt:]
        
        # Update the **Answer:** key
        new_block = re.sub(r'\*\*Answer:\*\*\s*\([a-e]\)', f'**Answer:** ({target_ans})', new_block)
        blocks[original_i] = new_block
        
    return "\n\n---\n\n".join(blocks)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python randomize_exam.py <path_to_markdown_file>")
        sys.exit(1)
        
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)
        
    text = file_path.read_text()
    
    # Calculate original distribution
    original_answers = re.findall(r'\*\*Answer:\*\*\s*\(([a-e])\)', text)
    orig_dist = {l: original_answers.count(l) for l in ['a', 'b', 'c', 'd', 'e']}
    print("Original Answer Distribution:", orig_dist)
    
    new_text = randomize_exam_options(text)
    
    # Calculate new distribution
    new_answers = re.findall(r'\*\*Answer:\*\*\s*\(([a-e])\)', new_text)
    new_dist = {l: new_answers.count(l) for l in ['a', 'b', 'c', 'd', 'e']}
    print("New Answer Distribution:     ", new_dist)
    
    out_path = file_path.with_name(f"{file_path.stem}-randomized{file_path.suffix}")
    out_path.write_text(new_text)
    print(f"\nRandomized exam safely written to new file: {out_path}")
