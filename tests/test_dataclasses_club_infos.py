import unittest
from datetime import datetime
from ffbb_api_client import ClubInfos, Municipality, TypeAssociation


class TestClubInfos(unittest.TestCase):
    def test_club_infos(self):
        data = {
            "id": 42,
            "nom": "Basket Club",
            "type": "Association",
            "adresse": "10 avenue du Stade",
            "telephone": "0123456789",
            "mail": "contact@basketclub.com",
            "commune": {
                "id": 1,
                "name": "Paris"
            },
            "type_association": {
                "id": 1,
                "libelle": "Association principale"
            },
            "urlSiteWeb": "https://basketclub.com",
            "idOrg": 100,
            "idCmne": 1,
            "cdOrg": "BC42",
            "nomOrg": "Basket Club",
            "dateAffiliation": "2020-09-01T00:00:00Z"
        }
        club = ClubInfos.from_dict(data)
        self.assertEqual(club.id, 42)
        self.assertEqual(club.name, "Basket Club")
        self.assertEqual(club.type, "Association")
        self.assertEqual(club.adress, "10 avenue du Stade")
        self.assertEqual(club.phone, "0123456789")
        self.assertEqual(club.email, "contact@basketclub.com")
        self.assertIsInstance(club.municipality, Municipality)
        self.assertIsInstance(club.association_type, TypeAssociation)
        self.assertEqual(club.url_site_web, "https://basketclub.com")
        self.assertEqual(club.organization_id, 100)
        self.assertEqual(club.municipality_id, 1)
        self.assertEqual(club.organization_code, "BC42")
        self.assertEqual(club.organization_name, "Basket Club")
        self.assertIsInstance(club.affiliation_date, datetime)

    def test_club_infos_none(self):
        data = {}
        club = ClubInfos.from_dict(data)
        self.assertIsNone(club.id)
        self.assertIsNone(club.name)
        self.assertIsNone(club.type)
        self.assertIsNone(club.adress)
        self.assertIsNone(club.phone)
        self.assertIsNone(club.email)
        self.assertIsNone(club.municipality)
        self.assertIsNone(club.association_type)
        self.assertIsNone(club.url_site_web)
        self.assertIsNone(club.organization_id)
        self.assertIsNone(club.municipality_id)
        self.assertIsNone(club.organization_code)
        self.assertIsNone(club.organization_name)
        self.assertIsNone(club.affiliation_date) 