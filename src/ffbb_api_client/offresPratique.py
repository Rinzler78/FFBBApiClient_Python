from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_int, from_none, from_str, from_union


@dataclass
class OffresPratique:
    id: Optional[int] = None
    type_pratique: Optional[str] = None
    categorie_pratique: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "OffresPratique":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        type_pratique = from_union([from_str, from_none], obj.get("typePratique"))
        categorie_pratique = from_union(
            [from_str, from_none], obj.get("categoriePratique")
        )
        return OffresPratique(id, type_pratique, categorie_pratique)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.type_pratique is not None:
            result["typePratique"] = from_union(
                [from_str, from_none], self.type_pratique
            )
        if self.categorie_pratique is not None:
            result["categoriePratique"] = from_union(
                [from_str, from_none], self.categorie_pratique
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OffresPratique):
            return False
        return (
            self.id == other.id
            and self.type_pratique == other.type_pratique
            and self.categorie_pratique == other.categorie_pratique
        )

    def __hash__(self) -> int:
        return hash((self.id, self.type_pratique, self.categorie_pratique))
