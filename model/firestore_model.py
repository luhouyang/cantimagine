import streamlit as st
from google.cloud import firestore
from entities.userdata_entity import UserdataEntity


def set_userdata(userdataEntity):
    db = firestore.Client.from_service_account_info(
        st.secrets['firebases_key'])
    res = db.collection("users").document(st.session_state.user_info["id"]).set(userdataEntity)

def get_userdata():
    db = firestore.Client.from_service_account_info(
        st.secrets['firebases_key'])
    res = db.collection("users").document(st.session_state.user_info["id"]).get()
    return res

def get_home_page_data():
    db = firestore.Client.from_service_account_info(st.secrets['firebases_key'])
    res = db.collection('users').order_by('date').limit(5).get()
    data = []
    for doc in res:
        data.append(UserdataEntity.from_firestore(doc))
    return data
