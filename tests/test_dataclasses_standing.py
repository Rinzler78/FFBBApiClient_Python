import unittest
from ffbb_api_client.standing import Standing


class TestStanding(unittest.TestCase):
    def test_standing(self):
        s = Standing(pos=1, points=10, win=5, lost=2)
        self.assertEqual(s.pos, 1)
        self.assertEqual(s.points, 10)
        self.assertEqual(s.win, 5)
        self.assertEqual(s.lost, 2)
        self.assertEqual(s, Standing(pos=1, points=10, win=5, lost=2))
        self.assertIsNone(s.draw)
        self.assertIsNone(s.penalties)
        self.assertIsNone(s.forfeited)
        self.assertIsNone(s.defaults)
        self.assertIsNone(s.arb)
        self.assertIsNone(s.ent)
        self.assertIsNone(s.scored)
        self.assertIsNone(s.conceded)
        self.assertIsNone(s.quotient)
        self.assertIsNone(s.club)
        self.assertIsNone(s.initi)
        # Test avec valeurs explicites
        s2 = Standing(
            draw=0, penalties=0, forfeited=0, defaults=0, arb=0, ent=0,
            scored=0, conceded=0, quotient=0, club="club", initi=0
        )
        self.assertEqual(s2.draw, 0)
        self.assertEqual(s2.penalties, 0)
        self.assertEqual(s2.forfeited, 0)
        self.assertEqual(s2.defaults, 0)
        self.assertEqual(s2.arb, 0)
        self.assertEqual(s2.ent, 0)
        self.assertEqual(s2.scored, 0)
        self.assertEqual(s2.conceded, 0)
        self.assertEqual(s2.quotient, 0)
        self.assertEqual(s2.club, "club")
        self.assertEqual(s2.initi, 0)
        self.assertEqual(s, Standing.from_dict(s.to_dict()))
        self.assertIsInstance(hash(s), int) 