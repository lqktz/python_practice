# -*- coding: utf-8 -*-

try:
from setuptools import setup
except ImportError:
from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'qli3',
    'url': 'URL to get it at.',
    'version': '0.1',
    'scripts': [],
    'name': 'ex48'
}

setup(**config)

