# Python XML-Microparser Module

The **python-xml-microparser** module is a small OOP based XML Parser without DTD and SAX functionality.

## 1. Documentation

Documentation including examples can be found at either [./doc](./doc) or [https://pythondocs.webcodex.de/xml-microparser/](https://pythondocs.webcodex.de/xml-microparser/).

## 2. Installation

Most Linux Distributions come with already Python3 met dependencies (see **2.1**). Just download the Relase Tarball [link](link) and continue with section **2.2**.

## 2.1. Dependencies

You need the `pip3` Python3 Package Installer, Python3 Setuptools `python3-setuptools` and the downloaded XML-Microparser
Package found under Releases.

```bash
# apt-get install python3-setuptools python3-pip
```

>[!IMPORTANT]  
> The following section describes how to install the XML-Microparser package globally. Newer PIP Package Manager Versions forbid this.
> It is possible to override by providing the `--break-system-packages` flag.

## 2.2. Non-Restrictive PIP Install

Do this for a pip system where `--break-system-packages` is not needed.

```bash
# sudo pip3 install dist/xmlmicroparser-0.50b0.tar.gz
```

## 2.3. Restrictive PIP Install

Do this for a pip system where `--break-system-packages` is needed.

```bash
# sudo pip3 install dist/xmlmicroparser-0.50b0.tar.gz --break-system-packages
```

## 3. Boost Python

Using the XML-Microparser Module with Boost Python C++ https://www.boost.org/doc/libs/1_86_0/libs/python/doc/html/index.html 
makes XML configuration handling in C++ projects easy.

See @ https://github.com/WEBcodeX1/http-1.2/.