from langchain_openai import ChatOpenAI

from src.llm_workflows.states.company import PositionState


def infer_tag(state: PositionState) -> PositionState:
    """LLM을 사용하여 태그 추론"""
    llm = ChatOpenAI(model="gpt-4.1-mini")
    prompt = PromptTemplate.from_template(
        """
        {documents}
        {position}
        """
    )

    tag = f"추론된 태그: {position['company']}"  # 예시
    
    return PositionState(
        position=position,
        documents=documents,
        output_tag=tag
    )
