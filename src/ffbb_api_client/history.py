from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from .converters import from_datetime, from_none, from_union, to_class
from .season import Season
from .type_association import TypeAssociation


@dataclass
class History:
    cessation: None
    affiliation_date: Optional[datetime] = None
    reaffiliation_date: Optional[datetime] = None
    season: Optional[Season] = None
    creation_date: Optional[datetime] = None
    association_type: Optional[TypeAssociation] = None

    @staticmethod
    def from_dict(obj: Any) -> "History":
        assert isinstance(obj, dict)
        cessation = from_union([from_datetime, from_none], obj.get("cessation"))
        affiliation_date = from_union(
            [from_datetime, from_none], obj.get("dateAffiliation")
        )
        reaffiliation_date = from_union(
            [from_datetime, from_none], obj.get("dateReaffiliation")
        )
        season = from_union([Season.from_dict, from_none], obj.get("saison"))
        creation_date = from_union([from_datetime, from_none], obj.get("creation"))
        association_type = from_union(
            [TypeAssociation.from_dict, from_none], obj.get("typeAssociation")
        )
        return History(
            cessation,
            affiliation_date,
            reaffiliation_date,
            season,
            creation_date,
            association_type,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.cessation is not None:
            result["cessation"] = from_none(self.cessation)
        if self.affiliation_date is not None:
            result["dateAffiliation"] = from_union(
                [lambda x: x.isoformat(), from_none], self.affiliation_date
            )
        if self.reaffiliation_date is not None:
            result["dateReaffiliation"] = from_union(
                [lambda x: x.isoformat(), from_none], self.reaffiliation_date
            )
        if self.season is not None:
            result["saison"] = from_union(
                [lambda x: to_class(Season, x), from_none], self.season
            )
        if self.creation_date is not None:
            result["creation"] = from_union(
                [lambda x: x.isoformat(), from_none], self.creation_date
            )
        if self.association_type is not None:
            result["typeAssociation"] = from_union(
                [lambda x: to_class(TypeAssociation, x), from_none],
                self.association_type,
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, History):
            return False
        return (
            self.cessation == other.cessation
            and self.affiliation_date == other.affiliation_date
            and self.reaffiliation_date == other.reaffiliation_date
            and self.season == other.season
            and self.creation_date == other.creation_date
            and self.association_type == other.association_type
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.cessation,
                self.affiliation_date,
                self.reaffiliation_date,
                self.season,
                self.creation_date,
                self.association_type,
            )
        )
