from dotenv import load_dotenv

load_dotenv()  # loading the environment variables

import streamlit as st
import base64
import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# func to load gemini pro model

model = genai.GenerativeModel("gemini-pro")

def get_response(question):
    response = model.generate_content(question)

    return response.text

## initialze streamlit app

st.set_page_config(page_title=" Question Answer Demo", page_icon="💎")

# Function to set a background image
def set_background(image_file):
    with open(image_file, "rb") as image:
        b64_image = base64.b64encode(image.read()).decode("utf-8")
    css = f"""
    <style>
    .stApp {{
        background: url(data:image/png;base64,{b64_image});
        background-size: cover;
        background-position: centre;
        backgroun-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set the background image
set_background("background_image.png")

st.header("Gemini LLM Application")

input = st.text_input("Input : ", key = "input")
submit = st.button("Ask the question")

## when submit button is clicked

if submit:
    response = get_response(input)

    st.subheader("Bot Response : ")
    st.write(response)


