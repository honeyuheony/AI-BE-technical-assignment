import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGEngine, PGVectorStore

load_dotenv()

CONNECTION_STRING = (
    f"postgresql+asyncpg://{os.getenv('PGVECTOR_USER')}:{os.getenv('PGVECTOR_PASSWORD')}@{os.getenv('PGVECTOR_HOST')}"
    f":{os.getenv('PGVECTOR_PORT')}/{os.getenv('PGVECTOR_NAME')}"
)
print(CONNECTION_STRING)

def get_vectorstore(table_name: str):
    openai_small_embedding = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    engine = PGEngine.from_connection_string(url=CONNECTION_STRING)

    vectorstore = PGVectorStore.create_sync(
        engine=engine,
        table_name=table_name,
        embedding_service=openai_small_embedding
    )

    return vectorstore


