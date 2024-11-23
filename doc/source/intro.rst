.. intro

==========================
Intro / Module Description
==========================

The **xmlmicroparser** Python Module provides basic XML Parser functionality without DTD /
XSLT / SAX features.

.. note::
    **No** "Document Type Definition", "Extensible Stylesheet Language Transformation" or
    "Simple API for XML", only **plain XML parsing** (recursive) supported.

1. Basic Install
================

.. code-block:: bash

    pip3 install xmlmicroparser

2. Dependencies
===============

Runs module independend.

3. Build Dependencies
=====================

On current Debian 12 / Ubuntu 22.04.3, 24.04.1 install the following additional packages (Documentation Rendering & Testing).

.. code-block:: bash

    # install base packages
    apt-get install python3-pip python3-sphinx python3-sphinx-rtd-theme

    # install pytest for running unit and integration tests
    apt-get install python3-pytest python3-pytest-pep8

4. Tests
========

To run all tests (unit and integration) after pip package installation.

.. code-block:: bash

    # run pytest
    cd ./ && pytest

5. Current Features
===================

- Basic XML Parsing (recursive)
- XML to JSON Transformation
- Extendable Transformation Classes

6. Planned Features
===================

- Multiple Transformation Types (e.g. YAML)
