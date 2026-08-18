from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import re

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
)

class AnaliseReview(BaseModel):
    sentimento: str = Field(description="Sentimento geral: 'positivo', 'negativo' ou 'neutro'")
    nota_estimada: int = Field(description="Nota de 1 a 5 baseada na satisfação do cliente")
    resumo: str = Field(description="Resumo da avaliação em uma única frase") 

parser = PydanticOutputParser(pydantic_object=AnaliseReview)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Você é um especialista em analisar avaliações de produtos. "
               "Analise o sentimento, estime uma nota de 1 a 5 e gere um resumo curto.\n\n"
               "{format_instructions}"),
    ("human", "{review}")
])

def preprocess_text(texto: str) -> str:
    
    if not isinstance(texto, str):
        raise TypeError("O texto deve ser uma string")

    if not texto:
        raise ValueError("O texto não pode estar vazio")
    
    texto = re.sub(r"\t", " ", texto)
    texto = "".join(c for c in texto if c.isprintable() or c == "\n")
    texto = re.sub(r" +", " ", texto)
    texto = re.sub(r"\n+", "\n", texto)
    texto = texto.strip()
    
    if not texto:
        raise ValueError("O texto não pode estar vazio após o processamento")
    
    return texto

def preprocess_review(data):
    return {"review": preprocess_text(data["review"]),
            "format_instructions": parser.get_format_instructions()}    

chain = RunnableLambda(preprocess_review) | prompt_template | model | parser

final_chain = RunnablePassthrough.assign(
    analise=chain
)
#response = final_chain.invoke({"review": "Produto excelente, chegou rápido e funciona perfeitamente!"})
"""response = final_chain.invoke({
    "review": "Comprei esse produto há duas semanas e já parou de funcionar. "
              "O material parece muito frágil, quebrou na primeira semana de uso normal. "
              "Pedi troca e o atendimento não respondeu até agora. Estou muito decepcionado, "
              "não recomendo a compra."
}) """

response = final_chain.invoke({
    "review": "O produto é razoável pelo preço. Funciona bem na maior parte do tempo, "
              "mas o acabamento poderia ser melhor. A entrega demorou um pouco mais "
              "do que eu esperava, mas chegou intacto. Não é excelente, mas também "
              "não é ruim, cumpre o que promete."
})

print(response)