from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

result = model.invoke(
    "Este é um teste. Se você recebeu a requisição, responda 'Teste OK'."
)

print(result.content)