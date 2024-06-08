import streamlit as st
from model.model import AIModel
from streamlit_extras.bottom_container import bottom


def chat_page():
    chat_ai = AIModel()
    chatPage = st.container()

    with chatPage:

        st.title("Chat Page")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        with bottom():
            query = st.chat_input("Chat with Question Bot")

        if prompt := query:
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for chunck in chat_ai.loadChatCompletion([{"role": m["role"], "content": m["content"]}
                                                          for m in st.session_state.messages]):
                    full_response += chunck.choices[0].delta.content or ""
                    message_placeholder.markdown(full_response + " ")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response})
