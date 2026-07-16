from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
import operator
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
import os 

llm = ChatOpenAI(
    model="gpt-4.1-mini",  # Your Azure deployment name
    base_url="https://openai-rg-nadeem.openai.azure.com/openai/v1",
    #add your api key below
    api_key= os.getenv("api_key") or os.getenv("OPENAI_API_KEY")
)

class State(TypedDict):
    human: str
    ai: str
    history: Annotated[list[BaseMessage], operator.add]

def chat_node(state: State):

    prompt = f"you have all the history as {state['history']} and you have to answer the question: {state['human']}"
    result = llm.invoke(prompt)
    answer = result.content
    print("AI:", answer)
    
    return {
        "ai":answer,
        "history": [
        HumanMessage(content=state["human"]),
        AIMessage(content=answer)
    ] }


graph = StateGraph(State)
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

memory = MemorySaver()

workflow = graph.compile(
    checkpointer= memory
)

config = {
    "configurable": {
        "thread_id": "nadeem"
    }
}

while True:
    question = str(input('YOU:'))
    if question == "end":
        break
    initial_state = {
        "human": question,
        "history":[]
    }
    workflow.invoke(initial_state,
                    config=config)



    