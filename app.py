import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Azure OpenAI credentials
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")    # example: https://manasazure.openai.azure.com/
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = "2024-02-01"  # MUST be this for ChatCompletion

# Streamlit UI
st.title("💬 Azure OpenAI Chatbot")

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                engine="gpt-4.1",   # 👈 give deployment name here
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success(response['choices'][0]['message']['content'])
    else:
        st.warning("Please enter a message.")
