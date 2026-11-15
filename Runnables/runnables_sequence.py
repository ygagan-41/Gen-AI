#prompt -> jokes

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="explain the following joke - {text}",
    input_variables=['text']
)

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser,prompt2,model,parser)

result = chain.invoke({'topic':'AI'})

print(result)