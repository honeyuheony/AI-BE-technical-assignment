from typing import Annotated, List

from langchain_core.documents import Document
from langgraph.graph import add_messages
from pydantic import BaseModel, Field


class CompanyTagState(BaseModel):
    positions: Annotated[List[dict], Field(..., description="회사 경험 데이터 json 형식")]
    documents: Annotated[
        List[List[Document]], add_messages, Field(default_factory=List, description="회사 경험 태그 추론을 위한 검색된 문서 목록")
    ]
    output_tag: Annotated[List[str], add_messages, Field(default_factory=List, description="결과 태그 목록")]

# 단일 position 처리를 위한 상태
class PositionState(BaseModel):
    position: dict
    documents: Annotated[List[Document], add_messages, Field(default_factory=list)]
    output_tag: Annotated[List[str], add_messages, Field(default_factory=list)]