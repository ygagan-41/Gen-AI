from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model='',dimensions=32)

result = embeddings.embed_query("Delhi is the capital of india")

print(str(result))