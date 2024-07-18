from setuptools import setup

setup(

    name = 'xmlmicroparser',
    version = '0.50beta',
    author = 'Claus Prüfer',
    author_email = 'pruefer@webcodex.de',
    maintainer = 'Claus Prüfer',
    description = 'A tiny plain xml parser without DTD capability.',
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
