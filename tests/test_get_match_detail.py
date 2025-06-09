from tests.test_base import TestFFBBApiClient


class Test_GetMatchDetail(TestFFBBApiClient):
    def test_with_known_match_id(self):
        result = self.api_client.get_match_detail(
            match_id=self._get_known_results().matchs[0].match_id
        )
        self.assertIsNotNone(result)

    def test_with_unknown_match_id(self):
        result = self.api_client.get_match_detail(match_id=0)
        self.assertIsNone(result)
