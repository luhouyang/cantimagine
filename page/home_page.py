import streamlit as st
from model.firestore_model import get_home_page_data


def home_page():
    homePage = st.container()
    with homePage:
        st.title("Home Page")
        st.divider()

        data = get_home_page_data()
        st.write(data[0].name_of_company)
