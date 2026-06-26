from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field



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

print(toool.invoke({'A':6, 'b':8}))


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

print(tools[0].invoke({'a':5, 'b':5}))