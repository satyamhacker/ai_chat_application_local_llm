# core_engine.py
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv

# Initialize Ollama client (make sure `ollama serve` is running in background)
load_dotenv()


llm = ChatOllama(
    model="mistral:7b",   # or any model you pulled with `ollama pull`
    temperature=0.7
)

# Simple synchronous call
response = llm.invoke("how are you in 10 words")
print(response.content)

# Streaming (token-by-token)
for chunk in llm.stream("i think you are good tell in 6 words"):
    print(chunk.content, end="", flush=True)
