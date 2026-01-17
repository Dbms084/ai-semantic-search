"""ChromaDB vector store creation."""

from langchain_community.vectorstores import Chroma
from app.embeddings.embedder import get_embeddings


def create_vector_store(chunks):
    embeddings = get_embeddings()

    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    vectordb.persist()
    return vectordb
