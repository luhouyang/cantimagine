# import packages
import streamlit as st
from model.model import AIModel
from model.prompt import elevator_system_message

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


# global state variables
if 'pitch_details' not in st.session_state:
     st.session_state.pitch_details = {
          'name_of_company': "",
          'offering': "",
          'audience': "",
          'problem_solved': "",
          'technologies': "",
          'area_of_operation': "",
          'market': "",
          'value': "",
          'competitor1': "",
          'competitor2': "",
          'key_difference': "",
          'state_of_startup': "",
          'resources_asked': "",
          'how_resources_used': ""
     }


#
# functions
#

# evaluate elevator pitch
def evaluatePitch():
    chat_ai = AIModel()
    container = st.container(height=500)
    with container:
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system",
                    "content": elevator_system_message.format_map(st.session_state.pitch_details)
                    },
                {
                    "role": "assistant", "content": "Here is your evaluation"
                    }
                ]
            
        st.session_state.messages.append({
            "role": "user", 
            "content": user_prompt_template.format_map(st.session_state.pitch_details)
            })

        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    for chunck in chat_ai.loadChatCompletion(
                        [
                         {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
                        ]
                        ):
                        full_response += chunck.choices[0].delta.content or ""
                        message_placeholder.markdown(full_response + " ")
                    message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})


# ui page
def pitch_page():
    pitchPage = st.container()
    with pitchPage:
        st.title("Elevator Pitch")
        st.divider()

        st.write("Text text2")
        st.text_input(label="company", placeholder="company")
        st.write("Text text2")
        st.text_input(label="offering", placeholder="offering")
