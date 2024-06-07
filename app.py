import streamlit as st
import page.home_page as home
import page.chat_page as chat
import page.account_page as acc
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Questionable",
        options=["Home", "Chat", "Account"],
        default_index=0)

if selected == "Home":
    home.home_page()
elif selected == "Chat":
    chat.chat_page()
elif selected == "Account":
    acc.account_page()
