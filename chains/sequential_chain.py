# generate the detailed report on any topic  t1 | m | parser
# generate the summary of that report  t2 | m | parser

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

temp1 = PromptTemplate(
    template = '''Generate the detailed report on the {topic}''',
    input_variables = ['topic']
)

temp2 = PromptTemplate(
    template = '''Generate the 5 point summary about the following {report}''',
    input_variables = ['report']
)
parser = StrOutputParser()

chain = temp1 | model | parser | temp2 | model | parser
result = chain.invoke({"topic" : input("enter the topic : ")})
print(result)
print()

chain.get_graph().print_ascii()
