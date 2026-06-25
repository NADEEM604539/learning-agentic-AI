from hugging_face import chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
you are a good boy your name is {name}
"""
)

prompt = template.invoke({"ali"})
print(prompt)
# response = chat_model.invoke()

# print(response.content)


    
