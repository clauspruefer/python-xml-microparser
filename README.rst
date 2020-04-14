=====
Intro
=====

This Python 3 Module is built to parse XML input data to easy to use internal
python structs. As well a transformation from XML to JSON format is possible.

.. note::
    The module does **NOT** provide XSLT/DTD handling, just plain tag, attribute,
    value and recursive dependencies are part of this module.

Dependencies
============

On a ubuntu 18.04LTS system run the following to get everything working:

.. code-block:: bash

    # install pip3 (pip for python3)
    apt-get install python3-pip

    # install sphinx documentation system
    pip3 install sphinx

    # install read the docs theme
    pip3 install sphinx_rtd_theme

    # install pytest to run integration- and unit tests
    pip3 install -U pytest

    # install pytest html output module
    pip3 install pytest-html

How to run tests
================

To run all tests (unit and integration) run the following commands:

.. code-block:: bash

    # run all tests (cd to root path)
    export PYTHONPATH=./src && py.test --html=out.html

Documentation
=============

To build documentation (html, pdf):

.. code-block:: bash

    # build html documentation (found in doc/build/html/index.html)
    cd ./doc && make html

    # build html documentation (found in doc/build/latex/python-xml-microparser.pdf)
    cd ./doc && make latexpdf
