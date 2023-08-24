import os
from langchain.document_loaders import Docx2txtLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = "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"

wordLoad = Docx2txtLoader('C:/Users/doug0002/Downloads/ChloFluo_Scientific_Data.docx')
index    = VectorstoreIndexCreator().from_loaders([wordLoad])

myQuery  = "What is solar induced chlorophyll fluorescence?"
response = index.query(myQuery)

print(response)