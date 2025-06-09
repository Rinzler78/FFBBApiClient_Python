import unittest

from ffbb_api_client import TypeAssociation


class TestTypeAssociation(unittest.TestCase):
    def test_type_association(self):
        t = TypeAssociation.from_dict({"id": 1, "libelle": "lbl", "code": "c"})
        self.assertEqual(t.id, 1)
        self.assertEqual(t.libelle, "lbl")
        self.assertEqual(t.code, "c")
        self.assertEqual(t, TypeAssociation.from_dict(t.to_dict()))
        self.assertIsInstance(hash(t), int)
