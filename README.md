# 📄 Legal RAG Knowledge Analyst

An AI-powered Retrieval-Augmented Generation (RAG) system that analyzes legal and technical documents using ChromaDB and Groq LLM.

The application allows users to upload PDF documents, extract information, retrieve relevant content, and generate context-aware answers with citations.

---

# 🚀 Features

- Upload PDF documents
- Extract text from PDFs
- Split documents into chunks
- Store embeddings in ChromaDB
- Retrieve relevant document chunks
- Generate responses using Groq LLM
- Citation-based answers
- Generate Summary Dashboard

Dashboard includes:

- Document Summary
- Risks
- Important Dates
- Stakeholders
- Key Clauses
- Missing Information

---

# 🛠 Tech Stack

| Technology | Usage |
|------------|--------|
| Python | Backend |
| Streamlit | Frontend |
| LangChain | RAG Pipeline |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Text Embeddings |
| Groq API | LLM |
| PyPDF | PDF Extraction |

---

# 📂 Project Structure

```text
legal_rag_analyst/

│
├── backend/
│   ├── __init__.py
│   ├── config.py
│   ├── step_1_pdf_loader.py
│   ├── step_2_text_splitter.py
│   ├── step_3_chromadb.py
│   ├── step_4_rag_chain.py
│   └── step_5_summary_dashboard.py
│
├── frontend/
│   └── app.py
│
├── data/
│
├── chroma_db/
│
├── .env
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone <repository_link>

cd legal_rag_analyst
```

---

## Step 2: Create Virtual Environment

Python 3.11:

```bash
py -3.11 -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt --prefer-binary
```

---

# 🔑 Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

Get Groq API key:

https://console.groq.com/

---

# ▶️ Run Project

```bash
streamlit run frontend/app.py
```

Application runs at:

```text
http://localhost:8501
```

---

# 🔄 Workflow

## Step 1: PDF Loading

File:

```text
step_1_pdf_loader.py
```

Responsibilities:

- Read uploaded PDFs
- Extract text
- Store page metadata

---

## Step 2: Text Chunking

File:

```text
step_2_text_splitter.py
```

Responsibilities:

- Split long documents
- Create overlapping chunks

Configuration:

```python
chunk_size=1000
chunk_overlap=200
```

---

## Step 3: ChromaDB Vector Store

File:

```text
step_3_chromadb.py
```

Responsibilities:

- Create embeddings
- Store vectors
- Create retrieval system

Embedding model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

---

## Step 4: RAG Pipeline

File:

```text
step_4_rag_chain.py
```

Responsibilities:

- Retrieve relevant chunks
- Send context to LLM
- Generate answers

---

## Step 5: Summary Dashboard

File:

```text
step_5_summary_dashboard.py
```

Responsibilities:

Generate:

- Risks
- Dates
- Stakeholders
- Clauses
- Missing Information

---

# 🧠 Example Questions

### General Questions

- What is this agreement about?
- Summarize the document
- What is the project duration?

### Stakeholder Questions

- List all stakeholders
- Who is the project manager?
- Who is the legal representative?

### Payment Questions

- Explain payment terms
- What happens if payment is delayed?

### Risk Questions

- What risks are mentioned?
- Explain security risks

### Legal Questions

- What are the termination conditions?
- What dispute resolution process exists?
- Which jurisdiction applies?

### Complex Questions

- Summarize risks and stakeholders
- Compare payment and termination clauses
- Explain major clauses with citations

---

# 🐞 Common Errors

## Error:

```python
PermissionError:
chroma.sqlite3 being used by another process
```

Reason:

ChromaDB file is locked.

Solution:

Stop Streamlit:

```bash
Ctrl + C
```

Delete:

```text
chroma_db/
```

Run again:

```bash
streamlit run frontend/app.py
```

Alternative fix:

Remove:

```python
shutil.rmtree(CHROMA_PATH)
```

from:

```python
step_3_chromadb.py

```
---

# 🌐 Live Demo

Try the deployed application here:

[Legal RAG Knowledge Analyst Live Demo](https://your-streamlit-link.streamlit.app)

Example:

```text
https://legal-rag-analyst.streamlit.app
```

---

# 📸 Application Preview

Upload legal PDF documents and ask questions such as:

- What risks are mentioned?
- Who are the stakeholders?
- Explain payment terms
- Summarize the agreement

The application retrieves relevant document chunks and generates contextual answers with citations.

---

# 🔮 Future Improvements

- Multiple PDF uploads
- Chat history memory
- Agentic RAG workflow
- Hybrid retrieval
- PostgreSQL + PGVector
- Authentication system
- Cloud deployment

---

# 👩‍💻 Author

Akhila Boddula

AI Engineer | Generative AI | RAG Systems | Agentic AI

GitHub:

https://github.com/akhilaboddula16

LinkedIn:

https://linkedin.com/in/akhila-boddula