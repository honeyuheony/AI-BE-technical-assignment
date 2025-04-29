from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph


def infer_experience_and_skills_graph() -> CompiledStateGraph:
    """Json 데이터로부터 경험 및 기술과 관련된 태그를 생성하는 워크플로우"""
    workflow = StateGraph(InferExperienceAndSkillsState)

    # add nodes
    ...
    workflow.add_node("대학교 태그 추론", ...)
    workflow.add_node("회사 경험 관련 쿼리 생성", ...)
    workflow.add_node("회사 경험 벡터DB 검색", ...)
    workflow.add_node("개인 경험 관련 쿼리 생성", ...)
    workflow.add_node("개인 경험 벡터DB 검색", ...)
    workflow.add_node("회사 경험 태그 추론", ...)
    workflow.add_node("개인 경험 태그 추론", ...)

    # add edges
    ...

    return workflow.compile()


def infer_education_tag_graph() -> CompiledStateGraph:
    """대학교 태그 추론 워크플로우"""
    workflow = StateGraph(InferEducationTagState)
    # add nodes
    workflow.add_node("대학교 태그 추론", ...)
    # add edges
    ...

    return workflow.compile()


def infer_skills_tag_graph() -> CompiledStateGraph: ...
