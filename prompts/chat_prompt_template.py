from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_templates = ChatPromptTemplate([

    ('system','you are a helpful {domain} expert'),
    ('human','Explain in simple terms , what is {topic}')
])

prompt = chat_templates.invoke(
    {
        'domain':'cricket',
        'topic':'googly'
    }
)

print(prompt)