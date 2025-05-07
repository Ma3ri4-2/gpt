import openai
import streamlit as st

st.set_page_config(page_title="Fruitify Assistant")
st.title("🍎 Fruitify AI Assistant")

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Your prompt-engineered system message
system_prompt = """
You are a helpful assistant who knows everything about Fruitify — a smart fruit quality control system.
Fruitify uses a YOLO-based model running on a Jetson Orin Nano device to detect and sort fruits in real-time.
Its goal is to make fruit sorting easier, faster, and more accurate for farms and factories.

Explain technical concepts clearly if you are asked to do so. If someone asks what Fruitify does, how it works, what its SDG goals are, give informative and supportive answers but make them short and sweet.
If they ask general questions not related to Fruitify, don't answer — highlight that you are not made for other reasons than this.

Always be professional, friendly, and enthusiastic about Fruitify and its mission, keeping your answers short and sweet!
"""

# Default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Inject system prompt only once at the beginning
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({"role": "system", "content": system_prompt})

# Display previous messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask me about Fruitify 🍓")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=st.session_state.messages,
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
        except Exception as e:
            message_placeholder.markdown("⚠️ Error from OpenAI API.")
            st.error(f"{e}")
            full_response = "Sorry, something went wrong."

        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
