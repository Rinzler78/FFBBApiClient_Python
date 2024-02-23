from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_int, from_none, from_str, from_union


@dataclass
class TypeAssociation:
    id: Optional[int] = None
    libelle: Optional[str] = None
    code: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "TypeAssociation":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        libelle = from_union([from_str, from_none], obj.get("libelle"))
        code = from_union([from_str, from_none], obj.get("code"))
        return TypeAssociation(id, libelle, code)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.libelle is not None:
            result["libelle"] = from_union([from_str, from_none], self.libelle)
        if self.code is not None:
            result["code"] = from_union([from_str, from_none], self.code)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TypeAssociation):
            return False
        return (
            self.id == other.id
            and self.libelle == other.libelle
            and self.code == other.code
        )

    def __hash__(self) -> int:
        return hash((self.id, self.libelle, self.code))
