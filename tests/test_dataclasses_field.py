import unittest

from ffbb_api_client import Field


class TestField(unittest.TestCase):
    def test_field(self):
        f = Field.from_dict({"groupId": 1, "name": "n", "title": "t", "desc": "d"})
        self.assertEqual(f.group_id, 1)
        self.assertEqual(f.name, "n")
        self.assertEqual(f.title, "t")
        self.assertEqual(f.desc, "d")
        self.assertEqual(f, Field.from_dict(f.to_dict()))
        self.assertIsInstance(hash(f), int)
