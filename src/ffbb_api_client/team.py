from dataclasses import dataclass
from typing import Any, Optional

from .category import Category, extract_category
from .competition_type import CompetitionType, extract_competition_type
from .converters import from_none, from_str, from_union
from .geographycale_zone import GeographycaleZone, extract_geographycale_zone
from .sex import Sex, extract_sex


@dataclass
class Team:
    id: Optional[str] = None
    sub_competition: Optional[str] = None
    name: Optional[str] = None
    group: Optional[str] = None
    category: Optional[Category] = None
    group_field: Optional[str] = None
    competition_type: Optional[CompetitionType] = None
    sex: Optional[Sex] = None
    geographycale_zone: Optional[GeographycaleZone] = None

    @staticmethod
    def from_dict(obj: Any) -> "Team":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        sub_competition = from_union([from_str, from_none], obj.get("subCompetition"))
        name = from_union([from_str, from_none], obj.get("name"))
        group = from_union([from_str, from_none], obj.get("group"))
        category = from_union([extract_category, from_none], obj.get("category"))
        group_field = from_union([from_str, from_none], obj.get("groupField"))
        competition_type = from_union([extract_competition_type, from_none], name)
        sex = from_union([extract_sex, from_none], group_field)
        geographycale_zone = from_union([extract_geographycale_zone, from_none], name)
        return Team(
            id,
            sub_competition,
            name,
            group,
            category,
            group_field,
            competition_type,
            sex,
            geographycale_zone,
        )

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
            and self.competition_type == other.competition_type
            and self.sex == other.sex
            and self.geographycale_zone == other.geographycale_zone
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
                self.competition_type,
                self.sex,
                self.geographycale_zone,
            )
        )
