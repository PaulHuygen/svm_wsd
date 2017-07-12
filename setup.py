#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='svn_wsd',
      version='0.1',
      description='Word-sence-Disambiguation module',
      author='Ruben Izquierdo',
      author_email='rubensanvi@gmail.com',
      url='https://github.com/cltl/svn_wsd',
      install_requires=['KafNafParserPy']
      )
