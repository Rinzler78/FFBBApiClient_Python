from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Optional

from .converters import from_list, from_none, from_str, from_union, to_class


class CompetitionType(Enum):
    CHAMPIONSHIP = "championship"
    CUP = "cup"


@dataclass
class Championship:
    name: Optional[str] = None
    id: Optional[str] = None
    type: Optional[CompetitionType] = None

    @staticmethod
    def from_dict(obj: Any) -> "Championship":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("id"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Championship(name, id, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Championship):
            return False
        return (
            self.name == other.name and self.id == other.id and self.type == other.type
        )

    def __hash__(self) -> int:
        return hash((self.name, self.id, self.type))


def championship_from_dict(s: Any) -> List[Championship]:
    return from_list(Championship.from_dict, s)


def championship_to_dict(x: List[Championship]) -> Any:
    return from_list(lambda x: to_class(Championship, x), x)
