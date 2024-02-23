from dataclasses import dataclass
from typing import Any, Optional, Union

from .converters import from_float, from_int, from_none, from_str, from_union, to_float


@dataclass
class Standing:
    pos: Optional[Union[int, str]] = None
    points: Optional[Union[int, str]] = None
    day: Optional[Union[int, str]] = None
    win: Optional[Union[int, str]] = None
    lost: Optional[Union[int, str]] = None
    draw: Optional[Union[int, str]] = None
    penalties: Optional[Union[int, str]] = None
    forfeited: Optional[Union[int, str]] = None
    defaults: Optional[Union[int, str]] = None
    arb: Optional[Union[int, str]] = None
    ent: Optional[Union[int, str]] = None
    scored: Optional[Union[int, str]] = None
    conceded: Optional[Union[int, str]] = None
    quotient: Optional[Union[float, str]] = None
    club: Optional[str] = None
    initi: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Standing":
        assert isinstance(obj, dict)
        pos = from_union([from_int, from_str, from_none], obj.get("pos"))
        points = from_union([from_int, from_str, from_none], obj.get("points"))
        day = from_union([from_int, from_str, from_none], obj.get("day"))
        win = from_union([from_int, from_str, from_none], obj.get("win"))
        lost = from_union([from_int, from_str, from_none], obj.get("lost"))
        draw = from_union([from_int, from_str, from_none], obj.get("draw"))
        penalties = from_union([from_int, from_str, from_none], obj.get("penalties"))
        forfeited = from_union([from_int, from_str, from_none], obj.get("forfeited"))
        defaults = from_union([from_int, from_str, from_none], obj.get("defaults"))
        arb = from_union([from_int, from_str, from_none], obj.get("arb"))
        ent = from_union([from_int, from_str, from_none], obj.get("ent"))
        scored = from_union([from_int, from_str, from_none], obj.get("scored"))
        conceded = from_union([from_int, from_str, from_none], obj.get("conceded"))
        quotient = from_union([from_float, from_str, from_none], obj.get("quotient"))
        club = from_union([from_str, from_none], obj.get("club"))
        initi = from_union([from_none, from_str], obj.get("initi"))
        return Standing(
            pos,
            points,
            day,
            win,
            lost,
            draw,
            penalties,
            forfeited,
            defaults,
            arb,
            ent,
            scored,
            conceded,
            quotient,
            club,
            initi,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.pos is not None:
            result["pos"] = from_union([from_int, from_str, from_none], self.pos)
        if self.points is not None:
            result["points"] = from_union([from_int, from_str, from_none], self.points)
        if self.day is not None:
            result["day"] = from_union([from_int, from_str, from_none], self.day)
        if self.win is not None:
            result["win"] = from_union([from_int, from_str, from_none], self.win)
        if self.lost is not None:
            result["lost"] = from_union([from_int, from_str, from_none], self.lost)
        if self.draw is not None:
            result["draw"] = from_union([from_int, from_str, from_none], self.draw)
        if self.penalties is not None:
            result["penalties"] = from_union(
                [from_int, from_str, from_none], self.penalties
            )
        if self.forfeited is not None:
            result["forfeited"] = from_union(
                [from_int, from_str, from_none], self.forfeited
            )
        if self.defaults is not None:
            result["defaults"] = from_union(
                [from_int, from_str, from_none], self.defaults
            )
        if self.arb is not None:
            result["arb"] = from_union([from_int, from_str, from_none], self.arb)
        if self.ent is not None:
            result["ent"] = from_union([from_int, from_str, from_none], self.ent)
        if self.scored is not None:
            result["scored"] = from_union([from_int, from_str, from_none], self.scored)
        if self.conceded is not None:
            result["conceded"] = from_union(
                [from_int, from_str, from_none], self.conceded
            )
        if self.quotient is not None:
            result["quotient"] = from_union(
                [to_float, from_str, from_none], self.quotient
            )
        if self.club is not None:
            result["club"] = from_union([from_str, from_none], self.club)
        if self.initi is not None:
            result["initi"] = from_union([from_none, from_str], self.initi)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Standing):
            return False
        return (
            self.pos == other.pos
            and self.points == other.points
            and self.day == other.day
            and self.win == other.win
            and self.lost == other.lost
            and self.draw == other.draw
            and self.penalties == other.penalties
            and self.forfeited == other.forfeited
            and self.defaults == other.defaults
            and self.arb == other.arb
            and self.ent == other.ent
            and self.scored == other.scored
            and self.conceded == other.conceded
            and self.quotient == other.quotient
            and self.club == other.club
            and self.initi == other.initi
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.pos,
                self.points,
                self.day,
                self.win,
                self.lost,
                self.draw,
                self.penalties,
                self.forfeited,
                self.defaults,
                self.arb,
                self.ent,
                self.scored,
                self.conceded,
                self.quotient,
                self.club,
                self.initi,
            )
        )
