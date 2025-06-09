from typing import List

from ffbb_api_client import CompetitionType
from tests.test_base import TestFFBBApiClient


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
