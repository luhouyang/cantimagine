import streamlit as st
import page.home_page as home
import page.chat_page as chat
import page.account_page as acc
import page.error_page as err
import page.pitch_page as pitch
from page.auth import auth_flow
from streamlit_option_menu import option_menu
import firebase_admin
from firebase_admin import credentials
from model.firestore_model import get_userdata
from entities.userdata_entity import UserdataEntity

try: 
    app = firebase_admin.get_app()
except ValueError as e:
    cert = {
        "type": st.secrets["firebases_key"]["type"],
        "project_id": st.secrets["firebases_key"]["project_id"],
        "private_key_id": st.secrets["firebases_key"]["private_key_id"],
        "private_key": st.secrets["firebases_key"]["private_key"],
        "client_email": st.secrets["firebases_key"]["client_email"],
        "client_id": st.secrets["firebases_key"]["client_id"],
        "auth_uri": st.secrets["firebases_key"]["auth_uri"],
        "token_uri": st.secrets["firebases_key"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["firebases_key"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["firebases_key"]["client_x509_cert_url"],
        "universe_domain": st.secrets["firebases_key"]["universe_domain"],
    }
    cred = credentials.Certificate(cert)
    firebase_admin.initialize_app(cred)

st.set_page_config(layout="wide")

if "google_auth_code" not in st.session_state:
    auth_flow()

if "google_auth_code" in st.session_state:
    user_info = st.session_state["user_info"]
    # st.write(user_info)

    with st.sidebar:

        selected = option_menu(
            menu_icon="robot",
            menu_title="StartupEco",
            options=["Home", "Elevator Pitch", "Idea Kitchen", "Account"],
            icons=["house-fill", "lightbulb", "chat-fill", "person-circle"],
            default_index=0,
        )

    # global state variables
    if 'userdata' not in st.session_state:
        try:
            data = get_userdata()
            userdataEntity = UserdataEntity.from_firestore(data)
            st.session_state.userdata = userdataEntity.to_dict()
        except:
            st.session_state.userdata = UserdataEntity().to_dict()

    if selected == "Home":
        home.home_page()

    elif selected == "Elevator Pitch":
        pitch.pitch_page()
    elif selected == "Idea Kitchen":
        chat.chat_page()
    elif selected == "Account":
        acc.account_page()
    else:
        err.error_page()
