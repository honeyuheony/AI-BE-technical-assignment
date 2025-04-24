from dependency_injector import containers, providers
from langchain_openai import OpenAIEmbeddings

from src.infrastructure.pgvector import PGVectorStoreImpl


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_env(".env")
    openai_small_embedding = providers.Singleton(
        OpenAIEmbeddings, api_key=config.openai.api_key, model="text-embedding-3-small", dimension=1536
    )
    CONNECTION_STRING = (
        f"postgresql+asyncpg://{config.pgvector.user}:{config.pgvector.password}@{config.pgvector.host}"
        f":{config.pgvector.port}/{config.pgvector.name}"
    )

    vector_store_openai = providers.Singleton(
        PGVectorStoreImpl,
        connection_string=CONNECTION_STRING,
        table_name="openai_vectors",
        vector_size=1536,
        embedding=openai_small_embedding,
    )

    # 필요에 따라 더 추가
