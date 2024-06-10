
from promptflow import tool
from langchain.chains import LLMMathChain
from langchain_openai import OpenAI

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> str:
    llm = OpenAI(temperature=0)
    llm_math = LLMMathChain.from_llm(llm, verbose=True)

    llm_math.invoke("What is 13 raised to the .3432 power?")
