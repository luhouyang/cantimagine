import streamlit as st
import page.home_page as home
import page.chat_page as chat
import page.account_page as acc
import page.error_page as err
import page.pitch_page as pitch
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
with st.sidebar:

    selected = option_menu(
        menu_icon="robot",
        menu_title="StartupEco",
        options=["Home", "Elevator Pitch", "Idea Kitchen", "Account"],
        icons=["house-fill", "lightbulb", "chat-fill", "person-circle"],
        default_index=0,
    )

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
