==================================================================
sparkgeo_devops: Command Line Tools
==================================================================

A repository for common Sparkgeo continuous integration and continuous deployment tools.

Installation
------------

Instal via PyPi

::
    ]$ pip install sparkgeo_devtools

Usage
-----

Use the command line help messages for descriptions on how to use the functions.

::
    ]$ sparkgeo --help


    Development
    -----------

    **Contributing**

    Please contribute! Please make pull requests directly to master. Before making a pull request, please:

    * Ensure that all new functionality is covered by unit tests.
    * Verify that all unit tests are passing.
    * Ensure that all functionality is properly documented.t
    * Ensure that all functions/classes have proper docstrings so sphinx can autogenerate documentation.
    * Fix all versions in setup.py (and requirements.txt)

    **Run Tests**

    Tests use `pytest`_ framework

    .. _pytest: http://pytest.org/latest/contents.html

    ::

      py.test [...]
      python -m pytest [...]


    **Create a new version**

    To create a new version::

        bumpversion ( major | minor | patch )
        git push --tags

    Don't forget to update the changelog and upload to pypi.
