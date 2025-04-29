import json

from dependency_injector.wiring import Provide, inject
from langchain_core.documents import Document

from containers import Container
from src.llm_workflows.states.company import PositionState


def retrieve_documents(state: PositionState) -> PositionState:
    # 여기서 retriever를 사용하여 문서 검색
    position = state.position
    documents = get_documents_from_vectorstore(json.dumps(position))

    state.documents = documents
    return state


@inject
def get_documents_from_vectorstore(
    query: str,
    vectorstore=Provide[Container.vector_store_openai],
) -> list[Document]:
    """벡터스토어에서 유사한 문서를 검색합니다."""
    return vectorstore.similarity_search(query)
