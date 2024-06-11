## Implementing the chatbot which displays history also

import os
from dotenv import load_dotenv
import streamlit as st
import base64
import google.generativeai as genai

load_dotenv()  # loading the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# func to load gemini pro model

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_response(question):
    response = chat.send_message(question, stream=True)
    return response

## initialze streamlit app

st.set_page_config(page_title=" Question Answer Demo")

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

## initialize session state for chat history if it doesn't exist

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input : ", key = "input")
submit = st.button("Ask the question")

if submit and input:
    response = get_response(input)
    # add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("Chat History:")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
