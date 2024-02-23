from dataclasses import dataclass
from typing import Any, List, Optional

from .converters import from_list, from_none, from_str, from_union, to_class


@dataclass
class Competition:
    name: Optional[str] = None
    id: Optional[str] = None
    group_field: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Competition":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("id"))
        group_field = from_union([from_str, from_none], obj.get("groupField"))
        return Competition(name, id, group_field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.group_field is not None:
            result["groupField"] = from_union([from_str, from_none], self.group_field)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Competition):
            return False
        return (
            self.name == other.name
            and self.id == other.id
            and self.group_field == other.group_field
        )

    def __hash__(self) -> int:
        return hash((self.name, self.id, self.group_field))


def competition_from_dict(s: Any) -> List[Competition]:
    return from_list(Competition.from_dict, s)


def competition_to_dict(x: List[Competition]) -> Any:
    return from_list(lambda x: to_class(Competition, x), x)
