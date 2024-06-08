from openai import OpenAI
import streamlit as st


class AIModel:
    def __init__(self):
        api_key = st.secrets.openai.openai_api_key

    def initModel():
        client = OpenAI(
            api_key=st.secrets.openai.openai_api_key,
        )
        return client

    def loadChatCompletion(self):
        client = self.initModel()
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-3.5-turbo",
        )
