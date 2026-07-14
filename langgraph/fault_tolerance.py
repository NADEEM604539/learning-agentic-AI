from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
import operator
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
import time

llm = ChatOpenAI(
    model="gpt-4.1-mini",  # Your Azure deployment name
    base_url="https://openai-rg-nadeem.openai.azure.com/openai/v1",
    #add your api key below
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
    time.sleep(4)
    
    return {
        "ai":answer,
        "history": [
        HumanMessage(content=state["human"]),
        AIMessage(content=answer)
    ] }

def print_history(state: State):
    print(state['history'])
    return {}
     
graph = StateGraph(State)
graph.add_node('chat_node', chat_node)
graph.add_node('print_history', print_history)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', 'print_history')
graph.add_edge('print_history', END)
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
    if question =="end":
        initial_state = {
        "human": question,
        "history":[]
            }
        workflow.invoke(initial_state,
                    config=config)
        break
    initial_state = {
        "human": question,
        "history":[]
    }
    workflow.invoke(initial_state,
                    config=config)
        
      


workflow.get_state({"configurable": {"thread_id": "nadeem"}})
history = list(workflow.get_state_history({"configurable":{"thread_id": "nadeem"}}))
print(history)
workflow.invoke(None, config =  {"configurable": {"thread_id": "nadeem"}})