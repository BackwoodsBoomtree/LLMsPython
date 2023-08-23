# App dev framework
import streamlit as st

# Dependencies
from langchain.llms import GPT4All

# Python toolchain imports
from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool

# Path to weights
PATH = 'G:/LLMs/GPT4All-13B-snoozy.ggmlv3.q4_0.bin'

# Instance of llm
myLlm = GPT4All(model = PATH, verbose = True)

# Create python agent
python_agent = create_python_agent(llm = myLlm, tool = PythonREPLTool(), verbose = True)

# Title
st.title('GPT Stack Test for Y\'all')

# Prompt text box
myPrompt = st.text_input('Give me your prompt!')

# if we hit enter
if myPrompt:
    # Pass prompt to chain
    response = python_agent.run(myPrompt)
    
    # Return response
    st.write(response)
