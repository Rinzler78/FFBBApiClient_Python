import unittest

from ffbb_api_client.geographycale_zone import (
    GeographycaleZone,
    extract_geographycale_zone,
)


class TestGeographycaleZone(unittest.TestCase):
    def test_enum(self):
        self.assertEqual(GeographycaleZone.SUD.value, "Sud")
        self.assertEqual(GeographycaleZone.NATIONAL.value, "National")

    def test_extract_geographycale_zone(self):
        self.assertEqual(extract_geographycale_zone("Sud"), GeographycaleZone.SUD)
        self.assertEqual(
            extract_geographycale_zone("National"), GeographycaleZone.NATIONAL
        )
        self.assertIsNone(extract_geographycale_zone("Inconnu"))
