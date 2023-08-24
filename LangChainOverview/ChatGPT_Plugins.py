import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.tools import AIPluginTool

os.environ["OPENAI_API_KEY"]  = "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"

tool = AIPluginTool.from_plugin_url("https://www.klarna.com/.well-known/ai-plugin.json")

llm   = ChatOpenAI(temperature = 0)
tools = load_tools(["requests"])
tools += [tool]

agent_chain = initialize_agent(tools, llm, agent = 'zero-shot-react-description', verbose = True)

agent_chain.run("What t-shirts are available in klarna?")