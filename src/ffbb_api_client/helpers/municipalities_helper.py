from typing import List

from ..models.municipality import Municipality


def create_set_of_municipalities(
    municipalities: List[Municipality],
) -> List[Municipality]:
    """
    Create a set of municipalities from a list of Municipality.

    Args:
        municipalities (List[Municipality]): The list of Municipality.

    Returns:
        set: The set of municipalities.
    """

    if len(municipalities) == 1:
        return municipalities

    dict_municipalities = {}
    for municipality in municipalities:
        try:
            dict_municipalities[municipality.id]
        except KeyError:
            dict_municipalities[municipality.id] = municipality
    return list(dict_municipalities.values())
