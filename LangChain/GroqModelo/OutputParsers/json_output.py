from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
)

parser = JsonOutputParser()

prompt_template = ChatPromptTemplate([("system",
                                       "Se a pergunta do usuário for relacionado ao setor financeiro, a escolha \
                                       deve ser 1, caso contrário a escolha pode ser qualquer numero diferente de \
                                       1. \n{format_instructions}\n Pergunta Usuário: {pergunta_user}")],
                                     partial_variables={"format_instructions": parser.get_format_instructions()})

chain = prompt_template | model | parser

output = chain.invoke({"pergunta_user": "Me diga quanto está o dollar."})

print("--"*50)
#print(type(output))
print("--"*50)
print(output)
print("--"*50)
