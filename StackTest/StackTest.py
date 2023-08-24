# Citation: Nicholas Renotte https://www.youtube.com/watch?v=5JpPo-NOq9s&ab

# App dev framework
import streamlit as st

# Dependencies
from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain

# Path to weights
# snoozyPath = 'G:/LLMs/GPT4All-13B-snoozy.ggmlv3.q4_0.bin'
hermesPath = 'G:/LLMs/nous-hermes-13b.ggmlv3.q4_0.bin'
falconPath = 'G:/LLMs/ggml-model-gpt4all-falcon-q4_0.bin'
wizardPath = 'G:/LLMs/wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin'

# Instance of llm
# snoozyLlm = GPT4All(model = snoozyPath, verbose = True)
hermesLlm = GPT4All(model = hermesPath, verbose = True)
falconLlm = GPT4All(model = falconPath, verbose = True)
wizardLlm = GPT4All(model = wizardPath, verbose = True)

# Prompt template
promptTemp = PromptTemplate(input_variables = ['question'],
                        template = """
                        Question: {question}
                        
                        Answer: Let's think step by step
                        """)

# LLM Chain
# snoozyChain = LLMChain(prompt = promptTemp, llm = snoozyLlm)
hermesChain = LLMChain(prompt = promptTemp, llm = hermesLlm)
falconChain = LLMChain(prompt = promptTemp, llm = falconLlm)
wizardChain = LLMChain(prompt = promptTemp, llm = wizardLlm)

# Title
st.title('GPT Stack Test for Fun Y\'all')

# Prompt text box
myPrompt = st.text_input('Give me your prompt!')

# if we hit enter
if myPrompt:
    # Snoozy
    # snoozyResponse = snoozyChain.run(myPrompt)
    # st.write('Snoozy says:')
    # st.write(snoozyResponse)
    
    # Hermes
    hermesResponse = hermesChain.run(myPrompt)
    st.write('Hermes says:')
    st.write(hermesResponse)
    
    # Falcon
    falconResponse = falconChain.run(myPrompt)
    st.write('GPT4All Falcon says:')
    st.write(falconResponse)
    
    # Wizard
    wizardResponse = wizardChain.run(myPrompt)
    st.write('Wizard says:')
    st.write(wizardResponse)
 