import unittest

from ffbb_api_client import Default, Thumbnails


class TestThumbnails(unittest.TestCase):
    def test_thumbnails(self):
        data = {
            "default": {"url": "url1", "width": 120, "height": 90},
            "medium": {"url": "url2", "width": 320, "height": 180},
            "high": {"url": "url3", "width": 480, "height": 360},
            "standard": {"url": "url4", "width": 640, "height": 480},
            "maxres": {"url": "url5", "width": 1280, "height": 720},
        }
        thumbs = Thumbnails.from_dict(data)
        self.assertIsInstance(thumbs.default, Default)
        self.assertIsInstance(thumbs.medium, Default)
        self.assertIsInstance(thumbs.high, Default)
        self.assertIsInstance(thumbs.standard, Default)
        self.assertIsInstance(thumbs.maxres, Default)
        self.assertEqual(thumbs, Thumbnails.from_dict(thumbs.to_dict()))
        self.assertIsInstance(hash(thumbs), int)
