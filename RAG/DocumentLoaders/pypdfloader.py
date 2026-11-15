from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(docs)

print(len(docs))

print(docs[0].page_content)

print(docs[1].metadata)

