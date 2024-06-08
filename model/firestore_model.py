import streamlit as st
from google.cloud import firestore

def set_userdata(output):
    db = firestore.Client.from_service_account_info(st.secrets['firebase'])
    doc_ref = db.collection("users").document().id
    db.collection("users").document(doc_ref).set(
        {
            "docId": doc_ref,
            "content": output
        }
    )

def get_userdata():
    # Then query to list all users
    db = firestore.Client.from_service_account_info(st.secrets['firebase'])
    users_ref = db.collection('users')
    return users_ref