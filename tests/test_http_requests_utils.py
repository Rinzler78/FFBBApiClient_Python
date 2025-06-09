import unittest
from unittest.mock import MagicMock, patch
from ffbb_api_client.http_requests_utils import (
    to_json_from_response,
    http_get_json,
    http_post_json,
)


class TestHttpRequestsUtils(unittest.TestCase):
    def test_to_json_from_response(self):
        mock_response = MagicMock()
        mock_response.text = '{"key": "value"}'
        result = to_json_from_response(mock_response)
        self.assertEqual(result, {"key": "value"})

        mock_response.text = '""{"key": "value"}'
        result = to_json_from_response(mock_response)
        self.assertEqual(result, {"key": "value"})

        mock_response.text = '{"key": "value"},'
        result = to_json_from_response(mock_response)
        self.assertEqual(result, {"key": "value"})

        mock_response.text = '[1][2]'
        result = to_json_from_response(mock_response)
        self.assertEqual(result, [1, 2])

    @patch("ffbb_api_client.http_requests_utils.requests.get")
    def test_http_get_json(self, mock_get):
        response = MagicMock()
        response.text = '{"x": 1}'
        mock_get.return_value = response
        result = http_get_json("http://example", {})
        self.assertEqual(result, {"x": 1})

    @patch("ffbb_api_client.http_requests_utils.requests.post")
    def test_http_post_json(self, mock_post):
        response = MagicMock()
        response.text = '{"y": 2}'
        mock_post.return_value = response
        result = http_post_json("http://example", {}, {"a": None, "b": 2})
        self.assertEqual(result, {"y": 2})
