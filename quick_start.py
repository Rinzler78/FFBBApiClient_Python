import os
from typing import List

from ffbb_api_client import (
    Area,
    Category,
    Championship,
    ClubDetails,
    ClubInfos,
    FFBBApiClient,
    GeographycaleZone,
    League,
    Municipality,
    Sex,
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
commune: List[Municipality] = api_client.search_municipalities("Senas")[0]

# Get clubs from the commune
club_infos: ClubInfos = api_client.search_clubs(commune.id)[0]

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

senior_men_regional_div2_team: Team = next(
    (
        team
        for team in club_details.teams
        if team.category.value == Category.SENIOR.value
        and team.sex.value == Sex.MASCULIN.value
        and team.geographycale_zone.value == GeographycaleZone.REGIONAL.value
        and team.division_number == 2
    ),
    None,
)

# Get matches for the team
agenda_and_results = api_client.get_results(team_id=senior_men_regional_div2_team.id)

print("\nMatches for Sénas Senior Men Regional Division 2:")
for match in agenda_and_results.matchs or []:
    if not match.played:
        continue  # Skip unplayed matches
    # Determine if Sénas is home or away
    is_home = "senas" in (match.hometeam or "").lower()
    # Determine win/loss
    if is_home:
        win = match.score.home > match.score.visitor
    else:
        win = match.score.visitor > match.score.home
    emoji = "✅" if win else "❌"
    # Print match info
    date_str = match.date.strftime("%d/%m/%Y") if match.date else "-"
    location = match.hometeam if is_home else match.visitorteam
    print(
        f"{emoji} {date_str} | Location: {location} | Home: {match.hometeam} "
        f"| Away: {match.visitorteam} | Score: {match.score}"
    )
