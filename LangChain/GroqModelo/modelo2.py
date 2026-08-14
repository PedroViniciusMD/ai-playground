from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.1
)

messages = [ #simulating an interaction
			 SystemMessage(content="Você é um especialista em astrofísica."),
			 HumanMessage(content="Qual a distancia do sol até a terra?"),
			 AIMessage(content="O Sol está a 49.600.000 km de distância da Terra."),
			 HumanMessage(content="E a distância da terra até marte?"),
]

# messages = [
# 			 ("system", "Você é um especialista em astrofísica."),
# 			 ("user", "Qual a distancia do sol até a terra?"),
# 			 ("assistant", "O Sol está a 49.600.000 km de distância da Terra."),
#            ("user", "E a distância da terra até marte?"),
# ]

result = model.invoke(messages)

print("-------------------------------------")
print(result)
print("-------------------------------------")

print(result.content)
print("-------------------------------------")
