"""
Basketball category classification for FFBB competitions.

This module defines the Category enum which represents different age and skill
categories used in French basketball competitions, from youth categories (U7-U20)
to senior and veteran levels.
"""

from enum import Enum


class Category(Enum):
    """
    Basketball age and skill categories for FFBB competitions.

    This enum defines the standard categories used in French basketball,
    ranging from youth categories (U7 through U20) to senior and veteran
    divisions. Each category represents a specific age group or skill level.

    Values:
        VETERANS: Veteran players category
        SENIOR: Senior/adult players category
        JUNIOR: Junior players category
        U20: Under-20 players category
        U18: Under-18 players category
        U17: Under-17 players category
        U15: Under-15 players category
        U13: Under-13 players category
        U11: Under-11 players category
        U9: Under-9 players category
        U8: Under-8 players category
        U7: Under-7 players category

    Example:
        >>> category = Category.U15
        >>> print(category.value)
        'U15'
        >>> veteran_cat = Category.VETERANS
        >>> print(veteran_cat.value)
        'Vétérans'
    """

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
