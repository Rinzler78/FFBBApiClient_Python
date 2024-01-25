import base64
import sys
from typing import List

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

from .api_types import (
    AgendaAndResults,
    Area,
    Championship,
    ClubDetails,
    ClubInfos,
    Commune,
    Competition,
    CompetitionType,
    League,
    MatchDetail,
    News,
    Videos,
    agenda_and_results_from_dict,
    area_from_dict,
    championship_from_dict,
    club_details_from_dict,
    club_infos_from_dict,
    commune_from_dict,
    competition_from_dict,
    league_from_dict,
    match_detail_from_dict,
    news_from_dict,
    videos_from_dict,
)
from .http_requests_utils import http_get_json, http_post_json, url_with_params


class FFBBApiClient:
    def __init__(
        self,
        basic_auth_user: str,
        basic_auth_pass: str,
        api_url: str = "http://mobiles.ffbb.com/php/v1_0_5/",
        ws_url: str = "https://mobiles.ffbb.com/webservices/v1/",
    ):
        """
        Initializes the FFBBApiClient.

        Args:
            basic_auth_user (str): The basic authentication username.
            basic_auth_pass (str): The basic authentication password.
            api_url (str, optional): API url.
            ws_url (str, optional): Webservices URL.
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

    def get_results(
        self,
        team_id: int = None,
        sub_competition: str = None,
        team_group: str = None,
        result_type: str = None,
        day: str = None,
    ) -> AgendaAndResults:
        """
        Get the agenda and results.

        Args:
            team_id (int, optional): The ID of the team.
            sub_competition (str, optional): The sub-competition.
            team_group (str, optional): The group of the team.
            result_type (str, optional): The type of the result.
            day (str, optional): The day of the result.

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
        return self.catch_result(
            lambda: agenda_and_results_from_dict(
                http_post_json(url, self.headers, params)
            )
        )

    def get_club_details(self, club_id: int) -> ClubDetails:
        """
        Get the details of a club.

        Args:
            club_id (int): The ID of the club.

        Returns:
            ClubDetails: The details of the club.
        """
        params = {"id": club_id}
        url = f"{self.api_url}club.php"
        return self.catch_result(
            lambda: club_details_from_dict(http_post_json(url, self.headers, params))
        )

    def get_area_competitions(
        self, area_id: str, competition_type: CompetitionType = None
    ) -> List[Competition]:
        """
        Get the competitions in an area.

        Args:
            area_id (str): The ID of the area.
            competition_type (CompetitionType, optional): The type of the competition.

        Returns:
            List[Competition]: The competitions in the area.
        """
        params = {
            "id": area_id,
            "type": competition_type.value if competition_type else None,
        }
        url = f"{self.api_url}areaCompetitions.php"
        return self.catch_result(
            lambda: competition_from_dict(http_post_json(url, self.headers, params))
        )

    def get_league_competitions(
        self, league_id: str, competition_type: CompetitionType = None
    ) -> List[Competition]:
        """
        Get the competitions in a league.

        Args:
            league_id (str): The ID of the league.
            competition_type (CompetitionType, optional): The type of the competition.

        Returns:
            List[Competition]: The competitions in the league.
        """
        params = {
            "id": league_id,
            "type": competition_type.value if competition_type else None,
        }
        url = f"{self.api_url}leagueCompetitions.php"
        return self.catch_result(
            lambda: competition_from_dict(http_post_json(url, self.headers, params))
        )

    # def get_lives(self) -> dict:
    #     url = f"{self.base_url}lives.php"
    #     return self.catch_result(lambda: http_post_json(url, self.headers))

    def get_match_detail(
        self,
        match_id: int,
        id: str = None,
        sub_competition: str = None,
        group: str = None,
        result_type: str = None,
        day: str = None,
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
        return self.catch_result(
            lambda: match_detail_from_dict(http_post_json(url, self.headers, params))
        )

    # def get_actu(self, url: str = None) -> dict:
    #     params = {
    #         "url": url
    #     }
    #     url = f"{self.base_url}actu.php"
    #     return self.catch_result(lambda: http_post_json(url, self.headers, params))

    def get_videos(self, id_cmne: str = None, org_name: str = None) -> Videos:
        """
        Get the videos.

        Args:
            id_cmne (str, optional): The ID of the commune.
            org_name (str, optional): The name of the organization.

        Returns:
            Videos: The videos.
        """
        params = {"idCmne": id_cmne, "nomOrg": org_name}
        url = f"{self.api_url}videos.php"
        return self.catch_result(
            lambda: videos_from_dict(http_post_json(url, self.headers, params))
        )

    def get_news(self) -> List[News]:
        """
        Get the news.

        Returns:
            List[News]: The news.
        """
        url = f"{self.api_url}news.php"
        return self.catch_result(
            lambda: news_from_dict(http_post_json(url, self.headers))
        )

    def get_areas(self, competition_type: CompetitionType = None) -> List[Area]:
        """
        Get the areas.

        Args:
            competition_type (CompetitionType, optional): The type of the competition.

        Returns:
            List[Area]: The areas.
        """
        params = {"type": competition_type.value if competition_type else None}
        url = f"{self.api_url}areas.php"
        return self.catch_result(
            lambda: area_from_dict(http_post_json(url, self.headers, params))
        )

    def get_leagues(self, competition_type: CompetitionType = None) -> List[League]:
        """
        Get the leagues.

        Args:
            competition_type (CompetitionType, optional): The type of the competition.

        Returns:
            List[League]: The leagues.
        """
        params = {"type": competition_type.value if competition_type else None}
        url = f"{self.api_url}leagues.php"
        return self.catch_result(
            lambda: league_from_dict(http_post_json(url, self.headers, params))
        )

    def get_top_championships(
        self, championship_type: str = None
    ) -> List[Championship]:
        """
        Get the top championships.

        Args:
            championship_type (str, optional): The type of the championship.

        Returns:
            List[Championship]: The top championships.
        """
        params = {"type": championship_type}
        url = f"{self.api_url}topChampionships.php"
        return self.catch_result(
            lambda: championship_from_dict(http_post_json(url, self.headers, params))
        )

    def get_communes(self, name: str) -> List[Commune]:
        """
        Get the communes.

        Args:
            name (str): The name of the commune.

        Returns:
            List[Commune]: The communes.
        """
        params = {"name": name}
        url = url_with_params(f"{self.ws_url}communes.php", params)
        return self.catch_result(
            lambda: commune_from_dict(http_get_json(url, self.headers))
        )

    def search_club(self, id_cmne: int = None, org_name: str = None) -> List[ClubInfos]:
        """
        Search for a club.

        Args:
            id_cmne (int, optional): The ID of the commune.
            org_name (str, optional): The name of the organization.

        Returns:
            List[ClubInfos]: The club information.
        """
        params = {"idCmne": id_cmne, "nomOrg": org_name}

        url = url_with_params(f"{self.ws_url}search_club.php", params)
        return self.catch_result(
            lambda: club_infos_from_dict(http_get_json(url, self.headers))
        )

    def catch_result(self, callback):
        """
        Catch the result of a callback function.

        Args:
            callback: The callback function.

        Returns:
            The result of the callback function or None if an exception occurs.
        """
        try:
            return callback()
        except Exception:
            return None
