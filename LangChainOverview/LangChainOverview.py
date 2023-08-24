# Citation: Sophia Yang https://www.youtube.com/watch?v=kmbS6FDQh7c&t=78s&ab_channel=SophiaYang

import os
import langchain
from langchain.llms import OpenAI, Cohere, HuggingFaceHub
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

print('HELLO!\n')

os.environ["OPENAI_API_KEY"]           = "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"
os.environ["COHERE_API_KEY"]           = "dfy6sa9PQ1jU6xZs5CWCgHurNNjy2jqEgKihwVVm"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["SERPAPI_API_KEY"]          = "499bc6604439611d10af444dc8d3d7775ea87fc10d0de30e26783b9b76071e89"

chatgpt = ChatOpenAI(model_name = 'gpt-3.5-turbo')
gpt3    = OpenAI(model_name = 'text-davinci-003')
cohere  = Cohere(model = 'command-xlarge')
flan    = HuggingFaceHub(repo_id = 'google/flan-t5-xxl')

text = "Should I stay in academia?"
print(text + "\n")

print('ChatGPT 3.5 Turbo says:\n')
print(chatgpt([HumanMessage(content = text)]))

print('\nChatGPT 3 Turbo says:\n')
print(gpt3(text))

print('\nCohere says:\n')
print(cohere(text))

print('\nFlan says:\n')
print(flan(text))

