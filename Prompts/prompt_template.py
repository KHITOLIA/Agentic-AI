from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import warnings
warnings.filterwarnings("ignore")

llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash", temperature = 0)

template = PromptTemplate(
    template = '''Please summarize the research paper titled {paper_name} with the following specifications \n
    Explaination Style {style_input}
    Explaination length {length_input}
    1. Mathematical details:
        -Include relveant maths equations if present in the paper
        -explain the mathematical concepts as well if present\n
    2. Analogies: 
     use relatable analogies to simplify the complex formulas or ideas from the paper
    if certain information is not available in the paper , respond with "Insufficient information"do not fumble the response''',
    input_variables = ['paper_name', 'style_input', 'length_input']
)

template.save("template.json")
# prompt = template.invoke({"paper_name" : "Attention is all you need", "style_input" : "Core maths and Code explaination", "length_input" : "Long"})
# response = llm.invoke(prompt).content[0]['text']
# print(response)

# d = {'a' : 1,'b' : 2}
# d['a']