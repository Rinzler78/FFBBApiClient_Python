import unittest
from ffbb_api_client.competition import Competition


class TestCompetition(unittest.TestCase):
    def test_competition(self):
        c = Competition(id="1", name="Compétition", group_field="A")
        self.assertEqual(c.id, "1")
        self.assertEqual(c.name, "Compétition")
        self.assertEqual(c.group_field, "A")
        self.assertEqual(c, Competition(id="1", name="Compétition", group_field="A"))
        self.assertIsInstance(hash(c), int) 