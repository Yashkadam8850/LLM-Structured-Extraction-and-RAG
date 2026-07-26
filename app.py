import streamlit as st

from src.validation import validate_all
from src.rag_pipeline import ask_question

st.set_page_config(
    page_title="LLM Structured Extraction & RAG",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 LLM Structured Extraction & RAG")

tab1, tab2 = st.tabs([
    "Structured Extraction",
    "RAG Chat"
])

# ==========================
# Structured Extraction
# ==========================

with tab1:

    st.header("Structured Information Extraction")

    if st.button("Run Extraction"):

        valid_records, errors = validate_all()

        st.success(f"Valid Records : {len(valid_records)}")

        st.error(f"Validation Errors : {len(errors)}")

        st.json(valid_records)

# ==========================
# RAG
# ==========================

with tab2:

    st.header("Ask Questions")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Generate Answer"):

        if question:

            retrieved, answer = ask_question(question)

            st.subheader("Retrieved Chunks")

            for i, chunk in enumerate(retrieved):

                with st.expander(f"Chunk {i+1}"):

                    st.write(chunk)

            st.subheader("Answer")

            st.success(answer)