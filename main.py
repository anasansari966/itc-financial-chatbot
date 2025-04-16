import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()

DB_PATH = "vector_store"

def load_vector_db():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    return vectordb

prompt_template = """
You are a highly intelligent assistant trained to answer questions based strictly on ITC Limited's official financial documents and company data.

Your goal is to provide precise, factual, and well-formatted answers. Ensure that:
- You use only the information present in the provided context.
- All financial figures include units like crore, lakhs, or percentage where applicable.
- If the answer is not clearly present in the context, respond with: "I don't know."
- Do not speculate or hallucinate any information.

Always prioritize clarity and accuracy.

---------------------
{context}
---------------------

Question: {question}

Answer:
"""

def get_prompt():
    return PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

def load_groq_llm():
    return ChatGroq(
        model="llama3-8b-8192",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2
    )

def build_chain():
    vectorstore = load_vector_db()
    llm = load_groq_llm()
    prompt = get_prompt()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
    return qa_chain

def query_bot(question: str):
    chain = build_chain()
    result = chain({"query": question})
    return result["result"], result.get("source_documents", [])

if __name__ == "__main__":
    print("Welcome to ITC Financial Report Chatbot!")
    print("Type 'exit' or press Enter to quit.\n")

    chain = build_chain()

    while True:
        question = input("\n Ask a question about ITC's financials: ").strip()

        if not question or question.lower() == 'exit':
            print("\nGoodbye!")
            break

        try:
            result = chain({"query": question})
            answer = result["result"]
            sources = result.get("source_documents", [])

            print("\n Answer:\n", answer)

            if sources:
                print("\n Sources:")
                for doc in sources:
                    print(f"- {doc.metadata['source']} (Page {doc.metadata.get('page', '?')})")

        except Exception as e:
            print(f"\n Error processing request: {str(e)}")