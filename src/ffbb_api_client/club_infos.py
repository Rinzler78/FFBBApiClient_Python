from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional

from .cartographie import Cartographie
from .commune import Commune
from .converters import (
    from_datetime,
    from_int,
    from_list,
    from_none,
    from_str,
    from_union,
    to_class,
)
from .historique import Historique
from .membre import Membre
from .offre_pratique import OffresPratique
from .salle import Salle
from .type_association import TypeAssociation


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
        commune_club_pro = from_union(
            [Commune.from_dict, from_none], obj.get("communeClubPro")
        )
        salle_club_pro = from_union(
            [Salle.from_dict, from_none], obj.get("salleClubPro")
        )
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
            [TypeAssociation.from_dict, from_none], obj.get("type_association")
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
            obj.get("offre_pratique"),
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
            result["type_association"] = from_union(
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
            result["offre_pratique"] = from_union(
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

    def __eq__(self, other):
        if isinstance(other, ClubInfos):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


def club_infos_from_dict(s: Any) -> List[ClubInfos]:
    return from_list(ClubInfos.from_dict, s)


def club_to_dict(x: List[ClubInfos]) -> Any:
    return from_list(lambda x: to_class(ClubInfos, x), x)
