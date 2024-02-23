from dataclasses import dataclass
from typing import Any, List, Optional

from .converters import from_list, from_none, from_str, from_union, to_class


@dataclass
class League:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "League":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return League(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, League):
            return False
        return self.id == other.id and self.name == other.name

    def __hash__(self) -> int:
        return hash((self.id, self.name))


def league_from_dict(s: Any) -> List[League]:
    return from_list(League.from_dict, s)


def league_to_dict(x: List[League]) -> Any:
    return from_list(lambda x: to_class(League, x), x)
