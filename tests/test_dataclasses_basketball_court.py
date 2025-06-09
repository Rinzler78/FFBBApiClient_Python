import unittest
from ffbb_api_client import BasketballCourt


class TestBasketballCourt(unittest.TestCase):
    def test_basketball_court(self):
        data = {
            "numero": None,
            "id": 1,
            "libelle": "Stade Municipal"
        }
        court = BasketballCourt.from_dict(data)
        self.assertIsNone(court.number)
        self.assertEqual(court.id, 1)
        self.assertEqual(court.label, "Stade Municipal")
        self.assertEqual(court, BasketballCourt.from_dict(court.to_dict()))
        self.assertIsInstance(hash(court), int) 