from enum import Enum


class GeographycaleZone(Enum):
    INTERNATIONAL = "International"
    NATIONAL = "National"
    REGIONAL = "Regional"
    SUD = "Sud"
    DEPARTEMENTAL = "Departemental"


def extract_geographycale_zone(input_str: str) -> GeographycaleZone:
    input_str = input_str.lower().replace("é", "e")
    for geographycale_zone in GeographycaleZone:
        lower_value = geographycale_zone.value.lower()
        if lower_value == input_str or lower_value in input_str:
            return geographycale_zone

    return None
