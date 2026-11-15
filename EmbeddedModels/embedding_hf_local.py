from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

""" text = "delhi is the capital of india"

vector = embedding.embed_query(text) """

docs = [
    "delhi is the capital of india",
    "kolkata is the capital of west bengal",
    "paris is the capital of france"
]

vector = embedding.embed_documents(docs)

print(str(vector))