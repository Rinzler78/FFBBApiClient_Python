from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional

from .basketball_court import BasketballCourt
from .converters import (
    from_datetime,
    from_int,
    from_list,
    from_none,
    from_str,
    from_union,
    to_class,
)
from .geo_location import GeoLocation
from .history import History
from .member import Member
from .municipality import Municipality
from .practice_offers import PracticeOffers
from .type_association import TypeAssociation


@dataclass
class ClubInfos:
    professional_club_name: None
    professional_club_address: None
    professional_club_town: None
    professional_club_court: None
    obe_participation: None
    id: Optional[int] = None
    parent_organization_id: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    adress: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    municipality: Optional[Municipality] = None
    association_type: Optional[TypeAssociation] = None
    court: Optional[BasketballCourt] = None
    url_site_web: Optional[str] = None
    membres: Optional[List[Member]] = None
    child_organizations: Optional[List[Any]] = None
    practice_offers: Optional[List[PracticeOffers]] = None
    certifications: Optional[List[Any]] = None
    geo_location: Optional[GeoLocation] = None
    history: Optional[List[History]] = None
    organization_id: Optional[int] = None
    municipality_id: Optional[int] = None
    organization_code: Optional[str] = None
    organization_name: Optional[str] = None
    affiliation_date: Optional[datetime] = None

    def __eq__(self, other):
        if isinstance(other, ClubInfos):
            return (
                self.professional_club_name == other.professional_club_name
                and self.professional_club_address == other.professional_club_address
                and self.professional_club_town == other.professional_club_town
                and self.professional_club_court == other.professional_club_court
                and self.obe_participation == other.obe_participation
                and self.id == other.id
                and self.parent_organization_id == other.parent_organization_id
                and self.code == other.code
                and self.name == other.name
                and self.type == other.type
                and self.adress == other.adress
                and self.phone == other.phone
                and self.email == other.email
                and self.municipality == other.municipality
                and self.association_type == other.association_type
                and self.court == other.court
                and self.url_site_web == other.url_site_web
                and self.membres == other.membres
                # and self.child_organizations == other.child_organizations
                and self.practice_offers == other.practice_offers
                # and self.certifications == other.certifications
                and self.geo_location == other.geo_location
                and self.history == other.history
                and self.organization_id == other.organization_id
                and self.municipality_id == other.municipality_id
                and self.organization_code == other.organization_code
                and self.organization_name == other.organization_name
                and self.affiliation_date == other.affiliation_date
            )
        return False

    def __hash__(self):
        return hash(
            (
                self.professional_club_name,
                self.professional_club_address,
                self.professional_club_town,
                self.professional_club_court,
                self.obe_participation,
                self.id,
                self.parent_organization_id,
                self.code,
                self.name,
                self.type,
                self.adress,
                self.phone,
                self.email,
                self.municipality,
                self.association_type,
                self.court,
                self.url_site_web,
                # tuple(self.membres) if self.membres is not None else None,
                # (
                #     tuple(self.child_organizations)
                #     if self.child_organizations is not None
                #     else None
                # ),
                (
                    tuple(self.practice_offers)
                    if self.practice_offers is not None
                    else None
                ),
                # (
                #     tuple(self.certifications)
                #     if self.certifications is not None
                #     else None
                # ),
                self.geo_location,
                tuple(self.history) if self.history is not None else None,
                self.organization_id,
                self.municipality_id,
                self.organization_code,
                self.organization_name,
                self.affiliation_date,
            )
        )

    @staticmethod
    def from_dict(obj: Any) -> "ClubInfos":
        assert isinstance(obj, dict)
        professional_club_name = from_union(
            [from_str, from_none], obj.get("nomClubPro")
        )
        adresse_professional_club_addresslub_pro = from_union(
            [from_str, from_none], obj.get("adresseClubPro")
        )
        professional_club_town = from_union(
            [Municipality.from_dict, from_none], obj.get("communeClubPro")
        )
        professional_club_court = from_union(
            [BasketballCourt.from_dict, from_none], obj.get("salleClubPro")
        )
        obe_participation = from_union(
            [from_str, from_none], obj.get("participationOBE")
        )
        id = from_union([from_int, from_none], obj.get("id"))
        parent_organization_id = from_union(
            [from_int, from_none], obj.get("idOrganismePere")
        )
        code = from_union([from_str, from_none], obj.get("code"))
        name = from_union([from_str, from_none], obj.get("nom"))
        type = from_union([from_str, from_none], obj.get("type"))
        adress = from_union([from_str, from_none], obj.get("adresse"))
        phone = from_union([from_str, from_none], obj.get("telephone"))
        email = from_union([from_none, from_str], obj.get("mail"))
        municipality = from_union(
            [Municipality.from_dict, from_none], obj.get("commune")
        )
        association_type = from_union(
            [TypeAssociation.from_dict, from_none], obj.get("type_association")
        )
        court = from_union([BasketballCourt.from_dict, from_none], obj.get("salle"))
        url_site_web = from_union([from_none, from_str], obj.get("urlSiteWeb"))
        members = from_union(
            [lambda x: from_list(Member.from_dict, x), from_none], obj.get("membres")
        )
        child_organizations = from_union(
            [lambda x: from_list(lambda x: x, x), from_none], obj.get("organismeFils")
        )
        practice_offers = from_union(
            [lambda x: from_list(PracticeOffers.from_dict, x), from_none],
            obj.get("offre_pratique"),
        )
        certifications = from_union(
            [lambda x: from_list(lambda x: x, x), from_none], obj.get("labellisation")
        )
        geo_location = from_union(
            [GeoLocation.from_dict, from_none], obj.get("cartographie")
        )
        history = from_union(
            [lambda x: from_list(History.from_dict, x), from_none],
            obj.get("historique"),
        )
        organization_id = from_union([from_int, from_none], obj.get("idOrg"))
        municipality_id = from_union([from_int, from_none], obj.get("idCmne"))
        organization_code = from_union([from_str, from_none], obj.get("cdOrg"))
        organization_name = from_union([from_str, from_none], obj.get("nomOrg"))
        affiliation_date = from_union(
            [from_datetime, from_none], obj.get("dateAffiliation")
        )
        return ClubInfos(
            professional_club_name,
            adresse_professional_club_addresslub_pro,
            professional_club_town,
            professional_club_court,
            obe_participation,
            id,
            parent_organization_id,
            code,
            name,
            type,
            adress,
            phone,
            email,
            municipality,
            association_type,
            court,
            url_site_web,
            members,
            child_organizations,
            practice_offers,
            certifications,
            geo_location,
            history,
            organization_id,
            municipality_id,
            organization_code,
            organization_name,
            affiliation_date,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.professional_club_name is not None:
            result["nomClubPro"] = from_none(self.professional_club_name)
        if self.professional_club_address is not None:
            result["adresseClubPro"] = from_none(self.professional_club_address)
        if self.professional_club_town is not None:
            result["communeClubPro"] = from_none(self.professional_club_town)
        if self.professional_club_court is not None:
            result["salleClubPro"] = from_none(self.professional_club_court)
        if self.obe_participation is not None:
            result["participationOBE"] = from_none(self.obe_participation)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.parent_organization_id is not None:
            result["idOrganismePere"] = from_union(
                [from_int, from_none], self.parent_organization_id
            )
        if self.code is not None:
            result["code"] = from_union([from_str, from_none], self.code)
        if self.name is not None:
            result["nom"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.adress is not None:
            result["adresse"] = from_union([from_str, from_none], self.adress)
        if self.phone is not None:
            result["telephone"] = from_union([from_str, from_none], self.phone)
        if self.email is not None:
            result["mail"] = from_union([from_none, from_str], self.email)
        if self.municipality is not None:
            result["commune"] = from_union(
                [lambda x: to_class(Municipality, x), from_none], self.municipality
            )
        if self.association_type is not None:
            result["type_association"] = from_union(
                [lambda x: to_class(TypeAssociation, x), from_none],
                self.association_type,
            )
        if self.court is not None:
            result["salle"] = from_union(
                [lambda x: to_class(BasketballCourt, x), from_none], self.court
            )
        if self.url_site_web is not None:
            result["urlSiteWeb"] = from_union([from_none, from_str], self.url_site_web)
        if self.membres is not None:
            result["membres"] = from_union(
                [lambda x: from_list(lambda x: to_class(Member, x), x), from_none],
                self.membres,
            )
        if self.child_organizations is not None:
            result["organismeFils"] = from_union(
                [lambda x: from_list(lambda x: x, x), from_none],
                self.child_organizations,
            )
        if self.practice_offers is not None:
            result["offre_pratique"] = from_union(
                [
                    lambda x: from_list(lambda x: to_class(PracticeOffers, x), x),
                    from_none,
                ],
                self.practice_offers,
            )
        if self.certifications is not None:
            result["labellisation"] = from_union(
                [lambda x: from_list(lambda x: x, x), from_none], self.certifications
            )
        if self.geo_location is not None:
            result["cartographie"] = from_union(
                [lambda x: to_class(GeoLocation, x), from_none], self.geo_location
            )
        if self.history is not None:
            result["historique"] = from_union(
                [lambda x: from_list(lambda x: to_class(History, x), x), from_none],
                self.history,
            )
        if self.organization_id is not None:
            result["idOrg"] = from_union([from_int, from_none], self.organization_id)
        if self.municipality_id is not None:
            result["idCmne"] = from_union([from_int, from_none], self.municipality_id)
        if self.organization_code is not None:
            result["cdOrg"] = from_union([from_str, from_none], self.organization_code)
        if self.organization_name is not None:
            result["nomOrg"] = from_union([from_str, from_none], self.organization_name)
        if self.affiliation_date is not None:
            result["dateAffiliation"] = from_union(
                [lambda x: x.isoformat(), from_none], self.affiliation_date
            )
        return result


def club_infos_from_dict(s: Any) -> List[ClubInfos]:
    return from_list(ClubInfos.from_dict, s)


def club_to_dict(x: List[ClubInfos]) -> Any:
    return from_list(lambda x: to_class(ClubInfos, x), x)
