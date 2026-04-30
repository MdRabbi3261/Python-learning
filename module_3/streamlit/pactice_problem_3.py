from google import genai
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()
st.title("Sentence Improver ✨")
st.write("Improve your sentence professionally")

promt = st.text_input("Enter your sentence:",value=None,placeholder="Type your sentence here")


api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
if st.button("Generate",type="primary"):
    if promt:
     prompt = f"Improve this sentence professionally: {promt}"
            
     response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=promt)

    st.subheader("Improved Sentence:")
    st.markdown(response.text)
else:
    st.write("Please enter a sentence and click the Generate button.")
