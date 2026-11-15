from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

def word_counter(text):
    return len(text.split())

prompt = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model,parser)

parallel_chain= RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_counter)
})

final_joke = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_joke.invoke({'topic':'cinema'})

print(result)