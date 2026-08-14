import streamlit as st

from utils import call_llama


st.title(":zap: Llama Chatbot")
st.caption("A Streamlit chatbot powered by :llama: Llama")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "How can I help you?"
        }
    ]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input():

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    st.chat_message("user").write(prompt)

    with st.spinner("Generating response..."):

        response = call_llama(
            "llama3.1:8b",
            st.session_state.messages
        )

        msg = response["message"]["content"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": msg
        }
    )

    st.chat_message("assistant").write(msg)