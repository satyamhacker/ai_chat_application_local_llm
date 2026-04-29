from dotenv import load_dotenv

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


# Load .env file
load_dotenv()

# Component 1: ChatPromptTemplate (system + human roles)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])



# Component 2: ChatOllama (LLM engine)
llm = ChatOllama(
    model="mistral:7b",
    temperature=0.7
)

# Component 3: StrOutputParser (output ko clean string mein convert karta hai)
output_parser = StrOutputParser()

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# 🔥 MEGAZORD ASSEMBLY (LCEL Chain)
lcel_chain = prompt | llm | output_parser  # Your existing chain from Step 1

memory_chain = RunnableWithMessageHistory(
    lcel_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

response = memory_chain.invoke(
    {"input": "explain yourself in 10 words"},
    config={"configurable": {"session_id": "teranaam_uuid_v4_123"}}
)
print(response)