"""Club details data model for FFBB API responses.

This module contains the ClubDetails dataclass which represents detailed
information about a basketball club, including its facilities, teams, and
general information.
"""

from dataclasses import dataclass
from typing import Any, List, Optional

from ..utils.converters import from_list, from_none, from_union, to_class
from .field import Field
from .team import Team


@dataclass
class ClubDetails:
    """
    Detailed information about a basketball club.

    This class represents comprehensive club data including facilities,
    teams, and general information returned by the FFBB API.

    Attributes:
        infos: List of general information fields about the club.
        fields: List of basketball courts/facilities owned by the club.
        teams: List of teams associated with the club.

    Example:
        >>> club = ClubDetails(
        ...     infos=[Field(name="Address", value="123 Main St")],
        ...     fields=[Field(name="Gym A", value="Indoor Court")],
        ...     teams=[Team(name="Senior Team")]
        ... )
    """

    infos: Optional[List[Field]] = None
    fields: Optional[List[Field]] = None
    teams: Optional[List[Team]] = None

    @staticmethod
    def from_dict(obj: Any) -> "ClubDetails":
        """
        Create a ClubDetails instance from a dictionary.

        Args:
            obj: Dictionary containing club details data from API response.

        Returns:
            ClubDetails instance with parsed data.

        Note:
            Teams are automatically sorted by category, geographical zone,
            sex, division number, and pool letter for consistent ordering.
        """
        assert isinstance(obj, dict)
        infos = from_union(
            [lambda x: from_list(Field.from_dict, x), from_none], obj.get("infos")
        )
        fields = from_union(
            [lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields")
        )
        teams = from_union(
            [lambda x: from_list(Team.from_dict, x), from_none], obj.get("teams")
        )

        if teams:
            teams = sorted(
                teams,
                key=lambda x: (
                    x.category.value if x.category else "",
                    x.geographical_zone.value if x.geographical_zone else "",
                    x.sex.value if x.sex else "",
                    x.division_number if x.division_number is not None else 0,
                    x.pool_letter if x.pool_letter else "",
                ),
            )

        return ClubDetails(infos, fields, teams)

    def to_dict(self) -> dict:
        """Convert the instance to a dictionary."""
        result: dict = {}
        if self.infos is not None:
            result["infos"] = from_union(
                [lambda x: from_list(lambda x: to_class(Field, x), x), from_none],
                self.infos,
            )
        if self.fields is not None:
            result["fields"] = from_union(
                [lambda x: from_list(lambda x: to_class(Field, x), x), from_none],
                self.fields,
            )
        if self.teams is not None:
            result["teams"] = from_union(
                [lambda x: from_list(lambda x: to_class(Team, x), x), from_none],
                self.teams,
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ClubDetails):
            return False
        return (
            self.infos == other.infos
            and self.fields == other.fields
            and self.teams == other.teams
        )

    def __hash__(self) -> int:
        return hash((self.infos, self.fields, self.teams))


def club_details_from_dict(s: Any) -> ClubDetails:
    """
    Create a ClubDetails instance from a dictionary.

    This is a convenience function that calls ClubDetails.from_dict().

    Args:
        s: Dictionary containing club details data from API response.

    Returns:
        ClubDetails instance with parsed data.
    """
    return ClubDetails.from_dict(s)


def club_details_to_dict(x: ClubDetails) -> Any:
    return to_class(ClubDetails, x)
