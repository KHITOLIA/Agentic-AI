from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOpenAI(model = 'gpt-5', temperature=0)

chat_history = [
    SystemMessage(content = "You are a helpful assistant in tech field so respond accordingly")
]

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    else:
        response = model.invoke(chat_history).content
        chat_history.append(AIMessage(content = response))
        print(f"AI : {response}" )
print(chat_history)
