from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_int, from_none, from_str, from_union


@dataclass
class BasketballCourt:
    number: Optional[None]
    id: Optional[int] = None
    label: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "BasketballCourt":
        assert isinstance(obj, dict)
        numero = from_none(obj.get("numero"))
        id = from_union([from_int, from_none], obj.get("id"))
        libelle = from_union([from_none, from_str], obj.get("libelle"))
        return BasketballCourt(numero, id, libelle)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.number is not None:
            result["numero"] = from_none(self.number)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.label is not None:
            result["libelle"] = from_union([from_none, from_str], self.label)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BasketballCourt):
            return False
        return (
            self.number == other.number
            and self.id == other.id
            and self.label == other.label
        )

    def __hash__(self) -> int:
        return hash((self.number, self.id, self.label))
