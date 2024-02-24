from dataclasses import dataclass
from typing import Any, List, Optional

from .converters import (
    from_int,
    from_list,
    from_none,
    from_str,
    from_union,
    is_type,
    to_class,
)


@dataclass
class Municipality:
    postal_code: Optional[int] = None
    insee_code: Optional[str] = None
    postal_community_code: Optional[int] = None
    id: Optional[int] = None
    label: Optional[str] = None
    municipality_id: Optional[int] = None
    municipality_label: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Municipality":
        assert isinstance(obj, dict)
        postal_code = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("codePostal")
        )
        insee_code = from_union(
            [from_none, lambda x: from_str(x)], obj.get("codeInsee")
        )
        postal_community_code = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("cdPostCmne")
        )
        id = from_union([from_int, from_none], obj.get("id"))
        label = from_union([from_str, from_none], obj.get("libelle"))
        municipality_id = from_union([from_int, from_none], obj.get("idCmne"))
        municipality_label = from_union([from_str, from_none], obj.get("lbCmne"))
        return Municipality(
            postal_code,
            insee_code,
            postal_community_code,
            id,
            label,
            municipality_id,
            municipality_label,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.postal_code is not None:
            result["codePostal"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.postal_code,
            )
        if self.insee_code is not None:
            result["codeInsee"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.insee_code,
            )
        if self.postal_community_code is not None:
            result["cdPostCmne"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.postal_community_code,
            )
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.label is not None:
            result["libelle"] = from_union([from_str, from_none], self.label)
        if self.municipality_id is not None:
            result["idCmne"] = from_union([from_int, from_none], self.municipality_id)
        if self.municipality_label is not None:
            result["lbCmne"] = from_union(
                [from_str, from_none], self.municipality_label
            )
        return result

    def __eq__(self, other):
        if isinstance(other, Municipality):
            return (
                self.postal_code == other.postal_code
                and self.insee_code == other.insee_code
                and self.postal_community_code == other.postal_community_code
                and self.id == other.id
                and self.label == other.label
                and self.municipality_id == other.municipality_id
                and self.municipality_label == other.municipality_label
            )
        return False

    def __hash__(self):
        return hash(
            (
                self.postal_code,
                self.insee_code,
                self.postal_community_code,
                self.id,
                self.label,
                self.municipality_id,
                self.municipality_label,
            )
        )


def commune_from_dict(s: Any) -> List[Municipality]:
    return from_list(Municipality.from_dict, s)


def commune_to_dict(x: List[Municipality]) -> Any:
    return from_list(lambda x: to_class(Municipality, x), x)
