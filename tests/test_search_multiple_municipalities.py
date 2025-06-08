from tests.test_base import TestFFBBApiClient
from typing import List


class Test_SearchMultipleMunicipalities(TestFFBBApiClient):
    def test_with_known_name(self):
        result = self.api_client.search_multiple_municipalities(["Senas", "Paris"])
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_with_most_used_letters(self):
        result = self.api_client.search_multiple_municipalities(
            ["a", "e", "i", "o", "u", "y", "b", "l", "m", "s"]
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_with_unknown_name(self):
        result = self.api_client.search_multiple_municipalities(["Blop", "Blap"])
        self.assertIsNone(result)

    def test_with_empty_name(self):
        result = self.api_client.search_multiple_municipalities(["", ""])
        self.assertIsNone(result) 