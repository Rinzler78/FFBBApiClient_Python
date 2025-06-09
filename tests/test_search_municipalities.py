from ffbb_api_client import Municipality
from tests.test_base import TestFFBBApiClient


class Test_SearchMunicipalities(TestFFBBApiClient):
    def test_with_known_name(self):
        result = self._get_know_municipality()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Municipality)

    def test_with_unknown_name(self):
        query = "Blop"
        result = self.api_client.search_municipalities(query)
        self.assertIsNone(result)

    def test_with_empty_name(self):
        query = ""
        result = self.api_client.search_municipalities(query)
        self.assertIsNone(result)
