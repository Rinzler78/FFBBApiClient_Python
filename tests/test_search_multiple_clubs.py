from tests.test_base import TestFFBBApiClient
from typing import List


class Test_SearchMultipleClubs(TestFFBBApiClient):
    def test_with_known_name(self):
        result = self.api_client.search_multiple_clubs(["Senas", "Paris"])
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_with_most_used_letters(self):
        result = self.api_client.search_multiple_clubs(
            [
                "basket",
                "club",
                "ball",
                "basketball",
                "sport",
                "as",
                "entente",
                "ctc",
                "bc",
            ]
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, List)
        self.assertGreater(len(result), 0)

    def test_with_unknown_name(self):
        result = self.api_client.search_multiple_clubs(["Blop", "Blap"])
        self.assertIsNone(result)

    def test_with_empty_name(self):
        result = self.api_client.search_multiple_clubs(["", ""])
        self.assertIsNone(result) 