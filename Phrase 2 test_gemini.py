import os
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# Test multimodal connectivity
model = genai.GenerativeModel("gemini-1.5-flash-pro")
response = model.generate_content("Hello PocketSmartAI, confirm AI connectivity.")
print("Gemini Response:", response.text)