import unittest

from ffbb_api_client.geographical_zone import (
    GeographycaleZone,
    extract_geographycale_zone,
)


class TestGeographycaleZone(unittest.TestCase):
    def test_enum(self):
        self.assertEqual(GeographycaleZone.SUD.value, "Sud")
        self.assertEqual(GeographycaleZone.NATIONAL.value, "National")

    def test_extract_geographycale_zone(self):
        # Sud
        self.assertEqual(
            extract_geographycale_zone("La zone est Sud"),
            GeographycaleZone.SUD,
        )
        self.assertEqual(
            extract_geographycale_zone("Sud"),
            GeographycaleZone.SUD,
        )
        # National
        self.assertEqual(
            extract_geographycale_zone("Compétition Nationale"),
            GeographycaleZone.NATIONAL,
        )
        self.assertEqual(
            extract_geographycale_zone("National"),
            GeographycaleZone.NATIONAL,
        )
        # Pre-National
        self.assertEqual(
            extract_geographycale_zone("Championnat Pre-National"),
            GeographycaleZone.PRE_NATIONAL,
        )
        self.assertEqual(
            extract_geographycale_zone("Pre-National"),
            GeographycaleZone.PRE_NATIONAL,
        )
        # International
        self.assertEqual(
            extract_geographycale_zone("Tournoi International"),
            GeographycaleZone.INTERNATIONAL,
        )
        self.assertEqual(
            extract_geographycale_zone("International"),
            GeographycaleZone.INTERNATIONAL,
        )
        # Regional
        self.assertEqual(
            extract_geographycale_zone("Championnat Regional"),
            GeographycaleZone.REGIONAL,
        )
        self.assertEqual(
            extract_geographycale_zone("Regional"),
            GeographycaleZone.REGIONAL,
        )
        # Pre-Regional
        self.assertEqual(
            extract_geographycale_zone("Tournoi Pre-Regional"),
            GeographycaleZone.PRE_REGIONAL,
        )
        self.assertEqual(
            extract_geographycale_zone("Pre-Regional"),
            GeographycaleZone.PRE_REGIONAL,
        )
        # Departemental
        self.assertEqual(
            extract_geographycale_zone("Championnat Departemental"),
            GeographycaleZone.DEPARTEMENTAL,
        )
        self.assertEqual(
            extract_geographycale_zone("Departemental"),
            GeographycaleZone.DEPARTEMENTAL,
        )
        # Cas ambigu : Pre-National vs National
        self.assertEqual(
            extract_geographycale_zone("Pre-National"),
            GeographycaleZone.PRE_NATIONAL,
        )
        self.assertEqual(
            extract_geographycale_zone("National"),
            GeographycaleZone.NATIONAL,
        )
        # Cas inconnu
        self.assertIsNone(extract_geographycale_zone("Inconnu"))
