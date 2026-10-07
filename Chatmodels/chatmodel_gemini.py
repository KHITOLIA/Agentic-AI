from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash", temperature = 0)
result = llm.invoke("What is machine learning ? ")
print(result.content[0]['text'])