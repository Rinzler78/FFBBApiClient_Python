import unittest

from ffbb_api_client import MatchDetail


class TestMatchDetail(unittest.TestCase):
    def test_match_detail(self):
        m = MatchDetail.from_dict({"category": "cat", "title": "t", "desc": "d"})
        self.assertEqual(m.category, "cat")
        self.assertEqual(m.title, "t")
        self.assertEqual(m.desc, "d")
        self.assertEqual(m, MatchDetail.from_dict(m.to_dict()))
        self.assertIsInstance(hash(m), int)
