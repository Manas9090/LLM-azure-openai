import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Azure OpenAI credentials
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")    # ex: https://manasazure.openai.azure.com/
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")  # 👈 pulled from .env dynamically

st.title("💬 Azure OpenAI Chatbot")

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                engine=os.getenv("AZURE_OPENAI_DEPLOYMENT"),  # ex: gpt-4.1
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success(response['choices'][0]['message']['content'])
    else:
        st.warning("Please enter a message.")
