from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel

# RunnableLambda --------

def add_one(x: int) -> int:
    return x + 1

ex1 = RunnableLambda(add_one)

resposta = ex1.invoke(1)

print("------ RunnableLambda")
print(resposta)
print("-----------------------------------------------------------")

# RunnableSequence --------

def add_one(x: int) -> int:
    return x + 1

def mul_two(x: int) -> int:
    return x * 2

runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)

sequence = runnable_1 | runnable_2

resposta = sequence.invoke(1)

# print(runnable_1.invoke(1))
# print(runnable_2.invoke(1))

print("------ RunnableSequence")
print(resposta)
print("-----------------------------------------------------------")

# RunnableParallel --------


def add_one(x: int) -> int:
    return x + 1

def mul_two(x: int) -> int:
    return x * 2

def mul_three(x: int) -> int:
    return x * 3

runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)
runnable_3 = RunnableLambda(mul_three)

sequence = runnable_1 | {
    "mul_two": runnable_2,
    "mul_three": runnable_3,
}

# sequence = runnable_1 | RunnableParallel(
#     {"mul_two": runnable_2, "mul_three": runnable_3}
# )

# sequence = runnable_1 | RunnableParallel(
#     mul_two=runnable_2,
#     mul_three=runnable_3,
# )

resposta = sequence.invoke(1)

print("------ RunnableParallel")
print(resposta)
print("-----------------------------------------------------------")

# RunnablePassthrough

chain = RunnablePassthrough() | RunnablePassthrough() | RunnablePassthrough ()

resposta = chain.invoke("hello world")


print("------ RunnablePassthrough")
print(resposta)
print("-----------------------------------------------------------")

# RunnablePassthrough + RunnableLambda


def entrada_para_letras_maiusculas(entrada: str):
    saida = entrada.upper()
    return saida

chain = RunnablePassthrough() | RunnableLambda(entrada_para_letras_maiusculas) | RunnablePassthrough()

resposta = chain.invoke("hello world")


print("------ RunnablePassthrough + RunnableLambda")
print(resposta)
print("-----------------------------------------------------------------------------")


# Assign OP

runnable = RunnablePassthrough() | RunnablePassthrough.assign(multiplica_3=lambda x: x["num"] * 3)

resposta = runnable.invoke({"num": 1})

print("------ Operador Assign -----------------------")
print(resposta)
print("-----------------------------------------------------------------------------")
