import os

from src.ffbb_api_client import FFBBApiClient
from tests.test_ffbb_api_client import (
    Test_GetClubDetails,
    Test_GetResults,
    Test_GetTopChampionships,
    Test_GetVideos,
    Test_SearchMultipleClubs,
    Test_SearchMultipleMunicipalities,
    Test_SearchMunicipalities,
)

# Retrieve api user / pass
basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")

# Create an instance of the api client
api_client: FFBBApiClient = FFBBApiClient(
    basic_auth_user=basic_auth_user,
    basic_auth_pass=basic_auth_pass,
    debug=True,
)

test = Test_GetClubDetails()
test.setUp()
test.test_with_empty_id()
test.test_with_known_id()

test = Test_GetTopChampionships()
test.setUp()
test.test_main()
test.test_cup()
test.test_championship()

test = Test_GetVideos()
test.setUp()
test.test_main()
test.test_with_known_club_id()
test.test_with_unknown_club_id()
test.test_with_with_known_org_name()
test.test_with_with_unknown_org_name()

test = Test_SearchMunicipalities()
test.setUp()
test.test_with_known_name()
test.test_with_unknown_name()
test.test_with_empty_name()

test = Test_SearchMultipleMunicipalities()
test.setUp()
test.test_with_known_name()
test.test_with_unknown_name()
test.test_with_empty_name()
test.test_with_most_used_letters()

test = Test_SearchMultipleClubs()
test.setUp()
test.test_with_known_name()
test.test_with_unknown_name()
test.test_with_empty_name()
test.test_with_most_used_letters()

test = Test_GetResults()
test.setUp()
test.test_without_parameters()
test.test_with_known_team_id()
test.test_with_known_0_team_id()
test.test_with_known_sub_competition()
test.test_with_known_group()
test.test_with_known_team_id_sub_competition()
test.test_with_known_team_id_sub_competition_group()
test.test_for_all_team_results()
