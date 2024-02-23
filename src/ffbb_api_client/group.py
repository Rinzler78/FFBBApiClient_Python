from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_none, from_str, from_union


@dataclass
class Group:
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Group":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Group(id, name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Group):
            return False
        return (
            self.id == other.id and self.name == other.name and self.type == other.type
        )

    def __hash__(self) -> int:
        return hash((self.id, self.name, self.type))
