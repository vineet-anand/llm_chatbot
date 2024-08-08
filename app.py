from langchain.llms import OpenAI
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st

def get_openai_response(question):
    llm= OpenAI(
                openai_api_key= os.environ["OPENAI_API_KEY"],
                model_name="gpt-3.5-turbo", 
                temperature = 0.6
                )
    response = llm(question)
    return response


st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)
submit = st.button("Ask the Question")

if submit:
    st.header("The Response is: ")
    st.write(response)