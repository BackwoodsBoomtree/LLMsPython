# App dev framework
import streamlit as st

# Dependencies
from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain

# Path to weights
snoozyPath = 'G:/LLMs/GPT4All-13B-snoozy.ggmlv3.q4_0.bin'
# gptPath    = 'G:/LLMs/chatgpt-gpt-3.5-turbo.txt'
falconPath = 'G:/LLMs/ggml-model-gpt4all-falcon-q4_0.bin'
wizardPath = 'G:/LLMs/GPT4All-13B-snoozy.ggmlv3.q4_0.bin'

# Instance of llm
snoozyLlm = GPT4All(model = snoozyPath, verbose = True)
# gptLlm    = GPT4All(model = gptPath, verbose = True)
falconLlm = GPT4All(model = falconPath, verbose = True)
wizardLlm = GPT4All(model = wizardPath, verbose = True)

# Prompt template
promptTemp = PromptTemplate(input_variables = ['question'],
                        template = """
                        Question: {question}
                        
                        Answer: Let's think step by step
                        """)

# LLM Chain
snoozyChain = LLMChain(prompt = promptTemp, llm = snoozyLlm)
# gptChain    = LLMChain(prompt = promptTemp, llm = gptLlm)
falconChain = LLMChain(prompt = promptTemp, llm = falconLlm)
wizardChain = LLMChain(prompt = promptTemp, llm = wizardLlm)

# Title
st.title('GPT Stack Test for Y\'all')

# Prompt text box
myPrompt = st.text_input('Give me your prompt!')

# if we hit enter
if myPrompt:
    # Snoozy
    snoozyResponse = snoozyChain.run(myPrompt)
    st.write('Snoozy says:')
    st.write(snoozyResponse)
    
    # GPT
    # gptResponse = gptChain.run(myPrompt)
    # st.write('ChatGPT 3.5 Turbo says:')
    # st.write(gptResponse)
    
    # Falcon
    falconResponse = falconChain.run(myPrompt)
    st.write('GPT4All Falcon says:')
    st.write(falconResponse)
    
    # Wizard
    wizardResponse = wizardChain.run(myPrompt)
    st.write('Wizard says:')
    st.write(wizardResponse)
 