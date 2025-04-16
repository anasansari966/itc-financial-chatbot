import streamlit as st
import re
from main import query_bot  # Import your existing functions


def extract_points(text):
    """Extracts numbered points from bot response"""
    points = re.findall(r'\d+\.\s*(.*?)(?=\n\d+\.|\n\n|$)', text, flags=re.DOTALL)
    return [point.strip() for point in points]


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'last_points' not in st.session_state:
    st.session_state.last_points = []

st.title("📈 ITC Financial Report Chatbot")
for entry in st.session_state.chat_history:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])
        if entry["role"] == "assistant" and entry.get("sources"):
            st.caption("Sources:")
            for source in entry["sources"]:
                st.caption(f"- {source}")

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    if user_input.strip().lower() == 'explain all':
        if not st.session_state.last_points:
            response = "No previous points to explain. Please ask a question first."
            sources = []
        else:
            query = "Explain in detail these points from the report:\n" + "\n".join(
                f"{i + 1}. {point}" for i, point in enumerate(st.session_state.last_points)
            )
            response, sources = query_bot(query)
    else:
        response, sources = query_bot(user_input)
        st.session_state.last_points = extract_points(response)

    source_list = [f"{doc.metadata['source']} (Page {doc.metadata.get('page', '?')})"
                   for doc in sources]

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response,
        "sources": source_list
    })

    st.rerun()