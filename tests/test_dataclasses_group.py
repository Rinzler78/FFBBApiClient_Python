import unittest
from ffbb_api_client import Group, CompetitionType


class TestGroup(unittest.TestCase):
    def test_group(self):
        g = Group.from_dict({"id": "1", "name": "A", "type": "CHAMPIONSHIP"})
        self.assertEqual(g.id, "1")
        self.assertEqual(g.name, "A")
        self.assertEqual(g.competition_type, CompetitionType.CHAMPIONSHIP)
        self.assertEqual(g, Group.from_dict(g.to_dict()))
        self.assertIsInstance(hash(g), int) 