from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
import operator
from langgraph.graph import StateGraph , START, END


llm = ChatOpenAI(
    model="gpt-4.1-mini",  # Your Azure deployment name
    base_url="https://openai-rg-nadeem.openai.azure.com/openai/v1",

    )


class State(TypedDict):
    question: str
    answer: str
    explanation: str
    history: Annotated[list[str], operator.add]


def chat_node(state: State) -> State:
   result = llm.invoke(state['question'])
   answer = result.content
   state['answer'] = answer
   return state

def expl_node(state: State) -> State:
    prompt = f"This is the question: {state['question']} and this is the answer {state['answer']}... you have to explain this"
    result = llm.invoke(prompt)
    state['explanation']= result.content
    return state


graph = StateGraph(State)


graph.add_node('chat_node', chat_node)
graph.add_node('expl_node', expl_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', 'expl_node')
graph.add_edge('expl_node', END)

workflow = graph.compile()

result = workflow.invoke({'question': "whats your name", 'history':['hi','hello']})
print(result)
