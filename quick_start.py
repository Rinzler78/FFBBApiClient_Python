import os
from typing import List

from ffbb_api_client import (
    Area,
    Championship,
    ClubDetails,
    ClubInfos,
    FFBBApiClient,
    League,
    Municipality,
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
