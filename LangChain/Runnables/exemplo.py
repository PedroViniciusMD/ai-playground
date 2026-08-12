from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel

element1 = RunnablePassthrough()

def char_count(entrada: dict) -> int:
    return len(entrada["input"])

convert_func = RunnableLambda(char_count)

element2 = RunnablePassthrough.assign(num_caract=convert_func)

def congrats(entrada: dict) -> str:
    result = entrada["input"] + " Congrats!!"
    return result

congrats_transforms = RunnableLambda(congrats)
congrats_passthrough = RunnablePassthrough()

element3 = RunnableParallel({
    "congrats_transforms": congrats_transforms,
    "congrats_passthrough": congrats_passthrough
}
)

element4 = RunnablePassthrough()

# complete chain
chain = element1 | element2 | element3 | element4

# invoking
final = chain.invoke({"input": "LangChain"})

print("--------------------------------------------------")
print(final)
print("--------------------------------------------------")
