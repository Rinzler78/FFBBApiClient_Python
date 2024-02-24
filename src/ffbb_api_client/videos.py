from dataclasses import dataclass
from typing import Any, List, Optional

from .converters import from_list, from_none, from_str, from_union, to_class
from .item import Item
from .page_info import PageInfo


@dataclass
class Videos:
    next_page_token: Optional[str] = None
    items: Optional[List[Item]] = None
    page_info: Optional[PageInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> "Videos":
        assert isinstance(obj, dict)
        next_page_token = from_union([from_str, from_none], obj.get("nextPageToken"))
        items = from_union(
            [lambda x: from_list(Item.from_dict, x), from_none], obj.get("items")
        )
        page_info = from_union([PageInfo.from_dict, from_none], obj.get("pageInfo"))
        return Videos(next_page_token, items, page_info)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.next_page_token is not None:
            result["nextPageToken"] = from_union(
                [from_str, from_none], self.next_page_token
            )
        if self.items is not None:
            result["items"] = from_union(
                [lambda x: from_list(lambda x: to_class(Item, x), x), from_none],
                self.items,
            )
        if self.page_info is not None:
            result["pageInfo"] = from_union(
                [lambda x: to_class(PageInfo, x), from_none], self.page_info
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Videos):
            return False
        return (
            self.next_page_token == other.next_page_token
            and self.items == other.items
            and self.page_info == other.page_info
        )

    def __hash__(self) -> int:
        return hash((self.next_page_token, self.items, self.page_info))


def videos_from_dict(s: Any) -> Videos:
    return Videos.from_dict(s)


def videos_to_dict(x: Videos) -> Any:
    return to_class(Videos, x)
