from typing import Annotated

from langgraph.graph import add_messages
from pydantic import BaseModel, Field


class EducationTagState(BaseModel):
    input_context: Annotated[str, Field(..., description="대학교 태그 추론을 위한 컨텍스트")]
    output_tag: Annotated[list[str], add_messages, Field(default_factory=list, description="결과 태그")]
