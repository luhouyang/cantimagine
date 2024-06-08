import streamlit as st
from openai import OpenAI


class AIModel:
    def __init__(self):
        self.api_key = st.secrets.openai.openai_api_key

    def initModel(self):
        client = OpenAI(
            api_key=self.api_key,
        )
        return client

    def loadChatCompletion(self, messages):
        client = self.initModel()
        stream = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
            stream=True, max_tokens=600, temperature=0.5
        )
        return stream
