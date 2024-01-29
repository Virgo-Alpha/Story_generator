import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the Gemini API key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')

def create_story(prompt: str):
    response = model.generate_content(
        f"Create a 3 act story of less than 500 words about {prompt}"
    )
    return response.text

# Streamlit app
def main():
    st.title("Story Generator")

    # Get user input prompt
    prompt = st.text_input("Enter your prompt:")

    if st.button("Generate Story"):
        if prompt:
            # Generate story based on the prompt
            story = create_story(prompt)

            # Button to clear the response
            if st.button("Clear Response"):
                st.text_input("Enter your prompt:", value="", key="clear_key")
                st.text("Response Cleared.")

            # Display the result
            st.header("**Generated Story:**")
            st.write(f"\n{story}")

        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
