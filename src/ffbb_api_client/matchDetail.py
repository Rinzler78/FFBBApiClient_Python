from dataclasses import dataclass
from typing import Any, List, Optional

from .converters import from_list, from_none, from_str, from_union, to_class


@dataclass
class MatchDetail:
    category: Optional[str] = None
    title: Optional[str] = None
    desc: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "MatchDetail":
        assert isinstance(obj, dict)
        category = from_union([from_str, from_none], obj.get("category"))
        title = from_union([from_str, from_none], obj.get("title"))
        desc = from_union([from_str, from_none], obj.get("desc"))
        return MatchDetail(category, title, desc)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.category is not None:
            result["category"] = from_union([from_str, from_none], self.category)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.desc is not None:
            result["desc"] = from_union([from_str, from_none], self.desc)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MatchDetail):
            return False
        return (
            self.category == other.category
            and self.title == other.title
            and self.desc == other.desc
        )

    def __hash__(self) -> int:
        return hash((self.category, self.title, self.desc))


def match_detail_from_dict(s: Any) -> List[MatchDetail]:
    return from_list(MatchDetail.from_dict, s)


def match_detail_to_dict(x: List[MatchDetail]) -> Any:
    return from_list(lambda x: to_class(MatchDetail, x), x)
