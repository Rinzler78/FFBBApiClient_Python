from tests.test_base import TestFFBBApiClient


class Test_GetResults(TestFFBBApiClient):
    def test_without_parameters(self):
        result = self.api_client.get_results()
        self.assertIsNone(result)

    def test_with_known_team_id(self):
        result = self.api_client.get_results(team_id=self._get_known_team().id)
        self.assertIsNotNone(result)

    def test_with_known_0_team_id(self):
        result = self.api_client.get_results(team_id=0)
        self.assertIsNone(result)

    def test_with_known_sub_competition(self):
        result = self.api_client.get_results(
            sub_competition=self._get_known_team().sub_competition
        )
        self.assertIsNone(result)

    def test_with_known_group(self):
        result = self.api_client.get_results(team_group=self._get_known_team().group)
        self.assertIsNone(result)

    def test_with_known_team_id_sub_competition(self):
        result = self.api_client.get_results(
            team_id=self._get_known_team().id,
            sub_competition=self._get_known_team().sub_competition,
        )
        self.assertIsNotNone(result)

    def test_with_known_team_id_sub_competition_group(self):
        result = self._get_known_results()
        self.assertIsNotNone(result)

    def test_for_all_team_results(self):
        know_result = self._get_known_results()
        day_count = int(know_result.days[-1].name)
        results = []
        for i in range(1, day_count + 1):
            result = self.api_client.get_results(
                team_id=self._get_known_team().id,
                sub_competition=self._get_known_team().sub_competition,
                team_group=self._get_known_team().group,
                day=i,
            )
            self.assertIsNotNone(result)
            results.append(result)
        self.assertEqual(len(results), day_count)
