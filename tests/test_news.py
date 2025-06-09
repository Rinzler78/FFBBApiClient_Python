import unittest

from ffbb_api_client.news import News


class TestNews(unittest.TestCase):
    def test_news(self):
        n = News(id=1, title="Actu")
        self.assertEqual(n.id, 1)
        self.assertEqual(n.title, "Actu")
        self.assertEqual(n, News(id=1, title="Actu"))
        self.assertIsInstance(hash(n), int)
