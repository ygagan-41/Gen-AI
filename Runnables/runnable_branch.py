from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summarize the following \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser

# RunnableSequence(prompt1,model,parser) same as model | prompt | parser

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>200, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)

result = final_chain.invoke({'topic':'cinema'})

print(result)