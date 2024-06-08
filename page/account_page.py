import streamlit as st
from streamlit_extras.bottom_container import bottom
from model.pdf_reader import extract_individual_data
from model.cloud_storage import upload_blob_from_memory


def uploadFile(file):
    data = extract_individual_data(file)
    upload_blob_from_memory(
        contents=data, destination_blob_name="PDFs")


def account_page():
    accountPage = st.container()
    with accountPage:
        st.title("Account Page")
        # col1, col2, col3 = st.columns(3)
        with bottom():
            left_col, right_col = st.columns((7, 3))
            with left_col:
                file = st.file_uploader(
                    "Upload your files here", type="pdf")

            with right_col:
                if file and st.button("Upload"):
                    uploadFile(file)
