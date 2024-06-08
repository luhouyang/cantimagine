# import packages
import streamlit as st
from model.model import AIModel
import model.prompt as prt
import datetime
from model.firestore_model import set_userdata
from entities.userdata_entity import UserdataEntity
from model.slides_generator import SlideGenerator

# global variables
user_prompt_template = """
My company, {name_of_company}, 
is developing {offering} to help {audience} to {problem_solved} with {technologies}.
We plan to operate in {area_of_operation}.
We compete in growing {market} market,
which last year was a {value} value market.
We are similar to {competitor1} and {competitor2},
but we {key_difference}.
Currently we have {state_of_startup}.
We are looking for {resources_asked} to help us {how_resources_used}.
"""


#
# functions
#

# evaluate elevator pitch
def evaluatePitch():
    chat_ai = AIModel()

    # if "slides_gen_messages" not in st.session_state:
    #     st.session_state.slides_gen_messages = [
    #         {
    #             "role": "system",
    #             "content": prt.slides_system_message.format_map(st.session_state.userdata)
    #         }
    #     ]
    # slide_gen = SlideGenerator()
    # slides_titles = slide_gen.slide_titles
    # slide_contents = [slide_gen.generate_slide_content(
    #     st.session_state.slides_gen_messages + [{"role": "user", "content": f'Generate pitch deck part for{title}'}]) for title in slides_titles]

    # slide_gen.create_presentation(slides_titles, slide_contents)
    # st.success("Presentation generated successfully!")
    # st.markdown(slide_gen.get_ppt_download_link(), unsafe_allow_html=True)

    # st.session_state.slides_gen_messages.append({
    #     "role": "user",
    #     "content": user_prompt_template.format_map(st.session_state.pitch_details)
    # })

    # for message in st.session_state.slides_gen_messages:
    #     if message["role"] != "system":
    #         with st.chat_message(message["role"]):
    #             st.markdown(message["content"])

    # with st.chat_message("assistant"):
    #     message_placeholder = st.empty()
    full_response = ""
    #     for chunck in chat_ai.loadChatCompletion(
    #         [
    #             {"role": m["role"], "content": m["content"]} for m in st.session_state.slides_gen_messages
    #         ]
    #     ):
    #         full_response += chunck.choices[0].delta.content or ""
    #         message_placeholder.markdown(full_response + " ")
    #     message_placeholder.markdown(full_response)
    # st.session_state.slides_gen_messages.append(
    #     {"role": "assistant", "content": full_response})

    st.session_state.userdata['pitch'] = full_response
    st.session_state.userdata['date'] = datetime.datetime.now()
    userdataEntity = UserdataEntity(**st.session_state.userdata)
    set_userdata(userdataEntity.to_dict())


def two_col(obj1, obj2):
    col1, col2 = st.columns(2)

    with col1:
        if value1 := st.text_input(key=obj1[2], label=obj1[0], placeholder=obj1[1], value=st.session_state.userdata[obj1[2]]):
            st.session_state.userdata[obj1[2]] = value1

    with col2:
        if value2 := st.text_input(key=obj2[2], label=obj2[0], placeholder=obj2[1], value=st.session_state.userdata[obj2[2]]):
            st.session_state.userdata[obj2[2]] = value2

# ui page


def pitch_page():
    pitchPage = st.container()
    with pitchPage:

        st.title("Elevator Pitch")
        left_col, right_col = st.columns(2)

        with left_col:
            container = st.container(height=400)
            with container:
                st.header("About Startup")
                two_col(["My company", "company name", 'name_of_company'], [
                        "Is developing", "product/service", 'offering'])
                two_col(["To help", "audience", 'audience'], [
                        "To solve", "problem solved", 'problem_solved'])
                two_col(["Using", "technologies", 'technologies'], [
                        "We plan to operate", "area of operation", 'area_of_operation'])
            container = st.container(height=200)
            with container:
                st.header("About Market")
                two_col(["We compete in", "market", 'market'], [
                        "Last years market value", "value e.g. 100 million", 'value'])

        with right_col:
            container = st.container(height=300)
            with container:
                st.header("Competitors & Key Difference")
                two_col(["We are similar to", "company 1", 'competitor1'], [
                    "We are similar to", "company 2", 'competitor2'])
                if value := st.text_input(label="Our key difference", placeholder="key difference", value=st.session_state.userdata['key_difference']):
                    st.session_state.userdata['key_difference'] = value
            container = st.container(height=300)
            with container:
                st.header("Funding")
                if value := st.text_input(label="Current state and progress", placeholder="state", value=st.session_state.userdata['state_of_startup']):
                    st.session_state.userdata['state_of_startup'] = value
                two_col(["We are looking for", "resources", 'resources_asked'], [
                        "To help us", "how resources are used", 'how_resources_used'])

        st.write(user_prompt_template.format_map(
            st.session_state.userdata))

        if st.button(label="Evaluate Pitch"):
            evaluatePitch()
