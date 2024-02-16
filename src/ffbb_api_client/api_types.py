from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Callable, List, Optional, Type, TypeVar, Union, cast

import dateutil.parser

T = TypeVar("T")


class CompetitionType(Enum):
    CHAMPIONSHIP = "championship"
    CUP = "cup"


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except Exception:
            pass
    assert False


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_stringified_bool(x: str) -> bool:
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Cartographie:
    code_postal: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    title: Optional[str] = None
    adress: Optional[str] = None
    ville: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Cartographie":
        assert isinstance(obj, dict)
        code_postal = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("codePostal")
        )
        latitude = from_union([from_float, from_none], obj.get("latitude"))
        longitude = from_union([from_float, from_none], obj.get("longitude"))
        title = from_union([from_str, from_none], obj.get("title"))
        adress = from_union([from_str, from_none], obj.get("adress"))
        ville = from_union([from_str, from_none], obj.get("ville"))
        return Cartographie(code_postal, latitude, longitude, title, adress, ville)

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
        if self.latitude is not None:
            result["latitude"] = from_union([to_float, from_none], self.latitude)
        if self.longitude is not None:
            result["longitude"] = from_union([to_float, from_none], self.longitude)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.adress is not None:
            result["adress"] = from_union([from_str, from_none], self.adress)
        if self.ville is not None:
            result["ville"] = from_union([from_str, from_none], self.ville)
        return result


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


def commune_from_dict(s: Any) -> List[Commune]:
    return from_list(Commune.from_dict, s)


def commune_to_dict(x: List[Commune]) -> Any:
    return from_list(lambda x: to_class(Commune, x), x)


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


@dataclass
class Membre:
    adresse2: Optional[int] = None
    code_postal: Optional[int] = None
    telephone_fixe: Optional[str] = None
    id: Optional[int] = None
    nom: Optional[str] = None
    prenom: Optional[str] = None
    id_licence: Optional[int] = None
    adresse1: Optional[str] = None
    ville: Optional[str] = None
    mail: Optional[str] = None
    telephone_portable: Optional[str] = None
    code_fonction: Optional[str] = None
    libelle_fonction: Optional[str] = None
    accord_diffusion_site_web: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> "Membre":
        assert isinstance(obj, dict)
        adresse2 = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("adresse2")
        )
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
            adresse2,
            code_postal,
            telephone_fixe,
            id,
            nom,
            prenom,
            id_licence,
            adresse1,
            ville,
            mail,
            telephone_portable,
            code_fonction,
            libelle_fonction,
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


@dataclass
class Salle:
    numero: None
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


