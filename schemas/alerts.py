from pydantic import BaseModel
from typing import Any, Dict
class AlertCreate(BaseModel):
    name: str
    rule: Dict[str, Any]
