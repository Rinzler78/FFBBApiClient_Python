from typing import List

from tests.test_base import TestFFBBApiClient


class Test_GetLeagueCompetitions(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_league_competitions(self._get_known_league().id)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_with_unknown_id(self):
        result = self.api_client.get_league_competitions(0)
        self.assertIsNone(result)
