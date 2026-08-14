from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.1
)

messages = [
        SystemMessage(content="Você é um assistente útil que responde ao usuário com detalhes e exemplos.")
]

while True:
    text = input("Entrada Usuário (digite 'q' para parar.): ")
    
    if text.lower() == "q":
        break

    messages.append(HumanMessage(content=text))

    result = model.invoke(messages)
    response = result.content
    messages.append(AIMessage(content=response))

    print(f"AI Response: {response}")

print("------------------------------")
print(messages)
