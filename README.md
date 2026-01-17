# 🔍 AI-Powered Semantic Search & Q&A over Google Docs (RAG System)

An end-to-end **Retrieval-Augmented Generation (RAG)** system that enables **semantic search and natural language question answering** over personal Google Docs.

Unlike traditional keyword search, this system understands the **meaning** of queries and generates **context-grounded answers** directly from user documents.

---

## 🚀 Features

- 🔗 **Google Drive Integration**  
  Securely ingests Google Docs using Google Drive & Docs APIs via service account authentication.

- 🧩 **Smart Text Chunking**  
  Documents are split into overlapping chunks to preserve semantic context.

- 🧠 **Semantic Search (Embeddings)**  
  Uses local Hugging Face embeddings (`all-MiniLM-L6-v2`) to capture meaning instead of keywords.

- 🗄️ **Vector Database (ChromaDB)**  
  Stores embeddings persistently for fast similarity-based retrieval.

- 🤖 **Retrieval-Augmented Generation (RAG)**  
  Retrieved document chunks are passed to a local LLM to generate grounded answers.

- 🛡️ **Hallucination Control**  
  The model answers **only from retrieved context** and replies *“I don’t know”* when information is missing.

- 💻 **Fully Local & Free**  
  Uses local embeddings and a local LLM (Phi-3 via Ollama). No OpenAI API required.

---

Google Docs
↓
Google Drive API (Ingestion)
↓
Text Cleaning & Chunking
↓
Local Embeddings (SentenceTransformers)
↓
ChromaDB (Vector Store)
↓
Semantic Retrieval
↓
Local LLM (Phi-3 via Ollama)
↓
Final Answer


---

## 🛠️ Tech Stack

| Component | Technology |
|---------|------------|
| Language | Python |
| Data Source | Google Drive API, Google Docs API |
| Embeddings | Hugging Face (`all-MiniLM-L6-v2`) |
| Vector Database | ChromaDB |
| LLM | Phi-3 (via Ollama) |
| Frameworks | LangChain (modular) |
| Authentication | Google Service Account |
| Environment | Virtualenv |

---

## 📂 Project Structure

ai-semantic-search/
├── app/
│ ├── main.py # RAG-powered Q&A interface
│ ├── index_documents.py # One-time document indexing
│ │
│ ├── ingestion/ # Google Drive ingestion
│ ├── embeddings/ # Chunking & embeddings
│ ├── vectorstore/ # ChromaDB logic
│ ├── search/ # Semantic retrieval
│ └── rag/ # Answer generation
│
├── chroma_db/ # Persistent vector database (gitignored)
├── service_account.json # Google credentials (gitignored)
├── requirements.txt
├── .env # Environment variables (gitignored)
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Dbms084/ai-semantic-search.git
cd ai-semantic-search

2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Google Drive API Setup

Create a Google Cloud project

Enable Google Drive API and Google Docs API

Create a Service Account

Download service_account.json

Share your Google Docs (or folder) with the service account email (Viewer access)

5️⃣ Index Documents (Run Once)
python -m app.index_documents
This step:

Fetches Google Docs

Chunks text

Generates embeddings

Stores them in ChromaDB

6️⃣ Run the Search & Q&A System
python -m app.main

Ask questions like:
What does Bengali culture emphasize?

🧪 Design Decisions

Local embeddings instead of OpenAI → avoids API limits and cost

Separation of indexing and querying → mirrors production RAG systems

ChromaDB → lightweight, persistent, fast vector search

Local LLM (Phi-3) → optimized for low-memory systems

🔮 Future Improvements

📌 Source citations in answers

🖥️ Streamlit / Web UI

🔄 Auto re-indexing when documents change

🧠 Hybrid search (keyword + semantic)

📄 Support for PDFs and local files

👩‍💻 Author

Debosmita Majumdar
Computer Science Undergraduate | AI / ML Enthusiast

## 🧠 System Architecture

