from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_int, from_none, from_union


@dataclass
class Day:
    name: Optional[int] = None
    desc: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "Day":
        assert isinstance(obj, dict)
        name = from_union([from_int, from_none], obj.get("name"))
        desc = from_union([from_int, from_none], obj.get("desc"))
        return Day(name, desc)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_int, from_none], self.name)
        if self.desc is not None:
            result["desc"] = from_union([from_int, from_none], self.desc)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Day):
            return False
        return self.name == other.name and self.desc == other.desc

    def __hash__(self) -> int:
        return hash((self.name, self.desc))
