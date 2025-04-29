import json

from langchain_core.documents import Document

from src.infrastructure.pgvector import get_vectorstore
from src.llm_workflows.states.company import PositionState


def retrieve_documents(state: PositionState) -> PositionState:
    # 여기서 retriever를 사용하여 문서 검색
    position = state.position
    vectorstore = get_vectorstore(table_name="company")
    documents = vectorstore.similarity_search(json.dumps(position))
    
    state.documents = documents
    return state