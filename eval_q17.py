import asyncio
import os
import sys
import re

sys.path.insert(0, os.path.abspath("src"))
from ag_exams.gemini_client import dispatch_gemini

async def main():
    with open("criminal-law/quiz-system/research/chapter-maps/chapter-22.md", "r") as f:
        ch22 = f.read()
    with open("criminal-law/quiz-system/research/chapter-maps/chapter-23.md", "r") as f:
        ch23 = f.read()
    with open("quiz-5-fixed-v3.md", "r") as f:
        quiz = f.read()
    
    q_match = re.search(r"(\*\*Q17\.\*\*.*?)(?=\*\*Q18\.\*\*|\Z)", quiz, re.DOTALL)
    if not q_match:
        print("Could not find Q17")
        return
    q17 = q_match.group(1)
    
    prompt = f"""
You are an expert criminal law professor. Please evaluate the following multiple-choice question against the provided text for Chapter 22 (Self-Defense) and Chapter 23 (Insanity).

Specifically, evaluate whether the 'correct' answer and the explanation align perfectly with the doctrine established in the chapters. Is the question doctrinally accurate, or does it misstate the rules from the chapters? Pay special attention to the nuances around purely delusional beliefs, imperfect self-defense in California under Elmore/Schuller, and Kahler v. Kansas.

### Chapter 22
{ch22}

### Chapter 23
{ch23}

### Question 17
{q17}

Provide a comprehensive analysis of the doctrinal accuracy of the question, the options, and the explanation.
"""
    try:
        result = await dispatch_gemini(
            prompt=prompt,
            system_instruction="You are a legal expert reviewing an exam question for accuracy against assigned readings.",
            use_diskcache=False
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
