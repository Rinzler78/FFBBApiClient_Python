import unittest
from ffbb_api_client import Item, Snippet


class TestItem(unittest.TestCase):
    def test_item(self):
        snippet_data = {
            "title": "Titre",
            "description": "Desc"
        }
        data = {
            "id": "item1",
            "snippet": snippet_data
        }
        item = Item.from_dict(data)
        self.assertEqual(item.id, "item1")
        self.assertIsInstance(item.snippet, Snippet)
        self.assertEqual(item, Item.from_dict(item.to_dict()))
        self.assertIsInstance(hash(item), int) 