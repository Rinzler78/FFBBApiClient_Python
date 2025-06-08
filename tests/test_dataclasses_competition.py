import unittest
from ffbb_api_client import Competition


class TestCompetition(unittest.TestCase):
    def test_competition(self):
        c = Competition.from_dict({"name": "C1", "id": "1", "groupField": "G"})
        self.assertEqual(c.name, "C1")
        self.assertEqual(c.id, "1")
        self.assertEqual(c.group_field, "G")
        self.assertEqual(c, Competition.from_dict(c.to_dict()))
        self.assertIsInstance(hash(c), int) 