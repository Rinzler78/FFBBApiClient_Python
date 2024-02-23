from dataclasses import dataclass
from typing import Any, List, Optional

from .converters import from_int, from_list, from_none, from_union, to_class
from .day import Day
from .group import Group
from .match import Match
from .standing import Standing


@dataclass
class AgendaAndResults:
    sub_competitions: Optional[List[Group]] = None
    groups: Optional[List[Group]] = None
    days: Optional[List[Day]] = None
    current_day: Optional[int] = None
    matchs: Optional[List[Match]] = None
    standings: Optional[List[Standing]] = None

    @staticmethod
    def from_dict(obj: Any) -> "AgendaAndResults":
        assert isinstance(obj, dict)
        sub_competitions = from_union(
            [lambda x: from_list(Group.from_dict, x), from_none],
            obj.get("subCompetitions"),
        )
        groups = from_union(
            [lambda x: from_list(Group.from_dict, x), from_none], obj.get("groups")
        )
        days = from_union(
            [lambda x: from_list(Day.from_dict, x), from_none], obj.get("days")
        )
        current_day = from_union([from_int, from_none], obj.get("currentDay"))
        matchs = from_union(
            [lambda x: from_list(Match.from_dict, x), from_none], obj.get("matchs")
        )
        standings = from_union(
            [lambda x: from_list(Standing.from_dict, x), from_none],
            obj.get("standings"),
        )
        return AgendaAndResults(
            sub_competitions, groups, days, current_day, matchs, standings
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.sub_competitions is not None:
            result["subCompetitions"] = from_union(
                [lambda x: from_list(lambda x: to_class(Group, x), x), from_none],
                self.sub_competitions,
            )
        if self.groups is not None:
            result["groups"] = from_union(
                [lambda x: from_list(lambda x: to_class(Group, x), x), from_none],
                self.groups,
            )
        if self.days is not None:
            result["days"] = from_union(
                [lambda x: from_list(lambda x: to_class(Day, x), x), from_none],
                self.days,
            )
        if self.current_day is not None:
            result["currentDay"] = from_union([from_int, from_none], self.current_day)
        if self.matchs is not None:
            result["matchs"] = from_union(
                [lambda x: from_list(lambda x: to_class(Match, x), x), from_none],
                self.matchs,
            )
        if self.standings is not None:
            result["standings"] = from_union(
                [lambda x: from_list(lambda x: to_class(Standing, x), x), from_none],
                self.standings,
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AgendaAndResults):
            return False
        return (
            self.sub_competitions == other.sub_competitions
            and self.groups == other.groups
            and self.days == other.days
            and self.current_day == other.current_day
            and self.matchs == other.matchs
            and self.standings == other.standings
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.sub_competitions,
                self.groups,
                self.days,
                self.current_day,
                self.matchs,
                self.standings,
            )
        )


def agenda_and_results_from_dict(s: Any) -> AgendaAndResults:
    return AgendaAndResults.from_dict(s)


def agenda_and_results_to_dict(x: AgendaAndResults) -> Any:
    return to_class(AgendaAndResults, x)
