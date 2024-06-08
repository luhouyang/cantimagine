import streamlit as st
from google.cloud import storage


def upload_blob_from_memory(contents, destination_blob_name, bucket_name="imagine-whack.appspot.com"):
    storage_client = storage.Client.from_service_account_info(
        st.secrets['firebases_key'])
    bucket = storage_client.bucket(bucket_name)

    full_destination_name = st.session_state.user_info['id'] + '/' + destination_blob_name
    blob = bucket.blob(full_destination_name)

    byte_data = (" ".join(contents)).encode('utf-8')
    blob.upload_from_string(byte_data)
