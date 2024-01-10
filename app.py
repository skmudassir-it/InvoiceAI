from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro-vision')

def get_resp(inp, image, prompt):
    response = model.generate_content([inp, image[0], prompt])
    return response.text

def inp_imgSetup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]

st.set_page_config(page_title="Automatic AI Invoice Extractor")
st.header("AI Invoice Extractor")
input=st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the invoice")

inp_prompt = """
you are an expert in understanding invoices. we will upload a image as invoices, 
and you will have to answer any question based on the invoice image provided
"""

if submit:
    image