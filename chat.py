import openai
from llama_index import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.llms import OpenAI
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.query_engine import SubQuestionQueryEngine
from llama_index import StorageContext, load_index_from_storage

from halo import Halo

if __name__ == '__main__':

    # Chat GPT Init 
    openai.api_key = "copy-and-paste-your-openai-api-key-here"
    llm = OpenAI(temperature=0, model="gpt-3.5-turbo", max_tokens=-1)
    service_context = ServiceContext.from_defaults(llm=llm)

    # Setup both indices by loading from the saved DBs that were created by embed.py
    alice_storage_context = StorageContext.from_defaults(persist_dir="alice_docs.DB")
    alice_index = load_index_from_storage(alice_storage_context)
    glass_storage_context = StorageContext.from_defaults(persist_dir="glass_docs.DB")
    glass_index = load_index_from_storage(glass_storage_context)

    # Setup query engine for both
    alice_engine = alice_index.as_query_engine(similarity_top_k=2)
    glass_engine = glass_index.as_query_engine(similarity_top_k=2)

    # ask user for question 
    print('\n\nWhat do you want to know about the 2 documents. Type QUIT when done.')

    # Set up the QueryEngineTool to use both engines for comparisons
    query_engine_tools = [
        QueryEngineTool(
            query_engine=alice_engine,
            metadata=ToolMetadata(
                name="alice_PDF",
                description="Provides information about Alice In Wonderland",
            ),
        ),
        QueryEngineTool(
            query_engine=glass_engine,
            metadata=ToolMetadata(
                name="glass_PDF",
                description="Provides information about Alice Through The looking Glass",
            ),
        ),
    ]
    s_engine = SubQuestionQueryEngine.from_defaults(query_engine_tools=query_engine_tools)

    ## Main Loop
    while True:
        # Get user input
        text = input('\n\nUSER: ').strip()

        # Break out of loop of asking questions when user types "QUIT" in capital letters
        if text == 'QUIT':
            break

        spinner = Halo(text='\nThinking...\n', spinner='dots')
        spinner.start()

        # Get response and print it before asking next question
        response = s_engine.query(text)
        print('\n\n' + str(response))

        spinner.stop()



