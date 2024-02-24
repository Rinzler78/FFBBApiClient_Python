from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from .converters import from_datetime, from_none, from_union, to_class
from .saison import Saison
from .type_association import TypeAssociation


@dataclass
class Historique:
    cessation: None
    date_affiliation: Optional[datetime] = None
    date_reaffiliation: Optional[datetime] = None
    saison: Optional[Saison] = None
    creation: Optional[datetime] = None
    type_association: Optional[TypeAssociation] = None

    @staticmethod
    def from_dict(obj: Any) -> "Historique":
        assert isinstance(obj, dict)
        cessation = from_none(obj.get("cessation"))
        date_affiliation = from_union(
            [from_datetime, from_none], obj.get("dateAffiliation")
        )
        date_reaffiliation = from_union(
            [from_datetime, from_none], obj.get("dateReaffiliation")
        )
        saison = from_union([Saison.from_dict, from_none], obj.get("saison"))
        creation = from_union([from_datetime, from_none], obj.get("creation"))
        type_association = from_union(
            [TypeAssociation.from_dict, from_none], obj.get("typeAssociation")
        )
        return Historique(
            cessation,
            date_affiliation,
            date_reaffiliation,
            saison,
            creation,
            type_association,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.cessation is not None:
            result["cessation"] = from_none(self.cessation)
        if self.date_affiliation is not None:
            result["dateAffiliation"] = from_union(
                [lambda x: x.isoformat(), from_none], self.date_affiliation
            )
        if self.date_reaffiliation is not None:
            result["dateReaffiliation"] = from_union(
                [lambda x: x.isoformat(), from_none], self.date_reaffiliation
            )
        if self.saison is not None:
            result["saison"] = from_union(
                [lambda x: to_class(Saison, x), from_none], self.saison
            )
        if self.creation is not None:
            result["creation"] = from_union(
                [lambda x: x.isoformat(), from_none], self.creation
            )
        if self.type_association is not None:
            result["typeAssociation"] = from_union(
                [lambda x: to_class(TypeAssociation, x), from_none],
                self.type_association,
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Historique):
            return False
        return (
            self.cessation == other.cessation
            and self.date_affiliation == other.date_affiliation
            and self.date_reaffiliation == other.date_reaffiliation
            and self.saison == other.saison
            and self.creation == other.creation
            and self.type_association == other.type_association
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.cessation,
                self.date_affiliation,
                self.date_reaffiliation,
                self.saison,
                self.creation,
                self.type_association,
            )
        )
