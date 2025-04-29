from typing import Annotated

from langchain_core.documents import Document
from langgraph.graph import add_messages
from pydantic import BaseModel, Field


class InferTagState(BaseModel):
    input_json: Annotated[dict, Field(..., description="회사, 재직기간, 직무(타이틀) 등의 인재 데이터 json 형식")]
    query: Annotated[str, Field("", description="경험 및 역량 추론을 위한 질문")]
    documents: Annotated[
        list[Document], add_messages, Field(default_factory=list, description="경험 및 역량 추론을 위한 검색된 문서 목록")
    ]
    context: Annotated[str, Field("", description="태그 추론을 위한 컨텍스트")]
    tags: Annotated[list[str], add_messages, Field(default_factory=list, description="결과 태그 목록")]
