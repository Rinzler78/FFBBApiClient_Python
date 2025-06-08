from tests.test_base import TestFFBBApiClient
from typing import List


class Test_GetAreasCompetitions(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_area_competitions(self._get_known_area().id)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_with_unknown_id(self):
        result = self.api_client.get_area_competitions(0)
        self.assertIsNone(result) 