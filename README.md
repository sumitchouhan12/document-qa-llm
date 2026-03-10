# AI Document Question Answering System (RAG)

This project is a Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF document and ask questions about its content.

The system retrieves relevant sections from the document and generates answers using a Large Language Model.

---

## Features

- Upload any PDF document
- Ask natural language questions
- AI retrieves relevant document sections
- Context-aware answers generated using LLM
- Simple interactive UI with Streamlit

---

## Tech Stack

Python  
LangChain  
FAISS Vector Database  
HuggingFace Transformers  
Sentence Transformers Embeddings  
Streamlit  

---

## Project Architecture

PDF Upload  
↓  
Document Loader  
↓  
Text Chunking  
↓  
Embeddings Generation  
↓  
Vector Database (FAISS)  
↓  
Retriever  
↓  
LLM Response Generation

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/document-qa-llm.git
cd document-qa-llm