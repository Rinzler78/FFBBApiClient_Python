import unittest
from ffbb_api_client import Area


class TestArea(unittest.TestCase):
    def test_area(self):
        a = Area.from_dict({"id": "13", "name": "Sud"})
        self.assertEqual(a.id, "13")
        self.assertEqual(a.name, "Sud")
        self.assertEqual(a, Area.from_dict(a.to_dict()))
        self.assertIsInstance(hash(a), int) 