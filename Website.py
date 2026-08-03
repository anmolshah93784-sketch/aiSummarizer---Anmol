import streamlit as st
import base64
import os
from pdfgen import create_pdf
from summarizer1 import summarize_notes

# 1.heading
st.set_page_config(
    page_title="AKGEC AI Summarizer",
    page_icon="📚",
    layout="centered"
)
# bg.jpg into data form
def get_local_image_base64(image_file):
    with open(image_file, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#check bg.jpg exist or not
try:
    img_base64 = get_local_image_base64("bg.jpg")
    st.markdown(
        f"""
        <style>
        /* set bg */
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), 
                              url("data:image/jpg;base64,{img_base64}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
            background-color: transparent !important;
        }}
        .main-title {{
            color: #FFFFFF !important;
            text-align: center;
            font-family: 'Poppins', sans-serif;
            font-weight: 800;
            text-shadow: 3px 3px 6px #000000;
        }}
        .stTextArea label {{
            color: #FFFFFF !important;
            font-weight: 600;
            text-shadow: 1px 1px 2px #000000;
        }}
        .stMarkdown p, .stMarkdown li {{
            color: #FFFFFF !important;
            font-size: 16px !important;
            font-weight: 500 !important;
            text-shadow: 1px 1px 3px #000000 !important;
        }}
        
        .stAlert p {{
            color: #1E4620 !important;
            font-weight: 700 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
except Exception as e:
    pass

# 3. set (UI)
st.markdown("<h1 class='main-title'>📚 AKGEC AI Notes Summarizer</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #E0E0E0;'>Get instant exam-ready bullet points from your senior AI teacher!</p>", unsafe_allow_html=True)

user_notes = st.text_area("📄 Paste your long college notes below:", height=180, placeholder="Type or paste your content here...")

if st.button("✨ Generate AI Summary", use_container_width=True):
    if user_notes.strip() != "":
        with st.spinner("AI Teacher is reading your notes... Please wait..."):
            summary_result = summarize_notes(user_notes)
            st.success("🎯 Your Exam-Ready Points:")
            st.write(summary_result)
            
            # PDF button
            pdf_data = create_pdf(summary_result)
            st.download_button(
                label="📥 Download Summary as PDF",
                data=pdf_data,
                file_name="AKGEC_AI_Summary.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning("Hey buddy! Please paste some notes first.")
