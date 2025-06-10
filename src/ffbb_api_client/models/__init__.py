# Model classes for the FFBB API Client

from .agenda_and_results import AgendaAndResults, agenda_and_results_from_dict
from .area import Area, area_from_dict
from .basketball_court import BasketballCourt
from .category import Category, extract_category
from .championship import Championship, championship_from_dict
from .club_details import ClubDetails, club_details_from_dict
from .club_infos import ClubInfos, club_infos_from_dict
from .competition import Competition, competition_from_dict
from .competition_type import CompetitionType, extract_competition_type
from .day import Day
from .default import Default
from .field import Field
from .geo_location import GeoLocation
from .geographical_zone import GeographicalZone, extract_geographical_zone
from .group import Group
from .history import History
from .item import Item
from .league import League, league_from_dict
from .match import Match
from .match_detail import MatchDetail, match_detail_from_dict
from .member import Member
from .municipality import Municipality, commune_from_dict
from .news import News, news_from_dict
from .page_info import PageInfo
from .practice_offers import PracticeOffers
from .resource_id import ResourceID
from .score import Score
from .season import Season
from .sex import Sex, extract_sex
from .snippet import Snippet
from .standing import Standing
from .team import (
    Team,
    extract_division_number,
    extract_phase_number,
    extract_pool_letter,
)
from .thumbnails import Thumbnails
from .type_association import TypeAssociation
from .videos import Videos, videos_from_dict

__all__ = [
    "AgendaAndResults",
    "agenda_and_results_from_dict",
    "Area",
    "area_from_dict",
    "BasketballCourt",
    "Category",
    "extract_category",
    "Championship",
    "championship_from_dict",
    "ClubDetails",
    "club_details_from_dict",
    "ClubInfos",
    "club_infos_from_dict",
    "Competition",
    "competition_from_dict",
    "CompetitionType",
    "extract_competition_type",
    "Day",
    "Default",
    "Field",
    "GeoLocation",
    "GeographicalZone",
    "extract_geographical_zone",
    "Group",
    "History",
    "Item",
    "League",
    "league_from_dict",
    "Match",
    "MatchDetail",
    "match_detail_from_dict",
    "Member",
    "Municipality",
    "commune_from_dict",
    "News",
    "news_from_dict",
    "PageInfo",
    "PracticeOffers",
    "ResourceID",
    "Score",
    "Season",
    "Sex",
    "extract_sex",
    "Snippet",
    "Standing",
    "Team",
    "extract_division_number",
    "extract_phase_number",
    "extract_pool_letter",
    "Thumbnails",
    "TypeAssociation",
    "Videos",
    "videos_from_dict",
]
