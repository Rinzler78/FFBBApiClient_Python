import json
import unittest

from requests.exceptions import ConnectionError

from ffbb_api_client import (
    ClubDetails,
    ClubInfos,
    Field,
    Municipality,
    Team,
    catch_result,
    CatchResultError,
)
from ffbb_api_client.club_details_helper import merge_club_details
from ffbb_api_client.clubs_infos_helper import create_set_of_clubs
from ffbb_api_client.http_requests_utils import encode_params, url_with_params
from ffbb_api_client.municipalities_helper import create_set_of_municipalities


class TestUtilities(unittest.TestCase):
    def test_create_set_of_municipalities(self):
        m1 = Municipality(id=1)
        m2 = Municipality(id=1)
        result = create_set_of_municipalities([m1, m2])
        self.assertEqual(result, [m1])

    def test_create_set_of_clubs(self):
        c1 = ClubInfos(None, None, None, None, None, id=1)
        c2 = ClubInfos(None, None, None, None, None, id=1)
        result = create_set_of_clubs([c1, c2])
        self.assertEqual(result, [c1])

    def test_merge_club_details(self):
        d1 = ClubDetails(infos=[Field(name="i1")], teams=[Team(name="t1")])
        d2 = ClubDetails(infos=[Field(name="i2")], teams=[Team(name="t2")])
        merged = merge_club_details(d1, d2)
        self.assertEqual(len(merged.infos), 2)
        self.assertEqual(len(merged.teams), 2)

    def test_encode_params_and_url(self):
        params = {"a": 1, "b": None}
        encoded = encode_params(params)
        self.assertEqual(encoded, "a=1")
        url = url_with_params("http://x", params)
        self.assertEqual(url, "http://x?a=1")

    def test_catch_result(self):
        calls = {"n": 0}

        def cb():
            calls["n"] += 1
            if calls["n"] < 2:
                raise ConnectionError
            return 42

        self.assertEqual(catch_result(cb), 42)

        def bad():
            raise json.decoder.JSONDecodeError("Expecting value", "", 0)

        self.assertIsNone(catch_result(bad))

        with self.assertRaises(CatchResultError):
            catch_result(lambda: (_ for _ in ()).throw(ValueError("boom")))
