# app.py
import streamlit as st
from core_engine import get_memory_chain  # Import your chain

# Page config (title + layout)
st.set_page_config(page_title="AI Guru", layout="wide")

# Cache the LLM chain (load once, reuse forever)
@st.cache_resource
def load_chain():
    return get_memory_chain()

memory_chain = load_chain()

# App header
st.title("🧠 AI Guru — Local LLM Chat")

# Sidebar info
st.sidebar.header("⚙️ Settings")
st.sidebar.write("Configure your model and session here.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

# 🔥 Get REAL AI response from your chain
    with st.chat_message("assistant"):
        with st.spinner("AI Guru is thinking..."):
            response_stream = memory_chain.stream(
                {"input": prompt},
                config={"configurable": {"session_id": "user_session_123"}}
            )
            response = st.write_stream(response_stream)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
