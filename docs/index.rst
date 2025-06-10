====================
ffbb_api_client
====================

**ffbb_api_client** is a Python client library for interacting with the FFBB (French Basketball Federation) APIs.

Features
========

- **Complete API Coverage**: Access to clubs, teams, matches, competitions, and more
- **Type Safety**: Comprehensive type annotations for better development experience
- **Organized Structure**: Clean separation between models, helpers, and utilities
- **Error Handling**: Robust error handling with custom exception types
- **Caching Support**: Built-in HTTP caching for improved performance
- **Flexible Logging**: Configurable logging for debugging and monitoring

Quick Start
===========

.. code-block:: python

    from ffbb_api_client import FFBBApiClient, configure_logging
    import logging

    # Configure logging (optional)
    configure_logging(logging.INFO)

    # Create client
    client = FFBBApiClient(
        basic_auth_user="your_username",
        basic_auth_pass="your_password"
    )

    # Get areas
    areas = client.get_areas()

    # Search for clubs
    clubs = client.search_clubs(org_name="Paris")

    # Get match details
    match = client.get_match_detail(match_id=12345)


Contents
========

.. toctree::
   :maxdepth: 2

   Overview <readme>
   User Guide <user_guide>
   Package Architecture <architecture>
   License <license>
   Authors <authors>
   Changelog <changelog>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _references: https://www.sphinx-doc.org/en/stable/markup/inline.html
.. _Python domain syntax: https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
.. _Sphinx: https://www.sphinx-doc.org/
.. _Python: https://docs.python.org/
.. _Numpy: https://numpy.org/doc/stable
.. _SciPy: https://docs.scipy.org/doc/scipy/reference/
.. _matplotlib: https://matplotlib.org/contents.html#
.. _Pandas: https://pandas.pydata.org/pandas-docs/stable
.. _Scikit-Learn: https://scikit-learn.org/stable
.. _autodoc: https://www.sphinx-doc.org/en/master/ext/autodoc.html
.. _Google style: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
.. _NumPy style: https://numpydoc.readthedocs.io/en/latest/format.html
.. _classical style: https://www.sphinx-doc.org/en/master/domains.html#info-field-lists
