from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model='',dimensions=32)

documents =[
    "Delhi is the capital of india",
    "Kolkata is the captial of west bengal"
]
result = embeddings.embed_documents("Delhi is the capital of india")

print(str(result))