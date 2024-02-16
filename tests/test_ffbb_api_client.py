import os
import unittest
from typing import List

from dotenv import load_dotenv

from ffbb_api_client import FFBBApiClient
from ffbb_api_client.api_types import (
    AgendaAndResults,
    Area,
    Championship,
    ClubDetails,
    ClubInfos,
    Commune,
    CompetitionType,
    League,
    Team,
    Videos,
)

load_dotenv()

basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")


class TestFFBBApiClient(unittest.TestCase):
    _known_commune_name: str = "Senas"
    _known_commune: Commune = None
    _known_club_infos: ClubInfos = None
    _known_club_details: ClubDetails = None
    _known_areas: List[Area] = None
    _known_area: Area = None
    _known_leagues: List[League] = None
    _known_league: League = None
    _known_championships: List[Championship] = None
    _known_championship: Championship = None

    _known_teams: List[Team] = None
    _known_team: Team = None

    _known_results: AgendaAndResults = None

    def setUp(self):
        # Initialisation des objects nécessaires pour les tests
        self.api_client = FFBBApiClient(
            basic_auth_user=basic_auth_user, basic_auth_pass=basic_auth_pass
        )

    def setup_method(self, method):
        self.setUp()

    def _get_know_commune(self):
        if not self._known_commune:
            self._known_commune = self.api_client.get_communes(
                self._known_commune_name
            )[0]

        return self._known_commune

    def _get_know_club_infos(self):
        if not self._known_club_infos:
            self._known_club_infos = self.api_client.search_club(
                self._get_know_commune().id
            )[0]

        return self._known_club_infos

    def _get_known_club_details(self):
        if not self._known_club_details:
            self._known_club_details = self.api_client.get_club_details(
                self._get_know_club_infos().id
            )

        return self._known_club_details

    def _get_areas(self):
        if not self._known_areas:
            self._known_areas = self.api_client.get_areas()

        return self._known_areas

    def _get_known_area(self):
        if not self._known_area:
            self._known_area = next(
                area for area in self._get_areas() if area.id == "0013"
            )

        return self._known_area

    def _get_leagues(self):
        if not self._known_leagues:
            self._known_leagues = self.api_client.get_leagues()

        return self._known_leagues

    def _get_known_league(self):
        if not self._known_league:
            self._known_league = next(
                league for league in self._get_leagues() if league.id == "SUD"
            )

        return self._known_league

    def _get_top_championships(self):
        if not self._known_championships:
            self._known_championships = self.api_client.get_top_championships()

        return self._known_championships

    def _get_known_championship(self):
        if not self._known_championship:
            self._known_championship = next(
                championship
                for championship in self._get_top_championships()
                if championship.name == "CHAMPIONNATS DEPARTEMENTAUX"
            )

        return self._known_championship

    def _get_known_teams(self):
        if not self._known_teams:
            self._known_teams = self._get_known_club_details().teams

        return self._known_teams

    def _get_known_team(self):
        if not self._known_team:
            self._known_team = next(
                team
                for team in self._get_known_teams()
                if team.category == "U13"
                and "Division 4" in team.name
                and "Phase 2" in team.name
                and "Poule D" in team.name
            )

        return self._known_team

    def _get_known_results(self):
        if not self._known_results:
            self._known_results = self.api_client.get_results(
                team_id=self._get_known_team().id,
                sub_competition=self._get_known_team().sub_competition,
                team_group=self._get_known_team().group,
            )

        return self._known_results


class Test_GetCommunes(TestFFBBApiClient):
    def test_with_known_name(self):
        result = self._get_know_commune()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Commune)

    def test_with_unknown_name(self):
        query = "Blop"
        result = self.api_client.get_communes(query)
        self.assertIsNone(result)

    def test_with_empty_name(self):
        query = ""
        result = self.api_client.get_communes(query)
        self.assertIsNone(result)


class Test_GetClubDetails(TestFFBBApiClient):
    def test_with_known_id(self):
        result = self._get_known_club_details()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ClubDetails)

    def test_with_unknown_id(self):
        club_id = "unknown_id"
        result = self.api_client.get_club_details(club_id)
        self.assertIsNone(result)

    def test_with_empty_id(self):
        club_id = ""
        result = self.api_client.get_club_details(club_id)
        self.assertIsNone(result)


