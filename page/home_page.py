import streamlit as st
from model.firestore_model import get_home_page_data


def home_page():
    homePage = st.container()
    with homePage:
        st.title("Home Page")
        st.divider()

        col1, col2, col3 = st.columns(3)
        col4, col5 = st.columns(2)
        if "home_page_data" in st.session_state:
            for i in range(len(st.session_state.home_page_data)):
                if (i % 3 == 0):
                    with col3:
                        container = st.container(height=200)
                        with container:
                            st.subheader(st.session_state.home_page_data[i].name_of_company)
                            st.markdown(st.session_state.home_page_data[i].offering)
                            st.markdown(st.session_state.home_page_data[i].problem_solved)
                elif (i % 2 == 0):
                    with col2:
                        container = st.container(height=200)
                        with container:
                            st.subheader(st.session_state.home_page_data[i].name_of_company)
                            st.markdown(st.session_state.home_page_data[i].offering)
                            st.markdown(st.session_state.home_page_data[i].problem_solved)
                elif (i % 2 == 1):
                    with col1:
                        container = st.container(height=200)
                        with container:
                            st.subheader(st.session_state.home_page_data[i].name_of_company)
                            st.markdown(st.session_state.home_page_data[i].offering)
                            st.markdown(st.session_state.home_page_data[i].problem_solved)
                elif (i % 4 == 0):
                    with col4:
                        container = st.container(height=200)
                        with container:
                            st.subheader(st.session_state.home_page_data[i].name_of_company)
                            st.markdown(st.session_state.home_page_data[i].offering)
                            st.markdown(st.session_state.home_page_data[i].problem_solved)
                elif (i % 5 == 0):
                    with col5:
                        container = st.container(height=200)
                        with container:
                            st.subheader(st.session_state.home_page_data[i].name_of_company)
                            st.markdown(st.session_state.home_page_data[i].offering)
                            st.markdown(st.session_state.home_page_data[i].problem_solved)
