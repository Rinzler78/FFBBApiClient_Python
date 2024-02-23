from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_none, from_str, from_union


@dataclass
class ResourceID:
    kind: Optional[str] = None
    video_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "ResourceID":
        assert isinstance(obj, dict)
        kind = from_union([from_str, from_none], obj.get("kind"))
        video_id = from_union([from_str, from_none], obj.get("videoId"))
        return ResourceID(kind, video_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.kind is not None:
            result["kind"] = from_union([from_str, from_none], self.kind)
        if self.video_id is not None:
            result["videoId"] = from_union([from_str, from_none], self.video_id)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ResourceID):
            return False
        return self.kind == other.kind and self.video_id == other.video_id

    def __hash__(self) -> int:
        return hash((self.kind, self.video_id))
