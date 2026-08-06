from huggingface_hub import InferenceClient
import streamlit as st

HF_TOKEN = st.secrets["HF_TOKEN"]
client = InferenceClient(api_key=HF_TOKEN)

def summarize_notes(My_notes):
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {"role": "user", "content": f"You are a professor and you have to summarize the notes in bullet points and At last, Also give some notes related exam ready questions with answers:\n\n{My_notes}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content
