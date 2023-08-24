import os
from langchain.document_loaders import Docx2txtLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = "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"

wordLoad = Docx2txtLoader('C:/Users/doug0002/Downloads/ChloFluo_Scientific_Data.docx')
index    = VectorstoreIndexCreator().from_loaders([wordLoad])

myQuery  = "What is solar induced chlorophyll fluorescence?"
response = index.query(myQuery)

print(response)