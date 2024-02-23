from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_int, from_none, from_str, from_union


@dataclass
class Salle:
    numero: Optional[None]
    id: Optional[int] = None
    libelle: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Salle":
        assert isinstance(obj, dict)
        numero = from_none(obj.get("numero"))
        id = from_union([from_int, from_none], obj.get("id"))
        libelle = from_union([from_none, from_str], obj.get("libelle"))
        return Salle(numero, id, libelle)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.numero is not None:
            result["numero"] = from_none(self.numero)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.libelle is not None:
            result["libelle"] = from_union([from_none, from_str], self.libelle)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Salle):
            return False
        return (
            self.numero == other.numero
            and self.id == other.id
            and self.libelle == other.libelle
        )

    def __hash__(self) -> int:
        return hash((self.numero, self.id, self.libelle))
