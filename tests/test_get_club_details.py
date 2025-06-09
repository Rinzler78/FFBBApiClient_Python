from ffbb_api_client import ClubDetails
from tests.test_base import TestFFBBApiClient


class Test_GetClubDetails(TestFFBBApiClient):
    def test_with_known_id(self):
        result = self._get_known_club_details()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ClubDetails)

    def test_with_unknown_id(self):
        club_id = 0
        result = self.api_client.get_club_details(club_id)
        self.assertIsNone(result)

    def test_with_empty_id(self):
        club_id = None
        result = self.api_client.get_club_details(club_id)
        self.assertIsNone(result)
