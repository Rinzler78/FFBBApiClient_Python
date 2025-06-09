import unittest
from unittest.mock import MagicMock
from ffbb_api_client.http_requests_utils import to_json_from_response


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