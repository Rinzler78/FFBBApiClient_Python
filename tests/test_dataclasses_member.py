import unittest

from ffbb_api_client.member import Member


class TestMember(unittest.TestCase):
    def test_member(self):
        data = {
            "id": 1,
            "nom": "Dupont",
            "prenom": "Jean",
            "adresse1": "1 rue de la Paix",
            "adresse2": "Bat A",
            "codePostal": "75001",
            "ville": "Paris",
            "mail": "jean.dupont@email.com",
            "telephoneFixe": "0102030405",
            "telephonePortable": "0607080910",
            "idLicence": 123456,
            "codeFonction": "COACH",
            "libelleFonction": "Coach principal",
            "accordDiffusionSiteWeb": True,
        }
        member = Member.from_dict(data)
        self.assertEqual(member.id, 1)
        self.assertEqual(member.last_name, "Dupont")
        self.assertEqual(member.first_name, "Jean")
        self.assertEqual(member.address_line1, "1 rue de la Paix")
        self.assertEqual(member.address_line2, "Bat A")
        self.assertEqual(member.postal_code, 75001)
        self.assertEqual(member.city, "Paris")
        self.assertEqual(member.email, "jean.dupont@email.com")
        self.assertEqual(member.landline_phone, "0102030405")
        self.assertEqual(member.mobile_phone, "0607080910")
        self.assertEqual(member.license_id, 123456)
        self.assertEqual(member.role_code, "COACH")
        self.assertEqual(member.role_label, "Coach principal")
        self.assertTrue(member.consent_to_website_publishing)

    def test_member_none(self):
        data = {}
        member = Member.from_dict(data)
        self.assertIsNone(member.id)
        self.assertIsNone(member.last_name)
        self.assertIsNone(member.first_name)
        self.assertIsNone(member.address_line1)
        self.assertIsNone(member.address_line2)
        self.assertIsNone(member.postal_code)
        self.assertIsNone(member.city)
        self.assertIsNone(member.email)
        self.assertIsNone(member.landline_phone)
        self.assertIsNone(member.mobile_phone)
        self.assertIsNone(member.license_id)
        self.assertIsNone(member.role_code)
        self.assertIsNone(member.role_label)
        self.assertIsNone(member.consent_to_website_publishing)

    def test_member_creation(self):
        m = Member(id=1, last_name="Dupont", first_name="Jean")
        self.assertEqual(m.id, 1)
        self.assertEqual(m.last_name, "Dupont")
        self.assertEqual(m.first_name, "Jean")
        self.assertEqual(m, Member(id=1, last_name="Dupont", first_name="Jean"))
