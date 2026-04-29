from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env file
load_dotenv()

# Component 1: ChatPromptTemplate (system + human roles)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Respond clearly and concisely."),
    ("human", "{user_input}")
])



# Component 2: ChatOllama (LLM engine)
llm = ChatOllama(
    model="mistral:7b",
    temperature=0.7
)

# Component 3: StrOutputParser (output ko clean string mein convert karta hai)
output_parser = StrOutputParser()

# 🔥 MEGAZORD ASSEMBLY (LCEL Chain)
lcel_chain = prompt | llm | output_parser

# Test karo
response = lcel_chain.invoke({"user_input": "What is LCEL? give me in 10 words"})
print(response)