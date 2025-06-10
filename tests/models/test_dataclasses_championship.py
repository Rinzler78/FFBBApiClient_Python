import unittest

from ffbb_api_client import Championship


class TestChampionship(unittest.TestCase):
    def test_championship(self):
        ch = Championship.from_dict({"name": "Champ", "id": "1", "type": "T"})
        self.assertEqual(ch.name, "Champ")
        self.assertEqual(ch.id, "1")
        self.assertEqual(ch.type, "T")
        self.assertEqual(ch, Championship.from_dict(ch.to_dict()))
        self.assertIsInstance(hash(ch), int)
