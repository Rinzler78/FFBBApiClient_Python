"""Shared pytest configuration for the test suite."""

# def pytest_collection_modifyitems(config, items):
#     """Skip tests requiring network access.

#     All tests inheriting from :class:`tests.test_base.TestFFBBApiClient` make
#     real HTTP requests to the FFBB API. In the execution environment used for
#     automated checks those requests fail, resulting in failing tests. To ensure
#     the rest of the suite can run we automatically mark such tests to be
#     skipped.
#     """

#     try:
#         from tests.test_base import TestFFBBApiClient
#     except Exception:
#         return

#     network_modules_prefixes = (
#         "tests.test_get_",
#         "tests.test_search_",
#         "tests.test_api_client_core",
#     )

#     for item in items:
#         test_class = getattr(item, "cls", None)
#         if test_class and issubclass(test_class, TestFFBBApiClient):
#             item.add_marker(pytest.mark.skip(reason="network tests skipped"))
#             continue

#         module_name = getattr(item.module, "__name__", "")
#         if module_name.startswith(network_modules_prefixes):
#             item.add_marker(pytest.mark.skip(reason="network tests skipped"))
