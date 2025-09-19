# test_api.py
from dotenv import load_dotenv
import os
import google.generativeai as genai
from openai import OpenAI

# Load .env file
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# --- Test OpenAI ---
def test_openai():
    try:
        client = OpenAI(api_key=OPENAI_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello from Farmer Chatbot!"}]
        )
        print("✅ OpenAI Response:", response.choices[0].message.content)
    except Exception as e:
        print("❌ OpenAI Error:", e)

# --- Test Gemini ---
def test_gemini():
    try:
        genai.configure(api_key=GEMINI_KEY)
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content("Hello from Farmer Chatbot!")
        print("✅ Gemini Response:", response.text)
    except Exception as e:
        print("❌ Gemini Error:", e)

if __name__ == "__main__":
    test_openai()
    test_gemini()
