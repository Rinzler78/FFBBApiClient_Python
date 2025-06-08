import unittest
from ffbb_api_client import Videos


class TestVideos(unittest.TestCase):
    def test_videos(self):
        v = Videos.from_dict({
            "nextPageToken": "npt",
            "items": [{"id": "i", "snippet": None}],
            "pageInfo": {"totalResults": 1, "resultsPerPage": 1}
        })
        self.assertEqual(v.next_page_token, "npt")
        self.assertEqual(len(v.items), 1)
        self.assertEqual(v.page_info.total_results, 1)
        self.assertEqual(v, Videos.from_dict(v.to_dict())) 