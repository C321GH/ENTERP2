from pydantic import BaseModel
from typing import Any, Dict, List
class IngestItem(BaseModel):
    id: str
    text: str
    metadata: Dict[str, Any] = {}
class IngestRequest(BaseModel):
    items: List[IngestItem]
    collection: str = "default"
    enrich: bool = True
