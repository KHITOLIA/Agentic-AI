from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_classic.prompts import ChatPromptTemplate

model = ChatOpenAI(model = 'gpt-5', temperature=0)

chat_template = ChatPromptTemplate([
    ('system', 'You are a {domain} expert'),
    ('human', 'Explain in simple terms what is {topic}')
])

# prompt = chat_template.invoke({"domain":"Maths", "topic" : "Coordinate system"})
# response = model.invoke(prompt).content
# chat_template.save('template1.json')
# print(response)

import json

from langchain_core.load import dumpd
prompt = dumpd(chat_template)
with open("chat_template.json", "w") as f:
    json.dump(prompt, f)