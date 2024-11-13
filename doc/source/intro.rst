.. intro

=====
Intro
=====

A tiny Python XML Parser Module without DTD / XSLT / SAX functionality.

.. note::
    **NO** DTD / XSLT / SAX parsing, just plain XML supported.

Dependencies
============

On current Debian 12 / Ubuntu 22.04.3, 24.04.1 install the following packages:

.. code-block:: bash

    # install packages
    apt-get install python3-pip python3-sphinx python3-sphinx-rtd-theme

    # install pytest to run integration and unit tests
    apt-get install python3-pytest python3-pytest-pep8

How to run tests
================

To run all tests (unit and integration) after pip package installation do:

.. code-block:: bash

    # run pytest
    pytest

Documentation
=============

To build documentation (html, pdf):

.. code-block:: bash

    # build html documentation (found in doc/build/html/index.html)
    cd ./doc && make html

    # build html documentation (found in doc/build/latex/python-xml-microparser.pdf)
    cd ./doc && make latexpdf
