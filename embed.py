import openai
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms import OpenAI
from llama_index import StorageContext

# Chat GPT Init 
openai.api_key = "copy-and-paste-your-openai-api-key-here"

# load the docs
alice_docs = SimpleDirectoryReader(input_files=["alice.pdf"]).load_data()
glass_docs = SimpleDirectoryReader(input_files=["glass.pdf"]).load_data()

# Save them to disk as vector DBs
alice_index = VectorStoreIndex.from_documents(alice_docs)
alice_index.storage_context.persist("alice_docs.DB")

glass_index = VectorStoreIndex.from_documents(glass_docs)
glass_index.storage_context.persist("glass_docs.DB")



