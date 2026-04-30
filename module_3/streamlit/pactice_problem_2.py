from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
promt = st.text_input("Enter your prompt",value=None,placeholder="Type your prompt here")


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
if st.button("Generate",type="primary"):
    if promt:
     response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=promt)


    st.markdown(response.text)
else:
    st.write("Please enter a prompt and click the Generate button.")
