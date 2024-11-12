# Python XML-Microparser Module

The **python-xml-microparser** module is a small OOP based XML Parser without DTD / XSLT / SAX functionality.

## 1. Documentation

Documentation including examples can be found at either [./doc](./doc) or [https://pythondocs.webcodex.de/xml-microparser/](https://pythondocs.webcodex.de/xml-microparser/).

## 2. Installation

```bash
# pip install xmlmicroparser
```

Or download the current Relase Zip / Tarball @ [Release 0.54Beta](https://github.com/clauspruefer/python-xml-microparser/releases/tag/0.54beta) and continue with section **2.2**.

## 2.1. Dependencies

You need Python3 setuptools to build the package manually. Pytest / PEP-8 packages are required to run tests.

```bash
# apt-get install python3-setuptools python3-pip python3-pytest python3-pytest-pep8
```

>[!IMPORTANT]  
> The following section describes how to install the XML-Microparser package globally. Newer PIP Package Manager Versions forbid this.
> It is possible to override by providing the `--break-system-packages` flag.

## 2.2. Non-Restrictive PIP Install

Do this for a pip system where `--break-system-packages` is not needed.

```bash
# sudo pip3 install ./python-xml-microparser-0.54beta.tar.gz
```

## 2.3. Restrictive PIP Install

Do this for a pip system where `--break-system-packages` is needed.

```bash
# sudo pip3 install ./python-xml-microparser-0.54beta.tar.gz --break-system-packages
```

## 3. Build Manually

Clone git repository and change dir.

```bash
# git clone https://github.com/clauspruefer/python-xml-microparser.git
# cd python-xml-microparser

```
## 3.1. Build As Non-Root-User

Build python-package with setup-tools (as non root user). This will generate the installabe tarball
into `./dist/xmlmicroparser-0.55b0.tar.gz`.

```bash
# python3 setup.py sdist
```

## 3.2. Install As Root-User

```bash
# sudo pip3 install ./dist/xmlmicroparser-0.55b0.tar.gz --break-system-packages
```

## 4. Run Tests / Pytest

```bash
# pytest
```

## 5. Example Usage / Boost::Python

Using the XML-Microparser Module with Boost Python C++ https://www.boost.org/doc/libs/1_86_0/libs/python/doc/html/index.html 
makes XML configuration handling in C++ projects easy.

See @ https://github.com/WEBcodeX1/http-1.2/.
