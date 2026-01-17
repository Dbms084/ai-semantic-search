"""Semantic search over ChromaDB."""

from langchain_community.vectorstores import Chroma
from app.embeddings.embedder import get_embeddings


def load_vector_store():
    embeddings = get_embeddings()
    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    return vectordb


def semantic_search(query: str, k: int = 3):
    vectordb = load_vector_store()
    results = vectordb.similarity_search(query, k=k)
    return results
