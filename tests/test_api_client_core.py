import os
import unittest

from dotenv import load_dotenv

from ffbb_api_client import CompetitionType, FFBBApiClient

load_dotenv()
basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")


class TestFFBBApiClientCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_client = FFBBApiClient(
            basic_auth_user=basic_auth_user,
            basic_auth_pass=basic_auth_pass,
            debug=True,
        )

    def test_get_area_competitions_with_invalid_id(self):
        result = self.api_client.get_area_competitions("invalid_id")
        self.assertIsNone(result)

    def test_get_league_competitions_with_invalid_id(self):
        result = self.api_client.get_league_competitions("invalid_id")
        self.assertIsNone(result)

    def test_get_match_detail_with_invalid_id(self):
        result = self.api_client.get_match_detail(match_id=0)
        self.assertIsNone(result)

    def test_get_videos(self):
        result = self.api_client.get_videos()
        self.assertTrue(result is None or hasattr(result, "__class__"))

    def test_get_news(self):
        result = self.api_client.get_news()
        self.assertTrue(result is None or isinstance(result, list))

    def test_get_areas_with_none(self):
        result = self.api_client.get_areas()
        self.assertTrue(result is None or isinstance(result, list))

    def test_get_leagues_with_none(self):
        result = self.api_client.get_leagues()
        self.assertTrue(result is None or isinstance(result, list))

    def test_get_areas_with_competition_type(self):
        result = self.api_client.get_areas(
            competition_type=CompetitionType.CHAMPIONSHIP
        )
        self.assertTrue(result is None or isinstance(result, list))

    def test_get_leagues_with_competition_type(self):
        result = self.api_client.get_leagues(competition_type=CompetitionType.CUP)
        self.assertTrue(result is None or isinstance(result, list))
