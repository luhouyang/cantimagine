import streamlit as st


def error_page():
    errorPage = st.container()
    with errorPage:
        st.header("Error 404")
