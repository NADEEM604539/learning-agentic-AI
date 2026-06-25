from hugging_face import chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

sys_message= SystemMessage("You are a good cook")

messages= [sys_message]
while True:
    user= input("How can i help you ")
    messages.append(HumanMessage(user))

    if user == "exit":
        break

    response = chat_model.invoke(messages)
    messages.append(AIMessage( response.content))
    print(response.content)

print(messages)

    
