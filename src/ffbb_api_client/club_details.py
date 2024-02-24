from dataclasses import dataclass
from typing import Any, List, Optional

from .converters import from_list, from_none, from_union, to_class
from .field import Field
from .team import Team


@dataclass
class ClubDetails:
    infos: Optional[List[Field]] = None
    fields: Optional[List[Field]] = None
    teams: Optional[List[Team]] = None

    @staticmethod
    def from_dict(obj: Any) -> "ClubDetails":
        assert isinstance(obj, dict)
        infos = from_union(
            [lambda x: from_list(Field.from_dict, x), from_none], obj.get("infos")
        )
        fields = from_union(
            [lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields")
        )
        teams = from_union(
            [lambda x: from_list(Team.from_dict, x), from_none], obj.get("teams")
        )
        return ClubDetails(infos, fields, teams)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.infos is not None:
            result["infos"] = from_union(
                [lambda x: from_list(lambda x: to_class(Field, x), x), from_none],
                self.infos,
            )
        if self.fields is not None:
            result["fields"] = from_union(
                [lambda x: from_list(lambda x: to_class(Field, x), x), from_none],
                self.fields,
            )
        if self.teams is not None:
            result["teams"] = from_union(
                [lambda x: from_list(lambda x: to_class(Team, x), x), from_none],
                self.teams,
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ClubDetails):
            return False
        return (
            self.infos == other.infos
            and self.fields == other.fields
            and self.teams == other.teams
        )

    def __hash__(self) -> int:
        return hash((self.infos, self.fields, self.teams))


def club_details_from_dict(s: Any) -> ClubDetails:
    return ClubDetails.from_dict(s)


def club_details_to_dict(x: ClubDetails) -> Any:
    return to_class(ClubDetails, x)
