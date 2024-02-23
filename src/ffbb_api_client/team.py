from dataclasses import dataclass
from typing import Any, Optional

from ffbb_api_client.converters import from_none, from_str, from_union


@dataclass
class Team:
    id: Optional[str] = None
    sub_competition: Optional[str] = None
    name: Optional[str] = None
    group: Optional[str] = None
    category: Optional[str] = None
    group_field: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Team":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        sub_competition = from_union([from_str, from_none], obj.get("subCompetition"))
        name = from_union([from_str, from_none], obj.get("name"))
        group = from_union([from_str, from_none], obj.get("group"))
        category = from_union([from_str, from_none], obj.get("category"))
        group_field = from_union([from_str, from_none], obj.get("groupField"))
        return Team(id, sub_competition, name, group, category, group_field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.sub_competition is not None:
            result["subCompetition"] = from_union(
                [from_str, from_none], self.sub_competition
            )
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.group is not None:
            result["group"] = from_union([from_str, from_none], self.group)
        if self.category is not None:
            result["category"] = from_union([from_str, from_none], self.category)
        if self.group_field is not None:
            result["groupField"] = from_union([from_str, from_none], self.group_field)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Team):
            return False
        return (
            self.id == other.id
            and self.sub_competition == other.sub_competition
            and self.name == other.name
            and self.group == other.group
            and self.category == other.category
            and self.group_field == other.group_field
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.id,
                self.sub_competition,
                self.name,
                self.group,
                self.category,
                self.group_field,
            )
        )
