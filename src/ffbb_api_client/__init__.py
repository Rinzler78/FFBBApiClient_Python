import base64
import json
import sys
from typing import List

from requests.exceptions import ConnectionError, ReadTimeout
from requests_cache import CachedSession

from .agenda_and_results import AgendaAndResults, agenda_and_results_from_dict  # noqa
from .area import Area, area_from_dict  # noqa
from .basketball_court import BasketballCourt  # noqa
from .category import Category  # noqa
from .championship import Championship, championship_from_dict  # noqa
from .club_details import ClubDetails, club_details_from_dict  # noqa
from .club_infos import ClubInfos, club_infos_from_dict  # noqa
from .competition import Competition, competition_from_dict  # noqa
from .competition_type import CompetitionType  # noqa
from .day import Day  # noqa
from .default import Default  # noqa
from .field import Field  # noqa
from .geo_location import GeoLocation  # noqa
from .geographycale_zone import GeographycaleZone  # noqa
from .group import Group  # noqa
from .history import History  # noqa
from .http_requests_utils import http_get_json, http_post_json, url_with_params  # noqa
from .item import Item  # noqa
from .league import League, league_from_dict  # noqa
from .match import Match  # noqa
from .match_detail import MatchDetail, match_detail_from_dict  # noqa
from .member import Member  # noqa
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

# Default cached session sqlite backend with 30 minutes expiration
default_cached_session = CachedSession(
    "http_cache", backend="sqlite", expire_after=1800, allowable_methods=("GET", "POST")
)

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "ffbb_api_client"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError


def catch_result(callback, is_retrieving: bool = False):
    """
    Catch the result of a callback function.

    Args:
        callback: The callback function.

    Returns:
        The result of the callback function or None if an exception occurs.
    """

    try:
        return callback()
    except json.decoder.JSONDecodeError as e:
        if e.msg == "Expecting value":
            return None
        raise e
    except ReadTimeout as e:
        if not is_retrieving:
            return catch_result(callback, True)
        raise e
    except ConnectionError as e:
        if not is_retrieving:
            return catch_result(callback, True)
        raise e
    except Exception as e:
        raise e


def merge_club_details(
    club_details: ClubDetails, other_club_details: ClubDetails
) -> ClubDetails:
    """
    Merge two club details.

    Args:
        club_details (ClubDetails): The club details.
        other_club_details (ClubDetails): The other club details.

    Returns:
        ClubDetails: The merged club details.
    """
    if club_details == other_club_details:
        return club_details
    if club_details is None:
        return other_club_details
    if other_club_details is None:
        return club_details

    results = ClubDetails()

    if club_details.fields is not None and other_club_details.fields is not None:
        results.fields = set(club_details.fields + other_club_details.fields)
    elif club_details.fields is not None:
        results.fields = set(club_details.fields)
    elif other_club_details.fields is not None:
        results.fields = set(other_club_details.fields)
    else:
        results.fields = set()

    if club_details.infos is not None and other_club_details.infos is not None:
        results.infos = set(club_details.infos + other_club_details.infos)
    elif club_details.infos is not None:
        results.infos = set(club_details.infos)
    elif other_club_details.infos is not None:
        results.infos = set(other_club_details.infos)
    else:
        results.infos = set()

    if club_details.teams is not None and other_club_details.teams is not None:
        results.teams = set(club_details.teams + other_club_details.teams)
    elif club_details.teams is not None:
        results.teams = set(club_details.teams)
    elif other_club_details.teams is not None:
        results.teams = set(other_club_details.teams)
    else:
        results.teams = set()

    results.teams = sorted(
        results.teams,
        key=lambda team: team.name,
    )

    return results


