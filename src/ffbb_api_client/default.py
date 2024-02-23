from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_int, from_none, from_str, from_union


@dataclass
class Default:
    url: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "Default":
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        width = from_union([from_int, from_none], obj.get("width"))
        height = from_union([from_int, from_none], obj.get("height"))
        return Default(url, width, height)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Default):
            return False
        return (
            self.url == other.url
            and self.width == other.width
            and self.height == other.height
        )

    def __hash__(self) -> int:
        return hash((self.url, self.width, self.height))
