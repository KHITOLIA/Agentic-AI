from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import warnings
warnings.filterwarnings("ignore")

def simple_prompt(text):
    llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash", temperature = 0)
    result = llm.invoke(text)
    print(result.content[0]['text'])

while True:
    print(simple_prompt(input("Enter your query : ")))