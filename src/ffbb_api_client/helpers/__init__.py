"""
Helper utilities for FFBB API Client data processing.

This module provides utility functions for common data processing tasks when working
with FFBB API responses. It includes helpers for:

- Session management and caching
- Error handling and retry logic
- Data merging and deduplication
- Club and municipality data processing

These helpers are designed to simplify common workflows and provide robust
error handling for API interactions.
"""

from .cached_session_helper import default_cached_session
from .catch_result_helper import CatchResultError, catch_result
from .club_details_helper import merge_club_details
from .clubs_infos_helper import create_set_of_clubs
from .municipalities_helper import create_set_of_municipalities

__all__ = [
    "default_cached_session",
    "CatchResultError",
    "catch_result",
    "merge_club_details",
    "create_set_of_clubs",
    "create_set_of_municipalities",
]
