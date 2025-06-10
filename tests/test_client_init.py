import unittest
from ffbb_api_client import FFBBApiClient


class TestFFBBApiClientInit(unittest.TestCase):
    def test_empty_basic_auth_user(self):
        with self.assertRaises(ValueError):
            FFBBApiClient(basic_auth_user="", basic_auth_pass="p")

    def test_empty_basic_auth_pass(self):
        with self.assertRaises(ValueError):
            FFBBApiClient(basic_auth_user="u", basic_auth_pass="")

    def test_empty_api_url(self):
        with self.assertRaises(ValueError):
            FFBBApiClient(basic_auth_user="u", basic_auth_pass="p", api_url="")

    def test_empty_ws_url(self):
        with self.assertRaises(ValueError):
            FFBBApiClient(basic_auth_user="u", basic_auth_pass="p", ws_url="")

