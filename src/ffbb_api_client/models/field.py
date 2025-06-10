"""Model for Field returned by the FFBB API."""

from dataclasses import dataclass
from typing import Any, Optional

from ..utils.converters import from_int, from_none, from_str, from_union, is_type


@dataclass
class Field:
    """
    Data class representing a field or property of a club or entity.
    """

    group_id: Optional[int] = None
    name: Optional[str] = None
    title: Optional[str] = None
    desc: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Field":
        """
        Create a Field instance from a dictionary.
        """
        assert isinstance(obj, dict)
        group_id = from_union(
            [from_none, from_int, lambda x: int(from_str(x))], obj.get("groupId")
        )
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        desc = from_union([from_str, from_none], obj.get("desc"))
        return Field(group_id, name, title, desc)

    def to_dict(self) -> dict:
        """
        Convert the Field instance to a dictionary.
        """
        result: dict = {}
        if self.group_id is not None:
            result["groupId"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.group_id,
            )
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.desc is not None:
            result["desc"] = from_union([from_str, from_none], self.desc)
        return result

    def __eq__(self, other: Any) -> bool:
        """
        Check equality with another Field instance.
        """
        if not isinstance(other, Field):
            return False
        return (
            self.group_id == other.group_id
            and self.name == other.name
            and self.title == other.title
            and self.desc == other.desc
        )

    def __hash__(self) -> int:
        """
        Compute the hash of the Field instance.
        """
        return hash((self.group_id, self.name, self.title, self.desc))
