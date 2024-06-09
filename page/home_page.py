import streamlit as st
from model.firestore_model import get_home_page_data


def home_page():
    homePage = st.container()
    with homePage:
        st.title("Welcome to Pigeon🕊️")
        st.text("Pigeon is your go-to platform to validate, develop, and solidify your startup idea.\nWith our integrated Gen AI, you can launch your brilliant idea in no time!")

        st.subheader("Key Features")
        st.markdown(
            "1. **ELEVATOR PITCH**: A generative AI *pitch deck* generator to help you secure investors and convince buyers in no time.")
        st.markdown(
            "2. **IDEA KITCHEN**: A well-trained *ideation expert* that assist you to access your startup idea critically.")
        st.markdown(
            "3. **WIDE KNOWLEDGE BASE**: The implementation of *Retrieval-Augmented Generation (RAG)* makes high precision prompting possible.")
        st.subheader("Registered Startups")
        col1, col2, col3 = st.columns(3)
        col4, col5 = st.columns(2)
        if "home_page_data" in st.session_state:
            for i in range(len(st.session_state.home_page_data)):
                if (i % 3 == 0):
                    with col3:
                        container = st.container(height=200)
                        with container:
                            st.subheader(
                                st.session_state.home_page_data[i].name_of_company)
                            st.markdown(
                                st.session_state.home_page_data[i].offering)
                            st.markdown(
                                st.session_state.home_page_data[i].problem_solved)
                elif (i % 2 == 0):
                    with col2:
                        container = st.container(height=200)
                        with container:
                            st.subheader(
                                st.session_state.home_page_data[i].name_of_company)
                            st.markdown(
                                st.session_state.home_page_data[i].offering)
                            st.markdown(
                                st.session_state.home_page_data[i].problem_solved)
                elif (i % 2 == 1):
                    with col1:
                        container = st.container(height=200)
                        with container:
                            st.subheader(
                                st.session_state.home_page_data[i].name_of_company)
                            st.markdown(
                                st.session_state.home_page_data[i].offering)
                            st.markdown(
                                st.session_state.home_page_data[i].problem_solved)
                elif (i % 4 == 0):
                    with col4:
                        container = st.container(height=200)
                        with container:
                            st.subheader(
                                st.session_state.home_page_data[i].name_of_company)
                            st.markdown(
                                st.session_state.home_page_data[i].offering)
                            st.markdown(
                                st.session_state.home_page_data[i].problem_solved)
                elif (i % 5 == 0):
                    with col5:
                        container = st.container(height=200)
                        with container:
                            st.subheader(
                                st.session_state.home_page_data[i].name_of_company)
                            st.markdown(
                                st.session_state.home_page_data[i].offering)
                            st.markdown(
                                st.session_state.home_page_data[i].problem_solved)
