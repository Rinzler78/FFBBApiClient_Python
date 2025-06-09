from typing import List

from tests.test_base import TestFFBBApiClient


class Test_GetNews(TestFFBBApiClient):
    def test_main(self):
        result = self.api_client.get_news()
        if result:
            self.assertIsInstance(result, List)
            self.assertGreater(len(result), 0)
