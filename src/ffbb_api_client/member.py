from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_bool, from_int, from_none, from_str, from_union, is_type


@dataclass
class Member:
    id: Optional[int] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[int] = None
    postal_code: Optional[int] = None
    city: Optional[str] = None
    email: Optional[str] = None
    landline_phone: Optional[str] = None
    mobile_phone: Optional[str] = None
    role_code: Optional[str] = None
    role_label: Optional[str] = None
    license_id: Optional[int] = None
    consent_to_website_publishing: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> "Member":
        assert isinstance(obj, dict)
        address_line2 = from_union([from_str, from_none], obj.get("adresse2"))
        postal_code = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("codePostal")
        )
        landline_phone = from_union([from_str, from_none], obj.get("telephoneFixe"))
        id = from_union([from_int, from_none], obj.get("id"))
        last_name = from_union([from_str, from_none], obj.get("nom"))
        first_name = from_union([from_str, from_none], obj.get("prenom"))
        id_licence = from_union([from_int, from_none], obj.get("idLicence"))
        address_line1 = from_union([from_str, from_none], obj.get("adresse1"))
        city = from_union([from_str, from_none], obj.get("ville"))
        email = from_union([from_str, from_none], obj.get("mail"))
        mobile_phone = from_union([from_str, from_none], obj.get("telephonePortable"))
        role_code = from_union([from_str, from_none], obj.get("codeFonction"))
        role_label = from_union([from_str, from_none], obj.get("libelleFonction"))
        consent_to_website_publishing = from_union(
            [from_bool, from_none], obj.get("accordDiffusionSiteWeb")
        )
        return Member(
            id,
            last_name,
            first_name,
            address_line1,
            address_line2,
            postal_code,
            city,
            email,
            landline_phone,
            mobile_phone,
            role_code,
            role_label,
            id_licence,
            consent_to_website_publishing,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.address_line2 is not None:
            result["adresse2"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.address_line2,
            )
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
        if self.landline_phone is not None:
            result["telephoneFixe"] = from_none(self.landline_phone)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.last_name is not None:
            result["nom"] = from_union([from_str, from_none], self.last_name)
        if self.first_name is not None:
            result["prenom"] = from_union([from_str, from_none], self.first_name)
        if self.license_id is not None:
            result["idLicence"] = from_union([from_int, from_none], self.license_id)
        if self.address_line1 is not None:
            result["adresse1"] = from_union([from_str, from_none], self.address_line1)
        if self.city is not None:
            result["ville"] = from_union([from_str, from_none], self.city)
        if self.email is not None:
            result["mail"] = from_union([from_str, from_none], self.email)
        if self.mobile_phone is not None:
            result["telephonePortable"] = from_union(
                [from_str, from_none], self.mobile_phone
            )
        if self.role_code is not None:
            result["codeFonction"] = from_union([from_str, from_none], self.role_code)
        if self.role_label is not None:
            result["libelleFonction"] = from_union(
                [from_str, from_none], self.role_label
            )
        if self.consent_to_website_publishing is not None:
            result["accordDiffusionSiteWeb"] = from_union(
                [from_bool, from_none], self.consent_to_website_publishing
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Member):
            return False
        return (
            self.id == other.id
            and self.last_name == other.last_name
            and self.first_name == other.first_name
            and self.address_line1 == other.address_line1
            and self.address_line2 == other.address_line2
            and self.postal_code == other.postal_code
            and self.city == other.city
            and self.email == other.email
            and self.landline_phone == other.landline_phone
            and self.mobile_phone == other.mobile_phone
            and self.role_code == other.role_code
            and self.role_label == other.role_label
            and self.license_id == other.license_id
            and self.consent_to_website_publishing
            == other.consent_to_website_publishing
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.id,
                self.last_name,
                self.first_name,
                self.address_line1,
                self.address_line2,
                self.postal_code,
                self.city,
                self.email,
                self.landline_phone,
                self.mobile_phone,
                self.role_code,
                self.role_label,
                self.license_id,
                self.consent_to_website_publishing,
            )
        )
