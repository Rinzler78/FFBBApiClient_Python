import unittest

from ffbb_api_client import Default


class TestDefault(unittest.TestCase):
    def test_default(self):
        obj = Default.from_dict({"url": "u", "width": 10, "height": 20})
        self.assertEqual(obj.url, "u")
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)
        self.assertEqual(obj, Default.from_dict(obj.to_dict()))
        self.assertIsInstance(hash(obj), int)
