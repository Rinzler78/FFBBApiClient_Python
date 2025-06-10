import os
from typing import Optional

from appdirs import user_cache_dir
from requests_cache import CachedSession


def create_cache_key(request, path: Optional[str] = None, **kwargs):
    """Return a cache key based on request data and optional cache path."""

    url = request.url
    method = request.method
    data_hash = request.body if request.body else "empty"
    key = f"{method} {url} {data_hash}"
    if path:
        key = f"{key} {path}"
    return key


def default_cached_session(path: Optional[str] = None) -> CachedSession:
    """Return a default :class:`CachedSession` instance.

    Parameters
    ----------
    path: str, optional
        Directory where the cache file will be stored. When ``None`` (default),
        a user specific cache directory, provided by :func:`appdirs.user_cache_dir`,
        is used.
    """

    if path is None:
        cache_dir = user_cache_dir("ffbb_api_client")
        os.makedirs(cache_dir, exist_ok=True)
        path = os.path.join(cache_dir, "http_cache")

    return CachedSession(
        path,
        backend="sqlite",
        expire_after=1800,
        allowable_methods=("GET", "POST"),
        key_fn=lambda request, **kw: create_cache_key(request, path=path, **kw),
    )
