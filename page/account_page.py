import streamlit as st
from streamlit_extras.bottom_container import bottom
from model.pdf_reader import extract_individual_data
from model.cloud_storage import upload_blob_from_memory


def uploadFile(file, destination):
    data = extract_individual_data(file)
    upload_blob_from_memory(
        contents=data, destination_blob_name=destination)


def account_page():
    accountPage = st.container()
    with accountPage:
        st.title("Account Page")
        col1, col2, col3 = st.columns(3)
        for i in range(len(st.session_state.pdf_datas)):
            if (i % 3 == 0):
                with col3:
                    container = st.container(height=200)
                    with container:
                        st.subheader(st.session_state.pdf_datas[i]["name"])
                        st.markdown(st.session_state.pdf_datas[i]["content"])
            elif (i % 2 == 0):
                with col2:
                    container = st.container(height=200)
                    with container:
                        st.subheader(st.session_state.pdf_datas[i]["name"])
                        st.markdown(st.session_state.pdf_datas[i]["content"])
            elif (i % 2 == 1):
                with col1:
                    container = st.container(height=200)
                    with container:
                        st.subheader(st.session_state.pdf_datas[i]["name"])
                        st.markdown(st.session_state.pdf_datas[i]["content"])

        with bottom():
            left_col, right_col = st.columns((8, 2))
            with left_col:
                file = st.file_uploader(
                    "Upload your files here", type="pdf")

            with right_col:
                # Add space to move the button down a bit

                st.subheader("")
                button = st.button("Upload", use_container_width=True)
                if file and button:
                    uploadFile(file, file.name)
                    st.success("Uploaded Successfully")
