import unittest
from ffbb_api_client import Snippet, ResourceID


class TestSnippet(unittest.TestCase):
    def test_snippet(self):
        s = Snippet.from_dict({
            "publishedAt": "2024-01-01T00:00:00",
            "channelId": "cid",
            "title": "t",
            "description": "desc",
            "thumbnails": {"default": {"url": "u"}},
            "channelTitle": "ct",
            "playlistId": "pid",
            "position": 1,
            "resourceId": {"kind": "k", "videoId": "vid"},
            "videoOwnerChannelTitle": "voct",
            "videoOwnerChannelId": "voci"
        })
        self.assertEqual(s.channel_id, "cid")
        self.assertEqual(s.title, "t")
        self.assertEqual(s.description, "desc")
        self.assertEqual(s.channel_title, "ct")
        self.assertEqual(s.playlist_id, "pid")
        self.assertEqual(s.position, 1)
        self.assertEqual(s.resource_id, ResourceID("k", "vid"))
        self.assertEqual(s.video_owner_channel_title, "voct")
        self.assertEqual(s.video_owner_channel_id, "voci")
        self.assertEqual(s, Snippet.from_dict(s.to_dict())) 