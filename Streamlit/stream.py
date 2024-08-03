import streamlit as st
import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()
model = genai.GenerativeModel(model_name='gemini-1.0-pro')

st.title("Sentiment Classification")

feedback=st.text_input("Enter the Feedback")


def prompt(feedback):
    prompt_template=f"""
        ### Role:
        - You are Sentiment Classification model. 

        ### feedback:
        {feedback}

        ### Task :
        - Classify feedback into "P" or "N" category.

        ### Guidelines:
        - return only category in output .
        
        ### Example:
        1.feedback : what a lovely product.
        sentiment:P
        2. feedback : poor quality product.
        sentiment:N

    """
    res=model.generate_content(prompt_template)
    return res.text

if st.button("Classify"):
    result=prompt(feedback)
    st.header(result)