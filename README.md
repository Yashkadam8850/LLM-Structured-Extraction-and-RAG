# 🤖 LLM Structured Extraction & Retrieval-Augmented Generation (RAG)

An end-to-end AI project demonstrating **LLM-powered Structured Information Extraction** and **Retrieval-Augmented Generation (RAG)** using **Mistral AI**, **Pydantic**, **Sentence Transformers**, **FAISS**, and **Streamlit**.

---

## 🚀 Live Demo
🌐 **Streamlit Application:**  
**http://llm-structured-extraction-and-rag-yzembazvu5ykmrr3rfesyk.streamlit.app/**
**![alt text]image-1.png**
**![alt text]image.png**

📂 **GitHub Repository:**  
**https://github.com/Yashkadam8850/LLM-Structured-Extraction-and-RAG**

---

# 📖 Project Overview

This project consists of two complete AI pipelines:

## 🔹 Part 1 — LLM-Powered Structured Information Extraction

Customer reviews are processed using a Large Language Model (LLM) to extract structured information. Every LLM response is validated using a **Pydantic schema** before being stored.

Extracted fields include:

- Category
- Urgency
- Sentiment
- Summary

The project also demonstrates schema validation by intentionally passing a malformed response through the validation pipeline.

---

## 🔹 Part 2 — Retrieval-Augmented Generation (RAG)

A small knowledge base is created from multiple text documents.

The pipeline:

- Loads documents
- Splits documents into chunks
- Generates embeddings
- Stores embeddings in FAISS
- Retrieves relevant chunks
- Uses Mistral AI to generate grounded answers

The assistant answers questions using **only the retrieved context**, reducing hallucinations.

---

# 🎯 Features

### ✅ Structured Extraction

- LLM-powered structured extraction
- Prompt Engineering
- Pydantic schema validation
- JSON output
- Enum validation
- Validation error handling
- Malformed fixture testing

---

### ✅ Retrieval-Augmented Generation (RAG)

- Document loading
- Text chunking
- Embedding generation
- Semantic search
- FAISS vector database
- Context retrieval
- Grounded answer generation

---

### ✅ Streamlit Web Application

- Interactive dashboard
- AI-powered document assistant
- Structured extraction demo
- Retrieved chunk visualization
- Professional UI

---

# 🏗 Project Architecture

```text
                 Customer Reviews
                        │
                        ▼
              Mistral Large Language Model
                        │
                        ▼
              Structured JSON Extraction
                        │
                        ▼
              Pydantic Schema Validation
                        │
                        ▼
            structured_output.json


                 Text Documents
                        │
                        ▼
                Document Chunking
                        │
                        ▼
          Sentence Transformer Embeddings
                        │
                        ▼
                 FAISS Vector Store
                        │
                        ▼
                Similarity Retrieval
                        │
                        ▼
                 Mistral AI Response
```

---

# 📂 Project Structure

```text
LLM-Structured-Extraction-and-RAG/
│
├── data/
│   ├── reviews.json
│   └── documents/
│       ├── doc1.txt
│       ├── doc2.txt
│       ├── doc3.txt
│       ├── doc4.txt
│       └── doc5.txt
│
├── output/
│   └── extracted_reviews.json
│
├── results/
│   ├── structured_output.json
│   ├── validation_log.txt
│   └── rag_demo.txt
│
├── src/
│   ├── __init__.py
│   ├── schema.py
│   ├── extraction.py
│   ├── validation.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   └── rag_pipeline.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Mistral AI | Large Language Model |
| Pydantic | Schema Validation |
| Sentence Transformers | Embedding Generation |
| all-MiniLM-L6-v2 | Embedding Model |
| FAISS | Vector Database |
| Streamlit | Web Application |
| LangChain Text Splitters | Document Chunking |
| Pandas | Data Processing |
| NumPy | Numerical Computing |

---

# 🤖 AI Models & Tools

## Large Language Model

**Model:** `mistral-small-latest`

**Reason**

- Fast inference
- Reliable structured outputs
- High-quality reasoning
- Simple API integration

---

## Embedding Model

**Model**

`all-MiniLM-L6-v2`

**Reason**

- Lightweight
- Fast embedding generation
- Excellent semantic similarity performance
- Runs locally without additional API cost

---

## Vector Store

**FAISS**

**Reason**

- High-speed similarity search
- Lightweight
- Industry-standard vector indexing library

---

# 📊 Structured Extraction Pipeline

The extraction pipeline performs the following steps:

1. Load customer reviews
2. Send reviews to Mistral AI
3. Generate structured JSON
4. Validate JSON using Pydantic
5. Save validated records
6. Log validation failures

---

## Example Structured Output

```json
{
  "category": "Delivery",
  "urgency": "High",
  "sentiment": "Negative",
  "summary": "Customer reports delayed delivery."
}
```

---

# ✅ Schema Validation

A Pydantic schema validates:

- Required fields
- Data types
- Enum values
- Missing values
- Invalid responses

---

# ⚠ Validation Failure Demonstration

The project intentionally includes a malformed response to demonstrate schema validation.

### Malformed Fixture

```json
{
  "category": "delivery",
  "urgency": "urgent",
  "sentiment": "Bad",
  "summary": "Package delayed."
}
```

### Validation Result

- Invalid enum values detected
- ValidationError raised
- Logged into `validation_log.txt`
- Record rejected

---

# 📚 Retrieval-Augmented Generation (RAG)

Pipeline:

```
Documents

↓

Chunking

↓

Embeddings

↓

FAISS

↓

Similarity Search

↓

Retrieved Context

↓

Mistral AI

↓

Grounded Answer
```

---

# 💬 Example Questions

- What is Artificial Intelligence?
- Explain Machine Learning.
- What is Deep Learning?
- What is Generative AI?
- What is Prompt Engineering?

---

# 📁 Output Files

The project generates:

### Structured Extraction

- `structured_output.json`
- `validation_log.txt`

### RAG

- `rag_demo.txt`

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Yashkadam8850/LLM-Structured-Extraction-and-RAG.git
```

Move into the project folder:

```bash
cd LLM-Structured-Extraction-and-RAG
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=YOUR_MISTRAL_API_KEY
```

**Important:** Never commit your API keys to GitHub.

---

# ▶ Run the Project

## Run the Structured Extraction & RAG Demo

```bash
python main.py
```

---

## Run the Streamlit Web Application

```bash
streamlit run app.py
```

---

# 📸 Application Preview

The Streamlit application provides:

- 📄 Structured Extraction Dashboard
- 📊 Validation Statistics
- 📋 Extracted Records Table
- 💬 AI Document Assistant
- 📚 Retrieved Document Chunks
- 🤖 Grounded AI Responses

---

# 📈 Future Improvements

- ChromaDB integration
- Hybrid Search (BM25 + Dense Retrieval)
- Multi-document upload
- PDF document support
- Conversation memory
- User authentication
- Docker deployment
- Cloud vector database support

---

# 👨‍💻 Author

# **Yash Kadam**

### Connect with me

- GitHub: https://github.com/Yashkadam8850
- LinkedIn: https://www.linkedin.com/in/yash-kadam-16a827363

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the repository
- 💡 Share your feedback
- 🤝 Contribute to improvements

---

## 📜 License

This project is developed for educational purposes as part of an AI/ML Capstone Project.
