# Python XML-Microparser Module

![push main](https://github.com/clauspruefer/python-xml-microparser/actions/workflows/pylint.yaml/badge.svg)
[![PyPI version](https://badge.fury.io/py/xmlmicroparser.svg)](https://badge.fury.io/py/xmlmicroparser)

The Python **xmlmicroparser** module is a small OOP based XML Parser without DTD / XSLT / SAX functionality.

## 1. Documentation

Documentation including examples can be found at either ./doc or [https://pythondocs.webcodex.de/xml-microparser](https://pythondocs.webcodex.de/xml-microparser).

## 2. Installation

```bash
# install via pip
pip install xmlmicroparser
```

Or download the current Release Zip / Tarball @ [Release 1.0rc1](https://github.com/clauspruefer/python-xml-microparser/releases/tag/1.0rc1) and continue with section **2.2**.

>[!NOTE]
> Since Python 3.3 (PEP 405) Virtual Environments are proposed.

```bash
# setup virtual-env
python3 -m venv .xml-microparser

#activate virtual-env
source .xml-microparser/bin/activate

# upgrade pip
python3 -m pip install --upgrade pip

# install xmlmicroparser module
pip3 install xmlmicroparser
```

## 2.1. Dependencies

You need Python3 setuptools to build the package manually. Pytest / PEP-8 packages are required to run tests.

```bash
# install base dependencies
apt-get install python3-setuptools python3-pip python3-pytest python3-pytest-pep8
```

>[!IMPORTANT]
> The following section describes how to install the XML-Microparser package globally. Newer PIP Package Manager Versions prohibit
> this by default. It is possible to override by providing the `--break-system-packages` flag.

## 2.2. Non-Restrictive PIP Install

Do this for a pip system where `--break-system-packages` is not needed.

```bash
# install local pip
sudo pip3 install ./xmlmicroparser-1.0rc1.tar.gz
```

## 2.3. Restrictive PIP Install

Do this for a pip system where `--break-system-packages` is needed.

```bash
# install local pip
sudo pip3 install ./xmlmicroparser-1.0rc1.tar.gz --break-system-packages
```

## 3. Build Manually

Clone git repository and change dir inside.

```bash
# clone and cd into repo
git clone https://github.com/clauspruefer/python-xml-microparser.git
cd python-xml-microparser
```
## 3.1. Build As Non-Root-User

Build python-package with setup-tools (as non root user). This will generate the installable tarball
into `./dist/xmlmicroparser-1.0rc1.tar.gz`.

```bash
# build source distribution
python3 setup.py sdist
```

## 3.2. Install As Root-User

```bash
# install via pip
sudo pip3 install ./dist/xmlmicroparser-1.0rc1.tar.gz --break-system-packages
```

## 4. Run Tests / Pytest

```bash
# run pytest
pytest
```

## 5. Example Usage / Boost::Python

Using the XML-Microparser Module with Boost Python C++ https://www.boost.org/doc/libs/1_86_0/libs/python/doc/html/index.html
makes XML configuration handling in C++ projects easy.

See @ https://github.com/WEBcodeX1/http-1.2.

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
