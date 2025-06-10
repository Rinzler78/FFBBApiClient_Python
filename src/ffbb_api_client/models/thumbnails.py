"""Model for Thumbnails returned by the FFBB API."""

from dataclasses import dataclass
from typing import Any, Optional

from ..utils.converters import from_none, from_union, to_class
from .default import Default


@dataclass
class Thumbnails:
    """
    Data class for Thumbnails information.

    Attributes:
        default: Value from the API.
        medium: Value from the API.
        high: Value from the API.
        standard: Value from the API.
        maxres: Value from the API.
    """

    default: Optional[Default] = None
    medium: Optional[Default] = None
    high: Optional[Default] = None
    standard: Optional[Default] = None
    maxres: Optional[Default] = None

    @staticmethod
    def from_dict(obj: Any) -> "Thumbnails":
        """Create an instance from a dictionary."""
        assert isinstance(obj, dict)
        default = from_union([Default.from_dict, from_none], obj.get("default"))
        medium = from_union([Default.from_dict, from_none], obj.get("medium"))
        high = from_union([Default.from_dict, from_none], obj.get("high"))
        standard = from_union([Default.from_dict, from_none], obj.get("standard"))
        maxres = from_union([Default.from_dict, from_none], obj.get("maxres"))
        return Thumbnails(default, medium, high, standard, maxres)

    def to_dict(self) -> dict:
        """Convert the instance to a dictionary."""
        result: dict = {}
        if self.default is not None:
            result["default"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.default
            )
        if self.medium is not None:
            result["medium"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.medium
            )
        if self.high is not None:
            result["high"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.high
            )
        if self.standard is not None:
            result["standard"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.standard
            )
        if self.maxres is not None:
            result["maxres"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.maxres
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Thumbnails):
            return False
        return (
            self.default == other.default
            and self.medium == other.medium
            and self.high == other.high
            and self.standard == other.standard
            and self.maxres == other.maxres
        )

    def __hash__(self) -> int:
        return hash((self.default, self.medium, self.high, self.standard, self.maxres))
