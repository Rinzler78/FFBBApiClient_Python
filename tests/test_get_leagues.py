from tests.test_base import TestFFBBApiClient
from typing import List
from ffbb_api_client import CompetitionType


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