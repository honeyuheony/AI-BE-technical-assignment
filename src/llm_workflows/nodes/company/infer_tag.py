from src.llm_workflows.states.company import PositionState


def infer_tag(state: PositionState) -> PositionState:
    # LLM을 사용하여 태그 추론
    position = state.position
    documents = state.documents

    # llm 호출 예시
    # tag = llm.predict(documents=documents, position=position)
    tag = f"추론된 태그: {position['company']}"  # 예시

    return PositionState(position=position, documents=documents, output_tag=tag)
