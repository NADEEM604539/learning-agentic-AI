from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    name: str
    age: int
    degree: str
    status: str


def name(state: State):
    print(state["name"])
    return {}


def adeel(state: State):
    print("Hello I am Adeel")
    return {
        "name": "Adeel is here"
    }


def nadeem(state: State):
    print("Hello I am Nadeem")
    return {
        "name": "Nadeem is here"
    }


def invalid(state: State):
    print("Invalid User")
    return {
        "status": "Invalid User"
    }


def router(state: State):

    if state["name"].lower() == "adeel":
        return "adeel"

    return "nadeem"


graph = StateGraph(State)

graph.add_node("name", name)
graph.add_node("adeel", adeel)
graph.add_node("nadeem", nadeem)
graph.add_node("invalid", invalid)

graph.add_edge(START, "name")

graph.add_conditional_edges(
    "name",
    router,
    {
        "adeel":"adeel",
        "nadeem":"nadeem"
    }
)

graph.add_edge("adeel", END)
graph.add_edge("nadeem", "invalid")
graph.add_edge("invalid", END)

workflow = graph.compile()

result = workflow.invoke(
    {
        "name": "nadeem",
        "age": 18,
        "degree": "BSCS14-C",
        "status": ""
    }
)

print(result)