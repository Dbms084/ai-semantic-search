"""RAG answer generation using Ollama."""

from langchain_ollama import OllamaLLM
from app.search.semantic_search import semantic_search


def generate_answer(query: str, k: int = 3):
    docs = semantic_search(query, k=k)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an assistant answering ONLY from the provided context.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""

    llm = OllamaLLM(model="phi3")
    response = llm.invoke(prompt)

    return response
