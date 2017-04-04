from distutils.core import setup
import os

setup(
    name         = 'snippyt',
    version      = '0.0.1',
    author       = 'Daniel D. Zhang',
    author_email = 'dzhang.idf@gmail.com',
    license      = 'BSD-3',
    description  = 'A command line snippet management for modern developers.',
    url          = 'https://github.com/idf/snippyt',
    packages     = [
        'snippyt',
        'snippyt.templates',
    ],
    package_data = {
        'snippyt.templates': [f for f in os.listdir('snippyt/templates') if '.' not in f]
    },
    scripts          = ['snip'],
    install_requires = [
        'docopt >= 0.6.2',
        'Jinja2 >= 2.9.5',
        'MarkupSafe >= 1.0',
    ]
)