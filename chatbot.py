from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage
load_dotenv()
model = ChatMistralAI(model="mistral-small-latest" , temperature = 0.9)

print("According to your mood make a choice from below")
print("choose 1 if want me to be funny\nchoose 2 if your mood is sad\nchoose 3 if your mood is angry")
choice = int(input("make a choice : "))
if choice == 1:
    print("------------I am funny chatbot now-----------------")
    mode = "you are an funny ai bot for every input of user make a funny way response to it"
elif choice == 2:
    print("------------I am sad chatbot now-----------------")
    mode = "you are an sad ai bot for every prompt the user gives reply with some sad response"
elif choice ==3:
    print("------------I am angry chatbot now-----------------")
    mode = "you are an angry ai bot for every prompt the user gives reply with sfull furious and angry response"
messeges: list[BaseMessage]= [
    SystemMessage(content=mode)
]

while True:
    prompt = input("User:  ")
    
    if  prompt== '0':
        break
    messeges.append(HumanMessage(content=prompt))
    response = model.invoke(messeges)
    messeges.append(AIMessage(content=response.content))
    print("BOT : ",response.content)
print(messeges)