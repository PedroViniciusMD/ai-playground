from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
)

class Route(BaseModel):
    escolha: int = Field(description="Rota escolhida")
    pensamento: str = Field(description="Campo para o pensamento que levou a decisão da rota escolhida")

parser = PydanticOutputParser(pydantic_object=Route)

prompt_template = ChatPromptTemplate([("system",
                                       "Se a pergunta do usuário for relacionado ao setor financeiro, \
                                       a escolha deve ser 1, caso contrário a escolha pode ser qualquer numero \
                                       diferente de 1. \n{format_instructions}\n Pergunta Usuário: {pergunta_user}")],
                                     partial_variables={"format_instructions": parser.get_format_instructions()})

chain = prompt_template | model | parser

output = chain.invoke({"pergunta_user": "Me diga sobre o clima"})

print("--"*50)
#print(type(output))
print("--"*50)
print(output)
print("--"*50)
print(f"Valor do parametro 'escolha': {output.escolha}")
#print(f"Valor do parametro 'pensamento': {output.pensamento}")
print("--"*50)
