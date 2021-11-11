from setuptools import setup

setup(

    name = 'python-xml-microparser',
    version = '0.53beta',
    author = 'Claus Prüfer',
    author_email = 'pruefer@webcodex.de',
    maintainer = 'Claus Prüfer',
    description = 'A tiny, plain xml parser without XSLT/DTD capability.',
    url = 'http://python-xml-microparser.docs.webcodex.de',
    license = 'GPLv3',
    long_description = open('./README.rst').read(),

    packages = [
        'xml_microparser'
    ],

    package_dir = {
        'xml_microparser': 'src/'
    },

    zip_safe = True

)
