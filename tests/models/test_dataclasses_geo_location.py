import unittest

from ffbb_api_client import GeoLocation


class TestGeoLocation(unittest.TestCase):
    def test_geo_location(self):
        data = {
            "codePostal": "13100",
            "latitude": 43.5297,
            "longitude": 5.4474,
            "title": "Aix-en-Provence",
            "adress": "Cours Mirabeau",
            "ville": "Aix-en-Provence",
        }
        geo = GeoLocation.from_dict(data)
        self.assertEqual(geo.postal_code, 13100)
        self.assertEqual(geo.latitude, 43.5297)
        self.assertEqual(geo.longitude, 5.4474)
        self.assertEqual(geo.title, "Aix-en-Provence")
        self.assertEqual(geo.adress, "Cours Mirabeau")
        self.assertEqual(geo.city, "Aix-en-Provence")
        self.assertEqual(geo, GeoLocation.from_dict(geo.to_dict()))
        self.assertIsInstance(hash(geo), int)

    def test_geo_location_none(self):
        data = {}
        geo = GeoLocation.from_dict(data)
        self.assertIsNone(geo.postal_code)
        self.assertIsNone(geo.latitude)
        self.assertIsNone(geo.longitude)
        self.assertIsNone(geo.title)
        self.assertIsNone(geo.adress)
        self.assertIsNone(geo.city)
