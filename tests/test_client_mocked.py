import unittest
from unittest.mock import patch

from ffbb_api_client import Area, FFBBApiClient, League


class TestFFBBApiClientMocked(unittest.TestCase):
    def setUp(self):
        self.client = FFBBApiClient("u", "p", debug=False)

    @patch("ffbb_api_client.http_post_json")
    def test_get_areas_and_leagues(self, mock_post):
        mock_post.return_value = [{"id": "1", "name": "A"}, {"id": "1", "name": "A"}]
        areas = self.client.get_areas()
        self.assertEqual(len(areas), 1)
        self.assertEqual(areas[0], Area(id="1", name="A"))

        mock_post.return_value = [{"id": "S", "name": "L"}]
        leagues = self.client.get_leagues()
        self.assertEqual(leagues[0], League(id="S", name="L"))

    @patch("ffbb_api_client.http_get_json")
    def test_search_functions(self, mock_get):
        mock_get.return_value = [{"id": 1, "libelle": "City", "idCmne": 1}]
        mun = self.client.search_municipalities("c")
        self.assertEqual(len(mun), 1)
        self.assertEqual(mun[0].municipality_id, 1)

        mock_get.return_value = [{"id": 1, "libelle": "City", "idCmne": 1}]
        res = self.client.search_multiple_municipalities(["a", "b"])
        self.assertEqual(len(res), 1)

        mock_get.return_value = [{"id": 1, "idCmne": 1, "libelle": "Club"}]
        clubs = self.client.search_clubs(id_municipality=1)
        self.assertEqual(len(clubs), 1)

        mock_get.return_value = [{"id": 1, "idCmne": 1, "libelle": "Club"}]
        clubs_multi = self.client.search_multiple_clubs(["Club"])
        self.assertEqual(len(clubs_multi), 1)

    @patch("ffbb_api_client.http_post_json")
    def test_get_club_details(self, mock_post):
        mock_post.side_effect = [
            {"infos": [{"name": "i1"}], "fields": None, "teams": [{"name": "t1"}]},
            {"infos": [{"name": "i2"}], "fields": None, "teams": None},
        ]
        details = self.client.get_club_details(10)
        self.assertEqual(len(details.infos), 2)
        self.assertEqual(len(details.teams), 1)
