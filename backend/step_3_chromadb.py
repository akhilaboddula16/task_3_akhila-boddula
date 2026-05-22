import os
import shutil

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from backend.config import EMBEDDING_MODEL, CHROMA_PATH, COLLECTION_NAME


def get_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
    return embeddings


def create_chroma_db(chunks, reset=True):
    embeddings = get_embeddings()

    if reset and os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME
    )

    return vectorstore


def load_chroma_db():
    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )

    return vectorstore