import logging
from enum import Enum

logger = logging.getLogger(__name__)


class Sex(Enum):
    MASCULIN = "Masculin"
    FEMININ = "Féminin"
    MIXTE = "Mixte"


def extract_sex(input_str: str) -> Sex:
    input_str = input_str.lower()
    for sex in Sex:
        lower_value = sex.value.lower()
        if lower_value == input_str or lower_value in input_str:
            return sex
    logger.warning("Unknown sex: %s", input_str)
    return None
