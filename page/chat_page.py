import streamlit as st
from model.model import AIModel
from streamlit_extras.bottom_container import bottom
from model.pdf_reader import formatText
import model.prompt as prt
import model.swot as swot


def getAvatar(role):
    if role == "user":
        return "😂"
    return "👩‍🎨"


def chat_page():
    chat_ai = AIModel()
    chatPage = st.container()

    with chatPage:

        st.title("Idea Kitchen")
        st.text("This kitchen is where you cook your idea.\nThe chatbot is a questionable one, often asks you questions, targetting your pain points.\nIt may be harsh but bear with it.")

        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "system",
                    "content": prt.question_bot_system_message},
                {"role": "assistant", "content": "Share your startup idea!"}]

        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        with bottom():

            # uploaded_files = st.file_uploader(
            #     'Upload relevant pdf', type='pdf', accept_multiple_files=True)

            query = st.chat_input("Chat with Question Bot")

        if prompt := query:
            internal_prompt = prompt
            # if uploaded_files is not None:
            #     df = extract_data(uploaded_files)
            if st.session_state.pdf_datas != []:
                internal_prompt += formatText(st.session_state.pdf_datas)

            concatenated_prompt = st.session_state.messages
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for chunck in chat_ai.loadChatCompletion([{"role": m["role"], "content": m["content"]}
                                                          for m in concatenated_prompt] + [{"role": "user", "content": internal_prompt}]):
                    full_response += chunck.choices[0].delta.content or ""
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)

            st.session_state.messages.append(
                {"role": "assistant", "content": full_response})
            if "SWOT" in full_response:
                parsed_swot_data = swot.extract_swot(full_response)
                st.subheader('SWOT Analysis Chart')
                swot_fig = swot.create_swot_chart(parsed_swot_data)
                st.pyplot(swot_fig)
