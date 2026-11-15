from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

chat_history = [
    SystemMessage(content='you are a helpful ai assistant'),
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content = user_input))

    if user_input == 'exit':
        break
    prompt = model.invoke(chat_history)
    chat_history.append(AIMessage(content=prompt.content))
    print("AI: ",prompt.content)

print(chat_history)