from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
)

prompt_template = ChatPromptTemplate([("user", "Escreva um resumo em {lingua} sobre o tema: {assunto}")])

chain1 = prompt_template | model

reponse1 = chain1.invoke({"lingua": "pt-br", "assunto":"carros"})

#print(type(reponse1))
print("--"*50)
print(reponse1.content)
print("--"*50)

output_parser = StrOutputParser()

chain1_output_test = prompt_template | model | output_parser

response2 = chain1_output_test.invoke({"lingua": "pt-br", "assunto":"carros"})

#print(type(response2)) 
print("--"*50)
print(response2)
print("--"*50)
