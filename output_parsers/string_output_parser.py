from langchain_classic.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import warnings 
warnings.filterwarnings("ignore")
parser = StrOutputParser()

# llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash", temperature = 0)
model = ChatOpenAI(model = 'gpt-5', temperature=0)
template1 = PromptTemplate(
    template = '''write a detailed report on {topic}''',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = '''Write 5 line summary on the following text {text}''',
    input_variables= ['text']
)

prompt1 = template1.invoke({"topic" : "Machine learning"})
# response1 = llm.invoke(prompt1).content[0]['text']
# print(response1)
# prompt2 = template2.invoke({"text" : response1})
# response2 = llm.invoke(prompt2).content[0]['text']
# print()
# print(response2)

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic" : "Machine Learning "})
print(result)