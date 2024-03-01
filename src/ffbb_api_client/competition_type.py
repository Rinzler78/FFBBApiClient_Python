from enum import Enum


class CompetitionType(Enum):
    CHAMPIONSHIP = "championship"
    CUP = "cup"


def extract_competition_type(input_str: str) -> CompetitionType:
    input_str = input_str.lower()
    for competition_type in CompetitionType:
        lower_value = competition_type.value.lower()
        if lower_value == input_str or lower_value in input_str:
            return competition_type

    if "coup" in input_str:
        return CompetitionType.CUP

    return CompetitionType.CHAMPIONSHIP