class Test_SearchClub(TestFFBBApiClient):
    def test_with_known_id_commune(self):
        result = self._get_know_club_infos()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ClubInfos)

    def test_with_unknown_id_commune(self):
        result = self.api_client.search_club(id_cmne="unknown_id")
        self.assertIsNone(result)

    def test_with_empty_id_commune(self):
        result = self.api_client.search_club(id_cmne="")
        self.assertIsNone(result)

    def test_with_known_org_name(self):
        result = self.api_client.search_club(
            org_name=self._get_know_club_infos().nom_org
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_with_unknown_org_name(self):
        result = self.api_client.search_club(org_name="unknown_org_name")
        self.assertIsNone(result)

    def test_with_empty_org_name(self):
        result = self.api_client.search_club(org_name="")
        self.assertIsNone(result)

    def test_with_specific_club_name(self):

        org_names = ["BASSE VALLEE DE L'ARC BC", "MARTIGUES SPORTS"]

        result = [
            self.api_client.search_club(org_name=org_name) for org_name in org_names
        ]
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


class Test_GetAreas(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_areas()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_championship(self):
        result = self.api_client.get_areas(CompetitionType.CHAMPIONSHIP)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_cup(self):
        result = self.api_client.get_areas(CompetitionType.CUP)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)


class Test_GetNews(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_news()

        if result:
            self.assertIsInstance(result, List)
            self.assertGreater(len(result), 0)


class Test_GetVideos(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_videos()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Videos)

    def test_with_known_club_id(self):
        result = self.api_client.get_videos(
            id_cmne=self._get_know_club_infos().commune.id_cmne
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Videos)

    def test_with_unknown_club_id(self):
        result = self.api_client.get_videos(id_cmne=0)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Videos)

    def test_with_with_known_org_name(self):
        result = self.api_client.get_videos(
            org_name=self._get_know_club_infos().nom_org
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Videos)

    def test_with_with_unknown_org_name(self):
        result = self.api_client.get_videos(org_name="test")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Videos)


class Test_GetLeagues(TestFFBBApiClient):
    def test_main(self):
        result = self._get_leagues()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_championship(self):
        result = self.api_client.get_leagues(CompetitionType.CHAMPIONSHIP)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_cup(self):
        result = self.api_client.get_leagues(CompetitionType.CUP)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)


class Test_GetTopChampionships(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_top_championships()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_championship(self):
        result = self.api_client.get_top_championships(CompetitionType.CHAMPIONSHIP)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_cup(self):
        result = self.api_client.get_top_championships(CompetitionType.CUP)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)


class Test_GetLeagueCompetitions(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_league_competitions(self._get_known_league().id)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_with_unknown_id(self):
        result = self.api_client.get_league_competitions(0)
        self.assertIsNone(result)


class Test_GetAreasCompetitions(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_area_competitions(self._get_known_area().id)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_with_unknown_id(self):
        result = self.api_client.get_area_competitions(0)
        self.assertIsNone(result)


class Test_GetResults(TestFFBBApiClient):
    def test_without_parameters(self):
        result = self.api_client.get_results()
        self.assertIsNone(result)

    def test_with_known_team_id(self):
        result = self.api_client.get_results(team_id=self._get_known_team().id)
        self.assertIsNotNone(result)

    def test_with_known_0_team_id(self):
        result = self.api_client.get_results(team_id=0)
        self.assertIsNone(result)

    def test_with_known_sub_competition(self):
        result = self.api_client.get_results(
            sub_competition=self._get_known_team().sub_competition
        )
        self.assertIsNone(result)

    def test_with_known_group(self):
        result = self.api_client.get_results(team_group=self._get_known_team().group)
        self.assertIsNone(result)

    def test_with_known_team_id_sub_competition(self):
        result = self.api_client.get_results(
            team_id=self._get_known_team().id,
            sub_competition=self._get_known_team().sub_competition,
        )
        self.assertIsNotNone(result)

    def test_with_known_team_id_sub_competition_group(self):
        result = self._get_known_results()
        self.assertIsNotNone(result)


class Test_GetMatchDetail(TestFFBBApiClient):
    def test_with_known_match_id(self):
        result = self.api_client.get_match_detail(
            match_id=self._get_known_results().matchs[0].match_id
        )
        self.assertIsNotNone(result)

    def test_with_unknown_match_id(self):
        result = self.api_client.get_match_detail(match_id=0)
        self.assertIsNone(result)
