import os
import sys
import streamlit as st

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from backend.step_1_pdf_loader import load_pdf
from backend.step_2_text_splitter import split_documents
from backend.step_3_chromadb import create_chroma_db, load_chroma_db
from backend.step_4_rag_chain import build_rag_chain
from backend.step_5_summary_dashboard import generate_summary_dashboard


st.set_page_config(
    page_title="Legal RAG Knowledge Analyst",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Legal RAG Knowledge Analyst")
st.write("ChromaDB + Groq API based RAG app for legal document analysis.")

uploaded_file = st.file_uploader(
    "Upload Legal or Technical PDF",
    type=["pdf"]
)

if uploaded_file:
    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join("data", uploaded_file.name)

    with open(pdf_path, "wb") as file:
        file.write(uploaded_file.read())

    st.success("PDF uploaded successfully.")

    if st.button("Process Document"):
        with st.spinner("Step 1: Loading PDF..."):
            documents = load_pdf(pdf_path)

        with st.spinner("Step 2: Splitting text into chunks..."):
            chunks = split_documents(documents)

        with st.spinner("Step 3: Storing embeddings in ChromaDB..."):
            create_chroma_db(chunks)

        st.success("Document processed successfully.")

        with st.spinner("Generating Summary Dashboard..."):
            dashboard = generate_summary_dashboard(documents)

        st.subheader("📊 Summary Dashboard")
        st.markdown(dashboard)

st.divider()

st.subheader("Ask Questions from the Document")

question = st.text_input(
    "Example: What are the risks mentioned in this contract?"
)

if st.button("Get Answer"):
    if not question:
        st.warning("Please enter a question.")
    else:
        try:
            vectorstore = load_chroma_db()
            rag_chain = build_rag_chain(vectorstore)

            with st.spinner("Retrieving relevant content and generating answer..."):
                answer, docs = rag_chain(question)

            st.subheader("Answer")
            st.markdown(answer)

            st.subheader("Retrieved Evidence")
            for doc in docs:
                page = doc.metadata.get("page_number", "Unknown")
                st.markdown(f"**Page {page}**")
                st.write(doc.page_content[:700])

        except Exception as e:
            st.error(f"Error: {e}")