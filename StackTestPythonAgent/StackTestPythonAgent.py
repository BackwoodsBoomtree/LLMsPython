# App dev framework
import streamlit as st

# Dependencies
from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain

# Path to weights
PATH = 'G:/LLMs/GPT4All-13B-snoozy.ggmlv3.q4_0.bin'

# Instance of llm
myLlm = GPT4All(model = PATH, verbose = True)

# Prompt template
promptTemp = PromptTemplate(input_variables = ['question'],
                        template = """
                        Question: {question}
                        
                        Answer: Let's think step by step
                        """)

# LLM Chain
chain = LLMChain(prompt = promptTemp, llm = myLlm)

# Title
st.title('GPT Stack Test for Y\'all')

# Prompt text box
myPrompt = st.text_input('Give me your prompt!')

# if we hit enter
if myPrompt:
    # Pass prompt to chain
    response = chain.run(myPrompt)
    
    # Return response
    st.write(response)
