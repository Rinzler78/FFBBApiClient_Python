import os
import string
from typing import List

from requests_cache import CachedSession

from ffbb_api_client import (
    AgendaAndResults,
    ClubDetails,
    ClubInfos,
    FFBBApiClient,
    Municipality,
    Team,
)
from tests.test_ffbb_api_client import Test_GetClubDetails

# Retrieve api user / pass
basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")

# Expire cache after 10 day
expire_after = 864000

cached_session = CachedSession(
    "playground.http_cache",
    backend="sqlite",
    expire_after=expire_after,
    allowable_methods=("GET", "POST"),
)

# Create an instance of the api client
api_client: FFBBApiClient = FFBBApiClient(
    basic_auth_user=basic_auth_user,
    basic_auth_pass=basic_auth_pass,
    debug=True,
    cached_session=cached_session,
)

search_patterns = list(string.ascii_lowercase)

municipalities = []

for pattern in search_patterns:
    result: List[Municipality] = None
    print(f"Searching municicpalities for {pattern}")
    try:
        result = api_client.search_municipalities(pattern)
    except Exception as e:
        print(f"An error occurred while searching municipalities: {str(e)}")

    if not result:
        continue

    municipalities.extend(result)

municipalities = list(set(municipalities))
municipalities.sort(key=lambda x: x.label)

clubs_infos = []

for search_pattern in search_patterns:
    result: ClubInfos = None
    print(f"Searching club for {search_pattern}")
    try:
        result = api_client.search_clubs(org_name=search_pattern)
    except Exception as e:
        print(f"An error occurred while searching clubs: {str(e)}")

    if not result:
        continue

    clubs_infos.extend(result)

clubs_infos = list(set(clubs_infos))
clubs_infos.sort(key=lambda x: x.name)

clubs_details = []

for club_info in clubs_infos:
    result: ClubDetails = None
    print(f"Searching club details for {club_info.name}")
    try:
        result = api_client.get_club_details(club_info.id)
    except Exception as e:
        print(f"An error occurred while retrieving club details: {str(e)}")

    if not result:
        continue

    clubs_details.append(result)

clubs_details = list(set(clubs_details))

teams = list({team for result in clubs_details for team in result.teams})
for team in teams:
    team_results: AgendaAndResults = None
    print(f"Retrieve results for team {team.name}")
    try:
        team_results = api_client.get_results(
            team_id=team.id,
            sub_competition=team.sub_competition,
            team_group=team.group,
        )
    except Exception as e:
        print(
            f"An error occurred while retrieving results for team {team.name}: {str(e)}"
        )
        continue

    if not team_results:
        continue

    print(f"Results for team {team.name} retrieved")


test = Test_GetClubDetails()
test.setUp()
test.test_with_empty_id()
test.test_with_known_id()


def merge_results(
    club_infos: ClubInfos, results: List[AgendaAndResults]
) -> AgendaAndResults:
    merged_results: AgendaAndResults = None

    if len(results) > 0:
        merged_results: AgendaAndResults = results[0]

        for result in results[1:]:
            for result_day in result.days:
                existing_day = next(
                    (day for day in merged_results.days if result_day.name == day.name),
                    None,
                )

                if existing_day:
                    continue

                merged_results.days.append(result_day)

            for result_group in result.groups:
                existing_group = next(
                    (
                        group
                        for group in merged_results.groups
                        if result_group.id == group.id
                    ),
                    None,
                )

                if existing_group:
                    continue

                merged_results.groups.append(result_group)

            for result_match in result.matchs:
                existing_match = next(
                    (
                        match
                        for match in merged_results.matchs
                        if result_match.match_id == match.match_id
                    ),
                    None,
                )

                if existing_match:
                    continue

                merged_results.matchs.append(result_match)

            for result_sub_competition in result.sub_competitions:
                existing_sub_competition = next(
                    (
                        sub_competition
                        for sub_competition in merged_results.sub_competitions
                        if result_sub_competition.id == sub_competition.id
                    ),
                    None,
                )

                if existing_sub_competition:
                    continue

                merged_results.sub_competitions.append(result_sub_competition)

        merged_results.matchs.sort(key=lambda x: x.date)
        merged_results.standings = merged_results.standings[1:]

        played_match = [match for match in merged_results.matchs if match.played]

        if len(played_match) == 0:
            merged_results.standings = []

    return merged_results


