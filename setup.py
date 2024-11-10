from setuptools import setup

setup(

    name = 'xmlmicroparser',
    author = 'Claus Prüfer',
    author_email = 'pruefer@webcodex.de',
    description = 'A tiny xml parser without DTD/XSLT/SAX functionality.',
    long_description = open('./README.md').read(),

    packages = [
        'xmlmicroparser'
    ],

    package_dir = {
        'xmlmicroparser': 'src/'
    },

    install_requires = [
    ],

    zip_safe = True

)
