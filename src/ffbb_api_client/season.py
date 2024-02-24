from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from .converters import (
    from_datetime,
    from_int,
    from_none,
    from_str,
    from_stringified_bool,
    from_union,
    is_type,
)


@dataclass
class Season:
    active: Optional[bool] = None
    id: Optional[int] = None
    code: Optional[str] = None
    label: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> "Season":
        assert isinstance(obj, dict)
        active = from_union(
            [from_none, lambda x: from_stringified_bool(from_str(x))], obj.get("actif")
        )
        id = from_union([from_int, from_none], obj.get("id"))
        code = from_union([from_str, from_none], obj.get("code"))
        label = from_union([from_str, from_none], obj.get("libelle"))
        start_date = from_union([from_datetime, from_none], obj.get("debut"))
        end_date = from_union([from_datetime, from_none], obj.get("fin"))
        return Season(active, id, code, label, start_date, end_date)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.active is not None:
            result["actif"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(bool, x))(x)).lower())(x)
                    ),
                ],
                self.active,
            )
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.code is not None:
            result["code"] = from_union([from_str, from_none], self.code)
        if self.label is not None:
            result["libelle"] = from_union([from_str, from_none], self.label)
        if self.start_date is not None:
            result["debut"] = from_union(
                [lambda x: x.isoformat(), from_none], self.start_date
            )
        if self.end_date is not None:
            result["fin"] = from_union(
                [lambda x: x.isoformat(), from_none], self.end_date
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Season):
            return (
                self.active == other.active
                and self.id == other.id
                and self.code == other.code
                and self.label == other.label
                and self.start_date == other.start_date
                and self.end_date == other.end_date
            )
        return False

    def __hash__(self) -> int:
        return hash(
            (
                self.active,
                self.id,
                self.code,
                self.label,
                self.start_date,
                self.end_date,
            )
        )
