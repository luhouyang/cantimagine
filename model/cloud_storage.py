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

    byte_data = ("".join(contents)).encode('utf-8')
    blob.upload_from_string(byte_data)

    st.session_state.userdata['blobs_urls'].append(full_destination_name)
    userdata = UserdataEntity(**st.session_state.userdata)
    set_userdata(userdata.to_dict())


def get_blob_from_firebase(bucket_name="imagine-whack.appspot.com"):
    storage_client = storage.Client.from_service_account_info(st.secrets['firebases_key'])
    bucket = storage_client.bucket(bucket_name)

    uris = st.session_state.userdata['blobs_urls']
    data = []
    for uri in uris:
        blob = bucket.blob(uri)
        print(blob.name.split("/")[1])
        res = blob.download_as_bytes()
        data.append({
            'name': blob.name.split("/")[1],
            'content': str(res.decode('utf-8'))
            })
    return data
