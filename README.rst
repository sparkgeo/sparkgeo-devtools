==================================================================
sparkgeo_devops: Command Line Tools
==================================================================

A repository for common Sparkgeo continuous integration and continuous deployment tools.

Installation
------------

Instal via PyPi

.. code-block::

  pip install sparkgeo_devtools

Usage
-----

Use the command line help messages for descriptions on how to use the functions.

.. code-block::

  sparkgeo --help


Development
-----------

**Contributing**

Please contribute! Please make pull requests directly to master. Before making a pull request, please:

* Ensure that all new functionality is covered by unit tests (pytest).
* Verify that all unit tests are passing.
* Ensure that all functionality is properly documented. (Mkdocs will be added soon.)
* Ensure that all functions/classes have proper docstrings.
* Create Pull Request.

**Run Tests**

Tests use `pytest`_ framework

.. _pytest: http://pytest.org/latest/contents.html

.. code-block::

  py.test [...]
  python -m pytest [...]


**Create a new version**

To create a new version:

.. code-block::

  bumpversion ( major | minor | patch )
  git push --tags (may not be required, ie - SourceTree)

Don't forget to update the changelog and upload to pypi.
