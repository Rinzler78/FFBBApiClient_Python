import os
from typing import List

from ffbb_api_client import (
    AgendaAndResults,
    Area,
    Championship,
    ClubDetails,
    ClubInfos,
    Commune,
    FFBBApiClient,
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
    previous_day_results: AgendaAndResults = None

    while True:
        day += 1

        day_results: AgendaAndResults = api_client.get_results(
            team_id=team.id,
            sub_competition=team.sub_competition,
            team_group=team.group,
            day=day,
        )

        if (
            not day_results
            or len(day_results.matchs) == 0
            or (
                previous_day_results
                and previous_day_results.matchs == day_results.matchs
            )
        ):
            break

        previous_day_results = day_results

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


communes: List[Commune] = api_client.get_communes("Senas")

other_clubs_names = []
for commune in communes:
    clubs_infos: List[ClubInfos] = api_client.search_club(commune.id)

    if not clubs_infos:
        continue

    for club_infos in clubs_infos:
        club_details: ClubDetails = api_client.get_club_details(club_infos.id)

        if not club_details or not club_details.teams:
            continue

        for team in club_details.teams:
            print(
                club_infos.nom,
                team.name,
                team.category,
                team.group,
                team.sub_competition,
                team.id,
            )
            team_results = get_all_results_for_team(team)

            if not team_results:
                continue

            other_clubs_names.extend(
                [standing.club for standing in team_results.standings[1:]]
            )

other_clubs_names = list({name for name in other_clubs_names if name != "Exempt"})

other_clubs_infos = []
for club_name in other_clubs_names:
    club_infos: List[ClubInfos] = None

    for part in club_name.split("-"):
        part = part.strip()
        club_infos = api_client.search_club(org_name=part)

        if club_infos:
            for club_info in club_infos:
                print(club_name, part, club_info.nom)

            other_clubs_infos.append((club_name, part, club_infos))
            break

    if not club_infos:
        other_clubs_infos.append((club_name, None, None))

print()
