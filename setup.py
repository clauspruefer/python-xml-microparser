from setuptools import setup

setup(

    name = 'python-xml-microparser',
    version = '0.50beta',
    author = 'Claus Prüfer',
    author_email = 'pruefer@webcodex.de',
    maintainer = 'Claus Prüfer',
    description = 'A tiny plain xml parser without DTD capability.',
    homepage = 'http://xml-microparser.python.webcodex.de',
    license = 'GPLv3',
    long_description = open('./README.rst').read(),

    packages = [
        'xml-microparser'
    ],

    package_dir = {
        'xml-microparser': 'src/'
    },

    install_requires = [
        'pycopg2'
    ],

    zip_safe = True

)
