import streamlit as st

from modules.search import search_web
from modules.scrape import scrape_url
from modules.llm import summarize_article
from modules.slides import generate_slide_outline
from modules.pptx import create_pptx


def generate_presentation(topic: str, output_file: str = None):
    if output_file is None:
        output_file = topic.replace(" ", "_") + ".pptx"

    results = search_web(topic, num_results=5)
    summaries = []
    for r in results:
        text = scrape_url(r["url"])
        if not text:
            print("Could not extract text from:", r["url"])
            continue
        summary = summarize_article(text, r["title"], topic)
        summaries.append(summary)
    slides = generate_slide_outline(summaries)
    create_pptx(slides, output_file)
    return output_file

# Streamlit UI
# Page config
st.set_page_config(
    page_title="Slide Deck Generator",
    layout="centered"
)

# Custom CSS for aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 12px;
    }
    h1 {
        text-align: center;
        color: #2c3e50;
    }
    .stButton>button {
        width: 120%;
        background-color: #2c3e50;
        color: white;
        border-radius: 8px;
        padding: 0.75rem;
        font-size: 1rem;
        
    }
    .stButton>button:hover {
        background-color: #34495e;
        color: #f1f1f1;
    }
    .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title & description
st.title("Slide Deck Generator")
st.markdown(
    """
    Turn any topic into a polished **PowerPoint presentation** in seconds!  
    Just type a topic and let AI do the work.
    """
)

# Input
col1, col2, col3 = st.columns([1, 3, 1])  
with col2:
    topic = st.text_input("Enter a topic:", placeholder="e.g., Artificial Intelligence")

# Action button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Generate Presentation"):
        if not topic.strip():
            st.warning("Please enter a valid topic.")
        else:
            with st.spinner("Creating your slides... Please wait ⏳"):
                output_file = generate_presentation(topic)

            st.success("Presentation generated successfully!")

            with open(output_file, "rb") as file:
                st.download_button(
                    label="Download Presentation",
                    data=file,
                    file_name=output_file,
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )
