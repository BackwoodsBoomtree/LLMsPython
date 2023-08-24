import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    )
os.environ["OPENAI_API_KEY"] = "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"

human_message_prompt = HumanMessagePromptTemplate(
    prompt = PromptTemplate(
        template = "What is a good name for a company that makes {product}?",
        input_variables = ["product"],
        )
    )

chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
chat  = ChatOpenAI(temperature = 0.9)
chain = LLMChain(llm = chat, prompt = chat_prompt_template)

second_prompt = PromptTemplate(
    input_variables = ["company_name"],
    template = "Write a catchphrase for the following company: {company_name}",
    )

llm = OpenAI(temperature = 0)

chain_two = LLMChain(llm = llm, prompt = second_prompt)

overall_chain = SimpleSequentialChain(chains = [chain, chain_two], verbose = True)

catchphrase = overall_chain.run("gems and minerals")
print(catchphrase)