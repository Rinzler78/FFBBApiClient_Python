"""
FFBB API Client - Python client library for interacting with FFBB APIs.

This package provides a comprehensive client for accessing the French Basketball
Federation (FFBB) APIs. It includes:

- FFBBApiClient: Main client class for API interactions
- Model classes: Data structures for API responses
- Helper functions: Utilities for data processing and caching
- Utilities: Core functionality for HTTP requests, logging, and data conversion

Example:
    Basic usage of the FFBB API client:

    >>> from ffbb_api_client import FFBBApiClient, configure_logging
    >>> import logging
    >>>
    >>> # Configure logging
    >>> configure_logging(logging.INFO)
    >>>
    >>> # Create client
    >>> client = FFBBApiClient(
    ...     basic_auth_user="your_user",
    ...     basic_auth_pass="your_pass"
    ... )
    >>>
    >>> # Get areas
    >>> areas = client.get_areas()
    >>> print(f"Found {len(areas)} areas")

Note:
    All public APIs are available through direct imports from this module.
    See the documentation for detailed usage examples and API reference.
"""

from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

# Import main client
from .ffbb_api_client import FFBBApiClient

# Import helper functions
from .helpers.cached_session_helper import default_cached_session
from .helpers.catch_result_helper import CatchResultError, catch_result
from .helpers.club_details_helper import merge_club_details
from .helpers.clubs_infos_helper import create_set_of_clubs
from .helpers.municipalities_helper import create_set_of_municipalities

# Import model classes
from .models.agenda_and_results import AgendaAndResults, agenda_and_results_from_dict
from .models.area import Area, area_from_dict
from .models.basketball_court import BasketballCourt
from .models.category import Category, extract_category
from .models.championship import Championship, championship_from_dict
from .models.club_details import ClubDetails, club_details_from_dict
from .models.club_infos import ClubInfos, club_infos_from_dict
from .models.competition import Competition, competition_from_dict
from .models.competition_type import CompetitionType, extract_competition_type
from .models.day import Day
from .models.default import Default
from .models.field import Field
from .models.geo_location import GeoLocation
from .models.geographical_zone import GeographicalZone, extract_geographical_zone
from .models.group import Group
from .models.history import History
from .models.item import Item
from .models.league import League, league_from_dict
from .models.match import Match
from .models.match_detail import MatchDetail, match_detail_from_dict
from .models.member import Member
from .models.municipality import Municipality, commune_from_dict
from .models.news import News, news_from_dict
from .models.page_info import PageInfo
from .models.practice_offers import PracticeOffers
from .models.resource_id import ResourceID
from .models.score import Score
from .models.season import Season
from .models.sex import Sex, extract_sex
from .models.snippet import Snippet
from .models.standing import Standing
from .models.team import (
    Team,
    extract_division_number,
    extract_phase_number,
    extract_pool_letter,
)
from .models.thumbnails import Thumbnails
from .models.type_association import TypeAssociation
from .models.videos import Videos, videos_from_dict

# Import utility functions
from .utils.converters import (
    from_bool,
    from_datetime,
    from_float,
    from_int,
    from_list,
    from_none,
    from_str,
    from_union,
    to_class,
    to_float,
)
from .utils.http_requests_utils import (
    encode_params,
    http_get,
    http_get_json,
    http_post,
    http_post_json,
    to_json_from_response,
    url_with_params,
)
from .utils.logger import configure_logging, logger

# Export all public API
__all__ = [
    # Main client
    "FFBBApiClient",
    # Helper functions
    "default_cached_session",
    "CatchResultError",
    "catch_result",
    "merge_club_details",
    "create_set_of_clubs",
    "create_set_of_municipalities",
    # Utility functions
    "from_bool",
    "from_datetime",
    "from_float",
    "from_int",
    "from_list",
    "from_none",
    "from_str",
    "from_union",
    "to_class",
    "to_float",
    "encode_params",
    "http_get",
    "http_get_json",
    "http_post",
    "http_post_json",
    "to_json_from_response",
    "url_with_params",
    "configure_logging",
    "logger",
    # Model classes
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

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "ffbb_api_client"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
