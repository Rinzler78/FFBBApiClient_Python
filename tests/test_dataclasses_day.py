import unittest
from ffbb_api_client import Day


class TestDay(unittest.TestCase):
    def test_day(self):
        d = Day.from_dict({"name": 1, "desc": 2})
        self.assertEqual(d.name, 1)
        self.assertEqual(d.desc, 2)
        self.assertEqual(d, Day(1, 2))
        self.assertEqual(d, Day.from_dict(d.to_dict()))
        self.assertIsInstance(hash(d), int) 