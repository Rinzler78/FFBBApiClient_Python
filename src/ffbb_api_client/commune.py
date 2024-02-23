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
class Commune:
    code_postal: Optional[int] = None
    code_insee: Optional[int] = None
    cd_post_cmne: Optional[int] = None
    id: Optional[int] = None
    libelle: Optional[str] = None
    id_cmne: Optional[int] = None
    lb_cmne: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Commune":
        assert isinstance(obj, dict)
        code_postal = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("codePostal")
        )
        code_insee = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("codeInsee")
        )
        cd_post_cmne = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("cdPostCmne")
        )
        id = from_union([from_int, from_none], obj.get("id"))
        libelle = from_union([from_str, from_none], obj.get("libelle"))
        id_cmne = from_union([from_int, from_none], obj.get("idCmne"))
        lb_cmne = from_union([from_str, from_none], obj.get("lbCmne"))
        return Commune(
            code_postal, code_insee, cd_post_cmne, id, libelle, id_cmne, lb_cmne
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.code_postal is not None:
            result["codePostal"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.code_postal,
            )
        if self.code_insee is not None:
            result["codeInsee"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.code_insee,
            )
        if self.cd_post_cmne is not None:
            result["cdPostCmne"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.cd_post_cmne,
            )
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.libelle is not None:
            result["libelle"] = from_union([from_str, from_none], self.libelle)
        if self.id_cmne is not None:
            result["idCmne"] = from_union([from_int, from_none], self.id_cmne)
        if self.lb_cmne is not None:
            result["lbCmne"] = from_union([from_str, from_none], self.lb_cmne)
        return result

    def __eq__(self, other):
        if isinstance(other, Commune):
            return (
                self.code_postal == other.code_postal
                and self.code_insee == other.code_insee
                and self.cd_post_cmne == other.cd_post_cmne
                and self.id == other.id
                and self.libelle == other.libelle
                and self.id_cmne == other.id_cmne
                and self.lb_cmne == other.lb_cmne
            )
        return False

    def __hash__(self):
        return hash(
            (
                self.code_postal,
                self.code_insee,
                self.cd_post_cmne,
                self.id,
                self.libelle,
                self.id_cmne,
                self.lb_cmne,
            )
        )


def commune_from_dict(s: Any) -> List[Commune]:
    return from_list(Commune.from_dict, s)


def commune_to_dict(x: List[Commune]) -> Any:
    return from_list(lambda x: to_class(Commune, x), x)
