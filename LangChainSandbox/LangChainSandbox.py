
# This script combines API calls and streamlit

# App dev framework
import os
import streamlit as st
import langchain
from langchain.llms import OpenAI, Cohere, HuggingFaceHub
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Keys
os.environ["OPENAI_API_KEY"]           = "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"
os.environ["COHERE_API_KEY"]           = "dfy6sa9PQ1jU6xZs5CWCgHurNNjy2jqEgKihwVVm"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["SERPAPI_API_KEY"]          = "499bc6604439611d10af444dc8d3d7775ea87fc10d0de30e26783b9b76071e89"

# Models
chatgpt = ChatOpenAI(model_name = 'gpt-3.5-turbo')
gpt3    = OpenAI(model_name = 'text-davinci-003')
cohere  = Cohere(model = 'command-xlarge')
flan    = HuggingFaceHub(repo_id = 'google/flan-t5-xxl')

# Title
st.title('GPT Stack Test for Fun Y\'all')

# Prompt text box
myPrompt = st.text_input('Give me your prompt!')

# if we hit enter
if myPrompt:
    st.write('ChatGPT 3.5 Turbo says:\n')
    st.write(chatgpt([HumanMessage(content = myPrompt)]))

    st.write('\nChatGPT 3 says:\n')
    st.write(gpt3(myPrompt))

    st.write('\nCohere says:\n')
    st.write(cohere(myPrompt))

    st.write('\nFlan says:\n')
    st.write(flan(myPrompt))