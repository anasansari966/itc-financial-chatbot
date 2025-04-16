import os
import pdfplumber
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = "itc_pdfs"
DB_PATH = "vector_store"

def extract_text_and_tables(pdf_path):
    all_chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            content_parts = []

            text = page.extract_text()
            if text:
                content_parts.append(f"Text:\n{text.strip()}")

            tables = page.extract_tables()
            for table_index, table in enumerate(tables):
                table_text = "\n".join([" | ".join(str(cell) for cell in row) for row in table])
                content_parts.append(f"Table {table_index + 1}:\n{table_text.strip()}")

            if content_parts:
                page_content = "\n\n".join(content_parts)
                all_chunks.append(Document(
                    page_content=page_content,
                    metadata={"source": os.path.basename(pdf_path), "page": page_num + 1}
                ))

    return all_chunks

def load_all_pdfs(data_dir):
    all_docs = []
    for filename in os.listdir(data_dir):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(data_dir, filename)
            print(f" Processing {filename}...")
            all_docs.extend(extract_text_and_tables(path))
    return all_docs

def vectorize_documents(documents):
    from langchain_community.vectorstores import Chroma
    from langchain_huggingface import HuggingFaceEmbeddings

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = Chroma(
        embedding_function=embeddings,
        persist_directory=DB_PATH
    )

    batch_size = 150
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        vector_db.add_documents(batch)
        print(f" Added batch {i // batch_size + 1}")

    vector_db.persist()
    print(f" Stored {len(chunks)} chunks in vector DB at '{DB_PATH}'")


if __name__ == "__main__":
    docs = load_all_pdfs(DATA_PATH)
    if docs:
        vectorize_documents(docs)
    else:
        print(" No documents found.")