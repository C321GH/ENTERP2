from pydantic import BaseModel
from typing import Dict, Any
class EntityUpsert(BaseModel):
    name: str
    meta: Dict[str, Any] = {}
