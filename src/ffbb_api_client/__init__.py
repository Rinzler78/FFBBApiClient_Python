from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

from .agenda_and_results import AgendaAndResults, agenda_and_results_from_dict  # noqa
from .ffbb_api_client import FFBBApiClient  # noqa
from .area import Area, area_from_dict  # noqa
from .basketball_court import BasketballCourt  # noqa

# Import du cache helper
from .cached_session_helper import default_cached_session  # noqa
from .catch_result_helper import catch_result, CatchResultError  # noqa
from .category import Category  # noqa
from .championship import Championship, championship_from_dict  # noqa
from .club_details import ClubDetails, club_details_from_dict  # noqa
from .club_details_helper import merge_club_details  # noqa
from .club_infos import ClubInfos, club_infos_from_dict  # noqa
from .clubs_infos_helper import create_set_of_clubs  # noqa
from .competition import Competition, competition_from_dict  # noqa
from .competition_type import CompetitionType  # noqa
from .day import Day  # noqa
from .default import Default  # noqa
from .field import Field  # noqa
from .geo_location import GeoLocation  # noqa
from .geographical_zone import GeographycaleZone  # noqa
from .group import Group  # noqa
from .history import History  # noqa
from .http_requests_utils import http_get_json, http_post_json, url_with_params  # noqa
from .item import Item  # noqa
from .league import League, league_from_dict  # noqa
from .logger import configure_logging, logger  # noqa
from .match import Match  # noqa
from .match_detail import MatchDetail, match_detail_from_dict  # noqa
from .member import Member  # noqa
from .municipalities_helper import create_set_of_municipalities  # noqa
from .municipality import Municipality, commune_from_dict  # noqa
from .news import News, news_from_dict  # noqa
from .page_info import PageInfo  # noqa
from .practice_offers import PracticeOffers  # noqa
from .resource_id import ResourceID  # noqa
from .score import Score  # noqa
from .season import Season  # noqa
from .sex import Sex  # noqa
from .snippet import Snippet  # noqa
from .standing import Standing  # noqa
from .team import Team  # noqa
from .thumbnails import Thumbnails  # noqa
from .type_association import TypeAssociation  # noqa
from .videos import Videos, videos_from_dict  # noqa

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "ffbb_api_client"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
