# ITC Financial Report Analysis Chatbot 🤖📈

A Retrieval-Augmented Generation (RAG) powered chatbot specialized in analyzing ITC Limited's financial reports and SEC filings. Built with cutting-edge AI technologies for accurate financial insights.

## Features ✨

- **PDF Scraping Automation**: Automated download of latest financial reports
- **Multi-Modal Extraction**: Handles both text and tabular data from PDFs
- **Vector Intelligence**: ChromaDB vector storage with Hugging Face embeddings
- **AI-Powered Insights**: Groq's Llama3-8B model for high-speed responses
- **Audit Trail**: Source citation with document references and page numbers
- **Enterprise-Ready**: Robust error handling and batch processing capabilities

## Tech Stack 🛠️

- **LangChain**: RAG pipeline orchestration
- **Groq Inference**: LLM processing acceleration
- **Hugging Face**: Sentence Transformers for embeddings
- **ChromaDB**: Vector similarity search
- **Streamlit**: Web interface deployment
- **PDF Plumber**: Advanced PDF text extraction

## Installation 💻

1. **Prerequisites**:
   - Python 3.9+
   - Groq API Key (Add to `.env` file)

2. **Clone repository**:
   ```bash
   git clone https://github.com/<your-username>/itc-financial-chatbot.git
   cd itc-financial-chatbot
