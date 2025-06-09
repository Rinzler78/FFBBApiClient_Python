import unittest
from ffbb_api_client.category import Category, extract_category


class TestCategory(unittest.TestCase):
    def test_enum(self):
        self.assertEqual(Category.U13.value, "U13")

    def test_extract_category(self):
        self.assertEqual(extract_category("U13"), Category.U13)
        self.assertIsNone(extract_category("UNKNOWN")) 