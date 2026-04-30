# app.py
import streamlit as st

# Page config (title + layout)
st.set_page_config(page_title="AI Guru", layout="wide")

# App header
st.title("🧠 AI Guru — Local LLM Chat")

# Sidebar info
st.sidebar.header("⚙️ Settings")
st.sidebar.write("Configure your model and session here.")

# Chat input + output area
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

    # Placeholder for AI response (later we’ll connect ChatOllama here)
    response = f"🤖 (AI Guru would reply to: {prompt})"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
