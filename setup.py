from setuptools import setup

setup(

    name = 'xmlmicroparser',
    version = '0.54beta',
    author = 'Claus Prüfer',
    author_email = 'pruefer@webcodex.de',
    maintainer = 'Claus Prüfer',
    description = 'A tiny xml parser without DTD/XSLT/SAX functionality.',
    license = 'GPLv3',
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
