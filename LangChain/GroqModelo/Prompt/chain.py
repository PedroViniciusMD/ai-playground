from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

# ChatPromptTemplate
print("----------------------------------------")

prompt_template = ChatPromptTemplate([
    ("user", "Escreva um poema em {lingua} sobre o tema: {assunto}")
]
)

chain1 = prompt_template | model

response = chain1.invoke({"lingua": "pt-br", "assunto":"naves"})

print(response.content)


print("----------------------------------------")

messages = [
    ("system", "Você é um poeta brasileiro famoso e escreve poemas de no máximo {versos} versos."),
    ("human", "Escreva para mim um poema sobre {assunto}."),
]

prompt_template = ChatPromptTemplate(messages)

chain2 = prompt_template | model

response = chain2.invoke({"versos": "3", "assunto":"carros"})

print(response.content)
