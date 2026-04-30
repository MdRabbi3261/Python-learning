import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

# load env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# client
client = genai.Client(api_key=api_key)

# uploader
images = st.file_uploader(
    "Upload the Photos of your note",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if images:
    pil_images = []

    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)

  
   

    prompt = """Summarize the picture in note format (max 100 words).
Make sure to add necessary markdown to differentiate sections."""

    # API call
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=pil_images+[ prompt]
    )

    st.text(response.text)