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