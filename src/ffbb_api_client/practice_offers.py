from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_int, from_none, from_str, from_union


@dataclass
class PracticeOffers:
    id: Optional[int] = None
    type: Optional[str] = None
    category: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "PracticeOffers":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        type_pratique = from_union([from_str, from_none], obj.get("typePratique"))
        categorie_pratique = from_union(
            [from_str, from_none], obj.get("categoriePratique")
        )
        return PracticeOffers(id, type_pratique, categorie_pratique)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.type is not None:
            result["typePratique"] = from_union([from_str, from_none], self.type)
        if self.category is not None:
            result["categoriePratique"] = from_union(
                [from_str, from_none], self.category
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PracticeOffers):
            return False
        return (
            self.id == other.id
            and self.type == other.type
            and self.category == other.category
        )

    def __hash__(self) -> int:
        return hash((self.id, self.type, self.category))
