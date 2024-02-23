from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from .converters import from_int, from_none, from_str, from_union
from .score import Score


@dataclass
class Match:
    formatted_date: Optional[datetime] = None
    time: Optional[str] = None
    hometeam: Optional[str] = None
    visitorteam: Optional[str] = None
    score: Optional[Score] = None
    date: Optional[datetime] = None  # Modified property type
    remise: Optional[int] = None
    round: Optional[int] = None
    match_id: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "Match":
        assert isinstance(obj, dict)
        formatted_date_str = from_union([from_int, from_none], obj.get("formattedDate"))
        formatted_date = (
            datetime.fromtimestamp(formatted_date_str) if formatted_date_str else None
        )
        time = from_union([from_str, from_none], obj.get("time"))
        hometeam = from_union([from_str, from_none], obj.get("hometeam"))
        visitorteam = from_union([from_str, from_none], obj.get("visitorteam"))
        score_str = from_union([from_str, from_none], obj.get("score"))
        score = None
        if score_str:
            home_score = None
            visitor_score = None

            try:
                home_score, visitor_score = map(int, score_str.split(" - "))
            except (ValueError, TypeError):
                pass

            score = Score(home_score, visitor_score)

        date_str = from_union([from_str, from_none], obj.get("date"))
        date = (
            datetime.strptime(f"{time} {date_str}", "%H:%M %d/%m/%Y")
            if date_str
            else None
        )
        remise = from_union([from_int, from_none], obj.get("remise"))
        round = from_union([from_int, from_none], obj.get("round"))
        match_id = from_union([from_int, from_none], obj.get("matchId"))
        return Match(
            formatted_date,
            time,
            hometeam,
            visitorteam,
            score,
            date,
            remise,
            round,
            match_id,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.formatted_date is not None:
            result["formattedDate"] = int(self.formatted_date.timestamp())
        if self.time is not None:
            result["time"] = from_union(
                [from_str, from_none], f"{self.date.hour}:{self.date.minute}"
            )
        if self.hometeam is not None:
            result["hometeam"] = from_union([from_str, from_none], self.hometeam)
        if self.visitorteam is not None:
            result["visitorteam"] = from_union([from_str, from_none], self.visitorteam)
        if self.score is not None:
            home = "" if self.score.home is None else self.score.home
            visitor = "" if self.score.visitor is None else self.score.visitor
            result["score"] = from_union([from_str, from_none], f"{home} - {visitor}")
        if self.date is not None:
            result["date"] = self.date.strftime("%d/%m/%Y")
        if self.remise is not None:
            result["remise"] = from_union([from_int, from_none], self.remise)
        if self.round is not None:
            result["round"] = from_union([from_int, from_none], self.round)
        if self.match_id is not None:
            result["matchId"] = from_union([from_int, from_none], self.match_id)
        return result

    @property
    def played(self) -> bool:
        return self.score is not None and self.score.played

    @property
    def is_ghost(self):
        return self.played and self.date.hour == 0 and self.date.minute == 0

    def __eq__(self, other):
        if isinstance(other, Match):
            return (
                self.formatted_date == other.formatted_date
                and self.time == other.time
                and self.hometeam == other.hometeam
                and self.visitorteam == other.visitorteam
                and self.score == other.score
                and self.date == other.date
                and self.remise == other.remise
                and self.round == other.round
                and self.match_id == other.match_id
            )
        return False

    def __hash__(self):
        return hash(
            (
                self.formatted_date,
                self.time,
                self.hometeam,
                self.visitorteam,
                self.score,
                self.date,
                self.remise,
                self.round,
                self.match_id,
            )
        )
