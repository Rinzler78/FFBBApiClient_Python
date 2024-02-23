from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from .converters import (
    from_datetime,
    from_int,
    from_none,
    from_str,
    from_stringified_bool,
    from_union,
    is_type,
)


@dataclass
class Saison:
    actif: Optional[bool] = None
    id: Optional[int] = None
    code: Optional[str] = None
    libelle: Optional[str] = None
    debut: Optional[datetime] = None
    fin: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> "Saison":
        assert isinstance(obj, dict)
        actif = from_union(
            [from_none, lambda x: from_stringified_bool(from_str(x))], obj.get("actif")
        )
        id = from_union([from_int, from_none], obj.get("id"))
        code = from_union([from_str, from_none], obj.get("code"))
        libelle = from_union([from_str, from_none], obj.get("libelle"))
        debut = from_union([from_datetime, from_none], obj.get("debut"))
        fin = from_union([from_datetime, from_none], obj.get("fin"))
        return Saison(actif, id, code, libelle, debut, fin)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.actif is not None:
            result["actif"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(bool, x))(x)).lower())(x)
                    ),
                ],
                self.actif,
            )
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.code is not None:
            result["code"] = from_union([from_str, from_none], self.code)
        if self.libelle is not None:
            result["libelle"] = from_union([from_str, from_none], self.libelle)
        if self.debut is not None:
            result["debut"] = from_union(
                [lambda x: x.isoformat(), from_none], self.debut
            )
        if self.fin is not None:
            result["fin"] = from_union([lambda x: x.isoformat(), from_none], self.fin)
        return result

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Saison):
            return (
                self.actif == other.actif
                and self.id == other.id
                and self.code == other.code
                and self.libelle == other.libelle
                and self.debut == other.debut
                and self.fin == other.fin
            )
        return False

    def __hash__(self) -> int:
        return hash(
            (self.actif, self.id, self.code, self.libelle, self.debut, self.fin)
        )
