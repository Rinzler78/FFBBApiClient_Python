import os
from typing import List

from ffbb_api_client.ffbb_api_client import FFBBApiClient
from ffbb_api_client.ffbb_api_client_types import (
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
commune: Commune = api_client.get_communes("Senas")[0]

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
results: AgendaAndResults = api_client.get_results(
    id=u13_team_D4_phase_2.id,
    sub_competition=u13_team_D4_phase_2.sub_competition,
    group=u13_team_D4_phase_2.group,
)
