.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/FFBBApiClient-Python.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/FFBBApiClient-Python
    .. image:: https://readthedocs.org/projects/FFBBApiClient-Python/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://FFBBApiClient-Python.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/FFBBApiClient-Python/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/FFBBApiClient-Python

    .. image:: https://img.shields.io/conda/vn/conda-forge/FFBBApiClient-Python.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/FFBBApiClient-Python
    .. image:: https://pepy.tech/badge/FFBBApiClient-Python/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/FFBBApiClient-Python
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/FFBBApiClient-Python
.. image:: https://img.shields.io/pypi/v/ffbb_api_client.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/ffbb_api_client/

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
