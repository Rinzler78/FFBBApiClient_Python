.. image:: https://github.com/Rinzler78/FFBBApiClient_Python/actions/workflows/ci.yml/badge.svg?branch=main
    :alt: CI Status
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/actions/workflows/ci.yml
.. image:: https://readthedocs.org/projects/ffbbapiclient-python/badge/?version=latest
    :alt: Documentation Status
    :target: https://ffbbapiclient-python.readthedocs.io/en/latest/?badge=latest
.. image:: https://coveralls.io/repos/github/Rinzler78/FFBBApiClient_Python/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://coveralls.io/github/Rinzler78/FFBBApiClient_Python?branch=main
.. image:: https://img.shields.io/pypi/v/ffbb_api_client.svg
    :alt: PyPI Version
    :target: https://pypi.org/project/ffbb_api_client/
.. image:: https://img.shields.io/github/license/Rinzler78/FFBBApiClient_Python.svg
    :alt: License
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/blob/main/LICENSE.txt
.. image:: https://img.shields.io/pypi/pyversions/ffbb_api_client.svg
    :alt: Python Versions
    :target: https://pypi.org/project/ffbb_api_client/
.. image:: https://pepy.tech/badge/ffbb_api_client/month
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/ffbb_api_client
.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/
.. image:: https://img.shields.io/github/issues/Rinzler78/FFBBApiClient_Python
    :alt: Issues
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/issues
.. image:: https://img.shields.io/github/issues-pr/Rinzler78/FFBBApiClient_Python
    :alt: Pull Requests
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/pulls
.. image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
    :alt: Contributions welcome
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/issues
.. image:: https://img.shields.io/github/last-commit/Rinzler78/FFBBApiClient_Python
    :alt: Last Commit
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/commits/main
.. image:: https://img.shields.io/github/forks/Rinzler78/FFBBApiClient_Python?style=social
    :alt: Forks
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/fork
.. image:: https://img.shields.io/github/stars/Rinzler78/FFBBApiClient_Python?style=social
    :alt: Stars
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/stargazers
.. image:: https://img.shields.io/github/downloads/Rinzler78/FFBBApiClient_Python/total.svg
    :alt: GitHub All Releases
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/releases
.. image:: https://img.shields.io/github/v/tag/Rinzler78/FFBBApiClient_Python
    :alt: Latest Release
    :target: https://github.com/Rinzler78/FFBBApiClient_Python/releases

====================
ffbb_api_client
====================

A Python client to interact with FFBB APIs.

`ffbb_api_client` allows you to interact with the FFBB API.
You can retrieve information about clubs, teams, matches, and more.

Features
--------

- Search for municipalities and clubs
- Retrieve detailed club information
- Fetch areas, leagues, and championships
- Get match details, results, and news

Installation
============

.. code-block:: bash

    pip install ffbb_api_client

Quick start
===========

.. code-block:: python

    import os
    from ffbb_api_client import FFBBApiClient

    # Load environment variables from a file if needed
    # from dotenv import load_dotenv
    # load_dotenv()

    # Retrieve API user and password
    basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
    basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")

    # Create an instance of the API client
    api_client = FFBBApiClient(
        basic_auth_user=basic_auth_user,
        basic_auth_pass=basic_auth_pass
    )

Examples
========

See `quick_start.py` for usage examples.

Error handling
==============

Unexpected errors raised by callbacks executed through ``catch_result`` are
wrapped in :class:`ffbb_api_client.CatchResultError`.  This makes it possible to
distinguish network or decoding issues from other failures.

Note
====

This project was set up using PyScaffold 4.5. For details and usage
information on PyScaffold, see https://pyscaffold.org/.

License
=======

`ffbb_api_client` is distributed under the Apache 2.0 license.

Development notes
=================

Command used to create this project:

.. code-block:: bash

    putup FFBBApiClient_Python -p ffbb_api_client -l Apache-2.0 -d "Allow to interact with FFBB APIs" -u "https://github.com/Rinzler78/FFBBApiClient_Python" -v --github-actions --venv .venv
