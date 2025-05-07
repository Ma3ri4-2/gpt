from langchain_ollama import OllamaLLM
import streamlit as st

st.title("Fruitify Chat Assistant 🍎")

# Initialize the Ollama model (make sure 'llama3.2' is correctly installed in Ollama)
model = OllamaLLM(model="llama3.2")

# Define the system prompt with Fruitify's background
system_prompt = """
You are a helpful assistant who knows everything about Fruitify — a smart fruit quality control system.
Fruitify uses a YOLO-based model running on a Jetson Orin Nano device to detect and sort fruits in real-time.
Its goal is to make fruit sorting easier, faster, and more accurate for farms and factories.

Explain technical concepts clearly if you are asked to do so. If someone asks what Fruitify does, how it works, what its SDG goals are , give informative and supportive answers but make them short and sweet.
If they ask general questions not related to fruitify don't answer highlight that you are not made for other reasons than this.

Always be professional, friendly, and enthusiastic about Fruitify and its mission keeping your answers short and sweet!
"""

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User prompt input
prompt = st.chat_input("Ask me anything about Fruitify!")

# If there's a new prompt
if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Combine system prompt with message history
    conversation = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages])
    full_prompt = f"{system_prompt.strip()}\n\n{conversation}"

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = model.invoke(full_prompt)
        message_placeholder.markdown(response)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
