import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import streamlit as st
import simple_webbrowser as swb
import firebase_admin
from firebase_admin import auth, credentials


def create_firebase_user(email):
    try:
        user = auth.get_user_by_email(email)
        # st.write(f"User already exists in Firebase: {user.uid}")
    except auth.UserNotFoundError:
        user = auth.create_user(
            email=email,
            email_verified=True
        )
        # st.write(f"Created new Firebase user: {user.uid}")


def auth_flow():
    auth_secret = {'web': st.secrets.fireauth}
    auth_code = st.query_params.get("code")
    # flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    #     "C:\\Users\\User\\Desktop\\python\\langchain_tuto\\not_uploaded\\auth-secret.json", # replace with you json credentials from your google auth app
    #     scopes=["https://www.googleapis.com/auth/userinfo.email", "openid"],
    #     redirect_uri="http://localhost:8501",
    # )
    flow = google_auth_oauthlib.flow.Flow.from_client_config(auth_secret,  # replace with you json credentials from your google auth app
                                                             scopes=[
                                                                 "https://www.googleapis.com/auth/userinfo.email", "openid"],
                                                             redirect_uri="http://localhost:8501",
                                                             )  # https://cantimagine-imaginewhack.streamlit.app
    if auth_code:
        flow.fetch_token(code=auth_code)
        credentials = flow.credentials
        # st.write("Login Done")
        user_info_service = build(
            serviceName="oauth2",
            version="v2",
            credentials=credentials,
        )
        user_info = user_info_service.userinfo().get().execute()
        assert user_info.get("email"), "Email not found in infos"
        st.session_state["google_auth_code"] = auth_code
        st.session_state["user_info"] = user_info

        create_firebase_user(user_info.get("email"))
    else:
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            container = st.container(border=True, height=400)
            with container:
                col4, col5, col6 = st.columns([1, 1, 1])
                with col5:
                    st.header("Log in")
                st.text("Sign in now to \naccelerate your startup idea!")
                # st.image("asset/spy.png", width=200)
                if st.button("Sign in with Google", use_container_width=True):
                    authorization_url, state = flow.authorization_url(
                        access_type="offline",
                        include_granted_scopes="true",
                        prompt="select_account"
                    )
                    # webbrowser.open_new_tab(authorization_url)
                    swb.website(url=authorization_url, new=1)
