from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    for doc in documents:
        doc.metadata["page_number"] = doc.metadata.get("page", 0) + 1
        doc.metadata["source"] = pdf_path

    return documents