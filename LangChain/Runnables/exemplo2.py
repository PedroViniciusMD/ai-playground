from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel


def sum_5 (num):
    return num + 5

def mult_10 (num):
    return num * 10

chain_1 = RunnableLambda(sum_5) | RunnableLambda(mult_10)
print(chain_1.invoke(3))

#----------------------------------------------------------

def name_upper (x):
    return x["name"].upper()

def name_len (x):
    return len(x["name"])

chain_2 = RunnableParallel (
    upper=RunnableLambda(name_upper),
    length=RunnableLambda(name_len))

print(chain_2.invoke({"name": "pedro"}))

#----------------------------------------------------------

chain_3 = RunnablePassthrough.assign(double=lambda x: x["num"] * 2)
print(chain_3.invoke({"num": 4}))

#----------------------------------------------------------
def split (string):
    return string.split()

def lower (string):
    return string.lower()

chain_4 = RunnableParallel(
    split=RunnableLambda(split),
    lower=RunnableLambda(lower)
)

print(chain_4.invoke("hello world!"))

#----------------------------------------------------------

def text_inverse (data):
    return data["text"][::-1]

def text_len (data):
    return len(data["text"])

def text_split(data):
    return data["text"].split()

chain_5 = RunnableParallel (
    inverse=RunnableLambda(text_inverse),
    len=RunnableLambda(text_len),
    split=RunnableLambda(text_split)
)

print(chain_5.invoke({"text": "LangChain is great"}))

#----------------------------------------------------------

def sum_dict (data):
    return data["a"] + data["b"]

chain_6 = RunnableParallel(
    original=RunnablePassthrough(),
    sum=RunnableLambda(sum_dict)
)

print(chain_6.invoke({"a": 2, "b": 3}))
