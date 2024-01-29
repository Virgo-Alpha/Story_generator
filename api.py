
# // TODO: Get a free LLM API
# // TODO: Test the API using a simple prompt

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the Gemini API key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

genai.configure(api_key = gemini_api_key)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Who is the GOAT in the NBA?")

print(response.text)
