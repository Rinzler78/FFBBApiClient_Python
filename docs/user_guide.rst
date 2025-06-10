==========
User Guide
==========

This guide provides detailed examples and best practices for using ``ffbb_api_client``.

Installation
============

Install from PyPI:

.. code-block:: bash

    pip install ffbb_api_client

Configuration
=============

Environment Variables
---------------------

Set your API credentials as environment variables:

.. code-block:: bash

    export FFBB_BASIC_AUTH_USER="your_username"
    export FFBB_BASIC_AUTH_PASS="your_password"

Or create a ``.env`` file:

.. code-block:: text

    FFBB_BASIC_AUTH_USER=your_username
    FFBB_BASIC_AUTH_PASS=your_password

Basic Usage
===========

Creating a Client
-----------------

.. code-block:: python

    import os
    from ffbb_api_client import FFBBApiClient

    # From environment variables
    client = FFBBApiClient(
        basic_auth_user=os.getenv("FFBB_BASIC_AUTH_USER"),
        basic_auth_pass=os.getenv("FFBB_BASIC_AUTH_PASS")
    )

    # Or directly (not recommended for production)
    client = FFBBApiClient(
        basic_auth_user="your_username",
        basic_auth_pass="your_password"
    )

Configuring Logging
-------------------

.. code-block:: python

    import logging
    from ffbb_api_client import configure_logging

    # Enable INFO level logging
    configure_logging(logging.INFO)

    # Enable DEBUG level for detailed output
    configure_logging(logging.DEBUG)

Common Operations
================

Searching for Clubs
-------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient

    client = FFBBApiClient(user="user", password="pass")

    # Search by organization name
    clubs = client.search_clubs(org_name="Paris")

    # Search by municipality ID
    clubs = client.search_clubs(id_municipality=75001)

    # Process results
    for club in clubs:
        print(f"Club: {club.org_name} (ID: {club.id})")

Getting Club Details
-------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, ClubDetails

    client = FFBBApiClient(user="user", password="pass")

    # Get detailed information for a club
    club_details: ClubDetails = client.get_club_details(club_id=12345)

    # Access club information
    if club_details.teams:
        for team in club_details.teams:
            print(f"Team: {team.name}")

    if club_details.fields:
        for field in club_details.fields:
            print(f"Field: {field.name}")

Fetching Match Information
-------------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, MatchDetail

    client = FFBBApiClient(user="user", password="pass")

    # Get detailed match information
    match: MatchDetail = client.get_match_detail(match_id=12345)

    # Access match details
    print(f"Match: {match.home_team} vs {match.away_team}")
    print(f"Date: {match.date}")
    print(f"Score: {match.score}")

Working with Areas and Competitions
----------------------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient

    client = FFBBApiClient(user="user", password="pass")

    # Get all areas
    areas = client.get_areas()
    for area in areas:
        print(f"Area: {area.name} (ID: {area.id})")

    # Get competitions for a specific area
    competitions = client.get_area_competitions(area_id=1)
    for competition in competitions:
        print(f"Competition: {competition.name}")

Error Handling
==============

Basic Error Handling
--------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, CatchResultError, catch_result

    client = FFBBApiClient(user="user", password="pass")

    try:
        areas = client.get_areas()
        print(f"Found {len(areas)} areas")
    except CatchResultError as e:
        print(f"API request failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

Using catch_result Helper
------------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, catch_result

    client = FFBBApiClient(user="user", password="pass")

    # Graceful error handling with automatic retries
    result = catch_result(lambda: client.get_areas())
    if result is not None:
        print(f"Successfully retrieved {len(result)} areas")
    else:
        print("Failed to retrieve areas (returned None)")

Advanced Usage
==============

Custom HTTP Session
-------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, default_cached_session

    # Create a custom cached session
    custom_session = default_cached_session(path="/tmp/my_cache")

    # Use with the client
    client = FFBBApiClient(
        basic_auth_user="user",
        basic_auth_pass="pass",
        cached_session=custom_session
    )

Working with Multiple Clients
-----------------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient

    # Different environments or configurations
    prod_client = FFBBApiClient(
        basic_auth_user="prod_user",
        basic_auth_pass="prod_pass",
        api_url="https://api.prod.ffbb.com/"
    )

    test_client = FFBBApiClient(
        basic_auth_user="test_user",
        basic_auth_pass="test_pass",
        api_url="https://api.test.ffbb.com/",
        debug=True
    )

Data Processing Helpers
----------------------

.. code-block:: python

    from ffbb_api_client import (
        FFBBApiClient,
        merge_club_details,
        create_set_of_clubs,
        create_set_of_municipalities
    )

    client = FFBBApiClient(user="user", password="pass")

    # Get multiple club details and merge them
    details1 = client.get_club_details(club_id=123)
    details2 = client.get_club_details(club_id=456)
    merged = merge_club_details(details1, details2)

    # Remove duplicates from lists
    all_clubs = [club1, club2, club1]  # Contains duplicates
    unique_clubs = create_set_of_clubs(all_clubs)

    municipalities = [city1, city2, city1]  # Contains duplicates
    unique_cities = create_set_of_municipalities(municipalities)

Best Practices
==============

1. **Environment Variables**: Always use environment variables for credentials
2. **Error Handling**: Implement proper error handling for production code
3. **Logging**: Enable appropriate logging levels for debugging
4. **Caching**: Use the built-in caching for better performance
5. **Resource Cleanup**: Client connections are automatically managed

Performance Tips
===============

1. **Use Caching**: The default cached session improves performance for repeated requests
2. **Batch Operations**: When possible, batch multiple API calls
3. **Filter Early**: Use API filters to reduce data transfer
4. **Monitor Logs**: Use logging to identify slow operations

Troubleshooting
===============

Common Issues
-------------

**Authentication Errors**
    - Verify your credentials are correct
    - Check that environment variables are set
    - Ensure your account has API access

**Network Timeouts**
    - Check your internet connection
    - Try increasing timeout values
    - Use retry logic with ``catch_result``

**Import Errors**
    - Ensure ``ffbb_api_client`` is installed: ``pip install ffbb_api_client``
    - Check your Python environment
    - Verify all dependencies are installed

**Data Issues**
    - Some API endpoints may return None for missing data
    - Always check for None values before processing
    - Use the helper functions for data validation

Getting Help
============

- **Documentation**: https://ffbbapiclient-python.readthedocs.io/
- **Issues**: https://github.com/Rinzler78/FFBBApiClient_Python/issues
- **Source Code**: https://github.com/Rinzler78/FFBBApiClient_Python
