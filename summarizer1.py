from huggingface_hub import InferenceClient
import streamlit as st

HF_TOKEN = st.secrets["HF_TOKEN"]
client = InferenceClient(api_key=HF_TOKEN)

def summarize_notes(My_notes):
    response = client.chat_completion(
        model="Qwen/Qwen2.5-Coder-7B-Instruct",
        messages=[
            {"role": "user", "content": f"You are a professor and you have to summarize the given notes in bullet points step by step and also give some notes related exam ready questions & answers or solve numericals if asked:\n\n{My_notes}"}
        ],
        max_tokens=500
    )
    return response['choices'][0]['message']['content']
