.. intro

==========================
Intro / Module Description
==========================

A tiny Python XML Parser Module without DTD / XSLT / SAX functionality.

.. note::
    **NO** DTD / XSLT / SAX parsing, only plain (recursive) XML supported.

1. Dependencies
===============

On current Debian 12 / Ubuntu 22.04.3, 24.04.1 install the following packages.

.. code-block:: bash

    # install base packages
    apt-get install python3-pip python3-sphinx python3-sphinx-rtd-theme

    # install pytest for running unit and integration tests
    apt-get install python3-pytest python3-pytest-pep8

2. How to run tests
===================

To run all tests (unit and integration) after pip package installation do.

.. code-block:: bash

    # run pytest
    cd ./ && pytest

3. Documentation
================

To build documentation (html, pdf).

.. code-block:: bash

    # build html documentation (found in doc/build/html/index.html)
    cd ./doc && make html

    # build html documentation (found in doc/build/latex/python-xml-microparser.pdf)
    cd ./doc && make latexpdf
