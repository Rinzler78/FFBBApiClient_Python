import os
import string
from typing import List

from ffbb_api_client import (
    AgendaAndResults,
    ClubDetails,
    ClubInfos,
    FFBBApiClient,
    Team,
)

# Retrieve api user / pass
basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")

# Create an instance of the api client
api_client: FFBBApiClient = FFBBApiClient(
    basic_auth_user=basic_auth_user, basic_auth_pass=basic_auth_pass
)


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
    result = api_client.search_clubs(org_name=org_name)

    if not result:
        print()

print()
