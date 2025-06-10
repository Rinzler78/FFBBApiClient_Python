from ..models.club_details import ClubDetails


def merge_club_details(
    club_details: ClubDetails, other_club_details: ClubDetails
) -> ClubDetails:
    """
    Merge two club details.

    Args:
        club_details (ClubDetails): The club details.
        other_club_details (ClubDetails): The other club details.

    Returns:
        ClubDetails: The merged club details.
    """
    if club_details == other_club_details:
        return club_details
    if club_details is None:
        return other_club_details
    if other_club_details is None:
        return club_details

    results = ClubDetails()

    if club_details.fields is not None and other_club_details.fields is not None:
        results.fields = set(club_details.fields + other_club_details.fields)
    elif club_details.fields is not None:
        results.fields = set(club_details.fields)
    elif other_club_details.fields is not None:
        results.fields = set(other_club_details.fields)
    else:
        results.fields = set()

    if club_details.infos is not None and other_club_details.infos is not None:
        results.infos = set(club_details.infos + other_club_details.infos)
    elif club_details.infos is not None:
        results.infos = set(club_details.infos)
    elif other_club_details.infos is not None:
        results.infos = set(other_club_details.infos)
    else:
        results.infos = set()

    if club_details.teams is not None and other_club_details.teams is not None:
        results.teams = set(club_details.teams + other_club_details.teams)
    elif club_details.teams is not None:
        results.teams = set(club_details.teams)
    elif other_club_details.teams is not None:
        results.teams = set(other_club_details.teams)
    else:
        results.teams = set()

    results.teams = sorted(
        results.teams,
        key=lambda team: team.name,
    )

    return results
