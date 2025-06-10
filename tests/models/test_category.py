import unittest

from ffbb_api_client import Category
from ffbb_api_client.models.category import extract_category


class TestCategory(unittest.TestCase):
    def test_enum(self):
        self.assertEqual(Category.U13.value, "U13")

    def test_extract_category(self):
        self.assertEqual(extract_category("U13"), Category.U13)
        self.assertIsNone(extract_category("UNKNOWN"))
