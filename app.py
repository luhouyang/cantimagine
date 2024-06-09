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
from model.firestore_model import get_userdata, get_home_page_data
from model.cloud_storage import get_blob_from_firebase
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

        col1, col2, col3 = st.columns(3)
        with col2:
            # st.image(image=user_info['picture'])
            st.image(image="asset/pigeon.png")
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.write(user_info['email'])

        selected = option_menu(
            menu_icon="robot",
            menu_title="Pigeon",
            options=["Home", "Elevator Pitch", "Idea Kitchen", "Data Source"],
            icons=["house-fill", "lightbulb", "chat-fill", "person-circle"],
            default_index=0,
        )

        container = st.container(height=300)
        with container:
            if "model" in st.session_state:
                st.session_state.model = "gpt-3.5-turbo"
            if "max_tokens" in st.session_state:
                st.session_state.max_tokens = 500
            if "temperature" in st.session_state:
                st.session_state.temperature = 0.5
            st.session_state.model = st.radio("Select model", options=[
                "gpt-3.5-turbo", "gpt-4"], index=0)
            st.session_state.max_tokens = st.number_input(
                "Max Tokens", value=500, min_value=0, max_value=4000, step=100, )
            st.session_state.temperature = st.slider(
                "Temperature", min_value=0.0, max_value=1.0, step=0.1, value=0.5)

    # global state variables
    if 'userdata' not in st.session_state:
        try:
            data = get_userdata()
            userdataEntity = UserdataEntity.from_firestore(data)
            st.session_state.userdata = userdataEntity.to_dict()
            st.session_state.home_page_data = get_home_page_data()
            st.session_state.pdf_datas = get_blob_from_firebase()
        except:
            st.session_state.userdata = UserdataEntity().to_dict()
            st.session_state.home_page_data = get_home_page_data()
            st.session_state.pdf_datas = []

    if selected == "Home":
        home.home_page()

    elif selected == "Elevator Pitch":
        pitch.pitch_page()
    elif selected == "Idea Kitchen":
        chat.chat_page()
    elif selected == "Data Source":
        acc.account_page()
    else:
        err.error_page()
