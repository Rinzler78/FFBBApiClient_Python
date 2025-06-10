from enum import Enum


class GeographicalZone(Enum):
    INTERNATIONAL = "International"
    NATIONAL = "National"
    PRE_NATIONAL = "Pre-National"
    REGIONAL = "Regional"
    PRE_REGIONAL = "Pre-Regional"
    SUD = "Sud"
    DEPARTEMENTAL = "Departemental"


def extract_geographical_zone(input_str: str) -> GeographicalZone:
    input_str = input_str.lower().replace("é", "e")
    # Trier les zones par longueur décroissante pour éviter les collisions
    zones_sorted = sorted(GeographicalZone, key=lambda z: len(z.value), reverse=True)
    for geographical_zone in zones_sorted:
        lower_value = geographical_zone.value.lower()
        if lower_value == input_str or lower_value in input_str:
            return geographical_zone
    return None
