from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
class Person(BaseModel):
    name : str
    age : int
    city : str

parser = PydanticOutputParser(pydantic_object = Person)

model = ChatOpenAI(model = 'gpt-5')
template = PromptTemplate(
    template = '''Give me the name age and city of any {movie} character \n{format_instruction}''',
    input_variables = ['movie'],
    partial_variables = {"format_instruction" : parser.get_format_instructions()}
)
prompt = template.invoke({"movie" : "Avengers"})
response = model.invoke(prompt)
print(response.content)