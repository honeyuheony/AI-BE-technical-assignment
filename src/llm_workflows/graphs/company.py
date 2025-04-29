from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.types import Send

from src.llm_workflows.nodes.company.infer_tag import infer_tag
from src.llm_workflows.nodes.company.retriever import retrieve_documents
from src.llm_workflows.states.company import CompanyTagState, PositionState


def create_position_graph():
    """단일 position 처리를 위한 그래프"""
    workflow = StateGraph(PositionState)

    workflow.add_node("retrieve", retrieve_documents)
    workflow.add_node("infer", infer_tag)

    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "infer")
    workflow.add_edge("infer", END)

    return workflow.compile()


def map_positions(state: CompanyTagState):
    """병렬 처리를 위한 노드 맵핑"""
    return [
        Send("process_position", PositionState(position=position, documents=[], output_tag=[])) for position in state.positions
    ]


def process_position_results(position_state: PositionState):
    """단일 position 결과를 메인 상태에 통합"""
    return {"documents": [position_state.documents], "output_tag": [position_state.output_tag]}


def create_company_tag_graph() -> CompiledStateGraph:
    """회사 경험 태그 추론 그래프"""
    workflow = StateGraph(CompanyTagState)

    position_graph = create_position_graph()
    workflow.add_node("process_position", position_graph)

    workflow.add_conditional_edges(START, map_positions, ["process_position"])

    workflow.add_edge("process_position", END)

    return workflow.compile()
