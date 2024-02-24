from dataclasses import dataclass
from typing import Any, Optional

from .converters import from_float, from_none, from_str, from_union, is_type, to_float


@dataclass
class GeoLocation:
    postal_code: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    title: Optional[str] = None
    adress: Optional[str] = None
    city: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "GeoLocation":
        assert isinstance(obj, dict)
        postal_code = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("codePostal")
        )
        latitude = from_union([from_float, from_none], obj.get("latitude"))
        longitude = from_union([from_float, from_none], obj.get("longitude"))
        title = from_union([from_str, from_none], obj.get("title"))
        adress = from_union([from_str, from_none], obj.get("adress"))
        city = from_union([from_str, from_none], obj.get("ville"))
        return GeoLocation(postal_code, latitude, longitude, title, adress, city)

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
        if self.latitude is not None:
            result["latitude"] = from_union([to_float, from_none], self.latitude)
        if self.longitude is not None:
            result["longitude"] = from_union([to_float, from_none], self.longitude)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.adress is not None:
            result["adress"] = from_union([from_str, from_none], self.adress)
        if self.city is not None:
            result["ville"] = from_union([from_str, from_none], self.city)
        return result

    def __eq__(self, other):
        if isinstance(other, GeoLocation):
            return (
                self.postal_code == other.postal_code
                and self.latitude == other.latitude
                and self.longitude == other.longitude
                and self.title == other.title
                and self.adress == other.adress
                and self.city == other.city
            )
        return False

    def __hash__(self):
        return hash(
            (
                self.postal_code,
                self.latitude,
                self.longitude,
                self.title,
                self.adress,
                self.city,
            )
        )
