from tests.test_base import TestFFBBApiClient
from ffbb_api_client import ClubInfos


class Test_SearchClubs(TestFFBBApiClient):
    def test_with_known_id_municipality(self):
        result = self._get_know_club_infos()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ClubInfos)

    def test_with_unknown_id_municipality(self):
        result = self.api_client.search_clubs(id_municipality="unknown_id")
        self.assertIsNone(result)

    def test_with_empty_id_municipality(self):
        result = self.api_client.search_clubs(id_municipality="")
        self.assertIsNone(result)

    def test_with_known_org_name(self):
        result = self.api_client.search_clubs(
            org_name=self._get_know_club_infos().organization_name
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_with_unknown_org_name(self):
        result = self.api_client.search_clubs(org_name="unknown_org_name")
        self.assertIsNone(result)

    def test_with_empty_org_name(self):
        result = self.api_client.search_clubs(org_name="")
        self.assertIsNone(result)

    def test_with_heavy_results(self):
        result = self.api_client.search_clubs(org_name="B")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0) 