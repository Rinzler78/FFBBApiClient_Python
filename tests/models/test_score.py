import unittest

from ffbb_api_client import Score


class TestScore(unittest.TestCase):
    def test_score(self):
        s = Score(home=42, visitor=12)
        self.assertEqual(s.home, 42)
        self.assertEqual(s.visitor, 12)
        self.assertEqual(str(s), "42 - 12")
        self.assertTrue(s.played)
        self.assertEqual(s, Score(42, 12))
        self.assertIsInstance(hash(s), int)