class FFBBApiClient:
    def __init__(
        self,
        basic_auth_user: str,
        basic_auth_pass: str,
        api_url: str = "https://mobiles.ffbb.com/php/v1_0_5/",
        ws_url: str = "https://mobiles.ffbb.com/webservices/v1/",
        debug: bool = False,
    ):
        """
        Initializes the FFBBApiClient.

        Args:
            basic_auth_user (str): The basic authentication username.
            basic_auth_pass (str): The basic authentication password.
            api_url (str, optional): API url.
            ws_url (str, optional): Webservices URL.
            debug (bool, optional): Enable debug mode.
        """
        self.api_url = api_url
        self.ws_url = ws_url
        self.basic_auth_user = basic_auth_user
        self.basic_auth_pass = basic_auth_pass
        self.headers = {
            "Authorization": "Basic "
            + base64.b64encode(
                f"{self.basic_auth_user}:{self.basic_auth_pass}".encode()
            ).decode()
        }
        self.debug = debug

    def get_results(
        self,
        team_id: int = None,
        sub_competition: str = None,
        team_group: str = None,
        result_type: str = None,
        day: str = None,
        cached_session: CachedSession = default_cached_session,
    ) -> AgendaAndResults:
        """
        Get the agenda and results.

        Args:
            team_id (int, optional): The ID of the team.
            sub_competition (str, optional): The sub-competition.
            team_group (str, optional): The group of the team.
            result_type (str, optional): The type of the result.
            day (str, optional): The day of the result.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            AgendaAndResults: The agenda and results.
        """
        params = {
            "id": team_id,
            "subCompetition": sub_competition,
            "group": team_group,
            "type": result_type,
            "day": day,
        }
        url = f"{self.api_url}results.php"
        return catch_result(
            lambda: agenda_and_results_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def get_club_details(
        self, club_id: int, cached_session: CachedSession = default_cached_session
    ) -> ClubDetails:
        """
        Get the details of a club.

        Args:
            club_id (int): The ID of the club.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            ClubDetails: The details of the club.
        """

        if club_id is None:
            return None

        result = merge_club_details(
            self._get_club_details_with_param(club_id, cached_session=cached_session),
            self._get_club_details_with_param(
                hex(club_id)[2:], cached_session=cached_session
            ),
        )
        return result

    def _get_club_details_with_param(
        self, club_id, cached_session: CachedSession = default_cached_session
    ) -> ClubDetails:
        """
        Get the details of a club.

        Args:
            club_id (int): The ID of the club.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            ClubDetails: The details of the club.
        """

        params = {"id": club_id if club_id else None}
        url = f"{self.api_url}club.php"
        return catch_result(
            lambda: club_details_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def get_area_competitions(
        self,
        area_id: str,
        competition_type: CompetitionType = None,
        cached_session: CachedSession = default_cached_session,
    ) -> List[Competition]:
        """
        Get the competitions in an area.

        Args:
            area_id (str): The ID of the area.
            competition_type (CompetitionType, optional): The type of the competition.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            List[Competition]: The competitions in the area.
        """
        params = {
            "id": area_id,
            "type": competition_type.value if competition_type else None,
        }
        url = f"{self.api_url}areaCompetitions.php"
        return catch_result(
            lambda: competition_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def get_league_competitions(
        self,
        league_id: str,
        competition_type: CompetitionType = None,
        cached_session: CachedSession = default_cached_session,
    ) -> List[Competition]:
        """
        Get the competitions in a league.

        Args:
            league_id (str): The ID of the league.
            competition_type (CompetitionType, optional): The type of the competition.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            List[Competition]: The competitions in the league.
        """
        params = {
            "id": league_id,
            "type": competition_type.value if competition_type else None,
        }
        url = f"{self.api_url}leagueCompetitions.php"
        return catch_result(
            lambda: competition_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def get_match_detail(
        self,
        match_id: int,
        id: str = None,
        sub_competition: str = None,
        group: str = None,
        result_type: str = None,
        day: str = None,
        cached_session: CachedSession = default_cached_session,
    ) -> MatchDetail:
        """
        Get the details of a match.

        Args:
            match_id (int): The ID of the match.
            id (str, optional): The ID of the match.
            sub_competition (str, optional): The sub-competition of the match.
            group (str, optional): The group of the match.
            result_type (str, optional): The type of the result.
            day (str, optional): The day of the result.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            MatchDetail: The details of the match.
        """
        params = {
            "id": id,
            "subCompetition": sub_competition,
            "group": group,
            "type": result_type,
            "day": day,
            "matchId": match_id,
        }
        url = f"{self.api_url}matchDetail.php"
        return catch_result(
            lambda: match_detail_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def get_videos(
        self,
        id_cmne: str = None,
        org_name: str = None,
        cached_session: CachedSession = default_cached_session,
    ) -> Videos:
        """
        Get the videos.

        Args:
            id_cmne (str, optional): The ID of the commune.
            org_name (str, optional): The name of the organization.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            Videos: The videos.
        """
        params = {"idCmne": id_cmne, "nomOrg": org_name}
        url = f"{self.api_url}videos.php"
        return catch_result(
            lambda: videos_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def get_news(
        self, cached_session: CachedSession = default_cached_session
    ) -> List[News]:
        """
        Get the news.

        Returns:
            List[News]: The news.
        """
        url = f"{self.api_url}news.php"
        return catch_result(
            lambda: news_from_dict(
                http_post_json(url, self.headers, cached_session=cached_session)
            )
        )

    def get_areas(
        self,
        competition_type: CompetitionType = None,
        cached_session: CachedSession = default_cached_session,
    ) -> List[Area]:
        """
        Get the areas.

        Args:
            competition_type (CompetitionType, optional): The type of the competition.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            List[Area]: The areas.
        """
        params = {"type": competition_type.value if competition_type else None}
        url = f"{self.api_url}areas.php"
        return catch_result(
            lambda: area_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def get_leagues(
        self,
        competition_type: CompetitionType = None,
        cached_session: CachedSession = default_cached_session,
    ) -> List[League]:
        """
        Get the leagues.

        Args:
            competition_type (CompetitionType, optional): The type of the competition.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            List[League]: The leagues.
        """
        params = {"type": competition_type.value if competition_type else None}
        url = f"{self.api_url}leagues.php"
        return catch_result(
            lambda: league_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def get_top_championships(
        self,
        championship_type: str = None,
        cached_session: CachedSession = default_cached_session,
    ) -> List[Championship]:
        """
        Get the top championships.

        Args:
            championship_type (str, optional): The type of the championship.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            List[Championship]: The top championships.
        """
        params = {"type": championship_type}
        url = f"{self.api_url}topChampionships.php"
        return catch_result(
            lambda: championship_from_dict(
                http_post_json(
                    url,
                    self.headers,
                    params,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def search_municipalities(
        self, name: str, cached_session: CachedSession = default_cached_session
    ) -> List[Municipality]:
        """
        Search for a municipality by name.

        Args:
            name (str): The name of the municipality to search for.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            List[Municipality]: A list of Municipality.
        """
        params = {"name": name}
        url = url_with_params(f"{self.ws_url}communes.php", params)
        return catch_result(
            lambda: commune_from_dict(
                http_get_json(
                    url,
                    self.headers,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )

    def search_clubs(
        self,
        id_cmne: int = None,
        org_name: str = None,
        cached_session: CachedSession = default_cached_session,
    ) -> List[ClubInfos]:
        """
        Search for a club.

        Args:
            id_cmne (int, optional): The ID of the commune.
            org_name (str, optional): The name of the organization.
            cached_session (CachedSession, optional): Enable caching.

        Returns:
            List[ClubInfos]: The club information.
        """
        params = {"idCmne": id_cmne, "nomOrg": org_name}

        url = url_with_params(f"{self.ws_url}search_club.php", params)
        return catch_result(
            lambda: club_infos_from_dict(
                http_get_json(
                    url,
                    self.headers,
                    debug=self.debug,
                    cached_session=cached_session,
                )
            )
        )
