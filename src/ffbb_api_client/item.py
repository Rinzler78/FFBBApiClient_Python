from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_none, from_str, from_union, to_class
from .snippet import Snippet


@dataclass
class Item:
    id: Optional[str] = None
    snippet: Optional[Snippet] = None

    @staticmethod
    def from_dict(obj: Any) -> "Item":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        snippet = from_union([Snippet.from_dict, from_none], obj.get("snippet"))
        return Item(id, snippet)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.snippet is not None:
            result["snippet"] = from_union(
                [lambda x: to_class(Snippet, x), from_none], self.snippet
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Item):
            return False
        return self.id == other.id and self.snippet == other.snippet

    def __hash__(self) -> int:
        return hash((self.id, self.snippet))
