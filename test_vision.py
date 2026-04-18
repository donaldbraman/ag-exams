import sys
from google import genai
from auth_utils.secrets import get_secret

api_key = get_secret("google-api-key")
client = genai.Client(api_key=api_key)

try:
    print("Uploading file...")
    img_file = client.files.upload(file='/Users/donaldbraman/.gemini/antigravity/brain/245cd57a-3eb6-4b01-8279-05ee40caa264/page_1.png')
    response = client.models.generate_content(
        model='gemini-3-pro-preview',
        contents=["Describe this image briefly.", img_file]
    )
    print("SUCCESS:", response.text)
except Exception as e:
    print("FAILED:", str(e))
    import traceback
    traceback.print_exc()
