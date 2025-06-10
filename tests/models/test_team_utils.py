import unittest

from ffbb_api_client import (
    Team,
    extract_division_number,
    extract_phase_number,
    extract_pool_letter,
)


class TestTeamUtils(unittest.TestCase):
    def test_extract_helpers(self):
        self.assertEqual(extract_division_number("Division 2"), 2)
        self.assertEqual(extract_pool_letter("Poule B"), "B")
        self.assertEqual(extract_phase_number("Phase 3"), 3)

    def test_team_from_dict(self):
        data = {
            "id": "1",
            "subCompetition": "SC",
            "name": "Division 1 Poule A Phase 2",
            "group": "G1",
            "category": "U13",
            "groupField": "M",
        }
        team = Team.from_dict(data)
        self.assertEqual(team.division_number, 1)
        self.assertEqual(team.pool_letter, "A PHASE 2")
        self.assertEqual(team.phase_number, 2)
