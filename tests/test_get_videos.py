from tests.test_base import TestFFBBApiClient
from ffbb_api_client import Videos


class Test_GetVideos(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_videos()
        if result:
            self.assertIsInstance(result, Videos)

    def test_with_known_club_id(self):
        result = self.api_client.get_videos(
            id_cmne=self._get_know_club_infos().municipality.municipality_id
        )
        if result:
            self.assertIsInstance(result, Videos)

    def test_with_unknown_club_id(self):
        result = self.api_client.get_videos(id_cmne=0)
        if result:
            self.assertIsInstance(result, Videos)

    def test_with_with_known_org_name(self):
        result = self.api_client.get_videos(
            org_name=self._get_know_club_infos().organization_name
        )
        if result:
            self.assertIsInstance(result, Videos)

    def test_with_with_unknown_org_name(self):
        result = self.api_client.get_videos(org_name="test")
        if result:
            self.assertIsInstance(result, Videos) 