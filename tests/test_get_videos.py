from ffbb_api_client import Videos
from tests.test_base import TestFFBBApiClient


class Test_GetVideos(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_videos()
        if result:
            self.assertIsInstance(result, Videos)

    def test_get_videos_basic(self):
        result = self.api_client.get_videos()
        if result:
            self.assertIsInstance(result, Videos)