@dataclass
class ClubInfos:
    nom_club_pro: None
    adresse_club_pro: None
    commune_club_pro: None
    salle_club_pro: None
    participation_obe: None
    id: Optional[int] = None
    id_organisme_pere: Optional[int] = None
    code: Optional[str] = None
    nom: Optional[str] = None
    type: Optional[str] = None
    adresse: Optional[str] = None
    telephone: Optional[str] = None
    mail: Optional[str] = None
    commune: Optional[Commune] = None
    type_association: Optional[TypeAssociation] = None
    salle: Optional[Salle] = None
    url_site_web: Optional[str] = None
    membres: Optional[List[Membre]] = None
    organisme_fils: Optional[List[Any]] = None
    offres_pratique: Optional[List[OffresPratique]] = None
    labellisation: Optional[List[Any]] = None
    cartographie: Optional[Cartographie] = None
    historique: Optional[List[Historique]] = None
    id_org: Optional[int] = None
    id_cmne: Optional[int] = None
    cd_org: Optional[str] = None
    nom_org: Optional[str] = None
    date_affiliation: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> "ClubInfos":
        assert isinstance(obj, dict)
        nom_club_pro = from_union([from_str, from_none], obj.get("nomClubPro"))
        adresse_club_pro = from_union([from_str, from_none], obj.get("adresseClubPro"))
        commune_club_pro = from_union([from_str, from_none], obj.get("communeClubPro"))
        salle_club_pro = from_union([from_str, from_none], obj.get("salleClubPro"))
        participation_obe = from_union(
            [from_str, from_none], obj.get("participationOBE")
        )
        id = from_union([from_int, from_none], obj.get("id"))
        id_organisme_pere = from_union(
            [from_int, from_none], obj.get("idOrganismePere")
        )
        code = from_union([from_str, from_none], obj.get("code"))
        nom = from_union([from_str, from_none], obj.get("nom"))
        type = from_union([from_str, from_none], obj.get("type"))
        adresse = from_union([from_str, from_none], obj.get("adresse"))
        telephone = from_union([from_str, from_none], obj.get("telephone"))
        mail = from_union([from_none, from_str], obj.get("mail"))
        commune = from_union([Commune.from_dict, from_none], obj.get("commune"))
        type_association = from_union(
            [TypeAssociation.from_dict, from_none], obj.get("typeAssociation")
        )
        salle = from_union([Salle.from_dict, from_none], obj.get("salle"))
        url_site_web = from_union([from_none, from_str], obj.get("urlSiteWeb"))
        membres = from_union(
            [lambda x: from_list(Membre.from_dict, x), from_none], obj.get("membres")
        )
        organisme_fils = from_union(
            [lambda x: from_list(lambda x: x, x), from_none], obj.get("organismeFils")
        )
        offres_pratique = from_union(
            [lambda x: from_list(OffresPratique.from_dict, x), from_none],
            obj.get("offresPratique"),
        )
        labellisation = from_union(
            [lambda x: from_list(lambda x: x, x), from_none], obj.get("labellisation")
        )
        cartographie = from_union(
            [Cartographie.from_dict, from_none], obj.get("cartographie")
        )
        historique = from_union(
            [lambda x: from_list(Historique.from_dict, x), from_none],
            obj.get("historique"),
        )
        id_org = from_union([from_int, from_none], obj.get("idOrg"))
        id_cmne = from_union([from_int, from_none], obj.get("idCmne"))
        cd_org = from_union([from_str, from_none], obj.get("cdOrg"))
        nom_org = from_union([from_str, from_none], obj.get("nomOrg"))
        date_affiliation = from_union(
            [from_datetime, from_none], obj.get("dateAffiliation")
        )
        return ClubInfos(
            nom_club_pro,
            adresse_club_pro,
            commune_club_pro,
            salle_club_pro,
            participation_obe,
            id,
            id_organisme_pere,
            code,
            nom,
            type,
            adresse,
            telephone,
            mail,
            commune,
            type_association,
            salle,
            url_site_web,
            membres,
            organisme_fils,
            offres_pratique,
            labellisation,
            cartographie,
            historique,
            id_org,
            id_cmne,
            cd_org,
            nom_org,
            date_affiliation,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.nom_club_pro is not None:
            result["nomClubPro"] = from_none(self.nom_club_pro)
        if self.adresse_club_pro is not None:
            result["adresseClubPro"] = from_none(self.adresse_club_pro)
        if self.commune_club_pro is not None:
            result["communeClubPro"] = from_none(self.commune_club_pro)
        if self.salle_club_pro is not None:
            result["salleClubPro"] = from_none(self.salle_club_pro)
        if self.participation_obe is not None:
            result["participationOBE"] = from_none(self.participation_obe)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.id_organisme_pere is not None:
            result["idOrganismePere"] = from_union(
                [from_int, from_none], self.id_organisme_pere
            )
        if self.code is not None:
            result["code"] = from_union([from_str, from_none], self.code)
        if self.nom is not None:
            result["nom"] = from_union([from_str, from_none], self.nom)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.adresse is not None:
            result["adresse"] = from_union([from_str, from_none], self.adresse)
        if self.telephone is not None:
            result["telephone"] = from_union([from_str, from_none], self.telephone)
        if self.mail is not None:
            result["mail"] = from_union([from_none, from_str], self.mail)
        if self.commune is not None:
            result["commune"] = from_union(
                [lambda x: to_class(Commune, x), from_none], self.commune
            )
        if self.type_association is not None:
            result["typeAssociation"] = from_union(
                [lambda x: to_class(TypeAssociation, x), from_none],
                self.type_association,
            )
        if self.salle is not None:
            result["salle"] = from_union(
                [lambda x: to_class(Salle, x), from_none], self.salle
            )
        if self.url_site_web is not None:
            result["urlSiteWeb"] = from_union([from_none, from_str], self.url_site_web)
        if self.membres is not None:
            result["membres"] = from_union(
                [lambda x: from_list(lambda x: to_class(Membre, x), x), from_none],
                self.membres,
            )
        if self.organisme_fils is not None:
            result["organismeFils"] = from_union(
                [lambda x: from_list(lambda x: x, x), from_none], self.organisme_fils
            )
        if self.offres_pratique is not None:
            result["offresPratique"] = from_union(
                [
                    lambda x: from_list(lambda x: to_class(OffresPratique, x), x),
                    from_none,
                ],
                self.offres_pratique,
            )
        if self.labellisation is not None:
            result["labellisation"] = from_union(
                [lambda x: from_list(lambda x: x, x), from_none], self.labellisation
            )
        if self.cartographie is not None:
            result["cartographie"] = from_union(
                [lambda x: to_class(Cartographie, x), from_none], self.cartographie
            )
        if self.historique is not None:
            result["historique"] = from_union(
                [lambda x: from_list(lambda x: to_class(Historique, x), x), from_none],
                self.historique,
            )
        if self.id_org is not None:
            result["idOrg"] = from_union([from_int, from_none], self.id_org)
        if self.id_cmne is not None:
            result["idCmne"] = from_union([from_int, from_none], self.id_cmne)
        if self.cd_org is not None:
            result["cdOrg"] = from_union([from_str, from_none], self.cd_org)
        if self.nom_org is not None:
            result["nomOrg"] = from_union([from_str, from_none], self.nom_org)
        if self.date_affiliation is not None:
            result["dateAffiliation"] = from_union(
                [lambda x: x.isoformat(), from_none], self.date_affiliation
            )
        return result


def club_infos_from_dict(s: Any) -> List[ClubInfos]:
    return from_list(ClubInfos.from_dict, s)


def club_to_dict(x: List[ClubInfos]) -> Any:
    return from_list(lambda x: to_class(ClubInfos, x), x)


@dataclass
class League:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "League":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return League(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


def league_from_dict(s: Any) -> List[League]:
    return from_list(League.from_dict, s)


def league_to_dict(x: List[League]) -> Any:
    return from_list(lambda x: to_class(League, x), x)


@dataclass
class Area:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Area":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Area(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


def area_from_dict(s: Any) -> List[Area]:
    return from_list(Area.from_dict, s)


def area_to_dict(x: List[Area]) -> Any:
    return from_list(lambda x: to_class(Area, x), x)


@dataclass
class Championship:
    name: Optional[str] = None
    id: Optional[str] = None
    type: Optional[CompetitionType] = None

    @staticmethod
    def from_dict(obj: Any) -> "Championship":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("id"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Championship(name, id, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


def championship_from_dict(s: Any) -> List[Championship]:
    return from_list(Championship.from_dict, s)


def championship_to_dict(x: List[Championship]) -> Any:
    return from_list(lambda x: to_class(Championship, x), x)


@dataclass
class News:
    id: Optional[int] = None
    date: Optional[str] = None
    url: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    title: Optional[str] = None
    image: Optional[str] = None
    excerpt: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "News":
        assert isinstance(obj, dict)
        id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        date = from_union([from_str, from_none], obj.get("date"))
        url = from_union([from_str, from_none], obj.get("url"))
        author = from_union([from_str, from_none], obj.get("author"))
        category = from_union([from_str, from_none], obj.get("category"))
        title = from_union([from_str, from_none], obj.get("title"))
        image = from_union([from_str, from_none], obj.get("image"))
        excerpt = from_union([from_str, from_none], obj.get("excerpt"))
        return News(id, date, url, author, category, title, image, excerpt)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.id,
            )
        if self.date is not None:
            result["date"] = from_union([from_str, from_none], self.date)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.author is not None:
            result["author"] = from_union([from_str, from_none], self.author)
        if self.category is not None:
            result["category"] = from_union([from_str, from_none], self.category)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.image is not None:
            result["image"] = from_union([from_str, from_none], self.image)
        if self.excerpt is not None:
            result["excerpt"] = from_union([from_str, from_none], self.excerpt)
        return result


def news_from_dict(s: Any) -> List[News]:
    return from_list(News.from_dict, s)


def news_to_dict(x: List[News]) -> Any:
    return from_list(lambda x: to_class(News, x), x)


@dataclass
class Field:
    group_id: Optional[int] = None
    name: Optional[str] = None
    title: Optional[str] = None
    desc: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Field":
        assert isinstance(obj, dict)
        group_id = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("groupId")
        )
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        desc = from_union([from_str, from_none], obj.get("desc"))
        return Field(group_id, name, title, desc)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.group_id is not None:
            result["groupId"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.group_id,
            )
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.desc is not None:
            result["desc"] = from_union([from_str, from_none], self.desc)
        return result


@dataclass
class Team:
    id: Optional[str] = None
    sub_competition: Optional[str] = None
    name: Optional[str] = None
    group: Optional[str] = None
    category: Optional[str] = None
    group_field: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Team":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        sub_competition = from_union([from_str, from_none], obj.get("subCompetition"))
        name = from_union([from_str, from_none], obj.get("name"))
        group = from_union([from_str, from_none], obj.get("group"))
        category = from_union([from_str, from_none], obj.get("category"))
        group_field = from_union([from_str, from_none], obj.get("groupField"))
        return Team(id, sub_competition, name, group, category, group_field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.sub_competition is not None:
            result["subCompetition"] = from_union(
                [from_str, from_none], self.sub_competition
            )
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.group is not None:
            result["group"] = from_union([from_str, from_none], self.group)
        if self.category is not None:
            result["category"] = from_union([from_str, from_none], self.category)
        if self.group_field is not None:
            result["groupField"] = from_union([from_str, from_none], self.group_field)
        return result


@dataclass
class ClubDetails:
    infos: Optional[List[Field]] = None
    fields: Optional[List[Field]] = None
    teams: Optional[List[Team]] = None

    @staticmethod
    def from_dict(obj: Any) -> "ClubDetails":
        assert isinstance(obj, dict)
        infos = from_union(
            [lambda x: from_list(Field.from_dict, x), from_none], obj.get("infos")
        )
        fields = from_union(
            [lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields")
        )
        teams = from_union(
            [lambda x: from_list(Team.from_dict, x), from_none], obj.get("teams")
        )
        return ClubDetails(infos, fields, teams)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.infos is not None:
            result["infos"] = from_union(
                [lambda x: from_list(lambda x: to_class(Field, x), x), from_none],
                self.infos,
            )
        if self.fields is not None:
            result["fields"] = from_union(
                [lambda x: from_list(lambda x: to_class(Field, x), x), from_none],
                self.fields,
            )
        if self.teams is not None:
            result["teams"] = from_union(
                [lambda x: from_list(lambda x: to_class(Team, x), x), from_none],
                self.teams,
            )
        return result


def club_details_from_dict(s: Any) -> ClubDetails:
    return ClubDetails.from_dict(s)


def club_details_to_dict(x: ClubDetails) -> Any:
    return to_class(ClubDetails, x)


@dataclass
class Day:
    name: Optional[int] = None
    desc: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "Day":
        assert isinstance(obj, dict)
        name = from_union([from_int, from_none], obj.get("name"))
        desc = from_union([from_int, from_none], obj.get("desc"))
        return Day(name, desc)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_int, from_none], self.name)
        if self.desc is not None:
            result["desc"] = from_union([from_int, from_none], self.desc)
        return result


@dataclass
class Group:
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Group":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Group(id, name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class Score:
    home: int
    visitor: int

    def __str__(self):
        return f"{self.home} - {self.visitor}"

    @property
    def played(self) -> bool:
        return self.home is not None and self.visitor is not None


@dataclass
class Match:
    formatted_date: Optional[datetime] = None
    time: Optional[str] = None
    hometeam: Optional[str] = None
    visitorteam: Optional[str] = None
    score: Optional[Score] = None
    date: Optional[datetime] = None  # Modified property type
    remise: Optional[int] = None
    round: Optional[int] = None
    match_id: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "Match":
        assert isinstance(obj, dict)
        formatted_date_str = from_union([from_int, from_none], obj.get("formattedDate"))
        formatted_date = (
            datetime.fromtimestamp(formatted_date_str) if formatted_date_str else None
        )
        time = from_union([from_str, from_none], obj.get("time"))
        hometeam = from_union([from_str, from_none], obj.get("hometeam"))
        visitorteam = from_union([from_str, from_none], obj.get("visitorteam"))
        score_str = from_union([from_str, from_none], obj.get("score"))
        score = None
        if score_str:
            home_score = None
            visitor_score = None

            try:
                home_score, visitor_score = map(int, score_str.split(" - "))
            except (ValueError, TypeError):
                pass

            score = Score(home_score, visitor_score)

        date_str = from_union([from_str, from_none], obj.get("date"))
        date = (
            datetime.strptime(f"{time} {date_str}", "%H:%M %d/%m/%Y")
            if date_str
            else None
        )
        remise = from_union([from_int, from_none], obj.get("remise"))
        round = from_union([from_int, from_none], obj.get("round"))
        match_id = from_union([from_int, from_none], obj.get("matchId"))
        return Match(
            formatted_date,
            time,
            hometeam,
            visitorteam,
            score,
            date,
            remise,
            round,
            match_id,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.formatted_date is not None:
            result["formattedDate"] = int(self.formatted_date.timestamp())
        if self.time is not None:
            result["time"] = from_union(
                [from_str, from_none], f"{self.date.hour}:{self.date.minute}"
            )
        if self.hometeam is not None:
            result["hometeam"] = from_union([from_str, from_none], self.hometeam)
        if self.visitorteam is not None:
            result["visitorteam"] = from_union([from_str, from_none], self.visitorteam)
        if self.score is not None:
            home = "" if self.score.home is None else self.score.home
            visitor = "" if self.score.visitor is None else self.score.visitor
            result["score"] = from_union([from_str, from_none], f"{home} - {visitor}")
        if self.date is not None:
            result["date"] = self.date.strftime("%d/%m/%Y")
        if self.remise is not None:
            result["remise"] = from_union([from_int, from_none], self.remise)
        if self.round is not None:
            result["round"] = from_union([from_int, from_none], self.round)
        if self.match_id is not None:
            result["matchId"] = from_union([from_int, from_none], self.match_id)
        return result

    @property
    def played(self) -> bool:
        return self.score is not None and self.score.played

    @property
    def is_ghost(self):
        return self.played and self.date.hour == 0 and self.date.minute == 0


@dataclass
class Standing:
    pos: Optional[Union[int, str]] = None
    points: Optional[Union[int, str]] = None
    day: Optional[Union[int, str]] = None
    win: Optional[Union[int, str]] = None
    lost: Optional[Union[int, str]] = None
    draw: Optional[Union[int, str]] = None
    penalties: Optional[Union[int, str]] = None
    forfeited: Optional[Union[int, str]] = None
    defaults: Optional[Union[int, str]] = None
    arb: Optional[Union[int, str]] = None
    ent: Optional[Union[int, str]] = None
    scored: Optional[Union[int, str]] = None
    conceded: Optional[Union[int, str]] = None
    quotient: Optional[Union[float, str]] = None
    club: Optional[str] = None
    initi: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Standing":
        assert isinstance(obj, dict)
        pos = from_union([from_int, from_str, from_none], obj.get("pos"))
        points = from_union([from_int, from_str, from_none], obj.get("points"))
        day = from_union([from_int, from_str, from_none], obj.get("day"))
        win = from_union([from_int, from_str, from_none], obj.get("win"))
        lost = from_union([from_int, from_str, from_none], obj.get("lost"))
        draw = from_union([from_int, from_str, from_none], obj.get("draw"))
        penalties = from_union([from_int, from_str, from_none], obj.get("penalties"))
        forfeited = from_union([from_int, from_str, from_none], obj.get("forfeited"))
        defaults = from_union([from_int, from_str, from_none], obj.get("defaults"))
        arb = from_union([from_int, from_str, from_none], obj.get("arb"))
        ent = from_union([from_int, from_str, from_none], obj.get("ent"))
        scored = from_union([from_int, from_str, from_none], obj.get("scored"))
        conceded = from_union([from_int, from_str, from_none], obj.get("conceded"))
        quotient = from_union([from_float, from_str, from_none], obj.get("quotient"))
        club = from_union([from_str, from_none], obj.get("club"))
        initi = from_union([from_none, from_str], obj.get("initi"))
        return Standing(
            pos,
            points,
            day,
            win,
            lost,
            draw,
            penalties,
            forfeited,
            defaults,
            arb,
            ent,
            scored,
            conceded,
            quotient,
            club,
            initi,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.pos is not None:
            result["pos"] = from_union([from_int, from_str, from_none], self.pos)
        if self.points is not None:
            result["points"] = from_union([from_int, from_str, from_none], self.points)
        if self.day is not None:
            result["day"] = from_union([from_int, from_str, from_none], self.day)
        if self.win is not None:
            result["win"] = from_union([from_int, from_str, from_none], self.win)
        if self.lost is not None:
            result["lost"] = from_union([from_int, from_str, from_none], self.lost)
        if self.draw is not None:
            result["draw"] = from_union([from_int, from_str, from_none], self.draw)
        if self.penalties is not None:
            result["penalties"] = from_union(
                [from_int, from_str, from_none], self.penalties
            )
        if self.forfeited is not None:
            result["forfeited"] = from_union(
                [from_int, from_str, from_none], self.forfeited
            )
        if self.defaults is not None:
            result["defaults"] = from_union(
                [from_int, from_str, from_none], self.defaults
            )
        if self.arb is not None:
            result["arb"] = from_union([from_int, from_str, from_none], self.arb)
        if self.ent is not None:
            result["ent"] = from_union([from_int, from_str, from_none], self.ent)
        if self.scored is not None:
            result["scored"] = from_union([from_int, from_str, from_none], self.scored)
        if self.conceded is not None:
            result["conceded"] = from_union(
                [from_int, from_str, from_none], self.conceded
            )
        if self.quotient is not None:
            result["quotient"] = from_union(
                [to_float, from_str, from_none], self.quotient
            )
        if self.club is not None:
            result["club"] = from_union([from_str, from_none], self.club)
        if self.initi is not None:
            result["initi"] = from_union([from_none, from_str], self.initi)
        return result


@dataclass
class AgendaAndResults:
    sub_competitions: Optional[List[Group]] = None
    groups: Optional[List[Group]] = None
    days: Optional[List[Day]] = None
    current_day: Optional[int] = None
    matchs: Optional[List[Match]] = None
    standings: Optional[List[Standing]] = None

    @staticmethod
    def from_dict(obj: Any) -> "AgendaAndResults":
        assert isinstance(obj, dict)
        sub_competitions = from_union(
            [lambda x: from_list(Group.from_dict, x), from_none],
            obj.get("subCompetitions"),
        )
        groups = from_union(
            [lambda x: from_list(Group.from_dict, x), from_none], obj.get("groups")
        )
        days = from_union(
            [lambda x: from_list(Day.from_dict, x), from_none], obj.get("days")
        )
        current_day = from_union([from_int, from_none], obj.get("currentDay"))
        matchs = from_union(
            [lambda x: from_list(Match.from_dict, x), from_none], obj.get("matchs")
        )
        standings = from_union(
            [lambda x: from_list(Standing.from_dict, x), from_none],
            obj.get("standings"),
        )
        return AgendaAndResults(
            sub_competitions, groups, days, current_day, matchs, standings
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.sub_competitions is not None:
            result["subCompetitions"] = from_union(
                [lambda x: from_list(lambda x: to_class(Group, x), x), from_none],
                self.sub_competitions,
            )
        if self.groups is not None:
            result["groups"] = from_union(
                [lambda x: from_list(lambda x: to_class(Group, x), x), from_none],
                self.groups,
            )
        if self.days is not None:
            result["days"] = from_union(
                [lambda x: from_list(lambda x: to_class(Day, x), x), from_none],
                self.days,
            )
        if self.current_day is not None:
            result["currentDay"] = from_union([from_int, from_none], self.current_day)
        if self.matchs is not None:
            result["matchs"] = from_union(
                [lambda x: from_list(lambda x: to_class(Match, x), x), from_none],
                self.matchs,
            )
        if self.standings is not None:
            result["standings"] = from_union(
                [lambda x: from_list(lambda x: to_class(Standing, x), x), from_none],
                self.standings,
            )
        return result


def agenda_and_results_from_dict(s: Any) -> AgendaAndResults:
    return AgendaAndResults.from_dict(s)


def agenda_and_results_to_dict(x: AgendaAndResults) -> Any:
    return to_class(AgendaAndResults, x)


@dataclass
class Competition:
    name: Optional[str] = None
    id: Optional[str] = None
    group_field: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Competition":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("id"))
        group_field = from_union([from_str, from_none], obj.get("groupField"))
        return Competition(name, id, group_field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.group_field is not None:
            result["groupField"] = from_union([from_str, from_none], self.group_field)
        return result


def competition_from_dict(s: Any) -> List[Competition]:
    return from_list(Competition.from_dict, s)


def competition_to_dict(x: List[Competition]) -> Any:
    return from_list(lambda x: to_class(Competition, x), x)


@dataclass
class ResourceID:
    kind: Optional[str] = None
    video_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "ResourceID":
        assert isinstance(obj, dict)
        kind = from_union([from_str, from_none], obj.get("kind"))
        video_id = from_union([from_str, from_none], obj.get("videoId"))
        return ResourceID(kind, video_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.kind is not None:
            result["kind"] = from_union([from_str, from_none], self.kind)
        if self.video_id is not None:
            result["videoId"] = from_union([from_str, from_none], self.video_id)
        return result


@dataclass
class Default:
    url: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "Default":
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        width = from_union([from_int, from_none], obj.get("width"))
        height = from_union([from_int, from_none], obj.get("height"))
        return Default(url, width, height)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        return result


@dataclass
class Thumbnails:
    default: Optional[Default] = None
    medium: Optional[Default] = None
    high: Optional[Default] = None
    standard: Optional[Default] = None
    maxres: Optional[Default] = None

    @staticmethod
    def from_dict(obj: Any) -> "Thumbnails":
        assert isinstance(obj, dict)
        default = from_union([Default.from_dict, from_none], obj.get("default"))
        medium = from_union([Default.from_dict, from_none], obj.get("medium"))
        high = from_union([Default.from_dict, from_none], obj.get("high"))
        standard = from_union([Default.from_dict, from_none], obj.get("standard"))
        maxres = from_union([Default.from_dict, from_none], obj.get("maxres"))
        return Thumbnails(default, medium, high, standard, maxres)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.default is not None:
            result["default"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.default
            )
        if self.medium is not None:
            result["medium"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.medium
            )
        if self.high is not None:
            result["high"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.high
            )
        if self.standard is not None:
            result["standard"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.standard
            )
        if self.maxres is not None:
            result["maxres"] = from_union(
                [lambda x: to_class(Default, x), from_none], self.maxres
            )
        return result


@dataclass
class Snippet:
    published_at: Optional[datetime] = None
    channel_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    thumbnails: Optional[Thumbnails] = None
    channel_title: Optional[str] = None
    playlist_id: Optional[str] = None
    position: Optional[int] = None
    resource_id: Optional[ResourceID] = None
    video_owner_channel_title: Optional[str] = None
    video_owner_channel_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Snippet":
        assert isinstance(obj, dict)
        published_at = from_union([from_datetime, from_none], obj.get("publishedAt"))
        channel_id = from_union([from_str, from_none], obj.get("channelId"))
        title = from_union([from_str, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        thumbnails = from_union(
            [Thumbnails.from_dict, from_none], obj.get("thumbnails")
        )
        channel_title = from_union([from_str, from_none], obj.get("channelTitle"))
        playlist_id = from_union([from_str, from_none], obj.get("playlistId"))
        position = from_union([from_int, from_none], obj.get("position"))
        resource_id = from_union(
            [ResourceID.from_dict, from_none], obj.get("resourceId")
        )
        video_owner_channel_title = from_union(
            [from_str, from_none], obj.get("videoOwnerChannelTitle")
        )
        video_owner_channel_id = from_union(
            [from_str, from_none], obj.get("videoOwnerChannelId")
        )
        return Snippet(
            published_at,
            channel_id,
            title,
            description,
            thumbnails,
            channel_title,
            playlist_id,
            position,
            resource_id,
            video_owner_channel_title,
            video_owner_channel_id,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.published_at is not None:
            result["publishedAt"] = from_union(
                [lambda x: x.isoformat(), from_none], self.published_at
            )
        if self.channel_id is not None:
            result["channelId"] = from_union([from_str, from_none], self.channel_id)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.thumbnails is not None:
            result["thumbnails"] = from_union(
                [lambda x: to_class(Thumbnails, x), from_none], self.thumbnails
            )
        if self.channel_title is not None:
            result["channelTitle"] = from_union(
                [from_str, from_none], self.channel_title
            )
        if self.playlist_id is not None:
            result["playlistId"] = from_union([from_str, from_none], self.playlist_id)
        if self.position is not None:
            result["position"] = from_union([from_int, from_none], self.position)
        if self.resource_id is not None:
            result["resourceId"] = from_union(
                [lambda x: to_class(ResourceID, x), from_none], self.resource_id
            )
        if self.video_owner_channel_title is not None:
            result["videoOwnerChannelTitle"] = from_union(
                [from_str, from_none], self.video_owner_channel_title
            )
        if self.video_owner_channel_id is not None:
            result["videoOwnerChannelId"] = from_union(
                [from_str, from_none], self.video_owner_channel_id
            )
        return result


@dataclass
class Item:
    id: Optional[str] = None
    snippet: Optional[Snippet] = None

    @staticmethod
    def from_dict(obj: Any) -> "Item":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        snippet = from_union([Snippet.from_dict, from_none], obj.get("snippet"))
        return Item(id, snippet)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.snippet is not None:
            result["snippet"] = from_union(
                [lambda x: to_class(Snippet, x), from_none], self.snippet
            )
        return result


@dataclass
class PageInfo:
    total_results: Optional[int] = None
    results_per_page: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "PageInfo":
        assert isinstance(obj, dict)
        total_results = from_union([from_int, from_none], obj.get("totalResults"))
        results_per_page = from_union([from_int, from_none], obj.get("resultsPerPage"))
        return PageInfo(total_results, results_per_page)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.total_results is not None:
            result["totalResults"] = from_union(
                [from_int, from_none], self.total_results
            )
        if self.results_per_page is not None:
            result["resultsPerPage"] = from_union(
                [from_int, from_none], self.results_per_page
            )
        return result


@dataclass
class Videos:
    next_page_token: Optional[str] = None
    items: Optional[List[Item]] = None
    page_info: Optional[PageInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> "Videos":
        assert isinstance(obj, dict)
        next_page_token = from_union([from_str, from_none], obj.get("nextPageToken"))
        items = from_union(
            [lambda x: from_list(Item.from_dict, x), from_none], obj.get("items")
        )
        page_info = from_union([PageInfo.from_dict, from_none], obj.get("pageInfo"))
        return Videos(next_page_token, items, page_info)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.next_page_token is not None:
            result["nextPageToken"] = from_union(
                [from_str, from_none], self.next_page_token
            )
        if self.items is not None:
            result["items"] = from_union(
                [lambda x: from_list(lambda x: to_class(Item, x), x), from_none],
                self.items,
            )
        if self.page_info is not None:
            result["pageInfo"] = from_union(
                [lambda x: to_class(PageInfo, x), from_none], self.page_info
            )
        return result


def videos_from_dict(s: Any) -> Videos:
    return Videos.from_dict(s)


def videos_to_dict(x: Videos) -> Any:
    return to_class(Videos, x)


@dataclass
class MatchDetail:
    category: Optional[str] = None
    title: Optional[str] = None
    desc: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "MatchDetail":
        assert isinstance(obj, dict)
        category = from_union([from_str, from_none], obj.get("category"))
        title = from_union([from_str, from_none], obj.get("title"))
        desc = from_union([from_str, from_none], obj.get("desc"))
        return MatchDetail(category, title, desc)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.category is not None:
            result["category"] = from_union([from_str, from_none], self.category)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.desc is not None:
            result["desc"] = from_union([from_str, from_none], self.desc)
        return result


def match_detail_from_dict(s: Any) -> List[MatchDetail]:
    return from_list(MatchDetail.from_dict, s)


def match_detail_to_dict(x: List[MatchDetail]) -> Any:
    return from_list(lambda x: to_class(MatchDetail, x), x)
