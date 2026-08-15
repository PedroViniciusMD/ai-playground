from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage


print("=========== Example 1 =========")
prompt_template = PromptTemplate.from_template("Gere para mim um poema sobre: {assunto}. Escreva em {lingua}")
rt = prompt_template.invoke({"assunto": "navegação", "lingua":"pt-br"})

print(rt)

print("=========== Example 2 =========")

prompt_template = ChatPromptTemplate(
    ["Gere para mim um poema sobre: {assunto}. Escreva em {lingua}"
     ]
)

rt = prompt_template.invoke({"assunto": "navegação", "lingua":"pt-br"})
print(rt)

#prompt_template = ChatPromptTemplate(
#    [
#        HumanMessagePromptTemplate.from_template("Gere para mim um poema sobre: {assunto}. Escreva em {lingua}")
#    ]
#)

#rt = prompt_template.invoke({"assunto": "navegação", "lingua":"pt-br"})
#print(rt)

#prompt_template = ChatPromptTemplate(
#    [
#        ("user", "Gere para mim um poema sobre: {assunto}. Escreva em {lingua}")
#     ])

#rt = prompt_template.invoke({"assunto": "navegação", "lingua":"pt-br"})
#print(rt)

print("=========== Example 3 =========")

prompt_template = ChatPromptTemplate([
									  ("system", "Você é um assistente de IA com habilidade de escritor de poesia."),
									  ("user", "Gere para mim um poema sobre: {assunto}. Escreva em {lingua}")
])

rt = prompt_template.invoke({"assunto": "navegação", "lingua":"pt-br"})
print(rt)

#prompt_template = ChatPromptTemplate([
#    ("system", "Você é um assistente de IA com habilidade de escritor de poesia."),
#	MessagesPlaceholder("msgs_user")
#]
#)

#rt = prompt_template.invoke(
#    {"msgs_user": [HumanMessage(content="Gere para mim um poema sobre: navegação. Escreva em pt-br")]
#     })
#print(rt)