====================
Package Architecture
====================

This document describes the organization and structure of the ``ffbb_api_client`` package.

Overview
========

The ``ffbb_api_client`` package is organized into logical modules to provide a clean and maintainable codebase:

.. code-block:: text

    ffbb_api_client/
    ├── __init__.py          # Main package exports
    ├── ffbb_api_client.py   # Main API client class
    ├── helpers/             # Utility functions for data processing
    ├── models/              # Data classes for API responses
    └── utils/               # Core utilities (HTTP, logging, converters)

Main Components
===============

Main Client
-----------

:class:`ffbb_api_client.FFBBApiClient`
    The main API client class that provides methods to interact with the FFBB API.
    All API endpoints are accessible through this class.

Models Package
--------------

The ``models`` package contains data classes that represent API responses:

- **Club and Team Data**: :class:`~ffbb_api_client.models.ClubDetails`, :class:`~ffbb_api_client.models.Team`
- **Competition Data**: :class:`~ffbb_api_client.models.Competition`, :class:`~ffbb_api_client.models.Championship`
- **Match Data**: :class:`~ffbb_api_client.models.Match`, :class:`~ffbb_api_client.models.MatchDetail`
- **Geographic Data**: :class:`~ffbb_api_client.models.Area`, :class:`~ffbb_api_client.models.Municipality`

All model classes include:

- Type annotations for better IDE support
- Serialization/deserialization methods
- Data validation and conversion

Helpers Package
---------------

The ``helpers`` package provides utility functions for data processing:

:func:`ffbb_api_client.helpers.cached_session_helper.default_cached_session`
    Creates a default cached HTTP session for API requests.

:func:`ffbb_api_client.helpers.catch_result_helper.catch_result`
    Wrapper for handling API request errors gracefully.

:func:`ffbb_api_client.helpers.club_details_helper.merge_club_details`
    Merges multiple club detail objects.

:func:`ffbb_api_client.helpers.create_set_of_clubs`
    Creates unique sets of club objects.

:func:`ffbb_api_client.helpers.create_set_of_municipalities`
    Creates unique sets of municipality objects.

Utils Package
-------------

The ``utils`` package contains core utilities:

**HTTP Utilities** (``http_requests_utils``)
    - :func:`~ffbb_api_client.utils.http_get_json` - GET requests returning JSON
    - :func:`~ffbb_api_client.utils.http_post_json` - POST requests returning JSON
    - :func:`~ffbb_api_client.utils.encode_params` - URL parameter encoding
    - :func:`~ffbb_api_client.utils.url_with_params` - URL construction

**Data Converters** (``converters``)
    - Type conversion functions for API data
    - JSON serialization/deserialization helpers
    - Data validation utilities

**Logging** (``logger``)
    - :func:`~ffbb_api_client.utils.configure_logging` - Logging configuration
    - :data:`~ffbb_api_client.utils.logger` - Pre-configured logger instance

Public API
==========

All public APIs are available through direct imports from the main package:

.. code-block:: python

    from ffbb_api_client import (
        # Main client
        FFBBApiClient,

        # Model classes
        ClubDetails, Team, Competition, Match,

        # Utility functions
        configure_logging, catch_result,

        # Exception handling
        CatchResultError
    )

This design ensures:

- **Clean imports**: No need for deep package navigation
- **Backwards compatibility**: Existing code continues to work
- **Logical organization**: Related functionality is grouped together
- **Maintainability**: Clear separation of concerns

Usage Examples
==============

Basic Usage
-----------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, configure_logging
    import logging

    # Configure logging
    configure_logging(logging.INFO)

    # Create client
    client = FFBBApiClient(
        basic_auth_user="your_user",
        basic_auth_pass="your_pass"
    )

    # Use the API
    areas = client.get_areas()

Working with Models
-------------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, ClubDetails, Team

    client = FFBBApiClient(user="user", password="pass")

    # Get club details (returns ClubDetails object)
    club_details = client.get_club_details(club_id=12345)

    # Access typed data
    teams: List[Team] = club_details.teams
    for team in teams:
        print(f"Team: {team.name}")

Error Handling
--------------

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, CatchResultError, catch_result

    client = FFBBApiClient(user="user", password="pass")

    try:
        # Use catch_result for graceful error handling
        result = catch_result(lambda: client.get_areas())
        if result is not None:
            print(f"Found {len(result)} areas")
    except CatchResultError as e:
        print(f"API request failed: {e}")

Design Principles
=================

The package architecture follows these principles:

**Separation of Concerns**
    Each module has a specific responsibility:
    - Models handle data representation
    - Helpers provide business logic utilities
    - Utils provide low-level functionality
    - Main client orchestrates API interactions

**Explicit Imports**
    All imports are explicit rather than using wildcard imports, improving:
    - Code clarity and maintainability
    - IDE support and autocomplete
    - Performance (no unnecessary imports)

**Backwards Compatibility**
    The public API maintains compatibility with existing code while providing
    a clean, organized internal structure.

**Type Safety**
    Comprehensive type annotations throughout the codebase for better
    development experience and error prevention.

Migration Notes
===============

For users upgrading from previous versions:

**No Breaking Changes**
    All existing imports continue to work as before. The refactoring only
    affects internal organization.

**Recommended Updates**
    While not required, you may want to update imports for clarity:

    .. code-block:: python

        # Old style (still works)
        from ffbb_api_client.logger import configure_logging

        # New style (recommended)
        from ffbb_api_client import configure_logging

**New Features**
    The organized structure enables better IDE support and documentation
    generation without any code changes required.
