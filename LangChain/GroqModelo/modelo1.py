from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.1
)

result = model.invoke(
    "O que você é capaz de fazer?"
)

print(result)
print()
print(result.content)
