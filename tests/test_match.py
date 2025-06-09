import unittest
from datetime import datetime

from ffbb_api_client.match import Match
from ffbb_api_client.score import Score


class TestMatch(unittest.TestCase):
    def test_match(self):
        dt = datetime(2024, 1, 1, 15, 0)
        s = Score(42, 12)
        m = Match(date=dt, time="15:00", hometeam="A", visitorteam="B", score=s)
        self.assertEqual(m.date, dt)
        self.assertEqual(m.time, "15:00")
        self.assertEqual(m.hometeam, "A")
        self.assertEqual(m.visitorteam, "B")
        self.assertEqual(m.score, s)
        self.assertTrue(m.played)
        d = m.to_dict()
        self.assertEqual(d["hometeam"], "A")
        self.assertIsInstance(hash(m), int)
