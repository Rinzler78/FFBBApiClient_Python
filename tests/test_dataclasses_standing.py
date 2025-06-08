import unittest
from ffbb_api_client import Standing


class TestStanding(unittest.TestCase):
    def test_standing(self):
        s = Standing.from_dict({
            "pos": 1, "points": 2, "day": 3, "win": 4, "lost": 5, "draw": 6,
            "penalties": 0, "forfeited": 0, "defaults": 0, "arb": 0, "ent": 0,
            "scored": 10, "conceded": 8, "quotient": 1.25, "club": "club", "initi": 0
        })
        self.assertEqual(s.pos, 1)
        self.assertEqual(s.points, 2)
        self.assertEqual(s.day, 3)
        self.assertEqual(s.win, 4)
        self.assertEqual(s.lost, 5)
        self.assertEqual(s.draw, 6)
        self.assertEqual(s.penalties, 0)
        self.assertEqual(s.forfeited, 0)
        self.assertEqual(s.defaults, 0)
        self.assertEqual(s.arb, 0)
        self.assertEqual(s.ent, 0)
        self.assertEqual(s.scored, 10)
        self.assertEqual(s.conceded, 8)
        self.assertEqual(s.quotient, 1.25)
        self.assertEqual(s.club, "club")
        self.assertEqual(s.initi, 0)
        self.assertEqual(s, Standing.from_dict(s.to_dict()))
        self.assertIsInstance(hash(s), int) 