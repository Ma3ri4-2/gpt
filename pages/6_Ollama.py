from langchain_ollama import OllamaLLM
import streamlit as st

st.title("Ollama-like Clone")

# Initialize the Ollama model (make sure 'llama3.2' is correctly installed in Ollama)
model = OllamaLLM(model="llama3.2")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User prompt input
prompt = st.chat_input("What is up?")

# If there's a new prompt
if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Create a combined prompt for Ollama (as it doesn't use role-based chat yet)
    full_prompt = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages])

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = model.invoke(full_prompt)
        message_placeholder.markdown(response)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
