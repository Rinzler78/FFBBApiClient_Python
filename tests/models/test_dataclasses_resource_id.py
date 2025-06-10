import unittest

from ffbb_api_client import ResourceID


class TestResourceID(unittest.TestCase):
    def test_resource_id(self):
        r = ResourceID.from_dict({"kind": "video", "videoId": "abc"})
        self.assertEqual(r.kind, "video")
        self.assertEqual(r.video_id, "abc")
        self.assertEqual(r, ResourceID.from_dict(r.to_dict()))
        self.assertIsInstance(hash(r), int)
