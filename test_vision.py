import sys
from google import genai
from auth_utils.secrets import get_secret

api_key = get_secret("google-api-key")
client = genai.Client(api_key=api_key)

try:
    print("Uploading page 3...")
    img_file = client.files.upload(file='/Users/donaldbraman/.gemini/antigravity/brain/245cd57a-3eb6-4b01-8279-05ee40caa264/page_3.png')
    response = client.models.generate_content(
        model='gemini-3-pro-preview',
        contents=["Look closely at the multiple-choice answer options (a, b, c, etc.) on this page. Are they tightly packed together on adjacent lines, or is there a clear, empty vertical space (a blank line) between each option?", img_file]
    )
    print("VISION PROOF:", response.text)
except Exception as e:
    print("FAILED:", str(e))
