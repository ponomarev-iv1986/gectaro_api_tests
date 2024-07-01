from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ResourceRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    id_: int = Field(alias="id")
    project_tasks_resource_id: int
    volume: float
    cost: float
    batch_number: Optional[int]
    batch_parent_request_id: Optional[int]
    is_over_budget: bool
    created_at: int
    updated_at: int
    user_id: int
    needed_at: int
    created_by: int


class ListResourceRequest(BaseModel):
    resource_requests: list[ResourceRequest]
