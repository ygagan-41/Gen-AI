from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt = PromptTemplate(
    template="write a summary for the following poem \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt',encoding='utf-8')

docs = loader.load()
""" 
print(docs)
print(len(docs))
print(type(docs))
print(docs[0].page_content)
print(docs[0].metadata) """

chain = prompt |model | parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)