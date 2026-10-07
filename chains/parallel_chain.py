from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_classic.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",
    task = "text-generation",
    max_new_tokens = 5000,
    temperature = 0
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

temp1 = PromptTemplate(
    template = '''Generate the detailed report on the {text}''',
    input_variables = ['text']
)

temp2 = PromptTemplate(
    template = '''Generate the 5 point summary about the following {text}''',
    input_variables = ['text']
)
temp3 = PromptTemplate(
    template = '''Return me the report and summary \n{report} and \n{summary}''',
    input_variables = ['topic', 'report']
)

parallel_chain = RunnableParallel(
    {'report' : temp1 | model | parser,
     'summary' : temp2 | model | parser}
)

merge_chain = temp3 | model | parser
chain = parallel_chain | merge_chain

chain.get_graph().print_ascii()
result = chain.invoke({"text" : "Machine learning"})

print(result)