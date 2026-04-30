from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

def get_memory_chain():
    """Returns the memory-enabled chain"""
    
    # Prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])

    # LLM
    llm = ChatOllama(
        model="mistral:7b",
        temperature=0.7
    )

    # Output parser
    output_parser = StrOutputParser()

    # Session store
    store = {}
    
    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    # Build chain
    lcel_chain = prompt | llm | output_parser
    
    memory_chain = RunnableWithMessageHistory(
        lcel_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history"
    )
    
    return memory_chain

# ❌ Comment out testing code
# response = memory_chain.invoke(...)
# print(response)