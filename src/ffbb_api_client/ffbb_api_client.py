import base64
from typing import List

from .ffbb_api_client_types import (
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
        base_url: str = "http://mobiles.ffbb.com/php/v1_0_5/",
        webservices_url: str = "https://mobiles.ffbb.com/webservices/v1/",
    ):
        self.base_url = base_url
        self.webservices_url = webservices_url
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
        id: int = None,
        sub_competition: str = None,
        group: str = None,
        result_type: str = None,
        day: str = None,
    ) -> AgendaAndResults:
        params = {
            "id": id,
            "subCompetition": sub_competition,
            "group": group,
            "type": result_type,
            "day": day,
        }
        url = f"{self.base_url}results.php"
        return self.catch_result(
            lambda: agenda_and_results_from_dict(
                http_post_json(url, self.headers, params)
            )
        )

    def get_club_details(self, id: int) -> ClubDetails:
        params = {"id": id}
        url = f"{self.base_url}club.php"
        return self.catch_result(
            lambda: club_details_from_dict(http_post_json(url, self.headers, params))
        )

    def get_area_competitions(
        self, id: str, type: CompetitionType = None
    ) -> List[Competition]:
        params = {"id": id, "type": type.value if type else None}
        url = f"{self.base_url}areaCompetitions.php"
        return self.catch_result(
            lambda: competition_from_dict(http_post_json(url, self.headers, params))
        )

    def get_league_competitions(
        self, id: str, type: CompetitionType = None
    ) -> List[Competition]:
        params = {"id": id, "type": type.value if type else None}
        url = f"{self.base_url}leagueCompetitions.php"
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
        params = {
            "id": id,
            "subCompetition": sub_competition,
            "group": group,
            "type": result_type,
            "day": day,
            "matchId": match_id,
        }
        url = f"{self.base_url}matchDetail.php"
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
        params = {"idCmne": id_cmne, "nomOrg": org_name}
        url = f"{self.base_url}videos.php"
        return self.catch_result(
            lambda: videos_from_dict(http_post_json(url, self.headers, params))
        )

    def get_news(self) -> List[News]:
        url = f"{self.base_url}news.php"
        return self.catch_result(
            lambda: news_from_dict(http_post_json(url, self.headers))
        )

    def get_areas(self, type: CompetitionType = None) -> List[Area]:
        params = {"type": type.value if type else None}
        url = f"{self.base_url}areas.php"
        return self.catch_result(
            lambda: area_from_dict(http_post_json(url, self.headers, params))
        )

    def get_leagues(self, type: CompetitionType = None) -> List[League]:
        params = {"type": type.value if type else None}
        url = f"{self.base_url}leagues.php"
        return self.catch_result(
            lambda: league_from_dict(http_post_json(url, self.headers, params))
        )

    def get_top_championships(self, type: str = None) -> List[Championship]:
        params = {"type": type}
        url = f"{self.base_url}topChampionships.php"
        return self.catch_result(
            lambda: championship_from_dict(http_post_json(url, self.headers, params))
        )

    def get_communes(self, name: str) -> List[Commune]:
        params = {"name": name}
        url = url_with_params(f"{self.webservices_url}communes.php", params)
        return self.catch_result(
            lambda: commune_from_dict(http_get_json(url, self.headers))
        )

    def search_club(self, id_cmne: int = None, org_name: str = None) -> List[ClubInfos]:
        params = {"idCmne": id_cmne, "nomOrg": org_name}

        url = url_with_params(f"{self.webservices_url}search_club.php", params)
        return self.catch_result(
            lambda: club_infos_from_dict(http_get_json(url, self.headers))
        )

    def catch_result(self, callback):
        try:
            return callback()
        except Exception:
            return None
