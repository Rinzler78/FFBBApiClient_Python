import os
from typing import List

from ffbb_api_client import FFBBApiClient
from ffbb_api_client.api_types import (
    AgendaAndResults,
    Area,
    Championship,
    ClubDetails,
    ClubInfos,
    Commune,
    League,
    Team,
)

# Retrieve api user / pass
basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")

# Create an instance of the api client
api_client: FFBBApiClient = FFBBApiClient(
    basic_auth_user=basic_auth_user, basic_auth_pass=basic_auth_pass
)

# Get communes by name
commune: List[Commune] = api_client.get_communes("Senas")[0]

# Get clubs from the commune
club_infos: ClubInfos = api_client.search_club(commune.id)[0]

# Get club detail from the club
club_details: ClubDetails = api_client.get_club_details(club_infos.id)

# Filter a team
u13_team_D4_phase_2: Team = next(
    team
    for team in club_details.teams
    if team.category == "U13"
    and "Division 4" in team.name
    and "Phase 2" in team.name
    and "Poule D" in team.name
)

# Get areas
areas: List[Area] = api_client.get_areas()

# Filter an area
area_0013: Area = next(area for area in areas if area.id == "0013")

# Get leagues
leagues: List[League] = api_client.get_leagues()

# Filter a league
league_sud: League = next(league for league in leagues if league.id == "SUD")

# Get top championships
top_championships: List[Championship] = api_client.get_top_championships()
top_championships_departments_championship: Championship = next(
    championship
    for championship in top_championships
    if championship.name == "CHAMPIONNATS DEPARTEMENTAUX"
)


# Get agenda and results for team
def get_all_results_for_team(team: Team) -> AgendaAndResults:

    day: int = 0
    results: AgendaAndResults = None

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

        if not results:
            results = day_results
            continue

        for day_results_day in day_results.days:
            existing_day = next(
                (day for day in results.days if day.name == day_results_day.name), None
            )

            if existing_day:
                continue

            results.days.append(day_results_day)

        for day_results_group in day_results.groups:
            existing_group = next(
                (group for group in results.groups if group.id == day_results_group.id),
                None,
            )

            if existing_group:
                continue

            results.groups.append(day_results_group)

        for day_results_match in day_results.matchs:
            existing_match = next(
                (
                    match
                    for match in results.matchs
                    if match.match_id == day_results_match.match_id
                ),
                None,
            )

            if existing_match:
                continue

            results.matchs.append(day_results_match)

        for day_results_sub_competition in day_results.sub_competitions:
            existing_sub_competition = next(
                (
                    sub_competition
                    for sub_competition in day_results.sub_competitions
                    if sub_competition.id == day_results_sub_competition.id
                ),
                None,
            )

            if existing_sub_competition:
                continue

            results.sub_competitions.append(day_results_sub_competition)

    return results


results = get_all_results_for_team(u13_team_D4_phase_2)

print(results)
