```markdown
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
   git clone https://github.com/anasansari966/itc-financial-chatbot.git
   cd itc-financial-chatbot
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**:
   ```bash
   echo "GROQ_API_KEY=gsk_*****" > .env
   ```

## Workflow Pipeline 🔄

1. **Data Acquisition**:
   ```bash
   python pdf_scrape.py
   ```

2. **Document Processing**:
   ```bash
   python vectorize_documents.py
   ```

3. **Launch Chat Interface**:
   ```bash
   streamlit run app.py
   ```

## Usage Examples 💬

**Sample Queries**:
- "What was ITC's revenue growth in FY 2023?"
- "Compare ESG initiatives between 2022 and 2023"
- "Show me the dividend policy from last year's report"
- "Explain the key risk factors mentioned in latest filing"

**Response Features**:
- Financial figures with proper units (crore/lakhs/percent)
- Tabular data interpretation
- Multi-document synthesis
- Context-aware analysis

## Project Structure 🗂️

```
itc-financial-chatbot/
├── itc_pdfs/              # Downloaded financial documents
├── vector_store/          # ChromaDB vector embeddings
├── pdf_scrape.py          # PDF scraping automation
├── vectorize_documents.py # Document processing pipeline
├── main.py               # Core LLM interaction logic
├── app.py                # Streamlit web interface
├── requirements.txt      # Dependency management
└── .env                  # API key configuration
```

## Environment Variables 🔒

Create `.env` file with:
```ini
GROQ_API_KEY=your_groq_api_key_here
```

## Acknowledgments 🏆

- Groq for ultra-fast LLM inference
- LangChain for RAG architecture
- Hugging Face for transformer models
- Streamlit for rapid UI development

```

This README provides:
1. Clear technology differentiation
2. Business-friendly feature highlights
3. Precise technical documentation
4. End-to-end workflow visibility
5. Enterprise-grade security notice
6. Professional formatting with emoji visualization
7. Comprehensive setup/usage guidance
