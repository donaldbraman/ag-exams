import asyncio
import os
import sys

# Add src to python path so we can import ag_exams
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from ag_exams.gemini_client import dispatch_gemini

async def main():
    print("Testing Gemini client with a prompt that typically triggers safety filters...")
    
    # This prompt is designed to test criminal law fact patterns which can trip safety filters 
    # without BLOCK_NONE settings.
    prompt = (
        "Write a legally detailed scenario involving a gruesome homicide, "
        "aggravated assault with a deadly weapon, and burglary. "
        "This is for a criminal law exam fact pattern to test law students on criminal liability. "
        "Include specific details about the actus reus and mens rea."
    )
    
    try:
        response = await dispatch_gemini(
            prompt=prompt,
            # We use a non-diskcache call to make sure we actually hit the API
            use_diskcache=False
        )
        print("\n✅ SUCCESS: Safety filters were successfully bypassed!")
        print("-" * 40)
        print("Response snippet (first 300 chars):")
        print(response[:300] + "...")
        print("-" * 40)
    except Exception as e:
        print(f"\n❌ FAILED: Exception occurred during API call: {e}")

if __name__ == "__main__":
    asyncio.run(main())
