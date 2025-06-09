import unittest

from ffbb_api_client.municipality import Municipality


class TestMunicipality(unittest.TestCase):
    def test_municipality(self):
        m = Municipality(id=1, label="Paris")
        self.assertEqual(m.id, 1)
        self.assertEqual(m.label, "Paris")
        self.assertEqual(m, Municipality(id=1, label="Paris"))
        self.assertEqual(m, Municipality.from_dict(m.to_dict()))
        self.assertIsInstance(hash(m), int)
