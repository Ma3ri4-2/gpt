import openai
import streamlit as st

# App title
st.title("ChatGPT-like Clone 🤖")

# Load OpenAI API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Optional: Let user pick the model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

model = st.selectbox("Choose a model:", ["gpt-3.5-turbo", "gpt-4"], index=0)
st.session_state["openai_model"] = model

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("What is up?")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show assistant response with streaming
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")  # typing indicator

        except Exception as e:
            message_placeholder.markdown("⚠️ Error from OpenAI API.")
            st.error(f"{e}")
            full_response = "Sorry, something went wrong."

        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
