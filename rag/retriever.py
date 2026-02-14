from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()


# Load vectorstore once
vectorstore = PineconeVectorStore.from_existing_index(
    index_name="security-policy-index",
    embedding=OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])
)

def retrieve_query(query, k=5):
    results = vectorstore.similarity_search_with_score(query, k=k)
    return results
