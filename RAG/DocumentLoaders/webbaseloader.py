from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

url = 'https://www.amazon.in/iQOO-Lite-Solar-Flame-Storage/dp/B07WYMJPVS/ref=s9_acsd_al_ot_c2_x_0_t?_encoding=UTF8&pf_rd_t='

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

