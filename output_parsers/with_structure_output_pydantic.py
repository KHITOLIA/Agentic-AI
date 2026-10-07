from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()

# review : sentiment, summary, pros, cons, name

class Review(BaseModel):
    sentiment : str =  Field(description = 'Give me the actuall sentiment of the given review provided')
    summary : str = Field(description = 'Describe the review into short summary')
    pros : str = Field(description = 'return all the pros mentioned in the review if present')
    cons : str = Field(description = 'return all the pros mentioned in the review if present')
    name : str = Field(description = 'Give me the name of the product in the review')

parser = PydanticOutputParser(pydantic_object=Review)

review_= '''I’m really impressed with the OnePlus N6. The Fresh Mint colour looks premium and stylish, and the phone feels solid and well-built in hand. The 120Hz display is smooth, and OxygenOS 16 makes the overall experience clean and responsive.


The biggest highlight for me is the 8000mAh battery — it easily handles heavy daily usage, and the 45W fast charging is also very convenient. The camera quality is good for everyday photos, especially in daylight.


The 128GB storage is more than enough for my regular apps, photos and videos. Overall, a great choice for anyone looking for excellent battery life, smooth performance and a premium-looking phone.


Definitely worth 5 stars! ⭐⭐⭐⭐⭐'''
model = ChatOpenAI(model = 'gpt-5').with_structured_output(Review)
response = model.invoke(review_)
print(response)