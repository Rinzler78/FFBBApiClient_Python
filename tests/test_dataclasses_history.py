import unittest
from datetime import datetime
from ffbb_api_client import History, Season, TypeAssociation


class TestHistory(unittest.TestCase):
    def test_history(self):
        data = {
            "cessation": "2022-06-30T00:00:00Z",
            "dateAffiliation": "2020-09-01T00:00:00Z",
            "dateReaffiliation": "2021-09-01T00:00:00Z",
            "saison": {
                "actif": "true",
                "id": 2021,
                "code": "S21",
                "libelle": "Saison 2021-2022",
                "debut": "2021-09-01T00:00:00Z",
                "fin": "2022-06-30T00:00:00Z"
            },
            "creation": "2019-01-01T00:00:00Z",
            "typeAssociation": {
                "id": 1,
                "libelle": "Association principale"
            }
        }
        history = History.from_dict(data)
        self.assertIsInstance(history.cessation, datetime)
        self.assertIsInstance(history.affiliation_date, datetime)
        self.assertIsInstance(history.reaffiliation_date, datetime)
        self.assertIsInstance(history.season, Season)
        self.assertIsInstance(history.creation_date, datetime)
        self.assertIsInstance(history.association_type, TypeAssociation)

    def test_history_none(self):
        data = {}
        history = History.from_dict(data)
        self.assertIsNone(history.cessation)
        self.assertIsNone(history.affiliation_date)
        self.assertIsNone(history.reaffiliation_date)
        self.assertIsNone(history.season)
        self.assertIsNone(history.creation_date)
        self.assertIsNone(history.association_type)

    def test_history_equality(self):
        h = History(cessation=None)
        self.assertIsNone(h.cessation)
        self.assertEqual(h, History(cessation=None)) 