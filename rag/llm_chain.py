from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.2
)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a security compliance assistant.

Rules:
- Answer ONLY from the context
- If information is missing, say "Insufficient evidence"
- Be concise and factual

Context:
{context}

Question:
{question}

Answer:
"""
)


chain = prompt | llm | StrOutputParser()
