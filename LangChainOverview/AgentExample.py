import os
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent

os.environ["OPENAI_API_KEY"]  = "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"
os.environ["SERPAPI_API_KEY"] = "499bc6604439611d10af444dc8d3d7775ea87fc10d0de30e26783b9b76071e89"

gpt3  = OpenAI(model_name = 'text-davinci-003')

# This method uses calculator
print('This is the calculator agent method:')
tools = load_tools(['serpapi', 'llm-math'], llm = gpt3)
agent = initialize_agent(tools, llm = gpt3, agent = 'zero-shot-react-description', verbose = True)
agent.run('In what year was American Fidelity Assurance founded? What is the square root of its founding year to two decimal places?')

# This method uses python and prints the code
print('\n\nThis is the python REPL agent method:')
tools = load_tools(['serpapi', 'python_repl'], llm = gpt3)
agent = initialize_agent(tools, llm = gpt3, agent = 'zero-shot-react-description', verbose = True)
agent.run('In what year was American Fidelity Assurance founded? What is the square root of its founding year to two decimal places?')