from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import warnings
warnings.filterwarnings("ignore")

# llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash", temperature = 0)
model = ChatOpenAI(model = 'gpt-5', temperature=0)
chat_history = []
while True:
    user_input = input("Enter the query : ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    else:
        response = model.invoke(chat_history).content
        chat_history.append(response)
        print(f"You : {user_input}")
        print()
        print(f"AI : {response}")
print(chat_history)