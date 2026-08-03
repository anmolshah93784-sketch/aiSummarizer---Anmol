import streamlit as st
from pdfgen import create_pdf
from summarizer1 import summarize_notes

# 1.heading
st.set_page_config(
    page_title="AKGEC AI Summarizer",
    page_icon="📚",
    layout="centered"
)
# 2.Theme bg
st.markdown(
    """
    <style>
    /* bg dark grey black */
    .stApp {
        background-color: #0E1117 !important;
    }
    
    /* neon blue colour */
    .main-title {
        color: #00F2FE !important;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        text-shadow: 0 0 10px #00F2FE, 0 0 20px #4FACFE;
        margin-bottom: 20px;
    }
    
    /* input box white */
    .stTextArea label {
        color: #FFFFFF !important;
        font-weight: 600;
        font-size: 16px !important;
    }

    /* AI output white */
    .stMarkdown p, .stMarkdown li {
        color: #FFFFFF !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }
    
    /* sucess box */
    .stAlert p {
        color: #1E4620 !important;
        font-weight: 700 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3.website UI
st.markdown("<h1 class='main-title'>📚 AKGEC AI Notes Summarizer</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #A0AAB2;'>Get instant exam-ready bullet points from your senior AI teacher!</p>", unsafe_allow_html=True)
user_notes = st.text_area("📄 Paste your long college notes below:", height=180, placeholder="Type or paste your content here...")

# Button
if st.button("✨ Generate AI Summary", use_container_width=True):
    if user_notes.strip() != "":
        with st.spinner("AI Teacher is reading your notes... Please wait..."):
            summary_result = summarize_notes(user_notes)
            st.success("🎯 Your Exam-Ready Points:")
            st.write(summary_result)
            
            # PDF डाउनलोड बटन
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
