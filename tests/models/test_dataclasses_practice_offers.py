import unittest

from ffbb_api_client import PracticeOffers


class TestPracticeOffers(unittest.TestCase):
    def test_practice_offers(self):
        data = {"id": 1, "typePratique": "Basket Loisir", "categoriePratique": "Adulte"}
        offer = PracticeOffers.from_dict(data)
        self.assertEqual(offer.id, 1)
        self.assertEqual(offer.type, "Basket Loisir")
        self.assertEqual(offer.category, "Adulte")
        self.assertEqual(offer, PracticeOffers.from_dict(offer.to_dict()))
        self.assertIsInstance(hash(offer), int)
