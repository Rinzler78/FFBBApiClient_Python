============
Testing Guide
============

This document explains how to run tests locally, mirroring the CI pipeline configuration.

Test Scripts Available
======================

1. Full CI-like Testing
------------------------

``run_tests.sh`` (Bash script)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    ./run_tests.sh

``run_tests.py`` (Python script - cross-platform)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    python run_tests.py

Both scripts execute the complete testing pipeline similar to GitHub Actions:

1. **Static Analysis**: Runs pre-commit hooks (if available)
2. **Package Build**: Builds wheel distribution using tox or pip build
3. **Test Execution**: Runs tests with proper coverage
4. **Coverage Report**: Generates HTML coverage report

2. Quick Testing
----------------

``quick_test.sh`` (Fast development testing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    ./quick_test.sh

Simplified script for rapid testing during development:

- Installs package in development mode
- Runs tests with verbose output
- Minimal setup for quick feedback

3. Manual Testing Commands
--------------------------

Using tox (recommended)
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Run all tests
    tox

    # Run tests with specific Python version
    tox -e py39

    # Clean and rebuild
    tox -e clean,build

Using pytest directly
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Install dependencies
    pip install -e .[testing]

    # Run all tests
    pytest

    # Run with coverage
    pytest --cov=ffbb_api_client --cov-report=html

    # Run specific test file
    pytest tests/test_get_videos.py -v

Environment Variables
=====================

For integration tests, set these environment variables:

.. code-block:: bash

    export FFBB_BASIC_AUTH_USER=your_username
    export FFBB_BASIC_AUTH_PASS=your_password

Without these, some integration tests may fail, but unit tests will still run.

Prerequisites
=============

Required
--------

- Python 3.9+ (as specified in setup.cfg)
- pip

Optional (for full CI experience)
----------------------------------

- tox: ``pip install tox``
- pre-commit: ``pip install pre-commit``
- coverage: ``pip install coverage``

CI Pipeline Mirroring
======================

The scripts are designed to mirror the GitHub Actions workflow in ``.github/workflows/ci.yml``:

+-----------------------+----------------------------------+
| CI Step               | Local Script Step               |
+=======================+==================================+
| Pre-commit checks     | Static analysis with pre-commit |
+-----------------------+----------------------------------+
| Build distribution    | Package build with tox/build    |
+-----------------------+----------------------------------+
| Test matrix           | Test execution with coverage    |
+-----------------------+----------------------------------+
| Coverage report       | HTML coverage generation        |
+-----------------------+----------------------------------+

Test Structure
==============

.. code-block:: text

    tests/
    ├── test_api_client_core.py      # Core API client tests
    ├── test_get_*.py                # API endpoint tests
    ├── test_dataclasses_*.py        # Data model tests
    ├── test_client_mocked.py        # Mocked integration tests
    └── test_*.py                    # Other unit tests

Troubleshooting
===============

Common Issues
-------------

1. **Import errors after refactoring**: Make sure to reinstall the package

   .. code-block:: bash

       pip install -e .

2. **Environment variable warnings**: Set FFBB credentials or ignore warnings for unit tests

3. **Pre-commit failures**: Install and configure pre-commit

   .. code-block:: bash

       pip install pre-commit
       pre-commit install

4. **Tox not found**: Install tox or use pytest directly

   .. code-block:: bash

       pip install tox

Debug Options
-------------

- Add ``-v`` to pytest for verbose output
- Use ``--tb=short`` for shorter tracebacks
- Add ``--lf`` to run only last failed tests
- Use ``--durations=10`` to see slowest tests

Integration with IDEs
=====================

Most IDEs can be configured to use these test commands:

- **VS Code**: Configure in ``.vscode/settings.json``
- **PyCharm**: Set up in Run/Debug configurations
- **vim/neovim**: Use with test runners like vim-test

Performance
===========

- **Quick tests**: ~10-30 seconds
- **Full CI pipeline**: ~2-5 minutes (depending on system)
- **Tox with multiple environments**: ~5-15 minutes
