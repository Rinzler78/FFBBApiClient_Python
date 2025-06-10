from enum import Enum


class GeographycaleZone(Enum):
    INTERNATIONAL = "International"
    NATIONAL = "National"
    PRE_NATIONAL = "Pre-National"
    REGIONAL = "Regional"
    PRE_REGIONAL = "Pre-Regional"
    SUD = "Sud"
    DEPARTEMENTAL = "Departemental"


def extract_geographycale_zone(input_str: str) -> GeographycaleZone:
    input_str = input_str.lower().replace("é", "e")
    # Trier les zones par longueur décroissante pour éviter les collisions
    zones_sorted = sorted(GeographycaleZone, key=lambda z: len(z.value), reverse=True)
    for geographycale_zone in zones_sorted:
        lower_value = geographycale_zone.value.lower()
        if lower_value == input_str or lower_value in input_str:
            return geographycale_zone
    return None
