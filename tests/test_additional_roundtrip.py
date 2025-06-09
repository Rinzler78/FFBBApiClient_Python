import unittest
from datetime import datetime

from ffbb_api_client import (
    BasketballCourt,
    ClubDetails,
    ClubInfos,
    GeoLocation,
    History,
    Match,
    Member,
    Municipality,
    News,
    PracticeOffers,
    Season,
    Standing,
    Team,
    TypeAssociation,
)


class TestMatchRoundtrip(unittest.TestCase):
    def test_match_roundtrip(self):
        data = {
            "formattedDate": 1609456200,
            "time": "12:30",
            "hometeam": "Home",
            "visitorteam": "Visitor",
            "score": "80 - 70",
            "date": "01/01/2021",
            "remise": 1,
            "round": 5,
            "matchId": 42,
        }
        match = Match.from_dict(data)
        self.assertTrue(match.played)
        self.assertFalse(match.is_ghost)
        self.assertEqual(match.to_dict()["matchId"], 42)
        self.assertEqual(match, Match.from_dict(match.to_dict()))


class TestNewsRoundtrip(unittest.TestCase):
    def test_news_roundtrip(self):
        data = {
            "id": "1",
            "date": "2025-01-01",
            "url": "http://example.com",
            "author": "John",
            "category": "Sport",
            "title": "Title",
            "image": "img",
            "excerpt": "desc",
        }
        news = News.from_dict(data)
        self.assertEqual(news, News.from_dict(news.to_dict()))
        self.assertIsInstance(hash(news), int)


class TestStandingRoundtrip(unittest.TestCase):
    def test_standing_roundtrip(self):
        data = {
            "pos": 1,
            "points": "10",
            "day": 5,
            "win": 3,
            "lost": 2,
            "draw": 1,
            "penalties": 0,
            "forfeited": 0,
            "defaults": 0,
            "arb": 0,
            "ent": 0,
            "scored": 100,
            "conceded": 90,
            "quotient": 1.1,
            "club": "Club",
            "initi": "I",
        }
        standing = Standing.from_dict(data)
        self.assertEqual(standing, Standing.from_dict(standing.to_dict()))


class TestTeamRoundtrip(unittest.TestCase):
    def test_team_roundtrip(self):
        data = {
            "id": "1",
            "subCompetition": "SC",
            "name": "Division 2 Poule B Phase 3",
            "group": "G1",
            "category": "U13",
            "groupField": "M",
        }
        team = Team.from_dict(data)
        self.assertEqual(team.division_number, 2)
        self.assertEqual(team.pool_letter, "B PHASE 3")
        self.assertEqual(team.phase_number, 3)
        # to_dict returns plain strings
        team.category = data["category"]
        team_dict = team.to_dict()
        self.assertEqual(team_dict["id"], "1")


class TestClubInfosRoundtrip(unittest.TestCase):
    def test_club_infos_roundtrip(self):
        club = ClubInfos(
            None,
            None,
            None,
            None,
            None,
            id=1,
            parent_organization_id=2,
            code="C",
            name="Name",
            type="T",
            adress="Adr",
            phone="123",
            email="a@b",
            municipality=Municipality(id=5, label="City"),
            association_type=TypeAssociation(id=1, libelle="TA"),
            court=BasketballCourt(number=None, id=1, label="Court"),
            url_site_web="http://site",
            membres=[Member(id=1)],
            child_organizations=["child"],
            practice_offers=[PracticeOffers(id=1, type="t", category="c")],
            certifications=["cert"],
            geo_location=GeoLocation(
                postal_code=75000,
                latitude=1.0,
                longitude=2.0,
                title="t",
                adress="a",
                city="c",
            ),
            history=[
                History(
                    None,
                    datetime(2024, 1, 1),
                    None,
                    Season(id=1),
                    datetime(2024, 1, 1),
                    TypeAssociation(id=2),
                )
            ],
            organization_id=3,
            municipality_id=5,
            organization_code="OC",
            organization_name="Org",
            affiliation_date=datetime(2024, 1, 1),
        )
        data = club.to_dict()
        self.assertEqual(club, ClubInfos.from_dict(data))


class TestClubDetailsRoundtrip(unittest.TestCase):
    def test_club_details_roundtrip(self):
        details = ClubDetails(infos=[], fields=[], teams=[])
        self.assertEqual(details, ClubDetails.from_dict(details.to_dict()))
