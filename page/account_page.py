import streamlit as st
from streamlit_extras.bottom_container import bottom
from model.pdf_reader import extract_individual_data
from model.cloud_storage import upload_blob_from_memory, get_shared_from_firebase


def uploadFile(file, destination):
    data = extract_individual_data(file)
    upload_blob_from_memory(
        contents=data, destination_blob_name=destination)


def account_page():
    accountPage = st.container()
    with accountPage:
        st.title("Data Source")
        st.text(
            "This is where all the data used to generate precise response for your startup idea.")

        data = get_shared_from_firebase()
        st.subheader("Shared Data")
        col1, col2 = st.columns(2)
        for j in range(len(data)):
            if (j % 2 == 1):
                with col1:
                    container = st.container(height=200)
                    with container:
                        st.subheader(data[j]["name"])
                        st.markdown(
                            data[j]["content"])
            else:
                with col2:
                    container = st.container(height=200)
                    with container:
                        st.subheader(data[j]["name"])
                        st.markdown(
                            data[j]["content"])

        st.subheader("Personal Data")
        col3, col4 = st.columns(2)
        if "pdf_datas" in st.session_state:
            for i in range(len(st.session_state.pdf_datas)):
                if (i % 2 == 0):
                    with col3:
                        container = st.container(height=200)
                        with container:
                            st.subheader(st.session_state.pdf_datas[i]["name"])
                            st.markdown(
                                st.session_state.pdf_datas[i]["content"])
                else:
                    with col4:
                        container = st.container(height=200)
                        with container:
                            st.subheader(st.session_state.pdf_datas[i]["name"])
                            st.markdown(
                                st.session_state.pdf_datas[i]["content"])

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
