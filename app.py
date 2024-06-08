import streamlit as st
import page.home_page as home
import page.chat_page as chat
import page.account_page as acc
import page.error_page as err
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
with st.sidebar:

    selected = option_menu(
        menu_icon="robot",
        menu_title="StartupEco",
        options=["Home", "Chat Bot", "Account"],
        icons=["house-fill", "chat-fill", "person-circle"],
        default_index=0,
    )

if selected == "Home":
    home.home_page()
elif selected == "Chat Bot":
    chat.chat_page()
elif selected == "Account":
    acc.account_page()
else:
    err.error_page()
