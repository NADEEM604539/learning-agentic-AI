# from typing import Optional, List, Literal, TypedDict , Dict
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
# from langchain_core.runnables import RunnableSequence , RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch
import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field
from langchain.messages import ToolMessage, HumanMessage

class Sch(BaseModel):
    A : int= Field(description="first value for addition")
    b : int= Field(description="2nd value for addition")

def add(A: int, b:int) -> int:
    """Adding two integers"""
    return A+b

toool = StructuredTool.from_function(
    func=add,
    name="add",
    description="ADDING TWO INTEGERS",
    args_schema=Sch
)

# print(toool.invoke({'A':6, 'b':8}))

@tool
def multiply(a:int,b:int):
    """Multiply"""
    return a*b

@tool
def div(a:int,b:int):
    """div"""
    return a/b

tools=[
    div,
    multiply
]

class toolkit:
    def get_tools(self):
        return[
            div,
            multiply
        ]

llm = ChatOpenAI(
    model="gpt-4.1-mini",  # Your Azure deployment name
    base_url="https://openai-rg-nadeem.openai.azure.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
    )

llm_with_tools = llm.bind_tools(tools)
messages=[]

promp='TELL ME IF WE MULTIPLY 5 INTO 8 WHAT WE GET'
messages.append(HumanMessage(promp))
results= llm_with_tools.invoke(promp)
print(results)
tool_mess = ToolMessage(
    content=results.tool_calls,
    tool_call_id= results.id
)
messages.append(tool_mess)
tool_calls = results.tool_calls
tool_map = {tool.name: tool for tool in tools}

for tool_call in tool_calls:
    tool_name = tool_call["name"]
    if tool_name in tool_map:
        print(tool_map[tool_name].invoke(tool_call["args"]))

final = llm.invoke(f"tell me what happend above from these messages: {messages}")
print("------------------------------------------")
print(final.content)
print("------------------------------------------")