# Get agenda and results for team
def get_all_results_for_team(
    api_client: FFBBApiClient, club_infos: ClubInfos, team: Team
) -> AgendaAndResults:

    day: int = 0
    results: List[AgendaAndResults] = []
    last_day_results: AgendaAndResults = None

    while True:
        day += 1

        day_results: AgendaAndResults = api_client.get_results(
            team_id=team.id,
            sub_competition=team.sub_competition,
            team_group=team.group,
            day=day,
        )

        if not day_results or len(day_results.matchs) == 0:
            break

        if club_infos:
            day_results.matchs = [
                match
                for match in day_results.matchs
                if club_infos.organization_name in match.hometeam
                or club_infos.organization_name in match.visitorteam
            ]

        if (
            last_day_results
            and last_day_results.sub_competitions == day_results.sub_competitions
            and last_day_results.groups == day_results.groups
            and last_day_results.days == day_results.days
            and last_day_results.matchs == day_results.matchs
            and last_day_results.standings == day_results.standings
        ):
            break

        last_day_results = day_results

        results.append(day_results)

    return merge_results(club_infos, results)


def get_all_results_for_teams(club_infos: ClubInfos, teams: List[Team]):
    return [(team, get_all_results_for_team(club_infos, team)) for team in teams]


def extract_possible_club_names(club_name: str):
    # remove '(' or ')' => crau bc (10), senas basket ball 2 (10)
    club_name = club_name.split("(")[0].strip()
    return [part.strip() for part in club_name.split("-")]


def search_teams_from_team_name(team_name: str) -> List[Team]:
    teams: List[Team] = []
    team_name = team_name.strip().lower()

    for name in extract_possible_club_names(team_name):
        clubs_infos = api_client.search_clubs(org_name=name)

        if clubs_infos:
            for club_infos in clubs_infos:
                club_details: ClubDetails = api_client.get_club_details(club_infos.id)

                filtered_teams = [
                    team for team in club_details.teams if name in team.name.lower()
                ]

                if filtered_teams:
                    teams.extend(filtered_teams)

    return teams


def get_datas(name: str):
    results = []
    all_other_teams_names = []

    print(f"Searching club for {name}")
    for possible_name in extract_possible_club_names(name):
        clubs_infos = api_client.search_clubs(org_name=possible_name)

        if not clubs_infos:
            continue

        for club_infos in clubs_infos:
            print(f"Searching club details for {club_infos.name}")
            club_details: ClubDetails = api_client.get_club_details(club_infos.id)

            if not club_details.teams:
                continue

            for team in club_details.teams:
                print(f"Retrieve results for team {team.name}")
                other_teams_names = []
                team_results: AgendaAndResults = api_client.get_results(
                    team_id=team.id,
                    sub_competition=team.sub_competition,
                    team_group=team.group,
                )

                if not team_results:
                    continue

                for std in team_results.standings[1:]:
                    if club_infos.name not in std.club and std.club != "Exempt":
                        other_teams_names.append(std.club)

                for ffbb_api_match in team_results.matchs:
                    if club_infos.name in ffbb_api_match.hometeam:
                        other_teams_names.append(ffbb_api_match.visitorteam)
                    else:
                        other_teams_names.append(ffbb_api_match.hometeam)

                other_teams_names = sorted(set(other_teams_names))
                all_other_teams_names.extend(other_teams_names)
                results.append(
                    (club_infos, club_details, team, team_results, other_teams_names)
                )

        break

    all_other_teams_names = sorted(set(all_other_teams_names))

    return results


# datas = get_datas("Senas")
# all_teams = []

# for data in datas:
#     all_teams.extend(data[4])

# all_teams = sorted(set(all_teams))

# for team_name in all_teams:
#     get_datas(team_name)


alphabet = list(string.ascii_lowercase)
for org_name in alphabet:
    print(f"Searching club for {org_name}")
    municipalities = api_client.search_clubs(org_name=org_name)

    if not municipalities:
        print()

print()
