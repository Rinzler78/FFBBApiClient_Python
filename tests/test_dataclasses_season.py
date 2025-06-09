import unittest
from datetime import datetime

from ffbb_api_client.season import Season


class TestSeason(unittest.TestCase):
    def test_season(self):
        data = {
            "actif": "true",
            "id": 2023,
            "code": "S23",
            "libelle": "Saison 2023-2024",
            "debut": "2023-09-01T00:00:00Z",
            "fin": "2024-06-30T00:00:00Z",
        }
        season = Season.from_dict(data)
        self.assertTrue(season.active)
        self.assertEqual(season.id, 2023)
        self.assertEqual(season.code, "S23")
        self.assertEqual(season.label, "Saison 2023-2024")
        self.assertIsInstance(season.start_date, datetime)
        self.assertIsInstance(season.end_date, datetime)
        self.assertEqual(season, Season.from_dict(season.to_dict()))
        self.assertIsInstance(hash(season), int)

    def test_season_none(self):
        data = {}
        season = Season.from_dict(data)
        self.assertIsNone(season.active)
        self.assertIsNone(season.id)
        self.assertIsNone(season.code)
        self.assertIsNone(season.label)
        self.assertIsNone(season.start_date)
        self.assertIsNone(season.end_date)

    def test_season_ffbb(self):
        s = Season(active=True, id=1, code="2023", label="Saison 2023")
        self.assertTrue(s.active)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.code, "2023")
        self.assertEqual(s.label, "Saison 2023")
        self.assertEqual(s, Season(active=True, id=1, code="2023", label="Saison 2023"))
