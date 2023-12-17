from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
import os
from langchain.schema import (
    HumanMessage
)

model_name = "gpt-3.5-turbo-0301"
os.environ["OPENAI_API_KEY"] = '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'

# llm = OpenAI(model_name=model_name, temperature=0)
chat_model = ChatOpenAI(model_name=model_name, temperature=0)

# llm.predict("hi!")

resp = chat_model([HumanMessage(content="question")])
answer = resp.content
print(answer)
