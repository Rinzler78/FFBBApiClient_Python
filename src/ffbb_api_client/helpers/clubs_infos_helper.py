from typing import List

from ..models.club_infos import ClubInfos


def create_set_of_clubs(clubs: List[ClubInfos]) -> List[ClubInfos]:
    """
    Create a set of clubs from a list of ClubInfos.

    Args:
        clubs (List[ClubInfos]): The list of ClubInfos.

    Returns:
        set: The set of clubs.
    """

    if len(clubs) == 1:
        return clubs

    dict_clubs = {}
    for club in clubs:
        try:
            dict_clubs[club.id]

        except KeyError:
            dict_clubs[club.id] = club

    return list(dict_clubs.values())
