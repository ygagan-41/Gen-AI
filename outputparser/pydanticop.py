from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b"
)

class person(BaseModel):
    name: str = Field(description="name of the person")
    age: int = Field(gt=18, description="age of the person")
    city: str = Field(description="name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

""" prompt = template.invoke({'place':'indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content) """

chain = template | model | parser

final_result = chain.invoke({'place':'American'})

print(final_result)