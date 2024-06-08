import streamlit as st
from google.cloud import storage
from model.firestore_model import set_userdata
from entities.userdata_entity import UserdataEntity


def upload_blob_from_memory(contents, destination_blob_name, bucket_name="imagine-whack.appspot.com"):
    storage_client = storage.Client.from_service_account_info(
        st.secrets['firebases_key'])
    bucket = storage_client.bucket(bucket_name)

    full_destination_name = st.session_state.user_info['id'] + '/' + destination_blob_name
    blob = bucket.blob(full_destination_name)

    byte_data = (" ".join(contents)).encode('utf-8')
    blob.upload_from_string(byte_data)

    newBlobs = st.session_state.userdata['blobs_urls'].append(full_destination_name)
    userdata = UserdataEntity(**st.session_state.userdata, blobs_urls=newBlobs)
    set_userdata(userdata)


def get_blob_from_memory(bucket_name="imagine-whack.appspot.com"):
    storage_client = storage.Client.from_service_account_info(st.secrets['firebase_key'])
    bucket = storage_client.bucket(bucket_name)

    uris = st.session_state.userdata['blobs_urls']
    data = []
    for uri in uris:
        blob = bucket.get_blob(uri)
        data.append(str(blob.decode('utf-8')))
    return data
