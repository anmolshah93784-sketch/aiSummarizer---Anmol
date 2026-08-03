import streamlit as st
import base64
import os
from pdfgen import create_pdf
from summarizer1 import summarize_notes

# Page configuration
st.set_page_config(
    page_title="AKGEC AI Summarizer",
    page_icon="📚",
    layout="centered"
)

# 🛠️ local image ko yha laya by path
def get_local_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

IMAGE_PATH = "bg.jpg"

try:
    if os.path.exists(IMAGE_PATH):
        img_base64 = get_local_image_base64(IMAGE_PATH)
        
        st.markdown(
            f"""
            <style>
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
                color: #1E4620 !important; /* यह सफ़लता वाले हरे बॉक्स के अंदर के टेक्स्ट को कड़क गहरा हरा रखेगा ताकि साफ़ पढ़े */
                font-weight: 700 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
except Exception as e:
    pass
# UI Layout
st.markdown("<h1 class='main-title'>📚 AKGEC AI Notes Summarizer</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #E0E0E0;'>Get instant exam-ready bullet points from your senior AI teacher!</p>", unsafe_allow_html=True)

user_notes = st.text_area("📄 Paste your long college notes below:", height=180, placeholder="Type or paste your content here...")

if st.button("✨ Generate AI Summary", use_container_width=True):
    if user_notes.strip() != "":
        with st.spinner("AI Teacher is reading your notes... Please wait..."):
            summary_result = summarize_notes(user_notes)
            st.success("🎯 Your Exam-Ready Points:")
            st.write(summary_result)
            pdf_data = create_pdf(summary_result)
            
            # pdf button on screen
            st.download_button(
                label="📥 Download Summary as PDF",
                data=pdf_data,
                file_name="AKGEC_AI_Summary.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning("Hey buddy! Please paste some notes first.")
