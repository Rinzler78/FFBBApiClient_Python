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

|

====================
ffbb_api_client
====================


    Allow to interact with FFBB apis


ffbb_api_client allow to interact with FFBB api.
You can retrieve information about clubs, teams, matches, etc...

Features
--------

- Search municipalities and clubs
- Retrieve detailed club information
- Fetch areas, leagues and championships
- Get match details, results and news


Installation
============

.. code-block:: bash

    pip install ffbb_api_client

Quick start
===========

.. code-block:: python

    import os
    from ffbb_api_client import FFBBApiClient

    # Load env from file if needed
    # from dotenv import load_dotenv
    # load_dotenv()

    # Retrieve api user / pass
    basic_auth_user = os.getenv("FFBB_BASIC_AUTH_USER")
    basic_auth_pass = os.getenv("FFBB_BASIC_AUTH_PASS")

    # Create an instance of the api client
    api_client = FFBBApiClient(
        basic_auth_user=basic_auth_user,
        basic_auth_pass=basic_auth_pass
    )

Examples
========

Take a look at quick_start.py to see how to use the library.

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.

Licence
=======

ffbb_api_client is distributed under the Apache 2.0 license.

Dev notes
=========

Command used to create this project:

.. code-block:: bash

    putup FFBBApiClient_Python -p ffbb_api_client -l Apache-2.0 -d "Allow to interact with FFBB apis" -u "https://github.com/Rinzler78/FFBBApiClient_Python" -v --github-actions --venv .venv
