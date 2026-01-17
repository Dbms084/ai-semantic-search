"""One-time document indexing pipeline."""

from app.ingestion.google_drive_loader import list_google_docs, read_google_doc
from app.embeddings.embedder import chunk_text
from app.vectorstore.chroma_store import create_vector_store


def run_indexing():
    all_chunks = []

    docs = list_google_docs()
    print(f"Indexing {len(docs)} documents")

    for doc in docs:
        text = read_google_doc(doc["id"])
        chunks = chunk_text(text)
        all_chunks.extend(chunks)

    create_vector_store(all_chunks)
    print("✅ Documents indexed into ChromaDB")


if __name__ == "__main__":
    run_indexing()
