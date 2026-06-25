import os

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Optional, List, Literal, TypedDict , Dict
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch


llm = ChatOpenAI(
    model="gpt-4.1-mini",  # Your Azure deployment name
    base_url="https://openai-rg-nadeem.openai.azure.com/openai/v1",
    api_key=os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
)

class Achobj(BaseModel):
    year: int = Field(description='tell me in which year he achieved')
    explanation: str = Field(description='tell me what he achieved')

class Schema(BaseModel):
    name: str
    education: Optional[List[str]]
    age: int =  Field(description="age should be greater than 50.", gt=50)

class Achievements(BaseModel):
    achievemets: List[Dict[str, Achobj]]

parser = PydanticOutputParser(pydantic_object=Schema)
Achievements_parser = PydanticOutputParser(pydantic_object=Achievements)

template = PromptTemplate(
    template="Tell me the about {poet} , his education along with his age when he died\n\n {format}",
    input_variables=['poet'],
    partial_variables={
        "format": parser.get_format_instructions()
    }
)
acheivemts_template = PromptTemplate(
    template="Tell me the about achievements of the {poet} year and explain it {format} ",
    input_variables=['poet'],
    partial_variables={
        "format": Achievements_parser.get_format_instructions()
    }
)

all_poets= []
branch = RunnableBranch(
    (lambda x : x['poet'] =='ALLAMA IQBAL', RunnableSequence(template, llm , parser)),
    (lambda x : x['poet'] =='GHALIB', RunnableSequence(acheivemts_template, llm, Achievements_parser)),
    RunnablePassthrough()
)
result = branch.invoke({'poet':'GHALIB'})
print(result)
print(dict(result))