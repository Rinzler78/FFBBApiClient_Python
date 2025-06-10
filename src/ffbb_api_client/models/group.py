"""Model for Group returned by the FFBB API."""

from dataclasses import dataclass
from typing import Any, Optional

from ..utils.converters import from_none, from_str, from_union
from .competition_type import CompetitionType, extract_competition_type


@dataclass
class Group:
    """
    Data class for Group information.

    Attributes:
        id: Value from the API.
        name: Value from the API.
        competition_type: Value from the API.
    """

    id: Optional[str] = None
    name: Optional[str] = None
    competition_type: Optional[CompetitionType] = None

    @staticmethod
    def from_dict(obj: Any) -> "Group":
        """Create an instance from a dictionary."""
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        competition_type = from_union(
            [extract_competition_type, from_none], obj.get("type")
        )
        return Group(id, name, competition_type)

    def to_dict(self) -> dict:
        """Convert the instance to a dictionary."""
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.competition_type is not None:
            result["type"] = from_union(
                [from_str, from_none], self.competition_type.value
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Group):
            return False
        return (
            self.id == other.id
            and self.name == other.name
            and self.competition_type == other.competition_type
        )

    def __hash__(self) -> int:
        return hash((self.id, self.name, self.competition_type))
