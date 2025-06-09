from typing import List

from ffbb_api_client import CompetitionType
from tests.test_base import TestFFBBApiClient


class Test_GetTopChampionships(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_top_championships()

        if result is None:
            self.skipTest("Result is None")

        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_championship(self):
        result = self.api_client.get_top_championships(CompetitionType.CHAMPIONSHIP)
        
        if result is None:
            self.skipTest("Result is None")
        
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_cup(self):
        result = self.api_client.get_top_championships(CompetitionType.CUP)

        if result is None:
            self.skipTest("Result is None")

        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

