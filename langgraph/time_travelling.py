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
    # api_key=
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

def router(state: State):
      if state['human'] == "end":
        return "print_history"
      return "chat_node"
     
graph = StateGraph(State)
graph.add_node('chat_node', chat_node)
graph.add_node('print_history', print_history)
graph.add_conditional_edges(START, router,
                            {
                                "chat_node": "chat_node",
                                "print_history": "print_history"
                            })
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
    if question == "end":
        break
    initial_state = {
        "human": question,
        "history":[]
    }
    workflow.invoke(initial_state,
                    config=config)

workflow.get_state({"configurable": {"thread_id": "nadeem", 'checkpoint_id': '1f17f547-e97a-652d-8004-5b631957a489'}})
# StateSnapshot(values={'human': 'kaha se ho', 'ai': 'Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?', 'history': [HumanMessage(content='kia nam hai tumhara', additional_kwargs={}, response_metadata={}), AIMessage(content='Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]), HumanMessage(content='kaha se ho', additional_kwargs={}, response_metadata={}), AIMessage(content='Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}, next=(), config={'configurable': {'thread_id': 'nadeem', 'checkpoint_id': '1f17f547-e97a-652d-8004-5b631957a489'}}, metadata={'source': 'loop', 'step': 4, 'parents': {}}, created_at='2026-07-14T07:20:30.304360+00:00', parent_config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-ae2a-64aa-8003-7410702c1f82'}}, tasks=(), interrupts=())

workflow.invoke(None, config =  {"configurable": {"thread_id": "nadeem", 'checkpoint_id': '1f17f547-e97a-652d-8004-5b631957a489'}})
# {'human': 'kaha se ho',
#  'ai': 'Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?',
#  'history': [HumanMessage(content='kia nam hai tumhara', additional_kwargs={}, response_metadata={}),
#   AIMessage(content='Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#   HumanMessage(content='kaha se ho', additional_kwargs={}, response_metadata={}),
#   AIMessage(content='Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}

history = list(workflow.get_state_history({"configurable":{"thread_id": "nadeem"}}))
print(history)
# [StateSnapshot(values={'human': 'kaha se ho', 'ai': 'Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?', 'history': [HumanMessage(content='kia nam hai tumhara', additional_kwargs={}, response_metadata={}), AIMessage(content='Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]), HumanMessage(content='kaha se ho', additional_kwargs={}, response_metadata={}), AIMessage(content='Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}, next=(), config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-e97a-652d-8004-5b631957a489'}}, metadata={'source': 'loop', 'step': 4, 'parents': {}}, created_at='2026-07-14T07:20:30.304360+00:00', parent_config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-ae2a-64aa-8003-7410702c1f82'}}, tasks=(), interrupts=()), StateSnapshot(values={'human': 'kaha se ho', 'ai': 'Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', 'history': [HumanMessage(content='kia nam hai tumhara', additional_kwargs={}, response_metadata={}), AIMessage(content='Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}, next=('chat_node',), config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-ae2a-64aa-8003-7410702c1f82'}}, metadata={'source': 'loop', 'step': 3, 'parents': {}}, created_at='2026-07-14T07:20:24.084986+00:00', parent_config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-ae27-637b-8002-2788e1a055a7'}}, tasks=(PregelTask(id='8eed1e6d-92ec-5096-e52d-753048d306c7', name='chat_node', path=('__pregel_pull', 'chat_node'), error=None, interrupts=(), state=None, result={'ai': 'Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?', 'history': [HumanMessage(content='kaha se ho', additional_kwargs={}, response_metadata={}), AIMessage(content='Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}),), interrupts=()), StateSnapshot(values={'human': 'kia nam hai tumhara', 'ai': 'Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', 'history': [HumanMessage(content='kia nam hai tumhara', additional_kwargs={}, response_metadata={}), AIMessage(content='Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}, next=('__start__',), config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-ae27-637b-8002-2788e1a055a7'}}, metadata={'source': 'input', 'step': 2, 'parents': {}}, created_at='2026-07-14T07:20:24.083723+00:00', parent_config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-8d5d-6f5a-8001-2c196ba81a50'}}, tasks=(PregelTask(id='8b8dc988-69c3-1974-13e3-945766202bde', name='__start__', path=('__pregel_pull', '__start__'), error=None, interrupts=(), state=None, result={'human': 'kaha se ho', 'history': []}),), interrupts=()), StateSnapshot(values={'human': 'kia nam hai tumhara', 'ai': 'Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', 'history': [HumanMessage(content='kia nam hai tumhara', additional_kwargs={}, response_metadata={}), AIMessage(content='Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}, next=(), config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-8d5d-6f5a-8001-2c196ba81a50'}}, metadata={'source': 'loop', 'step': 1, 'parents': {}}, created_at='2026-07-14T07:20:20.645841+00:00', parent_config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-5543-67f0-8000-3164e6bdf2a6'}}, tasks=(), interrupts=()), StateSnapshot(values={'human': 'kia nam hai tumhara', 'history': []}, next=('chat_node',), config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-5543-67f0-8000-3164e6bdf2a6'}}, metadata={'source': 'loop', 'step': 0, 'parents': {}}, created_at='2026-07-14T07:20:14.762978+00:00', parent_config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-553b-64c5-bfff-2403e90726f4'}}, tasks=(PregelTask(id='270f5e9c-69b5-f03c-23a6-47540ba7588a', name='chat_node', path=('__pregel_pull', 'chat_node'), error=None, interrupts=(), state=None, result={'ai': 'Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', 'history': [HumanMessage(content='kia nam hai tumhara', additional_kwargs={}, response_metadata={}), AIMessage(content='Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}),), interrupts=()), StateSnapshot(values={'history': []}, next=('__start__',), config={'configurable': {'thread_id': 'nadeem', 'checkpoint_ns': '', 'checkpoint_id': '1f17f547-553b-64c5-bfff-2403e90726f4'}}, metadata={'source': 'input', 'step': -1, 'parents': {}}, created_at='2026-07-14T07:20:14.759627+00:00', parent_config=None, tasks=(PregelTask(id='0fb5ff8f-9b75-04a8-7c53-b99753066f48', name='__start__', path=('__pregel_pull', '__start__'), error=None, interrupts=(), state=None, result={'human': 'kia nam hai tumhara', 'history': []}),), interrupts=())]

workflow.update_state({"configurable":{
    "thread_id":"nadeem",
    'checkpoint_id': '1f17f547-e97a-652d-8004-5b631957a489',
    'checkpoint_ns': ''
}},{"human":"tumhay pta mei kon hu"})
# {'configurable': {'thread_id': 'nadeem',
#   'checkpoint_ns': '',
#   'checkpoint_id': '1f17f571-a4a9-6893-8005-cf6b2bdff77c'}}

workflow.invoke(None, config =  {"configurable": {"thread_id": "nadeem", 'checkpoint_id': '1f17f571-a4a9-6893-8005-cf6b2bdff77c'}})
# {'human': 'tumhay pta mei kon hu',
#  'ai': 'Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?',
#  'history': [HumanMessage(content='kia nam hai tumhara', additional_kwargs={}, response_metadata={}),
#   AIMessage(content='Mera naam ChatGPT hai. Aap se milkar khushi hui! Aapka naam kya hai?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#   HumanMessage(content='kaha se ho', additional_kwargs={}, response_metadata={}),
#   AIMessage(content='Main ek AI hoon, isliye mera koi physical sthaan nahi hai. Lekin main yahan aapki madad ke liye hoon! Aap kaha se hain?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]}
