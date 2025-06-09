import os
import unittest
from typing import List

from dotenv import load_dotenv

from ffbb_api_client import (
    AgendaAndResults,
    Area,
    Category,
    Championship,
    ClubDetails,
    ClubInfos,
    FFBBApiClient,
    League,
    Municipality,
    Team,
)

load_dotenv()
basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")


class TestFFBBApiClient(unittest.TestCase):
    _known_municipality_name: str = "Senas"
    _known_municipality: Municipality = None
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
        self.api_client = FFBBApiClient(
            basic_auth_user=basic_auth_user,
            basic_auth_pass=basic_auth_pass,
            debug=True,
        )

    def setup_method(self, method):
        self.setUp()

    def _get_know_municipality(self):
        if not self._known_municipality:
            self._known_municipality = self.api_client.search_municipalities(
                self._known_municipality_name
            )[0]
        return self._known_municipality

    def _get_know_club_infos(self):
        if not self._known_club_infos:
            self._known_club_infos = self.api_client.search_clubs(
                self._get_know_municipality().id
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
                if team.category == Category.U13
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
