from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_classic.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)
template = PromptTemplate(
    template = '''Generate 5 facts about the {topic}''',
    input_variables = ['topic']
)

parser = StrOutputParser()
chain = template | model | parser
result = chain.invoke({"topic" : input("Enter the topic you want to search : ") })
print(result)

chain.get_graph().print_ascii()