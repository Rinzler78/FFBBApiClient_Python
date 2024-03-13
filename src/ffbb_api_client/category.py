from enum import Enum


class Category(Enum):
    VETERANS = "Vétérans"
    SENIOR = "Senior"
    JUNIOR = "Junior"
    U20 = "U20"
    U18 = "U18"
    U17 = "U17"
    U15 = "U15"
    U13 = "U13"
    U11 = "U11"
    U9 = "U9"
    U8 = "U8"
    U7 = "U7"


def extract_category(input_str: str) -> Category:
    input_str = input_str.lower().strip()

    if input_str:
        for category in Category:
            lower_value = category.value.lower()
            if lower_value == input_str or lower_value in input_str:
                return category
    return None
