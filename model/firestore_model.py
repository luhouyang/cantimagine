import streamlit as st
from google.cloud import firestore


def set_userdata(userdataEntity):
    db = firestore.Client.from_service_account_info(
        st.secrets['firebases_key'])
    res = db.collection("users").document(st.session_state.user_info["id"]).set(userdataEntity)


def get_userdata():
    # Then query to list all users
    db = firestore.Client.from_service_account_info(
        st.secrets['firebases_key'])
    res = db.collection("users").document(st.session_state.user_info["id"]).get()
    return res
