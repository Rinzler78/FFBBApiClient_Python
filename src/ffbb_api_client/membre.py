from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_bool, from_int, from_none, from_str, from_union, is_type


@dataclass
class Membre:
    id: Optional[int] = None
    nom: Optional[str] = None
    prenom: Optional[str] = None
    adresse1: Optional[str] = None
    adresse2: Optional[int] = None
    code_postal: Optional[int] = None
    ville: Optional[str] = None
    mail: Optional[str] = None
    telephone_fixe: Optional[str] = None
    telephone_portable: Optional[str] = None
    code_fonction: Optional[str] = None
    libelle_fonction: Optional[str] = None
    id_licence: Optional[int] = None
    accord_diffusion_site_web: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> "Membre":
        assert isinstance(obj, dict)
        adresse2 = from_union([from_str, from_none], obj.get("adresse2"))
        code_postal = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("codePostal")
        )
        telephone_fixe = from_union([from_str, from_none], obj.get("telephoneFixe"))
        id = from_union([from_int, from_none], obj.get("id"))
        nom = from_union([from_str, from_none], obj.get("nom"))
        prenom = from_union([from_str, from_none], obj.get("prenom"))
        id_licence = from_union([from_int, from_none], obj.get("idLicence"))
        adresse1 = from_union([from_str, from_none], obj.get("adresse1"))
        ville = from_union([from_str, from_none], obj.get("ville"))
        mail = from_union([from_str, from_none], obj.get("mail"))
        telephone_portable = from_union(
            [from_str, from_none], obj.get("telephonePortable")
        )
        code_fonction = from_union([from_str, from_none], obj.get("codeFonction"))
        libelle_fonction = from_union([from_str, from_none], obj.get("libelleFonction"))
        accord_diffusion_site_web = from_union(
            [from_bool, from_none], obj.get("accordDiffusionSiteWeb")
        )
        return Membre(
            id,
            nom,
            prenom,
            adresse1,
            adresse2,
            code_postal,
            ville,
            mail,
            telephone_fixe,
            telephone_portable,
            code_fonction,
            libelle_fonction,
            id_licence,
            accord_diffusion_site_web,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.adresse2 is not None:
            result["adresse2"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.adresse2,
            )
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
        if self.telephone_fixe is not None:
            result["telephoneFixe"] = from_none(self.telephone_fixe)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.nom is not None:
            result["nom"] = from_union([from_str, from_none], self.nom)
        if self.prenom is not None:
            result["prenom"] = from_union([from_str, from_none], self.prenom)
        if self.id_licence is not None:
            result["idLicence"] = from_union([from_int, from_none], self.id_licence)
        if self.adresse1 is not None:
            result["adresse1"] = from_union([from_str, from_none], self.adresse1)
        if self.ville is not None:
            result["ville"] = from_union([from_str, from_none], self.ville)
        if self.mail is not None:
            result["mail"] = from_union([from_str, from_none], self.mail)
        if self.telephone_portable is not None:
            result["telephonePortable"] = from_union(
                [from_str, from_none], self.telephone_portable
            )
        if self.code_fonction is not None:
            result["codeFonction"] = from_union(
                [from_str, from_none], self.code_fonction
            )
        if self.libelle_fonction is not None:
            result["libelleFonction"] = from_union(
                [from_str, from_none], self.libelle_fonction
            )
        if self.accord_diffusion_site_web is not None:
            result["accordDiffusionSiteWeb"] = from_union(
                [from_bool, from_none], self.accord_diffusion_site_web
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Membre):
            return False
        return (
            self.id == other.id
            and self.nom == other.nom
            and self.prenom == other.prenom
            and self.adresse1 == other.adresse1
            and self.adresse2 == other.adresse2
            and self.code_postal == other.code_postal
            and self.ville == other.ville
            and self.mail == other.mail
            and self.telephone_fixe == other.telephone_fixe
            and self.telephone_portable == other.telephone_portable
            and self.code_fonction == other.code_fonction
            and self.libelle_fonction == other.libelle_fonction
            and self.id_licence == other.id_licence
            and self.accord_diffusion_site_web == other.accord_diffusion_site_web
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.id,
                self.nom,
                self.prenom,
                self.adresse1,
                self.adresse2,
                self.code_postal,
                self.ville,
                self.mail,
                self.telephone_fixe,
                self.telephone_portable,
                self.code_fonction,
                self.libelle_fonction,
                self.id_licence,
                self.accord_diffusion_site_web,
            )
        )
