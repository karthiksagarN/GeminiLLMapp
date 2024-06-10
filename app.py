from dotenv import load_dotenv

load_dotenv()  # loading the environment variables

import streamlit as st
import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# func to load gemini pro model

model = genai.GenerativeModel("gemini-pro")

def get_response(question):
    response = model.generate_content(question)

    return response.text


## initialze streamlit app

