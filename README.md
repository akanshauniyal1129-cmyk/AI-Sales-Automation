# 🤖 AI Sales Automation Agent

An AI-powered sales automation system that helps businesses automate customer interaction, product information retrieval, and personalized responses using Large Language Models (LLMs), LangChain, and Retrieval-Augmented Generation (RAG).

## 📌 Project Overview

Traditional sales teams spend a lot of time answering repetitive customer queries, searching product information, and preparing responses.

This project builds an AI Sales Assistant that can understand customer queries, retrieve relevant information from a knowledge base, and generate intelligent responses automatically.

The system uses **RAG (Retrieval-Augmented Generation)** architecture to provide accurate and context-aware answers.

---

## 🚀 Features

* 🤖 AI-powered customer query handling
* 🔍 Retrieval-Augmented Generation (RAG) pipeline
* 📚 Knowledge base document processing
* 🧠 Semantic search using embeddings
* 💬 Context-aware responses using LLMs
* 📧 Automated sales communication workflow
* 🌐 Interactive Streamlit user interface

---

## 🏗️ System Architecture

```
User Query
     |
     ↓
Document Loader
     |
     ↓
Text Splitter
     |
     ↓
Embedding Generation
     |
     ↓
Vector Database
     |
     ↓
Retriever
     |
     ↓
LLM Response Generation
     |
     ↓
AI Sales Assistant
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### AI / ML

* LangChain
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Embeddings
* Vector Search

### Backend & Deployment

* Streamlit
* Python APIs

### Libraries

* LangChain
* FAISS / Vector Database
* Transformers
* Sentence Transformers

---

## 📂 Project Structure

```
AI-Sales-Automation/
│
├── agents/
│   └── email_agent.py
│
├── loader.py
├── splitter.py
├── vectorstore.py
├── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/akanshauniyal1129-cmyk/AI-Sales-Automation.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 💡 Use Cases

* Automated customer support
* Sales assistant chatbot
* Product recommendation assistant
* Lead qualification
* Business knowledge assistant

---

## 🎯 Key Learning Outcomes

* Built a complete RAG-based AI application
* Implemented document retrieval pipeline
* Worked with embeddings and vector databases
* Integrated LLMs into real-world business workflow
* Designed an AI agent-based automation system

---

## 👩‍💻 Author

**Akansha Uniyal**
