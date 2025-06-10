import unittest

from ffbb_api_client import GeographicalZone, extract_geographical_zone


class TestGeographicalZone(unittest.TestCase):
    def test_enum(self):
        self.assertEqual(GeographicalZone.SUD.value, "Sud")
        self.assertEqual(GeographicalZone.NATIONAL.value, "National")

    def test_extract_geographical_zone(self):
        # Sud
        self.assertEqual(
            extract_geographical_zone("La zone est Sud"),
            GeographicalZone.SUD,
        )
        self.assertEqual(
            extract_geographical_zone("Sud"),
            GeographicalZone.SUD,
        )
        # National
        self.assertEqual(
            extract_geographical_zone("Compétition Nationale"),
            GeographicalZone.NATIONAL,
        )
        self.assertEqual(
            extract_geographical_zone("National"),
            GeographicalZone.NATIONAL,
        )
        # Pre-National
        self.assertEqual(
            extract_geographical_zone("Championnat Pre-National"),
            GeographicalZone.PRE_NATIONAL,
        )
        self.assertEqual(
            extract_geographical_zone("Pre-National"),
            GeographicalZone.PRE_NATIONAL,
        )
        # International
        self.assertEqual(
            extract_geographical_zone("Tournoi International"),
            GeographicalZone.INTERNATIONAL,
        )
        self.assertEqual(
            extract_geographical_zone("International"),
            GeographicalZone.INTERNATIONAL,
        )
        # Regional
        self.assertEqual(
            extract_geographical_zone("Championnat Regional"),
            GeographicalZone.REGIONAL,
        )
        self.assertEqual(
            extract_geographical_zone("Regional"),
            GeographicalZone.REGIONAL,
        )
        # Pre-Regional
        self.assertEqual(
            extract_geographical_zone("Tournoi Pre-Regional"),
            GeographicalZone.PRE_REGIONAL,
        )
        self.assertEqual(
            extract_geographical_zone("Pre-Regional"),
            GeographicalZone.PRE_REGIONAL,
        )
        # Departemental
        self.assertEqual(
            extract_geographical_zone("Championnat Departemental"),
            GeographicalZone.DEPARTEMENTAL,
        )
        self.assertEqual(
            extract_geographical_zone("Departemental"),
            GeographicalZone.DEPARTEMENTAL,
        )
        # Cas ambigu : Pre-National vs National
        self.assertEqual(
            extract_geographical_zone("Pre-National"),
            GeographicalZone.PRE_NATIONAL,
        )
        self.assertEqual(
            extract_geographical_zone("National"),
            GeographicalZone.NATIONAL,
        )
        # Cas inconnu
        self.assertIsNone(extract_geographical_zone("Inconnu"))
