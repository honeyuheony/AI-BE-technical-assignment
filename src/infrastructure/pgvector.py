from langchain_postgres import PGEngine, PGVectorStore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PGVectorStoreImpl:
    def __init__(self, connection_string: str, table_name: str, vector_size: int, embedding):
        # SQLAlchemy 엔진(커넥션 풀) 생성
        self.engine = create_engine(connection_string, pool_size=5, max_overflow=10)
        self.Session = sessionmaker(bind=self.engine)
        # PGEngine 및 테이블 초기화
        pg_engine = PGEngine.from_connection_string(url=connection_string)
        # 테이블이 없으면 생성 (마이그레이션 예제 참고)
        pg_engine.init_vectorstore_table(table_name=table_name, vector_size=vector_size)
        # 최신 방식의 PGVectorStore 생성
        self.store = PGVectorStore.create_sync(
            engine=pg_engine,
            table_name=table_name,
            embedding_service=embedding,
        )

    def similarity_search(self, query: str):
        # 필요시 세션 사용 가능: with self.Session() as session:
        with self.Session() as session:
            return self.store.similarity_search(query)
