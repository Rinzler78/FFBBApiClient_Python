import unittest
from ffbb_api_client.club_details import ClubDetails


class TestClubDetails(unittest.TestCase):
    def test_club_details(self):
        d = ClubDetails(infos=[], fields=[], teams=[])
        self.assertEqual(d.infos, [])
        self.assertEqual(d.fields, [])
        self.assertEqual(d.teams, [])
        self.assertEqual(d, ClubDetails(infos=[], fields=[], teams=[])) 